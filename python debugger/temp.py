import decimal
from functools import reduce
import os
import sys
from collections import *
from decimal import *
from math import *
from bisect import *
from heapq import *
from io import BytesIO, IOBase
from itertools import groupby

input = lambda: sys.stdin.readline().rstrip("\r\n")
def value(): return tuple(map(int, input().split())) # multiple values
def arr(): return [int(i) for i in input().split()] # aay input
def sarr(): return [int(i) for i in input()] #aay from string
def starr(): return [str(x) for x in input().split()] #string aay
def inn(): return int(input()) # integer input
def svalue(): return tuple(map(str, input().split())) #multiple string values
def parr(): return [(value()) for i in range(n)] # aay of pairs
def Ceil(a,b): return a//b+int(a%b>0)
alphabet="abcdefghijklmnopqrstuvwxyz"
mo = 1000000007
inf=1e18
div=998244353
#print("Case #{}:".format(_+1),end=" ")
#print("Case #",z+1,":",sep="",end=" ")
# ----------------------------CODE-----------------------------#
n=int(input())
a=[]
for i in range(n): a.append(int(input()))
q=int(input())
x=[]
for i in range(q): x.append(int(input()))
l=[]
for i in range(q): l.append(int(input()))
r=[]
for i in range(q): r.append(int(input()))

sm=0
for j in range(q):
    temp=1e18
    id=0
    for i in range(l[j]-1,r[j]):
        if x[j]^a[i]<temp:
            temp=x[j]^a[i]
            id=i
    sm=(sm+id+1)%1000000007

print(sm)