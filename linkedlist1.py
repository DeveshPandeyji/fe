class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
      def __init__(self):
           self.head=None
      

      def insert_at_last(self,data):
           newnode=Node(data)
           if self.head is None:
                self.head=newnode
           else:
                last=self.head
                while last.next:
                 last=last.next
                last.next=newnode
      def insert_at_first(self,data):
          newnode=Node(data)
          if self.head is None:
              self.head = newnode
          else:
              new=self.head
              self.head=newnode
              first=self.head
              first.next=new 
      def insert_at_position(self,positionnumber,data):
          new=self.head
          if positionnumber==1:
              new.data=data
          else:
            for i in range(positionnumber-1):
                new=new.next 

            new.data=data
      def delete_node(self,data):
          first=self.head
          if first.data==data:
               self.head=first.next
          else:
               prev=None
               while first.data!=data:
                    prev=first
                    first=first.next 
               prev.next=first.next 
                  
      def display(self):
           current=self.head
           while current:
                print(current.data,end="->")
                current=current.next
           if current is None:
              print("NULL")
                          
l1=linkedlist()

l1.insert_at_last(100)
l1.insert_at_last(110)
l1.insert_at_position(1,10)
l1.insert_at_position(2,20)
l1.display()
#def linko():
 #a=input("CHOOSE THE OPTION\n1.ENTER THE DETAIL IN LINKED LIST\n2.DISPLAY THE LINKED LIST\n ")

 #if a=="1":
  # b=input("ENTER THE DATA BY ADDING COMMA(,)").split(",")
   #lis=list(b)
   #for i in lis:
    #   l1.append(i)
   #linko()
 #elif a=="2":
  #   l1.display()
   #  linko()
 #else:
  #   print("Please select from 1 or 2")
  #   linko()
#linko()
    

            
            






