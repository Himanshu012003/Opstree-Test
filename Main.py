# Online Python Playground
# Use the online IDE to write, edit & run your Python code
# Create, edit & delete files online

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end='')
            current = current.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

def add_lists(l1, l2):
    l1.reverse()
    l2.reverse()
    p1, p2 = l1.head, l2.head
    carry = 0
    result_list = LinkedList()

    while p1 or p2 or carry:
        sum_value = carry
        if p1:
            sum_value += p1.data
            p1 = p1.next
        if p2:
            sum_value += p2.data
            p2 = p2.next
        carry = sum_value // 10
        result_list.insert(sum_value % 10)

    result_list.reverse()
    return result_list

def subtract_lists(l1, l2):
    l1.reverse()
    l2.reverse()
    p1, p2 = l1.head, l2.head
    borrow = 0
    result_list = LinkedList()

    while p1:
        sub_value = p1.data - (p2.data if p2 else 0) - borrow
        if sub_value < 0:
            sub_value += 10
            borrow = 1
        else:
            borrow = 0
        result_list.insert(sub_value)
        p1 = p1.next
        if p2:
            p2 = p2.next

    result_list.reverse()
    return result_list

def multiply_lists(l1, l2):
    l1.reverse()
    l2.reverse()
    p1 = l1.head
    result = [0] * (get_length(l1) + get_length(l2))

    i = 0
    while p1:
        carry = 0
        p2 = l2.head
        j = 0
        while p2:
            product = p1.data * p2.data + result[i + j] + carry
            carry = product // 10
            result[i + j] = product % 10
            p2 = p2.next
            j += 1
        if carry > 0:
            result[i + j] += carry
        p1 = p1.next
        i += 1

    result_list = LinkedList()
    leading_zero = True
    for value in reversed(result):
        if leading_zero and value == 0:
            continue
        leading_zero = False
        result_list.insert(value)

    if result_list.head is None:
        result_list.insert(0)
    return result_list

def get_length(l):
    length = 0
    current = l.head
    while current:
        length += 1
        current = current.next
    return length

def create_list(num_str):
    l = LinkedList()
    for char in num_str:
        l.insert(int(char))
    return l

if __name__ == "__main__":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    list1 = create_list(num1)
    list2 = create_list(num2)

    print("List 1: ", end='')
    list1.print_list()
    print("List 2: ", end='')
    list2.print_list()

    sum_list = add_lists(list1, list2)
    print("Sum: ", end='')
    sum_list.print_list()

    diff_list = subtract_lists(list1, list2)
    print("Difference: ", end='')
    diff_list.print_list()

    prod_list = multiply_lists(list1, list2)
    print("Product: ", end='')
    prod_list.print_list()
