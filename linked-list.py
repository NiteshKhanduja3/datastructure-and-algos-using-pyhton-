# It is List  Which consists of node ( Data value and pointer)
#the first node is called the head and the tail 
#at the end the tail value is null
# In javascript we have to make a linked list there is no built ins
#Why we need Linked list? inserting in between link list is easy than array
#BigO of link list is  append and prepend = O(1) ,,, lookup ,delete and Insert is O(n)


#creating a link list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkdList:
    def __init__(self):
        self.head =None



    def Insert_In_List(self,data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
               current = current.next
               current.next = newNode
        else:
            self.head = newNode
    
    
    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.data), 
            temp = temp.next
    

if __name__ == '__main__':
    list1 =LinkdList()
    list1.head =Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    list1.head.next =second
    second.next = third
    third.next = fourth

    list1.Insert_In_List(22)
    list1.printList()

