import asammdf
import pandas as pd
from scipy import io
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
    df = mdf.to_dataframe()
    column_names = list(df.columns)
    column_names

    new_list = []
    for item in column_names:
        string_item = str(item)
        new_string = string_item.replace(".", "_")
        new_list.append(new_string)
    df.columns = new_list    
    io.savemat(save_file, {name: col.values for name, col in df.items()}, format='5')
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()