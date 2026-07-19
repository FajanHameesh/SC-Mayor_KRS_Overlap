# Mengidentifikasi nama MK untuk beberapa sampel ID_URL

import requests
import pandas as pd
import streamlit as st

@st.cache_data(max_entries=2)
def listMK():
    use_url = "https://krs.ipb.ac.id/api/StokSupportingCourse?tahunSemesterId=113"
    response = requests.get(use_url)
    data = response.json()

    result0 = []
    for idx,i in enumerate(data):
        hasil = (f'{i['KurikulumId']} - {i['Nama']}')
        result0.append(hasil)
        print(f'\n{i['KurikulumId']} - {i['Nama']} Done')
    return result0



