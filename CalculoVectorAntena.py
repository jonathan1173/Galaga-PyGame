import math
import pandas as pd
import cmath

# Corriente de dipolos
corriente = [0.668, 0.666, 0.664, 0.663, 0.661]

# Distancia entre dipolos 
distancia = [0, 0.493, 0.401, 0.326, 0.265]

# Número de onda
b = 1.84

# Ángulos en grados
angulos = range(0, 359, 10)

def sin_deg(angle_deg):
    """Seno en grados"""
    return math.sin(math.radians(angle_deg))

def cos_deg(angle_deg):
    """Coseno en grados"""
    return math.cos(math.radians(angle_deg))

def fn(angulo):
    """
    Calcula la función auxiliar fn para un ángulo dado en grados.
    """
    interior = cos_deg(angulo) if cos_deg(angulo) != 0 else 0
    interior2 = (math.pi / 2) * interior
    numerador = cos_deg(interior2) if cos_deg(interior2) != 0 else 0
    denominador = sin_deg(angulo) if sin_deg(angulo) != 0 else 0
    return 0 if denominador == 0 else numerador / denominador

def calculo_vector_antenna(corriente, distancia, theta):
    """
    Calcula la contribución de un dipolo en un ángulo dado (theta).
    Retorna el valor en forma compleja.
    """
    magnitud = corriente * fn(theta)
    fase = b * distancia * cos_deg(theta)
    return magnitud * cmath.exp(1j *  math.radians(fase))  # Representación en coordenadas complejas

# Lista para almacenar los resultados
datos = []
for theta in angulos:
    vector_total = sum(calculo_vector_antenna(i, dn, theta) for i, dn in zip(corriente, distancia))
    magnitud_total = abs(vector_total)  # Magnitud del vector resultante
    angulo_total = math.degrees(cmath.phase(vector_total))  # Fase en grados
    
    print(f"Ángulo: {theta}° -> Magnitud total: {magnitud_total:.6f}, Dirección total: {angulo_total:.6f}°")
    
    datos.append({
        "Ángulo (grados)": theta,
        "Magnitud Total": magnitud_total,
        "Dirección Total (grados)": angulo_total,
        "geogebra": f"({magnitud_total},{angulo_total})"
    })

# Crear DataFrame y exportar a Excel
df = pd.DataFrame(datos)
nombre_archivo = "patron_radiacion_total.xlsx"
df.to_excel(nombre_archivo, index=False)

print("\nArchivo Excel generado:", nombre_archivo)
