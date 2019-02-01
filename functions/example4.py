#to get data as a tuple


def example4(name, *data):
    print(name)
    print(data)


example4('name', 28, 'xyz', 988651818)

#get data as dict


def example5(name, **data):
    print(name)
    print(data)

    #print all data
    for i,j in data.items():
        print(i, ": ", j)

example5('name', age=28, company='xyz',mobile_no= 988651818)