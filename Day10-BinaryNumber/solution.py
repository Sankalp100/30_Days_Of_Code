n = int(input())

result = 0
max = 0

while n > 0:
    if n % 2 == 1:
        result += 1
        if result > max:
            max = result

    else:
        result = 0

    n //= 2

print(max)