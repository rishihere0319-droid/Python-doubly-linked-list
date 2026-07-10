class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        n = Node(data)
        n.next = self.head
        if self.head:
            self.head.prev = n
        self.head = n

    def insert_end(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = n
        n.prev = t

    def delete_begin(self):
        if not self.head:
            print("List Empty")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_end(self):
        if not self.head:
            print("List Empty")
            return
        t = self.head
        if not t.next:
            self.head = None
            return
        while t.next:
            t = t.next
        t.prev.next = None

    def forward(self):
        t = self.head
        while t:
            print(t.data, end=" <-> ")
            t = t.next
        print("None")

    def backward(self):
        if not self.head:
            print("List Empty")
            return
        t = self.head
        while t.next:
            t = t.next
        while t:
            print(t.data, end=" <-> ")
            t = t.prev
        print("None")


d = DLL()

while True:
    print("\n1.Insert Begin\n2.Insert End\n3.Delete Begin\n4.Delete End\n5.Forward\n6.Backward\n7.Exit")
    ch = input("Choice: ")

    if ch == "1":
        d.insert_begin(int(input("Value: ")))
    elif ch == "2":
        d.insert_end(int(input("Value: ")))
    elif ch == "3":
        d.delete_begin()
    elif ch == "4":
        d.delete_end()
    elif ch == "5":
        d.forward()
    elif ch == "6":
        d.backward()
    elif ch == "7":
        break
