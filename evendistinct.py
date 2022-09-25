from collections import Counter

def unique(list1):

    print(*Counter(list1))


list1 = [11, 25, 12, 42, 42]
print("the distinct values from 1st list is")
unique(list1)



list1.reverse()


if list1[0] % 2 == 0:
    print(list1[0], 'location 4')

elif list1[1] % 2 == 0:
    print(list1[1], 'location 3')

elif list1[2] % 2 == 0:
    print(list1[2], 'location 2')

elif list1[3] % 2 == 0:
    print(list1[3], 'location 1')

elif list1[4] % 2 == 0:
    print(list1[4], 'location 0')
else:
    print("0")
