#10952번
input_case = ""

while (input_case != "0 0"):
    input_case = input()
    a, b  = map(int, input_case.split(" "))
    if(input_case == "0 0"):
        break
    print(a+b)