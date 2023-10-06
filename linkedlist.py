#-------------------------------------------------------------------------------
# Name:        linkedlist
# Purpose:
#
# Author:      theo
#
# Created:     03/09/2023
#-------------------------------------------------------------------------------

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values is not None:
            for v in values:
                self.add_after_queue(v)
            pass

    def __repr__(self):
        if self.head is None:
            return("cette liste est vide")
        chaine = str(self.head)
        courant = self.head.next

        while courant is not None:

            chaine += "->" + str(courant)
            courant = courant.next
        return chaine

    def add_before_head(self, value):

        cell = ListNode(value)
        cell.value = value
        cell.next = self.head
        self.head = cell

    def add_after_queue(self, value):
        cell = ListNode(value)

        if self.head is None:

            self.add_before_head(value)
            return

        courant = self.head

        while courant.next is not None:
            courant = courant.next

        courant.next = cell

    def find(self, value):
        cell = self.head
        while cell.next == None:
            cell = cell.next
            if cell == value:
                return cell
                break

        print(value, "n'est pas dans la liste")



    def insert(self, value, pos):
        # insert a new cell containing the given element
        # at the given position (the head is 0)
        # if the position is larger than the length of the list,
        # the element is inserted at the end
        pass

    def delete(self, value):
        # deletes the first cell containing the given value
        # returns the deleted cell if an element was deleted
        pass

    def merge(self, other):
        # adds the other linked list at the end of the current list
        # the other list should be emptied after the operation
        pass

    def revert(self):
        # revert the content of the current linked list
        pass

class ListNode:

    def __init__(self, value=None, next=None):
        # a modifier
        self.value = value
        self.next = next

    def __repr__(self):

        return str(self.value)


def main():

    l1 = LinkedList([1,2,3])
    l1.add_after_queue(4)
    l1.add_after_queue(5)
    l1.add_after_queue(6)
    print(l1)
    print(l1.find(50))


if __name__ == '__main__':
    main()
