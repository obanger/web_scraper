# Web Scraper
**Simple web scraper:** 
Goal - create simple web scraper which can download web page and provide  
dictionary with key-value pair {tag: quantity of this tag on web page}  
Application works in console mode. It receive url as required argument and one of
required parameters: --get or --view.   
Example:   
```$ python3 tagcounter.py https://yandex.ru/ --get```    
```$ python3 tagcounter.py https://yandex.ru/ --view```  
- Call with combination of url and --get will provide downloading of page and saving into data base table with following columns:   
(website_name as second level domain,  
website_url as url,  
date as date of execution,  
dict with tags as dict pickled to blob format)  
and printing results on console  
- Call with combination of url and --view will provide only printing results received from data base on console    

**To run web_scraper:**
 - Clone repository:  
 ``` $ git clone git@github.com:obanger/web_scraper.git``` into your working directory
 - In directory which placed cloned repository ..path/to/web_scraper need execute following:  
  ```python3 -m venv web_scraper_venv```  
  check with 'ls' command if needed
 - Then activate your virtual environment:  
  ```$ source path/to/web_scraper_venv/bin/activate```  
  So now you will work under virtual env
 - Switch directory to ..path/to/web_scraper and install dependencies:  
   ```$ pip install -r requirements.txt```
 - run ```$ python3 tagcounter.py https://yandex.ru/ --get```
 