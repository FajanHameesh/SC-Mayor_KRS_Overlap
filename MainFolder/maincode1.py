import requests
import pandas as pd

base_url = 'https://krs.ipb.ac.id/api/DetailMataKuliah?kurikulumId='

def scrapper(id_ganjil_lower,id_ganjil_upper,id_genap_lower,id_genap_upper):

    def ambildata(id):
        use_url = base_url+str(id)
        response = requests.get(use_url)
        data = response.json() # type(data): dict
        return data

    def pisahstring(teks:str):
        waktu, ruangan = teks.split('di',maxsplit=1)
        hari,jam = waktu.split(" ",maxsplit=1)
        return hari, jam, ruangan


    def ambildata1(data):
        dt1 = data['ListJadwal']
        hasil_list = []
        for k in dt1:
            hari,jam,ruangan = pisahstring(k['Jadwal'][0])
            hasil = ({
                "matkul":data["Nama"],
                "jenis":k["JenisKelas"],
                "paralel":k["KelasParalel"],
                "hari":hari,
                "jam":jam,
                "ruangan":ruangan,
                "JadwalID":k["JadwalKuliahId"]
            })
            hasil_list.append(hasil)
        return hasil_list



    # Untuk Program Studi Fisika rentang ID matakuliah yang diampu berada pada sekitar rentang:
    # 196041-196060 pada semester genap
    # 192724-192743 pada semester ganjil

    # id_ganjil_lower = 192724
    # id_ganjil_upper = 192744
    # id_genap_lower = 196041
    # id_genap_upper = 196061

    id_list = [i for i in range(id_ganjil_lower,id_ganjil_upper)]+[i for i in range(id_genap_lower,id_genap_upper)]



    result0 = []
    for i in id_list:
        print(f"\nID: {i} start")
        raw = ambildata(str(i))

        result1 = (ambildata1(raw))
        for j in result1:
            result0.append(j)

        print(f"ID: {i} done")

    df_1 = pd.DataFrame(result0)
    return df_1