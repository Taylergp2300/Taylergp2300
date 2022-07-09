
def kaprecar2(num, index):  
    counter = num ** 2
    first_part = counter // 10**index
    second_part = counter - (first_part * 10**index)
    if (first_part + second_part) == num:
        print(num, 'is a kaprecar number')
list_of_index = [0,100,1000,10000,100000,1000000, 10000000, 100000000, 1000000000, 10000000000 ,100000000000 ,1000000000000]
to_the_power_of = [1,2,2,3,3,4,4,5,5,6,6,7]
for i in range(1,1000000):
    num = i
    for j in range(len(list_of_index)):
        if (num**2) < list_of_index[j] and (num**2) >= list_of_index[j-1]:
            index = to_the_power_of[j-1]
            kaprecar2(num, index)
