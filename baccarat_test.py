from baccarat import Game
import matplotlib.pyplot as plt
import numpy as np

rounds = 1000
games = 500
amount = 30000
OUTCOME = ['Player wins', 'Banker wins', 'Tie']
HANDS = ['player', 'banker']
hand = HANDS[0]
strategy = [1,1,2,4]
stage = 0
amount_records = np.zeros([rounds,games],dtype=int)
game = Game()
bet_unit = 500
threshold = 40000
mean_amount = np.zeros(games,dtype=float)

plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, rounds))))

for r in range(0,rounds):
    print('round:',r)
    stage = 0
    bet = strategy[stage]
    for g in range(0,games):
        print('bet:',bet)
        
        amount_records[r][g] = amount
        amount -= bet*bet_unit
        res, payback = game.play(hand, bet*bet_unit)
        # print('res:',res)
        amount += payback

        # print('amount:',amount)
        if amount <= bet_unit:
            print('Broken!')
            for i in range(g+1,games):
                amount_records[r][i] = amount
            break
        if amount >= threshold:
            print('Rich!')
            for i in range(g+1,games):
                amount_records[r][i] = amount
            break
        if res == OUTCOME[0]:
            stage = 0
        elif res == OUTCOME[1]:
            stage = (stage+1)%len(strategy)
        bet = strategy[stage]
        while bet*bet_unit > amount:
            bet -= 1
        

    plt.plot(np.arange(games), amount_records[r], '-', alpha=0.3+0.7*(r/rounds), linewidth=1) # x,y axis
    print('Final amount:', amount)
    amount = 30000

print('amount_records:')
print(amount_records)
for g in range(games):
    # print('means:',mean_amount)
    # print('g:', g)
    # print('col',g)
    # print(amount_records[:,g])
    # print(np.mean(amount_records[:,g]))
    mean_amount[g] = np.mean(amount_records[:,g])

plt.plot(np.arange(games), mean_amount, '-', linewidth=3) # avg
plt.show()
