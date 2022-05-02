import math
x=input("enter x:")
op=input()
if op=="radical":
    result=(math.sqrt(x))
if op=="sin":
    result=math.sin(math.radians(x))  
if op=="cos":
    result=math.cos(math.radians(x))
if op=="cot":
    result=math.cot(math.radians(x))
if op=="factorial":
    result=math.factorial(x)
print(result)