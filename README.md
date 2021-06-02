# Pic16BProject

**To run our local website, follow these instructions**:  

In the terminal,  
  
1. Make 'Web_page' the current directory in cmd:
`cd Pic16BProject/Web_page`

2. If you haven't installed `fbprophet` into your `PIC16B/Or any other environment in your anaconda`, enter this command:  
`conda install -n PIC16B -c conda-forge fbprophet`, the general command for any anaconda environment is as follows:  `conda install -n [NameOfVEnv] -c conda-forge fbprophet`.

3. Activate the customized PIC16B environment:
`conda activate PIC16B`
*（Remark: in some cases on Windows, try to directly use `activate PIC16B/Or any other environment in your anaconda` instead of using `conda activate PIC16B`. You can list all discoverable environments with `conda info --envs` in cmd.）*

4. Enable the Flask debug mode by setting the environment to development *(Remark: on Windows, you might use `set FLASK_ENV = development` in cmd)*:
`export FLASK_ENV=development`

5. Start the development server:
`flask run`

6. In your web browser, go to http://localhost:5000/ or the recommended server stated in terminal.



`.DS_Store` files are unique to each computer system, therefore they have been deleted to avoid merge conflicts and to ensure this project folder is usable for everyone. `ipynb_checkpoint` directories have also been deleted for better version control.

**Project Structure:**

*Note* Our project contains two parts. The first part is an analysis on US housing market given in the form of a report. Originally, we wanted to do the analysis on California housing, but we could not find enough data on California housing. However, our webpage is only for California Housing.

**Analysis part:** The analysis focuses on the following two points,

1. The differences between the demand in high-end homes and low-end ones prompt us to consider the social inequality in purchasing houses, especially among different racial groups. The code, datasets, and plots can be found in social_inequality_Related folder.

2. We also looked at the discussion of the overall US housing market. We tried to find what are the topics that people may discuss, and what are people’s common sentiments. The code, datasets, and plots can be found in Reddit Sentiment & Topic Modeling on House folder.

The summary of result can be found on the main page of our website (a copy of that part is in Housing Project Summary Report.pdf)

**Besides all the analysis, we have our Main Product: California Housing Website**

The data we used from the following resources,
> https://www.zillow.com/research/data/

> https://www.schooldigger.com/go/CA/schoolrank.aspx?level=3#

> https://en.wikipedia.org/wiki/California_locations_by_race

> https://www.ftb.ca.gov/pay/penalties-and-interest/interest-and-estimate-penalty-rates.html 

> https://en.wikipedia.org/wiki/List_of_California_locations_by_income

> https://en.wikipedia.org/wiki/California_locations_by_crime_rate


1. We incorporated data in crime rates, city population, public high schools, housing locations, people’s budgets, longitude and latitude, and future housing price predictions to shuffle our the ideal locations for people who wish to invest in houses. We created a web page where the user can input their preference to get area suggestions that fit those criteria in the form of a data frame.

2. For our website, we have a main page in which we wish to post some interesting graphs and findings that we have observed from the California database we have created. We have a time series file that can generate housing predictions using Facebook Prophet, and we are trying to implement that to our website. Other than the main page, the ask page on our website contains the questions that the user can input and we will retrieve the recommendations from our database. To run the website, you have to run flask since the website is local, and we have created a path that will not cause problems retrieving the information from the database. Note that the minimum budget must be a smaller number than the maximum budget. Also, if the questionnaire is submitted without filling out all the information, nothing will be returned.

*Remark on the progress of project:*
we have not combined the prediction plots into the results of our function. Ideally by the end of the project, the function will return a prediction plot that contains the houses past prices and future prices for each row of the generated data frame.




**Project Proposal:**


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

2. We will primarily analyze data on language English, and we will try to include data of other languages if possible to have a better/more comprehensive prediction and analysis on different communities.




**Tentative Timeline:**
1. By Week 2, we want to have found our datasets and be able to merge them into a database.
2. By Week 4, we would have created machine learning models to predict housing prices and what features lead to the worth of a house.
3. By Week 6, we would have trained our machine learning model and created graphs and plots to tell the story of why housing prices are the way they are, and where the housing prices could go in the future.
