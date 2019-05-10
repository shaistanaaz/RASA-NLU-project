from flask import Flask,render_template,url_for,request
from rasa_nlu.model import Metadata, Interpreter
from response import *
interpreter = Interpreter.load('./model/nlu/default/queries')
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")
	
def get_random_response(input):
    print (response[input])
    return response[input]

		
@app.route('/process',methods=["POST"])
def process():
	try:
		if request.method == 'POST':
		   rawtext = request.form['rawtext']
		   doc = interpreter.parse(rawtext)
		   INTENT=doc['intent']['name']
		  
		   if len(doc['entities'])==0:
							ENTITY="Unable to find entity"
		   else:
							ENTITY=doc['entities'][0]['entity']
			  
		   print("***************chat")
		   print(doc)
		#return render_template("index.html",results=INTENT)
		
		
		response_text = get_random_response(rawtext)
		print(response_text)
		return render_template("index.html",intent=INTENT,entity=ENTITY,results=response_text,query=rawtext)
	except Exception as e:
		print(e)
		return render_template("index.html",intent=INTENT,entity=ENTITY,results="Apologies,I am still learning on this topic.",query=rawtext)


app.config["DEBUG"] = True		
if __name__ == '__main__':
	app.run(debug=True)


