import math
import cmath
import pandas as pd

# corriente de dipolos
corriente = [0.668,0.666,0.664,0.663,0.661]

# distancia entre dipolos 
distancia = [0,0.493,0.401,0.326,0.265]

# numero de onda 
b=1.84

# angulos en grados
# modificar el numero para poner mas grados 
angulos = range(0,359,10)

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


def calculo_vector_antenna(corriente, distancia, theta):
    """Calcula el vector de la antena y lo retorna como número complejo."""
    magnitud = corriente * fn(theta)
    angulo_deg = b * distancia * cos_deg(theta)
    angulo_rad = math.radians(angulo_deg)
    
    return magnitud * cmath.exp(1j * angulo_rad)

datos = []  # Lista para almacenar los resultados de la suma de vectores

for theta in angulos:
    print(f"ángulo: {theta}")
    suma = 0 + 0j  # Inicializar la suma para evitar errores con los angulos 
    for i, dn in zip(corriente, distancia):
        print(f"corriente: {i}, distancia: {dn}")
        vector = calculo_vector_antenna(i, dn, theta)
        suma += vector
        
        mag, ang = cmath.polar(vector)
        print(f"vector: {mag:.3f} ∠ {math.degrees(ang):.3f}°\n")
    
    # Convertir la suma a forma polar
    magnitud_total, angulo_total_rad = cmath.polar(suma)
    angulo_total_deg = math.degrees(angulo_total_rad)
    # Mostrar el resultado en notación x∠y
    print(f"Vector suma: {magnitud_total:.3f} ∠ {angulo_total_deg:.3f}°")
    print("------------------------------")

    datos.append({
        "Ángulo (grados)": theta,
        "geogebra": f"({magnitud_total},{angulo_total_deg})"
    })

# crear exel

df = pd.DataFrame(datos)

nombre_archivo = 'resultado_suma_vectores.xlsx'

df.to_excel(nombre_archivo, index=False)

print(f"Archivo Excel '{nombre_archivo}' creado exitosamente.")
