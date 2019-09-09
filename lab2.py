List = [] 
print("Intial blank List: ") 
print(List)

List = ["venkatesh"] 
print("\nList with the use of String: ") 
print(List)

List = ["venkatesh", "prasad"] 
print("\nList containing multiple values: ") 
print(List[0])  
print(List[1])

List = [['venkatesh', 'prasad'] , ['cse']] 
print("\nMulti-Dimensional List: ") 
print(List)

List = [1, 2, 4, 4, 3, 3, 3, 6, 5] 
print("\nList with the use of Numbers: ") 
print(List)

List = [1, 2, 'venkatesh', 4, 'prasad', 6, 'cse'] 
print("\nList with the use of Mixed Values: ") 
print(List)

List.append(1) 
List.append(2) 
List.append(4) 
print("\nList after Addition of Three elements: ") 
print(List)

for i in range(1, 4): 
    List.append(i) 
print("\nList after Addition of elements from 1-3: ") 
print(List) 
  
# Adding Tuples to the List 
List.append((5, 6)) 
print("\nList after Addition of a Tuple: ") 
print(List) 
  
# Addition of List to a List 
List2 = ['venkatesh', 'prasad'] 
List.append(List2) 
print("\nList after Addition of a List: ") 
print(List)

# specific Position 
List.insert(3, 12) 
List2.insert(0, 'cmru') 
print("\nList after performing Insert Operation: ") 
print(List) 

# to the List at the end 
List.extend([8, 'python', 'lab']) 
print("\nList after performing Extend Operation: ") 
print(List) 

print("Accessing a element from the list") 
print(List[0])  
print(List[2])

print("Acessing a element from a Multi-Dimensional list") 
print(List[0][1]) 
print(List[1][0])



List = [1, 2, 3, 4, 5, 6, 
		7, 8, 9, 10, 11, 12] 
print("Intial List: ") 
print(List) 


List.remove(5) 
List.remove(6) 
print("\nList after Removal of two elements: ") 
print(List) 


for i in range(1, 5): 
	List.remove(i) 
print("\nList after Removing a range of elements: ") 
print(List) 


List.pop() 
print("\nList after popping an element: ") 
print(List) 


List.pop(2) 
print("\nList after popping a specific element: ") 
print(List) 


