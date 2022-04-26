from baccarat import Game

amount = 30000
OUTCOME = ['Player wins', 'Banker wins', 'Tie']
strategy = [1, 1, 2, 4]
stage = 0
amount_record = []
amount_records = []
game = Game()
bet_unit = 500
banker_hand = 0
player_hand = 0
tie_hand = 0

# print(game.play(10)[0])
for i in range(1, 10000):
    bet = strategy[stage]
    print('round ', i)
    if amount <= bet_unit:
        print('broken')
        break
    if amount >= 40000:
        print('wins')
        break
    print('bet:', bet)
    amount_record.append(amount)
    amount -= bet * bet_unit
    res, payback = game.play(bet * bet_unit)
    print('res:', res)

    # 计算奖金
    amount += payback

    # 如果是banker赢了
    if payback == 0:
        banker_hand += 1
        # 如果是player赢了
    elif payback == 2 * bet * bet_unit:
        player_hand += 1
        # 如果是tie
    else:
        tie_hand += 1

    if res == OUTCOME[0]:
        stage = 0
    elif res == OUTCOME[1]:
        stage = (stage + 1) % len(strategy)
    print('now you have: ', amount)

print('Final amount:', amount)
print('banker rate', banker_hand / i * 100)
print('player rate', player_hand / i * 100)
print('tie rate', tie_hand / i * 100)
print(banker_hand / i * 100 + player_hand / i * 100 + tie_hand / i * 100)
