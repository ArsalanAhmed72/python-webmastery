fruits = ["apple", "orange", "pineapple"] 
print(fruits)

t_fruits = tuple(fruits)                                # CONVERTING LIST INTO TUPLE
print("---------------AFTER CONVERTING LIST INTO TUPLE----------------")  
print(t_fruits)       

l_fruits = list(t_fruits)                               # CONVERTING TUPLE INTO LIST
print("---------------AFTER CONVERTING TUPLE INTO LIST----------------") 
print(l_fruits)
l_fruits.append("pineapple")
print("---------------AFTER APPLYING APPEND OPERATION-----------------") 
print(l_fruits)
l_fruits.remove("orange")
print("---------------AFTER APPLYING REMOVE OPERATION-----------------")
print(l_fruits)
