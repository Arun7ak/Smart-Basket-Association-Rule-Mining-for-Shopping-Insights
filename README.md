# Smart-Basket-Association-Rule-Mining-for-Shopping-Insights

This project analyzes grocery transactions using association rule mining. It uses both Apriori and FP-Growth algorithms to generate association rules and saves the models with Joblib. A Streamlit app lets you choose a product and see which items are frequently bought together.

## Features
- **Data Preparation:** Downloaded from Kaggle, cleaned with Pandas, and performed EDA .
- **Association Rule Mining:** Implemented using Apriori and FP-Growth.
- **Model Saving:** Models are saved with Joblib.
- **Interactive App:** A Streamlit app provides product recommendations based on the generated rules.

## How to Use
1. **Run the Notebook:**  
   Execute `MODEL_TRAINING.ipynb` to process the data, generate rules, and save the models.

2. **Launch the App:**  
   Run the following command:
   ```bash
   streamlit run market_analysis_st.py
   ```
   Then select a product from the dropdown to see frequently bought together items.
   
## Requirements
- Python  
- Pandas  
- mlxtend  
- Joblib  
- Streamlit
