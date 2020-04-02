#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Double beta and SE 

"""

import pandas as pd
import numpy as np
import argparse
import sys

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='This is to double the beta and SE in a GWAx scan from the output of plink ' ,formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-i', '--input', help='Input file name ',required='True')
    parser.add_argument('-or', '--Odd', help='ODDs ratio column name ',default='OR')
    parser.add_argument('-o', '--output', help='output file',required='True')
    parser.add_argument('-se', '--SE', help='Standard Error column name',default='SE')
    parser.add_argument('-N', '--num', help='Number of obs column name',default='N')
    results = parser.parse_args(args)
    return (results.input , results.Odd, results.output, results.SE , results.num)



def main(file_input , OR_column, output, SE ):
    raw = pd.read_csv(file_input, sep="\t" , header=0)
    raw["beta"]=  ( np.log(raw[OR_column]) ) + ( np.log(raw[OR_column]) )
    raw["SE"] = raw[SE] + raw[SE]
    raw["N"] = ( raw[N] / 4 )
    raw = raw.drop([OR_column], axis=1)
    raw.to_csv(output, sep="\t" , index=None)
    print ("finishing up")


if __name__ == '__main__':
    print( """
    #########################################################
    GWAx adjustment
    #########################################################
    """)
    file_input , OR_column, output, SE , N = check_arg(sys.argv[1:])
    print ("Assuming odds ratio column as : " + OR_column )
    print ("Assuming standed error column as : " + SE )
    print ("Assuming Number of Obs column as : " + N )
    print ("------------------------------------- " )
    print ("")
    print ("output file will be written to: " + output )

    main (file_input , OR_column, output, SE )



