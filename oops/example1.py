class example1:
    number = 1
    name = 'Nishant'

def Main():
    me = example1
    me.name = 'Nandish'
    me.number = 2

    print(str(me.name))
    print(str(me.number))

if __name__=='__main__':
        Main()