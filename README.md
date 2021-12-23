# Overview

A solution to the [House Price Prediction Problem on Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques), trying out five algorithms, namely:

- KNN.
- Polynomial Regression.
- Random Forest.
- AdaBoost.
- Gradient Boosting Tree.

All cross-validated for model selection with Grid Search for hyperparameter optimization. The winner model, GBT, is used in a Flask prediction service, deployed to Heroku on every push with GitHub Actions.

## Prediction Service

To try out the pridection service, send a `POST` request to `https://obada-house-price-prediction.herokuapp.com/predict` with the following body:

```json
{
  "MSSubClass": 20,
  "MSZoning": "RH",
  "LotFrontage": 80,
  "LotArea": 11622,
  "LotShape": "Reg",
  "LandContour": "Lvl",
  "LotConfig": "Inside",
  "LandSlope": "Gtl",
  "Neighborhood": "NAmes",
  "Condition1": "Feedr",
  "Condition2": "Norm",
  "BldgType": "1Fam",
  "HouseStyle": "1.5Story",
  "OverallQual": 5,
  "OverallCond": 1,
  "YearBuilt": 1961,
  "RoofStyle": "Gable",
  "RoofMatl": "CompShg",
  "Exterior1st": "VinylSd",
  "Exterior2nd": "VinylSd",
  "MasVnrType": "None",
  "MasVnrArea": "0",
  "ExterQual": "TA",
  "ExterCond": "TA",
  "Foundation": "CBlock",
  "BsmtQual": "TA",
  "BsmtCond": "TA",
  "BsmtExposure": "No",
  "BsmtFinType1": "Rec",
  "BsmtFinSF1": 468,
  "BsmtFinType2": "LwQ",
  "BsmtFinSF2": 144,
  "BsmtUnfSF": 270,
  "Heating": "GasA",
  "HeatingQC": "TA",
  "CentralAir": "Y",
  "Electrical": "SBrkr",
  "1stFlrSF": 896,
  "LowQualFinSF": "0",
  "GrLivArea": 896,
  "BsmtFullBath": "0",
  "BsmtHalfBath": "0",
  "FullBath": 1,
  "HalfBath": "0",
  "BedroomAbvGr": 2,
  "KitchenAbvGr": 1,
  "KitchenQual": "TA",
  "Functional": "Typ",
  "Fireplaces": "0",
  "FireplaceQu": "NA",
  "GarageType": "Attchd",
  "GarageFinish": "Unf",
  "GarageCars": 1,
  "GarageQual": "TA",
  "GarageCond": "TA",
  "PavedDrive": "Y",
  "WoodDeckSF": 140,
  "OpenPorchSF": "0",
  "EnclosedPorch": "0",
  "3SsnPorch": "0",
  "ScreenPorch": 120,
  "PoolArea": "0",
  "MiscVal": "0",
  "MoSold": 6,
  "YrSold": 2010,
  "SaleType": "WD",
  "SaleCondition": "Normal"
}
```

You should expect a request of the form:

```json
{ "prediction": 106586.82212252892 }
```
