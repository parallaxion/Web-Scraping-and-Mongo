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
    
    #print(mydb.list_collection_names())
    siteDat = mycol.find()

    dataForTemplate = mycol.find()
    
    print(dataForTemplate[0]['Mars Facts'])
    theFactTable = json.loads(dataForTemplate[0]['Mars Facts'])
    print(type(theFactTable))

    print(client)
    #str(client.server_info())
    return render_template("marstemplate.html", **locals())

    

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
        
    return str(pageDat)

if __name__ == "__main__":
    app.run(debug=True)

#homework inst url: https://wustl.bootcampcontent.com/wustl-bootcamp/WASHSTL201809DATA3/tree/master/12-Web-Scraping-and-Document-Databases/Homework/Instructions

#Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
#Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.
