from bs4 import BeautifulSoup
import re
import requests
import json

leaders_per_country = dict()
def get_first_paragraph(wikipedia_url, session):

    ''' Function that finds the first paragraph and sanitize its data from given wikipedia url'''

    a=session.get(wikipedia_url)
    soup=BeautifulSoup(a.content, 'html.parser')

    for paragraph in soup.find_all('p'):
        
        first_paragraph=""
        if paragraph.findParent('div',class_="bandeau-cell"):
            continue
        if paragraph.findParent('div',class_="no-wikidata"):
            continue
        p = paragraph.text.strip()
        if p != "":
            first_paragraph = p
            test=re.sub(pattern=r'\[.*?\]+ ', repl='', string=first_paragraph)
            clean_paragraph=re.sub(pattern=r'\(\/.*?\/.*?\)+', repl='', string=test)
            break
    return clean_paragraph

def get_leaders():

    #defining the urls
    countries_url = 'https://country-leaders.onrender.com/countries'
    cookie_url = 'https://country-leaders.onrender.com/cookie'
    leaders_url = 'https://country-leaders.onrender.com/leaders'

    #connecting url and generating cookies
    session=requests.Session()
    req_cookie=session.get(cookie_url) #cookie 
    cookie=req_cookie.cookies.get_dict()    

    #connecting countries url through same session (same_cookie)
    req_countries = session.get( countries_url, cookies=cookie ) 
    countries = req_countries.json()
    
    #looping over countries and saving leaders in dict
    for country in countries:
        req_leaders = session.get(leaders_url,cookies=cookie, params={'country' : country})

        #regenerating cookie once it fails after 30seconds
        if req_leaders.status_code==403:
            req_cookie=session.get(cookie_url)
            cookie=req_cookie.cookies.get_dict()
            
            req_leaders = session.get(leaders_url,cookies=cookie, params={'country' : country})
        leaders = req_leaders.json()
        
        leaders_list = []
        for leader in leaders:
            if 'wikipedia_url' in leader:
                wikipedia_url = leader['wikipedia_url']
                clean_paragraph1 = get_first_paragraph(wikipedia_url,session)
                leader_dict = {'id':leader['id'],'first_name': leader['first_name'], 'last_name': leader['last_name'], 'wikipedia_url': wikipedia_url, 'first_paragraph': clean_paragraph1}
                leaders_list.append(leader_dict)
        leaders_per_country[country] = leaders_list
    return leaders_per_country

get_leaders()

def save(leaders_per_country):

    #saving the filtered data
    with open("leaders.json", "w") as f:
        json.dump(leaders_per_country, f,  indent=4)

save(leaders_per_country)
