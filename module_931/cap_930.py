import os

import streamlit as st
from dotenv import load_dotenv
from google import genai


# The .env file keeps the Gemini API key separate from the Python code.
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if api_key is None:
    st.error("The Gemini API key was not found in the .env file.")
    st.stop()

client = genai.Client(api_key=api_key)


st.title("🤖 Sales Assistant")


# These fields collect the information required by the assignment.
product_name = st.text_input("Product name", "Customer Analytics Platform")

company_url = st.text_input("Company URL",  "https://sephora.com")

product_category = st.text_input(
    "Product category", "Data and customer analytics")

competitors = st.text_area(
    "Competitors",
    "https://www.ulta.com\nhttps://www.amazon.com\nhttps://www.walmart.com"
)

value_proposition = st.text_area(
    "Value proposition", "Our platform helps retail teams understand customer behavior.")

target_customer = st.text_input(
    "Target customer",
    "Director of Marketing"
)

uploaded_file = st.file_uploader(
    "Optional product overview",
    type=["pdf", "docx", "txt"]
)


if st.button("Generate Sales Insights"):

    if product_name == "":
        st.error("Please enter a product name.")

    elif company_url == "":
        st.error("Please enter a company URL.")

    elif product_category == "":
        st.error("Please enter a product category.")

    elif value_proposition == "":
        st.error("Please enter a value proposition.")

    elif target_customer == "":
        st.error("Please enter a target customer.")

    else:
        # This prompt organizes the information into the report sections.
        prompt = f"""
Create a simple one-page sales report.

Prospective company: {company_url}
Product: {product_name}
Product category: {product_category}
Competitors: {competitors}
Value proposition: {value_proposition}
Target customer: {target_customer}

Use these sections:

1. Company Strategy
2. Competitor Mentions
3. Leadership Information
4. Product and Strategy Summary
5. Source Links

Use clear and simple language.
Only include information related to this sales project.
If information cannot be confirmed, say that it is not confirmed.
Do not create fake links.
"""

        # Model choice: Gemini was used because it can create text summaries.
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        # This displays the one-page report created by Gemini.
        st.header("One-Page Sales Report")
        st.write(response.text)

        # This displays the source link entered by the user.
        st.header("Source Link Provided")
        st.write(company_url)

        if uploaded_file is not None:
            st.write("Product overview uploaded:", uploaded_file.name)
