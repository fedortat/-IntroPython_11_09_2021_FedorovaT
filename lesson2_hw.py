from random import randint

# 1)
value = randint(1, 300)
if value < 100:
    new_value = value / 2
else:
    new_value = - value
print(new_value)
#################################################
value = randint(1, 300)
value = int(value)
new_value = value / 2 if value < 100 else - value
print(new_value)

# 2)
value = randint(1, 300)
if value < 100:
    new_value = 1
else:
    new_value = 0
print(new_value)
#################################################
value = randint(1, 300)
value = int(value)
new_value = 1 if value < 100 else 0
print(new_value)

# 3)
value = randint(1, 300)
if value < 100:
    new_value = True
else:
    new_value = False
print(new_value)
#################################################
value = randint(1, 300)
value = int(value)
new_value = True if value < 100 else False
print(new_value)

# 4)
my_str = 'aSdF'
my_str = my_str.upper()
print(my_str)

# 5)
my_str = 'aSdF'
my_str = my_str.lower()
print(my_str)

# 6)
my_str = 'aSdF'
if len(my_str) < 5:
    print(my_str * 2)
else:
    print(my_str)
#################################################
my_str = 'aSdFgH'
if len(my_str) < 5:
    print(my_str * 2)
else:
    print(my_str)

# 7)
my_str = 'aSdF'
if len(my_str) < 5:
    print(my_str[::-1])
else:
    print(my_str)
#################################################
my_str = 'aSdFgH'
if len(my_str) < 5:
    print(my_str[::-1])
else:
    print(my_str)
