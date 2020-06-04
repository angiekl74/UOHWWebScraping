from flask import Flask, render_template, redirect, url_for, jsonify
from bs4 import BeautifulSoup as bs
from flask_pymongo import PyMongo
from scrape_mars import scrape_all

# Need to credit Justin Moore (UO Bootcamp tutor) for help tying up loose ends in route/scrape routes

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    x = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", mars = x)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape_all function in scrape_mars.py file
    mars_data = scrape_all()
    mongo.db.mars.replace_one({}, mars_data, upsert=True)
    
    # Redirect back to home page
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
