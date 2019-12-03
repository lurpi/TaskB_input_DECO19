# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright (C) 2006 Anders Logg
# Licensed under the GNU LGPL Version 2.1
#
# Modified by Garth N. Wells (gmsh function)
# Modified by Alexander H. Jarosch (gmsh fix)
# Modified by Angelo Simone (Gmsh and Medit fix)
# Modified by Andy R. Terrel (gmsh fix)
# Modified by Magnus Vikstrom (metis and scotch function)
#
# Modified by Luca Urpi (Gmsh 2.2 to OGS, exporting 2D triangle to .tin file)

import sys
import numpy as np

ifilename="mesh3_xcorrectP2P3.mesh" #generated from .geo file, having physical volumes defined before than surfaces (needed with material_ID)
ofilename="taskB-step3.msh"


def error ( message ):

#*****************************************************************************80
#
## ERROR prints an error message and exits.
#
  "Write an error message"

  for line in message.split ( "\n" ):
    print "*** %s" % line

  sys.exit(2)

#*****************************************************************************80

def write_header_mesh(ofile, cell_type, dim):

#*****************************************************************************80
#
## WRITE_HEADER_MESH writes the mesh header.
    ofile.write("""\
<?xml version=\"1.0\" encoding=\"UTF-8\"?>

<dolfin xmlns:dolfin=\"http://www.fenics.org/dolfin/\">
  <mesh celltype="%s" dim="%d">
""" % (cell_type, dim))

def write_header_graph(ofile, graph_type):

#*****************************************************************************80
#
## WRITE_HEADER_GRAPH writes the graph header.
#
    ofile.write("""\
<?xml version=\"1.0\" encoding=\"UTF-8\"?>

<dolfin xmlns:dolfin=\"http://www.fenics.org/dolfin/\">
  <graph type="%s">
""" % (graph_type))

#*****************************************************************************80

def write_header_OGS(ofile, pcs_type):
#
## WRITE_HEADER_OGS writes the OGS .msh header.
    if pcs_type==None:
        pcs_type="NO_PCS"
    ofile.write("#FEM_MSH \n$PCS_TYPE\n "+pcs_type+"\n")

def write_footer_OGS(ofile):

#*****************************************************************************80
#
## WRITE_FOOTER_OGSwrites the mesh footer.
#
    ofile.write("#STOP")

def write_footer_mesh(ofile):

#*****************************************************************************80
#
## WRITE_FOOTER_MESH writes the mesh footer.
#
    ofile.write("""\
  </mesh>
</dolfin>
""")

def write_footer_graph(ofile):

#*****************************************************************************80
#
## WRITE_FOOTER_GRAPH writes the graph footer.
#
    ofile.write("""\
  </graph>
</dolfin>
""")

def write_header_NODES(ofile, num_vertices):

#*****************************************************************************80
#
## WRITE_HEADER_VERTICES ???
#
    "Write NODES header"
    print "Expecting %d vertices" % num_vertices
    ofile.write("$NODES\n %d \n" % num_vertices)
    #ofile.write("    <edges size=\"%d\">\n" % num_vertices)

def write_footer_vertices(ofile):

#*****************************************************************************80
#
## WRITE_FOOTER_VERTICES ???
#
    "Write vertices footer"
    ofile.write("    </vertices>\n")
    print "Found all vertices"

def write_header_edges(ofile, num_edges):

#*****************************************************************************80
#
## WRITE_HEADER_EDGES ???
#
    "Write edges header"
    print "Expecting %d edges" % num_edges
    ofile.write("    <edges size=\"%d\">\n" % num_edges)

def write_footer_edges(ofile):

#*****************************************************************************80
#
## WRITE_FOOTER_EDGES ???
#
    "Write edges footer"
    ofile.write("    </edges>\n")
    print "Found all edges"

def write_NODES(ofile, vertex, x, y, z):

