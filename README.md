Final Project Proposal - Mean Squares

http://rpubs.com/woutcault/final_607_project

Team Members: Paul Perez, William Outcault, Aaron Zalki, John Suh

Proposal:  As a team, we’re interested in seeing if the weather determines a rider’s preference in taking a street taxi, or a ride-sharing self-employed limousine service. As we've all experienced taking street taxi’s and for-hire vehicles, we understand they are different experiences and each may serve as better options in different scenarios. New York City has public records taxi rides for yellow taxis, green taxis, and for-hire vehicles. These records are available here in .csv format from starting in the year 2009. We’re looking to pair this data along with historical weather data, obtaining via API. We’ll load all our data into a database allowing the team to query subsets and samples of the data to analyze.

Data Collection: To collect the taxi records, we’ll create a python script, and use a web driver to scrape the page for URL’s, and click on relevant URL’s to download our selected data files. For our historical weather information, we’ll apply and create an API app, and then start to collect the data for the same date range in which we decide to collect the taxi records.


Data Ingestion:  Once all of our data is collected, we’ll clean as necessary, and ingest into a database for which each team member can query. We will research and see if which database best fits our solution, as SQLite may not be able to handle the amount of data we plan to collect.

Analysis (Sample Questions): Do taxi types travel faster on rainy days? Are there more taxi rides in the winter compared to other season? Which month historically has earned the most US dollars from taxi rides. Visualize the number of taxi rides by taxi type by time of day (date part analysis). Linear regression to see if there is a correlation between trip distance and tip.

Project Workflow:

-Load taxi data .csv files using python scripts into SQL database.
-Load weather data via R API into SQL database.
-Tidy data and join weather data with taxi data (loaded from SQL to R).
-Perform a few different kinds of analysis. 
