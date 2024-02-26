# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 10:22:22 2023

@author: ferna
"""

# Importacion de Librerias

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import seaborn as sns


from keras.models import Sequential
from keras.layers import Dense


# Importacion del conjunto de datos
dataset = pd.read_csv('C:/Users/ferna/OneDrive/Documentos/Data science/Concrete Mix Design with Neural Network/Database/Database.csv')

X = dataset.iloc[:, :9].values
y = dataset.iloc[:,9:13].values

# Codificacion de datos categoricos
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

labelencoder_X_1 = LabelEncoder()
X[:, 0] = labelencoder_X_1. fit_transform(X[:, 0])

ss_X= MinMaxScaler()
ss_y= MinMaxScaler()
X = ss_X.fit_transform(X)
y = ss_y.fit_transform(y)

def plot_X(X):
    plt.figure(figsize=(10,6))
    sns.boxplot(data=X)
    plt.xticks(rotation=90);
    
    plot_X(X)

# Division de Los datos en datos de entrenamiento y datos de prueba
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size = 0.2,
                                                    random_state = 1)


# Parte 2 - Creacion de la red neuronal!
# Importacion de Librerias y paquetes de keras
import keras
from keras.models import Sequential
from keras.layers import Dense

#Inicializamos la Red Neuronal
red = Sequential ()
#Creamos La capa de entrada
red.add(Dense(
      9,
      input_dim = 9,
      activation = 'sigmoid'
      ))
#ler Capa oculta
red.add(Dense(
        14,
        activation = 'sigmoid'
        ))
#Capa de salida
red.add(Dense(
        4,
        activation= 'linear'
        ))

initial_learning_rate = 0.001
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate,
    decay_steps=1000,
    decay_rate=0.96,
    staircase=True)
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
red.compile(
            optimizer=optimizer,
            loss = 'mse',
            metrics = ['mae','mean_squared_logarithmic_error']
            )
#Entrenamiento
history = red. fit(X_train, y_train,
                   epochs = 1000 ,
                   batch_size= 45,
                   verbose=1,
                   validation_data=(X_test,y_test))
# Prediccion
diseño = pd.read_csv('C:/Users/ferna/OneDrive/Documentos/Data science/Concrete Mix Design with Neural Network/Input/Input.csv')
Z = diseño.iloc[:, 0:9].values

seco=ss_y.inverse_transform(red.predict(ss_X.transform(np.array(Z))))


def plot_history(history):
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Error Absoluto Promedio')
    plt.plot(history.epoch, history.history['loss'],
             label='Train_loss')
    plt.plot(history.epoch, history.history['val_loss'],
             label='Val_loss')
    plt.legend()
    plt.ylim([0,0.2])
    plt.show()
    
    plot_history(history)

def plot_history(history):
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('mae')
    plt.plot(history.epoch, history.history['mae'],
             label='Train_mae')
    plt.plot(history.epoch, history.history['val_mae'],
             label='Val_mae')
    plt.legend()
    plt.ylim([0,0.2])
    plt.show()
    
    plot_history(history)

def plot_history1(history):
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('mean_squared_logarithmic_error')
    plt.plot(history.epoch, history.history['mean_squared_logarithmic_error'],
             label='train_mean_squared_logarithmic_error')
    plt.plot(history.epoch, history.history['val_mean_squared_logarithmic_error'],
             label='val_mean_squared_logarithmic_error')
    plt.legend()
    plt.ylim([0,0.2])
    plt.show()
    plot_history1(history)