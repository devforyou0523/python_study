#25304번
last_cost = int(input())
list_number = int(input())
sum_cost = 0

for i in range(list_number):
    cost, amount = map(int, input().split(" "))
    sum_cost = sum_cost + (cost * amount)

if last_cost == sum_cost:
    print("Yes")
else:
    print("No")