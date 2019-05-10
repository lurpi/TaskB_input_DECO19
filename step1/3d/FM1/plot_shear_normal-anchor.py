# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:52:34 2015

@author: Luca Urpi
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def out_arr( outfile,list):
 filename=outfile
 f = open(filename, 'w')
 print >> f, "\n".join(list)
 f.close()
 return;
r1="taskB-3D_time_ANCHOR_TOP.tec"
r2="taskB-3D_time_ANCHOR_BOT.tec"
dip=np.deg2rad(65)

column_hist = ("TIME","STRAIN_PLS","PRESSURE1","STRESS_XX","STRESS_YY","STRESS_ZZ","STRESS_XY","STRESS_XZ","STRESS_YZ","VELOCITY_X1","VELOCITY_Y1","VELOCITY_Z1","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","p_(1st_Invariant)","q_(2nd_Invariant)","Effective_Strain")

p1 = pd.read_csv(r1, skiprows=2, header=0, names=column_hist, delimiter=r"\s+")  
p2 = pd.read_csv(r2, skiprows=2 ,header=0, names=column_hist, delimiter=r"\s+")  

X= p1["TIME"].values
Dx1 = p1["DISPLACEMENT_X1"].values
Dx2 = p2["DISPLACEMENT_X1"].values
Dy1 = p1["DISPLACEMENT_Y1"].values
Dy2 = p2["DISPLACEMENT_Y1"].values
Dz1 = p1["DISPLACEMENT_Z1"].values
Dz2 = p2["DISPLACEMENT_Z1"].values
Dx=Dx1-Dx2
Dy=Dy1-Dy2
Dz=Dz1 -Dz2 
Shear=-Dz*np.sin(dip)-Dy*np.cos(dip)
Norm=Dz*np.cos(dip)-Dy*np.sin(dip)
obs_point=[]
txt="time dx dy dz"
obs_point.append(txt)
for jjj in range(len(X)):
  if X[jjj]<850.:
    txt0=str(X[jjj])
    txt1=str(Dx[jjj])
    #txt2=str(Dx2[jjj])
    txt3=str(Dy[jjj])
    #txt4=str(Dy2[jjj])
    txt5=str(Dz[jjj])
    #txt6=str(Dz2[jjj])
    txt=txt0+" "+txt1+" "+txt3+" "+txt5
    obs_point.append(txt)
    
    #out_filename="to_matlab/obs_point-y"+y_title+"_x"+x_title+"_z"+z_title+".dat"
# out_filename="out_anchor_diff_displ.dat"

# print "\nWriting delta displ in delta_anchor.dat file"
# out_arr(out_filename,obs_point)

fig3 = plt.figure()
ax1 = fig3.add_subplot(111)

ax1.plot(X[0:-6], Shear[0:-6]*1e6, 'b-', lw=2.5,label='Shear anchor')
ax1.plot(X[0:-6], Norm[0:-6]*1e6, 'g-', lw=2.5,label='Norm anchor (positive = extension)')

#ax1.plot(X, Dx1, 'ro',label='P receiver')
ax1.set_xlabel('Time (s)', fontsize=28)
ax1.set_ylabel('Displacement ($\mu$m)', fontsize=28)
ax1.tick_params(axis='y', labelsize=24)
ax1.tick_params(axis='x', labelsize=24)
#ax1.set_xlim(0,25)
#ax2 = ax1.twinx()
#ax2.plot(X_st/86400, lake_level, 'k--', label='water level')
#ax2.set_ylabel('Lake level', fontsize=20)
plt.tight_layout()
plt.legend()
plt.grid()
plt.show()


