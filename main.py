#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
from tools import *


class Blackjack(object):
    def __init__(self):
        self.poker = Poker()
        self.player = Player()
        self.banker = Banker()
        self.flag = True

    def start_game(self):
        """开始游戏"""
        while len(self.poker.pokers) >= 20:
            print("*" * 50)
            print("开始游戏...")
            time.sleep(2)
            self.player.call(*self.poker.hand_out_poker())
            self.banker.call(*self.poker.hand_out_poker())
            self.__show_pokers_and_num(self.player)
            self.__show_pokers_and_num(self.banker)
            while self.flag:
                self.__player_call()
            self.__banker_call()
            self.__who_win(self.player.num, self.banker.num)

    def __player_call(self):
        """闲家要牌"""
        if self.player.num <= 21:
            if input("是否要牌（Y/N）") in 'yY':
                self.player.call(*self.poker.hand_out_poker())
                if self.player.num > 21 and 'A' in ''.join(self.player.pokers):
                    self.player.num -= 10
                    for i in range(len(self.player.pokers)):
                        if 'A' in self.player.pokers[i]:
                            self.player.pokers[i] = self.player.pokers[i][0] + 'a'
                self.__show_pokers_and_num(self.player)
            else:
                self.flag = False
                return self.player.stop()
        else:
            self.flag = False
            self.__who_win(self.player.num)

    def __banker_call(self):
        """庄家要牌"""
        while True:
            if self.banker.num < 17:
                print("庄家开始要牌...")
                time.sleep(2)
                self.banker.call(*self.poker.hand_out_poker())
                if self.banker.num > 21 and 'A' in ''.join(self.banker.pokers):
                    self.banker.num -= 10
                    for i in range(len(self.banker.pokers)):
                        if 'A' in self.banker.pokers[i]:
                            self.banker.pokers[i] = self.banker.pokers[i][0] + 'a'
                self.__show_pokers_and_num(self.banker)
            if self.banker.num > 21:
                self.__show_pokers_and_num(self.banker)
                self.flag = True
                return self.banker.stop()
            if self.banker.num >= 17:
                return self.banker.stop()

    def __show_pokers_and_num(self, role):
        print("%s 当前的牌为：%s，点数为：%d" % (role, role.pokers, role.num))

    def __who_win(self, player_num=0, banker_num=0):
        """比较输赢"""
        if player_num > 21:
            print("啊哦哦，庄家赢了")
        elif banker_num > 21:
            print("玩家赢了!!!!!")
        elif player_num > banker_num:
            print("玩家赢了!!!!!")
        elif player_num < banker_num:
            print("啊哦哦，庄家赢了")
        else:
            print("啊哦哦，平局")
        self.player = Player()
        self.banker = Banker()
        self.flag = True


if __name__ == '__main__':
    game = Blackjack()
    game.start_game()
