cats = ["luna", "felix", "nina"]
print(len(cats))

#add to the end
cats.append("monet")
print(cats)
#insert in a specific position
cats.insert(1, "sativa")
print(cats)

luna_index = cats.index("luna")
print(luna_index)

#remove from the end
index_last_item = cats.pop()
print(index_last_item)
print(cats)

#remove by value
cats.remove("sativa")
print(cats)

#final index is not included
slicing = cats[0:2]
print(slicing)
cats.sort()
print(cats)

print(cats.count("luna"))

l=[1,2,3,3,2,1]
print(l[4:])
print(l[-2:])
print(l[4:6])
print(l[2:6])
