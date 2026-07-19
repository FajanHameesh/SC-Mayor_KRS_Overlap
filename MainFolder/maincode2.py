import pandas as pd

def runn(df1,df2,paralel:str):    
    df1 = df1[df1['paralel']==paralel]
    df1 = df1[['matkul','hari','jam','paralel','jenis']]

    df2 = df2[['matkul','hari','jam','paralel','jenis']]

    df1[['mulai','selesai']] = df1['jam'].str.split("-",n=1,expand=True)
    df2[['mulai','selesai']] = df2['jam'].str.split("-",n=1,expand=True)
    df1['startMin'] = df1['mulai'].str[0:2].astype(int)*60 + df1['mulai'].str[3:5].astype(int)
    df2['startMin'] = df2['mulai'].str[0:2].astype(int)*60 + df2['mulai'].str[3:5].astype(int)
    df1['endMin'] = df1['selesai'].str[0:2].astype(int)*60 + df1['selesai'].str[3:5].astype(int)
    df2['endMin'] = df2['selesai'].str[0:2].astype(int)*60 + df2['selesai'].str[3:5].astype(int)

    def check_overlap(row, df_ref):
        for _, ref in df_ref.iterrows():
            if row["startMin"] < ref["endMin"] and row["endMin"] > ref["startMin"]:
                return True

        return False
    
    grouped1 = df1.groupby(by='hari')
    overlap_hasil = []
    for _,row in df2.iterrows():
        hari = row['hari']

        if hari in grouped1.groups:
            overlap = check_overlap(
                row,
                grouped1.get_group(hari)
            )
        else:
            overlap = False
        
        overlap_hasil.append(overlap)
    df2['overlap'] = overlap_hasil
    # df2["overlaps"] = df2.apply(
    # lambda row: (
    #     check_overlap(row, grouped1.get_group(row["hari"]))
    #     if row["hari"] in grouped1.groups
    #     else False
    # ),
    # axis=1
    # )
    df2 = df2[['matkul','jenis','paralel','hari','jam','overlap']]
    df2["overlap"] = df2["overlap"].apply(
    lambda x: "✅" if x else "❌"
    )
    df2New = df2[df2['overlap'] == '❌']
    df2baru = df2New[df2New["paralel"].duplicated(keep=False)]
    return df2, df2New, df2baru

