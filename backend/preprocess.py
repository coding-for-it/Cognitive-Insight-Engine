import re

def clean_text(raw):
    # Replace multiple newlines with one newline
    cleaned = re.sub(r'\n+', '\n', raw)
    return cleaned

def extract_sections(text):
    sections = {}
    # Simple section keywords - adjust as needed
    section_keywords = ['financial', 'discussion', 'overview', 'risk', 'ceo', 'management']

    for keyword in section_keywords:
        pattern = re.compile(rf"(?i)(.*{keyword}.*)", re.MULTILINE)
        matches = pattern.findall(text)
        if matches:
            sections[keyword] = matches
    return sections
