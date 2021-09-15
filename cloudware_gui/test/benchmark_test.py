import time

def cost(func):
    def wrapper():
        start = time.time()
        func()
        print('cost=%s', time.time() - start)
    return wrapper


end = 100000
@cost
def outerloop():
    for i in range(1, end):
        with open('a', 'a') as f:
            f.write('111\n')


@cost
def innerloop():
    with open('b', 'a') as f:
        for i in range(1, end):
            f.write('111\n') 

outerloop()
innerloop()