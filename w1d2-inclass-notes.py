#truthy / falsy

x = [0]

falsy = [0, False, "", [], (), {}, set(), None]

if falsy:
    print("there are values in the list")
else:
    print("list is empty")

def isTrue() -> int: 
    return 1

if isTrue():
    print("True")
else:
    print("false")

###########

#ternary operator

val = 0
if x:
    val = 1
else:
    val = 0

value = 1 if len(x) > 1 else 0
print(value)

###########

# walrus operator
nums = [0,1,2,4,6,7,7,81,12]
length = len(nums)
if (n := len(nums)) > 10:
    print("long list")
else:
    print("list is good")

###########

# match case

point = (5, 0)

match point:
    case (0, 0):
        print("origin")
    case (_, 0):
        print("x-axis")
    case (0, _):
        print("y-axis")
    case _:
        print("something else")



#enumerate

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# print(f"f{index} - {fruit}")

for i in range(len(fruits)):
    print(f"{i} - {fruits[i]}")

i = 0
for fruit in fruits:
    print(f"{i} - {fruits[i]}")
    i+=1

for i, fruit in enumerate(fruits):
    print(f"{i} - {fruit}")

################################

# zip

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "orange"]

prices = [0.99, 0.59, 2.99, 1.49, 3.99, 2.49, 2.99, 3.49, 1.99, 0.89]

menu = dict(zip(fruits, prices))

for fruit, price in zip(fruits, prices):
    print(f"{fruit} - ${price}")

################################

#for...else
for i in prices:
    if i == 4.00:
        break
else:
    print("no price 4.00")

################################################################
################################################################

integers = [5, 12, 7, 3, 9, 15, 8, 1, 6, 11]

squares = [i*i for i in integers]
even_squares = [i*i if i % 2 == 0 else i for i in integers]

print(even_squares)

squares = {i: i*i for i in integers if i % 2 == 0}
print(squares)

################################################################

#all()
#any()

nums = [2,4,7]
isEven = all(n % 2 == 0 for n in nums)
print(isEven)

nums = [3,1,7]
isOneEven = any(n % 2 == 0 for n in nums)
print(isOneEven)

#sorted()

grade_dict = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "David", "grade": 88},
    {"name": "Eva", "grade": 90},
    {"name": "Frank", "grade": 95},
    {"name": "Grace", "grade": 80},
    {"name": "Hannah", "grade": 84},
    {"name": "Ivy", "grade": 91},
    {"name": "Jack", "grade": 87}
]

students = sorted(grade_dict, key=lambda s: s['grade'])

## DO RESEARCH ON THIS VERY USEFUL
## IMPLEMENTS TIMSORT UNDER THE HOOD: 
    # https://www.geeksforgeeks.org/dsa/timsort/

# 1. Lambda for sorting strings by length
sort_by_length = lambda s: len(s)

# 2. Lambda for sorting numbers in descending order
sort_descending = lambda x: -x

# 3. Lambda for sorting tuples by the second element
sort_by_second = lambda t: t[1]

# 4. Lambda for sorting dictionaries by a specific key
sort_by_key = lambda d, key: d[key]

# 5. Lambda for sorting strings case-insensitively
sort_case_insensitive = lambda s: s.lower()

