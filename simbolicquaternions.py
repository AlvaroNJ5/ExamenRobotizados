import sympy as sp
import funciones_basicas as fb
import pyquaternion as pq
def quaternion_simbolico(axis : list, angle):
    'Devuelve u cuaternion que permite variables simbolicas'
    cuat = fb.simplifica_cuat_simbolico([sp.cos(angle/2), sp.sin(angle/2)*axis[0], sp.sin(angle/2)*axis[1], sp.sin(angle/2)*axis[2]])
    return sp.Quaternion(cuat[0],cuat[1],cuat[2],cuat[3])

def quaternion_simbolico_normalizado(axis : list, angle):
    norma = sp.sqrt(axis[0]**2+axis[1]**2+axis[2]**2)
    axis2 = []
    for dato in axis:
        axis2.append(dato/norma)
    cuat = fb.simplifica_cuat_simbolico([sp.cos(angle/2), sp.sin(angle/2)*axis2[0], sp.sin(angle/2)*axis2[1], sp.sin(angle/2)*axis2[2]])
    return sp.Quaternion(cuat[0],cuat[1],cuat[2],cuat[3])

def conjugado_cuaternio(cuaternio):
    return sp.Quaternion(cuaternio.args[0], -cuaternio.args[1],-cuaternio.args[2],-cuaternio.args[3])

   
def tras_rot_moviles(cuaternion, r : list, p : list):
    amp = sp.Symbol('amp')
    if type(cuaternion) == type(sp.Quaternion(amp,2,3,4)):
        return (cuaternion.mul(sp.Quaternion(0,r[0],r[1],r[2]))).mul(conjugado_cuaternio(cuaternion)) + sp.Quaternion(0,p[0],p[1],p[2])
    else:
        return cuaternion*pq.Quaternion(scalar=None, vector=r)*cuaternion.conjugate + pq.Quaternion(scalar=None, vector=p) 

def tras_rot_fijos(cuaternion, r : list, p : list):
    amp = sp.Symbol('amp')
    if type(cuaternion) == type(sp.Quaternion(amp,2,3,4)):
        return cuaternion.mul(sp.Quaternion(0,r[0]+p[0],r[1]+p[1],r[2]+p[2])).mul(conjugado_cuaternio(cuaternion))
    else:
        return cuaternion*pq.Quaternion(scalar=None, vector=[r[0]+p[0],r[1]+p[1],r[2]+p[2]])*cuaternion.conjugate   

def rot_tras_moviles(cuaternion, r : list, p : list):
    amp = sp.Symbol('amp')
    if type(cuaternion) == type(sp.Quaternion(amp,2,3,4)):
        return cuaternion.mul(sp.Quaternion(0,r[0]+p[0],r[1]+p[1],r[2]+p[2])).mul(conjugado_cuaternio(cuaternion))
    else:
        return cuaternion*pq.Quaternion(scalar=None, vector=[r[0]+p[0],r[1]+p[1],r[2]+p[2]])*cuaternion.conjugate   

def rot_tras_fijos(cuaternion, r : list, p : list):
    amp = sp.Symbol('amp')
    if type(cuaternion) == type(sp.Quaternion(amp,2,3,4)):
        return cuaternion.mul(sp.Quaternion(0,r[0],r[1],r[2])).mul(conjugado_cuaternio(cuaternion)) + sp.Quaternion(0,p[0],p[1],p[2])
    else:
        return cuaternion*pq.Quaternion(scalar=None, vector=r)*cuaternion.conjugate + pq.Quaternion(scalar=None, vector=p) 
