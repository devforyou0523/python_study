#10810번
basket_number, input_number = map(int, input().split(" "))
last_basket = [0 for i in range(basket_number) ]

for i in range (input_number):
    start_basket, end_basket, add_ball = map(int, input().split(" "))
    last_basket[start_basket-1:end_basket] = [add_ball for i in range(end_basket-start_basket+1)]

print(str(last_basket)[1:-1].replace(",",""))