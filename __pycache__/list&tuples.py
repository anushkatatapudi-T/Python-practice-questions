# # #qno1
# #1. Why can you do my_list[0] = 99 but not my_tuple[0] = 99? What's actually different in
# # memory?
# # #1. Why can you do my_list[0] = 99 but not my_tuple[0] = 99? What's actually different in
# # # memory?
# # #the differnce isn't storing list adn tuples stored in different memory , both this are object stored ina memory and also list is mutable(means you  can change their elements after creation also) but in immutable(you cannot change the elements onces it is created)

# # #qno2
# #2. a = [1, 2, 3]; b = a; b.append(4) — what is a now? Contrast with b = a.copy()
a = [1,2,3];b=a;b.append(4) #now the a has [1,2,3] ,b will become a,append means it add the data at the end of the list means now a will become[1,2,3,4]
b = a.copy() #which means the values of a will be stored in b
print(a)
print(b)

# # qno 3
# #3. What's a shallow copy problem? a = [[1,2],[3,4]]; b = a.copy(); b[0][0] = 99 — does a
# # change too? Why?
# # A shallow copy creates a new outer object.
# # But the nested objects (lists, dictionaries, etc.)
# # are still shared between the original and the copy.
# # Therefore, modifying a nested object through either
# # the original or the copied object affects both.
a = [[1,2],[3,4]]
b = a.copy()
b[0][0] = 99
print(a)
print(b)
# # a.copy() only copies the outer list.
# # The inner lists are shared between 'a' and 'b'.
# # So, changing b[0][0] also changes a[0][0].

# #qno 4
# 4. [1, 2, 3] + [4, 5] vs [1, 2, 3] * 2 — what do these do to a list (not numbers)?
a = [1,2,3] + [4,5] # to list + means joins or concatenates the two list in order 
b=[1,2,3] * 2 # to list * means it repeats entire lsit in number of given times [1,2,3] * 2 means 1,2,3,1,2,3
print(a,b)

# #qno 5
# #. Can a tuple contain a list? If so, can you still "mutate" the tuple indirectly? (t = (1, [2, 3]),
# # then t[1].append(4))
# # t = (1, [2, 3])
# # t[1].append(4)
# # As we know, a tuple is immutable. However, a tuple can contain a list.
# # We cannot replace or remove the elements of a tuple.
# # Here, t[1] refers to a list, which is mutable.
# # So, append() modifies the list inside the tuple, not the tuple itself.
# # print(t)

# #qno 6 
#6. When would you deliberately choose a tuple over a list, beyond "it's faster"?
#i would choose a tuple when the data should not changed after it is created 
#examples are :
#storing a dob
#storing a phone number
#storing a roll no
#storing a password

# #qno 7
number = [1,2,3,2,1,3,4]
result =[]
val = set()
for num in number :
    if num not in val :
        result.append(num)
        val.add(num)
print(result)        

# # qno 8
number = [4,6,3,9]
largest =float("-inf")
second_largest =float("-inf")
for num in number :
    if num > largest :
        second_largest = largest
        largest = num
    elif num >second_largest and num != largest :
        second_largest=num
print("largest:",largest)
print("second_largest :",second_largest)

# #qno 9
nested = [[1,2],[3,4],[5]]
result =[]
for sublist in nested :
    for item in sublist :
        result.append(item)
print(result)

# #qno 10
given = [1,2,3,4,5]
k = 2
print(given[-k:] + given[:-k])

#qno 11
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list
print(add_item(1))
print(add_item(2))
#questions
# 7.Remove duplicates while preserving order — given 
# [1,3,2,3,1,4] , output 
# [1,3,2,4] . (Hint: a set alone won't preserve order — think about what data
# structure tracks "have I seen this?" while you build a new list.)

# 8.Find the second-largest number in a list without sorting it and without using 
# twice in an obvious way. Try to do it in one pass.

# 9.Flatten a nested list:  [[1,2],[3,4],[5]] →[1,2,3,4,5] 

# 10.Rotate a list by :
# k positions: 
# [1,2,3,4,5] rotated by 2 → 
# slicing, in one line.

# 11.Tricky — the mutable default trap: Predict, then run:
# def add_item(item, my_list=[]):
# my_list.append(item)
# return my_list
# max()
# [4,5,1,2,3] . Do it with
# print(add_item(1))
# print(add_item(2))
# Does the second call start fresh, or does it remember the first call? Figure out *why*
# before running it (hint: relates directly to what we discussed about references — a default
# # argument is only evaluated *once*, at function definition time).