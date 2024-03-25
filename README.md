# From Mix to Model: A Machine Learning Revolution in Concrete Design

## About the project

The project is originally written in Spanish, and the focus is primarily on concrete mix design. Here I will review a small summary, but the data science detailed process is explained in this [Jupyter Notebook in Kaggle](https://www.kaggle.com/code/fernandoloayzacceres/designing-concrete-using-ann "link")  and if you want to check the original project, you can click this [link](https://repositorio.ucsm.edu.pe/handle/20.500.12920/12366 "link") and check it. 

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

Cement Brand | Specific Weight of Cement | Dry Specific Weight of fine Aggregate | Fineness module of Fine Aggregate | Dry Specific Weight of coarse Aggregate | Fineness module of Coarse Aggregate | Nominal Maximum Size | Concrete Strength at 28 days | Slump
------------- | -------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- 
3 |2850 | 2596.42459 | 2.42 | 2715.18145 | 6.17 | 0.5 | 245 | 4
3 |2850 | 2596.42459 | 2.42 | 2715.18145 | 6.17 | 0.5 | 294 | 4
3 |2850 | 2596.42459 | 2.42 | 2715.18145 | 6.17 | 0.5 | 364 | 4
3 |2850 | 2445.77632 | 3.18 | 2500.30754 | 6.93 | 0.75 | 245 | 4
3 |2850 | 2445.77632 | 3.18 | 2500.30754 | 6.93 | 0.75 | 294 | 4
3 |2850 | 2445.77632 | 3.18 | 2500.30754 | 6.93 | 0.75 | 364 | 4

245, 294 and 364 values correspond to 175, 210 and 280 values respectively, this is due to the security factor you must apply when designing concrete! Number 3 in Cement Brand represents "YURA IP".

And this is the output data:

Design Name | Cement Weight | Fine Aggregate Weight | Coarse Aggregate Weight | Water Weight 
------------- | -------------- | ------------- | ------------- | ------------- 
B-175 |408.52 | 833.97 | 769.34 | 233.29
B-210 |436.17 | 820.14 | 749.34 | 235.80
B-280 |480.01 | 780.96 | 739.33 | 239.42
L-175 |351.73 | 650.77 | 1009.54 | 198.08
L-210 |391.54 | 623.67 | 988.33 | 200.77
L-280 |440.55 | 587.81 | 968.45 | 205.82

### FIRST CONCLUSION

When designing concrete, there is an unbreakable pattern! To achieve greater concrete strength, a lower water-to-cement ratio is required.
And our neural network unraveled this pattern all on its own, notice how the water-to-cement ratio decreases as concrete strength requirements increase.

Next, we validated these results in the lab to confirm the functionality of the neural network and ensure that the generated designs were logical and practical.
Subsequently, the table below presents the concrete strength test results.

Design Name | Concrete Strength at 28 days
------------- | -------------- 
B-175 | 185.83
B-210 | 211.53
B-280 | 236
L-175 | 192.27
L-210 | 215.43
L-280 | 246.33

### SECOND CONCLUSION

Observe that our concrete designs were engineered to meet a safety factor requirement. What's noteworthy is that the results, consistent with numerous concrete design studies, underscore the necessity of incorporating a safety factor. So we must say, the Neural Network also learned the fact that every design needs security factor.

### THIRD CONCLUSION

Looking at the results, we noticed a pattern: 280 designs fell short, 210 barely made it, and 175 exceeded expectations. This suggests our Neural Network may have focused too much on designs like the 210 ones and not enough on the 175 and 280 cases, which indicates overfitting.
