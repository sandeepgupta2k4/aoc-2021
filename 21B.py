from collections import defaultdict

combinations = []
combinations.append((1, 1, 1))
combinations.append((1, 1, 2))
combinations.append((1, 1, 3))

combinations.append((1, 2, 1))
combinations.append((1, 2, 2))
combinations.append((1, 2, 3))

combinations.append((1, 3, 1))
combinations.append((1, 3, 2))
combinations.append((1, 3, 3))

combinations.append((2, 1, 1))
combinations.append((2, 1, 2))
combinations.append((2, 1, 3))

combinations.append((2, 2, 1))
combinations.append((2, 2, 2))
combinations.append((2, 2, 3))

combinations.append((2, 3, 1))
combinations.append((2, 3, 2))
combinations.append((2, 3, 3))

combinations.append((3, 1, 1))
combinations.append((3, 1, 2))
combinations.append((3, 1, 3))

combinations.append((3, 2, 1))
combinations.append((3, 2, 2))
combinations.append((3, 2, 3))

combinations.append((3, 3, 1))
combinations.append((3, 3, 2))
combinations.append((3, 3, 3))

comb_count = defaultdict(int)
for com in combinations:
    comb_count[sum(com)] += 1


def game(p1, p2, score1, score2, win_counts, turn, times):
    print(win_counts)
    if score1 >= 21:
        win_counts[1] += times
        return 1
    elif score2 >= 21:
        win_counts[2] += times
        return 2

    if turn == 1:
        for comb, tim in comb_count.items():
            player = p1 + comb
            if player > 10:
                player -= 10
            game(player, p2, score1 + player,
                 score2, win_counts, 2, tim * times)
    else:
        for comb, tim in comb_count.items():
            player = p2 + comb
            if player > 10:
                player -= 10
            game(p1, player, score1, score2 +
                 player, win_counts, 1, tim * times)


win_counts = defaultdict(int)
player1 = 6
player2 = 8
score1 = 0
score2 = 0
game(player1, player2, score1, score2, win_counts, 1, 1)
print(win_counts)
