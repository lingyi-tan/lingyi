import streamlit as st
from pathlib import Path

md_path = Path.cwd() / "markdown"
md_file = md_path / __file__.replace("py", "md")

st.markdown(Path(md_file).read_text(), unsafe_allow_html=True)