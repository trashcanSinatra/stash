import os
import sys
from numbers import Number
from threading import Timer

class Stash:

    def __init__(self, cacheMax=1024, itemSizeMax=96):
        self.cache = dict()
        self.hitCount = 0
        self.missCount = 0
        self.size = 0
        self.items = 0  
        self.cacheLimit = cacheMax
        self.itemSizeLimit = itemSizeMax
    

    def put(self, key, value, time, timeoutFunc=None):
        
        if(time <> None
           and (isinstance(time, Number) is False
           or time <= 0)
          ):
            raise ValueError("Time parameter must be a number.")
        elif(timeoutFunc <> None 
             and callable(timeoutFunc) is False
            ):
            raise ValueError("Timeout Function is not a valid function.")
        
        if key in self.cache:
            oldRecord = self.cache[key]
            timer = oldRecord['timer']
            timer.cancel()
        else:
            self.size += 1
        
        record = {
                    'value' : value,
                    'time' : time,
                    'func' : timeoutFunc
                 }

        def delete(key, value):
            self.remove(key)
            if callable(timeoutFunc):
                timeoutFunc(key, value)

        record['timer'] = Timer(time, delete, [key, value])
        record['timer'].start()

        self.cache[key] = record
        return value


    def remove(self, key=None):
        self.size -= 1
        del self.cache[key]
    
    def clear(self):
        print('To DO')
    
    def get(self, value):
        print('To Do')
    
    def hits(self):
        return self.hitCount

    def misses(self):
        return self.missCount

    def size(self):
        return self.size

    def memsize(self, val=None):
        if val is None:
            print(self.size.__sizeof__())
        else:
            print(self.hitCount.__sizeof__())
    
    def exportJson():
        print('To Do')
    
    def importJson():
        print('To Do')




def env(var):
    print(var)


if __name__ == "__main__":
    print("This module is to be imported.")