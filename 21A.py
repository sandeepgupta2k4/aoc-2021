player1 = 6
player2 = 8

score1 = 0
score2 = 0
current_dice = 1
dice_rolls = 0


def turn(current_dice, player, score):
    player += ((current_dice + current_dice + 1 + current_dice + 2) % 10)
    if player > 10:
        player -= 10
    score += player
    current_dice += 3
    return score, player, current_dice


while score1 < 1000 and score2 < 1000:
    score1, player1, current_dice = turn(current_dice, player1, score1)
    dice_rolls += 3
    if score1 >= 1000:
        break
    score2, player2, current_dice = turn(current_dice, player2, score2)
    dice_rolls += 3

if score1 > score2:
    print(dice_rolls * score2)
else:
    print(dice_rolls * score1)
