import time
i = 0
while True:
    if i % 4 == 0:
        print "\rLoading",
    time.sleep(0.5)
    print ".",
    i += 1
    i %= 4
