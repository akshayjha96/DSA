#Insert a new node as the head node
#Insert as the head node
#By removing the existing head node we would lost the connection of the linkedlist and the next of the replaced node would not know how to point to the node replaced and that breaks the connection between the nodes of our linkedlist 
#Store head node in a temporary node
#then remove the current head node and store new instance to the head node and next of new node point to the second node and point next of second node to third node
#Preserve the current head node in a temporary node ; Make the new node as the head node ; Make the next of your new node point to the temporary node

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
    
    def insertHead(self,newNode):
        # this method accepts data => Akku and next as none (new node)
        temporaryNode = self.head #john
        self.head = newNode #Akku
        self.head.next = temporaryNode
        del temporaryNode #now that we don't need temporary node we are deleting it.
        
    def insertEnd(self,newNode):
        #head => john -> None
        if self.head is None:
            self.head = newNode
        else:
            # head => John->Ben->Node || John -> matthew
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
        #head =>john->ben->Matthew->None
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
firstNode = Node("John")
#add tjis node to the li nkedlist
#create an object of the class linkedlist(which is initially empty) (make sure the head of the lin kedlist is none)
linkedList = LinkedList()
linkedList.insertEnd(firstNode)

secondNode = Node("Ben")
linkedList.insertEnd(secondNode)
thirdNode = Node("Matthew")
linkedList.insertEnd(thirdNode)
fourthNode = Node("Akku")
linkedList.insertHead(fourthNode) #method for inserting in the beggining of the list
linkedList.printList()