import base64
import os
import random
from PIL import Image
import pandas as pd
import streamlit as st

# 1. Define your target Excel file
EXCEL_FILE = "TESTGUESTLIST.xlsx"

# Page configuration
st.set_page_config(page_title="The Wedding Machine", page_icon="💍", layout="centered")

image_file = "TWMB.jpg"


def set_background(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode()

        st.markdown(
            f"""
            <style>
            /* Force the background onto the main view wrapper */
            .stApp {{
                background-image: url("data:image/jpeg;base64,{encoded_string}") !important;
                background-size: cover !important;
                background-position: center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
            }}

            /* Clear out default solid background overlays blocking it */
            .stMain, .stMainBlockContainer {{
                background: transparent !important;
            }}

            .wedding-title {{
                background-color: rgba(139, 90, 43, 0.9);
                color: #FDFBF7;
                padding: 12px;
                border-radius: 6px;
                border: 2px solid #4A2E1B;
                text-align: center;
                font-family: 'Palatino', serif;
                font-weight: bold;
                font-size: 1.1rem;
                margin-bottom: 20px;
            }}
            .custom-label {{
                background-color: rgba(139, 90, 43, 0.9);
                color: #FDFBF7;
                padding: 8px 12px;
                border-radius: 6px;
                border: 2px solid #4A2E1B;
                display: inline-block;
                font-size: 0.95rem;
                margin-bottom: 5px;
            }}
            .stButton > button {{
                background-color: #8B5A2B !important;
                color: #FDFBF7 !important;
                border: 2px solid #4A2E1B !important;
                border-radius: 6px !important;
                width: 100%;
                font-weight: bold;
            }}
            .stButton > button:hover {{
                background-color: #5C3A21 !important;
                color: #FDFBF7 !important;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.error(f"Could not find image file: {image_file}")
# App Header
st.title("💍 The Wedding Machine")
st.write("Welcome! Enter your name below to find your seat and assignment.")

# Link opening utility (replaces webbrowser.open)
st.sidebar.markdown("[Go to Wedding Website](https://example.com)")

# Input Section
search_term = st.text_input("Enter your Name (First Name, Last Name, or Nickname):", placeholder="e.g., Juan").strip()
search_button = st.button("Search Guest List", type="primary")

# Search Logic
if search_button:
    # Safety Check: If the search box is empty
    if not search_term:
        st.warning("⚠️ Please type a name first!")

    # Safety Check: If the Excel file is missing
    elif not os.path.exists(EXCEL_FILE):
        st.error(f"❌ File Error: Could not find file '{EXCEL_FILE}'")

    else:
        # Read the excel file
        df = pd.read_excel(EXCEL_FILE)

        # Combine columns for a full-name lookup
        fullname = df["Pangalan"].astype(str) + " " + df["Apelido"].astype(str)

        # Filter dataframe for matching names
        results = df[
            df["Pangalan"].astype(str).str.contains(search_term, case=False, na=False) |
            df["Apelido"].astype(str).str.contains(search_term, case=False, na=False) |
            fullname.str.contains(search_term, case=False, na=False)
            ]

        # Case 1: No results found
        if results.empty:
            st.info("💡 You were using your whole name weren't you? Go on try your nickname :)")

        # Case 2: Exactly one match found
        elif len(results) == 1:
            guest = results.iloc[0]

            # Select a random comment from the available columns
            randocomment = guest[random.choice(["Mungkahi1", "Mungkahi2"])]

            # Display successful guest information
            st.success(f"### 🎉 Welcome, {guest['Pangalan']} {guest['Apelido']}!")
            st.markdown(f"**Your Assignment:** {guest['Gawain']}")
            st.info(f"💬 *{randocomment}*")

        # Case 3: Multiple matches found
        elif len(results) > 1:
            st.warning("⚠️ **Multiple Matches Found**")
            st.write("I found multiple guests matching your search. Please search again using your full name.")

            # Display the matching names neatly in a list
            for _, guest in results.iterrows():
                st.markdown(f"• **{guest['Pangalan']} {guest['Apelido']}** — {guest['Gawain']}")

# 7. Action Links & Buttons
if st.button("Show me the invitation!"):
    st.markdown(
        "[Click here to open the invitation](https://www.canva.com/design/DAHLwCT15lo/gAiU1GbQT-QrcsTOZ_uvSA/view?utm_content=DAHLwCT15lo&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h417e3fcbf5)",
        unsafe_allow_html=True,
    )

if st.button("When and where is the wedding happening?"):
    st.markdown(
        "[Click here to open wedding details](https://lascabanasbypollas.lodgify.com)",
        unsafe_allow_html=True,
    )

st.write("---")

# 8. Turn off / Exit Simulation
if st.button("Turn off the Wedding Machine"):
    st.info(
        "The Wedding Machine is safely running in the cloud. You can simply close this browser tab!"
    )