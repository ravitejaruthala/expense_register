from support_file import *

streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

pages = {
    "Page Navigation" : [
        st.Page("Add_Data.py", title="Enter your data."),
        st.Page("View_Data.py", title="View your data."),
        st.Page("Update_Data.py", title="Update your data.")
    ],
}
pg = st.navigation(pages)
pg.run()
initialize_db()
st.markdown(streamlit_style, unsafe_allow_html=True)