#11022번
input_case_num = int(input())

for i in range (input_case_num):
    a, b =map(int, input().split(" "))
    print(f"Case #{i+1}: {a} + {b} = {a+b}")