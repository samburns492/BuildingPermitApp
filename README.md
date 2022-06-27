# BuildingPermitApp
Plotly dash application + Machine Learning Jupyter Notebook

created by Sam Burns

In order to run the dashboard just go to https://capstonebuildingpermit.herokuapp.com/
Enter for user: username
	password: password

The necessary libraries are the lastest versions of the following libraries:
pandas 
numpy 
matplotlib.pyplot 
sklearn 
xgboost as xgb
sklearn.preprocessing 
from sklearn.preprocessing 
plotly.express 
pymongo



If the app fails to load at first try reloading the webage
The main.py file is used to deploy the heroku app


The machine learning algorithm and data processing are all outlined in the Jupyter Notebook located in this folder.
The notebook uses a function to call the two datasets used in the program from a Mongo Database. To enable this fucntionality:

1. The IP needs to be added to an access list by an admin (aka. me) so this isn't function during evaluation.

2. you need to convert the cell to 'Code' in Jupyter Notebook and convert the 'pd.read_csv()' function containing cell into 'Markdown.'

3. Please allow several minutes (<10 minutes) for the notebook to run fully. 

Building permit data can be accessed freely from the City of San Francisco:
The data can be found at https://data.sfgov.org/Housing-and-Buildings/Building-Permits/i98e-djp9. 

The key columns used in the application are the location, permit type, filed date and issued date. This data includes building permits from as far back as 1908 and as 
recent as 2022. The data is cleaned extensively and uploaded to MongoDB. The data is saved in the local submitted folder as “bp_scrubbed.csv.” Which is the same data 
downloaded from the Mongo Atlas DB collection “RealEstateCluster1.”

Housing Sales Data:
Can be accessed via Redfin's website at https://redfin.com/news/data-center

The data that is freely available from Redfin contains 5 years of housing market data including a breakdown of the housing data by metro and county locality. The machine learning model trained for the application uses data generated from roughly January 2017 to December 2022. The data is continuously updated roughly every Thursday meaning the model can be further developed using the same formatted data but more up to date. 
