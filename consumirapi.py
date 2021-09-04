#!/usr/bin/env python
# coding: utf-8


## Import Libraries
import pandas as pd
import streamlit as st
import urllib.request
import json

filmes = pd.read_csv("movies.csv")
classes_filmes = pd.read_csv("filmes-Final.csv")


# título
st.title("Web Movies Recomendation") 
# subtítulo
st.markdown("equipe: Adiel Silva,Felipe Brasil,Franklin Perseu,William dos Santos")
# subtítulo
st.markdown("Trabalho de apresentação para o módulo de computing clouding")

#['filmeId', 'nota_media', 'Thriller', 'Musical', 'Adventure', 'Western',
       #'Mystery', 'Comedy', 'Fantasy', 'War', 'Animation', 'Romance', 'IMAX',
       #'Horror', 'Crime', 'Action', 'Children', 'Drama', 'Sci-Fi', 'class']

filmeId = st.text_input("filme Id", key="filmeId", value=0)
Thriller = st.text_input("Thriller", key="Thriller", value=0)
Musical = st.text_input("Musical", key="Musical", value=0)
Adventure = st.text_input("Adventure", key="Adventure", value=0)
Western = st.text_input("Western", key="Western", value=0)
Mystery = st.text_input("Mystery", key="Mystery", value=0)
Comedy = st.text_input("Comedy", key="Comedy", value=0)
Fantasy = st.text_input("Fantasy", key="Fantasy", value=0)
War = st.text_input("War", key="War", value=0)
Animation = st.text_input("Animation", key="Animation", value=0)
Romance = st.text_input("Romance", key="Romance", value=0)
IMAX = st.text_input("IMAX", key="IMAX", value=0)
Horror = st.text_input("Horror", key="Horror", value=0)
Crime = st.text_input("Crime", key="Crime", value=0)
Action = st.text_input("Action", key="Action", value=0)
Children = st.text_input("Children", key="Children", value=0)
Drama = st.text_input("Drama", key="Drama", value=0)
SciFi = st.text_input("Sci-Fi", key="SciFi", value=0)
FilmNoir = st.text_input("Film-Noir", key="FilmNoir", value=0)
Documentary = st.text_input("Documentary", key="Documentary", value=0)
# inserindo um botão na tela
btn_predict = st.button("Realizar Previsão")

if btn_predict:
    data = {
        "Inputs": {
                "input1":
                [
                    {
                        'Column 0': "0",
                        'filmeId': filmeId,   
                        'nota_media': "5",  
                        'Horror': Horror,   
                        'Crime': Crime,   
                        'Children': Children,   
                        'Thriller': Thriller,   
                        'Film-Noir': FilmNoir,   
                        'Documentary': Documentary,   
                        'Fantasy': Fantasy,   
                        'Mystery': Mystery,   
                        'Comedy': Comedy,   
                        'Drama': Drama,   
                        'Musical': Musical,   
                        'Adventure': Adventure,   
                        'Romance': Romance,   
                        'War': War,   
                        'Animation': Animation,   
                        'IMAX': IMAX,   
                        'Action': Action,   
                        'Western': Western,   
                        'Sci-Fi': SciFi,   
                        'class': "0",     

                               
                             
                            
                    }
                ],
        },
        "GlobalParameters":  {
     }
    }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/88cee1267b3f4781be5764f390ed1fa2/services/f1e5d50315564cc3ab193edfeea56489/execute?api-version=2.0&format=swagger'
    api_key = '6WkC96kzPJulU1jWjo76ZqZUVmBKiqrB6Adk7rROj/EKvEVVkfu3z45A/iSPpayY7aUM1T5bgr4NgPkzov5N6Q==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        print(result )
        parsed_json = (json.loads(result))

        print(parsed_json)
        y = json.loads(json.dumps(parsed_json, indent=4, sort_keys=True))
        x = y['Results']
        z = x['output1']
        m = z[0]

        #st.markdown("A classe do filme" ,m['Scored Labels'])
        label_retorno = int(m['Scored Labels'])
        
        
        classes_filmes =  classes_filmes[classes_filmes["class"] == label_retorno]
        
        
        # classes_filmes = classes_filmes[classes_filmes["nota_media"] > 3]
        classes_filmes = classes_filmes.sample(n=5)
        for i in range(5):
            st.markdown(filmes["title"][filmes["movieId"] == classes_filmes.iloc[i,0]].values)
        
            
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
else:
    print("error")
    
	
	
