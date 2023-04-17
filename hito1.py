import pandas as pd

#NOTA: con matplotlib se podrian graficar algunos datos

# *** Data frame de usuarios ***

user_df = pd.read_csv('users_filtered.csv')
user_df_final = user_df[['username','user_id','user_completed','user_onhold'\
                        ,'user_dropped','user_plantowatch','gender','birth_date']]

# Exploracion de datos

dim_user = user_df_final.shape
print("dimensiones tabla usuarios = " + str(dim_user))
#print(user_df_final.describe()) # Estadisticas de los datos
#print(user_df_final.info()) # Tipos de los datos y cantidas de no-nulos

# Conversion a csv

#user_df_final.to_csv('users_df.csv', index=False)



# *** Data frame de lista de animes ***

anime_df = pd.read_csv('anime_filtered.csv')
anime_df_final = anime_df[['anime_id','title','type','source','episodes','aired'\
                           ,'duration','rating','score','scored_by','rank','popularity'\
                           ,'members','producer','licensor','studio','genre','opening_theme'\
                           ,'ending_theme']]

# Exploracion de datos

dim_anime = anime_df_final.shape
print("dimensiones tabla animes = " + str(dim_anime))
#print(anime_df_final.describe()) # Estadisticas de los datos
#print(anime_df_final.info()) # Tipos de los datos y cantidas de no-nulos

# Conversion a csv

#anime_df_final.to_csv('anime_df.csv', index=False)






