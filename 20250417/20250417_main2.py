#2480번
input_dice = input()
dice_1, dice_2, dice_3 = map(int, input_dice.split(" "))

if (dice_1 == dice_2 == dice_3):
    print((dice_1*1000)+10000)
elif (dice_1 == dice_2):
    print((dice_1*100)+1000)
elif (dice_2 == dice_3):
    print((dice_2*100)+1000)
elif (dice_1 == dice_3):
    print((dice_1*100)+1000)
elif (dice_1 != dice_2 != dice_3 != dice_1):
    print((max(list(map(int, input_dice.split(" ")))))*100)