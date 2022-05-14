min = input("please input the minimum number of the range:")
max = input("please input the maximum number of the range:")
mul = input("please input the number that you want to skip:")
for i in range(min, max):
    if i % mul == 0:
        continue
    print(i)
