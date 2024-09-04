
#--------------------------------------------------------------------- #
# This a script that gives the action, projects, or checks a symmetry for
# the AN system: Tau(l), sigma_x, sigma_y and all its combinations 
#--------------------------------------------------------------------- #

import numpy as np

def ProjectTrans(fields_data,NY,NXH,width,shift):
    #shift = width/n
    fields_data_t = [np.copy(fields_data[0]), np.copy(fields_data[1]), np.copy(fields_data[2]), np.copy(fields_data[3])]
    Projection = [None] * 4
    for k in range(4):
        for i in range(NXH):
            fields_data_t[k][i,:] = np.exp(2*1j*i*np.pi*(shift/width))*fields_data_t[k][i,:]
    D = 0
    for k in range(4):
        D = D + np.linalg.norm(fields_data_t[k] - fields_data[k])
    for k in range(4):
        Projection[k]=(fields_data[k]+fields_data_t[k])/2

    return fields_data_t,Projection,D

def ProjS1Trans(fields_data,NY,NXH,width,shift):
    #shift = width/n
    fields_data_t = [np.copy(fields_data[0]), np.copy(fields_data[1]), np.copy(fields_data[2]), np.copy(fields_data[3])]
    Projection = [None] * 4
    for k in [0,2]:
        for j in range(NY):
            if j % 2 == 0:
                fields_data_t[k][:,j] = fields_data_t[k][:,j]
            elif j % 2 == 1:
                fields_data_t[k][:,j] = -fields_data_t[k][:,j]
                
    for k in [1,3]:
        for j in range(NY):
            if j % 2 == 0:
                fields_data_t[k][:,j] = -fields_data_t[k][:,j]
            elif j % 2 == 1:
                fields_data_t[k][:,j] = fields_data_t[k][:,j]

    for k in range(4):
        for i in range(NXH):
            fields_data_t[k][i,:] = np.exp(2*1j*i*np.pi*(shift/width))*fields_data_t[k][i,:]
    D = 0
    for k in range(4):
        D = D + np.linalg.norm(fields_data_t[k] - fields_data[k])
    for k in range(4):
        Projection[k]=(fields_data[k]+fields_data_t[k])/2
    return fields_data_t,Projection,D

def ProjS2Trans(fields_data,NY,NXH,width,shift):
    #shift = width/n
    fields_data_t = [np.copy(fields_data[0]), np.copy(fields_data[1]), np.copy(fields_data[2]), np.copy(fields_data[3])]
    Projection = [None] * 4
    for k in [0,3]:
        for i in range(NXH):
            fields_data_t[k][i,:] = np.conj(fields_data_t[k][i,:])
                
    for k in [1,2]:
        for i in range(NXH):
            fields_data_t[k][i,:] = -np.conj(fields_data_t[k][i,:])

    for k in range(4):
        for i in range(NXH):
            fields_data_t[k][i,:] = np.exp(2*1j*i*np.pi*(shift/width))*fields_data_t[k][i,:]
    D = 0
    for k in range(4):
        D = D + np.linalg.norm(fields_data_t[k] - fields_data[k])
    for k in range(4):
        Projection[k]=(fields_data[k]+fields_data_t[k])/2
    return fields_data_t,Projection,D
