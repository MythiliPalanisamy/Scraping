## My first scraper

# The Mission

In this project, we will guide you step by step through the process of:

1. creating a self-contained development environment.
2. retrieving some information from an API (a website for computers)
3. leveraging it to scrape a website that does not provide an API
4. saving the output for later processing

Here we query an API for a list of countries and their past leaders. We then extract and sanitize their short bio from Wikipedia. Finally, we save the data to disk.

# Creating a clean environment
* using venv created a new environment called `wikipedia_scraper_env`.
* Activated and added my environment to .gitignore.

# API Scraping
* retrived informations of country list and leader list with the help of user cookie.
* from leaders list filtered their wikipedia url and scraped the first paragraph.(not from API but from the root link)
* sanitized output with regex.
*created session instead of cookie.
*saved the work in .json file.

# Situation
this project was done as a part of AI Bootcamp at Becode.org

# Completion
* Name                -   Mythili Palanisamy
* Repository          -   Wikipedia Scrapper
* Type of Challenge   -   Learning
* Duration            -   3 days
* Submission          -   23/06/2023  5:30PM
* Team challenge      -   solo