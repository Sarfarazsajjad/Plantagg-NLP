For setting up this project please make sure you have a virutal env setup

This project use python verison 3.8.0

Once python virtual env is setup 

pip install -r requirements.txt 

This will install all the project dependecies

Then navigate to folder NLP_Process

For data captured and sanitized from MBG plant site flow goes as follows:

1. First run the the MBG.py file from which sanitized data from mbg-master.csv is read and transformed data is written in mbg-data.csv which contains URLs for plants based on common or botanical name.

2. Then run MBGplantData.py in which plant URLs from previously populated mbg-data.csv is read and transformed plant data is written in MBGPlantDatafinal.csv

3. Then run MBGplantDataV2.py in which previously populated MBGPlantDatafinal.csv is read and transformed data is written in MBGPlantDataV2.csv

4. To run the above process for plants based on common names only run MBGCommonNames.py which will populate data in MBGCommonNames.csv and then based on file name uncomment code in MBGplantDataV2.py accordingly

5. To run the above process for plants based on common names only run MBGBotanicalNames.py which will populate data in MBGBotanicalNames.csv and then based on file name uncomment code in MBGplantDataV2.py accordingly

6. Data from point 4 and 5 are found in files MBGCommonNamesV2.csv and MBGBotanicalNamesV2.csv


Please keep this file updated in the future...
