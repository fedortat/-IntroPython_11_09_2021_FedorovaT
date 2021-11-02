# 1)
my_list = [3, 14, 88, 345, 130, 4, 192]
for value in my_list:
    if value > 100:
        print(value)



# 2)
my_list = [3, 14, 88, 345, 130, 4, 192]
my_results = []
for value in my_list:
    if value > 100:
        my_results.append(value)
print(my_results)

# 3)
my_list = [3, 14, 88, 345, 130, 4, 192]
my_new_list = my_list[-2:]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(sum(my_new_list))
print(my_list)

my_list = [3, 14, 88, 345, 130, 4, 192]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-2] + my_list[-1])
print(my_list)


#########################
my_list = [88]
my_new_list = my_list[-2:]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(sum(my_new_list))
print(my_list)

# 4)
my_string = '0123456789'
my_list1 = []
for symbol_1 in my_string:
    for symbol_2 in my_string:
        my_list1.append(int(symbol_1 + symbol_2))
print(my_list1)