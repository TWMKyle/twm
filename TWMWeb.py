import ssl

import base64
import os
import random
from PIL import Image
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection, gsheets_connection

st.video("https://www.youtube.com/watch?v=XKR0O5OM1iw")

# Bypass SSL certificate verification
os.environ['CURL_CA_BUNDLE'] = ''
ssl._create_default_https_context = ssl._create_unverified_context

# 1. Define your target Excel file
#EXCEL_FILE = "TESTGUESTLIST.xlsx"

if "active_guest" not in st.session_state:
    st.session_state.active_guest = None
if "rsvp_status" not in st.session_state:
    st.session_state.rsvp_status = None
if "random_comment" not in st.session_state:
    st.session_state.random_comment = None

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(ttl=0) # ttl=0 ensures you don't cache stale data on fresh reads


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
st.write("Welcome! I hope you are as excited as us! Check out this page!")

# Link opening utility (replaces webbrowser.open)
st.sidebar.markdown("[Go to Wedding Website](https://example.com)")

# Input Section
search_term = st.text_input("Enter your Name:", placeholder="e.g., Pat, Kyle").strip()
search_button = st.button("Search Your Name", type="primary")

# Search Logic
if search_button:

    # Always clears out all values
    st.session_state.active_guest = None
    st.session_state.rsvp_status = None
    st.session_state.random_comment = None

    # Displays a neat audio controller bar so guests can pause or adjust volume


    # Safety Check: If the search box is empty
    if not search_term:
        st.warning("⚠️ Please type a name first!")

    # Old Safety Check: If the Excel file is missing
    #elif not os.path.exists(GList):
    #    st.error(f"❌ File Error: Could not find file '{GList}'")

    # New Safety Check
    elif df is None or df.empty:
        st.error("❌ Data Error: Could not load data from Google Sheets")

    else:
        # Read the excel file
        # df = pd.read_excel(GList)

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
            st.info("💡 I can't seem to find you, can you please try again? :)")

        # Case 2: Exactly one match found
        elif len(results) == 1:
            guest = results.iloc[0]
            st.session_state.active_guest = results.iloc[0]
            st.session_state.random_comment = random.choice(["Mungkahi1", "Mungkahi2"])
            st.session_state.rsvp_status = None

            # Select a random comment from the available columns
            randocomment = guest[random.choice(["Mungkahi1", "Mungkahi2"])]


            # Display successful guest information
            st.success(f"### 🎉 Welcome, {guest['Pangalan']} {guest['Apelido']}!")
            st.markdown(f"**Your Assignment:** {guest['Gawain']}")
            st.info(f"💬 *{randocomment}*")

            st.rerun()

        # Case 3: Multiple matches found
        elif len(results) > 1:
            st.warning("⚠️ **Multiple Matches Found**")
            st.write("I found multiple guests matching your search. Try using your nickname or full name.")

            # Display the matching names neatly in a list
            for _, guest in results.iterrows():
                st.markdown(f"• **{guest['Pangalan']} {guest['Apelido']}** — {guest['Gawain']}")

## --- DISPLAY & RSVP PANEL - --
# This code runs outside the search button block, reading directly from memory!
if st.session_state.active_guest is not None:
    guest_row_index = st.session_state.active_guest.name
    guest = st.session_state.active_guest
    comment_col = st.session_state.random_comment
    randocomment = guest[comment_col]

    # Display guest information
    st.success(f"### 🎉 Welcome, {guest['Pangalan']} {guest['Apelido']}!")
    st.markdown(f"**Your Assignment:** {guest['Gawain']}")
    st.info(f"💬 *{randocomment}*")

    st.write("---")
    st.write("**Are you attending?**")

    # Side-by-side RSVP buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("👍 Yes, I'll be there!", key="btn_yes", use_container_width=True):
            df.at[guest_row_index, 'RSVP_Status'] = "attending"
            df ['RSVP_Status'] = df['RSVP_Stauts'].astype(str)
            updated_row = df.loc[[guest_row_index]]
            conn.update(worksheet="Sheet1", data=updated_row)
            st.session_state.rsvp_status = "attending"
            st.rerun()

    with col2:
        if st.button("👎 No, I can't make it", key="btn_no", use_container_width=True):
            df.at[guest_row_index, 'RSVP_Status'] = "declined"
            df ['RSVP_Status'] = df['RSVP_Stauts'].astype(str)
            updated_row = df.loc[[guest_row_index]]
            conn.update(worksheet="Sheet1", data=updated_row)
            st.session_state.rsvp_status = "declined"
            st.rerun()


    # Evaluate the RSVP choice from state memory
    if st.session_state.rsvp_status == "attending":
        st.balloons()
        st.success("💖 Thank you for that! We will see you on our wedding day!")
    elif st.session_state.rsvp_status == "declined":
        st.info("😢 We will miss you! Thank you for letting us know.")
## end of RSVP

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
