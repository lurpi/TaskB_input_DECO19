# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 13:45:57 2017

@author: Luca
"""
import numpy as np

#set TOUGH2 groups and boundaries (very large volumes) to elements 
#


#known number of element in the mesh

def read_NODES(name_mesh):
 file_grid=name_mesh
 read_nodes=0
 nodes={} # initialize dictionary, to have lookup function later
#-----------------
#with best implementation of reading a file, so python garbage collector will 
#-for sure- close the open file before opening another file (another with command)
#-----------------
 with open(file_grid, 'r') as grid: # 'r' = read 'rU' read UNIVERSAL EOL  
    grid.seek(0) #goes to the beginning of file, useful if need to iterate multiple times over the file
    for line in grid:
       if read_nodes==2: # first nodes line was the number of nodes, skip
        if '$EndNodes' not in line:    
           # read line as name (dict key) id_node, xyz pos
             line_s=line.split(' ')
             id_node=int(line_s[0])
             pos=(float(line_s[1]),float(line_s[2]),float(line_s[3]))
           # build dictionary element
             node_elem=(id_node,pos)
             nodes[id_node]=node_elem
        else:  
             read_nodes=0
       if read_nodes==1: # first nodes line is the number of nodes, read and skip
          read_nodes=2
       if '$Nodes' in line:    
          read_nodes=1
 return nodes

def create_new_MESH(name_mesh, nnodes):
 file_grid=name_mesh
 read_nodes=0
 out_mesh=''
#-----------------
#with best implementation of reading a file, so python garbage collector will 
#-for sure- close the open file before opening another file (another with command)
#-----------------
 with open(file_grid, 'r') as grid: # 'r' = read 'rU' read UNIVERSAL EOL  
    grid.seek(0) #goes to the beginning of file, useful if need to iterate multiple times over the file
    for line in grid:
       out=line 
       if read_nodes==2: # first nodes line was the number of nodes, skip
        if '$EndNodes' not in line:
             line_s=line.split(' ')
             id_node=int(line_s[0])
             out=str(nnodes[id_node][0])+' '+str(nnodes[id_node][1][0])+' '+str(nnodes[id_node][1][1])+' '+str(nnodes[id_node][1][2])+'\n'
        else:  
             read_nodes=0
       if read_nodes==1: # first nodes line is the number of nodes, read and skip
          read_nodes=2
       if '$Nodes' in line:    
          read_nodes=1
       out_mesh=out_mesh+out
 return out_mesh

fname='mesh3d.msh'
nodes=read_NODES(fname)
new_nodes={}
new_x = {0 : 0,
                1 : 1,
                2 : 2,
                3 : 3,
                4 : 4,
                5 : 5,
                6 : 6,
                7 : 7,
                8 : 8,
                9 : 8.5,
                10 : 9,
                11 : 9.46,
                12 : 9.64,
                13 : 9.82,
                14 : 9.91,
                15 : 10.0,
                16 : 10.09,
                17 : 10.18,
                18 : 10.36,
                19 : 10.54,
                20 : 11,
                21 : 11.5,
                22 : 12,
                23 : 13,
                24 : 14,
                25 : 15,
                26 : 16,
                27 : 17,
                28 : 18,
                29 : 19,
                30 : 20,
} # dictionary to define new x refined around well
for i in nodes:
    id_node=int(nodes[i][0])
    pos_x=new_x[nodes[i][1][0]]
    pos=(pos_x,nodes[i][1][1],nodes[i][1][2])
    node_elem=(id_node,pos)
    new_nodes[id_node]=node_elem

out=create_new_MESH(fname,new_nodes)    
"""
read_nodes=0
out_mesh=''
with open(fname, 'r') as grid: # 'r' = read 'rU' read UNIVERSAL EOL  
    grid.seek(0) #goes to the beginning of file, useful if need to iterate multiple times over the file
    for line in grid:
       out=line 
       if read_nodes==2: # first nodes line was the number of nodes, skip
        if '$EndNodes' not in line:
             line_s=line.split(' ')
             id_node=int(line_s[0])
             out=str(new_nodes[id_node][0])+' '+str(new_nodes[id_node][1][0])+' '+str(new_nodes[id_node][1][1])+' '+str(new_nodes[id_node][1][2])
        else:  
             read_nodes=0
       if read_nodes==1: # first nodes line is the number of nodes, read and skip
          read_nodes=2
       if '$Nodes' in line:    
          read_nodes=1
       print line   
       out_mesh=out_mesh+'\n'+out
"""
f = open(fname[0:-5]+'_xcorrectP2P3.mesh', 'w') # 'r' = read
f.write(out)
f.close()
