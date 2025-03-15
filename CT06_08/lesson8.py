import time
numberForCountdownAsker = input("What number would you like to count down")
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)