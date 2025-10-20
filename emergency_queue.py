class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

class MinHeap:
    def __init__(self):
        self.data = []
    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2

            current_task = self.data[index] 
            parent_task = self.data[parent_index]
            if current_task.urgency < parent_task.urgency:
                temp = self.data[index]
                self.data[index] = self.data[parent_index]
                self.data[parent_index] = temp
                index = parent_index
            else: 
                break
    def heapify_down(self, index):
    
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index 

        
        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left


        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right


        if smallest != index:
    
            temp = self.data[index]
            self.data[index] = self.data[smallest]
            self.data[smallest] = temp
        
            self.heapify_down(smallest)
	
    def insert(self, task):
        self.data.append(task) 
        self.heapify_up(len(self.data) - 1)
    
    def peek(self):
        if self.data is None:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data: 
            return None

        if len(self.data) == 1: 
            return self.data.pop()

        min_value = self.data[0] 
        self.data[0] = self.data.pop()
        self.heapify_down(0) 
        return min_value 
    
    def print_heap(self):
        print("\nCurrent Tasks")
        for task in self.data:
            print(f"-{task.name} ({task.urgency})")
    
heap = MinHeap()
heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))
next_up = heap.peek()   
print(next_up.name, next_up.urgency)
served = heap.remove_min()
print(served.name)
heap.print_heap()
"""
Why is a tree appropriate for the doctor structure?

Tree is appropriate for the doctor structure because there is an importance to the hierarchy of the doctors. They are not tasks therefore 
they are not meant to be ranked and checked off like such. A tree has a specific order in which it should be both sorted and printed. 

When might a software engineer use preorder, inorder, or postorder traversals?
A software engineer may use preorder, inorder, or postorder traversals if they are creating a system in which order matters. For instance if 
they were to create a file with certain data for an upcoming project but want multiple files allocated into one and so on from there, these 
tasks could list where each item is located in relation to its parent and the root. 

How do heaps help simulate real-time systems like emergency intake?
Heaps help to simulate real-time systems like emergency intake through its high-priority list that it creates. Through heaps it ranks the tasks 
given based on the input of the user. A heap is then able to either allow the user to look at the first task of importance or if the task is 
finished it can remove the task. A heap resets the order of the data and the process can continue. For an emergency intake someone may not know 
the level of importance each item has so a heap would be able to document or showcase just that. 
"""
