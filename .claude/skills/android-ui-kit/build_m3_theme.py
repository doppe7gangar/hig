#!/usr/bin/env python3
"""A Material 3 colour scheme from one brand colour, derived the way Android does it.

Material doesn't pick colours one by one. It takes a seed, reads its hue
and chroma in HCT (Google's colour space: CAM16 hue and chroma, L* tone),
builds six tonal palettes from it, and assigns every role a tone from one
of them -- primary is tone 40 of the primary palette in light and 80 in
dark, surface is tone 98 of the neutral palette, and so on. A scheme
picked by eye drifts off that grid in ways that read as "not quite
Android": containers too saturated, surfaces too grey, dark mode that
isn't the same hue.

So this ports the parts of Google's material-color-utilities (Apache 2.0)
that the derivation needs -- CAM16, the HCT solver, tonal palettes -- and
maps the roles at the tones the Material 3 Design Kit uses. The kit's own
baseline is the check: seeded with #6750A4, this reproduces the kit's
scheme (verify_android_ui.py holds it to that).

    python3 build_m3_theme.py "#C1552E" -o theme.css
    python3 build_m3_theme.py "#C1552E" --format compose -o Color.kt
    python3 build_m3_theme.py "#C1552E" --secondary "#2E6BC1" -o theme.css

The seed is a seed, not the primary: a bright brand comes out darker at
tone 40, because white text has to read on it. That's what Material Theme
Builder and Android's dynamic colour do too.
"""

import argparse
import math
import re
import sys

# ------------------------------------------------------------------ sRGB, L*

SRGB_TO_XYZ = ((0.41233895, 0.35762064, 0.18051042),
               (0.2126, 0.7152, 0.0722),
               (0.01932141, 0.11916382, 0.95034478))
WHITE_D65 = (95.047, 100.0, 108.883)
M16 = ((0.401288, 0.650173, -0.051461),
       (-0.250268, 1.204414, 0.045854),
       (-0.002079, 0.048952, 0.953127))


