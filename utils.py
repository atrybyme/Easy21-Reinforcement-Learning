import numpy as np
import random

def e_greedy_expo(game,Q_table,N_state_action,No):
    series = []
    state = [game.playersum,game.dealersum]
    while state !="finish":
        sar = [] # denotes state action pair at any time t
        sar.append(state)
        n_state = np.sum(N_state_action[state[0]-1,state[1]-1])
        epsilon = float(No)/float((No + np.sum(n_state)))
        if (random.random()<epsilon):
            action = random.randint(0, 1)
        else:
            if Q_table[state[0]-1, state[1]-1, 0] == Q_table[state[0]-1, state[1]-1, 1]:
                action=random.randint(0, 1)
            else:
                action = np.argmax(Q_table[state[0]-1,state[1]-1])
        state,reward = game.step(action)
        sar.append(action)
        sar.append(reward)
        series.append(sar)
    return series


