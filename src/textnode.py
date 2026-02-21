from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"  
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text and 
            self.text_type == other.text_type and 
            self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": 
                                    text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    
    filtered_blocks = []
    for block in blocks:
        cleaned_block = block.strip()
        
        if cleaned_block != "":
            filtered_blocks.append(cleaned_block)
            
    return filtered_blocks



class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"


def block_to_block_type(block):
    lines = block.split("\n")

    # Headings: 1-6 '#' followed by a space
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"

    # Code blocks: Start and end with ```
    if len(lines) > 1 and block.startswith("```") and block.endswith("```"):
        return "code"

    # Quote blocks: Every line starts with >
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                break
        else:
            return "quote"

    # Unordered list: Every line starts with "- "
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                break
        else:
            return "unordered_list"

    # Ordered list: Every line starts with "i. " starting at 1
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                break
            i += 1
        else:
            return "ordered_list"

    # Default
    return "paragraph"
