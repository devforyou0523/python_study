#10430번
input_number = input()
a = int(input_number.split(" ")[0])
b = int(input_number.split(" ")[1])
c = int(input_number.split(" ")[2])

print("{}".format((a+b)%c))
print("{}".format(((a%c)+(b%c))%c))
print("{}".format((a*b)%c))
print("{}".format(((a%c)*(b%c))%c))