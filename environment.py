# Author : Shubhansh Awasthi
# username : atrybyme

# importing  essential library
import random

class Env():
    #def __init__(self):
    playersum = random.randint(1,10)
    dealersum = random.randint(1,10)
    def draw(self):
        card_value = random.randint(1,10)
        if random.randint(1,3)<3:
            return card_value
        else:
            return (-1*card_value)
    def step(self,action):
        if action==1:
            self.playersum += self.draw()
            if self.playersum <1 or self.playersum>21:
                return "finish",-1.0
            else:
                return [self.playersum,self.dealersum],0
        else:
            while(self.dealersum<17):
                self.dealersum += self.draw()
                if self.dealersum<1 or self.dealersum>21:
                    return "finish",1.0
            if self.dealersum>self.playersum:
                return "finish",-1.0
            elif self.dealersum<self.playersum:
                return "finish",1.0
            else:
                return "finish",0.0
    def state(self):
        return [self.playersum,self.dealersum]