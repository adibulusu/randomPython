class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, val):
        # node instantiation
        node = Node(val, self.head)
        # assigns the head (first) node to node created
        self.head = node

    def insert_end(self, val):
        if self.head == None:
            self.head = Node(val, None)
            return

        curr = self.head
        # iterates through linked list to find end
        while curr.next:
            curr = curr.next

        # when it reaches the end, a new node is created there
        curr.next = Node(val, None)

    def insert_values(self, val_list):
        # clears linked list of values
        self.head = None
        # iterates through value list and appends each value using insert end functiiono
        for values in val_list:
            self.insert_end(values)

    def find_length(self):
        count = 0
        # iterate through list and count after each node
        curr = self.head
        while curr:
            count += 1
            curr = curr.next

        return count

    def remove_element(self, index):
        # stop if index is less thann 0 or greater than length of list
        if index < 0 or index >= self.find_length():
            raise Exception("Invalid index")
        # if index is 0, that means u want to remove head
        # assign next value as new head and ur done
        if index == 0:
            self.head = self.head.next
            return
        # for any other value, manually count and iterate through list
        count = 0
        curr = self.head
        while curr:
            # once u stop at index previous to what u want to remove
            # assign next value to next next value
            # that creates link between current value and value after what u want to remove
            if count == index - 1:
                curr.next = curr.next.next
                break
            count+=1
            curr = curr.next

    def insert_at(self, index, val):
        if index < 0 or index >= self.find_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_beginning(val)
            return

        count = 0
        curr = self.head
        while curr:
            # once u stop at index previous to where u want to add
            # create new node that inserts value, and then links to next value
            if count == index - 1:
                node = Node(val, curr.next)
                curr.next = node
                break
            count+=1
            curr = curr.next

    def insert_after_value(self, val_after, val):
        curr = self.head
        while curr:
            if curr.next is None:
                self.insert_end(val)
                break
            if curr.val == val_after:
                node = Node(val, curr.next)
                curr.next = node
                break
            curr = curr.next

    def remove_by_value(self, val):
        curr = self.head
        while curr:
            if curr.next.val == val:
                curr.next = curr.next.next
                break
            curr = curr.next
        

    def printList(self):
        if self.head == None:
            print("Empty linked list")
            return

        curr = self.head

        while curr:
            print(curr.val, end=" ")
            curr = curr.next



if __name__ == "__main__":
    l1 = LinkedList()
    # l1.insert_beginning(5)
    # l1.insert_beginning(6)
    # l1.insert_end(7)
    l1.insert_values([5,4,7,6,8])
    l1.find_length()
    l1.printList()
    print("\nLength: ", l1.find_length())
    l1.remove_element(2)
    l1.printList()
    print("\nLength: ", l1.find_length())
    l1.insert_at(3, 9)
    l1.printList()
    print("\nLength: ", l1.find_length())
    l1.insert_after_value(6,10)
    l1.printList()
    print("\nLength: ", l1.find_length())
    l1.remove_by_value(4)
    l1.printList()
    print("\nLength: ", l1.find_length())
    l1.remove_by_value(10)
    l1.printList()
    print("\nLength: ", l1.find_length())


