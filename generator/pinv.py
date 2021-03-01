#!/usr/bin/env python3

import sympy

def get(v, i):
	return globals()[v.name+str(i)]

a = sympy.var("xx xy xz xw yx yy yz yw zx zy zz zw wx wy wz ww", rational = True)
b = sympy.var([ v.name + "2" for v in a], rational=True)
c = sympy.var([ v.name + "3" for v in a], rational=True)
e = sympy.var([ v.name + "4" for v in a], rational=True)
sympy.var(["frac"])

R = sympy.simplify(sympy.Matrix([[xx, yx],[xy, yy],[xz, yz]]).pinv())

for v in a:
	R = R.subs(v*v, globals()[v.name+"2"])

#R = R.subs(-2*xx*xy*yx*yy - 2*xx*xz*yx*yz + xx2*yy2 + xx2*yz2 - 2*xy*xz*yy*yz + xy2*yx2 + xy2*yz2 + xz2*yx2 + xz2*yy2, frac)

#R = R.subs(xy, 0)
R = R.subs(yy, 0)
R = R.subs(xz, 0)
R = R.subs(yz, 0)
#R = R.subs(xy2, 0)
R = R.subs(yy2, 0)
R = R.subs(xz2, 0)
R = R.subs(yz2, 0)

R = R.transpose()

#print(-2*xx*xy*yx*yy - 2*xx*xz*yx*yz + xx2*yy2 + xx2*yz2 - 2*xy*xz*yy*yz + xy2*yx2 + xy2*yz2 + xz2*yx2 + xz2*yy2)
print(R)
print(R[0])
print(R[1])
print(R[2])
print(R[3])
print(R[4])
print(R[5])