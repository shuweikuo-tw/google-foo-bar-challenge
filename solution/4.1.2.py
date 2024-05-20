#!/usr/bin/env python2.7

#running-with-bunnies
def getless(row, dajavu):
  num = {'index':0, 'cost': row[0],'dajavu': dajavu}
  for i, node in enumerate(row):
    if node < num['cost'] and node != 0 and str(i) not in dajavu:
      num['cost'] = node
      num['index'] = i
  return num
l = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]

def solution(times, time_limit):
  least = ''
  s = 0
  node = []
  for row in times:
    item = getless(row, least)
    least += str(item['index'])
  for i in least:
    i = int(i)
    time_limit -= times[s][i]
    s = i
    if i != len(times)-1:
      time_limit -= times[s][-1]
    if time_limit >= 0 and i not in [0, len(times)-1]:
      node.append(i-1)
  return node

l = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
print(solution(l, 1))