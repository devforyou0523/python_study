#10951번
input_case = ""

while (True):
    try:
        input_case = input()
        a, b  = map(int, input_case.split(" "))
    except EOFError:
        break
    print(a+b)