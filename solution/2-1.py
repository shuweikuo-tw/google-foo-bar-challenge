#!/usr/bin/env python2.7


def startFinding(l ,t):
  s = 0
  endPoint = 0
  for index, n in enumerate(l):
    s += n
    if s == t:
      endPoint = index

    # Find target or reach the end or greater than limit.
    if s == t or index == len(l) - 1 or s > 250:
      break
  return endPoint

def solution(l, t):
  fromAndTo = [-1, -1]
  endPoint = 0
  for i in range(len(l)):
    endPoint = startFinding(l[i:], t)
    if endPoint != 0:
      fromAndTo[1] = endPoint + i
      fromAndTo[0] = i
      break
    elif endPoint == 0 and l[i] == t:
      fromAndTo = [i, i]
      break
  return(fromAndTo)
print(solution([4, 3, 10, 2, 8], 12))
print(solution([1, 2, 3, 4], 15))
print(solution([1, 2, 15, 3, 4, 8, 1, 1, 1, 1], 30))
