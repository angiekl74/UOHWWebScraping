from splinter import Browser
from bs4 import BeautifulSoup 
import requests
import time
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

# PART 1 - Visit NASA news website to get headline/paragraph 
def scrape_info_1(browser):
            
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Find NASA news title
    news_title = soup.find_all('div', class_='content_title')[1].text
    # Find NASA paragraph
    news_p = soup.find_all('div', class_="article_teaser_body")[0].text
    
    mars_data = {
            "title": news_title,
            "paragraph": news_p}

    return mars_data

# PART 2 - Get main image                                             
def scrape_info_2(browser):
  
    #Visit Nasa's JPL Mars Space url using splinter module
    jpl_feature_image_url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_feature_image_url)
    time.sleep(2)
    #create HTML object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #get base Nasa link
    main_url ='https://www.jpl.nasa.gov'
    #get image url from the soup object.
    featured_image = soup.find('article')['style'][23:-3]

    #Create one full image url link
    featured_image_url = main_url+featured_image

    return featured_image_url

# PART 3 - Get Twitter weather         
def scrape_info_3(browser):
 
    twitter_url='https://twitter.com/marswxreport?lang=en'
    html = requests.get(twitter_url).text
    time.sleep(2)
    soup = BeautifulSoup(html,'html.parser')
    results = soup.find_all('div', class_="content")

    weather_all = []
    for result in results:
        tweet = result.find("div", class_="js-tweet-text-container").text
        weather_all.append(tweet)

    search_results = [i for i in weather_all if 'InSight' and 'sol' in i] 
    mars_weather=(search_results)[0][1:-27]
    
    return mars_weather

# PART 4 - Mars Facts
def scrape_info_4():

    mars_facts_url = "https://space-facts.com/mars/"
    tables = pd.read_html(mars_facts_url)
    mars_facts_df = tables[1]
    mars_facts_df.set_index('Mars - Earth Comparison', inplace=True)
    mars_facts_df.head()

    html_table = mars_facts_df.to_html()

    return html_table

# PART 5 - Mar Hemispheres
def scrape_info_5(browser):

    list = ["https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced",
            "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced",
            "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced",
            "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"]

    title = []
    image = []

    for l in list:
        html = requests.get(l).text
        soup = BeautifulSoup(html, "html.parser")
    
        image_title = soup.title.text.split('|')[0]
        title.append(image_title)
    
        hemisphere_image_urls = soup.find('div', class_='downloads').find('li').find('a')['href']
        image.append(hemisphere_image_urls)
    

    all_hemisphere_image_urls =[
        {"title": title[0], "img_url": image[0]},
        {"title": title[1], "img_url": image[1]},
        {"title": title[2], "img_url": image[2]},
        {"title": title[3], "img_url": image[3]}
        ]
        
    return all_hemisphere_image_urls

# Need to credit Justin Moore (bootcamp tutor) for helping create scrape_all function
def scrape_all():
    browser = init_browser()
    mars_news = scrape_info_1(browser)
    data = {
        "news_title": mars_news["title"] ,
        "new_paragraph": mars_news["paragraph"],
        "featured_image": scrape_info_2(browser),
        "mars_weather": scrape_info_3 (browser),
        "mars_facts": scrape_info_4(),
        "mars_hemis": scrape_info_5(browser)
    }

    browser.quit()
    return data