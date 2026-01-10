#print message
x="This is python"
print(x)

#Add two numbers
num1=input("enter value of A:")
num2=input("enter value of B:")
sum_result= int (num1)+ int(num2)
print("The sum is:",sum_result)

#Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

    #check leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.") 
else:
    print(f"{year} is not a leap year.") 


#store and print constant value
SPEED_OF_LIGHT = 299792458
PI = 3.14159
MAX_VALUE = 100
print(SPEED_OF_LIGHT)
print(PI)
print(MAX_VALUE)

#square of a number
num = float(input("Enter a number: "))  
square = num ** 2                       
print(f"Square: {square}")    

#area of circle
import math
radius = float(input("Enter the radius: "))
area = math.pi * radius ** 2  
print(f"Area of the circle: {area:.2f}")

#check data type
num = 42
text = "hello"
print(type(num)) 
print(type(text)) 

#math function
import math
print(math.pi)       
print(math.sqrt(16))  
print(math.sin(math.pi / 2))  

#power
base = float(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print(base ** exponent) 

#positive or negative
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")  
elif num < 0:
    print("Negative") 
else:
    print("Zero")

    #print PI Value
    import math
print(math.pi)