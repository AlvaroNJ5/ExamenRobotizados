import sympy as sp
import funciones_basicas as fb

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
    aux = 0
    solicitud = []
    for a in sp.preorder_traversal(cuaternio):

        if aux == 0:
            aux+=1
            continue
        elif aux == 1:
            solicitud.append(a)
            aux+=1
            continue
        else:
            solicitud.append(-a)
    return sp.Quaternion(solicitud[0],solicitud[1],solicitud[2],solicitud[3])
   
    

    

