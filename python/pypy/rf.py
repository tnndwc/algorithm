import time

num = 0
with open('C:\Users\wangying\Desktop\stdout.log', 'r') as f:
    for line in f:
        num += 1
        '%s %d' % (line, num)

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))