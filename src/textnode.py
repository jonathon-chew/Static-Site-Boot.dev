#!/opt/homebrew/bin/python3

class TextNode:

    def __init__(self, text, textType, url=None) -> None:
        self.text = text
        self.text_type = textType 
        self.url = url
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        if self.url == None :
            return f"TextNode(text='{self.text}', text_type='{self.text_type}', url=None)"   
        return f"TextNode(text='{self.text}', text_type='{self.text_type}', url='{self.url}')"

def main():
    node1 = TextNode("Hello", "bold", "http://example.com")
    node2 = TextNode("Hello", "bold", "http://example.com")
    node3 = TextNode("Hello", "italic")

    print(node1 == node2)
    print(node1 == node3)

