#1330번
input_number = input()
a, b = map(int, input_number.split(" "))

if (a>b):
    print(">")
elif (a<b):
    print("<")
elif (a==b):
    print("==")