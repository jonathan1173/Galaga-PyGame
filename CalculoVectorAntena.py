import math
import pandas as pd

# corriente de dipolos
corriente = [1.41, 0.242, 0.0418, 7.2e-3, 1.24e-3, 2.13e-4]

# distancia entre dipolos 
distancia = [0, 0.53, 0.46, 0.39, 0.34, 0.28]

# número de onda
b = 1.84

# ángulos en grados (puedes modificar para más ángulos)
angulos = range(20)

def sin_deg(angle_deg):
    """Seno en grados"""
    return math.sin(math.radians(angle_deg))

def cos_deg(angle_deg):
    """Coseno en grados"""
    return math.cos(math.radians(angle_deg))

def tan_deg(angle_deg):
    """Tangente en grados"""
    return math.tan(math.radians(angle_deg))

def fn(angulo):
    """
    Calcula la función auxiliar fn para un ángulo dado en grados.
    """
    interior = cos_deg(angulo) if cos_deg(angulo) != 0 else 0
    interior2 = (math.pi / 2) * interior
    numerador = cos_deg(interior2) if cos_deg(interior2) != 0 else 0
    denominador = sin_deg(angulo) if sin_deg(angulo) != 0 else 0
    
    if denominador == 0:
        return 0
    return numerador / denominador

def calculo_vector_antenna(corriente, distancia, theta):
    """
    Calcula la magnitud y la dirección (fase) del vector de la antena para un dipolo
    y un ángulo theta (en grados).
    """
    magnitud = corriente * fn(theta)
    angulo = b * distancia * cos_deg(theta)
    return magnitud, angulo

datos = []  

for idx, (i, dn) in enumerate(zip(corriente, distancia), start=1):
    print(f"------------------------------\nDipolo {idx}:\n-> Corriente: {i}\n-> Distancia: {dn}")
    for theta in angulos:
        magnitud, angulo = calculo_vector_antenna(i, dn, theta)
        print(f"\nÁngulo: {theta}\nVector: {magnitud} e^ {angulo}")
        datos.append({
            "Dipolo": idx,
            "Ángulo (grados)": theta,
            "Magnitud": magnitud,
            "Dirección": angulo
        })
    print("------------------------------")

df = pd.DataFrame(datos, columns=["Dipolo", "Ángulo (grados)", "Magnitud", "Dirección"])

nombre_archivo = "resultado_magnitud_direccion.xlsx"
df.to_excel(nombre_archivo, index=False)

print("\nArchivo Excel generado:", nombre_archivo)
