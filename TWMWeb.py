import ssl
import gspread
import base64
import os
import random
from PIL import Image
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection, gsheets_connection


wedding_photos = [
    "https://raw.githubusercontent.com/TWMKyle/twm/main/IMG_8287 2.JPG",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/IMG_82882.JPG",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/IMG_3815.jpg",
]

img_src1 = "https://raw.githubusercontent.com/TWMKyle/twm/main/a38d642b-d7f2-4989-91bc-13fd2048683c.jpg"
img_srcp = "https://raw.githubusercontent.com/TWMKyle/twm/main/rustic-barn-wood-wallpaper-showcasing-natural-browns-textured-finish-perfect-cozy-interiors-countrythemed-decor-ideas_184076-37815.jpg.avif"



# You can stack multiple images or add other sidebar widgets below it
st.sidebar.write("### Wedding Details")
st.sidebar.write("📍 Venue: The Garden Pavilion")
st.sidebar.write("📅 Date: June 20, 2027")
# Link opening utility (replaces webbrowser.open)
st.sidebar.markdown("[Show me the invitation!](https://www.canva.com/design/DAHLwCT15lo/gAiU1GbQT-QrcsTOZ_uvSA/view?utm_content=DAHLwCT15lo&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h417e3fcbf5)")
st.sidebar.markdown("[Show me the venue please!](https://lascabanasbypollas.lodgify.com)")


# 2. Inject styling to target the ENTIRE Streamlit app frame
st.markdown(
    f"""
    <style>
    /* This selector targets the entire background canvas of Streamlit */
    [data-testid="stAppViewContainer"] {{
        background-image: url('{img_src1}') !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }}

    /* Target the main st.title */
    h1, .stApp h1 {{
        color: #FFFFFF !important; /* Rose Gold color */
        font-family: 'Georgia', serif; /* Optional: Elegant wedding font */
    }}

    /* Target the st.write body text */
    p, .stApp p {{
        color: #FFFFFF !important; /* Soft Charcoal dark text */
        font-size: 1.1rem;
    }}


    /* 1. CUSTOM PORTRAIT SCROLLABLE STACK */
    .photo-scroll-container {{
        max-height: 450px;          /* Maximum height of the viewing window */
        overflow-y: scroll;         /* Enables vertical scrolling */
        overflow-x: hidden;         /* Hides horizontal scroll spillover */
        border-radius: 12px;
        padding: 0.5rem;
        background-color: #FAFAFA;  /* Muted background backing track */
        border: 1px solid #EAEAEA;
        margin-bottom: 1.5rem;
    }}

    /* Style the portrait images inside the stack */
    .portrait-stack-img {{
        width: 100%;
        height: auto;
        aspect-ratio: 2 / 3;        /* Forces an elegant portrait frame */
        object-fit: cover;          /* Prevents compression squishing */
        border-radius: 8px;
        margin-bottom: 0.75rem;     /* Space between stacked photos */
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);
        display: block;
        /* FIX: Removed the hardcoded background-image property that was breaking the loop */
    }}

    [data-testid="stSidebar"] {{
        background-image: url('{img_srcp}') !important;
        background-size: contain !important;     /* CHANGE THIS: Fits the whole image */
        background-position: top center !important; /* Pins it neatly to the top edge */
        background-repeat: no-repeat !important;  /* Stops it from tiling vertically */
        background-attachment: scroll !important; /* Lets it scroll away naturally */
        background-color: #FDF6E2 !important;     /* Fallback solid background color below the image */
    }}

    /* OPTIONAL OVERLAY: Makes text highly readable over a busy image background */
    [data-testid="stSidebarUserContent"] {{
        background-color: rgba(255, 255, 255, 0.8) !important; /* White tint with 80% opacity */
        padding: 2rem 1.5rem !important;
        border-radius: 12px;
        margin: 1rem;
    }}

    /* Elegant custom scrollbar tailoring for modern web browsers */
    .photo-scroll-container::-webkit-scrollbar {{
        width: 6px;
    }}
    .photo-scroll-container::-webkit-scrollbar-track {{
        background: transparent;
    }}
    .photo-scroll-container::-webkit-scrollbar-thumb {{
        background: #D4AF37;        /* Gold-tinted slider mechanism */
        border-radius: 10px;
    }}

     /* 2. TYPOGRAPHY SCHEME */
    h1, .stApp h1 {{
        color: #FFFFFF !important; 
        font-family: 'Georgia', serif; 
    }}
    h1 span[data-testid="stMarkdownMaterialIcon"] {{
        color: #FFFFFF !important;
        -webkit-text-fill-color: #D4AF37 !important;
    }}
    p, .stApp p, [data-testid="stSidebar"] p {{
        color: #333333 !important; 
        font-size: 1.1rem;
    }}
    
        /* 3. MOSS GREEN & METALLIC GOLD BUTTONS */
    div[data-testid="stBaseButton-primary"] button,
    div[data-testid="stBaseButton-secondary"] button,
    [data-testid="stAppViewBlockContainer"] button,
    button {{
        background-color: #4A5D4E !important;    /* Solid Moss Green */
        color: #FFFFFF !important;               /* Clean white text for readability */
        border: 2px solid #D4AF37 !important;    /* Metallic Gold Border */
        border-radius: 8px !important;           /* Soft elegant rounded corners */
        font-family: 'Georgia', serif !important;
        font-weight: bold !important;
        padding: 0.5rem 1.5rem !important;
        transition: all 0.3s ease !important;    /* Smooth hover effect */
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1) !important;
    }}

    /* Make text inside buttons explicitly white if nested in paragraph elements */
    div[data-testid="stBaseButton-primary"] button p,
    div[data-testid="stBaseButton-secondary"] button p,
    button p {{
        color: #FFFFFF !important;
    }}

    /* Interactive Hover State: Darker moss green and a glowing gold shadow */
    div[data-testid="stBaseButton-primary"] button:hover,
    div[data-testid="stBaseButton-secondary"] button:hover,
    button:hover {{
        background-color: #3B4B3E !important;    /* Deeper Moss Green on hover */
        border-color: #F3E5AB !important;        /* Brighter Champagne Gold border on hover */
        box-shadow: 0px 6px 15px rgba(214, 175, 55, 0.4) !important; /* Elegant gold glow */
        transform: translateY(-2px);              /* Subtle lift animation */
        cursor: pointer;
    }}
    
    </style>
    """,
    unsafe_allow_html=True
)


