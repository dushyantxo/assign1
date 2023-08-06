import numpy as np

a=np.array([1,-1])
b=np.array([-4,6])
c=np.array([-3,-5])

m_ab=b-a
m_ac=c-a
print("slope of ab and ac")
print(m_ab,m_ac)

m_be=-np.flip(m_ac)
m_cf=-np.flip(m_ab)
print("slope of be and cf")
print(m_be,m_cf)

import sympy as sp

x, y,  = sp.symbols('x y ')

d=sp.Matrix([x, y])
print("variable matrix")
print(d)

d_transpose=np.transpose(d)

result=np.cross((d_transpose-b),(m_be))

#print(result)

print("equation of be")
print(f"{d_transpose-a}.{m_be}=0")

result1=np.cross((d_transpose-c),(m_cf))

#print(result1)

print("equation of cf")
print(f"{d_transpose-b}.{m_cf}=0")
