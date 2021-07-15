#!python

from sas7bdat import SAS7BDAT
import pandas as pd
import numpy as np

filename = 'nehrs2018.sas7bdat'
with SAS7BDAT(filename, skip_header=False) as reader:
    for row in reader:
        pass
        #print(row)

    df = reader.to_data_frame()
    df.to_csv('data.csv')

print(df)
