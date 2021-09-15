with open('read.txt', 'r') as f:
    buffer = f.readline()
    if buffer == '':
        print('1')
    if not buffer:
        print('2')