import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="TEXCHEM AI Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("TEXCHEM AI Cloud Assistant")
st.write("Welcome to TEXCHEM's Excel Data Assistant")

st.divider()

st.subheader("Upload Excel File")

uploaded_file = st.file_uploader(
    "Apni Excel file select karein",
    type=["xlsx", "xls"]
)

if uploaded_file is not None:
    try:
        excel_file = pd.ExcelFile(uploaded_file)

        sheet_name = st.selectbox(
            "Excel Sheet select karein",
            excel_file.sheet_names
        )

        df = pd.read_excel(
            uploaded_file,
            sheet_name=sheet_name
        )

        st.success("Excel file successfully load ho gayi!")
        st.dataframe(df, use_container_width=True)

        st.write("Total Rows:", len(df))
        st.write("Total Columns:", len(df.columns))

    except Exception as e:
        st.error(f"Excel file read nahi ho saki: {e}")
