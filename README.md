# Air Quality Predictor

### Predicting Unsafe Air Quality (AQI > 100) Using Environmental, Weather, and Demographic Data

**Authors:**  
Bhavna Sreekumar  
Sarkis Shil-Gevorkyan  
Christopher Strouse  

---

## Project Objective

The goal of this project is to predict whether a given day will experience unsafe air quality conditions (AQI > 100) using environmental, meteorological, temporal, and demographic variables.

This problem is important because poor air quality has major public health impacts, particularly in densely populated and environmentally vulnerable regions. Predictive modeling can support early warning systems, environmental monitoring, and public health preparedness.

---

## Predictive Questions

### Primary Question
Can machine learning models accurately predict unsafe AQI conditions using environmental and demographic data?

### Secondary Questions
- Which environmental and weather-related variables most strongly influence unsafe AQI conditions?
- How do different machine learning algorithms perform under severe class imbalance conditions?
- Can explainable AI methods improve understanding of AQI prediction behavior?

---

## Dataset

The project integrates multiple public datasets to build a county-level air quality prediction framework for California.

### Data Sources

- **EPA Air Quality Data (2021–2025)**  
  Daily AQI, PM2.5, and ozone observations from the U.S. Environmental Protection Agency (EPA)

- **NOAA Weather Data**  
  Historical weather observations including temperature, precipitation, wind speed, and related atmospheric variables

- **U.S. Census Population Data**  
  County-level demographic and population estimates

### Engineered Features

Additional features created during preprocessing include:

- Season
- Weekend indicator
- Temperature range
- Rain indicators

---

## Data Access

Due to file size limitations, datasets are stored in Google Drive:

https://drive.google.com/drive/folders/1ynkHP16cOvcZ6zCXRGuHYju9hGEbfB7I?usp=sharing

---

## How to Run This Project

1. Open the dataset link above  
2. Click **“Add shortcut to Drive”**  
3. Ensure the folder is saved directly in **My Drive**  
4. Open the notebook in **Google Colab**  
5. Run the following to mount Google Drive:

```python
from google.colab import drive
drive.mount('/content/drive')
```

---

## Streamlit Deployment

Interactive deployment of the AQI prediction project:

Streamlit App URL:  
[https://air-quality-predictor2-u8wqtkam3tbrbxabvb9weq.streamlit.app/]

The Streamlit application allows users to explore model predictions, feature importance visualizations, and AQI forecasting outputs through an interactive interface.

---

## Models Used

Three machine learning classification models were implemented and compared:

- **Logistic Regression**  
  Baseline interpretable classification model

- **Random Forest**  
  Tree-based ensemble model capable of capturing nonlinear feature interactions

- **XGBoost**  
  Gradient boosting model optimized for predictive performance and handling complex relationships

---

## Model Evaluation

Because unsafe AQI observations represented a small minority of the dataset, the project emphasized evaluation metrics appropriate for class imbalance.

### Evaluation Metrics

- **AUC (Area Under ROC Curve)** — overall classification performance
- **Recall (Class 1)** — ability to correctly identify unsafe AQI conditions
- **Precision (Class 1)** — reduction of false alarms
- **F1-Score** — balance between precision and recall

Cross-validation and hyperparameter tuning were also applied to improve model robustness and generalization performance.

---

## Key Findings

- Ozone concentration consistently emerged as one of the strongest independent predictors of unsafe AQI conditions
- Weather-related variables such as temperature range, precipitation, wind speed, and seasonal patterns contributed meaningful predictive signal
- Seasonal effects captured broader environmental conditions associated with wildfire activity and summer heat
- XGBoost achieved the strongest overall AUC and accuracy performance
- Logistic Regression achieved the strongest recall for unsafe AQI observations under class imbalance conditions
- Feature importance analysis and SHAP interpretation improved model explainability and highlighted the importance of environmental context in AQI forecasting
- PM2.5 initially produced unrealistically high performance because it directly contributes to AQI calculation, so it was removed from the final predictor set to improve methodological validity

---

## Final Model Evaluation

Multiple models were evaluated, including Logistic Regression, Random Forest, and XGBoost.

While XGBoost achieved the strongest overall AUC and accuracy, Random Forest and Logistic Regression provided valuable interpretability and comparative insights under severe class imbalance conditions. The project emphasized comparative model evaluation rather than relying on a single performance metric.

---

## Explainability & Feature Importance

The project incorporated explainable AI techniques including:

- Feature importance analysis
- SHAP (SHapley Additive exPlanations)

These methods improved transparency by identifying which environmental and meteorological variables most strongly influenced model predictions.

---

## Limitations

- Severe class imbalance (~2% unsafe AQI observations)
- Limited availability of external environmental variables such as wildfire intensity, traffic density, and industrial emissions
- Weather data was geographically limited relative to statewide AQI coverage
- Environmental conditions can vary significantly across California regions and seasons

---

## Future Improvements

Potential future enhancements include:

- Incorporating wildfire activity and smoke intensity data
- Adding traffic and industrial emissions datasets
- Expanding spatial weather coverage across California counties
- Applying time-series forecasting methods
- Improving spatial and temporal feature engineering
- Exploring advanced imbalance handling techniques

---

## Repository Structure

- `Air_Quality_Project.ipynb` — Fully executed notebook
- `README.md` — Project overview and instructions
- `requirements.txt` — Python dependencies
- `models/` — Saved trained models
- `figures/` — Visualizations and plots

---

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Conclusion

This project demonstrated how machine learning techniques can be applied to predict unsafe air quality conditions using environmental, meteorological, temporal, and demographic variables.

The analysis showed that ozone concentration, weather-related variables, and seasonal patterns all contributed meaningful predictive signal for AQI classification. Integrating multiple external datasets improved the overall analytical framework and provided a more comprehensive representation of environmental conditions across California counties.

The project also highlighted the challenges associated with predicting rare environmental risk events under severe class imbalance conditions. Feature importance analysis and SHAP interpretation improved transparency by identifying which variables most strongly influenced model predictions.

Overall, the project demonstrated how explainable machine learning methods can support environmental monitoring and public health forecasting initiatives.
````

