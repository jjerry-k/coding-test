import time

def check_time(func, args):
    start_time = time.time()
    func(args)
    end_time = time.time()

    print(f"time : {end_time-start_time}")