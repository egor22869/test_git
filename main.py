n, number = input(), []
number.append(n)

def removing_spacec():
    for item in number:
        items_strip = item.replace(" ", "")

    for i in items_strip:
        if int(i) % 2 == 0:
            print(i)
            break
removing_spacec()



