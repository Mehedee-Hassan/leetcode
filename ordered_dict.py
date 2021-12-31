from collections import OrderedDict
import collections


def test():

    t = [('a',1),('d',1),('c',1)]

    o_dict = collections.OrderedDict()
    for element in t:
        o_dict[element[0]] = element[1]

    print(o_dict.popitem(last=False))
    # return the element and value
    
    # ouput :  ('a',1)
    

test()

