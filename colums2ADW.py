import pandas as pd

# cargar el ds
df = pd.read_excel("D:\ORACLE\Oracle Content\OCI2021\Telecom\TABLERO ORACLE.xlsx",'Compilado',engine='openpyxl')
print(df.columns)
#trabajar en la cols para que autonomous lo reconozca mas facil
#quitar espacios en blanco
df = df.rename(columns=lambda x: x.strip())
#quitar si existen espacios en blanco por _
# remove spaces in columns name
df.columns = df.columns.str.replace(' ','_')
# rename Pandas columns to upper
df.columns= df.columns.str.upper()
# cambiar acentos
df.columns = df.columns.str.replace('Ñ','N')
print(df.columns)
df.to_csv(r"D:/ORACLE/Oracle Content/temp/data.csv", index=False)
print("Archivo exportado")