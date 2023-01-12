import time
def cached(func):
    nums={}

    def wrapper(n):
        try:
            return nums[n]
        except KeyError:
            nums[n]=func(n)
            return nums[n] 
    return wrapper


@cached
def fiba(n):
    if(n<3):
        return 1
    return fiba(n-1)+fiba(n-2)

while True:
    n=int(input())
    t=time.time()
    a=fiba(n)
    dt=time.time()-t
    print(f"It took {dt} seconds to find {n}th num of fibonacci which is:",end=' ')
    print(a)
