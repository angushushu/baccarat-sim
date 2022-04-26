from baccarat import Game

rounds = 10
games = 500
amount = 5000
OUTCOME = ['Player wins', 'Banker wins', 'Tie']
strategy = [1,2,3,6]
stage = 0
amount_records = []
game = Game()
bet_unit = 500
# print(game.play(10)[0])

for r in range(0,rounds):
    amount_records.append([])
    print(amount_records)
    print('round:',r)
    stage = 0
    bet = strategy[stage]
    for g in range(0,games):
        if amount <= bet_unit:
            print('broken')
            break
        print('bet:',bet)
        
        amount_records[r].append(amount)
        amount -= bet*bet_unit
        res, payback = game.play(bet*bet_unit)
        print('res:',res)
        amount += payback

        print('amount:',amount)
        if res == OUTCOME[0]:
            stage = 0
        elif res == OUTCOME[1]:
            stage = (stage+1)%len(strategy)
        bet = strategy[stage]
        
    print('Final amount:', amount)
    amount = 5000


print(amount_records)