import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_single_prop(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_empty_props(self):
        node = HTMLNode(tag="p", value="This is a paragraph.")
        self.assertEqual(node.props_to_html(), '')

    def test_repr_method(self):
        node = HTMLNode(tag="h1", value="Header", props={"class": "header"})
        self.assertEqual(repr(node), 'HTMLNode(tag=h1, value=Header, children=[], props={\'class\': \'header\'})')

    def test_htmlnode_with_children(self):
        child_node = HTMLNode(tag="span", value="Child Text")
        parent_node = HTMLNode(tag="div", children=[child_node], props={"class": "container"})
        self.assertEqual(repr(parent_node), 'HTMLNode(tag=div, value=None, children=[HTMLNode(tag=span, value=Child Text, children=[], props={})], props={\'class\': \'container\'})')

if __name__ == "__main__":
    unittest.main()
