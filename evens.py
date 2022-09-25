values = [1,3,3,3,5]
values.reverse()
print(values)

if values[0] % 2 == 0:
    print(values[0],'location 0')

elif values[1] % 2 == 0:
    print(values[1], 'location 1')

elif values[2] % 2 == 0:
    print(values[2], 'location 2')

elif values[3] % 2 == 0:
    print(values[3], 'location 3')

elif values[4] % 2 == 0:
    print(values[4], 'location 4')
else:
    print("0")
