import time
from time import strftime
from time import gmtime



def timer(function):
     
    def wrapper(*args, **dargs):
       
        start = time.time()
        res = function(*args, **dargs)
        # print('{:.5} s'.format (time.time()-start))
        end = time.time()
        elapsed = end - start
        print ('elapse',elapsed)
        # print(strftime("%H:%M:%S", gmtime( elapsed)))
        
        return res, elapsed
    return wrapper
    