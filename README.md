# Credit Card Customer Churn Analysis and Prediction

Analyze credit card customer attrition with Python and SQL, then extend the analysis into a predictive model and a Power BI report.

**Status:** Exploratory analysis and SQL segmentation completed in the notebook. Predictive modeling and Power BI reporting are planned.

[Open analysis notebook](01_data_analysis.ipynb) · [Run in Google Colab](https://colab.research.google.com/github/mehakgupta0406/credit-card-customer-churn/blob/main/01_data_analysis.ipynb)

## Business objective

Identify customer characteristics and account activity patterns associated with churn. The planned model will estimate churn risk to help a retention team prioritize customers for investigation and outreach.

The analysis addresses:
- How common is churn?
- How do transaction activity and inactivity differ between existing and attrited customers?
- How does churn vary by card category, product count, contact frequency, and credit utilization?

## Dataset

Source: [Credit Card Customers by Sakshi Goyal on Kaggle](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers), provided as `BankChurners.csv`.

The source file contains **10,127 customers and 23 columns**, covering demographics, account tenure, product relationships, transaction activity, credit limits, and utilization.

| Customer status | Customers | Share |
| --- | ---: | ---: |
| Existing Customer | 8,500 | 83.93% |
| Attrited Customer | 1,627 | 16.07% |

The derived target, `Churn`, is **1 for attrited customers** and **0 for existing customers**.

## Tools

| Tool | Role |
| --- | --- |
| Python and pandas | Data inspection, preparation, and analysis |
| Matplotlib | Comparison charts |
| SQLite and SQL | Customer segmentation and churn-rate calculations |
| scikit-learn — planned | Model training and evaluation |
| Power BI — planned | Interactive reporting |

## Analysis completed

- Checked dataset dimensions, column types, blank values, and duplicate customer IDs.
- Found no blank values or duplicate customer IDs. Retained explicit `Unknown` categories in education, marital status, and income.
- Removed the two supplied `Naive_Bayes_Classifier...` columns to avoid target leakage in later modeling.
- Created the binary churn target.
- Plotted average transaction count, transaction amount, and inactive months by customer status.
- Loaded the prepared data into a SQLite `customers` table.
- Used SQL to calculate customer counts, churn counts, and churn rates across five segmentation dimensions.

## Key findings

| Area | Observed result | Interpretation |
| --- | --- | --- |
| Product relationships | Churn is 27.84% for customers with two products versus 10.50% for those with six. | Fewer product relationships are generally associated with higher churn. |
| Contact frequency | Churn rises from 1.75% at zero contacts to 33.52% at five contacts. All 54 customers with six contacts churned. | The six-contact pattern needs investigation; contact reasons and timing are unavailable. |
| Credit utilization | Churn is 21.16% below 25% utilization, 6.11% at 50% to below 75%, and 15.69% at 75% and above. | The relationship is not consistently increasing or decreasing. |
| Card category | Platinum has 25% churn among only 20 customers. Blue accounts for 1,519 churned customers. | Compare group size and churn volume alongside rates. |
| Inactivity | Churn increases from 4.48% at one inactive month to 29.89% at four, then declines. | Inactivity alone does not explain churn. The zero-month group has only 29 customers. |

These findings describe associations. They do not establish the causes of churn or prove that a retention action will work.

## Run the notebook

1. Download and unzip `BankChurners.csv` from the dataset source.
2. Open `01_data_analysis.ipynb` in Jupyter or Google Colab.
3. Place the CSV in the notebook's working directory. In Colab, upload it to the session's Files panel.
4. Run the cells from top to bottom.

For a local environment:

```bash
pip install pandas matplotlib jupyter jinja2
jupyter notebook
```

SQLite support is included with Python. The notebook creates `customer_churn.db`; rerunning the table-loading cell replaces the `customers` table. The CSV must be downloaded separately.

## Next steps

- Build preprocessing and modeling pipelines, excluding `CLIENTNUM` and `Attrition_Flag` from model inputs.
- Compare a logistic regression baseline with a tree-based classifier.
- Evaluate on a held-out test set using precision, recall, and precision–recall metrics, alongside accuracy.
- Generate customer risk scores and prepare report tables.
- Build a Power BI report covering historical churn, customer segments, and model results.

## Limitations

The dataset is a customer snapshot without a dated sequence of outcomes. It supports retrospective churn classification, but cannot verify whether currently existing customers later leave or establish a specific future prediction window.

The classes are imbalanced: predicting every customer as existing would achieve 83.93% accuracy while detecting no churners. Model evaluation must account for this. Retention impact would require a separate experiment.
