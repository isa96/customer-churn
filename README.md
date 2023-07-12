# Customer Churn Classification

This project aims to built classification churn of customer based on transaction data, *visit* data & *login* data


# Brief Summary of Project

The flow of this *project*, first EDA (*Exploratory Data Analysis*) to find out the basic picture of the *dataset*. 
Second, *cleaning* and *preprocessing* of the *dataset*. Third, built 4 Neural Network Model (Sequential Neural Network, 
Improvement Sequential Neural Network, Functional Neural Network, Improvement Functional Neural Network) and 
choose Improvement Functional Neural Network as Best Model. Result of the model using Neural Network with own architecture shows 90% Accuracy and 
F1-Score 91% on test-set


# Project Conclusion

1. The `Recall` in the *train-set* and *validation-set* are quite close and have high values (0.95 & 0.94). Which means the model is stable/*reliable* in calculating the `Recall` value.
2. The `ROC-AUC` on the *train-set* and *validation-set* is quite close and has a high value (0.97). Which means the model is stable/*reliable* in calculating the `ROC-AUC` value.
3. The *Loss* of *train-set* and *validation-set* are quite close and have a low value (0.16). Which means the model can classify *churn* well.
4. The `Recall` value for *churn* class in *train-set* (last epoch) and *test-set* are not much different. For *train-set* it is 0.90 and for *test-set* it is 0.95. Which means the model is *goodfit*
5. Based on the *AUC* value (0.90), it can be concluded that the model is not influenced by *treshold*.
6. The model has 91% accuracy (Can classify the *churn* class well) 
