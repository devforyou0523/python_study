#32963번 (이거 왜 시간초과)
import sys

apple_num, question_num = map(int, sys.stdin.readline().split(" "))
taste_list = list(map(int,sys.stdin.readline().split(" ")))
size_list = list(map(int,sys.stdin.readline().split(" ")))
pick_size_list = []

for i in range (question_num):

    pick_taste = int(sys.stdin.readline())
    max_size = 0
    pick_size_list = []

    for j in range(apple_num):
        if taste_list[j] >= pick_taste:
            pick_size_list.append(size_list[j])
    
    max_size = max(pick_size_list)

    print(pick_size_list.count(max_size))