#!/usr/bin/env python2.7


class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'

  def disable(self):
    self.HEADER = ''
    self.OKBLUE = ''
    self.OKGREEN = ''
    self.WARNING = ''
    self.FAIL = ''
    self.ENDC = ''

# [
# [0,  1, 10, 10, 10],
# [10, 0,  1,  1,  2],
# [10, 1,  0, 10, 10],
# [10, 1,  10, 0, 10],
# [10, 10, 10, 10, 0]
# ]
# 7

# Start  End  Delta Time Status
#     -   0     -    7   Bulkhead initially open
#     0   1     1    6
#     1   2     1    5
#     2   1     1    4   Return to bunny 1, since bunny 2 does not have potential.
#     1   3     1    3
#     3   1     1    2   Return to bunny 1, since bunny 3 does not have potential.
#     1   4     2    0   The bunnies exit.
getmin = lambda item:item[1]
iteminside = lambda item,l: True if item in l else False

def getless(row, graph):
  for i in xrange(graph.edge):
    node = row[i]
    if graph.edge >= i >= 0 and node != 0:
      if graph.costs[i] > node:
        graph.costs[i] = node
        graph.distances[i] = set([row.index(0)])
      elif graph.costs[i] == node:
        graph.distances[i].add(row.index(0))

class graphic:
  def __init__(self, times, time_limit, fromto):
    self.graph = times
    self.budget = time_limit
    self.fromto = fromto
    self.distances = [set()]*len(times)
    self.edge = len(times)
    self.dajavu = set([0])
    self.costs = [float('inf')] * len(times)

  def indexof(self, current):
    l = set([])
    for i in xrange(len(self.distances)):
      if current in self.distances[i]:
        l.add(i)
    return l

  def relationtree(self):
    # print(self.costs)
    # print([list(item) for item in self.distances])
    c = 0
    while len(self.dajavu) < self.edge-2:
      try:
        next = float('inf')
        index = self.indexof(self.fromto)
        print('iindex',index)
        if len(index) == 1:
          next = list(index)[0]
        else:
          for i in xrange(len(index)):
            next = list(index)[i]
            if next not in self.dajavu:
              break
        if next != float('inf'):
          print('next',next)
          self.dajavu.add(next)
          c += self.costs[next]
          self.fromto = next
        print(self.fromto,self.distances)
      except KeyError:
        print('KeyError')
        return self.dajavu
      except RuntimeError:
        print('RuntimeError')
        return self.dajavu
      else:
        if len(self.dajavu) == self.edge or c > self.budget:
          print('self.dajavu',self.dajavu,c)
          return sorted(list(self.dajavu))
        else:
          print('self.dajavu',self.dajavu,c)

          continue

def solution(times, time_limit):
  graph = graphic(times, time_limit, 0)

  # getless(times[graph.fromto], graph)
  # graph.relationtree()
  # try:
  # except RuntimeError:
  #   return graph.costs
  # finally:
  #   return graph.distances

  for edge in xrange(graph.edge):
    row = times[edge]
    getless(row, graph)
  return graph.relationtree()

l1 = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
l2 = [[0,  1,  5,  5,  2],[10, 0,  2,  6,  10],[10, 10, 0,  1,  5],[10, 10, 10, 0,  1],[10, 10, 10, 10, 0]]
l3 = [[0, 1, 3, 4, 2],[10, 0, 2, 3, 4],[10, 10, 0, 1, 2],[10, 10, 10, 0, 1],[10, 10, 10, 10, 0]]
l4 = [[0, 2, 2, 2, -1],[9, 0, 2, 2, -1],[9, 3, 0, 2, -1],[9, 3, 2, 0, -1],[9, 3, 2, 2, 0]]
l5 = [[0,  1, 10, 10, 10],[10, 0,  1,  1,  2],[10, 1,  0, 10, 10],[10, 1,  10, 0, 10],[10, 10, 10, 10, 0]]
l6 = [[0, 1, 1, 1, 1],[1, 0, 1, 1, 1],[1, 1, 0, 1, 1],[1, 1, 1, 0, 1],[1, 1, 1, 1, 0]]
l7 = [[0, 5, 11, 11, 1],[10, 0, 1, 5, 1],[10, 1, 0, 4, 0],[10, 1, 5, 0, 1],[10, 10, 10, 10, 0]]
print('needs to check')
print('l5: ',solution(l5, 7), '[0, 1, 2]') #Check
# print('l3: ',solution(l3, 4), '[]') #Check
# print('l7: ',solution(l7, 10),'[0, 1]')#Check
# print('below are passed')
# print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
# print('l1: ',solution(l1, 1), )
# print('l2: ',solution(l2, 5), '[0, 1, 2]')
# print('l4: ',solution(l4, 1), '[1, 2]')
# print('l6: ',solution(l6, 3),'[0, 1]')
