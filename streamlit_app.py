import json
import streamlit as st

def extract_ids(json_data, key='id'):
    """Recursively extracts all 'id' values from JSON data."""
    ids = []
    
    if isinstance(json_data, dict):
        if key in json_data:
            ids.append(json_data[key])
        for value in json_data.values():
            ids.extend(extract_ids(value, key))
    
    elif isinstance(json_data, list):
        for item in json_data:
            ids.extend(extract_ids(item, key))
    
    return ids

# Streamlit App
st.title("JSON ID Extractor")

uploaded_file = st.file_uploader("Upload a JSON file", type=["json"])
if uploaded_file is not None:
    data = json.load(uploaded_file)
    id_list = extract_ids(data)
    st.write("Extracted IDs:")
    st.json(id_list)
