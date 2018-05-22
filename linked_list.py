


#Start of a node, node has always two parts, that which holds the data and the other which hold the next.node
#data=None this is done if no data is given. Important when creating the head for a linked list.
class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        

#when linked list initializes it creates a hea        
class linked_list:
    def __init__(self):
        self.head = node()
        
    #append method which append an element to the end node of linked list. (means in last node's next.node data is None)
    def append(self,data):
        
        #making new node in which some data is put
        new_node = node(data)
        
        #this is so that we start from the first node (data is None)
        cur = self.head
        
        #While loop is to check when we get the last node whose next.node data = None
        while cur.next != None:     
            #nodes are checked one by one from first to last 
            cur = cur.next
        #when we finally have None in cur.next we put the new_node there.
        cur.next = new_node
        
    #just get's the length of the linked list. 
    def length(self):
        #again we start by the first node
        cur = self.head
        total = 0
        while cur.next != None:
            total+=1
            cur = cur.next
        
        return total
    
    def display(self):
        #putting datavalues to a list. 
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)
        
        
    def delete(self,index):
        
        #if there isn't such index existing
        if (index>=self.length() or index<0):
            print("Index out of bounds in delete method")
            return
        cur_index = 0
        cur_node=self.head
        while True:
            
            #so last_node.next gets the cur_node.next
            #so when we delete a node, we just   node1->delete pointer node2 -> node3   ===>    node1 -> put the pointer node3 
            #this will probably leave node2.next hanging so that ===>   node1 and node2 -> node 3
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index==index:
                last_node.next = cur_node.next
                return
            cur_index +=1
            
            
    def insert_index(self, data, index):
        #index too big or small
        if (index>= self.length() or index<0):
            print("index is out of bounds in insert_index method")
            return
        
        #different explaining method
        #1. node1 ---disconnect---> node2 
        #2. node1 ---connect---> node3 
        #3. node1 -> node3 ---connect---> node2
        #4. node1 -> node3 -> node2
        new_node = node(data)
        current_index = 0
        current_node = self.head
        while current_index != index:
            current_node = current_node.next
            current_index +=1
        new_node.next = current_node.next
        current_node.next = new_node
        print(current_node.next.data)
    
    #loop if node2 <= node3, insert node2 ===> node1 -> node2 -> node3
    def insertion_sort(self, data):
        cur = self.head
        new_node = node(data)
        while True:
            if cur.next == None:
                cur.next = new_node
                break
            elif new_node.data <= cur.next.data:
                new_node.next = cur.next
                cur.next = new_node
                break
            elif new_node.data > cur.next.data:
                cur = cur.next
                continue
            else:
                break
            
            
            
    #if a value exists in linked list get the index for that value
    def get_index(self,value):
        cur = self.head
        index = 0
        cur = cur.next
        #this while loop checks the whole list if there exists given value
        while cur.next != None:
            if(cur.data == value):
                break
            #if there isn't such a value.
            elif(self.length() -1 - index == 0):
                print("no such value")
                return 0
            cur = cur.next
            index +=1
        return index
            
    #I tried to deal with two my own lists rather than []
    def sort_with_temparray(self):
        temparray = linked_list()
        llength = self.length()
        tempdata = 0
        lasttemp = 0
        for x in range(llength):
            #always from the beginning 
            cur = self.head
            tempdata = cur.next.data
            #till the end of the list
            while cur.next != None:
                
                cur = cur.next
                
                #needed to get the last value. 
                if(cur.next == None):
                    lasttemp = cur.data
                    print("This is lasttemp: ",lasttemp)
                #so if tempdata is bigger it needs to be changed for the smaller one (cur.data)
                elif(tempdata >= cur.data):
                    tempdata = cur.data
                    print("This is tempdata: ",tempdata)
            #check the last value of the list
            if(lasttemp < tempdata):
                tempdata = lasttemp
            #temparray should be in order from smallest to biggest
            temparray.append(tempdata)
          
            
            #we delete the values in the first list
            self.delete(self.get_index(tempdata))
           
            temp_cur = temparray.head
        #we append temparray values in the first list
        for x in range(temparray.length()):
            temp_cur = temp_cur.next
            self.append(temp_cur.data)
            
        
        
        
    
            
                
        
lista = linked_list()
lista.display()

lista.append(1) 
lista.append(2) 
lista.append(4) 
lista.append(7) 
lista.append(133)
lista.insert_index(500, 4)
lista.insert_index(500, 55) 
lista.insertion_sort(3)
lista.insertion_sort(3)
lista.insertion_sort(600)
lista.insert_index(500, 4)
lista.insert_index(523234, 4)
lista.insert_index(500, 1)
lista.insert_index(5023340, 0)

lista.append(133)
lista.append(1333)
lista.append(14233)
lista.display()
lista.append(40)
lista.display()
print("length: ",lista.length())
print(lista.get_index(1))
lista.sort_with_temparray()
lista.delete(0)
lista.display()