import streamlit as st
from .maincode1 import scrapper
from .maincode2 import runn
from .codeinf import codeinf
from .listMK import listMK
def gui():

    st.title("SC-Mayor Overlap Tracker awkwkw")

    # Input user
    bound1 = st.number_input(
        "ID Ganjil Lower",
        min_value=0,
        value=192730
    )
    st.info(f"{codeinf(bound1)}")

    bound2 = st.number_input(
        "ID Ganjil Upper",
        min_value=0,
        value=192738
    )
    st.info(f"{codeinf(bound2)}")

    bound3 = st.number_input(
        "ID Genap Lower",
        min_value=0,
        value=196041
    )
    st.info(f"{codeinf(bound3)}")

    bound4 = st.number_input(
        "ID Genap Upper",
        min_value=0,
        value=196041
    )
    st.info(f"{codeinf(bound4)}")

    listmk = listMK()
    bound5_raw = st.selectbox(
        "Matkul SC",
        listmk
    )
    bound5,_ = str(bound5_raw).split('-',maxsplit=1)
    bound5 = int(bound5)

    paralell = st.number_input(
        "Paralel",
        min_value=1,
        value=1
    )

    # Tombol eksekusi
    if st.button("Analisa"):

        with st.spinner("Mengambil data..."):
            df1 = scrapper(bound1,bound2+1,bound3,bound4)
            df2 = scrapper(bound5,bound5+1,bound5,bound5)
            df3,df3_2 = runn(df1,df2,str(paralell))
        st.success("Selesai!")

        # Menampilkan dataframe
        st.subheader("Mayor (all paralel)")
        st.dataframe(df1)

        st.subheader("SC")
        st.dataframe(df2)

        st.subheader("Overlap Test (based on selected mayor paralel)")
        st.dataframe(df3)

        st.subheader("Non-Overlap Paralel/s")
        st.dataframe(df3_2)
