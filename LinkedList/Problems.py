import LinkedList


class Problems :
    def sortLinkedList(self, inputList):
        if inputList is None :
            return None

        list0 = LinkedList.SinglyLinkedList()
        list1 = LinkedList.SinglyLinkedList()
        list2 = LinkedList.SinglyLinkedList()

        current = inputList.head

        while current is not None:
            if current.data == 0:
                list0.append(current)
            elif current.data == 1:
                list1.append(current)
            else :
                list2.append(current)
            current = current.next

        if list0.tail is not None :
            list0.tail.next = None

        if list1.tail is not None :
            list1.tail.next = None

        if list2.tail is not None :
            list2.tail.next = None

        result = LinkedList.SinglyLinkedList()

        self.appendList(list0, result)
        self.appendList(list1, result)
        self.appendList(list2, result)

        return result


    def appendList(self, toAdd, original):
        if toAdd.head is None or toAdd is None :
            return None
        original.append(toAdd.head)
        original.tail = toAdd.tail

    def oddEvenLinkedList(self, inputList):
        if inputList is None :
            return None

        listOdd = LinkedList.SinglyLinkedList()
        listEven = LinkedList.SinglyLinkedList()

        current = inputList.head

        while current is not None :
            if current.data%2 ==0 :
                listEven.append(current)
            elif current.data%2 != 0 :
                listOdd.append(current)

            current = current.next

        if listOdd.tail is not None :
            listOdd.tail.next = None

        if listEven.tail is not None :
            listEven.tail.next = None

        return [listOdd,listEven]

    #Question

    '''Given a Linked List with a cycle, find the node where the cycle begins.
    For example, node 2 in the below image.'''

    def findLengthOfCycle(self, head):
        fastPointer = head
        slowPointer = head

        while( fastPointer != None) :
            fastPointer = fastPointer.next
            if fastPointer == slowPointer :
                break
            if fastPointer != None :
                fastPointer = fastPointer.next
                if fastPointer == slowPointer:
                    break
            slowPointer = slowPointer.next

        if fastPointer == None :
            raise Exception('No cycle')

        fastPointer = fastPointer.next
        count = 1
        while(slowPointer != fastPointer) :
            fastPointer = fastPointer.next
            count += 1

        return count


    def startOfCycle(self, head):
        fastPointer = head
        slowPointer = head

        cycleLength = self.findLengthOfCycle(head)

        temp = cycleLength
        while temp > 0 :
            fastPointer = fastPointer.next
            temp -= 1

        while slowPointer != fastPointer :
            fastPointer = fastPointer.next
            slowPointer = slowPointer.next

        return fastPointer






a = LinkedList.SinglyLinkedList()
a.generateListFromArray([1,2,3,4,5])
print(a.head)
count = 0
n = a.head
while(count<3) :
    n = n.next
    count += 1

a.append(n)
start = Problems().startOfCycle(a.head)
print(start.data)





