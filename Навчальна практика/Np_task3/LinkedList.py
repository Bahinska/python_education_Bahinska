from Node import *
from helper import *
import random

class LinkedList:
    def __init__(self):
        self.head = None

    def len(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def user_input(self, size):
        for i in range(size):
            self.push_back(number_check(input()))

    def random_gen(self, size):
        a, b = range_input()
        for i in range(size):
            self.push_back(random.randint(a, b))

    def push_back(self, value):
        new_element = Node(value)
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def delete(self, value):
        prev = None
        current = self.head
        while current and (current.item != value):
            prev = current
            current = current.next

        # now element to del is current
        if current.item == value:
            if current == self.head:  # if element to delete is head
                self.head = current.next
            else:
                prev.next = current.next

            while current.next:
                current = current.next
        else:
            raise Exception("Element does not exist")

    def pop(self):
        current = self.head
        if current is None:
            raise IndexError('Empty LinkedList')
        if current.next is None:
            self.clear()
            return
        while current.next:
            if current.next.next is None:
                current.next = None
            else:
                current = current.next

    def clear(self):
        temp = self.head
        if temp is None:
            raise IndexError('Empty LinkedList')
        while temp:
            self.head = temp.next
            temp = self.head

    def delete_by_index(self, pos):
        if pos < 0 | pos > self.len():
            raise Exception("Invalid index")

        if pos == self.len()-1:
            self.pop()
        if pos == 0:
            self.head = self.head.next
        else:
            prev = None
            current = self.head
            i = 0
            while current:
                if i == pos:
                    prev.next = current.next
                prev = current
                current = current.next
                i += 1

    def insert(self, value, pos):
        if pos < 0 | pos > self.len():
            raise Exception("Invalid index")

        if pos == 0:
            self.head = Node(value, self.head)
        if pos == self.len():
            self.push_back(value)
        else:
            current = self.head
            i = 0
            while current.next:
                if i == pos - 1:
                    current.next = Node(value, current.next)
                current = current.next
                i += 1

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.item) + " "
            current = current.next
        return result

    def processing(self):
        current = self.head
        while current:
            if current.item == 0:
                current = current.next
                continue
            num = str(current.item)
            x = num[0]
            y = num[1]
            if ((num[2] == x) & (num[3] == y)) | ((num[2] == y) & (num[3] == x)):
                pass
            else:
                self.delete(current.item)
                self.push_back(0)

            current = current.next
