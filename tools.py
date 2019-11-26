import random


class Poker(object):
    def __init__(self):
        self.pokers = []
        huase = '♥♠♣♦'
        num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for i in huase:
            for j in num:
                self.pokers.append(i + j)
        random.shuffle(self.pokers)

    def hand_out_poker(self):
        poker = self.pokers.pop()
        poker_num = poker[1:]
        if poker_num in 'KJQ10':
            poker_num = '10'
        if poker_num == 'A':
            poker_num = '11'
        return poker, int(poker_num)


class Banker(object):
    """庄家"""

    def __init__(self):
        self.pokers = []
        self.num = 0

    def __str__(self):
        return "庄家"

    def call(self, poker, num):
        self.pokers.append(poker)
        self.num += num

    def stop(self):
        return self.pokers, self.num


class Player(object):
    """闲家"""

    def __init__(self):
        self.pokers = []
        self.num = 0

    def __str__(self):
        return "闲家"

    def call(self, poker, num):
        self.pokers.append(poker)
        self.num += num

    def stop(self):
        return self.pokers, self.num
