import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import r2_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
import pickle

import warnings
warnings.filterwarnings("ignore")

def predict():
   


    # Una variable para la ruta, buenas prácticas
    # path_to_data = "./uno.csv"
    # df = pd.read_csv(path_to_data)
    #path_to_data = teclado()


    df["hypertension"] = df["hypertension"].astype(bool)
    df["heart_disease"] = df["heart_disease"].astype(bool)
    df["stroke"] = df["stroke"].astype(bool)
    df["stroke"].value_counts()



    df.isnull().sum(axis = 0)





    categoricas = ["gender", "ever_married", "work_type", "Residence_type", "smoking_status", "hypertension", "heart_disease", "stroke"]
    numericas = ["age", "avg_glucose_level", "bmi"]




    ## se elimina variable objetivo, por que es la que queremos predecir
    X = df.drop("stroke", axis=1)
    y = df["stroke"]

    print("X:\n",X)
    print("y:\n",y)


    X.head()
    y.head()

    #XX.head()
    #yy.head()


    categoricas = ["gender", "ever_married", "work_type", "Residence_type", "smoking_status", "hypertension", "heart_disease"]



        
    carga_transformer = pickle.load(open('transformer_entrenado.pkl', 'rb'))    
    carga_modelo = pickle.load(open('modelo_entrenado.pkl', 'rb'))

    transformer = carga_transformer
    model = carga_modelo
    df = transformer.transform(df)
    print(df)
    predict=model.predict(df)
    return predict

