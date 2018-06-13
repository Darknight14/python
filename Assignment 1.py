
# coding: utf-8

# ## Data Types in Python
# 
# ### Int
# 
# ### Float
# 
# ### String
# 
# ### Boolean
# 
# ### List
# 
# ### Tuple
# 
# ### Set
# 
# ### Dictionary
# 

# ### Int 

# In[1]:


a = 10


# In[2]:


type(a)


# In[3]:


print(a)


# ### Float

# In[4]:


my_float = 7.5


# In[5]:


type(my_float)


# In[6]:


print(my_float)


# ### String

# In[7]:


my_string = "Python Assignment"


# In[8]:


type(my_string)


# In[9]:


print(my_string)


# ### Boolean

# In[10]:


my_bool = 5*5 > 3*9


# In[11]:


type(my_bool)


# In[12]:


print(my_bool)


# ### List
# #### Lists are mutable. Lists allow duplicate values. Elements in the Lists can be accessed using the Index. Lists are represented with [ ].  Lists have several functions

# In[13]:


my_list = [10, 20, 30, 40, 50, 20]


# In[14]:


type(my_list)


# In[15]:


print(my_list)


# In[16]:


my_list[0]


# In[17]:


my_list[-1]


# In[18]:


my_list[-1] = 60


# In[19]:


print(my_list)


# #### Fucntions of List
# #### List append() method takes single item and adds it to the end of the list. The item can be number, string, another list, dict etc. 
# #### The syntax of append() method is:
# ##### list.append(item)

# In[20]:


my_list.append(70)


# In[21]:


print(my_list)


# #### List extend() method will extend the list by adding all elements of a list that were passed as an argument to the end of the list. 
# ##### Common error: does not return the new list, just modifies the original.
# ##### Syntax: list1.extend(list2)

# In[ ]:


my_list2 = [80, 90]


# In[23]:


type(my_list2)


# In[24]:


my_list.extend(my_list2)


# In[25]:


print('Extended List is: ',my_list)


# #### Add elements of tuple and set to List

# In[26]:


tup = (100, 110)


# In[27]:


type(tup)


# In[28]:


set1 = {120, 130}


# In[29]:


type(set1)


# In[30]:


my_list.extend(tup)


# In[31]:


print("Extended List after adding Tuple: ",my_list)


# In[32]:


my_list.extend(set1)


# In[33]:


print("Extended List after adding Set: ",my_list)


# #### The native datatypes like tuple and set passed to extend() method is automatically converted to list. And, the elements of the list are appended to the end.

# #### List insert() method will insert the element to the list at a specified index. 
# ##### Syntax: list.insert(index, element)
# #### Insert() has two parameters
# ###### 1. index = position where element needs to be inserted
# ###### 2. element = this is the element to be inserted in the list

# In[38]:


my_list.insert(0, 10)


# In[39]:


print("Updated List is: ", my_list)


# ###### This function is O(n)

# ### List remove() will search for the element in the list and remove the first occurrence of the element
# #### list.remove(element)

# In[40]:


print(my_list)


# In[41]:


my_list.remove(1)


# In[42]:


print("Updated List is: ", my_list)


# In[43]:


my_list.remove(10)


# In[44]:


print("Updated List is: ", my_list)


# In[45]:


my_list.remove(5)


# ### List index() method searches an element in the list and returns its index
# ##### Syntax: list.index(element)

# In[46]:


my_list.index(60)


# In[47]:


my_list.index(55)


# In[48]:


print("Index of the element 40 is: ", my_list.index(40))


# #### Find index of tuple and list inside a list

# In[50]:


random = ['a', ('a', 'b'), [3, 4]]


# In[51]:


print(" Index of the Tuple ('a', 'b') is :", random.index(('a', 'b'))) 


# In[52]:


print(" Index of the List [3, 4] is :", random.index([3, 4])) 


# ### List count() method returns the number of occurrences of an element in a list.
# ##### Syntax: list.count(element)

# In[53]:


