import gdb
import sys
import copy
from ctypes import *
class LocatePointers(gdb.Command):
	'''This command locate pointers in a given area of Memory. It takes two arguments: the address of the memory region and its size. 
		The output reports all the pointers present in the area that point to other addresses in the same range '''	
	
	
	def __init__(self):
		gdb.Command.__init__(self,"fpointers", gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, True)

	def invoke(self, arg, from_tty):
		arg_list=gdb.string_to_argv(arg)
		i_address=int(arg_list[0],0)
		size=int(arg_list[1],0)
		f_address=i_address+size
		initial=copy.deepcopy(i_address)
		for i in range (size):
			x=gdb.execute('x/gx ' + str(hex(i_address)), False, True)
			x=x.split('\t')
			x[0]=x[0][:-1]
			x[1]=x[1][:-1]
			x[1]=int(x[1],0)
			if x[1]<=f_address and x[1]>=initial:
				x[1]=hex(x[1])
				p1=x[0]
				p2=x[1]
				print("Pointer at "+str(p1)+" --> "+str(p2))

LocatePointers()
