from lib.stash import Stash, env


test = Stash()
test.memsize()

def call_test(key, val):
    print(key + " " + val)


test.put("Aaron", "Value", 2, call_test)



env('AARON')

