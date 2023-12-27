#This is a comment, just use hashtag
names= ["John", "Juan", "Harry", "Metro", "Booming"]
print(names)

#Append adds a value to the end of the list
names.append("Draco")
print(names)

#Sorts in alphabetical order
names.sort()
print(names)

#Create empty set
s=set()

#Add elements
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)
#Remove
s.remove(3)
print(s)
print(f"The set has {len(s)} elements")