list1 = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j],end=" ")
    print() 

list2 = [50,40,20,40,20,60,20,80,90]
print(list2.count(20)) # count the number of times 20 appears in the list
print(list2.count(25)) # count the number of times 40 appears in the list

#Del list(index1:index2:step)

list2 = [50,40,20,40,20,60,20,80,90]
del list2[1:6:2] # delete the elements from index 1 to 6 with step 2
print(list2) # print the modified list