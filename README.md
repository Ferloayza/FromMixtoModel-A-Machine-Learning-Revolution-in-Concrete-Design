# Neural Networks for concrete mix design

## About the project

The project is originally written in Spanish, and the focus is primarily on concrete mix design. However, I am going to explain the process of data science but if you want to check the original project, you can click this [link](https://repositorio.ucsm.edu.pe/handle/20.500.12920/12366 "link") and check it. 

This project is a research that proposes an alternative to conventional concrete mix designs methods using neural networks. Usually there are different methods for designing, and we wanted to create a new method which is basically generated from different methods who have been already made, combine them and find a new alternative.

You need different data to design concrete, material properties mainly, but methods for concrete design use different properties, and they don´t usually share all the data they need for the design. But this project tries to collect the main data they all share in order to generate a database which contains the main researches about concrete design in the city of Arequipa in Peru.

## Project Scope

Something I want to clarify before continuing is that we made this project very limited in data terms because the research focused mainly on a Civil engineer perspective, so we used just the data we found in the city of Arequipa.

## Motivation

Well, you just need to know something about concrete design. You must have different material properties (Concrete, aggregates, water) and with some math process, the design tells you how much cement, water, rocks and sand you have to mix in order to have a specific concrete resistance. Introduce data to obtain data back, that’s why we decided to use neural networks. We thought all that math process different concrete design methods use, could be done by a computer.

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

[![](https://github.com/Ferloayza/NeuroMix-Designing-Concrete-with-AI/assets/158125362/26c404ed-0d1a-4ca8-9ad4-124714f3167f)](https://numpy.org/ "Numpy")

[![](https://github.com/Ferloayza/NeuroMix-Designing-Concrete-with-AI/assets/158125362/13404df9-50c1-41e7-948a-554dc152ae3b)](https://matplotlib.org/ "Matplotlib")

[![](https://github.com/Ferloayza/NeuroMix-Designing-Concrete-with-AI/assets/158125362/4f6cc6e3-b4c4-491b-b61f-79a86b2ebdaf)](https://pandas.pydata.org/ "Pandas")

[![](https://github.com/Ferloayza/NeuroMix-Designing-Concrete-with-AI/assets/158125362/7c83624b-5c54-4d53-a149-fdf69c1a3dd9)](https://www.tensorflow.org/ "Tensorflow")

[![](https://github.com/Ferloayza/NeuroMix-Designing-Concrete-with-AI/assets/158125362/f5e626e1-ebf3-4eb2-97b1-954c09203acc)](https://seaborn.pydata.org/ "Seaborn")

[![](https://github.com/Ferloayza/NeuroMix-Designing-Concrete-with-AI/assets/158125362/c63c8b9b-8ba7-408a-8fc9-69dc30820516)](https://scikit-learn.org/stable/ "Scikit-Learn")

[![](https://github.com/Ferloayza/NeuroMix-Designing-Concrete-with-AI/assets/158125362/ff69e08f-ea41-484f-83d2-39e0f3bbbc3a)](https://keras.io/ "Keras")
