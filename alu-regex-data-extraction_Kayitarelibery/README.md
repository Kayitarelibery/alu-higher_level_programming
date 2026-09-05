# Regex Data Extraction & Validation
**Author:** [Kayitare Anakin Libery]

## Overview
This program extracts and validates structured data (emails, phone numbers, URLs,
and credit card numbers) from a raw text file using regular expressions. It also
demonstrates basic security awareness by detecting suspicious/injection-like input
and masking sensitive data before output.

## How to Run
1. Make sure Python 3 is installed.
2. Place your input text in `input/raw-text.txt`.
3. From the project root, run:
4. Console output will show extracted data. Full results are saved to
   `output/sample-output.json`.

## Data Types Extracted
- **Emails** — general email format, plus a second validation step that classifies
  emails ending in `@alueducation.com`, `@alumni.alueducation.com`, or
  `@si.alueducation.com` as ALU-affiliated.
- **Phone numbers** — handles Rwandan international format (`+250 xxx xxx xxx`)
  and US-style parenthesized format (`(xxx) xxx-xxxx`).
- **URLs** — matches both `http` and `https`, with or without `www`, including
  query strings.
- **Credit card numbers** — matches 16-digit numbers separated by hyphens or
  spaces. Obviously fake/test numbers (all zeros) are filtered out.

## Security Considerations
- Extracted credit card numbers are **masked** before being printed or written to
  output — only the last 4 digits are shown (e.g. `************4444`).
- The raw input text is scanned for suspicious patterns (script tags, SQL
  injection-style strings, control/null bytes) before extraction. If any are
  found, a warning is printed, signaling that the input should not be
  automatically trusted.
- Lookaround assertions in the email and credit card regex patterns prevent
  partial/malformed matches (e.g. `not-an-email@@@fake..com` is correctly
  rejected rather than partially matched).

## Known Limitations
- Phone number matching currently supports Rwandan (+250) and US-style formats
  only; other international formats are not covered.
- Credit card validation checks format only, not checksum validity (e.g. no
  Luhn algorithm check).