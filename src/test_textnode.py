import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node", "bold")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_text_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_url(self):
        node = TextNode("This is a text node", "bold", "http://example.com")
        node2 = TextNode("This is a text node", "bold", "http://example.org")
        self.assertNotEqual(node, node2)

    def test_eq_with_none_url(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("Hello", "bold", "http://example.com")
        self.assertEqual(repr(node), "TextNode(text='Hello', text_type='bold', url='http://example.com')")

    def test_repr_none_url(self):
        node = TextNode("Hello", "italic")
        self.assertEqual(repr(node), "TextNode(text='Hello', text_type='italic', url=None)")


if __name__ == "__main__":
    unittest.main()
