#!/usr/bin/python
total = 0
a = 1
b = 2
for i in range(1,9):
      #print(i)
    total = a + b
    a = b
    b = total
print(total)
