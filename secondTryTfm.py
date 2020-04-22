import pickle
import bson
import pandas as pd


#%%
#Cargamos los datos de los usuarios, y tomamos solo un trozo de los datos para no guardarlo todo.

filename = "usuarios.pickle"
usuarios = pd.read_pickle(filename)

usuariosMuestra = usuarios.iloc[range(0,50000),]

usuariosMuestra.head(5)

#Machacamos la variable usuarios con un 0 para que no ocupe mucha memoria
usuarios = 0
# %%
#Cargamos los datos de los tweets.
filename = "tweets.pickle"
tweets = pd.read_pickle(filename)

#Todos los ids de los usuarios de la muestra
idsMuestra = usuariosMuestra["_id"].to_list()

#Solo nos quedamos con las interacciones que se hayan realizado entre un par de 
#usuarios cuyos ids hayamos cogido antes.
tweetsMuestra = tweets[tweets.user_id.isin(idsMuestra)
                       & (tweets.in_reply_to_user_id.isin(idsMuestra) | 
                            tweets.retweet_or_quote_user_id.isin(idsMuestra))]

#Machacamos los datos de tweets original para que no ocupe memoria
tweets = 0
#%%
#Primero vamos a crear un diccionario, que contendrá todas las interacciones 
#que se hayan realizado entre todo par de usuarios

#Definimos el diccionario en el que vamos a guardar todas las interacciones de
#cada usuario.
 
userInter = {}

for u in idsMuestra:
    userInter[u] = {"quote" : [], "retweet" : [], "reply" : [], "followers" : []}



for u in idsMuestra:
    
    for follower in list(usuariosMuestra.loc[u]["followers"]):
        
        if (follower in idsMuestra):
            userInter[u]["followers"].append(follower)

#%%
dict = {3: "D", "b":"B", "c":"C", "e" : {"j" : "J", "a" : "A"}}

print("d" in dict)

dict["f"] = "F"

for i in dict:
    print(i)

#%%
a = 14
b = 125 
ab = "(" + str(a) + "," + str(b) + ")"
print(ab)
    
#%%    
#index
print(list(tweetsMuestra.columns.values))

#%%

print(tweetsMuestra.loc[6101440]["tweet_type"])

#%%
for follower in list(usuariosMuestra.iloc[4][3]):
    print(follower)

#%%
print(int(tweetsMuestra.loc[6101440]["user_id"]))
#%%

for user, user_group in usuariosMuestra.groupby("_id", axis = 1):
    for 
#%%   
