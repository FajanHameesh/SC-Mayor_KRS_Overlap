# Mengidentifikasi nama MK untuk beberapa sampel ID_URL

import requests
import pandas as pd
import streamlit as st

@st.cache_data(max_entries=2)
def listMK(id):
    use_url = f"https://krs.ipb.ac.id/api/StokSupportingCourse?tahunSemesterId={str(id)}"
    response = requests.get(use_url)
    data = response.json()

    result0 = {}
    for idx,i in enumerate(data):
        result0[i["Nama"]] = int(i['KurikulumId'])
    return result0



