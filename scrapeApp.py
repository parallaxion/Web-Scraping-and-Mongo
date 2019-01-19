#flask
from flask import Flask, jsonify, render_template
import json

import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = client["database"]
mycol = mydb["marsfacts"]

app = Flask(__name__)

@app.route('/')
def core():
    #{{dataForTemplate[0]}}
    #
    # {{dataForTemplate[0]['News Title']}}
    #print(mydb.list_collection_names())
    siteDat = mycol.find()
    print('1')
    dataForTemplate = mycol.find()
    exists = dataForTemplate.count()
    print('2')
    #print(dataForTemplate[0]['Mars Facts'])
    print('1')
    #theFactTable = json.loads(dataForTemplate[0]['Mars Facts'])
    print('1')
    #print(type(theFactTable))
    print('1')
    #facts = dataForTemplate[0]['Mars Facts']
    print('1')
    #facts = facts.decode('utf-8')
    #print(facts)
    #str(client.server_info())
    if exists != 0:
        return render_template("marstemplate.html", dataForTemplate=dataForTemplate) #, facts=facts
    else:
        return render_template("marstemplate.html", dataForTemplate = [[]])

    

@app.route('/scrape')
def scrapebutton():
    print(mydb.list_collection_names())
    from scrape_mars import scrape
    try:
        pageDat = scrape()
        #pageDat = str(pageDat)
    except:
        pageDat = "Error Scraping Data"

   
    mycol.insert(pageDat)
        
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)

#homework inst url: https://wustl.bootcampcontent.com/wustl-bootcamp/WASHSTL201809DATA3/tree/master/12-Web-Scraping-and-Document-Databases/Homework/Instructions

#Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
#Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.
