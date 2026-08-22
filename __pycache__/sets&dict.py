#Word frequency counter: Given a sentence string, build a dictionary mapping each
# word to how many times it appears.
s = input("enter :")
value = s.split()
count = {}
for word in value :
    if word not in count:
        count[word]=1
    else :
        count[word]= count[word] + 1
print(count)   

# Find common elements between two lists using sets, without loops.
a = [1,2,4,6,7]
b = [1,2,5,9,7]
print(set(a) & set(b))    

#invert a dictionary: 
# {"a": 1, "b": 2} → 
# two keys originally had the same value?
# {1: "a", 2: "b"} . What would go wrong if
a = {'a':1,'b':2}
b ={}
for key in a :
    b[a[key]] = key
print(b) 

# one key pair is lost because the duplicated key is inverted dictionary so it overwrites the previous one("a")
a = ["eat", "tea", "tan", "ate", "nat", "bat"]
all = {}
for word in a :
    key = "".join(sorted(word)) 
    if key not in all :
        all[key] = [word]
    else :
        all[key].append(word)
print(all)    

#tricky: Why does this crash, and how do you fix it?
# counts = {}
# for word in ["a", "b", "a", "c"]:
# counts[word] += 1

# solution
counts = {}
for word in ["a", "b", "a", "c"]:
    if word not in counts:
        counts[word] = 1
    else :
        counts[word] += 1   
print(counts)
  
 
# # {1, 2, 2, 3, 3, 3} — what does this evaluate to? Why are sets useful for deduplication?
# # sets are useful because it removes the duplicate values also it only store the non repeated value/or we can say repeated values i automatically remove the duplicates
# # example
a =  {1, 2, 2, 3, 3, 3}
print(a)# in this it remove the repeated number in dictionary

#Can a set contain a list? Why or why not? Can it contain a tuple?
#No a set cannot contain , since set only store immutable objects in list it contains muttable so you cannot add list in a set(objects can change(not hashable))
#yes , a set can contain tuple , because a set store immutable adn also a tuple store immutable and its hashable(objects cannot change)
d = {"a": 1, "b": 2} #Using square brackets [] means Python expects the key to exist. If the key is missing, Python raises a KeyError and the program stops unless you handle the error.
print(d.get("c")) #get() checks whether the key exists in the dictionary. If the key exists, it returns its value. If the key does not exist, it returns None by default instead of giving an error.
 
#Are dictionaries ordered in Python 3.7+? Does that mean they're sorted?
# Yes. From Python 3.7 onward,
#  dictionaries preserve the insertion order
#  of key-value pairs. However,
#  they are not sorted automatically. 
# They keep items in the order they were added, not in alphabetical or numerical order.

a = [1,2,3,4]
b = [2,3,4,5,6]
print(set(a)&set(b)) #Intersection returns the elements that are common in both sets.(interaction)
print(set(a)|set(b)) #Union combines all unique elements from both sets. Duplicate values appear only once.
print(set(a)-set(b)) #Difference returns the elements that are present in the first set but not in the second set.
print(set(a)^set(b)) #Symmetric difference returns the elements that are present in either set, but not in both. In other words, it excludes the common elements.

#Can dictionary keys be a list? Why not — what property must a key have?
#no a list cannot contain dictionary key
#because list are muttable means it can chnage after it is created
#a key shouldbe must hashable means (immutable) which cannot chnage after  it is created