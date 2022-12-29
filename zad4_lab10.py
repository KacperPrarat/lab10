import pandas as pd 
df=pd.read_csv('miasta (1).csv')
print(df.to_string())


dodatek={'Rok':[2010],
        "Gdansk":[460],
        "Poznan":[555],
        "Szczecin":[405]}

df2=pd.DataFrame(dodatek)

lista=[df,df2]
df3=pd.concat(lista)
print(df3.to_string())
df3.to_csv("miasta2.csv")