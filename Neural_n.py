import csv

w = -200
keep_w = -200
keep_loss = 100000000000
#w = -16.625
loop = 10
alpha = 10

def loss(w):
    return w**2 - 4.0*w

def gradient(w):
    return 2*w - 4.0

fp = open('begin.csv' ,'w')
write = csv.writer(fp, delimiter=',')

def lo(w ,alpha):
    for i in range(loop):
        w = w - alpha * gradient(w)

for i in range(-200,200):

    lo(i ,alpha)
    if(loss(i) < keep_loss):
        keep_loss = loss(i)
        keep_w = i

    w+=1

for i in range(loop):
    keep_w = keep_w - alpha * gradient(keep_w)
    write.writerows([[keep_w, loss(keep_w)]])
print(keep_w , loss(keep_w))
