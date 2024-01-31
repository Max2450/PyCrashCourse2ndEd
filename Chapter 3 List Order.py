# 3-8 list 5+ locations, print it unsorted and sorted, etc.

#unsorted original list
locations = ["Japan", "Norway", "France", "South Korea", "Iceland"]
print(locations)

#temp sorted a-z
print(sorted(locations))
print(locations)

#z-a temp sorted
print(sorted(locations, reverse=True))
print(locations)

#original list perm reversed
locations.reverse()
print(locations)
#restored original order
locations.reverse()
print(locations)

#perm sort a-z
locations.sort()
print(locations)
#perm sort z-a
locations.sort(reverse=True)
print(locations)
