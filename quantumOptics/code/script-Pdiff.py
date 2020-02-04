# Script for reading in LabView files and performing computation on photon counts (A, B, A', B')

import pandas as pd
import numpy as np

# Reading in txt file with counts
path = 'your path here'

dat = pd.read_table(path, sep = '\t')#might need names param, play with read-in

# Function to provide count differences
def getDiff(A, B, Aprime, Bprime):

	diff = A - B + Aprime - Bprime
	print('difference: ', diff)
	return diff

def percentError(diff, B, Bprime):
	'''Percent error function'''
	err = diff / (B + Bprime)
	print('% Error: ', err)
	return err


