list = [1,2,3,4,6,9,0,6,15,36,12]
sum = 0
for item in list:
    sum +=item

print(list)
print(sum)

avg = sum/len(list)
print(avg)

list.sort()
print(list)

print("The smallest value is: ", list[0])
print("The biggest value is: ", list[-1])