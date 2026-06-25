class Node:
    def __init__(self, data, next):
        self.data = data
        self.next=next

class LinkedList:
    def __init__ (self):
        self.head = None

    def insert_first(self, data):
        self.head = Node(data, self.head)

    def insert_last(self, data):
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(data, itr.next)

    def counter(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        print(count)
        return count 

    def insert_middle(self, data):
        itr = self.head
        count = self.counter()
        position = count//2
        for _ in range (position-1):
            itr = itr.next
        itr.next = Node(data, itr.next)

    def insert_at_pos(self, data):
        position = input("Enter the index num: ")
        list_length = self.counter()
        if int(position) >= int(list_length):
            print("Index out of bound!")
        else:
            itr = self.head
            for _ in range (int(position)-1):
                itr = itr.next
            itr.next = Node(data, itr.next)

    def print(self):
        llstr = ''
        if self.head is None:
            print("The list is Empty!")
        else:
            itr=self.head
            while itr:
                llstr += str(itr.data) + '-->'
                itr=itr.next
        print(llstr)

if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_first(20)
    llist.insert_first(30)
    llist.insert_first(40)
    llist.insert_first(50)
    llist.insert_last(69)
    llist.insert_last(100)
    llist.insert_middle(15)
    llist.insert_middle(47)
    llist.insert_at_pos(93)
    llist.insert_at_pos(1007)
    llist.counter()
    llist.print()