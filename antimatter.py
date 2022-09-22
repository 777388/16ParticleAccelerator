print("This may cause a blue light to shoot out of your computer, in case of antimatter creation at point of matter, causing a gamma ray burst followed by memory error")
import threading

def electron(currentposition, lastposition):
        while True:
                currentposition = lastposition
                lastposition = currentposition
                print(currentposition, end="\r", flush=True)
if __name__ =="__main__":
        def knot():
                t1 = threading.Thread(target=electron, args=(2,1))
                t2 = threading.Thread(target=electron, args=(1,2))
                t3 = threading.Thread(target=electron, args=(3,4))
                t4 = threading.Thread(target=electron, args=(4,3))
                t1.start()
                t2.start()
                t3.start()
                t4.start()
                print("    "+num, end="\r", flush=True)
                while True:
                        t1 = t4
                        print(" t4", end="\r", flush=True)
                        t2 = t3
                        print(" t3", end="\r", flush=True)
                        t4 = t1
                        print(" t1", end="\r", flush=True)
                        t3 = t2
                        print(" t2", end="\r", flush=True)
        t5 = threading.Thread(target=knot, args=("dimension one",)
        t6 = threading.Thread(target=knot, args=("dimension two",)
        t7 = threading.Thread(target=knot, args=("dimension three",)
        t8 = threading.Thread(target=knot, args=("dimension four",)
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()

