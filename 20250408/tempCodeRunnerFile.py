for number in range(first_input_number, second_input_number +1):
    for i in range (2, number):
        if number % i == 0:
            break
        elif i == number:
            prime_number_list.append(number)
            break
if len(prime_number_list) == 0:
    print(-1)
else:
    print(sum(prime_number_list))
    print(min(prime_number_list))