my_list.count(20)


# In[54]:


random = [1, 4, 3, 5, 3, 4, 1]


# In[55]:


random.count(4)


# ### List pop() method removes and returns the element at the given index (passed as an argument) from the list.
# ##### Syntax: list.pop(index)
# #### pop() parameter
# #### The pop() method takes a single argument (index) and removes the element present at that index from the list.
# #### If the index passed to the pop() method is not in the range, it throws IndexError: pop index out of range exception.
# #### The parameter passed to the pop() method is optional. If no parameter is passed, the default index -1 is passed as an argument which returns the last element. 
# 
# 

# In[56]:


print(my_list)


# In[57]:


my_list.pop(-1)


# In[58]:


my_list.pop(11)


# In[59]:


print(my_list)


# In[60]:


my_list.pop()


# In[63]:


my_list.pop(-9)


# In[64]:


print(my_list)


# ### List reverse() method reverses the elements of a given list
# ##### Syntax: list.reverse()
# #### reverse() doesn't take any arguments

# In[74]:


print(my_list)


# In[75]:


my_list.reverse()


# In[76]:


print("Updated List: ", my_list)


# ### List sort() method sorts the given list
# ##### Syntax: list.sort(key=..., reverse=...)
# #### Alternatively, you can also use Python's in-built function sorted() for the same purpose.
# #### sorted(list, key=..., reverse=...)
# #### Note: Simplest difference between sort() and sorted() is: sort() doesn't return any value while, sorted() returns an iterable list.
# 
# 

# In[77]:


vowels = ['e', 'a', 'u', 'o', 'i']


# In[78]:


vowels.sort()


# In[79]:


print('Sorted list:', vowels)


# In[80]:


vowels.sort(reverse=True)


# In[81]:


print('Sorted list:', vowels)


# In[82]:


sorted(vowels, reverse = True)


# In[83]:


sorted(vowels, reverse = False)


# ### List copy() method returns a shallow copy of the list
# #### A list can be copied with = operator.

# In[84]:


print(my_list)


# In[85]:


new_list = my_list


# In[86]:


print(new_list)


# #### The problem with copying the list in this way is that if you modify the new_list, the old_list is also modified.

# In[87]:


new_list.append(10)


# In[89]:


print("New List: ", new_list)
print("Old List: ", my_list)


# #### if you need the original list unchanged when the new list is modified, you can use copy() method. This is called shallow copy.
# ##### syntax: new_list = list.copy()
# 

# In[90]:


new_list = my_list.copy()


# In[91]:


new_list.remove(10)


# In[92]:


print("New List: ", new_list)
print("Old List: ", my_list)


# ### List clear() method removes all items from the list.
# ##### Syntax: list.clear()

# In[93]:


print("New List: ", new_list)
print("Old List: ", my_list)
print("Random list: ", random)
print("Vowels List: ", vowels)


# In[94]:


random.clear()
vowels.clear()


# In[95]:


print("New List: ", new_list)
print("Old List: ", my_list)
print("Random list: ", random)
print("Vowels List: ", vowels)


# In[99]:


del new_list[:]
del my_list[:]


# In[100]:


print("New List: ", new_list)
print("Old List: ", my_list)
print("Random list: ", random)
print("Vowels List: ", vowels)


# ## Tuple
# ### Tuples are immutable. Tuples allow duplicate values. Elements in the Tuples can be accessed using the Index. Tuples are represented with (). Tuples have couple of functions

# In[101]:


my_tuple = ('a', 'b', 'c', 'e', 'd', 'e')


# In[102]:


type(my_tuple)


# In[103]:


print(my_tuple)


# In[104]:


my_tuple[4]


# In[105]:


my_tuple[-1]


# ### Functions of Tuple
# 
# #### Tuple count() method returns the number of occurrences of an element in a tuple

# In[106]:


my_tuple.count('e')


# #### Tuple index() method searches an element in a tuple and returns its index.

# In[110]:


my_tuple.index('d')