def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", h):
        raise ValueError(f"not a hex colour: {h!r}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#%02X%02X%02X" % tuple(rgb)


def linearized(c8):
    """0-255 sRGB channel to linear, 0-100."""
    n = c8 / 255
    return (n / 12.92 if n <= 0.040449936 else ((n + 0.055) / 1.055) ** 2.4) * 100


def true_delinearized(c):
    n = c / 100
    return (n * 12.92 if n <= 0.0031308 else 1.055 * n ** (1 / 2.4) - 0.055) * 255


def delinearized(c):
    return max(0, min(255, round(true_delinearized(c))))


def _lab_f(t):
    return t ** (1 / 3) if t > 216 / 24389 else (24389 / 27 * t + 16) / 116


def _lab_invf(ft):
    ft3 = ft ** 3
    return ft3 if ft3 > 216 / 24389 else (116 * ft - 16) / (24389 / 27)


def y_from_lstar(lstar):
    return 100 * _lab_invf((lstar + 16) / 116)


def lstar_from_rgb(rgb):
    y = sum(SRGB_TO_XYZ[1][i] * linearized(rgb[i]) for i in range(3))
    return 116 * _lab_f(y / 100) - 16


def rgb_from_lstar(lstar):
    c = delinearized(y_from_lstar(lstar))
    return (c, c, c)


def _mul(m, v):
    return [sum(m[r][i] * v[i] for i in range(3)) for r in range(3)]


def _matmul(a, b):
    return [[sum(a[r][k] * b[k][c] for k in range(3)) for c in range(3)] for r in range(3)]


def _inverse(m):
    (a, b, c), (d, e, f), (g, h, i) = m
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    return [[(e * i - f * h) / det, (c * h - b * i) / det, (b * f - c * e) / det],
            [(f * g - d * i) / det, (a * i - c * g) / det, (c * d - a * f) / det],
            [(d * h - e * g) / det, (b * g - a * h) / det, (a * e - b * d) / det]]


# ------------------------------------------------------------------ CAM16

def _viewing_conditions():
    """CAM16's default viewing conditions, as material-color-utilities sets them."""
    adapting = 200 / math.pi * y_from_lstar(50) / 100
    surround = 2.0
    rw, gw, bw = _mul(M16, WHITE_D65)
    f = 0.8 + surround / 10
    c = (0.59 + (0.69 - 0.59) * (f - 0.9) * 10 if f >= 0.9
         else 0.525 + (0.59 - 0.525) * (f - 0.8) * 10)
    d = max(0.0, min(1.0, f * (1 - (1 / 3.6) * math.exp((-adapting - 42) / 92))))
    rgb_d = [d * (100 / w) + 1 - d for w in (rw, gw, bw)]
    k = 1 / (5 * adapting + 1)
    k4 = k ** 4
    fl = k4 * adapting + 0.1 * (1 - k4) ** 2 * (5 * adapting) ** (1 / 3)
    n = y_from_lstar(50) / WHITE_D65[1]
    z = 1.48 + math.sqrt(n)
    nbb = 0.725 / n ** 0.2
    af = [(fl * rgb_d[i] * w / 100) ** 0.42 for i, w in enumerate((rw, gw, bw))]
    ra = [400 * x / (x + 27.13) for x in af]
    aw = (2 * ra[0] + ra[1] + 0.05 * ra[2]) * nbb
    return dict(n=n, aw=aw, nbb=nbb, ncb=nbb, c=c, nc=f, rgb_d=rgb_d, fl=fl, z=z)


VC = _viewing_conditions()
# Linear RGB (0-100) straight to CAM16's discounted, scaled cone responses,
# and back: the two matrices the solver's inner loop runs on.
SCALED_DISCOUNT_FROM_LINRGB = _matmul(
    [[VC["fl"] * VC["rgb_d"][i] / 100 if i == j else 0 for j in range(3)] for i in range(3)],
    _matmul(M16, SRGB_TO_XYZ))
LINRGB_FROM_SCALED_DISCOUNT = _inverse(SCALED_DISCOUNT_FROM_LINRGB)
Y_FROM_LINRGB = SRGB_TO_XYZ[1]
CRITICAL_PLANES = [linearized(i + 0.5) for i in range(255)]


def _adapt(c):
    af = abs(c) ** 0.42
    return math.copysign(400 * af / (af + 27.13), c) if c else 0.0


def _unadapt(a):
    base = max(0.0, 27.13 * abs(a) / (400 - abs(a)))
    return math.copysign(base ** (1 / 0.42), a) if a else 0.0


def hct(rgb):
    """(hue, chroma, tone) of an sRGB colour."""
    sd = _mul(SCALED_DISCOUNT_FROM_LINRGB, [linearized(c) for c in rgb])
    ra, ga, ba = (_adapt(c) for c in sd)
    a = (11 * ra - 12 * ga + ba) / 11
    b = (ra + ga - 2 * ba) / 9
    u = (20 * ra + 20 * ga + 21 * ba) / 20
    p2 = (40 * ra + 20 * ga + ba) / 20
    hue = math.degrees(math.atan2(b, a)) % 360
    j = 100 * (p2 * VC["nbb"] / VC["aw"]) ** (VC["c"] * VC["z"])
    e_hue = 0.25 * (math.cos(math.radians(hue) + 2) + 3.8)
    p1 = 50000 / 13 * e_hue * VC["nc"] * VC["ncb"]
    t = p1 * math.hypot(a, b) / (u + 0.305)
    alpha = t ** 0.9 * (1.64 - 0.29 ** VC["n"]) ** 0.73
    return hue, alpha * math.sqrt(j / 100), lstar_from_rgb(rgb)


# ------------------------------------------------------------- HCT solver

def _sanitize_radians(x):
    return (x + math.pi * 8) % (math.pi * 2)


def _hue_of(linrgb):
    sd = _mul(SCALED_DISCOUNT_FROM_LINRGB, linrgb)
    ra, ga, ba = (_adapt(c) for c in sd)
    return math.atan2((ra + ga - 2 * ba) / 9, (11 * ra - 12 * ga + ba) / 11)


def _cyclic(a, b, c):
    return _sanitize_radians(b - a) < _sanitize_radians(c - a)


def _set_coordinate(src, coord, dst, axis):
    t = (coord - src[axis]) / (dst[axis] - src[axis])
    return [src[i] + (dst[i] - src[i]) * t for i in range(3)]


def _nth_vertex(y, n):
    kr, kg, kb = Y_FROM_LINRGB
    ca = 0.0 if n % 4 <= 1 else 100.0
    cb = 0.0 if n % 2 == 0 else 100.0
    if n < 4:
        g, b = ca, cb
        r = (y - g * kg - b * kb) / kr
        return [r, g, b] if 0 <= r <= 100 else None
    if n < 8:
        b, r = ca, cb
        g = (y - r * kr - b * kb) / kg
        return [r, g, b] if 0 <= g <= 100 else None
    r, g = ca, cb
    b = (y - r * kr - g * kg) / kb
    return [r, g, b] if 0 <= b <= 100 else None


def _bisect_to_segment(y, target):
    left = right = None
    left_hue = right_hue = 0.0
    uncut = True
    for n in range(12):
        mid = _nth_vertex(y, n)
        if mid is None:
            continue
        mid_hue = _hue_of(mid)
        if left is None:
            left = right = mid
            left_hue = right_hue = mid_hue
            continue
        if uncut or _cyclic(left_hue, mid_hue, right_hue):
            uncut = False
            if _cyclic(left_hue, target, mid_hue):
                right, right_hue = mid, mid_hue
            else:
                left, left_hue = mid, mid_hue
    return left, right


def _bisect_to_limit(y, target):
    left, right = _bisect_to_segment(y, target)
    left_hue = _hue_of(left)
    for axis in range(3):
        if left[axis] == right[axis]:
            continue
        if left[axis] < right[axis]:
            lp = math.floor(true_delinearized(left[axis]) - 0.5)
            rp = math.ceil(true_delinearized(right[axis]) - 0.5)
        else:
            lp = math.ceil(true_delinearized(left[axis]) - 0.5)
            rp = math.floor(true_delinearized(right[axis]) - 0.5)
        for _ in range(8):
            if abs(rp - lp) <= 1:
                break
            mp = (lp + rp) // 2
            mid = _set_coordinate(left, CRITICAL_PLANES[mp], right, axis)
            mid_hue = _hue_of(mid)
            if _cyclic(left_hue, target, mid_hue):
                right, rp = mid, mp
            else:
                left, left_hue, lp = mid, mid_hue, mp
    return [(left[i] + right[i]) / 2 for i in range(3)]


def _find_by_j(hue_rad, chroma, y):
    j = math.sqrt(y) * 11
    t_inner = 1 / (1.64 - 0.29 ** VC["n"]) ** 0.73
    e_hue = 0.25 * (math.cos(hue_rad + 2) + 3.8)
    p1 = e_hue * 50000 / 13 * VC["nc"] * VC["ncb"]
    hs, hc = math.sin(hue_rad), math.cos(hue_rad)
    for rnd in range(5):
        jn = j / 100
        alpha = 0.0 if chroma == 0 or j == 0 else chroma / math.sqrt(jn)
        t = (alpha * t_inner) ** (1 / 0.9)
        p2 = VC["aw"] * jn ** (1 / VC["c"] / VC["z"]) / VC["nbb"]
        gamma = 23 * (p2 + 0.305) * t / (23 * p1 + 11 * t * hc + 108 * t * hs)
        a, b = gamma * hc, gamma * hs
        ra = (460 * p2 + 451 * a + 288 * b) / 1403
        ga = (460 * p2 - 891 * a - 261 * b) / 1403
        ba = (460 * p2 - 220 * a - 6300 * b) / 1403
        lin = _mul(LINRGB_FROM_SCALED_DISCOUNT, [_unadapt(ra), _unadapt(ga), _unadapt(ba)])
        if min(lin) < 0:
            return None
        fnj = sum(Y_FROM_LINRGB[i] * lin[i] for i in range(3))
        if fnj <= 0:
            return None
        if rnd == 4 or abs(fnj - y) < 0.002:
            if max(lin) > 100.01:
                return None
            return tuple(delinearized(c) for c in lin)
        j -= (fnj - y) * j / (2 * fnj)
    return None


def solve(hue, chroma, tone):
    """The sRGB colour at an HCT hue, chroma and tone -- or, when that
    chroma is out of gamut at that tone, the most chromatic one there is."""
    if chroma < 0.0001 or tone < 0.0001 or tone > 99.9999:
        return rgb_from_lstar(tone)
    hue_rad = math.radians(hue % 360)
    y = y_from_lstar(tone)
    exact = _find_by_j(hue_rad, chroma, y)
    if exact:
        return exact
    return tuple(delinearized(c) for c in _bisect_to_limit(y, hue_rad))


# ------------------------------------------------------------- the scheme

# Role -> (palette, light tone, dark tone), at the tones the Material 3
# Design Kit's baseline scheme sits on.
ROLES = [
    ("primary", "primary", 40, 80), ("on-primary", "primary", 100, 20),
    ("primary-container", "primary", 90, 30), ("on-primary-container", "primary", 30, 90),
    ("secondary", "secondary", 40, 80), ("on-secondary", "secondary", 100, 20),
    ("secondary-container", "secondary", 90, 30), ("on-secondary-container", "secondary", 30, 90),
    ("tertiary", "tertiary", 40, 80), ("on-tertiary", "tertiary", 100, 20),
    ("tertiary-container", "tertiary", 90, 30), ("on-tertiary-container", "tertiary", 30, 90),
    ("surface", "neutral", 98, 6), ("surface-dim", "neutral", 87, 6), ("surface-bright", "neutral", 98, 24),
    ("surface-container-lowest", "neutral", 100, 4), ("surface-container-low", "neutral", 96, 10),
    ("surface-container", "neutral", 94, 12), ("surface-container-high", "neutral", 92, 17),
    ("surface-container-highest", "neutral", 90, 22),
    ("on-surface", "neutral", 10, 90), ("on-surface-variant", "neutral-variant", 30, 80),
    ("outline", "neutral-variant", 50, 60), ("outline-variant", "neutral-variant", 80, 30),
    ("inverse-surface", "neutral", 20, 90), ("inverse-on-surface", "neutral", 95, 20),
    ("inverse-primary", "primary", 80, 40),
]
# Error doesn't follow the seed; these are the kit's, in both appearances.
ERROR = {
    "light": {"error": "#B3261E", "on-error": "#FFFFFF", "error-container": "#F9DEDC", "on-error-container": "#852221"},
    "dark": {"error": "#F2B8B5", "on-error": "#601410", "error-container": "#8C1D18", "on-error-container": "#F9DEDC"},
}
ORDER = [r[0] for r in ROLES[:12]] + list(ERROR["light"]) + [r[0] for r in ROLES[12:]] + ["scrim", "shadow"]


def palettes(seed, secondary=None, tertiary=None):
    """The kit's palettes: primary at the seed's hue with chroma of at
    least 48, secondary 16, tertiary 60 degrees round at 24, neutrals at
    6 and 8. A given secondary or tertiary colour supplies its own hue
    and chroma instead."""
    h, c, _ = hct(hex_to_rgb(seed))
    out = {"primary": (h, max(48.0, c)), "secondary": (h, 16.0),
           "tertiary": ((h + 60) % 360, 24.0), "neutral": (h, 6.0), "neutral-variant": (h, 8.0)}
    for role, given in (("secondary", secondary), ("tertiary", tertiary)):
        if given:
            gh, gc, _ = hct(hex_to_rgb(given))
            out[role] = (gh, gc)
    return out


def scheme(seed, secondary=None, tertiary=None):
    """{"light": {role: hex}, "dark": {role: hex}}."""
    pal = palettes(seed, secondary, tertiary)
    out = {}
    for mode, col in (("light", 2), ("dark", 3)):
        roles = {}
        for row in ROLES:
            h, c = pal[row[1]]
            roles[row[0]] = rgb_to_hex(solve(h, c, row[col]))
        roles.update(ERROR[mode])
        roles["scrim"] = roles["shadow"] = "#000000"
        out[mode] = {k: roles[k] for k in ORDER}
    return out


def contrast(a, b):
    def lum(h):
        def ch(c):
            c /= 255
            return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
        r, g, b_ = hex_to_rgb(h)
        return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b_)
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


