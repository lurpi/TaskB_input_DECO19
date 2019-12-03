cl_5 = 0.05;
cl_10 = 0.1;
cl_25 = 0.25;
cl_1000 = 1.;
cl_250 = 2.5 ;
cl_750 = 5. ;
cl_outer = 5. ;

dip_fault=60 ;
slp = 1.0/Tan(dip_fault*(Pi/180)) ;//0.466307658155; // 1 over tan dip (here 65 degree)

dip_fault_minor=30;
slp_min_inv = Tan(dip_fault_minor*(Pi/180)) ;//0.5773502691896257

width=20;
length=20;
left_margin = -3; 
bottom = -23.;
top= -3.;

// fault passes through point (0,10,-10)
aaa=(1/slp)*10+10;
width_b=(bottom+aaa)*slp ;//length/2-(slp*(top-bottom)/2.); // if dip 65 5.3369234;
width_t=(top+aaa)*slp;//length/2+(slp*(top-bottom)/2.); // if dip 65 14.6630766;

fault_thickness=0.021131 ; //assumption
damage_thickness= 0.021131  ; //assumption

f_dam=damage_thickness/Sin(dip_fault*(Pi/180)); // old one was 3 colukmns ,thickness of 0.10492
f_cor=fault_thickness/Sin(dip_fault*(Pi/180));

fault_minor_thickness=.005 ; //assumption
damage_minor_thickness= 0.005  ; //assumption

f_min_dam=damage_minor_thickness/Sin(dip_fault_minor*(Pi/180)); 
f_min_cor=fault_minor_thickness/Sin(dip_fault_minor*(Pi/180));

//f_cor=0.233153829;

dy1=1.5*Sin(dip_fault*(Pi/180)); //1.36 if fault with dip 65degree;
dy2a=0.25;
dy2b=-0.25;
dy3=-1.898676193; // crossing point of a fault with dip 60 and a minor fault dipping 30 (above boundary, minor fault thickness 0.005 m);
dy4=-1.905171384; // crossing point of a fault with dip 60 and a minor fault dipping 30;
dy5=-3.0*Sin(dip_fault*(Pi/180)); //2.6 if fault with dip 60degree;

dx1=slp*dy1;  // 0.466307658155 
dx2a=slp*dy2a;  // 0.11657691453875
dx2b=slp*dy2b;  // 0.
dx3=slp*dy3;  // -0.11657691453875
dx4=slp*dy4;  // -0.6341784150908
dx5=slp*dy5;  // -0.6994614872325

dy2amin =(5+dx2a)*slp_min_inv; 
dy2bmin =(5+dx2b)*slp_min_inv; 
dy3min =(5+dx3)*slp_min_inv; 
dy4min =(5+dx4)*slp_min_inv;
dy5min =(5+dx5)*slp_min_inv;

// additional points for the minor fault
dxmin_a = fault_minor_thickness;
dxmin_1 = 0.2;
dxmin_2 = 1.5;
dxmin_3a = -6.995+left_margin;
dxmin_3b = -7.005+left_margin;
dymin_1 =dxmin_1*slp_min_inv;
dymin_2 =dxmin_2*slp_min_inv;
dymin_3a =dxmin_3a*slp_min_inv;
dymin_3b =dxmin_3b*slp_min_inv;

//injection point into minor fault;
Point(7002)={0, 7-f_min_cor*0.5, -13, cl_10};  
Point(7003)={0, 7+f_min_cor*0.5, -13, cl_10};  
Point(7012)={0, 7-f_min_cor*0.5+dxmin_1, -13+dymin_1, cl_10};  
Point(7013)={0, 7+f_min_cor*0.5+dxmin_1, -13+dymin_1, cl_10};  
Point(7022)={0, 7-f_min_cor*0.5+dxmin_2, -13+dymin_2, cl_10};  
Point(7023)={0, 7+f_min_cor*0.5+dxmin_2, -13+dymin_2, cl_10};  
Point(7032)={0, 7-f_min_cor*0.5+dxmin_3a, -13+dymin_3a, cl_10};  
Point(7033)={0, 7+f_min_cor*0.5+dxmin_3b, -13+dymin_3b, cl_10};  

  
Point(101) ={0, left_margin, bottom, cl_10};  
//Point(1010)={0, 0, -10.+dy5-dy5min, cl_10};  
Point(1012)={0, left_margin,  -10.+dy4-dy4min, cl_10};  
//Point(1014)={0, 0,  -10.+dy3-dy3min, cl_10};  
//Point(1015)={0, 0,  -10.+dy2b-dy2bmin, cl_10}; 
//Point(1040)={0, 0,  -10.+dy2a-dy2amin, cl_10}; 
Point(1044)={0, left_margin,  -10.+dy1, cl_10}; 
Point(104) ={0, left_margin, top, cl_10};  
 
