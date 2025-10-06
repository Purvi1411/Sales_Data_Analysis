import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- Data Loading and Caching ---
@st.cache_data
def load_data():
    """Loads and returns the cleaned sales data, ensuring correct date type."""
    file_path = os.path.join('data', 'processed', 'cleaned_sales_data.csv')
    
    if not os.path.exists(file_path):
        st.error("Processed data file not found! Please check your data folder.")
        return pd.DataFrame()

    df = pd.read_csv(file_path)
    
    # FIX: Use the correct column name 'Order Date' and handle date format
    if 'Order Date' in df.columns:
        df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed') 
    else:
        st.error("Critical column 'Order Date' not found. Please check data cleaning.")
        return pd.DataFrame()
        
    return df

# --- Main Application Logic ---
def main():
    st.set_page_config(layout="wide")
    st.title("Amazon Sales Performance Dashboard 📈")
    
    sales_df = load_data()
    
    if sales_df.empty:
        st.warning("Cannot run analysis. Please ensure your data file is correct.")
        return

    # Get unique categories and regions for filtering
    # Assuming 'Item Type' and 'Region' are correct
    unique_categories = ['All'] + sorted(sales_df['Item Type'].unique().tolist())
    unique_regions = ['All'] + sorted(sales_df['Region'].unique().tolist())

    # --- Sidebar Filtering ---
    with st.sidebar:
        st.header("Filter Options")
        selected_region = st.selectbox('Select Region', unique_regions)
        selected_category = st.selectbox('Select Item Type', unique_categories)

    # Apply filtering
    filtered_df = sales_df
    if selected_region != 'All':
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]
        
    if selected_category != 'All':
        filtered_df = filtered_df[filtered_df['Item Type'] == selected_category]

    
    # --- Integration of KPIs (Key Metrics) ---
    # FIX: Use the correct column names 'Total Revenue' and 'Total Profit'
    total_revenue = filtered_df['Total Revenue'].sum()
    total_profit = filtered_df['Total Profit'].sum()
    total_orders = filtered_df.shape[0] # Total number of rows/orders

    
    # --- Display KPIs ---
    st.header(f"Key Metrics: {selected_category} in {selected_region}")
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Revenue", f"${total_revenue:,.0f}")
    col2.metric("Total Profit", f"${total_profit:,.0f}")
    col3.metric("Total Orders", f"{total_orders:,}")

    st.divider()

    # --- Display Charts (Trend Analysis) ---
    st.subheader("Monthly Sales Trend Analysis")
    
    # FIX: Use 'Total Revenue' as the main metric for the trend chart
    monthly_sales = filtered_df.groupby(filtered_df['Order Date'].dt.to_period('M'))['Total Revenue'].sum().reset_index()
    monthly_sales['OrderDate_Str'] = monthly_sales['Order Date'].astype(str) 
    
    fig = px.line(monthly_sales, x='OrderDate_Str', y='Total Revenue', title='Revenue Volume Over Time', markers=True)
    st.plotly_chart(fig, use_container_width=True)

    # --- Additional Table View ---
    st.subheader("Raw Data Sample")
    st.dataframe(filtered_df.head(10))


if __name__ == "__main__":
    main()