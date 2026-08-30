from pathlib import Path
from glob import glob
from json import load
RES_PATH = Path(__file__ + "/../../res/").resolve()
CACHE_PATH = RES_PATH.joinpath(Path("cache.json")).resolve()