"""Raptor: Benchmark Your Code

How It Works
Step 1:
You Input The Filename

Step 2:
The program starts to parse that python file.

Step 3
First it finds function starting with bench.
then in an dictionary it stores the function name and its code as string.
this repeats for all functions.


Step 4
At last using timeit, this script benchmarks each code stored in that dictionary
"""

import argparse
import sys
import os
import timeit

def main():
    """Setup The Parser"""
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', metavar='F', type=str,
                        help='File To BenchMark')
    parser.add_argument('-t', type=int, default=10000,
                        help='Time To Run Code In BenchMark')
    args = parser.parse_args()
    if not os.path.isfile(args.filename):
        sys.stdout.write(
            "File Entered Does Not Exist."
        )
    function_code = parse(args.filename)
    setup_code = convert_list_to_code(function_code["SETUP"], True)
    del function_code["SETUP"]

    if function_code == {}:
        sys.stdout.write("Error: No BenchMarking Function Found""")
        exit()

    sys.stdout.write("========== Bench Marking ===========")
    for function_name in function_code:
        code = convert_list_to_code(function_code[function_name], False)
        time_took = timeit.timeit(setup=setup_code,
                                  stmt=code,
                                  number=args.t)
        sys.stdout.write("\n")
        sys.stdout.write("[{}] Took {} Seconds For {} Run(s)".format(
            function_name, time_took, args.t
        ))

def parse(filename):
    """Finds All The Function Code"""
    function_code = {
        "SETUP" : []
    }
    current_function = "SETUP"
    with open(filename, "r") as file:
        for line in file.readlines():
            line = line.replace("\n", "")
            if line[:9] == "def bench":
                #The function is a benching function
                current_function = line[4:][:-4]
                function_code[current_function] = []
            elif line != "\n" and line[:4] == "    ":
                function_code[current_function].append(line)
            elif line[:4] != "    ":
                function_code["SETUP"].append(line)
    return function_code

def convert_list_to_code(list_code, is_setup):
    """Converts Code In List To Actual Code"""
    code = "def test():\n" if not is_setup else ""
    for line in list_code:
        code += line + "\n"
    if not is_setup:
        code += "test()"
    return code


if __name__ == "__main__":
    main()
