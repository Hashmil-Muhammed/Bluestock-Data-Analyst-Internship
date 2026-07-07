import streamlit as st
import os
import sys
from pathlib import Path

# 1. First: Set up the path
root_path = Path(__file__).resolve().parents[1] # This points to the 'src' folder
sys.path.append(str(root_path))

# 2. Second: Now import from dashboard
from dashboard.utils.db import load_data

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set page configuration
st.set_page_config(
    page_title="Nifty 100 Intelligence",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar configuration (Logo & Navigation)
st.sidebar.title("Nifty 100 Intelligence")
st.sidebar.markdown("---")
st.sidebar.write("welcome, AI Engineer Hashmil")

# Main title
st.title("Nifty 100 Intelligence Platform")
st.subheader("Capstone Project - Bluestock Fintech Internship")

st.markdown("""
### welcome to Your Financial Analytics Dashboard
Use the sidebar to Navigate through the different analytical modules:
1. **Home / Overview**
2. **Company Profile**
3. **Financial Screener**
4. **Peer Comparison**
5. **Trend Analysis**
6. **Sector Analysis**
7. **Capital Allocation Map**
8. **Annual Reports**
""")

# Custom CSS for branding
st.markdown("""
            <style>
               .stApp {
                   background-color: #f8f9fa;
               }
               .sidebar .sidebar-content {
                   background-color: #ffffff;
               }
            </style>
""", unsafe_allow_html=True)
