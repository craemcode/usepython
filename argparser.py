'''This program enables users to run commandline programs without hustle'''

import argparse

'''create the parser'''
parser = argparse.ArgumentParser(description="calculate the power of any number")

'''add the arguments'''
parser.add_argument("base",help="the base",
                        type=int)
parser.add_argument("exponent",help="the power to raise the base",
                        type=int)
parser.add_argument("-v","--verbose",help="Increase information of putput",
                    action="store_true")

'''parse the arguments'''
args = parser.parse_args()

answer = args.base**args.exponent

#print the answer in verbose mode
print(f"-----------------{__file__}-----------------------------")
if args.verbose:
    print(f"{args.base} raised to power {args.exponent} is {answer}")
else: 
    print(answer)
