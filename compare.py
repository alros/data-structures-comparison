from hwcounter import count, count_end
import numpy as np

from data import *
from array_structure import *
from btree import *
from hash_map import *

#
# prepare data

tot_elements = 10000
key_to_find = 5000
expected_key_to_find = "key{i}".format(i=key_to_find)
expected_value_to_find = "value{i}".format(i=key_to_find)
data = [Data("key{i}".format(i=i),"value{i}".format(i=i)) for i in range(1,tot_elements)]
np.random.shuffle(data)

#
# for the stats

performances = []

class Performance:
    def __init__(self, name:str, init:int, find:int, fail:bool) -> None:
        self.name = name
        self.init = init
        self.find = find
        self.fail = fail

structs = [ArrayStructure(tot_elements), LinkedList(), BTree(), HashMap()]

#
# actual test

for struct in structs:
    fail = False
    start = count()
    for d in data:
        struct.add(d)
    init = count_end() - start

    start = count()
    if struct.find(expected_key_to_find) != expected_value_to_find:
        fail = True
    find = count_end() - start
    
    performances.append(Performance(struct.__class__.__name__, init,find, fail))

#
# output

print('{:15} {:15} {:15} {}'.format('type','time to insert','time to find', 'fail'))
for performance in performances:
    print('{name:15} {init:15} {find:15} {fail}'.format(
        name = performance.name, 
        init = "{:,}".format(performance.init), 
        find = "{:,}".format(performance.find), 
        fail = performance.fail))

# example:
# type            time to insert  time to find    fail
# ArrayStructure  43,993,376      9,033,290       False
# LinkedList      145,084,444     9,202,950       False
# BTree           796,571,810     669,562         False
# HashMap         233,445,188     258,856         False