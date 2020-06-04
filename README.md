## Web Scraping Homework - Mission to Mars

## Table of contents
* [Homework_Assignment_Background](##Homework_Assignment_Background)
* [Project_Task](##Project_Task)
* [Technologies](##Technologies)
* [Setup](##setup)
* [Methodology](##Methodology)


## Homework_Assignment_Background 

In this assignment, we built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following points in the project task section outlines what we did to accomplish the assignment.


## Project_Task 

1. Complete the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.  The following outlines what we needed to scrape and assign it to varibales.
    * Created a title variable to hold the latest News Title and Paragraph Text from NASA Mars News (https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest)
    * Created a feature_image variable to save a complete url string for Mars Space Featured Image (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
    * Created a weather variable to hold the latest Mars weather tweet from the Mars Weather twitter account (https://twitter.com/marswxreport?lang=en)
    * Created a facts variable to hold facts about the planet including Diameter, Mass, etc and used Pandas to convert the data to a HTML table string.(https://space-facts.com/mars/)
    * Created hemisphere variables to hold high resolution images for each of Mar's hemispheres. Used a Python dictionary to store the data using the keys img_url and title.
    Appended the dictionary with the image url string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.(https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

2. MongoDB and Flask Application
    * Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
    * Converted Jupyter notebook code into a Python script called scrape_mars.py with a function called "scrape". This function executes all of scraping code from above and returns one Python dictionary containing all of the scraped data.
    * Created a route called "/scrape" that imported scrape_mars.py script and called scrape function.
    * The updated data stores the return value in Mongo as a Python dictionary.
    * Created a root route / that will query the Mongo database and pass the mars data into an HTML template to display the data.
    * Created a template HTML file called index.html that takes the mars data dictionary and display all of the data in the appropriate HTML elements. 


## Technologies
The project is created with:

* jupyter==1.0.0
* pandas==0.25.1
* splinter==0.13.0
* beautifulsoup4==4.8.0
* flask==1.1.1
* flask-PyMongo==2.3.0
* pymongo==3.10.1
* bootstrap===4.3.1
* CSS
* ChromeDriver


## Setup
1. To install jupyter botebook (https://jupyter.org/install) 
2. To install splinter (https://pypi.org/project/splinter/)
3. To install beautifulsoup (https://pypi.org/project/beautifulsoup4/)
4. To install flask (https://pypi.org/project/Flask/)
5. To install mongodb (https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/)
6. To install pandas (https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
7. To link directly to the latest Bootstrap release (https://getbootstrap.com/docs/4.1/getting-started/introduction/) 
8. To install chromedriver (https://chromedriver.chromium.org/downloads)


## Methodology

1. Wrote code to scrape the above facts required by homework assignment (To review code: mission_to_mars.ipynb).  Reviewed the code in pandas to ensure it was working.

2. Created scrape_mars.py file and transfered all scrape code here.
3. Created flask app with 2 routes (To review code: app.py)
    * Created a home route
    ```python
    @app.route("/")
        def home():
        x = mongo.db.mars.find_one()
        return render_template("index.html", mars = x)
    ```
    * Created a scrape route
    ```python
    @app.route("/scrape")
    def scrape():
        mars_data = scrape_all()
        mongo.db.mars.replace_one({}, mars_data, upsert=True)
        return redirect(url_for('home'))
    ```

4. To visualize html page, you must run the app.py file from the terminal.

    * Open terminal and type:
        ```python
        python app.py
        ```
    * In address bar, type:
        ```
        http://localhost:5000/
        ```                                   

    * Below are snapshots of the landing page for the assignment.

    <img src="screenShotImages/final_hw1_image.png" width="500" height="300">


    <img src="screenShotImages/final_hw2_image.png" width="500" height="300">