html_photo_stack = '<div class="photo-scroll-container">'
for url in wedding_photos:
    html_photo_stack += f'<img src="{url}" class="portrait-stack-img" />'
html_photo_stack += '</div>'

# 2. Inject the scroll stack container right into the side panel
st.sidebar.markdown(html_photo_stack, unsafe_allow_html=True)

st.video("https://www.youtube.com/watch?v=XKR0O5OM1iw")

# Bypass SSL certificate verification
os.environ['CURL_CA_BUNDLE'] = ''
ssl._create_default_https_context = ssl._create_unverified_context

# 1. Define your target Excel file
# EXCEL_FILE = "TESTGUESTLIST.xlsx"

if "active_guest" not in st.session_state:
    st.session_state.active_guest = None
if "rsvp_status" not in st.session_state:
    st.session_state.rsvp_status = None
if "random_comment" not in st.session_state:
    st.session_state.random_comment = None

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(ttl=0)  # ttl=0 ensures you don't cache stale data on fresh reads

credentials = {
    "type": st.secrets["connections"]["gsheets"]["type"],
    "project_id": st.secrets["connections"]["gsheets"]["project_id"],
    "private_key_id": st.secrets["connections"]["gsheets"]["private_key_id"],
    "private_key": st.secrets["connections"]["gsheets"]["private_key"],
    "client_email": st.secrets["connections"]["gsheets"]["client_email"],
    "client_id": st.secrets["connections"]["gsheets"]["client_id"],
    "auth_uri": st.secrets["connections"]["gsheets"]["auth_uri"],
    "token_uri": st.secrets["connections"]["gsheets"]["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["connections"]["gsheets"]["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["connections"]["gsheets"]["client_x509_cert_url"]
}
# Authenticate the secure writer client immediately on app startup
gc = gspread.service_account_from_dict(credentials)

# Page configuration
st.set_page_config(page_title="The Wedding Machine", page_icon="💍", layout="centered")



# App Header
st.title("💍 The Wedding Machine")
st.write("Welcome! I hope you are as excited as us! Check out this page!")


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
    # elif not os.path.exists(GList):
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
            try:
                # Open sheet and target your column coordinate smoothly
                sh = gc.open_by_url(
                    "https://docs.google.com/spreadsheets/d/1QsBYqBDMM5VGixJE-gA_xGcSi78kDJSKSqFOSAJ8k98/edit?gid=0#gid=0")
                ws = sh.worksheet("Sheet1")

                row_to_update = int(guest_row_index) + 2
                ws.update_cell(row_to_update, 6, "attending")  # Updates ONLY column F cell

                st.session_state.rsvp_status = "attending"
                st.rerun()
            except Exception as e:
                st.error(f"❌ Cloud Write Error: {e}")

    with col2:
        if st.button("👎 No, I can't make it", key="btn_no", use_container_width=True):
            try:
                sh = gc.open_by_url(
                    "https://docs.google.com/spreadsheets/d/1QsBYqBDMM5VGixJE-gA_xGcSi78kDJSKSqFOSAJ8k98/edit?gid=0#gid=0")
                ws = sh.worksheet("Sheet1")

                row_to_update = int(guest_row_index) + 2
                ws.update_cell(row_to_update, 6, "declined")

                st.session_state.rsvp_status = "declined"
                st.rerun()
            except Exception as e:
                st.error(f"❌ Cloud Write Error: {e}")

    # Evaluate the RSVP choice from state memory
    if st.session_state.rsvp_status == "attending":
        st.balloons()
        st.success("💖 You have successfully RSVP'd!! We will see you on our wedding day!")
    elif st.session_state.rsvp_status == "declined":
        st.info("😢 Thank you for letting us know! If you ever change your mind, just click yes next time :) .")
## end of RSVP

# 7. Action Links & Buttons

st.write("---")

# 8. Turn off / Exit Simulation
if st.button("Turn off the Wedding Machine"):
    st.info(
        "The Wedding Machine is safely running in the cloud. You can simply close this browser tab!"
    )


