'''
Created on Sep 18, 2014

@author: shravan
'''

import sys
from sys import argv
from timeit import itertools
from numpy import *
from termcolor import colored
import linecache
 

def entry():
    # Get source and target file contents
    if len(argv) != 3:
        sys.exit('Error!! \n Format :  mydiff.py <Source File> <Target File>')
        
    source_contents = get_contents(argv[1])
    target_contents = get_contents(argv[2])
    
    # Call the function that obtains difference
    get_diff(source_contents, target_contents)
    
# Open each file and output the contents to the console
def get_contents(file_name):
    with open(file_name, 'r') as file_object:
        contents = file_object.read()
    return contents

# Get line by line difference
def get_diff(source_contents, target_contents):
    source = source_contents.split('\n')
    target = target_contents.split('\n')
    line_number = 1
    for source_line, target_line in itertools.izip(source, target):
        source_length = len(source_line)
        target_length = len(target_line)
        calc_matrix = zeros((source_length + 1, target_length + 1))
        sequence_length = calculate_sequence_length(calc_matrix,
                                                    source_length + 1, 
                                                    target_length + 1,
                                                    source_line, 
                                                    target_line)
        if int(sequence_length) != source_length:
            print 'Line Number : ' + str(line_number)
            print colored(' - ' + source_line, 'red')
            print colored(' + ' + target_line, 'green')
            print '----------------------------------------------------------'
        else:
            print 'Line Number : ' + str(line_number) + ' : No Change'
            print '----------------------------------------------------------'
            
        line_number += 1
    
    # Handle the remaining lines
    if line_number > len(source):
       remaining_lines = target[line_number-1:]
       for line in remaining_lines:
           print 'Line Number : ' + str(line_number)
           print colored(' - ' + line, 'red')
           print '----------------------------------------------------------'
           line_number += 1
    else: 
        remaining_lines = source[line_number-1:]
        for line in remaining_lines:
           print 'Line Number : ' + str(line_number)
           print colored(' + ' + line, 'green')
           print '----------------------------------------------------------'
           line_number += 1
     
# returns the sequence length, given two lines
def calculate_sequence_length(calc_matrix, src_len, trg_len, src_line,
                               trg_line):
    
    # Convert the strings to lowercase
    src_line = src_line.lower()
    trg_line = trg_line.lower()
    
    # Apply LCS algorithm
    for i in range (1, src_len):
        for j in range (1, trg_len):
            if src_line[i-1] == trg_line[j-1]:
                calc_matrix[i][j] = calc_matrix[i-1][j-1] + 1
            else:
                calc_matrix[i][j] = max(calc_matrix[i-1][j],
                                        calc_matrix[i][j-1])
                
    # return the longest match
    return calc_matrix[i][j]
                

if __name__ == '__main__':
    entry()