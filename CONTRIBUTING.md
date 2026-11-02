# Contributing

Thank you for improving hig. Please submit small, focused changes with tests.

## Before a pull request

1. Confirm you created each contribution or have permission to license it for distribution under the project's Apache-2.0 licence. Retain any applicable third-party notices.
2. Read [COPYRIGHT_POLICY.md](COPYRIGHT_POLICY.md) before adding screenshots, fonts, icons, scraped documentation, copied prose or AI-generated material.
3. Update [NOTICE](NOTICE) when the licence inventory or provenance changes.
4. Run `python3 scripts/provenance_guard.py` and `python3 scripts/doctor.py --fast`. Run relevant platform/design tests described in [TESTING.md](TESTING.md) for implementation changes.
5. Explain which platforms and interaction states you tested, and link supporting official design/API documentation as applicable.

## Pull request checklist

- [ ] The change contains no unlicensed third-party content, including generated output or embedded assets.
- [ ] New dependencies and external assets have documented licences and approved redistribution uses.
- [ ] User-visible examples, templates and screenshots have been inspected for protected artwork.
- [ ] Relevant automated checks passed; limitations or skipped tests are stated.
- [ ] Changes to external measurements or platform guidance are linked to dated source material.
- [ ] This contribution can be distributed under Apache-2.0, except specifically identified third-party components under compatible terms.

## Review

Passing CI is necessary but not sufficient for accepting content with third-party rights implications. Maintainers may request evidence of origin or a simpler implementation that links to official resources instead of republishing them. Do not add Apple proprietary assets or mirrors of its HIG content merely because they are publicly downloadable.
