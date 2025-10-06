Full-Stack Sales Optimization Engine: From Raw Data to Live BI.
Overview
This project demonstrates the complete workflow of a Data Scientist by transitioning raw, historical sales data into a live, interactive Business Intelligence (BI) application using Streamlit. The core objective is to provide dynamic tools for optimizing sales performance, tracking key metrics, and visualizing revenue trends in real-time.

Dataset
The analysis is based on historical Amazon Sales Data. Key metrics include:

Time Series: Order Date

KPIs: Total Revenue, Total Profit

Dimensions: Region, Item Type

Methodology
Refactoring & Modularization: All core analysis logic (KPI calculation, trend plotting) was successfully moved from Jupyter Notebooks into reusable Python functions within the src/analysis.py file, ensuring modularity and maintainability.

Web Integration (Streamlit): The app.py file uses Streamlit to create the full-stack application, linking the user interface (interactive filters) with the backend logic.

Deployment: The final application is deployed to the Streamlit Community Cloud, making it accessible as a public-facing web service.

Key Features
Interactive Filters: Users can instantly filter all metrics and charts by Region and Item Type using the sidebar.

Live KPI Display: Total Revenue and Total Profit metrics update in real-time based on the applied filters.

Time Series Analysis: Displays interactive charts (using Plotly) of sales/revenue trends over time.

Tools and Technologies
Framework: Streamlit (for the full-stack web application)

Data Science: Pandas (data processing)

Visualization: Plotly Express (interactive charts)

Languages: Python

How to Run the Application
Clone the Repository:
[Provide the command to clone your project from a platform like GitHub.]

Install Dependencies:
pip install -r requirements.txt

Launch the Dashboard: Navigate to the project's root directory in your terminal and run:
streamlit run app.py






G