#!/usr/bin/env python2
# -*- coding: utf-8 -*


import os
import sys
from os import path
from random import randint
import copy
import random
from itertools import permutations

#function to initiate matrix
def puzzle_init():
	puzzle=[['0' for x in range(5)] for x in range(5)]
	return puzzle

def Load_Blocks():
	blocks_raw=[]
	blocks=[]
	for i in range(1,len(sys.argv)):
		blocks_raw.append(open(sys.argv[i]).read(10))
	for i in range(len(blocks_raw)):
		maxlength=0
		block_text=blocks_raw[i].split('\n')
		block_text=[x for x in block_text if x!='']
		maxlength=len(max(block_text,key=len))
		block=[['0' for x in range(maxlength)] for x in range(len(block_text))]
		cnt=0
		for j in range(len(block)):
			length=len(block_text[j])
			for k in range(length):
				if block_text[j][k]!=' ':
					block[j][k]=block_text[j][k]
		blocks.append(block)
	#print blocks
	return blocks

#function to find an available slot in the puzzle
def zr_mat(mat):
	ni=0
	mi=0
	for i in range(5):
		for j in range(5):
			if mat[i][j]=='0':
				ni=i
				mi=j
				ind=[ni,mi]
				return ind
	ind=[0,0]
	return ind
		

#function to check if it is possible to put a given block in the puzzle starting from a certain point
def possible_put(mat,z,block):
	if block==[]:
		return False
	init_row=z[0]
	init_col=z[1]
	u=0
	if block[0][0]=='0':
		if init_col==0:
			return False
		for e in range(len(block[0])):
                	if block[0][e]!='0':
                                u=e
                                break
		init_col=init_col-u
	pa=init_row+len(block)
	ph=init_col+len(block[0])
	if (pa>5):
		return False
	elif (ph>5):
		return False	
	for r in range(len(block)):
		for c in range(len(block[0])):
			if block[r][c]!='0':
				if mat[init_row+r][init_col+c]!='0':
					return False
	return True
	
#function to put block in the puzzle
def put_block(mat,block):
	i_state=copy.deepcopy(mat)
        z_ind=zr_mat(mat)
        px=z_ind[0]
        py=z_ind[1]
	if possible_put(mat,z_ind,block)==False:
		return i_state
	u=0
        if block[0][0]=='0':
        	for e in range(len(block[0])):
                	if block[0][e]!='0':
                        	u=e
                                break
                py=py-e
        	h=py+len(block[0])
        a=px+len(block)
        h=py+len(block[0])
	if (a<6) and (h<6):
                for i in range(px,a):
			if i>5:
				return i_state
                        for j in range(py,h):
				if j>5:
					return i_state
                                if mat[i][j]=='0':
                                        if block[i-px][j-py]!='0':
                                                mat[i][j]=block[i-px][j-py]
				else:
					if block[i-px][j-py]!='0':
						return i_state
                return mat
        return i_state	
	


#function to check if puzzle is solved
def check_matrix(mat):
        for i in range(5):
                for j in range(5):
                        if mat[i][j]=='0':
                        	return 1
        return 0


		
#function to restart the puzzle by scratch
def restart_puzzle(mat):
	mat=[['0'for x in range(5)]for x in range(5)]
	return mat

#function to print the puzzle nicely
def print_puzzle(solved_puzzle):
        for i in range(len(solved_puzzle)):
                l=""
                for j in range(len(solved_puzzle)):
			l += solved_puzzle[i][j]
        	print l
 
#function to generate all the possible block combinations
def generate_combinations(blocks):
	initial=list(range(len(blocks)))
	permut=[]
	for p in permutations(initial):
		permut.append(p)
		#print p
	return permut

#function to try all the possible combinations of the blocks
def try_all(puzzle,permut,blocks):
	puzzle_restart=copy.deepcopy(puzzle)
	for i in range(len(permut)):
		for j in range(len(permut[i])):
			index=permut[i][j]
        		puzzle=put_block(puzzle,blocks[index])
			#print j
			if check_matrix(puzzle)!=1:
				#print puzzle
				return puzzle
		puzzle=restart_puzzle(puzzle)
	return puzzle

#main function
def main():
	puzzle=puzzle_init()
	blocks=Load_Blocks()
	permut=generate_combinations(blocks)
	final_puzzle=try_all(puzzle,permut,blocks)
	print_puzzle(final_puzzle)
############################################################# PROGRAM EXECUTION ####################################################################
main()