#*****************************************************************************80
#
## WRITE_VERTEX ???
#
    "Write vertex"
    if largefile==0:
       ofile.write("%d %.12f %.12f %.12f\n" % (vertex, x, y, z))

def write_graph_vertex(ofile, vertex, num_edges, weight = 1):

#*****************************************************************************80
    "Write graph vertex"
    ofile.write("      <vertex index=\"%d\" num_edges=\"%d\" weight=\"%d\"/>\n" % \
        (vertex, num_edges, weight))

def write_graph_edge(ofile, v1, v2, weight = 1):

#*****************************************************************************80
	 "Write graph edge"
	 ofile.write("      <edge v1=\"%d\" v2=\"%d\" weight=\"%d\"/>\n" % \
        (v1, v2, weight))

def write_header_ELE(ofile, num_cells):

#*****************************************************************************80
    "Write cells header"
    ofile.write("$ELEMENTS\n %d \n" % num_cells)
    print "Expecting %d cells" % num_cells

def write_header_cells(ofile, num_cells):

#*****************************************************************************80
    "Write cells header"
    ofile.write("    <cells size=\"%d\">\n" % num_cells)
    print "Expecting %d cells" % num_cells

def write_footer_cells(ofile):

#*****************************************************************************80
    "Write cells footer"
    ofile.write("    </cells>\n")
    print "Found all cells"

def write_cell_interval ( ofile, cell, n0, n1 ):
#*****************************************************************************80
    "Write cell (interval)"
    ofile.write("      <interval index=\"%d\" v0=\"%d\" v1=\"%d\"/>\n" % \
        (cell, n0, n1))

def write_cell_triangle(ofile, cell, n0, n1, n2):
#*****************************************************************************80
    "Write cell (triangle)"
    ofile.write("      <triangle index=\"%d\" v0=\"%d\" v1=\"%d\" v2=\"%d\"/>\n" % \
        (cell, n0, n1, n2))
        
def write_cell_tetrahedron(ofile, cell, n0, n1, n2, n3):

#*****************************************************************************80
    "Write cell (tetrahedron)"
    ofile.write("      <tetrahedron index=\"%d\" v0=\"%d\" v1=\"%d\" v2=\"%d\" v3=\"%d\"/>\n" % \
        (cell, n0, n1, n2, n3))

def write_ELE_tetrahedron(ofile, cell, mat, n0, n1, n2, n3):

#*****************************************************************************80
#elem_nr and material_ID in OGS are starting from 0==> -1 in the expression
    "Write ele (tetrahedron)"
    ofile.write("%d %d tet %d %d %d %d\n" % \
        (cell-1, np.abs(mat/2-13) , n0, n1, n2, n3)) 

def write_ELE_quad(ofile, cell, mat, n0, n1, n2, n3):

#*****************************************************************************80
#elem_nr and material_ID in OGS are starting from 0==> -1 in the expression
    "Write ele (tetrahedron)"
    ofile.write("%d %d quad %d %d %d %d\n" % \
        (cell-1, np.abs(mat/2-13) , n0, n1, n2, n3)) 

		
def write_ELE_triangle(ofile, cell, n0, n1, n2):
#*****************************************************************************80
    "Write cell (triangle)"
    if largefile==0:
        vertex_n0=vertex_coord[n0]
        vertex_n1=vertex_coord[n1]
        vertex_n2=vertex_coord[n2]        
    else:
        vertex_n0=str(vertex_x[n0])+" "+str(vertex_y[n0])+" "+str(vertex_z[n0])
        vertex_n1=str(vertex_x[n1])+" "+str(vertex_y[n1])+" "+str(vertex_z[n1])
        vertex_n2=str(vertex_x[n2])+" "+str(vertex_y[n2])+" "+str(vertex_z[n2])
    out="%d %s %s %s\n" % \
     (cell, str(vertex_n0)[1:-2].replace(",", ""), str(vertex_n1)[1:-2].replace(",", ""), str(vertex_n2)[1:-2].replace(",", ""))
    ofile.write(out)

