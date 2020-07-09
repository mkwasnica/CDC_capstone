CDC_capstone - Team Pandas

Welcome to the CDC - Natality dataset capstone project.
Our goal is to examine the various maternal and infant helath factors surrounding pregnancy and delivery that result in infants being admitted to intensive care, and share these insights with healthcare policy professionals (hospital executives, government and community health policy makers)
through an interactive dashboard.

This README file will walk through steps to acquire the external data, process and prepare data for examination and visualization in a Python notebook. 

The Interactive Tableau dashboard --> https://public.tableau.com/profile/mohamad.sayed#!/vizhome/NICU_Admittance_15868167993400/NICUAdmittanceVisualization

The Tableau dashboard takes the prepared data and independently recreates the most interesting visualizations found in the Python notebooks. 




Step 1: Clone  a copy of this Git repo if you already haven't.


Step 2:

 Follow the links below and unzip the external data files. Resulting files should be in Fixed Width Format (FWF):

CDC births data 2018: 
ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/natality/Nat2018us.zip
CDC births data 2017:
ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/natality/Nat2017us.zip
CDC births data 2016: 
ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/natality/Nat2016us.zip
CDC births data 2015:
ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/natality/Nat2015us.zip
CDC births data 2014:
ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/natality/Nat2014us.zip

Name each file NatXXXX.txt (XXXX being the year) and put them in the data/external ( Note: this is not same as  the src/data directory)


Step 3: 
	Execute each cell in the CH Parser notebook found in the notebooks directory. Output should be csv files in the data/raw folder.
==============================

NYCDSA capstone project examining CDC data for natality

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
