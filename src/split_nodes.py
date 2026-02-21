from textnode import TextNode, TextType
from extract_markdowns import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_nodes = []
        sections = node.text.split(delimiter)


        if len(sections) % 2 == 0:
            raise Exception(f"Invalid Markdown syntax: formatted text not closed with delimiter '{delimiter}'")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        
        new_nodes.extend(split_nodes)
        
    return new_nodes



def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        # If it's not a text node, we don't try to split it
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        original_text = node.text
        images = extract_markdown_images(original_text)
        
        # If no images, keep the node as is
        if len(images) == 0:
            new_nodes.append(node)
            continue

        for image in images:
            image_alt = image[0]
            image_link = image[1]
            
            # We reconstruct the markdown string to use as the delimiter
            # Example: "![alt](url)"
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)
            
            # If there is text before the image, add it
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
                
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            # Add the image node
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            
            # Update the original text to be everything AFTER the image
            # so we can process the next image in the loop
            original_text = sections[1]

        # If there is any text left over after the last image, add it
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
            
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        # ... check type ...
        original_text = node.text
        links = extract_markdown_links(original_text)
        
        print(f"DEBUG: Found links {links} in text '{original_text}'") # Add this!
        
        if len(links) == 0:
            new_nodes.append(node)
            continue

        original_text = node.text
        links = extract_markdown_links(original_text)

        if len(links) == 0:
            new_nodes.append(node)
            continue

        for link in links:
            link_text = link[0]
            link_url = link[1]
            
            sections = original_text.split(f"[{link_text}]({link_url})", 1)
            
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
                
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
            
    return new_nodes