from itertools import permutations
def allPermutations(a):
     permList = permutations(a)
     for perm in list(permList):
         print (''.join(perm))
a=raw_input().split()
allPermutations(a)
