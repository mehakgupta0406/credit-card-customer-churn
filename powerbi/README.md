# Power BI churn dashboard

[Download the Power BI report](Credit_Card_Churn_Dashboard.pbix)

The **Churn overview** page explores historical credit card customer attrition. It uses the prepared dataset of 10,127 customers and 22 columns from the Python analysis. The imported table is named `Customers`. Customer IDs are stored as text, count fields as whole numbers, and ratios and decimal-valued fields as decimal numbers.

## Open the report

1. Download `Credit_Card_Churn_Dashboard.pbix`. GitHub does not render this binary file; use its download option.
2. Open the downloaded file in a recent version of Power BI Desktop.
3. Select **Churn overview**. The imported data is included, so you can inspect the report without refreshing it first.
4. Use the card type, gender, and income category dropdowns to filter the page. Clear selections to return to all customers.
5. Hover over chart bars to inspect customer counts and churn volume alongside churn rates.

The report is a local Desktop file. No published Power BI service link is included.

## Measures

All measures are defined on `Customers` in the **Dashboard KPIs** display folder. Their DAX is also available in [measures.dax](measures.dax).

| Measure | Definition | Display format |
| --- | --- | --- |
| Total Customers | Number of customer rows in the current filter context | Whole number |
| Churned Customers | Sum of the binary churn flag, returning zero if no rows match | Whole number |
| Existing Customers | Total customers minus churned customers | Whole number |
| Churn Rate | Churned customers divided by total customers | Percentage, two decimal places |
| Average Transactions | Average transaction count per selected customer | One decimal place |
| Average Utilization | Average utilization ratio among selected customers | Percentage, one decimal place |

The first four measures appear as KPI cards. The two average measures are available in the model for additional visuals. A churn rate with no customers is left blank rather than reported as zero.

## Refresh on another computer

The PBIX retains its original local CSV source path. Update that path before refreshing:

1. Download `BankChurners.csv` from the [original Kaggle dataset](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers).
2. Run [01_data_analysis.ipynb](../01_data_analysis.ipynb) and export the prepared dataframe:

   ```python
   df.to_csv("bank_churn_prepared.csv", index=False)
   ```

3. In Power BI Desktop, choose **Home → Transform data → Data source settings**.
4. Select the CSV source, choose **Change Source**, and browse to your `bank_churn_prepared.csv`.
5. Confirm the `Customers` query contains 22 columns, including `Churn`, and excludes the two supplied `Naive_Bayes_Classifier...` columns.
6. Select **Close & Apply**, refresh, clear report filters, and check the totals below.

## Validation performed

| Selection | Customers | Churned | Existing | Churn rate |
| --- | ---: | ---: | ---: | ---: |
| All customers | 10,127 | 1,627 | 8,500 | 16.07% |
| Blue cardholders | 9,436 | 1,519 | 7,917 | 16.10% |

The headline measures and Blue-card slicer results were checked in Power BI Desktop against independent calculations from the prepared CSV. The report was saved with all slicers cleared.

## Interpretation

- Compare counts and rates together. Platinum has 25% churn but only 20 customers; Blue accounts for 1,519 churned customers.
- Contacts and inactivity describe observed associations. The data does not establish why a customer left or whether an intervention would prevent churn.
- The source is a snapshot without a dated sequence of future outcomes. This dashboard does not provide a validated future prediction window, trained-model scores, or measured retention impact.
