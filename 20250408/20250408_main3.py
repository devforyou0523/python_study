#2581번(수정필요)
first_input_number = int(input())
second_input_number = int(input())
prime_number_list = []

if first_input_number ==  second_input_number:
    print(-1)
else:
    if first_input_number == 0:
        prime_number_list.append(1)
    for number in range(first_input_number, second_input_number +1):
        for i in range (2, number):
            if number % i == 0:
                break
            elif i+1 == number:
                prime_number_list.append(number)
                break
    if len(prime_number_list) == 0:
        print(-1)
    else:
        print(sum(prime_number_list))
        print(min(prime_number_list))