# Text roles and what they sit on: each needs 4.5:1.
PAIRS = [("on-primary", "primary"), ("on-primary-container", "primary-container"),
         ("on-secondary-container", "secondary-container"), ("on-tertiary-container", "tertiary-container"),
         ("on-surface", "surface"), ("on-surface-variant", "surface-container-highest"),
         ("primary", "surface"), ("inverse-on-surface", "inverse-surface")]


def notes(sch):
    out = []
    for mode in ("light", "dark"):
        for fg, bg in PAIRS:
            r = contrast(sch[mode][fg], sch[mode][bg])
            if r < 4.5:
                out.append(f"{mode}: {fg} on {bg} is {r:.2f}:1, under 4.5")
    return out


# ---------------------------------------------------------------- output

def to_css(sch, seed, extra=""):
    def block(mode, indent):
        return "\n".join(f"{indent}--md-sys-color-{k}: {v};" for k, v in sch[mode].items())
    return f"""/* Material 3 scheme from {seed.upper()}{extra}, generated by build_m3_theme.py.
   Regenerate rather than edit: every role is a tone of a palette, and a
   hand-tuned value stops matching its dark twin. Link it after
   material-components.css so these win. */

:root {{
{block("light", "  ")}
}}

@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
{block("dark", "    ")}
  }}
}}

:root[data-theme="dark"] {{
{block("dark", "  ")}
}}
"""


