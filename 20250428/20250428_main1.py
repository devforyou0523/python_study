#10871번
repeat_number, target_number = map(int, input().split(" "))
input_list = map(int, input().split(" "))
edited_list = [number for number in input_list if number < target_number]

print(str(edited_list)[1:(len(str(edited_list))-1)].replace(",", ""))