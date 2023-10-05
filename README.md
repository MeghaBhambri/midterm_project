# Weekly Sales Analysis of a Retail Store

## Short Introduction

The "ABC Sales Forecasting" dataset available on Kaggle is a comprehensive dataset that provides historical sales data for various retail stores and departments. This dataset is suitable for retail sales analysis and demand forecasting projects. The dataset contains several key features and columns that will be used for analysis and forecasting:

- **Store**: An identifier for the store.
- **Dept**: An identifier for the department within the store.
- **Date**: The date of the sale.
- **Weekly_Sales**: The weekly sales for the given store and department.
- **IsHoliday**: A boolean flag indicating whether the week includes a holiday.
- **Temperature**: The average temperature in the region.
- **Fuel_Price**: The cost of fuel in the region.
- **CPI (Consumer Price Index)**: The Consumer Price Index for the region.
- **Unemployment**: The unemployment rate in the region.
- **Markdown**: The discounts/promotions offered.

## Questions for Analysis

### Question 1

- How do different types of stores (e.g., Type A, Type B, Type C) perform in terms of average weekly sales and growth over time?

### Question 2

- Are there significant seasonal patterns in average weekly sales? Analyze.

### Question 3

- How do external factors such as temperature, fuel prices, CPI, and unemployment rates affect weekly sales?

### Question 4

- How do holidays impact weekly sales? Compare the sales during holiday weeks to non-holiday weeks.

### Question 5

- Do promotional promotions lead to increased weekly sales?

## Source of Data

The dataset was obtained from Kaggle.

## Findings

### Question 1/Answer

1. The order of average weekly sales is A > B > C.
2. Peak sales occur in the months of December and November. Stores A and B follow the same pattern, but store C shows no change in weekly sales.

### Question 2/Answer

Significant seasonal patterns in average weekly sales include a peak in December, stability in sales across three years, a rising trend from October onwards, dips in January, and a notable decline in September. Understanding these patterns can help businesses better plan their inventory, marketing strategies, and promotions to maximize sales throughout the year.

### Question 3/Answer

There is no linear relationship between weekly sales and external factors such as temperature, fuel prices, CPI, and unemployment rates.

### Question 4/Answer

The t-test results indicate that the observed difference in mean sales between holiday and non-holiday weeks is highly unlikely to have occurred by random chance alone. Therefore, it provides evidence that holidays do have a significant impact on weekly sales, at least in terms of their mean values.

### Question 5/Answer

Overall, the correlations between individual promotion types and weekly sales are relatively weak, indicating that there is not a strong linear relationship between the presence of these promotions and the weekly sales figures. However, correlations only measure linear relationships, and there may be more complex or non-linear interactions to explore.

When interpreting correlations, it's important to keep in mind that correlation does not imply causation. A lack of strong correlation does not necessarily mean that markdowns do not impact sales; it might mean that their impact is not purely linear or that other factors play a significant role.

Holidays combined with promotions tend to show higher average weekly sales. This is evident in the analysis where comparison in mean sales during holiday weeks with and without promotions.

## Conclusion

Store A consistently outperforms B and C, with peak sales in December. Weekly sales follow seasonal patterns, rising from October and dipping in January. Holidays significantly boost sales, especially when combined with promotions, while external factors show weak correlations.

## Next Steps

In the future, further analysis and modeling could be performed to develop more accurate sales forecasts and explore the impact of other potential factors on weekly sales. Additionally, strategies for optimizing promotions and holiday promotions can be devised to enhance overall sales performance.
