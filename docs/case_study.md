# Credit card customer churn: portfolio case study

## Business question

Which customer groups account for the most observed churn, and which account activity patterns should a retention team investigate?

This project analyzes a snapshot of **10,127 credit card customers**, of whom **1,627 were attrited**, giving an overall churn rate of **16.07%**. The aim is to support investigation and campaign planning. Retention improvements have not been measured.

## Data and workflow

Source: [Credit Card Customers on Kaggle](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers).

1. **Prepare data in Python.** Check missing values and duplicate customer IDs, retain explicit `Unknown` categories, remove the two supplied classifier outputs, and derive the binary `Churn` flag.
2. **Analyze segments with SQL.** Compare customer counts, churn volume, and churn rates across product relationships, contacts, inactivity, utilization, card categories, and tenure.
3. **Build Power BI reporting.** Import the prepared data, set column types, create six DAX measures, and build an overview with KPI cards, segment charts, a card-category table, and three slicers.
4. **Validate results.** Reconcile the dashboard totals and the Blue-card filter against the prepared CSV. The [supporting SQL](../sql/retention_segments.sql) reproduces the segment evidence below using the notebook's `customers` table.

## Findings

| Segment | Customers | Churned | Churn rate | Decision relevance |
| --- | ---: | ---: | ---: | --- |
| All customers | 10,127 | 1,627 | 16.07% | Overall reference rate. |
| Utilization below 25% | 5,822 | 1,232 | 21.16% | Accounts for 75.72% of observed churn; investigate engagement barriers. |
| Two products | 1,243 | 346 | 27.84% | Higher observed churn than the six-product group. |
| Six products | 1,866 | 196 | 10.50% | Product count is associated with churn; this does not establish a benefit from selling more products. |
| Five contacts in 12 months | 176 | 59 | 33.52% | Investigate contact reasons and whether contacts preceded closure. |
| Six contacts in 12 months | 54 | 54 | 100.00% | An unusual small group requiring data and timing checks. |
| Blue cardholders | 9,436 | 1,519 | 16.10% | Accounts for 93.36% of churn volume, with a rate close to the overall rate. |
| Platinum cardholders | 20 | 5 | 25.00% | A high rate in a very small group; insufficient reason to make this the main priority. |

The segments overlap. Their churn counts or shares must not be added together.

## Proposed business actions

These are recommendations for investigation and testing, not interventions already implemented.

| Priority | Proposed action | Evidence and rationale | How to evaluate it |
| --- | --- | --- | --- |
| 1 | Research barriers to engagement among currently active customers with low utilization. Test an optional service or onboarding check-in if the research identifies a useful intervention. | The below-25% group contains 1,232 observed churners. Low utilization does not explain why they left. | After defining eligibility and a future churn window, compare a randomized intervention group with a control group on churn and transaction activity. Track opt-outs and complaints. |
| 2 | Audit high-contact records before using contact count for outreach or modeling. Collect contact dates, direction, reason, resolution status, and account-closure dates. | All 54 six-contact customers churned. Contacts could occur during or after closure, making the pattern unsuitable as an early signal. | Measure the share of contacts occurring before closure, missing timestamps, unresolved cases, and repeat contacts. If a service intervention is later tested, evaluate future churn against a control group. |
| 3 | Prioritize campaign planning using both churn volume and reliable segment rates. Investigate behavioral subsegments within the large Blue-card population. | Blue contributes 1,519 churners; Platinum contributes five. Card category alone provides little basis for targeting Blue customers because its rate is near the overall rate. | Before a campaign, deduplicate overlapping segments and check the reachable population. After a controlled pilot, compare incremental retained customers and cost per additional retained customer. |

## What a retention pilot would require

- A new cohort of currently active customers; already-attrited customers cannot be retained retrospectively.
- A business-approved churn definition and future observation window, with features measured before intervention and outcome.
- A randomized control group, a sample-size plan, and one primary outcome agreed before launch.
- Recorded outreach costs and outcomes. Estimated savings or return on investment cannot be established from this dataset alone.

The primary comparison would be the difference in future churn rates between control and intervention groups, reported in percentage points with uncertainty. Transaction activity can be a secondary outcome; it is not a substitute for demonstrating retention.

## Deliverables and current scope

- [Python and SQL analysis](../01_data_analysis.ipynb)
- [Power BI dashboard](../powerbi/Credit_Card_Churn_Dashboard.pbix), [usage guide](../powerbi/README.md), and [DAX measures](../powerbi/measures.dax)
- [SQL evidence for retention segments](../sql/retention_segments.sql)
- [Model preparation](../02_model_training.ipynb): stratified split and categorical encoding

Model training, evaluation, and risk scoring remain planned. The source lacks a dated sequence of outcomes, so the analysis establishes associations rather than causes or validated future prediction performance.
