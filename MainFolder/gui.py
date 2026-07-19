import streamlit as st
from .maincode1 import scrapper
from .maincode2 import runn
from .codeinf import codeinf
from .listMK import listMK
from pathlib import Path

base_dir = Path(__file__).resolve().parent

def gui():
    st.image(base_dir/"banner.png", use_container_width=False)

    st.title("SC-Mayor Overlap Tracker awkwkw")
    st.markdown(
    """
    ### Additional Links:
    
    • [Readme](https://github.com/FajanHameesh/SC-Mayor_KRS_Overlap/blob/main/README.md)
    • [Simak IPB](https://simak.ipb.ac.id/Publik/JadwalKuliah)
    • [StudentPortal](https://studentportal.ipb.ac.id)
    """
)

    semester = st.selectbox(
        "Semester: ",
        ['Ganjil','Genap']
    )

    col1, col2 = st.columns(2)

    if semester == 'Ganjil':
        bound3 = 196041
        bound4 = bound3
        semId = 113

        with col1:
            bound1 = st.number_input(
            "ID paling bawah matkul semester terkait",
            min_value=0,
            value=192730
        )
            st.info(f"{codeinf(bound1)}")

        with col2:
            bound2 = st.number_input(
            "ID paling atas matkul semester terkait",
            min_value=0,
            value=192738
        )
            st.info(f"{codeinf(bound2)}")  

    elif semester == 'Genap':      
        bound1 = 196041
        bound2 = bound1
        semId = 114
        with col1:
            bound3 = st.number_input(
            "ID paling bawah matkul semester terkait",
            min_value=0,
            value=196041
        )
            st.info(f"{codeinf(bound3)}")

        with col2:
            bound4 = st.number_input(
            "ID paling atas matkul semester terkait",
            min_value=0,
            value=196041
        )
            st.info(f"{codeinf(bound4)}")

    listmk = listMK(semId)
    bound5_raw = st.selectbox(
        "Matkul SC",
        listmk.keys()
    )
    bound5 = listmk[bound5_raw]
    st.info(
        f'[Info SC](https://krs.ipb.ac.id/MK/{str(bound5)})'
        )

    paralell = st.number_input(
        "Paralel (Currently can't handle mixed mayor paralel)",
        min_value=1,
        value=1
    )

    # Tombol eksekusi
    if st.button("Analisa"):

        with st.spinner("Mengambil data..."):
            df1 = scrapper(bound1,bound2+1,bound3,bound4)
            df2 = scrapper(bound5,bound5+1,bound5,bound5)
            df3,df3_2,df3_3 = runn(df1,df2,str(paralell))
        st.success("Selesai!")

        # Menampilkan dataframe
        st.subheader("Mayor (all paralel)")
        st.dataframe(df1)

        st.subheader("SC")
        st.dataframe(df2)

        st.subheader("Overlap Test (based on selected mayor paralel)")
        st.dataframe(df3)

        st.subheader("Non-Overlap Paralel/s")
        col5, col6 = st.columns(2)
        
        with col5:
            st.dataframe(df3_2)
        with col6:
            df1_filtered = df1[df1['paralel']==str(paralell)]
            st.dataframe(df1_filtered[['matkul','jenis','paralel','hari','jam']])
        
        st.subheader("Possible SC Paralel")
        st.dataframe(df3_3)
