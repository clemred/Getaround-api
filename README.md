# Geataround project

Getaround is the Airbnb for cars. You can rent cars from any person for a few hours to a few days. Late returns at checkout can generate high friction for the next driver if the car was supposed to be rented again on the same day.
In order to mitigate those issues they’ve decided to implement a minimum delay between two rentals. A car won’t be displayed in the search results if the requested checkin or checkout times are too close from an already booked rental. It solves the late checkout issue but also potentially hurts Getaround/owners revenues: we need to find the right trade off.


## Dataset

Create a "data" folder in the AT&T\_project directory and download in this file.

There are two files you need to download:
    • [Delay Analysis](https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/get_around_delay_analysis.xlsx) 👈 Data Analysis 
    • [Pricing Optimization](https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/get_around_pricing_project.csv) 👈 Machine Learning 


## Streamlit dashboard

The Streamlit dashboard is deployed via a [Github repository](https://github.com/clemred/Getaround-dashboard) and can be found [here](https://blank-app-yr18alc9iv.streamlit.app/).




## Model notebook

There is a notebook with EDA and the trained neural network: **Model.ipynb**.
The methodology I have followed is pretty well indicated.
