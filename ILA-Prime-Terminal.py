import time
import random

def breaker():
    print("\n")
    time.sleep(0.1)
    print("-----------------------------------------------------------------")
    time.sleep(0.1)
    print("\n")

def bootoptions():
    print("#####################################")
    print("BOOT SERVER OPTIONS")
    print("#####################################")
    print("A-SYNC_MDS")
    print("Jerry's_free_hosting_server_2003")
    print("Microsoft.NET_PUBLIC-127")
    print("SWIFT_NET_LOCAL-000292")
    print("AT&T_NULLZONE")
    print("FREE_US_FROM_KJU")
    print("Bonzi Software, Inc._DATAHOST")
    print("*1*2*4*8*16*")
    print("IMHAVINGFUN_8^##")
    print("")
    

print("COMPLETION...0%")
time.sleep(0.7)
progress = 0
while progress < 100:
    increment = random.randint(1, 5)
    progress = min(progress + increment, 100)
    print(f"COMPLETION...{progress}%")
    time.sleep(random.uniform(0.1, 0.3))
    if progress >= 100:
        print("COMPLETION...100%")
        print("COMPLETE")
        breaker()
        wait_for_ready()
        break



    
    

