import json
import csv
import os
import pandas as pd

# Get the list of all files and directories
path = "/Users/hanifi.demirel/braze/txt/"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")


with open(path + 'full_json.json', 'w') as outfile:
    for fname in dir_list:
        print(fname)
        if '.txt' in fname:
            with open(path + fname) as infile:
                # outfile.write("[")
                for line in infile:
                    outfile.write(line)
                # outfile.write("]")

print("full json completed")

# with open(path + 'full_json.json', encoding='utf-8') as inputfile:
#     df = pd.read_json(inputfile, encoding="utf8", lines=True)
#     df.to_csv(path + 'csvfile.csv', encoding='utf-8', index=False)

# with open(path + 'full_json.json', encoding='utf-8') as inputfile:
#     for line in inputfile:
#         df = pd.read_json(line, encoding="utf8", lines=True)
#         df.to_csv(path + 'csvfile.csv', encoding='utf-8', index=False)


## tek tırnak çift tırnağa çevirlcek ve boolean değerlerin önüne ve sonuna tırnak konulcak