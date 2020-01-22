For setting up this project please make sure you have a virutal env setup

This project use python verison 3.8.0

Once python virtual env is setup 

pip install -r requirements.txt 

This will install all the project dependecies

Then navigate to folder NLP_Process

For data captured and sanitized from MGB plant site flow goes as follows:

1. First run the the MGB.py file from which sanitized data from mgb-master.csv is read and transformed data is written in mgb-data.csv

2. Then run MGBplantData.py in which previously populated mgb-data.csv is read and transformed data is written in MGBPlantDatafinal.csv

3. Then run MGBplantDataV2 in which previously populated MGBPlantDatafinal.csv is read and transformed data is written in MGBPlantDataV2.csv