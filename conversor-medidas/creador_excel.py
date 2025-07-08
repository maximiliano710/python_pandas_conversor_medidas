import pandas as pd

# dataframe es la informacion basica de la piezas y centimetros para poder armar el Excel

data = {
    "Piezas:" : ["Pata","Tablero","Puerta","Estante","Panel Lateral"],
    "Centimetros:" : [40,120,60,30,180]
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel

df.to_excel("muebles_medidas.xlsx", index=False)