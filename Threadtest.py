import threading
#import time
#import os
from multiprocessing import Process
import ui
import app

def startUI():
    #while True:
    ui.ui()

def startAPP():
    app.runAPP()
    #pass


lockThreads = threading.Lock()
threads = []

if __name__ == "__main__":
    thread1 = threading.Thread(target=startUI)
    thread2 = threading.Thread(target=startAPP)
    threading.Lock()

    thread1.start()
    thread2.start()

    threads.append(thread1)
    threads.append(thread2)
    
    
    #thread1.join()
    #thread2.join()
        
   # t1.join()
    #t2.join()