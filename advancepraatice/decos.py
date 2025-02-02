

def calculation(param):
    def wrapper(qnty,price):
        param(qnty,price)
        total_price=qnty*price
        print(total_price)
    return wrapper

@calculation
def ice_cream(qnty,price):
    print('bill breakup')

ice_cream(3,20)
    