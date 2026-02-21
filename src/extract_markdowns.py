import re


def extract_markdown_links(text):
    # This matches [anchor text](url) 
    # and specifically ignores patterns starting with !
    return re.findall(r"(?<!\!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_images(text):
    # This matches ![alt text](url)
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

