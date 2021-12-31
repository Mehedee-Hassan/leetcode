from collections import OrderedDict
import collections


def test():

    t = [('a',9),('d',1),('c',1)]

    o_dict = collections.OrderedDict()
    for element in t:
        o_dict[element[0]] = element[1]

    print(o_dict.popitem())
    # return the element and value
    # output : ('c',1)
    # --------------------------orderd by valus not key ---------------------


test()