def write_ELE_hex(ofile, cell, mat, n0, n1, n2, n3, n4, n5, n6, n7):

#*****************************************************************************80
#elem_nr and material_ID in OGS are starting from 0==>they are defined in the .geo file (i.e. for the minor fault Physical Volume(6) = {8,9};  )
    "Write ele (tetrahedron)"
    ofile.write("%d %d hex %d %d %d %d %d %d %d %d\n" % \
        (cell-1, mat , n0, n1, n2, n3, n4, n5, n6, n7)) 

#
## GMSH2XML converts a Gmsh msh file to Dolfin XML format.
#
#  Discussion:
#
#This function can only handle triangles and tetrahedrons.
#
#  Modified:
#
#18 October 2014
#ifilename="lake-2layers_phys-names-shifted.msh" #generated from .geo file, having physical volumes defined before than surfaces (needed with material_ID)
#ofilename="lake.msh"
rob=0
if rob==0 :
#def gmsh2xml ( ifilename, ofilename ):

#Convert between .gmsh v2.0 format (http://www.geuz.org/gmsh/) and .xml, 
#parser implemented as a state machine:
#
#0 = read 'MeshFormat'
#1 = read  mesh format data
#2 = read 'EndMeshFormat'
#3 = read 'Nodes'
#4 = read  number of vertices
#5 = read  vertices
#6 = read 'EndNodes'
#7 = read 'Elements'
#8 = read  number of cells
#9 = read  cells
#10 = done  


#  Open files
#
    ifile = open(ifilename, "r")
    ofile = open(ofilename, "w")    # note the 'b' meaning binary
#
#  Scan file for cell type
#
    cell_type = None
    dim = 0
    dim_2_count=0
    dim_3_count=0
    line = ifile.readline()
    while line:

# Remove newline
     if line[-1] == "\n":
        line = line[:-1]
    # Read physical name (useful for properties and for .tin file)
        if line.find("$PhysicalNames") == 0:                        
            line = ifile.readline()
            num_units  = int(line)
            line = ifile.readline()
            physical_names = {}
            phys_list= []#vertices_2_used = []
            while line.find("$EndPhysicalNames") == -1:
             unit = line[:-2].split(" ",2) #rsplit, to force to have only 3groups (physical name can have space)
             unit_type = int(unit[0])
             unit_tags = int(unit[1])
             unit_name = unit[2][1:]  # names coming from .geo file --gmsh innput--
             phys_list.append(unit) #        vertices_2_used.extend(node_num_list)
             physical_names[unit_tags] = unit_name
             line = ifile.readline()
            #for n,v in enumerate(phys_list):
             #physical_dict[v] = n
    # Read dimension
        if line.find("$Elements") == 0:
                        
            line = ifile.readline()
            num_cells  = int(line)
            num_cells_counted = 0
            if num_cells == 0:
                error("No cells found in gmsh file.")
                line = ifile.readline()
            else:
                line = ifile.readline()
