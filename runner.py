import importlib
import pathlib
from pyaoc.utils import Day
import time

YEAR = "2023"

for i in range(1, 26):
    name = f"day{i:02}"
    if not pathlib.Path(f"pyaoc/{YEAR}/{name}.py").exists():
        continue
    module = importlib.import_module(f"pyaoc.{YEAR}.{name}")
    day: Day = module.day
    t1 = time.time()
    p1 = day.part_1()
    elapsed_time1 = (time.time()-t1) * 10**3
    print(name, "part 1", p1, elapsed_time1)

    t2 = time.time()
    p2 = day.part_2()
    elapsed_time2 = (time.time()-t2) * 10**3
    print(name, "part 2", day.part_2(), elapsed_time2)