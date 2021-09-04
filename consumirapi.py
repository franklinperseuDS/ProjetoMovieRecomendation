#!/usr/bin/env python
# coding: utf-8


## Import Libraries
import pandas as pd
import streamlit as st
import urllib.request
import json

filmes = pd.read_csv("movies.csv")
# título
st.title("Web Data movies Recomendation") 
# subtítulo
st.markdown("equipe: A,F,F,W")
# subtítulo

#['filmeId', 'nota_media', 'Thriller', 'Musical', 'Adventure', 'Western',
       #'Mystery', 'Comedy', 'Fantasy', 'War', 'Animation', 'Romance', 'IMAX',
       #'Horror', 'Crime', 'Action', 'Children', 'Drama', 'Sci-Fi', 'class']

Col1 = st.text_input("filme Id", key="Col1", value=0)
Col2 = st.text_input("Nota", key="Col2", value=0)
Col3 = st.text_input("Thriller", key="Col3", value=0)
Col4 = st.text_input("Musical", key="Col4", value=0)
Col5 = st.text_input("Adventure", key="Col5", value=0)
Col6 = st.text_input("Western", key="Col6", value=0)
Col7 = st.text_input("Mystery", key="Col7", value=0)
Col8 = st.text_input("Comedy", key="Col8", value=0)
Col9 = st.text_input("Fantasy", key="Col9", value=0)
Col10 = st.text_input("War", key="Col10", value=0)
Col11 = st.text_input("Animation", key="Col11", value=0)
Col12 = st.text_input("Romance", key="Col12", value=0)
Col13 = st.text_input("IMAX", key="Col13", value=0)
Col14 = st.text_input("Horror", key="Col14", value=0)
Col15 = st.text_input("Crime", key="Col15", value=0)
Col16 = st.text_input("Action", key="Col16", value=0)
Col17 = st.text_input("Children", key="Col17", value=0)
Col18 = st.text_input("Drama", key="Col18", value=0)
Col19 = st.text_input("Sci-Fi", key="Col19", value=0)
Col20 = st.text_input("class", key="Col20", value=0)

# inserindo um botão na tela
btn_predict = st.button("Realizar Previsão")

if btn_predict:
    data = {
        "Inputs": {
                "input1":
                [
                    {
                            'Col1': Col1,   
                            'Col2': Col2,   
                            'Col3': Col3,   
                            'Col4': Col4,   
                            'Col5': Col5,   
                            'Col6': Col6,   
                            'Col7': Col7,   
                            'Col8': Col8,   
                            'Col9': Col9,   
                            'Col10': Col10,   
                            'Col11': Col11,   
                            'Col12': Col12,   
                            'Col13': Col13,   
                            'Col14': Col14,   
                            'Col15': Col15,   
                            'Col16': Col16,   
                            'Col17': Col17,   
                            'Col18': Col18,   
                            'Col19': Col19,   
                            'Col20': Col20,   
                              
                    }
                ],
        },
        "GlobalParameters":  {
     }
    }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/88cee1267b3f4781be5764f390ed1fa2/services/44e7c9a8cbad464bb360b96f4cba0fc9/execute?api-version=2.0&format=swagger'
    api_key = 'nEt2xrG1hoA+R5/YqEj67p8nvIiChhJkOMENUe8CyPcRZ3ti+jnJAtHqnVjN1a3+A/2gN2kzdbPhedJT35IP8g==' # Replace this with the API key for the web service
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
        #print(m['Scored Labels'])
             
        if m['Scored Labels'] == '1':
            st.markdown("Previsão de Risco = Baixo Risco")
        else:
            st.markdown("Previsão de Risco = Alto Risco")
            
       
                 
        
            
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
else:
    print("error")
    
	
	
