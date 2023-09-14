n = int(input())
total = []

for i in range(n):
    number = int(input())
    if number % 10 == 3:
        total.append(number)
print(min(total))
