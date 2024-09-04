import ANSymmetries as ANS
import os
import h5py
import scipy.io
import numpy as np
from mpi4py import MPI
import time
import pathlib

from dedalus import public as de
from dedalus.extras import flow_tools

import sys
sys.setrecursionlimit(10000)

import logging
logger = logging.getLogger(__name__)

import timeit
start = timeit.default_timer()

#---------------------------------------- #
# Input file
#---------------------------------------- #
input_filename = './solution2d.h5'
input_file = h5py.File(input_filename, 'r')
#---------------------------------------- #

#---------------------------------------- #
# Solver parameters
#---------------------------------------- #
Ra = 0.68
dt = 0.01

#psign = 1
psign = 0
real_bool = 1
imag_bool = 0

pmag = 1e-4
sim_index=1

height = 1.0*np.array(input_file.get('/params/height'))
width = 1.0*np.array(input_file.get('/params/width'))
NX = int(1.0*np.array(input_file.get('/params/NX')))
NY = int(1.0*np.array(input_file.get('/params/NY')))
NXH = int(NX/2)

Re = 0.0136
Er = 1.0
#---------------------------------------- # 
QAA_data_coeff = np.array(input_file.get('/QAA_coeff'))
QAB_data_coeff = np.array(input_file.get('/QAB_coeff'))
U_data_coeff = np.array(input_file.get('/U_coeff'))
V_data_coeff = np.array(input_file.get('/V_coeff'))
input_file.close()
fields_data = [np.copy(QAA_data_coeff), np.copy(QAB_data_coeff), np.copy(U_data_coeff), np.copy(V_data_coeff)]
A,B,C=ANS.ProjS1Trans(fields_data,NY,NXH,width,width/2)
print(fields_data)