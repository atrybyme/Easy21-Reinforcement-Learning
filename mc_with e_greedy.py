# Author : Shubhansh Awasthi
# Algorith used : Monte Carlo Control with epsilon-greedy Exploration.
# This code used table lookup method.  

import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
#import utility file it contains e-greedy exploration function
from utils import *
# Import Game Environment file
from environment import *

# hyperparameters
# Considering No Discounting of future reward :
gamma = 1.0
No = 100.0
epochs = 200000
# Size of Lookup table will be (player_state_size*dealer_state_size*action_size)
# Starting with 0 value for each possible state-action pair
Q_table = np.zeros((21,10,2))
# Number of time each state-action pair is visited will be saved in this matrix
N_state_action  = np.zeros((21,10,2))
Error_per_epoch = []
game = Env()
for ep in range(epochs):
    # Sampling policy with epsilon_greedy Exploration and recording it in policy
    game.reset()
    policy = []
    state = [game.playersum, game.dealersum]
    while state != "finish":
         # sar denotes [state,action,pair] at any time t
        sar = [] 
        sar.append(state)
        # e_greedy_expo function gives us the next action value
        action = e_greedy_expo(game,Q_table,N_state_action,No)
        state, reward = game.step(action)
        sar.append(action)
        sar.append(reward)
        #we append sar at every time step
        policy.append(sar)
    #Total discounted reward be g_t = r_t + gamma*r_t+1 + .....
    #lets create a array giving g_T at any time t
    G = []
    g_t=0.0
    for t in range(len(policy)):
    #updating the policy accoding to monte carlo
        g_t = gamma*g_t + policy[len(policy)-t-1][2]
        G.append(g_t)
    G.reverse()
    sum_of_sq_error=0
    for t in range(len(policy)):
        state,action,reward = policy[t]
        N_state_action[state[0]-1,state[1]-1,action] +=1
        alfa = 1/float(N_state_action[state[0]-1,state[1]-1,action])
        error = G[t]-np.max(Q_table[state[0]-1, state[1]-1, :])
        Q_table[state[0]-1, state[1]-1, action] += alfa*error
        sum_of_sq_error +=(error*error)
    mean_square_error = sum_of_sq_error/len(policy)
    Error_per_epoch.append(mean_square_error)
    if ep%100==0:
        print("Epochs Completed ",ep,"out of total ",epochs)
#plt.plot(Error_per_epoch)
#plt.show()
# Plot a graph showing the valuefunction of that state
## deviding data into 3d corddinates
X = []
Y = []
Z = []
for x in range(21):
    for y in range(10):
        X.append(x+1)
        Y.append(y+1)
        Z.append(np.amax(Q_table[x,y,:]))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(Y, X, Z, cmap=cm.coolwarm)
ax.set_xlabel('Initial Card Value of Dealer')
ax.set_ylabel('Total Card Value of Player')
ax.set_zlabel('Value of State')

plt.show()
