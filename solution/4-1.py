#!/usr/bin/env python2.7


#running-with-bunnies

from bisect import bisect_left, bisect_right

# True as bulkhead currently is open, False represents closing state.
gate_state = lambda t:True if t>=0 else False
min_cost = lambda l: min(l)
shiftingright = lambda l:l[bisect_right(l, 0)]
rightnext = lambda l,s:l[bisect_right(l, s)]
minindex = lambda r, m: r.index(m)
hasdelay = lambda r: True if min(r) < 0 else False

class sedtattr:
  def __init__(self, s=0, e=0, d=0, t=0):
    self.s = s
    self.e = e
    self.d = d
    self.t = t

class attr:
  rowat = 0
  collections = []
  guess = 0
  def __init__(self, matrix, timelimit):
    self.matrix = matrix
    self.row = matrix[self.rowat]
    self.mintime = min(matrix[0])
    self.timelimit = timelimit
    self.gatestate = True

  def collect(self):
    if 0 < self.rowat < len(self.matrix)-1:
      self.collections.append(self.rowat-1)

  def upattr(self):
    self.row = self.matrix[self.rowat]
    self.mintime = min(self.row) if min(self.row) != 0 else shiftingright(sorted(self.row))
    self.gatestate = gate_state(self.timelimit)
    self.collect()
    if self.minat() - 1 in self.collections:
      self.guess = rightnext(sorted(self.row), self.minat())
    else:
      self.guess = self.minat()

  # Get index of min cost of time.
  def minat(self):
    firstleast = minindex(self.row, self.mintime)
    return firstleast if firstleast == self.guess else self.guess

  # If you still have time and there are unpicked bunnies out there.
  def next(self):

    for i,time in enumerate(self.row):
      if i != self.rowat:
        print('i',i,' took ', time, self.rowat)


    if self.minat()-1 not in self.collections:
      # Least cost equal to guess and have not collect the bunnies.
      self.rowat = self.minat()
    # else:
      # Visited, multiple same least cost index.

      # while self.minat() in self.collections:
      #   self.mintime = rightnext(sorted(self.row), self.mintime)
      #   print('if in', self.minat() not in self.collections)
      #   if self.minat() not in self.collections:
      #     self.rowat = self.minat()
      #     print('rowat',self.rowat)

    self.timelimit -= self.mintime
    self.upattr()

def getnext(r, t):
  return [i for i, n in enumerate(r) if n == t]

def isbulkhead(i):
  return True if i == bunnies else False

def isover(row, tl):
  # Completed saving bunnies or ran out time tokens.
  return True if tl == 0 or len(workers) == bunnies else False

def solution(matrix, time_limit):
  pa = attr(matrix, time_limit)
  sedt = sedtattr()
  print(hasdelay(matrix[pa.guess]), )
  while pa.gatestate != False and hasdelay(matrix[pa.guess]) != False :
    # if pa.minat() in pa.collections:
    #   break
    pa.next()
    sedt = sedtattr(pa.rowat, pa.minat(), pa.mintime, pa.timelimit)
    print('collection',pa.collections)
    # for item in vars(pa).items():
    #   print(item)
  global workers, workers_scale, bunnies, at_row, gate, Depath
  at_row = 0
  workers = []
  workers_scale = 0
  bunnies = len(matrix)
  # at_row = inspect(matrix) # Array of integers represent the index of the current row in the mattrix.
  gate = gate_state(time_limit)
  Depath = [] # List of stored arraies with [s, e] presents delay path.

  # isover isnt really over.
  # while isover(matrix[at_row], time_limit) == False:
  #   if time_limit < 0 and min_cost(matrix[at_row]) < 0:

  #   elif time_limit == min_cost(matrix[at_row]):

  #   return sorted(workers)
  # else:
  #   return escape(0, at_row, matrix[0][at_row[0]], time_limit)

print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
# print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))

  # [0, 2, 2, 2, -1]
  # [9, 0, 2, 2, -1]
  # [9, 3, 0, 2, -1]
  # [9, 3, 2, 0, -1]
  # [9, 3, 2, 2,  0]

# tl=3
# [0, 1, 1, 1, 1]
# [1, 0, 1, 1, 1]
# [1, 1, 0, 1, 1]
# [1, 1, 1, 0, 1]
# [1, 1, 1, 1, 0]

# 0,4,1,2   0,1,1,2
# 4,1,1,1   1,2,1,1
# 1,4,1,0   2,4,1,0
# since it hits the time limitation and no negtive time delay token in the matrix, return result as [0,1]

# # Ideal case
# if len(self.collections) != len(matrix)-2:            # Bunnies all escaped before gate closed, subtract 2 for head and tail.
#   if self.timelimit > self.mintime:                   # Either visited or not, cost of time still affordable.
#     if self.minat() - 1 not in self.collections:      # Grab bunnies.
#     else:                                             # No bunnies.
#   else:                                               # Cannot afford the cost of time.




# gdt
# 000 false
# 001 false
# 010 true
# 011 true
# 100
# 101
# 110
# 111