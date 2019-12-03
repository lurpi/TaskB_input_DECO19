cl_5 = 0.05;
cl_10 = 0.1;
cl_25 = 0.25;
cl_1000 = 1.;
cl_250 = 2.5 ;
cl_750 = 5. ;
cl_outer = 5. ;

dip_fault=65 ;
slp = 1.0/Tan(dip_fault*(Pi/180)) ;//0.466307658155; // 1 over tan dip (here 65 degree)


width=20;
length=20;
bottom = -20.;
top= -0.;

width_b=length/2-(slp*(top-bottom)/2.); // if dip 65 5.3369234
width_t=length/2+(slp*(top-bottom)/2.); // if dip 65 14.6630766

f_dam=0.10492;
f_cor=0.023315383;

//f_cor=0.233153829;



dy1=1.;
dy2=0.25;
dy3=-0.25;
dy4=-1.36;
dy5=-1.5;

dx1=slp*dy1;
dx2=slp*dy2;
dx3=slp*dy3;
dx4=slp*dy4;
dx5=slp*dy5;
  
Point(101)={0, 0, bottom, cl_10};  
Point(1010)={0, 0, -10.+dy5, cl_10};  
Point(1012)={0, 0, -10.+dy4, cl_10};  
Point(1014)={0, 0, -10.+dy3, cl_10};  
Point(1040)={0, 0, -10.+dy2, cl_10}; 
Point(1044)={0, 0, -10.+dy1, cl_10}; 
Point(104)={0, 0, top, cl_10};  
 
Point(102)={0, width_t-f_dam-f_cor*0.5, top, cl_10};  
Point(1020)={0, 10-f_dam-f_cor*0.5+dx1 , -10.+dy1, cl_10};
Point(1023)={0, 10-f_dam-f_cor*0.5+dx2 , -10.+dy2, cl_10};
Point(1025)={0, 10-f_dam-f_cor*0.5+dx3 , -10.+dy3, cl_10};
Point(1027)={0, 10-f_dam-f_cor*0.5+dx4 , -10.+dy4, cl_10};
Point(1030)={0, 10-f_dam-f_cor*0.5+dx5 , -10.+dy5, cl_10};
Point(103)={0, width_b-f_dam-f_cor*0.5, bottom, cl_10};  

Point(112)={0, width_t-f_cor*0.5, top, cl_10};  
Point(1120)={0, 10-f_cor*0.5+dx1 , -10.+dy1, cl_10};
Point(1123)={0, 10-f_cor*0.5+dx2 , -10.+dy2, cl_10};
Point(1125)={0, 10-f_cor*0.5+dx3 , -10.+dy3, cl_10};
Point(1127)={0, 10-f_cor*0.5+dx4 , -10.+dy4, cl_10};
Point(1130)={0, 10-f_cor*0.5+dx5 , -10.+dy5, cl_10};
Point(113)={0, width_b-f_cor*0.5, bottom, cl_10};  

Point(122)={0, width_t+f_cor*0.5, top, cl_10}; 
Point(1220)={0, 10+f_cor*0.5+dx1 , -10.+dy1, cl_10};
Point(1223)={0, 10+f_cor*0.5+dx2 , -10.+dy2, cl_10};
Point(1225)={0, 10+f_cor*0.5+dx3 , -10.+dy3, cl_10};
Point(1227)={0, 10+f_cor*0.5+dx4 , -10.+dy4, cl_10};
Point(1230)={0, 10+f_cor*0.5+dx5 , -10.+dy5, cl_10};
Point(123)={0, width_b+f_cor*0.5, bottom, cl_10};  

Point(132)={0, width_t+f_dam+f_cor*0.5, top, cl_10};
Point(1320)={0, 10+f_dam+f_cor*0.5+dx1 , -10.+dy1, cl_10};
Point(1323)={0, 10+f_dam+f_cor*0.5+dx2 , -10.+dy2, cl_10};
Point(1325)={0, 10+f_dam+f_cor*0.5+dx3 , -10.+dy3, cl_10};
Point(1327)={0, 10+f_dam+f_cor*0.5+dx4 , -10.+dy4, cl_10};
Point(1330)={0, 10+f_dam+f_cor*0.5+dx5 , -10.+dy5, cl_10};
Point(133)={0, width_b+f_dam+f_cor*0.5, bottom, cl_10};  

