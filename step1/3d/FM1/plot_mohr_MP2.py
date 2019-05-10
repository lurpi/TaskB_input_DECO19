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
 
def shear_norm_stress(point, dip, strike): # point is a string, dip and strike angle in degrees
 r=point
 p = pd.read_csv(r, skiprows=2, header=0, names=column_hist_mp2, delimiter=r"\s+") 
 dr=np.deg2rad(dip)
 sr=np.deg2rad(strike)
 t= p["TIME"].values
 normal_stress=[]
 shear_stress=[]
 if (strike == 0) or (strike == 180):
     shh=p["STRESS_XX"].values
     sho=p["STRESS_XY"].values
     shz=p["STRESS_XZ"].values
     soo=p["STRESS_YY"].values
     soz=p["STRESS_YZ"].values
     szz=p["STRESS_ZZ"].values
 elif (strike == 90) or (strike == -90):
     soo=p["STRESS_XX"].values
     sho=p["STRESS_XY"].values
     soz=p["STRESS_XZ"].values
     shh=p["STRESS_YY"].values
     shz=p["STRESS_YZ"].values
     szz=p["STRESS_ZZ"].values     
 else:
     sxx=p["STRESS_XX"].values
     sxy=p["STRESS_XY"].values
     sxz=p["STRESS_XZ"].values
     syy=p["STRESS_YY"].values
     syz=p["STRESS_YZ"].values
     szz=p["STRESS_ZZ"].values
     shh=[]
     shz=[]
     for jj in range(0,len(t),1):
       horiz_comp = sxx*np.cos(sr)+syy*np.sin(sr)
       shear_comp = sxz*np.cos(sr)+syz*np.sin(sr)
       shh.append(horiz_comp)
       shz.append(shear_comp)
 for jj in range(0,len(t),1):
    norm=(((shh[jj])*np.sin(dr)*np.sin(dr))-2*shz[jj]*(np.sin(dr)*np.cos(dr))+(szz[jj])*(np.cos(dr)*np.cos(dr)))
    shear=(0.5*(szz[jj]-shh[jj])*np.cos(-2.*dr)+(shz[jj]*np.sin(2*dr)))
    normal_stress.append(norm)      
    shear_stress.append(shear)      
 
 return t,normal_stress, shear_stress

r0="taskB-3d_time_INJ_POINT_00.tec"
r1="taskB-3d_time_MONITORING2.tec"
r2="taskB-3d_time_MONITORING3.tec"
r3="taskB-3d_time_MP_18below.tec"
r3="taskB-3d_time_INJ_POINT_00.tec"
mp2="taskB-3d_time_MONITORING2.tec"
strike = 90
dip = 65

column_hist1 = ("TIME","STRAIN_PLS","PRESSURE1","STRESS_XX","STRESS_YY","STRESS_ZZ","STRESS_XY","STRESS_XZ","STRESS_YZ","VELOCITY_X1","VELOCITY_Y1","VELOCITY_Z1","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","p_(1st_Invariant)","q_(2nd_Invariant)"," Effective_Strain")
column_hist_mp2=("TIME","STRAIN_PLS","PRESSURE1","STRESS_XX","STRESS_YY","STRESS_ZZ","STRESS_XY","STRESS_XZ","STRESS_YZ","VELOCITY_X1","VELOCITY_Y1","VELOCITY_Z1","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","p_(1st_Invariant)","q_(2nd_Invariant)","Effective_Strain")
column_hist0 = ("TIME","PRESSURE1","p_(1st_Invariant)","q_(2nd_Invariant)"," Effective_Strain")
column_hist3 = ("TIME","STRAIN_PLS","PRESSURE1","STRESS_XX","STRESS_YY","STRESS_ZZ","STRESS_XY","STRESS_XZ","STRESS_YZ","VELOCITY_X1","VELOCITY_Y1","VELOCITY_Z1","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","p_(1st_Invariant)","q_(2nd_Invariant)","Effective_Strain")

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
S1 = p1["STRAIN_PLS"].values * Elementthickness
S2 = p2["STRAIN_PLS"].values * Elementthickness
S_f2 = p3["STRAIN_PLS"].values * Elementthickness

T3,N3,S3=shear_norm_stress(mp2, dip, strike)

tx = -1.*np.arange(0., 9e6, 1e5)
ty = np.arange(0., 9e6, 1e5)

plt.figure(figsize=(11,7))
plt.scatter(N3, S3, c=T3, s=50, cmap=plt.cm.CMRmap, edgecolors='None', alpha=0.75)
plt.plot(tx,np.tan(np.deg2rad(22))*ty, 'b--')
plt.plot(tx,-1.0*np.tan(np.deg2rad(22))*ty, 'b--')
plt.axis([-6.75e6, -0., -2.e6, 2e6])
plt.annotate('Time 0',
                   xy=(N3[0],S3[0]), xycoords='data',
                   xytext=(10, -35), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", edgecolor='green',shrinkB=0., 
                                   connectionstyle="angle3", lw=2.5), bbox=dict(boxstyle="square", fc="w"))
plt.annotate('Time :'+np.str(np.trunc(T3[-1])),
                   xy=(N3[-1],S3[-1]), xycoords='data',
                   xytext=(10, +35), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", edgecolor='green',shrinkB=0., 
                                   connectionstyle="angle3", lw=2.5), bbox=dict(boxstyle="square", fc="w"))
if len(T3)>43:                                   
   plt.annotate('Time :'+np.str(np.trunc(T3[43]))+' Pressure :'+np.str(np.trunc(P_f2[43]/1.e3)/1.e3)+' MPa',
                   xy=(N3[43],S3[43]), xycoords='data',
                   xytext=(-200, -35), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", edgecolor='green',shrinkB=0., 
                                   connectionstyle="angle3", lw=2.5), bbox=dict(boxstyle="square", fc="w"))
if len(T3)>73:                                   
    plt.annotate('Time :'+np.str(np.trunc(T3[73]))+' Pressure :'+np.str(np.trunc(P_f2[73]/1.e3)/1.e3)+' MPa',
                   xy=(N3[73],S3[73]), xycoords='data',
                   xytext=(-150, -47.5), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", edgecolor='green',shrinkB=0., 
                                   connectionstyle="angle3", lw=2.5), bbox=dict(boxstyle="square", fc="w"))
if len(T3)>96:                                   
    plt.annotate('Time :'+np.str(np.trunc(T3[96]))+' Pressure :'+np.str(np.trunc(P_f2[96]/1.e3)/1.e3)+' MPa',
                   xy=(N3[96],S3[96]), xycoords='data',
                   xytext=(-100, -60), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", edgecolor='green',shrinkB=0., 
                                   connectionstyle="angle3", lw=2.5), bbox=dict(boxstyle="square", fc="w"))
plt.title('Stress evolution in the fault, point %s' %mp2, fontsize=24)
plt.ylabel('Shear stress (MPa)', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
#set_ylabel('treatment')
cb=plt.colorbar()
cb.set_label('Injection time', fontsize=14)
#leg=plt.legend()
plt.grid()
plt.show()

