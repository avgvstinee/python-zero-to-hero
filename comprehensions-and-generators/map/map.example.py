
aa = map(lambda *a: a, range(3))
print(aa) # map object

bb = list(map(lambda *a: a, range(3)))
print(bb) # 1 iterable to list

cc = list(map(lambda *x: x, range(3), 'abc'))
print(cc) # 2 iterables to list

dd = list(map(lambda *a: a, range(3), 'abc', range(4,7)))
print(dd) # 3 iterables to list

ee = list(map(lambda *a: a, (), 'abc')) # empty tuple is shortest 
print(ee) # []

ff = list(map(lambda *a: a,(1,2),'abc')) # (1,2) shortest
print(ff) # [(1,'a'), (2,'b')]
gg = list(map(lambda *a: a,(1,2,3,4),'abc')) # 'abc' shortest
print(gg) # [(1,'a'), (2,'b'), (3,'c')]