# ## Sets
# 
# #### A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed). However, the set itself is mutable. We can add or remove items from it. Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.
# 
# #### A set is created by placing all the items (elements) inside curly braces {}, separated by comma or by using the built-in function set(). It can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have a mutable element, like list, set or dictionary, as its element.

# In[58]:


my_set = {1, 2, 3, 4, 5, 4, 3, 6}


# In[16]:


print(my_set)


# In[59]:


my_set1 = {6, 7, 8, 9, 10}


# In[18]:


type(my_set)
type(my_set1)


# ##### Creating an empty Set
# ##### Empty curly braces {} will make an empty dictionary in Python. To make a set without any elements, use the set() function without any argument.
# 
# 

# In[115]:


a = {}


# In[116]:


type(a)


# In[119]:


a = set()


# In[120]:


type(a)


# #### Set add() method adds a given element to a set. If the element is already present, it doesn't add any element.

# In[121]:


my_set.add(4)


# In[38]:


my_set.add(7)


# In[20]:


print("Updated Set is: ", my_set)


# #### Set remove() method searches for the given element in the set and removes it.

# In[124]:


my_set.remove(7)


# In[125]:


print("Updated Set is: ", my_set)


# In[126]:


my_set.remove(9)


# ### Set copy
# #### if you need the original set unchanged when the new set is modified, you can use copy() method. This is called shallow copy.
# ##### Syntax: set.copy()

# In[127]:


new_set = my_set.copy()


# In[128]:


type(new_set)


# In[129]:


print(new_set)


# In[130]:


new_set.add(7)


# In[132]:


print(new_set)
print(my_set)


# #### If you want to use = operator for shallow copy a set, you can use set().

# In[135]:


new_set = set(my_set)


# In[136]:


print(new_set)
print(my_set)


# In[137]:


new_set.add(7)


# In[138]:


print(new_set)
print(my_set)


# ### Set clear() method will clear he elements in the set
# ##### Syntax: set.clear()

# In[139]:


new_set.clear()


# In[141]:


print("After Clear", new_set)


# ### Set difference() method returns the set difference of two sets
# ##### Syntax: A.difference(B)

# In[142]:


print(my_set)
print(my_set1)


# In[143]:


my_set.difference(my_set1)


# In[144]:


my_set1.difference(my_set)


# In[145]:


print(my_set - my_set1)


# In[146]:


print(my_set1 - my_set)


# #### Set difference_update()
# #### The difference_update() updates the set calling difference_update() method with the difference of sets.
# ##### Syntax: A.difference_update(B)
# #### Here, A and B are two sets. The difference_update() updates set A with the set difference of A-B.

# In[147]:


my_set.difference_update(my_set1)


# In[148]:


print("Result of difference update is: ", my_set.difference_update(my_set1))


# ### Set discard() method removes a specified element from the set (if present).
# ##### Syntax: set.discard(ele)

# In[149]:


my_set1.discard(10)


# In[150]:


print(my_set1)


# ### Set intersection() method returns a new set with elements that are common to all sets.
# ##### Syntax: A.intersection(*other_sets)

# In[153]:


print(my_set)
print(my_set1)


# In[154]:


my_set.add(6)


# In[61]:


my_set.add(7)


# In[62]:


print(my_set)
print(my_set1)


# In[63]:


my_set.intersection(my_set1)


# In[64]:


my_set1.intersection(my_set)


# In[159]:


print(my_set & my_set1)


# #### Set intersection_update() updates the set calling intersection_update() method with the intersection of sets.
# ##### Syntax: A.intersection_update(*other_sets)

# In[21]:


print(my_set)
print(my_set1)


# In[8]:


new_set = {9, 10, 11, 12}


# In[22]:


print("The intersection update of the two is: ", my_set1.intersection_update(my_set1))
print(my_set)
print(my_set1)
#print(new_set)


