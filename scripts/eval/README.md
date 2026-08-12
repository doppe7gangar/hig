# Measuring whether these skills actually get used

A reference skill can be perfectly written and still be worthless, because
skills are *pull*-based: Claude decides whether to consult one. This corpus
is an unusually hard case for that decision, since it competes with what the
model already believes it knows about Apple's guidelines. Content quality and
"does it get consulted" are independent questions, and only the second one
determines whether any of this pays off.

```
python3 scripts/eval/test_skill_triggering.py
```

Installs every `apple-hig*` skill into a throwaway project, runs `claude -p`
against realistic queries, and reports which skill was invoked. Cases include
Apple-adjacent near-misses (Xcode code signing, Core Data migrations) because
a skill that fires on those is interrupting work it can't help with.

## Two traps that produced confidently wrong numbers

Both of these were hit while building this, and both produced a clean,
plausible, entirely fictional result. They're recorded here because the
failure mode is silent — you get a number, and the number looks fine.

**1. Measuring a stub instead of the skill.** The `skill-creator`
description optimizer (`scripts/run_loop.py`) does not install the skill it
is optimizing. It writes a stub *command* into `.claude/commands/`
containing only the description text under a generated name like
`apple-hig-skill-698268f4`, then measures whether Claude invokes that. For a
skill whose value is its instructions, that's a fair proxy. For a 178-page
reference corpus it is not: the thing being offered contains nothing worth
opening, and the name doesn't look like the skill. It reported 0–11% recall.
Testing the real installed skill on the same queries gave 100%. Its own
four-iteration winner was the original description, which is the tell — when
every candidate scores the same, the instrument isn't discriminating.

**2. Folding timeouts into "didn't trigger".** A harness that returns
false-y on `TimeoutExpired` cannot distinguish "Claude declined to consult
the skill" from "the run didn't finish". This matters because the branch
that *does* consult the skill does strictly more work, so it is the branch
that times out — the artifact points the same direction as the hypothesis,
which is the worst case for noticing it. A 240s limit with 5 parallel
workers produced a clean 100% → 0% result that was entirely timeouts. The
harness here reports `TIMEOUT` and `ERROR` as distinct outcomes and defaults
to 600s.

The general lesson: when a triggering measurement disagrees with a
hands-on check, suspect the harness before rewriting the skill. Confirm what
the harness installs, and confirm that a non-trigger is a real decision
rather than a process that died.

## Interpreting results

Ambiguity is expected and mostly fine. A macOS question landing on
`apple-hig` rather than `apple-hig-macos` still gets a correct answer from
the full corpus — it just misses the concentrated platform notes. The
failure worth acting on is the reverse: a platform skill winning a
cross-platform question, since those skills deliberately carry only the
platform deltas and answering from deltas alone is confidently incomplete.
Each platform `SKILL.md` warns about exactly this.
