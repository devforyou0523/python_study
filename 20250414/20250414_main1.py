#2753번 (수정필요)
input_number = int(input())
if ((input_number % 4 == 0 and input_number%100 != 0) or (input_number % 400 == 0)):
    print ("1")
else:
    print("0")