def _camel(role):
    return "".join(p.capitalize() if i else p for i, p in enumerate(role.split("-")))


def to_compose(sch, seed, package="com.example.ui.theme"):
    lines = [f"package {package}", "", "import androidx.compose.material3.darkColorScheme",
             "import androidx.compose.material3.lightColorScheme", "import androidx.compose.ui.graphics.Color", "",
             f"// Material 3 scheme from {seed.upper()}, generated by build_m3_theme.py.", ""]
    for mode in ("light", "dark"):
        for k, v in sch[mode].items():
            lines.append(f"val {_camel(k)}{mode.capitalize()} = Color(0xFF{v[1:]})")
        lines.append("")
    for mode in ("light", "dark"):
        lines.append(f"val {mode.capitalize()}Colors = {mode}ColorScheme(")
        lines += [f"    {_camel(k)} = {_camel(k)}{mode.capitalize()}," for k in sch[mode]]
        lines += [")", ""]
    return "\n".join(lines)


def to_xml(sch, seed):
    lines = ['<?xml version="1.0" encoding="utf-8"?>',
             f"<!-- Material 3 scheme from {seed.upper()}, generated by build_m3_theme.py. -->", "<resources>"]
    for mode in ("light", "dark"):
        lines += [f'    <color name="md_theme_{_camel(k)}_{mode}">#FF{v[1:]}</color>' for k, v in sch[mode].items()]
    return "\n".join(lines + ["</resources>", ""])


FORMATS = {"css": to_css, "compose": to_compose, "xml": to_xml}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("seed", help='brand colour, e.g. "#C1552E"')
    ap.add_argument("--secondary", help="a second brand colour for the secondary palette")
    ap.add_argument("--tertiary", help="a third brand colour for the tertiary palette")
    ap.add_argument("--format", choices=sorted(FORMATS), default="css")
    ap.add_argument("-o", "--out", help="write here instead of stdout")
    a = ap.parse_args()
    try:
        sch = scheme(a.seed, a.secondary, a.tertiary)
    except ValueError as e:
        sys.exit(str(e))
    text = FORMATS[a.format](sch, a.seed)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"wrote {a.out}: {len(sch['light'])} roles, light and dark, from {a.seed.upper()}")
    else:
        sys.stdout.write(text)
    for n in notes(sch):
        print("contrast: " + n, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
