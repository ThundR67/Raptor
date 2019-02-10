# Raptor

A Easy Way To Benchmark Your Code.

# How To Use It
Step 1: First You Will Need To Create A Benchmark File For Your Project

```python3
"""to_benchmark.py"""

#Add All Your Setup
import math


#Write Your Benchmarking Functions
def bench_square_root():
    """Name Your Function Starting With bench. Or Raptor Wont Detect It
    Also the function should not take any arguments"""
    return math.sqrt(25)
    
def bench_multiply():
    return 5 ** 25
```


Step 2: Download raptor.py
```
pip install python-raptor
```

Then, Run This In Your Terminal

**NOTICE: The -t Argument Takes An Integer Which Tells Raptor How Many Times
Should Each Benchmarking Function Run**
```
raptor.py to_benchmark.py -t 10000
```

Step 3: See The  Output. Voilaaaaa!!!!!!!!!

Output
```
========== Bench Marking ===========
[bench_square_root] Took 0.0025385 Seconds For 10000 Run(s)
[bench_multiply] Took 0.0010813999999999997 Seconds For 10000 Run(s)
```



# Future Features
1. I want to add an history, which can show you how much faster or slower your program has gotten
2. I want to add colored output
3. I want to add better exception handling


# Built With
Raptor Uses Timeit Module To Benchmark Your Code


# Author
Roshan Jignesh Mehta - sonicroshan122@gmail.com