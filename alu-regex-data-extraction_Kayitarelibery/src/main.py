import re
import json

EMAIL_PATTERN = r"(?<![\w.+-])[\w+-]+(?:\.[\w+-]+)*@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}(?![\w.-])"

ALU_DOMAINS = (
    "@alueducation.com",
    "@alumni.alueducation.com",
    "@si.alueducation.com"
)

PHONE_PATTERN = r"(?:\+250[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{3}|\(\d{3}\)[\s-]?\d{3}-\d{4})"

URL_PATTERN = r"https?://(?:www\.)?[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+(?:/[^\s]*)?"

CREDIT_CARD_PATTERN = r"(?<![\d-])(?:\d{4}-\d{4}-\d{4}-\d{4}|\d{4} \d{4} \d{4} \d{4})(?![\d-])"

def mask_card(card):
    digits = card.replace("-", "").replace(" ", "")
    return "*" * (len(digits) - 4) + digits[-4:]

SUSPICIOUS_PATTERNS = [
    r"<script.*?>.*?</script>",
    r"(?i)drop\s+table",
    r"[\x00-\x08\x0b\x0c\x0e-\x1f]",
]

def scan_for_threats(text):
    threats_found = []
    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, text):
            threats_found.append(pattern)
    return threats_found

with open("input/raw-text.txt", "r", encoding="utf-8") as file:
    text = file.read()

threats = scan_for_threats(text)
if threats:
    print(f"\nWarning: {len(threats)} suspicious pattern(s) detected in input.")

emails = re.findall(EMAIL_PATTERN, text)

alu_emails = [
    email for email in emails
    if email.endswith(ALU_DOMAINS)
]

phone_numbers = re.findall(PHONE_PATTERN, text)

urls = re.findall(URL_PATTERN, text)

credit_cards = re.findall(CREDIT_CARD_PATTERN, text)

valid_credit_cards = [
    card for card in credit_cards
    if card.replace("-", "").replace(" ", "") != "0000000000000000"
]

print("All emails:")
for email in emails:
    print(email)

print("\nALU emails:")
for email in alu_emails:
    print(email)

print("\nPhone numbers:")
for phone in phone_numbers:
    print(phone)

print("\nURLs:")
for url in urls:
    print(url)

print("\nCredit cards:")
for card in valid_credit_cards:
    print(mask_card(card))

results = {
    "emails": emails,
    "alu_emails": alu_emails,
    "phone_numbers": phone_numbers,
    "urls": urls,
    "credit_cards": [mask_card(card) for card in valid_credit_cards],
    "threats_detected": len(threats)
}

with open("output/sample-output.json", "w", encoding="utf-8") as outfile:
    json.dump(results, outfile, indent=2)

print("\nResults written to output/sample-output.json")    