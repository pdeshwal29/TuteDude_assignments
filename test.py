#!/usr/bin/env python3

print("hello, this is me")


list = [1,2,3,4, 66, 99, 73]

for i in list:
    if i%2==0:
        print("even number", i)
    else:
        print("odd nuner", i)


list=['rohit', 'preeti', 'nisha', 'ruben']

for i in list:
    if i.startswith('r'):
        print(i)


x=3
y=4
print(3+4)
print(3*4)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


number=0
for i in range(1,11):
    sum=number+i
    print("current number:", i, "previous number:", number, "sum:", sum)
    number=i



child1={
    "name":"rohit",
    "age":31
}
child2={
    "name":"preeti",
    "age":29
}

myfamily={
    "child1":child1,
    "child2":child2
    
}

print(myfamily)


i=0
while i<=10:
    print(i)
    i +=1

s=0
n=int(input("enter a number:"))
for x in range(1, n+1, 1):
    s+=x
print("\n")
print("sum is",s)

n=2
for i in range(1, 11, 1):
    product=n*i
    print(product)

print("\n")

def fahrenheit_to_celsius(f):
  return (f - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))