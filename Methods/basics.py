

def add_numbers(n1, n2):

    return n1 + n2


sum1 = add_numbers(2, 4)
sum2 = add_numbers('nishant', ' nandish')
print(sum1)
print(sum2)
print('****Methods Ends*********')


def is_metro(city):
    list = ['bengalore', 'dehli', 'mumbai']

    if city in list:
        return True
    else:
        return False

x = is_metro('dehli')
print(x)