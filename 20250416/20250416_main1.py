#14681번
input_x = input()
input_y = input()

if (input_x >0 and input_y>0):
    print("1")
if (input_x >0 and input_y<0):   
    print("4")
if (input_x <0 and input_y>0):
    print("2")
if (input_x <0 and input_y<0):
    print("3")