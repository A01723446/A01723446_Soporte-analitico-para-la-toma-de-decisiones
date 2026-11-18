import pandas as pd

colaboradores = pd.read_excel("Catalogo_Colaboradores.xlsx")
df = pd.DataFrame(colaboradores)

def crearcolumnas():
    df["SalarioDiario"] = df["Sueldo Neto Total"] / 192
    df["CostoInterno"] = df["Sueldo Neto IMSS"] + df["Sueldo Complementos"]
    return

def Limpieza():
    df.columns = df.columns.str.strip()
    return

def estadisticasreferencia():
    SalarioPromedio = df["SalarioDiario"].mean()
    SueldoPromedio = df["Sueldo Neto IMSS"].mean()
    CompensacionPromedio = df["Sueldo Complementos"].mean()
    CostoInternoPromedio = df["CostoInterno"].mean()

    print("Salario promedio:", SalarioPromedio)
    print("Sueldo promedio:", SueldoPromedio)
    print("Compensacion promedio:", CompensacionPromedio)
    print("Costo interno promedio:", CostoInternoPromedio)
    return

def actualiza():
    df.to_excel("archivocambiado.xlsx", index=False)
    return

Limpieza()
crearcolumnas()
estadisticasreferencia()
actualiza()

df.head()