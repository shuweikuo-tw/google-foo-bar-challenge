#!/usr/bin/env python2.7

l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
def solution(l):
  sort_versions = lambda ver: map(int, ver.split('.'))
  l.sort(key=sort_versions)
  return l
print(solution(l))
