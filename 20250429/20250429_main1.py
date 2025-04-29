#2562번
number_list = []

for i in range (9):
    number_list.append(int(input()))

print(f"{max(number_list)}")
print(f"{number_list.index(max(number_list))+1}")
