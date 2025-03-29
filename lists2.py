front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined_list= front_end + back_end #concatenation

print(joined_list) 



full_stack = joined_list.copy() #copying the list

print(full_stack)



full_stack.insert(5, "SQL") #inserting an element at a specific index
full_stack.insert(6, "Python")

print(full_stack)