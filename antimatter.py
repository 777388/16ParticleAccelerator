
print("This may cause a blue light to shoot out of your computer, in case of antimatter creation at point of matter, causing a gamma ray burst followed by memory error")
import threading
import signal
import sys

def sigint_handler(signal, frame):
    print("")
    print(store+" "+store2+" "+store3)
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

def electron(currentposition, lastposition):
        while True:
                currentposition = lastposition
                lastposition = currentposition
                print(currentposition, end="\r", flush=True)
                store = lastposition
def knot(dimension):

        t1 = threading.Thread(target=electron, args=(2,1))
        t2 = threading.Thread(target=electron, args=(1,2))
        t3 = threading.Thread(target=electron, args=(3,4))
        t4 = threading.Thread(target=electron, args=(4,3))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        while True:
                t1 = t4
                print("  t4", end="\r", flush=True)
                store2 = "t4"
                t2 = t3
                print("  t3", end="\r", flush=True)
                store2 = "t3"
                t3 = t2
                print("  t2", end="\r", flush=True)
                store2 = "t2"
                t4 = t1
                print("  t1", end="\r", flush=True)
                store2 = "t1"
                print("       "+dimension, end="\r", flush=True)
                store3 = dimension
        t1.join()
        t2.join()
        t3.join()
        t4.join()

if __name__ =="__main__":
        store = "uncertain side,"
        store2 = "uncertain thread,"
        store3 = "uncertain dimension"
        t5 = threading.Thread(target=knot, args=("dimension 1",))
        t6 = threading.Thread(target=knot, args=("dimension 2",))
        t7 = threading.Thread(target=knot, args=("dimension 3",))
        t8 = threading.Thread(target=knot, args=("dimension 4",))
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t5.join()
        t6.join()
        t7.join()
        t8.join()

