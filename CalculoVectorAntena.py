import math

# corriente de dipolos
corriente = [1.41,0.242,0.0418,7.2e-3,1.24e-3,2.13e-4]

# distancia entre dipolos 
distancia = [0,0.53,0.46,0.39,0.34,0.28]

# numero de onda 
b=1.84

# angulos en grados
# modificar el numero para poner mas grados 
angulos = range(50)

def sin_deg(angle_deg):
    """Seno en grados"""
    return math.sin(math.radians(angle_deg))

def cos_deg(angle_deg):
    """Coseno en grados"""
    return math.cos(math.radians(angle_deg))

def tan_deg(angle_deg):
    """Tangente en grados"""
    return math.tan(math.radians(angle_deg))


def fn(angulo_rad) :
    
    interior = cos_deg(angulo_rad) if cos_deg(angulo_rad) != 0 else 0
    interior2 = (math.pi / 2) * interior
    numerador = cos_deg(interior2) if cos_deg(interior2) != 0 else 0
    denominador = sin_deg(angulo_rad) if sin_deg(angulo_rad) != 0 else 0
    
    if denominador == 0:
        return 0
    
    return numerador / denominador

# # Ejemplo de uso:
# parametros de la funcion: grados 
#resultado = fn(30)
#print(f"Resultado de fn(30): {resultado}")

def calculo_vector_antenna(corriente, distancia, theta):
    """Calcula el vector de la antena"""
    
    magnitud = corriente * fn(theta)
    angulo = b * distancia * cos_deg(theta)

    return f"{magnitud} e^j {angulo}"

# # Ejemplo de uso:
# parametros de la funcion: corriente , distancia , grados 
#vector = calculo_vector_antenna(corriente[1], distancia[1], 10)
#print(f"El resultado del vector es: {vector}"


for i, dn in zip(corriente, distancia):
    print(f"""
------------------------------
-> corriente: {i}
-> distancia: {dn}""")
    for theta in angulos:
        resultado = calculo_vector_antenna(i, dn, theta)
        
        print(f"""
angulo: {theta}
vector: {resultado} \n""")
    print("------------------------------")

    