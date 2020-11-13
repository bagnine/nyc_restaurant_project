# nyc_restaurant_project
#### Introduction:

The COVID-19 pandemic and enforced business closures to mitigate transmission has dramatically altered the landscape of American commerce.  According to Yelp's Local Economic Impact Report 163,735 businesses were listed as closed as of August 31st as a result of the pandemic.  The hospitality and restaurant industry has been particularly hard hit with the National Restaurant Association estimating that 1 in 6 restaurants nationwide has closed, nearly 3 million employees are out of work and that an estimated $240 billion in sales will be lost by the end of 2020 due to the pandemic.

Beyond the immediate impact of the pandemic, there is a growing concensus among public health experts of an increased likelihood of future events.  Factors including increased population density, increased contact with mammalian vectors and the volume of global travel have increased the rate at which new infectious diseases emerge. In the last 20 years there were 6 major threats - SARS, MERS, Ebola, avian influenza, swine flu and COVID-19. 

To address these issues, our project aimed to (1) identify the characteristics of restaurants that have closed as a result of the pandemic in New York City (NYC), (2) use attributes of surviving restaurants to recommend better business models, and (3) characterize the market opportunity when restrictions are fully lifted.  

#### Methods:

Data for this analysis was collected from a variety of sources.  A list of COVID-19 related restaurant closures in NYC was compiled from lifestyle websites including theinfatuation.com and donyc.com.  The name and zipcode of closed restaurants were compiled for cross-referencing with other websites. In total 187 closed restaurants were identified. A sample of open restaurants in the zipcodes where closures occured was collected using the YELP API business search.  We requested 35 results per zip code.  Returned restaurants were sorted by relevance and distance so results were not perfectly matched by zip code.  We excluded any results outside of the boroughs of Manhattan, Queens or Brooklyn.  Additionally, restaurants with fewer than 16 reviews were excluded to avoid including any restaurants newly opened during the pandemic in our sample.  After excluding duplicates our sample contained 1173 open restaurants.  

Information on both closed and open restaurants collected from the YELP API included the category (cuisine), price point, coordinates, and type of transactions (reservations, delivery and/or takeout). Information on COVID19 safety procedures including whether or not they had outdoor seating was scraped from yelp.com.  Population density by zipcode was collected from usa.com. The number of restaurants by zipcode was collected from NYC OpenData based on Department of Health and Mental Hygiene Restaurant Inspection Results.

Value counts were calculated for all categorical variables. Descriptive statistics and histograms were created for continuous variables to assess the distribution and evaluate measures of central tendency and dispersion. Chi-square test of association were used to assess the relationship of our categorical features of interest with closure, and the independent samples t-test was used to assess the relationship between closure and our continuous features of interest.

#### Models:

In the interest of interpretability and reprouducability, we used Logistic Regression and Decision Tree Classifier models to make our predictions. Through an iterative process, we were able to evaluate the relevance of our features via coefficients, cross-reference features between the models, and use the differences between the model to identify non-linear relationships and re-process our data. 

In one example, Decision Tree split multiple times on the distance to the nearest subway station, which was returning a near-zero coefficient in our regression model. By incorporating the distance split, we were able to identify the interaction between subway distance and restaurant frequency- when there are no close subways but low numbers of restaurants in the zipcode, success is likely, and when a restaurant is close to a subway in an area with 480+ restaurants it's likely to do  very well. By dummying our distance to subway feature into greater than and less than .5km, we were able to improve our regression model's recall and accuracy scores.

After tuning both models and performing new statistical tests, we settled on a final Logistic Regression model. 

#### Our Findings:

By far the greatest predictive element among our sample was outdoor seating, followed by the quality of Yelp ratings and the combination of delivery, takeout and reservation features. 

The most predictive attributes of the closed restaurant class were all restaurant types- pizza and breakfast restaurants, cafes and bars. 

Based on the factors in our model, the most likely restaurants to survive in the pandemic are Latin American, Chinese and South Asian restaurants with outdoor seating and high Yelp ratings that offer delivery, takeout and take reservations. 

#### Next Steps:

We'd like to take a second look at this data in a season where outdoor dining is less of a determining factor. Additionally, we'd like to acknowledge the limits of our data in terms of the class imbalance created by the smaller sample size of closed restaurants, though in this case we don't hope for more closures in order to improve our forecasting. 

Additionally, we'd like to acknowledge that while our model suggests that eating on site is a make-or-break for New York restaurants, we don't believe that to be a sufficient reason to skirt public health guidelines or advocate for reopening at full capacity before it's safe to do so. 

#### Repository Structure:

├── README.md                                            <- README for reviewers of this project
├── Project_Presentation.pdf                             <- PDF version of project presentation
├── data
│   ├── Closed restaurant zip codes.xlsx                 <- Manually gathered data on closed restaurants
│   ├── closed.csv                                       <- closed restaurant data from Yelp API
|   ├── DOITT_SUBWAY_STATION_01_13SEPT2010.csv           <- Subway station location info
|   ├── mergeddata.csv                                   <- Complete dataframe with all restaurants and features
|   ├── openrest.csv                                     <- Open restaurants pulled by zip code from Yelp API
|   ├── pop density by zip ny.xlsx                       <- Population density figures by zip code
|   ├── Restaurants__rolled_up_.csv                      <- Restaurant data from NYC Dept of Health
├── EDA_merged.ipynb                                     <- Data exploration and feature engineering notebook
├── models.ipynb                                         <- Modeling notebook
├── Univariable & bivariable analysis.ipynb              <- Statistical testing notebook
├── yelp_data_gather.ipynb                               <- Web scraping and API calling notebook
└── notebooks                                            <- Supplemental exploration notebooks