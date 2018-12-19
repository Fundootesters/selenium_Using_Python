
a = 10


def test(a):
    print("Value of a is " + str(a))
    a = 12
    print("After declaring again " + str(a))


print("Value of a is outside method " + str(a))
test(a)
