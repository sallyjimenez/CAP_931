# Sales Agent Prototype Project

## Purpose

This project is a sales assistant prototype. It uses Gemini to create a short sales report about a prospective company.

## Features

I created a Streamlit application in Python that allows a sales representative to enter:

- Product name
- Company URL
- Product category
- Competitors
- Value proposition
- Target customer
- Optional product overview file

The application checks that the required fields are completed before generating a report.

## Gemini Integration

I connected the application to the Gemini API using the Google GenAI Python package.

The API key is stored in a `.env` file instead of being written directly in the Python code. This helps protect the API key.

The Gemini prompt asks for:

1. Company Strategy
2. Competitor Mentions
3. Leadership Information
4. Product and Strategy Summary
5. Source Links

## Output

The application displays a one page sales report in the browser. It also displays the company URL as a source link and shows the name of an uploaded product overview file when one is provided.

## Tools Used

- Python
- Streamlit
- Gemini API
- Google GenAI Python package
- python-dotenv
- uv
- GitHub

## How to Run the Project

Install the project packages:

```text
uv sync
```
