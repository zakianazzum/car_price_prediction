# Used Car Price Analysis

This repository provides an in-depth analysis of automobile prices based on a dataset of both new and used cars. The analysis investigates how different factors such as brand, model, engine size, mileage, and economic events influence the prices of vehicles. By identifying trends and patterns, this project aims to build predictive models to estimate the price of used cars. Please note that the insights and conclusions drawn in the repository are based on the dataset provided and may not reflect the real world within the broader automobile market.

# Dataset Description

The dataset used in this analysis contains information about a variety of used and new cars, focusing on factors that influence car prices. It includes details such as the car's brand, model, engine size, and other relevant features. The dataset is used to explore the relationships between these factors and how they affect car pricing.
The dataset used in this analysis was collected from []

# Analysis Highlights

## Brand and Model Insights

- Luxury Cars: BMW, Tesla, and Mercedes dominate the luxury segment, with BMW having significant price fluctuations by model.

- Most Expensive Models: The Mercedes GLC is the most expensive model, while the BMW 3 Series is slightly more affordable, highlighting the role of model-specific features in pricing.

- Popular Brands: Toyota and Audi have the highest counts, reflecting their popularity in the used car market.

## Attribute-Specific Observations

- Mileage: Cars with moderate mileage command higher prices compared to those with very low or very high mileage.

- Engine Size: No strict linear relationship with price, larger and smaller engines are often priced higher than medium-sized ones.

- Condition: Newer cars are priced higher, but older cars in good condition can retain significant value.

# Key Takeaways

- Luxury vs. Mainstream Brands: Luxury brands are more sensitive to economic fluctuations, while mainstream brands exhibit stable pricing trends.

- Fuel Type Preference: Diesel cars remain popular in the luxury segment, while electric vehicles are gaining traction, particularly after 2020.

- Economic Events: Pricing trends align with major global events, emphasizing the interconnectedness of the automobile market with broader economic factors.

# Visualizations

The analysis includes a variety of visualizations to support the findings:

- Price Distribution by Brand and Model: Bar chart showing average prices.
- Yearly Price Trends: Line graph of price trends over time.
- Mileage vs. Price Scatterplot: Scatterplot demonstrating the non-linear relationship.
- Fuel Type Price Comparison: Boxplot of prices across fuel types.
- Impact of Condition on Price: Grouped bar chart showing price differences by condition.

# Model Performance and Evaluation

## Model Implemented

To predict used car prices, two models were implemented:

1. Polynomial Regression
2. XGBoost (Extreme Gradient Boosting)

### Polynomial Regression

The Polynomial Regression model was applied to capture non-linear relationships between features and the target variable (car price). The model was evaluated using the following metrics:

- Train R2 Score: 0.230
- Test R2 Score: -0.363

While Polynomial Regression was able to capture non-linearity in the data, the model showed poor performance on the test set, indicating potential overfitting or an insufficiently complex model.

### XGBoost (Extreme Gradient Boosting)

XGBoost, an ensemble method utilizing boosting techniques, was applied to improve predictive accuracy. The model was evaluated using the following metrics:

- Train R2 Score: 0.595
- Test R2 Score: -0.131

XGBoost performed better than Polynomial Regression on the training set but still struggled to generalize to the test set, as indicated by the negative R2 score on the test set.

## Model Comparison

- Polynomial Regression: The model performed poorly on the test data with negative R2, suggesting that it might not be the best choice for this dataset.

- XGBoost: Although it performed better on the training data, the XGBoost model still showed a decrease in performance on the test data, indicating that further tuning or feature engineering may be required to improve generalization.

# Conclusion

The analysis of the used car market reveals important insights into factors influencing car prices, including brand, model, mileage, engine size, fuel type, and condition. While both Polynomial Regression and XGBoost have some predictive power, the models are currently underperforming on the test set, indicating that more work is needed.

The next steps for this project involve:

- Model Improvement: Currently working to improve the models, such as tuning, hyperparameters, using additional features, or trying different algorithms.

- Further analysis: Exploring other machine learning models and methodologies to identify the most effective model for predicting used car prices.
