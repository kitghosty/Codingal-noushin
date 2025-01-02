# //////////datatype

# Numeric types
num1 = 10   # int
num2 = 20.5 #float

#Sequence types
text = "Hello, Python!" #str
fruits = ["apple", "banana", "cherry"] #list / array

# Mapping type
student_info = {"name": "Alex", "age": 21} #dict / obj

#Boolean type
is_python_fun = True #bool

#Print the data types
print(type(num1))  # Output: <class 'int'>
print(type(text))  # Output: <class 'str'>
print(type(student_info)) # Output: <class 'dict'>

# Arithmatic operators
a = 10
b = 3
print("Addition:", a + b)     # Output: Addition: 13
print("Substraction:", a - b) # Output: Substraction: 7
print("Multiplication:", a * b) # Output: Multiplication 30
print("Division:", a / b)     # Output: Division 3.3333333333333335
print("Modulus:", a % b)     # Output: Modulus: 1

# Comparison operators
print("Is a equal to b?", a == b) # Output: False
print("Is a greater than b?", a > b) # Output: True
print("Is a smaller than b?", a < b) # Output: False

# Logical operators
x = True
y = False
print("x and y", x and y) # Output: False
print("x or y", x or y) # Output: True
print("not x" , not x) # Output: False
print("not y", not y) # Output: True

# Assignment operators
c = 5
c += 2 # same as c = c + 2
print("c after += 2:", c) # Output: 7

# Operation on strings

#Concatenation
str1 = "Hello"
str2 = "World"
combined = str1 + " " + str2
print("Concatenated string:", combined) # Output: Hello World

# Repititon
repeated = str1 * 3
print("Repeated string:", repeated) # Output: HelloHelloHello

# Slicing
slice_str = combined[0:5] # Gets the substirng "Hello"
print("Sliced string:", slice_str)

#Methods
upper_str = str1.upper() #Converts to "HELLO"
print("Upper case string:", upper_str)

lower_str = str2.lower() # Converts to "world"
print("Lower case string:", lower_str)

#String length
print("Length of combined stirng:", len(combined)) # Output: 11


# // inputs
print("hello welcome to codingal")
name = input("what is your name? ")
print("hello", name)