import csv

w = 10
loop = 100
alpha = 0.5

def loss(w):
    return w**2 - 4.0*w

def gradient(w):
    return 2*w - 4.0

fp = open('begin1.csv' ,'w')
write = csv.writer(fp, delimiter=',')

for i in range(loop):
    print(alpha * gradient(w),end=' ')
    w = w - alpha * gradient(w)
    write.writerows([[w, loss(w)]])
    print(w , loss(w))
