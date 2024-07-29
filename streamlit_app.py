import streamlit as st

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"]  > .main {{
background-image: url("https://www.popsci.com/wp-content/uploads/2022/10/31/NearEarthObject_40085801.jpg?auto=webp&width=1440&height=1080");
background-size: 100%;
background-position: top left;
background-reapeat: no-reapeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar] {{
right:2rem;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("neo.jpg");
background-position: center;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Near Earth Object")
st.sidebar.header("Object")
