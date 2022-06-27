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
