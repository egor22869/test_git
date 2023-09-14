number = input()

n2 = number.split()

chet = 0
notchet = 0

for i in n2:
    if int(i) % 2 == 0:
        chet += 1
    else:
        notchet += 1
if chet == notchet:
    print("equal")
elif chet > notchet:
    print("even")
else:
    print("odd")

