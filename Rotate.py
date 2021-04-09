class Node:
    
    def __init__(self,value,next=None):
        self.value =value;
        self.next =next;
        
class LinkedList:
    
    def __init__(self):
        self.head =None;
        
    def append(self,value):
        if self.head ==None:
            self.head =Node(value);
        else:
            t =self.head;
            while t.next:
                t =t.next;
            t.next = Node(value);
            
    def remove(self,value):
        t = self.head;
        if t.value ==value:
            self.head =t.next;
            
        elif t ==None:
            print('There are no elements in this linkedlist');
            
        else:
            while t.next:
                if t.next.value ==value:
                    a = t.next.next;
                    t.next =a;
                    break;
                t =t.next;
                
    def printall(self):
        if self.head ==None:
            print('There are no values in this linkedlist');
        else:
            t=self.head;
            
            while t.next:
                print(t.value);
                t = t.next;
            print(t.value);
            
    def rotate(self):
        
        t =self.head;
        
        while t.next.next:
            t=t.next;
            
        a=t.next;
        t.next=None;
        a.next = self.head;
        self.head = a;
        
        
x= LinkedList();
x.append(1);
x.append(2);
x.append(3);
x.append(4);
x.remove(1);
x.printall()
x.rotate();
x.printall()