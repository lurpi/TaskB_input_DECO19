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
r0="taskB-2d_time_INJ_POINT.tec"
r1="taskB-2d_time_MONITORING2.tec"
r2="taskB-2d_time_MONITORING2.tec"
r3="taskB-2d_time_AW2.tec"


column_hist1 = ("TIME","STRAIN_PLS","PRESSURE1","STRESS_XX","STRESS_YY","STRESS_ZZ","STRESS_XY","STRESS_XZ","STRESS_YZ","VELOCITY_X1","VELOCITY_Y1","VELOCITY_Z1","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","p_(1st_Invariant)","q_(2nd_Invariant)"," Effective_Strain")
column_hist0 = ("TIME","STRAIN_PLS","VELOCITY_X1","VELOCITY_Y1","VELOCITY_Z1","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","PRESSURE1","STRESS_XX","STRESS_YY","STRESS_ZZ","p_(1st_Invariant)","q_(2nd_Invariant)","Effective_Strain")
column_hist3 = ("TIME","STRAIN_PLS","VELOCITY_X1","VELOCITY_Y1","VELOCITY_Z1","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","PRESSURE1","STRESS_XX","STRESS_YY","STRESS_ZZ","STRESS_XY","STRESS_XZ","STRESS_YZ","p_(1st_Invariant)","q_(2nd_Invariant)"," Effective_Strain")

p0 = pd.read_csv(r0, skiprows=2, header=0, names=column_hist0, delimiter=r"\s+")  

p1 = pd.read_csv(r1, skiprows=2, header=0, names=column_hist1, delimiter=r"\s+")  
p2 = pd.read_csv(r2, skiprows=2 ,header=0, names=column_hist1, delimiter=r"\s+")  
p3 = pd.read_csv(r3, skiprows=2, header=0, names=column_hist3, delimiter=r"\s+") 
 
#p3 = pd.read_csv(r3, skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,18,19,20,21,22,23,24,25,26,27,28] ,header=0,skipfooter=1, names=column_hist3, delimiter=r"\s+")  
Elementthickness = 0.02331/4
X= p0["TIME"].values
X1= p1["TIME"].values
X2= p2["TIME"].values
X_f2= p3["TIME"].values
P_inj = p0["PRESSURE1"].values
P1 = p1["PRESSURE1"].values
P2 = p2["PRESSURE1"].values
P_f2 = p3["PRESSURE1"].values
S1 = p1["STRAIN_PLS"].values #* Elementthickness
S2 = p2["STRAIN_PLS"].values #* Elementthickness
S_f2 = p3["STRAIN_PLS"].values #* Elementthickness
v1= p0["VELOCITY_Z1"].values


dS1=[]
dS2=[]
dS_f2=[]

for i in range(len(S1)-1):
 tmp=(S1[i+1]-S1[i])/(X1[i+1]-X1[i])
 if tmp==0:
     tmp=' '
 dS1.append(tmp)
 tmp2=(S2[i+1]-S2[i])/(X2[i+1]-X2[i])
 if tmp2==0:
     tmp2=-1e10
 dS2.append(tmp2)
 tmp_f2=(S_f2[i+1]-S_f2[i])/(X_f2[i+1]-X_f2[i])
 if tmp_f2==0:
     tmp_f2=-1e10 
 dS_f2.append(tmp_f2) 
fig3 = plt.figure(figsize=(9,9))
ax1 = fig3.add_subplot(111)

#ax1.plot(X[0:-6], Dy[0:-6]*1e6, 'b-', lw=2.5,label='Dy')
#ax1.plot(X[0:-6], Dz[0:-6]*1e6, 'g-', lw=2.5,label='Dz')
#ax1.plot(X[0:-6], Dy2[0:-6]*1e6, 'b-.',lw=2.5, label='Dy bottom anchor')
#ax1.plot(X[0:-6], Dz2[0:-6]*1e6, 'g-.',lw=2.5, label='Dz bottom anchor')

ax2 = ax1.twinx()
#ax1.plot(-1000, 5, 'b-', lw=2.5,label='Dy')
#ax2.plot(-1000, 5, 'g-', lw=2.5,label='Dz')
ax1.plot(X, P_inj/1.e6, 'k--', lw=1.5,label='Injection pressure')
ax1.plot(X2, P2/1.e6, 'k-', lw=2.5,label='Pressure at P3')
#ax1.plot(X_f2, P_f2/1.e6, 'g-', lw=2.5,label='Pressure at 18cm below')


ax2.plot(X2[:-1], S2[:-1], 'bo', lw=2.5,label='Plastic shear displacement at P3')
#ax2.plot(X[:-1], v1[:-1], 'bo', lw=2.5,label='Plastic shear displacement at P3')
ax2.plot(X[:-1], S1[:-1], 'g*', lw=2.5,label='Plastic shear displacement at injection point')
#ax1.plot(X, Dx1, 'ro',label='P receiver')
ax1.set_xlabel('Time (s)', fontsize=28)
#ax1.set_ylabel('Displacement ($\mu$m)', fontsize=28)
ax1.set_ylabel('Pressure (MPa)', fontsize=28)
ax1.tick_params(axis='y', labelsize=24)
#ax2.tick_params(axis='y', labelsize=28)
ax1.tick_params(axis='x', labelsize=24)
#ax1.set_ylim(0,7)
max_X=1.5*(min(np.amax(X),440))
#ax1.set_xlim(0,max_X)
ax1.set_xlim(0,1000)
ax1.set_ylim(0,7)
ax2.set_ylabel('Plastic strain', fontsize=28)
ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax2.tick_params(axis='y', labelsize=24)
#ax2.set_ylim(0,5e-3)
#ax2 = ax1.twinx()
#ax2.plot(X_st/86400, lake_level, 'k--', label='water level')
#ax2.set_ylabel('Lake level', fontsize=20)
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
plt.legend(lines + lines2, labels + labels2, loc=2)
plt.tight_layout()
plt.grid()
plt.savefig("FM1_upd.png",dpi=600)
plt.show()



