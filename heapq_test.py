import heapq

temp = []
i = 10
for val in range(5):
    heapq.heappush(temp,(-val,i))
    i +=1


print(temp)

heapq.heappush(temp,(-4,16))
print(temp)

print(heapq.heappop(temp))

print(temp)


temp = []
i = 10
for val in range(5):
    heapq.heappush(temp,-val)
    i +=1


print(temp)

heapq.heappush(temp,-4)
print(temp)

print(heapq.heappop(temp))

print(temp)




"""
Press ENTER or type command to continue
[(-4, 14), (-3, 13), (-1, 11), (0, 10), (-2, 12)]
[(-4, 14), (-3, 13), (-4, 16), (0, 10), (-2, 12), (-1, 11)]
(-4, 14)
[(-4, 16), (-3, 13), (-1, 11), (0, 10), (-2, 12)]

# ssame value exisits

[-4, -3, -1, 0, -2]
[-4, -3, -4, 0, -2, -1]
-4
[-4, -3, -1, 0, -2]

"""
