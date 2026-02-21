from textnode import markdown_to_blocks


def test_markdown_to_blocks_extended(self):
    md = """
# Heading

This is a paragraph.


- Item 1
- Item 2
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "# Heading",
            "This is a paragraph.",
            "- Item 1\n- Item 2",
        ],
    )

    md_empty = "   \n\n  \n  "
    self.assertEqual(markdown_to_blocks(md_empty), [])

    md_spaced = "  Block 1  \n\n\n   Block 2   "
    self.assertEqual(
        markdown_to_blocks(md_spaced),
        ["Block 1", "Block 2"]
    )