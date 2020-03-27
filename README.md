For setting up this project please make sure you have a virutal env setup

This project use python verison 3.8.0


For mac setup run the following from terminal
1. brew install pyenv
2. pyenv install 3.8.0
3. pyenv global 3.8.0
4. pyenv exec python -m venv venv3.8.0
5. source venv3.8.0/bin/activate
6. python --version to see 3.8.0

Once python virtual env is setup install project dependencies 

pip install -r requirements.txt 

Then navigate to folder NLP_Process and ignore other code..

For data captured and sanitized from MBG plant site flow goes as follows:

1. First run the the MBG.py file from which sanitized data from mbg-master.csv is read and transformed data is written in mbg-data.csv which contains URLs for plants based on common or botanical name.

2. Then run MBGplantData.py in which plant URLs from previously populated mbg-data.csv is read and transformed plant data is written in MBGPlantDatafinal.csv

3. Then run MBGplantDataV2.py in which previously populated MBGPlantDatafinal.csv is read and transformed data is written in MBGPlantDataV2.csv

4. To run the above process for plants based on common names only run MBGCommonNames.py which will populate data in MBGCommonNames.csv and then based on file name uncomment code in MBGplantDataV2.py accordingly

5. To run the above process for plants based on common names only run MBGBotanicalNames.py which will populate data in MBGBotanicalNames.csv and then based on file name uncomment code in MBGplantDataV2.py accordingly

6. Data from point 4 and 5 are found in files MBGCommonNamesV2.csv and MBGBotanicalNamesV2.csv


7. Made v3-data folder that beaks down master file of 34k records in to 250 records each with data-<1-181> so that extracting data would be easy in case of loss of connection.

8. Total of only 2k plants were found from the provided list of 34k Plants please run  



Please keep this file updated in the future...