# #### Set isdisjoint() method returns True if two sets are disjoint sets. If not, it returns False.
# #### Two sets are said to be disjoint sets if they have no common elements.
# ##### Syntax: set_a.isdisjoint(set_b)

# In[23]:


my_set.isdisjoint(my_set1)


# In[24]:


my_set.isdisjoint(new_set)


# In[25]:


print(my_set)
print(my_set1)
print(new_set)


# #### Set issubset() method returns True if all elements of a set are present in another set (passed as an argument). If not, it returns False.
# ##### Syntax: A.issubset(B)

# In[53]:


my_set2 = {4,5,6}
my_set3 = {6,7}


# In[66]:


print(my_set)
print(my_set1)
print(my_set2)
print(my_set3)
print(new_set)


# In[69]:


print(my_set3.issubset(my_set))
print(my_set2.issubset(my_set))
print(my_set.issubset(my_set1))
print(new_set.issubset(my_set1))


# #### Set pop() method removes an arbitrary element from the set and returns the element removed. The pop() method doesn't take any arguments.
# #### The pop() method returns an arbitrary (random) element from the set. Also, the set is updated and will not contain the element (which is returned).

# In[70]:


my_set3.pop()


# In[71]:


print(my_set3)


# In[72]:


print(my_set2)


# In[73]:


my_set2.pop()


# In[74]:


print(my_set2)


# In[75]:


print(my_set1)
my_set1.pop()
print(my_set1)


# #### Set symmetric_difference() returns a new set which is the symmetric difference of two sets. The symmetric difference of two sets A and B is the set of elements which are in either of the sets A or B but not in both.
# ##### Syntax: A.symmetric_difference(B)
# 

# In[76]:


print(my_set)
print(my_set1)
print(my_set2)
print(my_set3)
print(new_set)


# In[77]:


print(my_set.symmetric_difference(my_set1))
print(my_set1.symmetric_difference(my_set2))
print(my_set2.symmetric_difference(my_set3))
print(my_set3.symmetric_difference(my_set1))
print(new_set.symmetric_difference(my_set1))


# In[78]:


print( my_set ^ my_set1)


# #### Set  symmetric_difference_update() method updates the set calling the symmetric_difference_update() with the symmetric difference of sets.
# ##### Syntax: A.symmetric_difference_update(B)

# In[ ]:


print(my_set)
print(my_set1)
print(my_set2)
print(my_set3)
print(new_set)


# In[80]:


print(my_set3)
print(new_set)
print(my_set3.symmetric_difference_update(new_set))


# #### Set union() method returns a new set with distinct elements from all the sets.
# ##### Syntax: A.union(*other_sets)

# In[81]:


print(my_set)
print(my_set1)
print(my_set2)
print(my_set3)
print(new_set)


# In[82]:


print(my_set2.union(my_set3))


# In[83]:


print(my_set|new_set)


# #### Set update() adds elements from a set (passed as an argument) to the set (calling the update() method).
# ##### Syntax: A.update(B)

# In[84]:


print(my_set3)
print(my_set3.update(my_set2))
print(my_set3)


# ## Dictionary
# #### It is a key, value pair mapping. Unique Keys are mapped to the values. Use {} curly brackets to construct the dictionary, and [] square brackets to index it.Dictionaries are mutable. Dictionaries are unordered, so the order that the keys are added doesn't necessarily reflect what order they may be reported back. Dictionaries are optimized to retrieve values when the key is known.
# 
# ##### Syntax: dict = {Key1: value1, key2: value2,.... }

# In[87]:


my_dict = {'name':'Jack', 'age': 26}


# In[88]:


type(my_dict)


# In[89]:


print(my_dict['name'])


# In[90]:


print(my_dict['age'])


# ### The functions of Dictionary
# 
# #### Copy
# #### copy() method returns a shallow copy of the dictionary.
# ##### Syntax: dict.copy()

# In[91]:


new_dict = my_dict.copy()


# In[92]:



print('Orignal: ', my_dict)
print('New: ', new_dict)


