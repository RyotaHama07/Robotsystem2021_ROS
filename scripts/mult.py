#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import random
import time

def cb(message):
    if int(Lv) == 1:
        n1 = message.data / 10
        n2 = random.randint(1, 10) 
        n = int(n1) * int(n2)
        print('%d * %d = '% (n1, n2), end='')
        a = input()
        if int(n) == int(a):
            print('正解')
        else:
            print('不正解')
            print('正解は %d です。'% (n))

    elif int(Lv) == 2:
        n1 = message.data
        n2 = random.randint(1, 10)
        n = n1 * n2
        print('%d * %d = '% (n1, n2), end='')
        a = input()
        if int(n) == int(a):
            print('正解')
        else:
            print('不正解')
            print('正解は %d です'% (n))

    elif int(Lv) == 3:
        n1 = message.data
        n2 = random.randint(1, 100)
        n = n1 * n2
        print('%d * %d = '% (n1, n2), end='')
        a = input()
        if int(n) == int(a):
            print('正解')
        else:
            print('不正解')
            print('正解は %d です。'% (n))

    print('')
    time.sleep(1)

def choice():
    print('表示される掛け算を計算しましょう！')
    print('３つの難易度があります。')
    print('Lv1 : 1桁×1桁のみ\nLv2 : 2桁×1桁を含む\nLv3 : 2桁×2桁を含む')
    Lv = input("レベルを1から3の間で選んでください。 ")
    Lv = int(Lv)
    if Lv < 1 or Lv > 3:
        while Lv < 1 or Lv > 3:
            print('1から3の範囲で入力されていません。')
            Lv = input("レベルを1から3の間で選んでください。 ")
            Lv = int(Lv)
    print('\nスタート')
    print('')
    return Lv


if __name__ == '__main__':
    rospy.init_node('mult')
    Lv = choice()
    sub = rospy.Subscriber('random_num', Int32, cb) 
    rospy.spin()
