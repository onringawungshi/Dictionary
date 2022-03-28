# Python Dictionary is used to store the data in a key-value pair format.

# Dictionary comprehension is a method for transforming one dictionary into another dictionary. 

# 1.Keys must be a single element
# 2.Value can be any type such as list, tuple, integer, etc.

# The dictionary can be created by using 
# multiple key-value pairs enclosed with the curly brackets {}, 
# and each key is separated from its value by the colon (:).

# Syntax:Dict = {"Name": "Tom", "Age": 22}  

# Python provides the built-in function dict() method which is also used to create dictionary.
# The empty curly braces {} is used to create empty dictionary.

# Properties of Dictionary keys

# 1. In the dictionary, we cannot store multiple values for the same keys.
# If we pass more than one value for a single key,
# then the value which is last assigned is considered as the value of the key.

# Dictionary functions:
# 1 cmp(dict1, dict2) :-It compares the items of both the dictionary and returns true 
#                    if the first dictionary values are greater than the second dictionary, 
#                   otherwise it returns false.
# 2 len(dict) :-	It is used to calculate the length of the dictionary.
# 3 str(dict) :-	It converts the dictionary into the printable string representation.
# 4 type(variable) :-	It is used to print the type of the passed variable.

# Methods:

# 1 dic.clear() :-	It is used to delete all the items of the dictionary.
# 2 dict.copy() :-	It returns a shallow copy of the dictionary.
# 3 dict.fromkeys(iterable, value = None, /) :-	Create a new dictionary from the iterable with the values equal to value.
# 4 dict.get(key, default = "None") :-	It is used to get the value specified for the passed key.
# 5 dict.has_key(key) :-	It returns true if the dictionary contains the specified key.
# 6 dict.items() :-	It returns all the key-value pairs as a tuple.
# 7 dict.keys() :-	It returns all the keys of the dictionary.
# 8 dict.setdefault(key,default= "None") :-	It is used to set the key to the default value if the key is not specified in the dictionary
# 9 dict.update(dict2):- 	It updates the dictionary by adding the key-value pair of dict2 to this dictionary.
# 10 dict.values() :-	It returns all the values of the dictionary.
# 11 len() 	:-used to calculate the len of the list.
# 12 popItem():- The popitem() removes the arbitrary element from a dictionary,
#      The popitem() method removes the last inserted item
# 13 clear() :- method removes all elements to the whole dictionary. 	
# 13 pop() :-The pop() method accepts the key as an argument and remove the associated value.	
# 14 count() :-	
# 15 index() :-

# dict={"name":"onring","age":22,"plce":"bangalore"}
# r=dict["plce"]
# s=dict.get("age")
# print(r)
# print(s)
# print(dict["name"])

# d={"state":"manipur","village":"phungyar","flower":"rose","singer":"yungyung"}
# x=d.get("state")
# r=d["flower"]
# a=d["village"]
# print(x)
# print(d["singer"])
# print(r)
# print(a)


# lis=dict(name="onring",location="navgurukul",city="bangalore")
# print(lis)


# a=dict(name="onring",place="manipur",age=23)
# x=a.get("age")
# b=a["place"]
# print(a["name"])
# print(x)
# print(b)


# dic={"name":"onring","place":"bangalore"}
# dic["car brand"]="bugatti"
# dic["flower"]="rose"
# print(dic)

# a={"name":"onring","age":12}
# b=a.get("flower")
# print(b)


# a={"name":"onring","age":12}
# a["s"]={"clor":"black","p":"pen"}
# print(a)


# dic={"name":"onring","age":67,"car":"honda"}
# if "car" in dic:
#     print("yes car in the dictionary")
# else:
#     print("no car is not in the dictionary list")

# a={"name":"onring","age":12}
# b=a.copy()
# print(b)

# a={"name":"onring","place":"bangalore","food":"pizza"}
# del a["place"]
# print(a)

# a={"name":"onring","place":"bangalore","food":"pizza"}
# a.popitem()
# print(a)

# a={"name":"onring","place":"bangalore","food":"pizza"}
# a.pop("name")
# print(a)


# students_rolls={"onring":12,"manori":32,"ning":1,"sem":13,"ktm":30}
# for students in students_rolls:
#     print(students_rolls[students])
  
    
# students_rolls={"onring":12,"manori":32,"ning":1,"sem":13,"ktm":30}
# for students in students_rolls:
#     print(students)


# students_rolls={"onring":12,"manori":32,"ning":1,"sem":13,"ktm":30}
# for students,rolls in students_rolls.items():
#     print(students,rolls)