# #### Dict fromKeys() method creates a new dictionary from the given sequence of elements with a value provided by the user. 
# 
# ##### Syntax: dictionary.fromkeys(sequence[, value])
# 
# #### The fromkeys() method takes two parameters:
# #### sequence - sequence of elements which is to be used as keys for the new dictionary
# #### value (Optional) - value which is set to each each element of the dictionary
# 

# #### Create a dictionary from a sequence of keys

# In[93]:


keys = {'a', 'e', 'i', 'o', 'u' }


# In[95]:


vowels = dict.fromkeys(keys)


# In[96]:


print(vowels)


# In[97]:


type(vowels)


# #### Create a dictionary from a sequence of keys with value

# In[98]:


value = 'vowel'


# In[100]:


vowels = dict.fromkeys(keys, value)


# In[101]:


print(vowels)


# #### Create a dictionary from mutable object list

# In[102]:


value = [1]


# In[103]:


vowels = dict.fromkeys(keys, value)
print(vowels)


# In[104]:


# updating the value
value.append(2)
print(vowels)


# #### Dict get() method returns the value for the specified key if key is in dictionary.
# ##### Syntax: dict.get(key[, value]) 
# #### The get() method takes maximum of two parameters:
# #### key - key to be searched in the dictionary
# #### value (optional) - Value to be returned if the key is not found. The default value is None.

# ##### How get() works for dictionaries?

# In[105]:


person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))
print('Age: ', person.get('age'))


# In[106]:


# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 0.0))


# ##### Python get() method Vs dict[key] to Access Elements
# ##### The get() method returns a default value if the key is missing.
# ##### However, if the key is not found when you use dict[key], KeyError exception is raised.

# #### Dict items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
# ##### Syntax: dictionary.items()
# 

# In[107]:


print(person.items())


# In[108]:


del[person['name']]


# In[109]:


print(person.items())


# ### Dict keys() method returns a view object that displays a list of all the keys in the dictionary
# ##### Syntax: dict.keys()

# In[110]:


person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print(person.keys())


# In[111]:


empty_dict = {}
print(empty_dict.keys())


# ### Dict popitem() returns and removes an arbitrary element (key, value) pair from the dictionary.
# ##### Syntax: dict.popitem()

# In[115]:


person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}


# In[116]:


print(person)
result = person.popitem()
print(person)
print(result)


# #### Dict setdefault() method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
# ##### Syntax: dict.setdefault(key[, default_value])
# #### The setdefault() takes maximum of two parameters:
# #### key - key to be searched in the dictionary
# #### default_value (optional) - key with a value default_value is inserted to the dictionary if key is not in the dictionary.
# #### If not provided, the default_value will be None.

# In[117]:


person = {'name': 'Phill', 'age': 22}


# In[118]:


age = person.setdefault('age')


# In[119]:


print('person = ',person)
print('Age = ',age)


# #### Dict pop() method removes and returns an element from a dictionary having the given key.
# ##### Syntax: dictionary.pop(key[, default])
# ##### key - key which is to be searched for removal
# ##### default - value which is to be returned when the key is not in the dictionary
# 

# In[120]:


sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('apple')
print('The popped element is:', element)
print('The dictionary is:', sales)


# #### Dict values() method returns a view object that displays a list of all the values in the dictionary.
# ##### Syntax: dictionary.values()

# In[122]:


print(sales.values())


# #### Dict update() method updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs. The update() method adds element(s) to the dictionary if the key is not in the dictionary. If the key is in the dictionary, it updates the key with the new value.
# ##### Syntax: dict.update([other])
# ##### The update() method takes either a dictionary or an iterable object of key/value pairs (generally tuples).
# 

# In[123]:


d = {1: "one", 2: "three"}
d1 = {2: "two"}


# In[124]:


# updates the value of key 2
d.update(d1)
print(d)


# In[125]:


d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d)


# In[126]:


d = {'x': 2}


# In[127]:


d.update(y = 3, z = 0)
print(d)


# ## End of Assignment 1
