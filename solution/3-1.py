#!/usr/bin/env python2.7


def solution(m):
  w, h = len(m[0]), len(m)
  s_min = 401

  for modified_map in modified_maps(m):
    shortest_length = min_path(modified_map, w, h)

    s_min = min(shortest_length, s_min)

    if s_min == w + h - 1:
      return s_min
  return s_min

def min_path(m, w, h):
  cord = {1: {(0,0)}}

  path_length = 2
  # if 
  #   print 'found '
  while path_length < 401 and cord[path_length-1]:
    #while set([(5,5)]) not in cord.values() and cord[path_length-1]:

    fringe = set()
    for x in cord[path_length-1]:
      # print 'cord',cord,'cord.values()',cord.values()
      expand_x = {y for y in neighbors(x,m) if not any(y in visited for visited in cord.values())}
      fringe = fringe | expand_x

    if (h-1, w-1) in fringe:
      return path_length

    cord[path_length] = fringe

    path_length += 1
  return 401

def neighbors(x, m):
  i, j = x
  w, h = len(m[0]), len(m)
  candidates = {(i-1,j), (i+1,j), (i,j-1), (i,j+1)}
  neighbors = set()
  for y in candidates:
    i, j = y
    if i>=0 and i<h and j>=0 and j<w and m[i][j] == 0:
      neighbors.add(y)

  return neighbors

def modified_maps(m):
  yield m
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == 1:
        copy = [[col for col in row] for row in m]
        yield copy
l = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(solution(l))
