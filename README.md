# Data Mining 2 Project - IMDb Movie Analysis

This repository contains the code, datasets, and results for the Data Mining 2 course project at the University of Pisa (MSc in Data Science). The project focuses on comprehensive analysis of IMDb movie data using various machine learning and data mining techniques.

## 📊 Project Overview

This project performs extensive analysis on IMDb movie dataset, covering both **tabular data analysis** and **time series analysis**. The analysis includes:

- **Exploratory Data Analysis (EDA)**
- **Outlier Detection and Handling**
- **Machine Learning Classification**
- **Neural Networks**
- **Ensemble Methods**
- **Time Series Clustering**
- **Motif and Discord Discovery**
- **Explainable AI (XAI)**
- **Advanced Regression Techniques**

## 📁 Local Project Structure

```
├── dataset/                     # Data files
│   ├── imdb.csv                # Main IMDb dataset
│   ├── imdb_ts.csv             # Time series data
│   ├── train_raw.csv           # Raw training data
│   ├── test_raw.csv            # Raw test data
│   └── description.txt         # Dataset description
├── Images/                     # Generated visualizations
├── models/                     # Trained model files
├── best_models/               # Best performing models
├── arrays/                    # Preprocessed arrays
├── backups/                   # Data backups
├── XAI-Lib/                   # Explainable AI library
└── Jupyter Notebooks          # Analysis notebooks
```

## 🎯 Analysis Components

### Tabular Data Analysis

- **TABULAR_EDA.ipynb** - Exploratory Data Analysis
- **TABULAR_OUTLIERS.ipynb** - Outlier detection and handling
- **TABULAR_NN.ipynb** - Neural Network implementation
- **TABULAR_ENSEMBLE.ipynb** - Ensemble methods
- **TABULAR_EXPLAINABLE.ipynb** - Explainable AI analysis
- **TABULAR_IMBALANCED.ipynb** - Handling imbalanced data
- **TABULAR_ADV_REGR.ipynb** - Advanced regression techniques
- **TAB_ML_EXP.ipynb** - Machine learning experiments

### Time Series Analysis

- **TIME_SERIES_EDA.ipynb** - Time series exploratory analysis
- **TIME_SERIES_CLUSTERING.ipynb** - Time series clustering
- **TIME_SERIES_MOTIFS_DISCORDS.ipynb** - Motif and discord discovery

## 📈 Dataset Features

The IMDb dataset includes various features such as:

- **Basic Info**: title, runtime, release year, rating
- **Content Details**: genres, country of origin, title type
- **Engagement Metrics**: number of votes, reviews, ratings
- **Technical Specs**: sound mixes, external links
- **Awards**: nominations and wins
- **Credits**: cast, crew, companies information

## 🛠️ Technologies Used

- **Python** - Primary programming language
- **Pandas & NumPy** - Data manipulation and analysis
- **Scikit-learn** - Machine learning algorithms
- **TensorFlow/Keras** - Neural networks
- **Matplotlib & Seaborn** - Data visualization
- **UMAP & t-SNE** - Dimensionality reduction
- **Optuna** - Hyperparameter optimization
- **XAI Libraries** - Explainable AI techniques

## 👨‍💻 Author

Davide Rizzello - University of Pisa, MSc in Data Science
