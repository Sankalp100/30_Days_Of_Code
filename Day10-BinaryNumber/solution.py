from __future__ import print_function

num = int(input())

result = 0
max = 0

while(num):
 if num % 2 == 1:
  result+=1
  if result>max:
      max=result
 else:
  result=0

 num = num//2


print(max)