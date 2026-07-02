Design a text editor with a cursor that can do the following:

    Add text to where the cursor is.
    Delete text from where the cursor is (simulating the backspace key).
    Move the cursor either left or right.

When deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text and cannot be moved beyond it. More formally, we have that 0 <= cursor.position <= currentText.length always holds.

Implement the TextEditor class:

    TextEditor() Initializes the object with empty text.
    void addText(string text) Appends text to where the cursor is. The cursor ends to the right of text.
    int deleteText(int k) Deletes k characters to the left of the cursor. Returns the number of characters actually deleted.
    string cursorLeft(int k) Moves the cursor to the left k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.
    string cursorRight(int k) Moves the cursor to the right k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.

# Solution
# Doubly Linked List, not that good at it

# TC: O(K) for all
# SC: O(N) where N is the maximum number of text


class Node:
    def __init__(self,char = None):
        self.char = char
        self.prev = self.next = None
class TextEditor:
    def __init__(self):
        self.head = Node()
        self.current = self.head
    def addText(self, text: str) -> None:
        old_next = self.current.next
        for s in text:
            self.current.next = Node(s)
            self.current.next.prev = self.current
            self.current = self.current.next
        if old_next is not None:
            self.current.next = old_next
            old_next.prev = self.current
    def deleteText(self, k: int) -> int:
        count = 0
        for _ in range(k):
            if self.current.char is None:
                break
            prev = self.current.prev
            nxt = self.current.next
            prev.next = nxt
            if nxt is not None:
                nxt.prev = prev
            self.current = prev
            count += 1
        return count

    def cursorLeft(self, k: int) -> str:
        for _ in range(k):
            if self.current.prev is not None:
                self.current = self.current.prev
        return self.helper()

    def cursorRight(self, k: int) -> str:
        for _ in range(k):
            if self.current.next is not None:
                self.current = self.current.next
        return self.helper()
    def helper(self) -> str:
        res = []
        curr = self.current
        for _ in range(10):
            if curr and curr.char is not None:
                res.append(curr.char)
                curr = curr.prev
        return "".join(reversed(res))


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
