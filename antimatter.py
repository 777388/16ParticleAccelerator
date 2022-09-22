
#This may cause a blue light to shoot out of your computer, in case of antimatter creation at point of matter, causing a gamma ray burst followed by memory error
#Which numbers you land at determine what side, thread and dimension were stopped at, followed by a check of if it matches the stored data. If stored data is uncertain it was stopped between dimensions.
print("ctrl+c to stop the roulette wheel, if matched thats what timeline, side and thread you're in")
print("if not matched, you've switched timelines during times flow backwards")
print("if caught between two, the dimensions are uncertain")
print("if both sides are the same, time flowed backwards")

import threading
import signal
import sys

def sigint_handler(signal, frame):
    print("")
    print(store+"----"+store1+" "+store2+" "+store3)
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

def electron(currentposition, lastposition):
        while True:
                print(currentposition, end="\r", flush=True)
                currentposition = lastposition
                lastposition = currentposition
                print("-----"+str(lastposition), end="\r", flush=True)
                store = currentposition
                store1 = lastposition
def knot(dimension):

        t1 = threading.Thread(target=electron, args=(1,2))
        t2 = threading.Thread(target=electron, args=(3,4))
        t3 = threading.Thread(target=electron, args=(5,6))
        t4 = threading.Thread(target=electron, args=(7,8))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        while True:
                t1 = t4
                print("       t4", end="\r", flush=True)
                store2 = "t4"
                t2 = t3
                print("       t3", end="\r", flush=True)
                store2 = "t3"
                t3 = t2
                print("       t2", end="\r", flush=True)
                store2 = "t2"
                t4 = t1
                print("       t1", end="\r", flush=True)
                store2 = "t1"
                print("           "+dimension, end="\r", flush=True)
                store3 = dimension
        t1.join()
        t2.join()
        t3.join()
        t4.join()

if __name__ =="__main__":
        store = "uncertain side"
        store1 = "uncertain side,"
        store2 = "uncertain thread,"
        store3 = "uncertain timeline"
        t5 = threading.Thread(target=knot, args=("timeline 1",))
        t6 = threading.Thread(target=knot, args=("timeline 2",))
        t7 = threading.Thread(target=knot, args=("timeline 3",))
        t8 = threading.Thread(target=knot, args=("timeline 4",))
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t5.join()
        t6.join()
        t7.join()
        t8.join()

