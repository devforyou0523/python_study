#2884번
input_time = input()
input_hour, input_minute = map(int, input_time.split(" "))
edited_hour = 0;
edited_minute = 0;

if (input_minute - 45 == 0):
    print (f"{input_hour} 0")
elif (input_minute - 45 > 0):
    edited_minute = input_minute-45
    print (f"{input_hour} {edited_minute}")
elif (input_minute - 45 < 0):
    edited_hour = input_hour - 1
    if edited_hour == - 1:
        edited_hour = 23
    edited_minute = 60 - (45 - input_minute)
    print (f"{edited_hour} {edited_minute}")