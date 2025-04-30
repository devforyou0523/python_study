#10813번(수정필요)
basket_number, input_number = map(int, input().split(" "))
last_basket = [i for i in range(1, basket_number+1) ]

for i in range (input_number):
    start_basket, end_basket, add_ball = map(int, input().split(" "))
    temp_basket = 0
    last_basket[start_basket-1] = temp_basket
    last_basket[end_basket-1] = last_basket[start_basket-1]
    last_basket[start_basket-1] = temp_basket

print(str(last_basket)[1:-1].replace(",",""))