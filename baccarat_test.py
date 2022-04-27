from asyncio.windows_events import INFINITE
from cmath import inf
from baccarat import Game
import matplotlib.pyplot as plt
import numpy as np

# 勿动
OUTCOME = ['Player wins', 'Banker wins', 'Tie']
HANDS = ['player', 'banker']
# 程序变量，勿动
game = Game()
stage = 0

# 以下为可修改变量
rounds = 100 # 游戏次数
games = 50 # 局数
bet_unit = 500 # 砝码大小
init_amount = 5000.0 # 本金
threshold = INFINITE #2*init_amount # 阈值
hand = HANDS[1] # 压桩压弦
strategy = [1,1,2,4] # 押注策略

# 统计用
hand_cnt = 0
banker_hand = 0
player_hand = 0
tie_hand = 0
amount_records = np.zeros([rounds,games],dtype=int)
mean_amount = np.zeros(games,dtype=float)

plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, 25))))

for r in range(0,rounds):
    print('-----round {}-----'.format(r))
    amount = init_amount
    stage = 0
    bet = strategy[stage]
    for g in range(0,games):
        # print('bet:',bet)
        
        amount_records[r][g] = amount
        amount -= bet*bet_unit
        res, payback = game.play(hand, bet*bet_unit)
        # print('res:',res)
        amount += payback

        # print('amount:',amount)
        if amount < bet_unit:
            # print('Broken with {}'.format(amount))
            for i in range(g+1,games):
                amount_records[r][i] = amount
            break
        if amount >= threshold:
            # print('Reached threshold with {}'.format(amount))
            for i in range(g+1,games):
                amount_records[r][i] = amount
            break
        # 根据胜利方统计
        hand_cnt += 1
        if res == OUTCOME[0]:
            player_hand += 1
        elif res == OUTCOME[1]:
            banker_hand += 1
        else:
            tie_hand += 1
        # 根据玩家对结果的预测决定下一步
        if payback == 2*bet*bet_unit:
            stage = 0
        elif payback == 0:
            stage = (stage+1)%len(strategy)
        bet = strategy[stage]
        while bet*bet_unit > amount:
            bet -= 1
        
    plt.plot(np.arange(games), amount_records[r], '-', alpha=0.3+0.7*(r/rounds), linewidth=1) # x,y axis
    print('Final amount:', amount)

print('amount_records:')
print(amount_records)
for g in range(games):
    mean_amount[g] = np.mean(amount_records[:,g])
plt.plot(np.arange(games), mean_amount, '-', linewidth=3) # avg
plt.show()

print('Final amount:', mean_amount[games-1])
print('banker rate - {}%'.format(banker_hand / hand_cnt * 100))
print('player rate - {}%'.format(player_hand / hand_cnt * 100))
print('tie rate - {}%'.format(tie_hand / hand_cnt * 100))
print(banker_hand / hand_cnt + player_hand / hand_cnt + tie_hand / hand_cnt)
