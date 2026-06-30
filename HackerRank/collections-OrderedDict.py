# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

N = int(input())
net_price = 0
item_dict = OrderedDict()

for i in range(N):
    name_price = list(input().split())
    price = int(name_price[-1])
    name = " ".join(name_price[:-1])
    item_dict[name] = item_dict.get(name, 0) + price

print("\n")

for key, value in item_dict.items():
    print(key, value)
    


"""
Task

You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format

1. The first line contains the number of items, N.
2. The next N lines contains the item's name and price, separated by a space.

Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

Explanation

BANANA FRIES: Quantity bought: 1, Price: 12
Net Price: 12
POTATO CHIPS: Quantity bought: 2, Price: 30
Net Price: 60
APPLE JUICE: Quantity bought: 2, Price: 10
Net Price: 20
CANDY: Quantity bought: 4, Price: 5
Net Price: 20
"""
