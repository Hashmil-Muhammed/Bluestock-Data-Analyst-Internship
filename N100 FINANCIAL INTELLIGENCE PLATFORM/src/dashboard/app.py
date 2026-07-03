import streamlit as st

# Set page configuration
st.set_page_config(
    page_title = "Nifty 100 Intelligence",
    page_icon = "📈",
    layout ="wide",
    initial_sidebar_state = "expanded"
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
