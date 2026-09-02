from pathlib import Path
from glob import glob
from json import load
from time import time_ns
RES_PATH = Path(__file__ + "/../../res/").resolve()
CACHE_PATH = RES_PATH.joinpath(Path("cache.json")).resolve()

def run_and_time(func, args):
    start = time_ns()
    func(*args)
    end = time_ns() - start
    print(f"Time taken: {end/(10**9)}s")