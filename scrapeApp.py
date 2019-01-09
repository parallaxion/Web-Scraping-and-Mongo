#flask
from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)



@app.route('/scrape')
def scrapebutton():
    from scrape_mars import scrape
    try:
        pageDat = scrape()
        pageDat = str(pageDat)
    except:
        pageDat = "Error Scraping Data"
        
    return pageDat

if __name__ == "__main__":
    app.run(debug=True)

#homework inst url: https://wustl.bootcampcontent.com/wustl-bootcamp/WASHSTL201809DATA3/tree/master/12-Web-Scraping-and-Document-Databases/Homework/Instructions
#Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
#Store the return value in Mongo as a Python dictionary.
#Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
#Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.
