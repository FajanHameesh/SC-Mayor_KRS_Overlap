import requests
import pandas as pd
import tkinter as tk

base_url = 'https://krs.ipb.ac.id/api/DetailMataKuliah?kurikulumId='

def ambildata(id):
    use_url = base_url+str(id)
    response = requests.get(use_url)
    data = response.json() # type(data): dict

    hasil = ({
        "ID": id,
        "KODE":data['Kode'],
        "MK":data['Nama']
    })
    return hasil

# Untuk Program Studi Fisika rentang ID matakuliah yang diampu berada pada sekitar rentang:
# 196041-196060 pada semester genap
# 192724-192743 pada semester ganjil

hasil_1 = []

for i in range(196041,196041+3):
    hasil_1.append(ambildata(i))
    print(f'\nID:{i} done')

df = pd.DataFrame(hasil_1)

print(hasil_1)
print(df)
