# there is an inbuilt function named heapq in the python
# heapify :- converts regular heap into the heap
# heappush :- add the elemen to the heap without altering the orignal heap
# heappop:-  returns the smallest funtion from the heap
# heapreplace :- replace the smallest element with new value supplied


import heapq
H = [21,1,35,67,89,32,14,456]

heapq.heapify(H)
print (H)
# Add an element

heapq.heappush(H,3)
print(H)

#removing element from the heap

heapq.heappop(H)
print(H)

#replacing the element inside the heap

heapq.heapreplace(H,6)
print(H)