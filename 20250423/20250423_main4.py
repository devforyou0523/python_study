#2439번
input_number = int(input())
blank_number = input_number-1

for i in range(input_number):
        print(f"{" "*blank_number}{"*"*(i+1)}")
        blank_number -= 1