#
#  Now iterate through elements to find largest dimension.  
#
#  Gmsh format might include elements of lower dimensions in the element list.
#
#  We also need to count number of elements of correct dimensions.
#
#  Also determine which vertices are not used.
#

            vertices_2_used = []
            vertices_3_used = []
            count=0
            while line.find("$EndElements") == -1:
                element = line.split()
                elem_type = int(element[1])
                num_tags = int(element[2])
                count=count+1
                if elem_type == 2:
                    if dim < 2:
                        cell_type = "triangle"
                        print cell_type
                        dim = 2
                    node_num_list = [int(node) for node in element[3 + num_tags:]]
                    vertices_2_used.extend(node_num_list)
                    print node_num_list
                    dim_2_count += 1
                    line = ifile.readline()				
                if elem_type == 3:
                    if dim < 2:
                        cell_type = "quad"
                        print cell_type
                        dim = 2
                    node_num_list = [int(node) for node in element[3 + num_tags:]]
                    vertices_2_used.extend(node_num_list)
                    
                    dim_2_count += 1
                    line = ifile.readline()	
                    if dim_2_count == 5:
                      aaaaa= element
                elif elem_type == 4:
                    if dim < 3:
                        cell_type = "tetrahedron"
                        dim = 3
                        #vertices_2_used = None
                    node_num_list = [int(node) for node in element[3 + num_tags:]]
                    vertices_3_used.extend(node_num_list)
                    
                    dim_3_count += 1
                    line = ifile.readline()
                elif elem_type == 5:
                    if dim < 3:
                        cell_type = "hex"
                        dim = 3
                        #vertices_2_used = None
                    node_num_list = [int(node) for node in element[3 + num_tags:]]
                    print node_num_list
                    vertices_3_used.extend(node_num_list)
                    dim_3_count += 1
                    line = ifile.readline()	
                    
                #line = ifile.readline()
        print line
        line = ifile.readline()
        """
        else:
            
            print line
            # Read next line
            line = ifile.readline()
        """
#
#  Check that we got the cell type and set num_cells_counted
#
    if cell_type == None:
        error("Unable to find cell type.")


    if dim == 2:
        #num_cells_counted = dim_2_count
        vertex_set = set ( vertices_2_used )
        vertices_2_used = None
    else:
        #num_cells_counted = dim_3_count
        vertex_set = set ( vertices_3_used + vertices_2_used )        
        #vertices_3_used = None    
    num_cells_counted= dim_2_count + dim_3_count
    vertex_dict = {}
    for n,v in enumerate(vertex_set):
        vertex_dict[v] = n
#
# Step to beginning of file
#
    ifile.seek(0)
#
# Write header
#  
    write_header_OGS(ofile,None)   
   #write_header_mesh(ofile, cell_type, dim)
#   
# Initialize node list (gmsh does not export all vertexes in order)
#
    nodelist = {}
#   
# Current state
#
    state = 0
