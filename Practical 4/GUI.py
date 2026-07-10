import tkinter as tk

class Node:
    def __init__(self, d):
        self.data = d
        self.prev = self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def begin(self, d):
        n = Node(d)
        n.next = self.head
        if self.head:
            self.head.prev = n
        self.head = n

    def end(self, d):
        n = Node(d)
        if not self.head:
            self.head = n
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = n
        n.prev = t

    def del_begin(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def del_end(self):
        if not self.head:
            return
        t = self.head
        if not t.next:
            self.head = None
            return
        while t.next:
            t = t.next
        t.prev.next = None

    def show(self, rev=False):
        if not self.head:
            return "List Empty"
        a = []
        t = self.head
        if rev:
            while t.next:
                t = t.next
            while t:
                a.append(str(t.data))
                t = t.prev
        else:
            while t:
                a.append(str(t.data))
                t = t.next
        return " <-> ".join(a)

d = DLL()

def update(text):
    lbl.config(text=text)

root = tk.Tk()
root.title("Doubly Linked List")
root.geometry("500x300")

e = tk.Entry(root)
e.pack(pady=5)

tk.Button(root, text="Insert Begin",
          command=lambda:[d.begin(int(e.get())), update(d.show()), e.delete(0,'end')]).pack()

tk.Button(root, text="Insert End",
          command=lambda:[d.end(int(e.get())), update(d.show()), e.delete(0,'end')]).pack()

tk.Button(root, text="Delete Begin",
          command=lambda:[d.del_begin(), update(d.show())]).pack()

tk.Button(root, text="Delete End",
          command=lambda:[d.del_end(), update(d.show())]).pack()

tk.Button(root, text="Forward",
          command=lambda:update(d.show())).pack()

tk.Button(root, text="Backward",
          command=lambda:update(d.show(True))).pack()

lbl = tk.Label(root, text="List Empty", font=("Arial",12))
lbl.pack(pady=20)

root.mainloop()
