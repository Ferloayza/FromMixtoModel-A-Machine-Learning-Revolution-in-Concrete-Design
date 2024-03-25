# From Mix to Model: A Machine Learning Revolution in Concrete Design

## About the project

The project is originally written in Spanish, and the focus is primarily on concrete mix design. However, I am going to explain the process of data science but if you want to check the original project, you can click this [link](https://repositorio.ucsm.edu.pe/handle/20.500.12920/12366 "link") and check it. 

This research project introduces an innovative approach to concrete mix design, leveraging neural networks to revolutionize traditional methodologies. Rather than adhering to a singular design method, we amalgamate various existing techniques, harnessing their collective wisdom to forge a novel alternative

To design concrete properly, you need different kinds of data, mainly about the materials you're using. But the methods people use for concrete design often rely on different sets of data, and they don't always share all the information they use. This project is about gathering the most important data that all these methods have in common. We're building a database that brings together the key research findings on concrete design in Arequipa, Peru.

## Project Scope

Before we proceed further, I'd like to clarify that our project deliberately limited its scope in terms of data. It primarily focused on the perspective of civil engineering. Therefore, we only utilized the data available within the city of Arequipa

## Motivation

To understand concrete design, you need to grasp various material properties like concrete, aggregates, and water. Through mathematical processes, the design indicates the ideal proportions of cement, water, rocks, and sand required to achieve a specific strength for the concrete. We chose to employ neural networks because they enable us to input data and receive precise design information in return. We believed that the computational tasks involved in the diverse methods of concrete design could be effectively handled by a computer.

## Process Summary

We made a database with the main researches about concrete design in Arequipa.

We trained our Neural Network with the data, and were able to create a new method for designing concrete, but we didn´t just create this neural network able to design concrete, we made the process in the laboratory in order to find out if the Neural Network was actually working.

Basically the Neural Network told us how much cement, water, rocks and sand we had to use to obtain a 210kg/cm2 concrete resistance. 

We tested it in the laboratory, and we verified that it worked. 

## Database

Different mix designs require different data, some of them include properties that others do not, we had to clean the data, and use properties every mix design share. And we made 2 neural networks.

As mentioned before, our project scope was limited, so our database is made up of 190 data.

We tried to make a neural network able to design any conventional concrete resistance (usually between 175 kg/cm2 – 280 kg/cm2 in the city of Arequipa). So the data we needed was basically mix designs of 175 kg/cm2, 210 kg/cm2 280 kg/cm2.

However, we couldn´t find as much data of 175 kg/cm and 280 kg/cm2, as we found of 210 kg/cm2. And this are the percentages:

- 175 kg/cm2 = 10%
- 210 kg/cm2 = 74%
- 280 kg/cm2 = 16%

Notice that 210 kg/cm2 resistance represents 74% of the data. One of our hypotheses was that this might cause overfitting and it did.

## Input Data used

The first one includes this data as input variables:

- Specific weight of cement
- Loose unit weight of fine aggregate (sand)
- Compacted unit weight of fine aggregate (sand)
- Dry specific weight of fine aggregate (sand)
- Fineness module of fine aggregate (sand)
- Loose unit weight of coarse aggregate (rock)
- Compacted unit weight of coarse aggregate (rock)
- Dry specific weight of coarse aggregate (rock)
- Fineness module of coarse aggregate (rock)
- Nominal maximum size
- Compression Resistance at 28 days
- Slump
- Air percentage

That was all the data the mix designs we used in the city of Arequipa shared, but when we made the tests, the results weren’t what we expected. So, we decided to eliminate some data. Our second and final neural network had these input data:

- Cement Brand
- Specific weight of cement
- Dry specific weight of fine aggregate (sand)
- Fineness module of fine aggregate (sand)
- Dry specific weight of coarse aggregate (rock)
- Fineness module of coarse aggregate (rock)
- Nominal maximum size
- Compression Resistance at 28 days
- Slump

## Output Data

The output data is what civil engineers need to mix the concrete and use it. 

- Cement weight
- Fine aggregate weight
- Coarse aggregate weight
- Water weight 

## Technologies Used

- TensorFlow
- Pandas
- Keras
- Scikit-learn
- Matplotlib

## Results and Conclusions

There are 6 designs we made
We had two different sets of materials, and for each set, we made 3 concrete designs. 175, 210 and 280 kg/cm2.
This is for you to understand the input data! All of the data was tested in the lab.

Cement Brand  | Specific Weight of Cement  | Dry Specific Weight of fine Aggregate  | Fineness module of Fine Aggregate  | Dry Specific Weight of coarse Aggregate  | Fineness module of Coarse Aggregate  | Nominal Maximum Size  | Concrete Strength at 28 days  | Slump   
------------- | -------------- | -------------
Content Cell  | Content Cell   | -------------dsd
Content Cell  | Content Cell   | -------------  

First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell 