#   
# Write data
#
    largefile = 0 
    num_vertices_read = 0
    num_cells_read = 0
    vertex_coord={}
    num_TET_read = 0
    num_QUAD_read = 0
    num_HEX_read = 0
    material_id=0
    while state != 10:

        # Read next line
        line = ifile.readline()
        if not line: break

        # Skip comments
        if line[0] == '#':
            continue

        # Remove newline
        if line[-1] == "\n":
            line = line[:-1]

        if state == 0:
            if line == "$MeshFormat":
                state = 1
        elif state == 1:
            (version, file_type, data_size) = line.split()
            state = 2
        elif state == 2:
            if line == "$EndMeshFormat":
                state = 3
        elif state == 3:
            if line == "$Nodes":
                state = 4
        elif state == 4:
            #num_vertices = int(line)
            num_vertices = len(vertex_dict)
            write_header_NODES(ofile, num_vertices)
            state = 5
        elif state == 5:
            (node_no, x, y, z) = line.split()
            if vertex_dict.has_key(int(node_no)):
                node_no = vertex_dict[int(node_no)]
            else:
                continue
            nodelist[int(node_no)] = num_vertices_read
            x = float(x)
            y = float(y)
            z = float(z)
            coords=(x,y,z)
            if num_vertices <= 900000: #arbitrary limit, if larger file, split x&y&z
              vertex_coord[node_no] = coords              
            else:
               if largefile==0:
                   largefile=1
                   vertex_x={}
                   vertex_y={}
                   vertex_z={}
               vertex_x[node_no] = x                           
               vertex_y[node_no] = y
               vertex_z[node_no] = z
            write_NODES(ofile, num_vertices_read, x, y, z)
            num_vertices_read +=1
            
            if num_vertices == num_vertices_read:
                #write_footer_vertices(ofile)                
                state = 6
        elif state == 6:
            if line == "$EndNodes":
                state = 7
        elif state == 7:
            if line == "$Elements":
                state = 8
        elif state == 8:
            if dim == 3:
            	write_header_ELE(ofile, dim_3_count)   
            else:
            	write_header_ELE(ofile, dim_2_count)   
            state = 9
        elif state == 9:
            element = line.split()
            elem_type = int(element[1])
            num_tags  = int(element[2])
            phys_name = int(element[3]) 
            gmsh_id = int(element[4])
            if elem_type == 2:
                node_num_list = [vertex_dict[int(node)] for node in element[3 + num_tags:]]
                for node in node_num_list:
                    if not node in nodelist:
                        error("Vertex %d of triangle %d not previously defined." %
                              (node, num_cells_read))
                n0 = nodelist[node_num_list[0]]
                n1 = nodelist[node_num_list[1]]
                n2 = nodelist[node_num_list[2]]
                tin_filename=str(physical_names.get(phys_name))+".tin"
                #tin_filename=str(phys_name)+".tin"
                tinfile = open(tin_filename, "a")
                write_ELE_triangle(tinfile, num_cells_read, n0, n1, n2)
                tinfile.close()
                num_cells_read +=1 
            #elif elem_type == 4 and dim == 3:
            elif elem_type == 3:
                num_QUAD_read +=1
                node_num_list = [vertex_dict[int(node)] for node in element[3 + num_tags:9]]
                for node in node_num_list:
                    if not node in nodelist:
                        error("Vertex %d of quad %d not previously defined." % 
                              (node, num_cells_read))
                n0 = nodelist[node_num_list[0]]
                n1 = nodelist[node_num_list[1]]
                n2 = nodelist[node_num_list[2]]
                n3 = nodelist[node_num_list[3]]
                write_ELE_quad(ofile, num_QUAD_read, phys_name, n0, n1, n2, n3)
                num_cells_read +=1     
            elif elem_type == 4:
                num_TET_read +=1
                node_num_list = [vertex_dict[int(node)] for node in element[3 + num_tags:9]]
                for node in node_num_list:
                    if not node in nodelist:
                        error("Vertex %d of tetrahedron %d not previously defined." % 
                              (node, num_cells_read))
                n0 = nodelist[node_num_list[0]]
                n1 = nodelist[node_num_list[1]]
                n2 = nodelist[node_num_list[2]]
                n3 = nodelist[node_num_list[3]]
                write_ELE_tetrahedron(ofile, num_TET_read, phys_name, n0, n1, n2, n3)
                num_cells_read +=1      
            elif elem_type == 5:
                num_HEX_read +=1
                node_num_list = [vertex_dict[int(node)] for node in element[3 + num_tags:13]]
                for node in node_num_list:
                    if not node in nodelist:
                        error("Vertex %d of tetrahedron %d not previously defined." % 
                              (node, num_cells_read))
                n0 = nodelist[node_num_list[0]]
                n1 = nodelist[node_num_list[1]]
                n2 = nodelist[node_num_list[2]]
                n3 = nodelist[node_num_list[3]]
                n4 = nodelist[node_num_list[4]]
                n5 = nodelist[node_num_list[5]]
                n6 = nodelist[node_num_list[6]]
                n7 = nodelist[node_num_list[7]]
                write_ELE_hex(ofile, num_HEX_read, phys_name, n0, n1, n2, n3, n4, n5, n6, n7)
                num_cells_read +=1 
            if num_cells_counted == num_cells_read:
              #write_footer_cells(ofile)                
              state = 10
        elif state == 10:
            break
#
# Check that we got all data
#
    if state == 10:
        print "Conversion done"
    else:
        error("Missing data, unable to convert \n\ Did you use version 2.0 of the gmsh file format?")
#  
# Write footer
#
    write_footer_OGS(ofile)  
#
# Close files


    ifile.close()
    ofile.close()       