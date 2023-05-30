# INSERTING A NEW NODE IN BETWEEN TWO NODES
# singly linkedlist
#create nodes
#create linkedlist 
#add nodes to linkedlist
#print list

class Node:
    #to create node
    def __init__(self,data):
        #accepts the data which we pass
        self.data = data #initilize the data part of first node parimeter
        self.next =None #since next pointer initially points to nowhere we are assigning it to none


class LinkedList:
    #to create a linked list
    def __init__(self):
        self.head = None

    def listLength(self):
        #traverse the LL from fist to last and each iteration increase the count
        currentNode =self.head
        length =0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def insertHead(self,newNode):
        # this method accepts data => and next as none (new node)
        temporaryNode = self.head 
        self.head = newNode 
        self.head.next = temporaryNode
        del temporaryNode #now that we don't need temporary node we are deleting it.    

    
    def insertAt(self,newNode,Position):
        #logic
        #traverse the list till position 1 ; Store the details of previous node ;  Make a connection from the next of previous node to new node ; Make a connection from next of new node to node at position 1
        #The new node now becomes your node at position 1 and the node that was earlier at position 1 now becomes the node at position 2
        #head=>10->20->30->None || newNode => 15-> Node || position =>1
        if Position <0 or Position > self.listLength():
            print("invalid position")
            return
        if Position == 0:
            self.insertHead(newNode)
            return
        currentNode = self.head #starts from the head node 10,20..
        currentPosition = 0 #keeps track of current node initial position 
        while True:
            if currentPosition == Position:
                previousNode.next = newNode
                newNode.next =currentNode
                break
            else:
                previousNode = currentNode #storing current node data and value in a temprory variable because it is going to change to next node
                currentNode =currentNode.next
                currentPosition += 1 # 0, 1
        
    def insertEnd(self,newNode):
        #head => john -> None
        if self.head is None:
            self.head = newNode
        else:
            # head => 10->20->Node || 10 -> 30
            # Always next of our last node points to none so we need to break the connection bw next opf our last node and make th enext of our last node to new node
            lastNode = self.head #lets have a node called lastnode which starts from the first node
            #traverse the list from the start till the end to identify the last node
            #now arrive at the last node of our linkedlist 
            while True:
                #check if the last node next is none
                if lastNode.next is None:
                    break #means we reached our last node and we are feee to break our while loop
                lastNode =lastNode.next #if not reached to last node advance to next node
            #once while loop breaks we are at the last node break the connection from last node.next as none to last node .next as new node    
            lastNode.next =newNode
    
    def printList(self):
        #head =>10->20->30->None
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            #if current node is none means last head 
            print(currentNode.data)
            currentNode = currentNode.next

        
# Node => data(data which we feel to store), next(the pointer which points to the next node)
#object for our next class
#firstNode.data => John, FirstNode.next => None
firstNode = Node(10)
#add this node to the linkedlist
#create an object of the class linkedlist(which is initially empty) (make sure the head of the linkedlist is none)
linkedList = LinkedList()
linkedList.insertEnd(firstNode)

secondNode = Node(20)
linkedList.insertEnd(secondNode)
thirdNode = Node(30)
linkedList.insertEnd(thirdNode)
fourthNode = Node(15)
linkedList.insertAt(fourthNode,1) #Node and position to be inserted at
linkedList.printList()
