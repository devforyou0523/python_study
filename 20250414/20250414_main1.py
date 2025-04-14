input_number = float(input())

print(f"input_number/4 is {input_number / 4}")
if (input_number % 4 == 0 and input_number%100 != 0.0):
    print ("1")
elif (input_number%400 == 0.0):
    print("1")
else:
    print("0")