Point(102)={0, width_t-f_dam-f_cor*0.5, top, cl_10};  
Point(1020)={0, 10-f_dam-f_cor*0.5+dx1 , -10.+dy1, cl_10};
Point(1023)={0, 10-f_dam-f_cor*0.5+dx2a , -10.+dy2a, cl_10};
//Point(1024)={0, 10-f_dam-f_cor*0.5+dx2b , -10.+dy2b, cl_10};
Point(1025)={0, 10-f_dam-f_cor*0.5+dx3 , -10.+dy3, cl_10};
Point(1027)={0, 10-f_dam-f_cor*0.5+dx4 , -10.+dy4, cl_10};
Point(1030)={0, 10-f_dam-f_cor*0.5+dx5 , -10.+dy5, cl_10};
Point(103)={0, width_b-f_dam-f_cor*0.5, bottom, cl_10};  

Point(112)={0, width_t-f_cor*0.5, top, cl_10};  
Point(1120)={0, 10-f_cor*0.5+dx1 , -10.+dy1, cl_10};
Point(1123)={0, 10-f_cor*0.5+dx2a , -10.+dy2a, cl_5};
//Point(1124)={0, 10-f_cor*0.5+dx2b , -10.+dy2b, cl_5};
Point(1125)={0, 10-f_cor*0.5+dx3 , -10.+dy3, cl_10};
Point(1127)={0, 10-f_cor*0.5+dx4 , -10.+dy4, cl_10};
Point(1130)={0, 10-f_cor*0.5+dx5 , -10.+dy5, cl_10};
Point(113)={0, width_b-f_cor*0.5, bottom, cl_10};  

Point(122)={0, width_t+f_cor*0.5, top, cl_10}; 
Point(1220)={0, 10+f_cor*0.5+dx1 , -10.+dy1, cl_10};
Point(1223)={0, 10+f_cor*0.5+dx2a , -10.+dy2a, cl_5};
//Point(1224)={0, 10+f_cor*0.5+dx2b , -10.+dy2b, cl_5};
Point(1225)={0, 10+f_cor*0.5+dx3 , -10.+dy3, cl_10};
Point(1227)={0, 10+f_cor*0.5+dx4 , -10.+dy4, cl_10};
Point(1230)={0, 10+f_cor*0.5+dx5 , -10.+dy5, cl_10};
Point(123)={0, width_b+f_cor*0.5, bottom, cl_10};  

Point(132)={0, width_t+f_dam+f_cor*0.5, top, cl_10};
Point(1320)={0, 10+f_dam+f_cor*0.5+dx1 , -10.+dy1, cl_10};
Point(1323)={0, 10+f_dam+f_cor*0.5+dx2a , -10.+dy2a, cl_10};
//Point(1324)={0, 10+f_dam+f_cor*0.5+dx2b , -10.+dy2b, cl_10};
Point(1325)={0, 10+f_dam+f_cor*0.5+dx3 , -10.+dy3, cl_10};
Point(1327)={0, 10+f_dam+f_cor*0.5+dx4 , -10.+dy4, cl_10};
Point(1330)={0, 10+f_dam+f_cor*0.5+dx5 , -10.+dy5, cl_10};
Point(133)={0, width_b+f_dam+f_cor*0.5, bottom, cl_10};  

Point(105)={0, length+left_margin, bottom, cl_10};  
Point(1050)={0, length+left_margin, -10.+dy5, cl_10};  
//Point(1052)={0, length+left_margin, -10.+dy4, cl_10};  
Point(1054)={0, length+left_margin, -10.+dy3, cl_10};  
//Point(1055)={0, length+left_margin, -10.+dy2b, cl_10};  
Point(1060)={0, length+left_margin, -10.+dy2a, cl_10};  
Point(1066)={0, length+left_margin, -10.+dy1, cl_10};  
Point(106)={0, length+left_margin, top, cl_1000};  

