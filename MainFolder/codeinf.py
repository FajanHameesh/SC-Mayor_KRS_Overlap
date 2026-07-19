import requests
import streamlit as st
base_url = 'https://krs.ipb.ac.id/api/DetailMataKuliah?kurikulumId='

@st.cache_data(max_entries=2)
def codeinf(id):
    use_url = base_url+str(id)
    response = requests.get(use_url)
    data = response.json() # type(data): dict
    return data['Nama']
