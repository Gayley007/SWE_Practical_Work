# define node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
# Implement append method
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
#implement display method
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))
#Implement insert method
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node
#Implement delete method
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
#implement search method
    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1
# implement reverse method
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


#middle element of the linked list.
    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None
# detect if the linked list has a cycle.
    def has_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
# remove duplicates from an unsorted linked list.
    def remove_duplicates(self):
        if not self.head:
            return
        seen = set()
        current = self.head
        seen.add(current.data)
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next
# merge two sorted linked lists into a single sorted 
    def merge_sorted(self, other):
        dummy = Node(0)
        tail = dummy
        a, b = self.head, other.head
        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

# main Print
#3.4
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()
#5
ll.insert(4, 1)
print("List 1 after inserting 4:")
ll.display()
#6
ll.delete(2)
print("List 1 after deleting:")
ll.display()
#7
print("Position of 4 in List 1:", ll.search(4))
print("Position of 4 in List 1:", ll.search(5))
#8
ll.reverse()
print("List 1 after reversing:")
ll.display()

#EXERCISE
print("Middle Element:", ll.find_middle())

print("Has Cycle:", ll.has_cycle())

ll.remove_duplicates()
print("List 1 after removing duplicates:")


ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)
ll1.display()
ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

merged_list = ll1.merge_sorted(ll2)
print("Merged List:")
merged_list.display()