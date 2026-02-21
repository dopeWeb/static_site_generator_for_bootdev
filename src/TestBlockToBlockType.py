import unittest
from textnode import block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Main Title"), "heading")
        self.assertEqual(block_to_block_type("### Sub Title"), "heading")
        self.assertEqual(block_to_block_type("####### Not a heading"), "paragraph")

    def test_code(self):
        code_block = "```\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(code_block), "code")

    def test_quote(self):
        quote = "> This is a quote\n> that spans lines"
        self.assertEqual(block_to_block_type(quote), "quote")
        bad_quote = "> This is a quote\nInvalid line"
        self.assertEqual(block_to_block_type(bad_quote), "paragraph")

    def test_unordered_list(self):
        ul = "- Item 1\n- Item 2"
        self.assertEqual(block_to_block_type(ul), "unordered_list")
        bad_ul = "- Item 1\n* Item 2"
        self.assertEqual(block_to_block_type(bad_ul), "paragraph")

    def test_ordered_list(self):
        ol = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(ol), "ordered_list")
        bad_ol = "1. First\n3. Third" # Пропуск номера
        self.assertEqual(block_to_block_type(bad_ol), "paragraph")
        wrong_start = "2. First\n3. Second"
        self.assertEqual(block_to_block_type(wrong_start), "paragraph")

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("Just a normal text."), "paragraph")

if __name__ == "__main__":
    unittest.main()
