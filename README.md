# Pic16BProject

Our goals for the housing project has changed in that we focused on creating the website where the user can input there preference on California housing, and get a dataframe of area suggestions that fit those criteria. We have a main page in which we wish to post some interesting graphs and findings that we have observed from the California database we have created. We have a time series file that can generate housing predictions using Facebook Prophet, and we are trying to implement that to our website. Other than the main page, the ask page on our website contains the questions that the user can input and we will retrieve the recommendations from our database. To run the website, you have to run flask since the website is local, and we have created a path that will not cause problems retrieving the information from the database. Note that the minimum budget must be a smaller number than the maximum budget. Also, if the questionnaire is submitted without filling out all the information, nothing will be returned.



**Abstract:**
Every person will be interested in housing prices at least once in their life. There are many reasons for owning a house: having a place to live, using it as a rental property for income, or other potential reasons. My teammates and I want to see throughout the years, which geographic areas in California (or on a smaller scale) are the most dynamic in pricing and what the reasons are behind it. What are the social, economic, political sensitivities behind this? I believe we can understand and visualize the data from many angles. One very interesting angle will be how covid has influenced the housing market in California. This project can potentially both help predict housing price in new or existing neighborhoods and identify structural inequalities.

**Planned Deliverables:**
What is “Full success” and what is “Partial success”?

“Full success” is considered as our group achieving two goals. 
1. The first one is to understand California housing. In order to achieve the first goal, we might first build a predictive model that can fairly accurately predict housing price in California. While the most influential predictors (feature selection) are the key to a high prediction rate, the most predictive features are important to identify structural inequalities that cause living conditions to be extremely polarized in California. For example, we see affluent places like Beverly Hills, and not too far away there is Skid Row, a place that has the largest stable populations of homeless people in the United States. However, the goal of the project is not to build a super accurate prediction model, but to understand the housing market and to identify structural inequalities. So unsupervised learning algorithms like clustering, anomaly detection, or even neural networks will be considered. The way to present our understanding of California housing should be through creative, yet informative plots. 
2. The second goal is to invent a simple algorithm that can recommend Californians a neighborhood to live in provided with their preferences. 
 “Partial success” for our project is considered as building a predictive model to predict housing prices in California and creating some plots to merely demonstrate some characteristics of the California housing market. A “Partial success” is either achieving one goal from above or achieving both but in a less interesting manner.

**Resources Required:**
What particular risks might be applicable for your project?

1. There are housing data from the **Zillow** website.
2. More data such as from the California public schools could be merged with the data on Zillow. 
3. There are also open source data of housing from the Kaggle website.


**Tools/Skills Required:**
We need both supervised and unsupervised machine learning methods, database management, complex visualization. Feature selection might be the most important. With very predicative features, a linear regression might even be very predicative.


**Risks:**
1. It turns out that the data doesn’t exist and we need to change plans or change the direction we want to address structural inequalities. The particular risk that is applicable to the project is that at the end, we are not able to identify structural inequalities, but merely create cool plots.
2. I am also not too sure how much data we need to deal with and is available to us. The data from public schools and other data on social aspects may not be comprehensive enough for us to extract useful information for us. Also lost of data on social aspects may not be provided for public use. 
3. If we have a huge dataset, machine learning methods like boosting are very time consuming. The huge data amount and the training and revision of models may consume a lot of time to operate on computers, so the revision process might consume a large amount of time.


**Ethics:**
1. If we are predicting housing prices, it will be very important not to have race as a latent variable factored into our machine learning algorithm, as neighborhoods in the United States are very segregated. Rather we should focus on areas with development, job opportunities, and school quality. Then again, these variables could potentially lead to predicting that housing prices in certain neighborhoods to be lower.

2. We will primarily analyze data on language English, and we will try to include data of  other languages if possible to have a better/more comprehensive prediction and analysis on different communities.




**Tentative Timeline:**
1. By Week 2, we want to have found our datasets and be able to merge them into a database. 
2. By Week 4, we would have created machine learning models to predict housing prices and what features lead to the worth of a house.
3. By Week 6, we would have trained our machine learning model and created graphs and plots to tell the story of why housing prices are the way they are, and where the housing prices could go in the future.
