# Copyright and third-party resource policy

This project is an independent design and engineering toolkit. It is not affiliated with, sponsored by, or endorsed by Apple or Google.

## What may be contributed

- Original code, documentation, tests, design components, and independently authored explanations which the contributor has the right to license under Apache-2.0.
- Factual measurements, API identifiers, and hyperlinks to official platform documentation, accompanied by source/provenance information where appropriate.
- Third-party assets **only** when their licence permits the actual proposed redistribution and use, with complete attribution and licence documentation.

## What must not be committed without documented permission

- Copies or substantial transcriptions of Apple Human Interface Guidelines pages, Apple's official UI kits, screenshots extracted from design resources, or Apple documentation summaries copied verbatim.
- SF Pro, SF Symbols artwork, or other proprietary fonts/icons provided under terms that prohibit republication in this repository.
- Files obtained by scraping or downloading a third-party website when the relevant licence or terms do not authorise their distribution.
- Images embedded as base64, or renamed binary assets intended to bypass the provenance checks.
- Generated artefacts that contain third-party artwork which cannot lawfully be redistributed.

Public availability is not permission to redistribute. Attribution by itself does not confer a licence. Rewording a source does not automatically eliminate copyright concerns.

## Required review for external content

Before adding any third-party material, document:
1. **Origin:** official source URL, creator, and version/date accessed.
2. **Rights:** exact licence or written permission and any relevant restrictions.
3. **Use:** how the repository and generated outputs will reproduce, adapt, or distribute the material.
4. **Notices:** required licence text, copyright notices, and attribution.
5. **Alternatives:** whether an official link or locally user-obtained reference can serve the same purpose without repository redistribution.

Update `NOTICE` as applicable. If permissions are uncertain, do not add the asset until reviewed.

## Apple references

Prefer links to https://developer.apple.com/design/human-interface-guidelines/ and https://developer.apple.com/design/resources/. Guidance should be expressed independently and linked to the relevant source. Do not bundle an offline mirror, screenshots from official kits, or other original protected materials without specific rights to do so. User-local retrieval is not automatically authorised: comply with the applicable Apple terms and access restrictions.

## Automated checks and their limits

Run `python3 scripts/provenance_guard.py` before opening a pull request. The optional `--corpus` mode can detect some exact HIG text matches **when a separately obtained authorised local reference is available**. CI does not possess this corpus and therefore does not perform that comparison. Passing the guard proves neither authorship nor licence compliance: human review is still required.

## Reports and takedown requests

For a suspected infringement, open a repository issue without attaching or reposting disputed material, or contact the maintainer privately through the repository's available contact information. Maintainers should promptly investigate and, where warranted, remove the material.

This document is a project policy, not legal advice.
