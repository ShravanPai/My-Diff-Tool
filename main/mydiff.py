'''
Created on Sep 18, 2014

@author: shravan
'''
from sys import argv
from timeit import itertools
from numpy import *

def entry():
    # Get source and target file contents
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
        calc_matrix = zeros((source_length, target_length))


if __name__ == '__main__':
    entry()