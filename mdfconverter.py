import asammdf
import pandas as pd
import scipy
import time
import argparse

def parse_arguments():
    """
    Parse commandline arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, help="Path to MF4 file")
    parser.add_argument("--output_file", default="output.mat", type=str, help="Path to save output .mat file")

    return parser.parse_args()


def main():
    args = parse_arguments()
    load_file = args.input_file
    save_file = args.output_file
    start_time = time.time()
    mdf = asammdf.MDF(load_file)
    mdf.export('mat',save_file, format='5')
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()