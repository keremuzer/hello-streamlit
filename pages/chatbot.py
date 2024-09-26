import streamlit as st
import requests

# Assuming you have your API key stored securely (not shown here)
API_KEY = ""  # Replace with your actual API key
API_URL = ""  # Replace with your API endpoint

def query_api(file_data, chunk_size=1, chunk_overlap=1, separator="example"):
    headers = {"Authorization": f"Bearer {API_KEY}"}  # Include authorization header

    try:
        response = requests.post(
            API_URL,
            files={"files": (file_data.name, file_data.read(), "application/pdf")},
            data={"chunkSize": chunk_size, "chunkOverlap": chunk_overlap, "separator": separator},
            headers=headers,
        )
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None

st.title("Chatbot Interface")

file_uploader = st.file_uploader("Upload a PDF file:", type="pdf")

if file_uploader is not None:
    # Display a spinner while processing the file
    with st.spinner("Processing..."):
        output = query_api(file_uploader)

    if output is not None:
        st.success("API call successful!")
        # Display the API response in a clear and informative way (modify based on your API's output)
        st.write(output)
    else:
        st.error("API call failed. Please check the console for errors.")
