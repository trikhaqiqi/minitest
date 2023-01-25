my_list = []

for i in range(1, 100):
    my_list.append(i)

# print(my_list) # 👉️ [1 s/d 100]

kosong = []
for number in my_list:
    if number % 3 == 0 and number % 5 == 0:
        kosong.append("ApaBole")
    elif number % 3 == 0:
        # print("even")
        kosong.append("Apa")
    elif number % 5 == 0:
        kosong.append("Bole")
    else:
        # print(number)
        kosong.append(number)

print(kosong)