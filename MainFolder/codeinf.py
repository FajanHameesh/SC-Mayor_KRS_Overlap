import requests
base_url = 'https://krs.ipb.ac.id/api/DetailMataKuliah?kurikulumId='

def codeinf(id):
    use_url = base_url+str(id)
    response = requests.get(use_url)
    data = response.json() # type(data): dict
    return data['Nama']