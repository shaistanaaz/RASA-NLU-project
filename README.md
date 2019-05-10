# RASA-NLU-project
It is an automated bot that can response different categories of questions with different kind of entities.
CREATING ENVIRONMENT:
•	Made a folder my_project in the desired location from command prompt
•	Upgraded the pip to pip 19.0.3
•	Created virtual environment of name my_env  and activated it by using following commands
pip install virtualenv
Virtualenv my_env
my_env\Scripts\Activate.bat
•	Installed rasa_nlu , rasa_core,spacy,spacy language model using pip install commands
•	After installing required libraries freeze all the requirements in requirements.txt


TRAINING THE MODEL:
•	Used https://rasahq.github.io/rasa-nlu-trainer/ for building training dataset and downloaded it in json format
 



•	Made a configuration file config_spacy.json , for pipeline and training data set details
 



•	Built a nlu_test.py file to train the model
 


•	Trained the model by running python nlu_test.py from the terminal
•	The model is stored with the name of queries in model folder

MAKING BOT:
•	Possible cleansing of data using Microsoft Excel and macros. 
•	Generated response.py file containing responses of all queries using above prepared data.
 
•	Build a folder templates containing HTML file( index.html) for User Interface.
 

•	Build an application.py file using Flask .
 

•	By running python application.py from command prompt, the webpage can be accessed via http://localhost:5000 server.
 

 
•	The final output will be like as given in output png file
 

•	Intent output country_name is based on my model data classification.
•	Entity output cuisine is based on the fact that potato is classified as cuisine.
•	Result output Russia is based on the data stored in response.py created over the dataset available(approx. 8000 records)


 


 


