from collections import OrderedDict

normal_dict1 = {} # Order does not matter; LIFO only (pops last item)
normal_dict1['a'] = 1
normal_dict1['b'] = 1
normal_dict1['c'] = 1
normal_dict1['d'] = 1
normal_dict1['e'] = 1

normal_dict2 = {}
normal_dict2['c'] = 1
normal_dict2['b'] = 1
normal_dict2['d'] = 1
normal_dict2['e'] = 1
normal_dict2['a'] = 1

ordered_dict1 = OrderedDict() # Order does not matter; FIFO or LIFO (pops from either end)
ordered_dict1['a'] = 1
ordered_dict1['b'] = 1
ordered_dict1['c'] = 1
ordered_dict1['d'] = 1
ordered_dict1['e'] = 1

ordered_dict2 = OrderedDict()
ordered_dict2['c'] = 1
ordered_dict2['b'] = 1
ordered_dict2['d'] = 1
ordered_dict2['e'] = 1
ordered_dict2['a'] = 1


print(normal_dict1 == normal_dict2) # True
print(ordered_dict1 == ordered_dict2) # False