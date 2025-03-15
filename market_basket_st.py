#IMPORTING LIBRARIES
import streamlit as st
import pandas as pd
import joblib

# APPLY CUSTOM CSS FOR STYLING
st.markdown(
    """
    <style>
        body {
            background-color: #d7ebf6;
        }
        .stApp {
            background-color: #d1e8ff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        }
        h1 {
            color: #800020;
        }
        .stSelectbox label {
            font-size: 16px;
            font-weight: bold;
            color: #333;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# LOAD FP-GROWTH RULES FROM THE SAVED .PKL FILE
rules_fp = joblib.load(r"D:\MARKET BASKET ANALYSIS\fp rules.pkl")

# EXTRACT UNIQUE PRODUCT NAMES FROM ANTECEDENTS FOR THE DROPDOWN
unique_products = sorted(set(item for items in rules_fp["antecedents"] for item in items))

# ADD SIDEBAR FOR OVERVIEW
st.sidebar.title("💡 App Overview")
st.sidebar.write("This Market Basket Recommendation System uses **FP-Growth** to find frequently bought-together products.")
st.sidebar.write("Select a product from the dropdown, and the system will recommend other products that are commonly purchased with it.")
st.sidebar.write("📌 **Key Features:**")
st.sidebar.markdown("- FP-Growth Algorithm for fast association rule mining")
st.sidebar.markdown("- Lift Score-based ranking for strong recommendations")
st.sidebar.markdown("- Interactive and user-friendly interface")

# STREAMLIT UI
st.title("🛒 MARKET BASKET ANALYSIS")
st.markdown("<br>", unsafe_allow_html=True)  # Adds a larger space
st.write("Select a product to see frequently bought-together products.")

# USER INPUT - SELECT BOX
product_input = st.selectbox("🔍 Choose a Product:", unique_products)

# WRITE RECOMMENDATION LOGIC
if product_input:
    # FIND RULES WHERE THE SELECTED PRODUCT APPEARS IN THE ANTECEDENTS
    matching_rules = rules_fp[rules_fp["antecedents"].apply(lambda x: product_input in x)]
    
    if not matching_rules.empty:
        # EXTRACT RECOMMENDED PRODUCTS AND SORT BY LIFT SCORE
        recommended_products = matching_rules.explode("consequents")[["consequents", "lift"]]
        recommended_products = recommended_products.sort_values(by="lift", ascending=False)

        # REMOVE DUPLICATE RECOMMENDATIONS, KEEPING THE HIGHEST LIFT SCORE
        recommended_products = recommended_products.drop_duplicates(subset=["consequents"], keep="first")

        # DISPLAY RECOMMENDATIONS
        st.subheader("🛍️ Frequently Bought Together:")
        for _, row in recommended_products.iterrows():
            st.write(f"✅ **{row['consequents']}** (Lift: {row['lift']:.2f})")
    else:
        st.warning("No strong associations found for this product. Try another one!")
