#example 1
def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)
print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))

#example 2
import time
def count(start=0, end=10):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")
count(5, 15)