num = int(input())

phoneBook = {}

for i in range(0, num):
    entry = str(input()).split(" ")

    name = entry[0]
    phone = int(entry[1])
    phoneBook[name] = phone

for j in range(0, num):
    name = str(input())

    if name in phoneBook:
        phone = phoneBook[name]
        print(name + "=" + str(phone))
    else:
        print("Not found")