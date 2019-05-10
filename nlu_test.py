from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter


training_data=load_data('testData.json')
trainer=Trainer(config.load('config_spacy.json'))
interpreter = trainer.train(training_data)
model_directory=trainer.persist('./model/nlu',fixed_model_name='queries')



#x=interpreter.parse("Where we can find Eiffel Tower?")
#print(x)