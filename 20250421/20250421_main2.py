#15552번
import sys
calc_number = int(sys.stdin.readline())

for i in range(calc_number):
    a,b = map(int, sys.stdin.readline().split(" "))
    print(a+b)