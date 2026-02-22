import unittest

from gencontent import extract_title


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_title_success(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")

    def test_extract_title_with_spaces(self):
        md = "#    Hello World    "
        self.assertEqual(extract_title(md), "Hello World")

    def test_extract_title_multiline(self):
        md = "Some text\n\n# Real Title\nMore text"
        self.assertEqual(extract_title(md), "Real Title")

    def test_extract_title_no_h1_raises(self):
        md = "## This is H2\nJust text"
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_extract_title_empty_string(self):
        with self.assertRaises(ValueError):
            extract_title("")

if __name__ == "__main__":
    unittest.main()