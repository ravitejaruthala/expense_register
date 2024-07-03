from support_file import *

provider_options = ["Canadian Tire","Food Basics","Home Depot","Metro","No Frills", "Walmart", "None of the above"]
category_options = ["Gas","Grocery","Home Improvement"]

with st.form("Expenses_Form", clear_on_submit=True):
    input_date = st.date_input("**Enter the date of the purchase:**")
    input_bill = st.text_input("**Enter the bill number:**", max_chars=50, placeholder="Type here")
    input_provider = st.selectbox("**Service Provider:**", provider_options, index=None, placeholder="Select")
    input_category = st.selectbox("**Purchase Category:**", category_options, index=None, placeholder="Select")
    input_pretax = st.number_input("**Insert the pre-tax amount:**", value=None, placeholder="0.00")
    input_tax = st.number_input("**Insert the tax amount**", value=None, placeholder="0.00")
    input_comments = st.text_area("**Purchase comments:**", placeholder="Add comments, if any.")
    columns = st.columns([12, 1.5], gap="small")
    with columns[0]:
        submitted = st.form_submit_button("Submit")
    with columns[1]:
        reseted = st.form_submit_button('Reset')
    if submitted:
        save_expenses(input_date, input_bill, input_provider, input_category, round(float(input_pretax),2), round(float(input_tax),2), input_comments)
    elif reseted:
        st.session_state.bill_value = None
        st.toast('All the values were cleared!', icon="🧹")

        

        
        


