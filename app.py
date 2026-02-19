import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fundamental Dashboard", layout="wide")
st.title("ファンダメンタル分析ダッシュボード（テスト起動）")

csv_file = st.file_uploader("前提数値一覧CSV（縦持ち）", type=["csv"])
if csv_file is None:
    st.info("CSVをアップすると表示します。")
else:
    df = pd.read_csv(csv_file)
    st.dataframe(df, use_container_width=True)
