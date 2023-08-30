"""
Melvin Shajee
CS 100 2022S Section 102
HW 08, April 6th, 2022
"""


# problem 1
def file_copy(in_file, out_file):
    open(in_file, 'r')
    open(out_file, 'w')
    for line in in_file:
        out_file.write(line + '\n')
    out_file.close()