Line(1) = {105, 1054};
//Line(2) = {1050, 1052};
//Line(2) = {1052, 1054};
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
Line(33) = {1012, 1044};
Line(35) = {1044, 104};
Line(36) = {105, 133};
Line(37) = {133, 123};
Line(38) = {123, 113};
Line(39) = {113, 103};
Line(40) = {103, 101};
Line(41) = {106, 132};
Line(42) = {132, 122};
Line(43) = {122, 112};
Line(44) = {112, 102};
Line(45) = {102, 104};
Line(46) = {7022, 7012};
Line(47) = {7012, 7002};
Line(48) = {7002, 7032};
Line(49) = {7032, 7033};
Line(50) = {7033, 7003};
Line(51) = {7003, 7013};
Line(52) = {7013, 7023};
Line(53) = {7023, 1027};
Line(54) = {7022, 1025};
Line(55) = {101, 7033};
Line(56) = {7032, 1012};

Line Loop(57) = {-12, -11, -10, -9, -8, -7, -36, 1,4, 5, 6, 41};
Plane Surface(58) = {57}; // RIGHT INTACT;

Line Loop(59) = {28, 29, 30, 45, -35, -33, -56, -48, -47, -46, 54};
Plane Surface(60) = {59}; // TOP LEFT INTACT;

Line Loop(61) = {50, 51, 52, 53, -26, -25, 40, 55};
Plane Surface(62) = {61}; // BOTTOM LEFT INTACT;

Line Loop(63) = {37, 13, 14, 15, 16, 17, 18, -42, -12, -11, -10, -9, -8, -7};
Plane Surface(64) = {63}; // DAMAGE right;
Line Loop(65) = {30, -44, -24, -23, -22, -21, -20, -19, 39, 25, 26, 27, 28, 29};
Plane Surface(66) = {65}; // DAMAGE LEFT;
Line Loop(67) = {24, -43, -18, -17, -16, -15, -14, -13, 38, 19, 20, 21, 22, 23};
Plane Surface(68) = {67}; // faultcore;
Line Loop(69) = {50, 51, 52, 53, 27, -54, 46, 47, 48, 49};
Plane Surface(70) = {69}; // MINOR faultcore;

// define transifinte lines ... to have strucutred-like mesh;
Transfinite Line {6} =4; //top right intact;
Transfinite Line {41} =4; //top horiz right intact;
Transfinite Line {5} =2; //top horiz right intact;
Transfinite Line {4,1} =3; //top horiz right intact;
Transfinite Line {36} =7; //bottom horiz right intact;
Transfinite Line {40,55} =4; //bottom left corner intact;
Transfinite Line {45} =9; //top left corner intact;
Transfinite Line {35,33,56} =4; //left top intact;


Transfinite Line {30,24,18,12} =6; //top faultdamages;
Transfinite Line {29,23,17,11} =8; //top faultdamages;
Transfinite Line {28,22,16,10} =12; //top faultdamages;

Transfinite Line {25,19,13,7} =19; //bottom faultdamages;

Transfinite Line {49,27,9,15,21} =5; // minor fault;
Transfinite Line {53,26,20,14,8} =12; // minor fault;
Transfinite Line {26,20,14,8} =11; // minor fault;
Transfinite Line {50,48} =19 ;//Using Progression 1.15; // minor fault;
Transfinite Line {51,47} =3; // minor fault;
Transfinite Line {52,46} =9; // minor fault;
Transfinite Line {53,54} =13; // minor fault;

Transfinite Line {39, 44} =2; // left damage ;
Transfinite Line {37, 42} =2; // right damage;
Transfinite Line {38,43} =5; // fault core;

// define transifinte surfaces ... to finalize strucutred-like mesh;
// Tell Gmsh what the corner points are(going clockwise or counter-clockwise);
Transfinite Surface {68} = {123,113, 112, 122}; // fault core;
Transfinite Surface {66} = {113, 103, 102,  112};      // left damage ;
Transfinite Surface {64} = {133,  123, 122,  132};     // right damage;
Transfinite Surface {70} = {1025, 1027, 7033, 7032 }; // minor fault;

//Transfinite Surface {62} = {1025, 1027, 7033, 7032 }; // minor fault;
// Recombine the triangles into quads;
Recombine Surface{58,60,62};
Recombine Surface{70,64,66,68};

zdir[] = Extrude{30.0, 0, 0} { Surface{58, 60 , 62 , 64, 66 , 68, 70}; Layers{30}; Recombine;};

Physical Volume(500) = {1};// RIGHT INTACT; 
Physical Volume(501) = {2}; // top left INTACT;
Physical Volume(502) = {3}; // BOTTOM LEFT INTACT;
Physical Volume(503) = {4}; // DAMAGE right;
Physical Volume(504) = {5}; // DAMAGE left;
Physical Volume(505) = {6}; // major fault;
Physical Volume(506) = {7}; // minor fault;
