A solution to the [House Price Prediction Problem on Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques), trying out five algorithms, namely:

* KNN.
* Polynomial Regression.
* Random Forest.
* AdaBoost.
* Gradient Boosting Tree.

All cross-validated for model selection with Grid Search for hyperparameter optimization. The winner model, GBT, is used in a Flask prediction service, deployed to Heroku on every push with GitHub Actions.

