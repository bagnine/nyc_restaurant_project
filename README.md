# nyc_restaurant_project
Introduction:

The COVID-19 pandemic and enforced business closures to mitigate transmission has dramatically altered the landscape of American commerce.  According to Yelp's Local Economic Impact Report 163,735 businesses were listed as closed as of August 31st as a result of the pandemic.  The hospitality and restaurant industry has been particularly hard hit with the National Restaurant Association estimating that 1 in 6 restaurants nationwide has closed, nearly 3 million employees are out of work and that an estimated $240 billion in sales will be lost by the end of 2020 due to the pandemic.

Furthermore, scientists warn that the likelihood of a new pandemic is not zero *insert stat/better phrasing here https://www.bbc.com/news/science-environment-52775386*

To address this gap in the literature we compared the characteristics of closed and open restaurants in New York City.  As a secondary aim, we wanted to characterize the market opportunity when restrictions are fully lifted.  

Methods:

Data for this analysis came from a variety of sources.  

A list of COVID19 related restaurant closures in NYC was compiled from lifestyle websites including theinfatuation.com and donyc.com.  The name and zipcode of closed restaurants were compiled for cross-referencing with other websites.

A sample of open restaurants in the zipcodes where closures occured was collected using the YELP API business search.  

Information on both closed and open restaurants collected from the YELP API included the category (cuisine), price point, coordinates, type of transactions (reservations, delivery and/or takeout), and whether or not they had outdoor seating.  *HOURS OF OPERATION*

Information on COVID19 safety procedures was scrapped from the yelp.com using beautifulsoup *this needs editing*

Population density by zipcode was collected from usa.com. The density of restaurants by zipcode was collected from NYC OpenData based on Department of Health and Mental Hygiene Restaurant Inspection Results.