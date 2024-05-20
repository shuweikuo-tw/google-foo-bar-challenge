#!/usr/bin/env python2.7

# fuel-injection-perfection
def recursion(n):
  while n > 1:
    global moves
    if n&1 == 0:  #Remain 0 by divide 2.
      n >>= 1
    else:
      if n == 3 or n % 4 ==1:
        n-=1
      else:
        n+=1
    moves+=1

def solution(n):
  look_up = [3, 4]
  foot_print = []
  import math
  global moves, look_up_destination, power_times, is_integer
  is_integer = lambda a: a.is_integer()
  power_times = lambda a:math.log(a, 2)
  look_up_destination = lambda a:a in look_up

  n = int(n)
  moves = 0
  recursion(n)
  return moves
print(solution('124480579411363943422977485485450829978158403576349485507396127987323092328068524587695005561434534623452345436346456353425362283769712245781118297614280332424240701048410620648401132628401374562794562558123463462235342526466804149296501029546541499918765438784295157088047123009825235235168758962399'))

def ask():
  print('Insert random integer as destination from 1.')
  destination = input()
  if isinstance(destination, int) == False:
    return
  else:
    print('It took',solution(destination),'moves to reach destination', destination)
    ask()
ask()