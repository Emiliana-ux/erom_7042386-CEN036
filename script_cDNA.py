#!/usr/bin/env python3

import sys


DNA = sys.arg[1]

n1 = int(sys.arg[2])
n2 = int(sys.arg[3])
n3 = int(sys.arg[4])
n4 = int(sys.arg[5])

start_codons = ['ATG']
stop_codons = ['TAG', 'TAA', 'TGA']

string = 'CGTCGTCGCCGCCGCCGCCATGTCGGGAGGTGGTGTGATCCGTGGCCCGACGAAAAAAAAAAAAAGCGG$
contigs	= ['ATG', 'TAG', 'TAA', 'TGA') 
positions = [20, 49, 66, 98] #position for each contig on string