Point(105)={0, length, bottom, cl_10};  
Point(1050)={0, length, -10.+dy5, cl_10};  
Point(1052)={0, length, -10.+dy4, cl_10};  
Point(1054)={0, length, -10.+dy3, cl_10};  
Point(1060)={0, length, -10.+dy2, cl_10};  
Point(1066)={0, length, -10.+dy1, cl_10};  
Point(106)={0, length, top, cl_10};  

Line(1) = {105, 1050};
Line(2) = {1050, 1052};
Line(3) = {1052, 1054};
Line(4) = {1054, 1060};
Line(5) = {1060, 1066};
Line(6) = {1066, 106};
Line(7) = {133, 1330};
Line(8) = {1330, 1327};
Line(9) = {1327, 1325};
Line(10) = {1325, 1323};
Line(11) = {1323, 1320};
Line(12) = {1320, 132};
Line(13) = {123, 1230};
Line(14) = {1230, 1227};
Line(15) = {1227, 1225};
Line(16) = {1225, 1223};
Line(17) = {1223, 1220};
Line(18) = {1220, 122};
Line(19) = {113, 1130};
Line(20) = {1130, 1127};
Line(21) = {1127, 1125};
Line(22) = {1125, 1123};
Line(23) = {1123, 1120};
Line(24) = {1120, 112};
Line(25) = {103, 1030};
Line(26) = {1030, 1027};
Line(27) = {1027, 1025};
Line(28) = {1025, 1023};
Line(29) = {1023, 1020};
Line(30) = {1020, 102};
Line(31) = {101, 1010};
Line(32) = {1010, 1012};
Line(33) = {1012, 1014};
Line(34) = {1014, 1040};
Line(35) = {1040, 1044};
Line(36) = {1044, 104};
Line(37) = {105, 133};
Line(38) = {133, 123};
Line(39) = {123, 113};
Line(40) = {113, 103};
Line(41) = {103, 101};
Line(42) = {106, 132};
Line(43) = {132, 122};
Line(44) = {122, 112};
Line(45) = {112, 102};
Line(46) = {102, 104};

Line Loop(47) = {37, 7, 8, 9, 10, 11, 12, -42, -6, -5, -4, -3, -2, -1};
Line Loop(49) = {38, 13, 14, 15, 16, 17, 18, -43, -12, -11, -10, -9, -8, -7};
Line Loop(51) = {39, 19, 20, 21, 22, 23, 24, -44, -18, -17, -16, -15, -14, -13};
Line Loop(53) = {40, 25, 26, 27, 28, 29, 30, -45, -24, -23, -22, -21, -20, -19};
Line Loop(55) = {41, 31, 32, 33, 34, 35, 36, -46, -30, -29, -28, -27, -26, -25};
Plane Surface(50) = {49};
Plane Surface(48) = {47};
Plane Surface(52) = {51};
Plane Surface(54) = {53};
Plane Surface(56) = {55};

// Tell Gmsh how many cells you want per edge;
Transfinite Line {1, 7, 13, 19, 25, 31} = 18;
Transfinite Line {2, 8, 14, 20, 26, 32} = 2;
Transfinite Line {3, 9, 15, 21, 27, 33} = 4;
Transfinite Line {4, 34} = 5;
Transfinite Line {10, 16, 22, 28} = 25;
Transfinite Line {5, 11, 17, 23, 29, 35} = 5;
Transfinite Line {6, 12, 18, 24, 30, 36} = 19;
Transfinite Line {41, 46, 42, 37 } =5;
Transfinite Line {40, 45,  43, 38 } =4;
// Transinite the fault, how many columns of elem them?
Transfinite Line {39, 44 } =5;

// Tell Gmsh what the corner points are(going clockwise or counter-clockwise);
Transfinite Surface {56} = {101, 104, 102,  103};
Transfinite Surface {54} = {103,  102, 112,  113};
Transfinite Surface {52} = {113,  112, 122,  123};
Transfinite Surface {50} = {123,  122, 132,  133};
Transfinite Surface {48} = {133, 132, 106, 105};

// Recombine the triangles into quads;
Recombine Surface{56,54,52,50,48};

//Physical Surface("0left") = {18};
//Physical Surface("1damage") = {20};

//Physical Surface("2core") = {22};
//Physical Surface("3damage") = {24};
//Physical Surface("4right") = {26};

zdir[] = Extrude{30., 0, 0} { Surface{56,54,52,50,48}; Layers{30}; Recombine;};
Physical Volume(137) = {1};
Physical Volume(138) = {2};
Physical Volume(139) = {3};
Physical Volume(140) = {4};
Physical Volume(141) = {5};


// requires python script afterwards to redistribute x coordinates