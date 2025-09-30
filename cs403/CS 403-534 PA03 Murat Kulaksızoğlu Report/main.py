from FindCitations import *
from FindCyclicReferences import *
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["COUNT", "CYCLE"])
    parser.add_argument("workers", type=int)
    parser.add_argument("filename")
    args = parser.parse_args()
    if args.operation == "COUNT":
        mr = FindCitations(args.workers)
        mr.start(args.filename)
    elif args.operation == "CYCLE":
        mr = FindCyclicReferences(args.workers)
        mr.start(args.filename)

    