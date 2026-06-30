from collections import Counter

shoe_qty = int(input("No. of shoes:"))
shoe_size = list(map(int, input("Enter size of shoes available:").split()))
customer_no = int(input("Enter no. of customers in the shop:"))
shoe_size_avail = Counter(shoe_size)

result = 0

for i in range(customer_no):
    shoe_size_price = list(map(int, input("Enter size and price of shoe customer wants:\n").split()))
    if shoe_size_price[0] in shoe_size_avail and shoe_size_avail[shoe_size_price[0]] > 0:
        shoe_size_avail[shoe_size_price[0]] -= 1
        result += shoe_size_price[1]

print(result)



"""
Task

Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Input Format

1. The first line contains X, the number of shoes.
2. The second line contains the space separated list of all the shoe sizes in the shop.
3. The third line contains N, the number of customers.
4. The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.

Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output

200

Explanation

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.
"""
