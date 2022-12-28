import time
x = []
for i in range(10001):
    x.append(i)
start = time.time()


def bubblesort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
    return a


bubblesort(x)
end = time.time()
print(end-start)
# 100liczb-natychmiastowe
# 1000liczb- 0.06448221206665039 sekundy
# 10000liczb-9.247878313064575 sekundy
