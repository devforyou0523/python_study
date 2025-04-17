#10950번
calc_number = int(input())
for i in range(calc_number):
    input_number = input()
    a,b = map(int, input_number.split(" "))
    print(a+b)