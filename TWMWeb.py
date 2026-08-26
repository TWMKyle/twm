import ssl
import gspread
import base64
import os
import random
from PIL import Image
import streamlit as st

# Make sure variables img_src1 and img_srcp are defined before running this snippet

import streamlit as st

# Make sure variables img_src1 and img_srcp are defined before running this snippet

st.markdown(
    f"""
    <style>
    /* 1. IMPORT ELEGANT WEDDING FONTS FROM GOOGLE FONTS */
    @import url('https://googleapis.com');

    /* This selector targets the entire background canvas of Streamlit */
    [data-testid="stAppViewContainer"] {{
        background-image: url('{img_src1}') !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }}

    /* 2. MAIN TITLES & HEADERS (SHRUNK PINYON SCRIPT) */
    h1, .stApp h2 {{
        color: #D4AF37 !important; /* Elegant Gold instead of plain white */
        font-family: 'Cormorant Garamond', cursive !important; 
        font-size: 3.2rem !important; /* SHRUNK: Delicate calligraphic layout */
        font-weight: normal !important;
        line-height: 1.1 !important;
    }}

    /* Make sure the material ring icon scales down with the title text */
    h1 span[data-testid="stMarkdownMaterialIcon"] {{
        color: #D4AF37 !important;
        -webkit-text-fill-color: #D4AF37 !important;
        font-size: 2.2rem !important; /* SHRUNK */
        vertical-align: middle !important;
    }}

    /* 3. MAIN PANEL BODY TEXT & DESCRIPTIONS (STRICTLY FOR CONTENT CONTAINER ONLY) */
    .stMain p,
    .stMain [data-testid="stMarkdownContainer"] p,
    .stAppViewBlockContainer p {{
        color: #FFFFFF !important; /* Forces normal st.write text to be White on background */
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 0.95rem !important;
        letter-spacing: 0.02rem !important;
    }}

    /* 4. SIDEBAR SPECIFIC TEXT: REMAIN SOLID CHARCOAL BLACK */
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {{
        color: #333333 !important; /* Keeps sidebar fonts dark */
        -webkit-text-fill-color: #333333 !important;
        font-family: 'Cormorant Garamond', serif !important;
    }}

    /* 5. CUSTOM PORTRAIT SCROLLABLE STACK (REFINED FOR ELEGANCE) */
    .photo-scroll-container {{
        max-height: 400px !important;          
        overflow-y: scroll !important;         
        overflow-x: hidden !important;         
        border-radius: 16px !important;
        padding: 0.8rem !important;
        background-color: #FCFBF7 !important;  /* Soft Warm White Canvas backdrop */
        border: 1px solid rgba(212, 175, 55, 0.3) !important; /* Ultra-fine gold accent border */
        margin-bottom: 1.5rem !important;
        box-shadow: inset 0px 2px 8px rgba(0, 0, 0, 0.02) !important;
    }}

    /* Style the portrait images inside the stack with smooth transitional physics */
    .portrait-stack-img {{
        width: 100% !important;
        height: auto !important;
        aspect-ratio: 2 / 3 !important;        
        object-fit: cover !important;          
        border-radius: 8px !important;
        margin-bottom: 1rem !important;     
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.04) !important;
        display: block !important;
        transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease !important;
    }}

    /* Delicate lift animation on picture hover */
    .portrait-stack-img:hover {{
        transform: scale(1.02) translateY(-2px) !important;
        box-shadow: 0px 8px 20px rgba(212, 175, 55, 0.15) !important;
    }}

    [data-testid="stSidebar"] {{
        background-image: url('{img_srcp}') !important;
        background-size: contain !important;     
        background-position: top center !important; 
        background-repeat: no-repeat !important;  
        background-attachment: scroll !important; 
        background-color: #FDF6E2 !important;     
    }}

    /* OVERLAY: Makes text highly readable over a busy image background */
    [data-testid="stSidebarUserContent"] {{
        background-color: rgba(255, 255, 255, 0.8) !important; 
        padding: 1.5rem 1.2rem !important; /* DECREASED: Tighter side layout padding */
        border-radius: 12px !important;
        margin: 0.75rem !important;
    }}

    /* Elegant custom scrollbar tailoring for modern web browsers */
    .photo-scroll-container::-webkit-scrollbar {{
        width: 4px !important; /* Sleeker scrollbar track line */
    }}
    .photo-scroll-container::-webkit-scrollbar-track {{
        background: transparent !important;
    }}
    .photo-scroll-container::-webkit-scrollbar-thumb {{
        background: rgba(212, 175, 55, 0.4) !important; /* Subtler gold slider accent */        
        border-radius: 10px !important;
    }}
    
    /* UNIVERSAL BUTTON BASE STRUCTURE STYLING */
    div[data-testid="stBaseButton-primary"] button,
    div[data-testid="stBaseButton-secondary"] button,
    [data-testid="stAppViewBlockContainer"] button,
    button:not([data-testid="baseButton-header"]) {{
        background-color: #4A5D4E !important;    
        border: 2px solid #D4AF37 !important;    
        border-radius: 8px !important;           
        font-family: 'Cormorant Garamond', serif !important; 
        padding: 0.35rem 1rem !important;        
        transition: all 0.3s ease !important;    
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1) !important;
    }}

    /* FORCE TEXT CODES INSIDE INTERACTIVE APP BUTTONS TO BE UPPERCASE WHITE */
    div[data-testid="stBaseButton-primary"] button p,
    div[data-testid="stBaseButton-secondary"] button p,
    .stApp div[data-testid="stBaseButton-primary"] button p,
    .stApp div[data-testid="stBaseButton-secondary"] button p,
    .stMain button p,
    .stMain button div,
    .stMain button span,
    .stMain button [data-testid="stMarkdownContainer"] {{
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important; 
        font-size: 0.75rem !important;           
        font-weight: 600 !important;
        letter-spacing: 0.08rem !important;      
        text-transform: uppercase !important;    
    }}

    /* EXPLICITLY PROTECTION FOR THE SIDEBAR COLLAPSE ICON SYSTEM */
    [data-testid="baseButton-header"],
    [data-testid="baseButton-header"] *,
    [data-testid="collapsedControl"],
    [data-testid="collapsedControl"] * {{
        text-transform: none !important; 
        letter-spacing: normal !important;
        color: #333333 !important;
    }}

    /* Interactive Hover State */
    div[data-testid="stBaseButton-primary"] button:hover,
    div[data-testid="stBaseButton-secondary"] button:hover,
    button:not([data-testid="baseButton-header"]):hover {{
        background-color: #3B4B3E !important;    
        border-color: #F3E5AB !important;        
        box-shadow: 0px 6px 15px rgba(214, 175, 55, 0.4) !important; 
        transform: translateY(-1px) !important;              
        cursor: pointer !important;
    }}
    
    /* Ensure smaller text stays white on hover */
    button:hover [data-testid="stMarkdownContainer"],
    button:hover p {{
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }}

    .header-silhouette-box {{
        background-color: rgba(255, 255, 255, 0) !important; 
        backdrop-filter: blur(12px) !important;                  
        -webkit-backdrop-filter: blur(12px) !important;          
        border-radius: 16px !important;                          
        padding: 2rem 2.5rem !important;                        
        border: 1px solid rgba(255, 255, 255, 0.4) !important; 
        box-shadow: 0px 8px 32px rgba(0, 0, 0, 0.08) !important;  
        margin-bottom: 2.5rem !important;                          
        text-align: center !important;                           
        width: 100% !important;
        box-sizing: border-box !important;
    }}

    /* Target the Title directly inside the custom HTML layout block */
    .header-silhouette-box h1 {{
        color: #D4AF37 !important;
        font-family: 'Pinyon Script', cursive !important;
        font-size: 3.4rem !important;
        margin-top: 0px !important;
        margin-bottom: 0.5rem !important;
        font-weight: normal !important;
    }}

    /* Target the Paragraph Description text directly inside the custom HTML layout block */
    .header-silhouette-box p {{
        color: #2C3E50 !important; 
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        margin: 0px !important;
    }}

    /* 6. FORCE STREAMLIT ALERTS/SUCCESS BOX TEXT TO WHITE ONLY */
    [data-testid="stNotification"] p, 
    [data-testid="stAlert"] p,
    [data-testid="stNotification"] span,
    [data-testid="stAlert"] span,
    div[data-testid="stAlertContainer"] p {{
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection, gsheets_connection


wedding_photos = [

    "https://raw.githubusercontent.com/TWMKyle/twm/main/bikephoto.jpg",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/671741678_818147120879329_7560801041831527780_n.jpg",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/IMG_8287 2.JPG",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/IMG_82882.JPG",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/IMG_3815.jpg",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/Unknown-7.jpg",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/Unknown-8.jpg",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/Unknown-9.jpg",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/Unknown-10.jpg",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/Unknown-11.jpg",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/Unknown-12.jpg",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/Unknown-13.jpg",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/Unknown-14.jpg",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/Unknown-15.jpg",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/Unknown-16.jpg",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/Unknown-17.jpg",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/Unknown-18.jpg",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/Unknown-19.jpg",
    "https://raw.githubusercontent.com/TWMKyle/twm/main/Unknown-20.jpg",


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

st.markdown(
    f"""
    <style>
    /* 1. IMPORT ELEGANT WEDDING FONTS FROM GOOGLE FONTS */
    @import url('https://googleapis.com');

    /* This selector targets the entire background canvas of Streamlit */
    [data-testid="stAppViewContainer"] {{
        background-image: url('{img_src1}') !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }}

    /* 2. MAIN TITLES & HEADERS (SHRUNK PINYON SCRIPT) */
    h1, .stApp h2 {{
        color: #D4AF37 !important; /* Elegant Gold instead of plain white */
        font-family: 'Cormorant Garamond', cursive !important; 
        font-size: 3.2rem !important; /* SHRUNK: Delicate calligraphic layout */
        font-weight: normal !important;
        line-height: 1.1 !important;
    }}

    /* Make sure the material ring icon scales down with the title text */
    h1 span[data-testid="stMarkdownMaterialIcon"] {{
        color: #D4AF37 !important;
        -webkit-text-fill-color: #D4AF37 !important;
        font-size: 2.2rem !important; /* SHRUNK */
        vertical-align: middle !important;
    }}

    /* 3. MAIN PANEL BODY TEXT & DESCRIPTIONS (STRICTLY FOR CONTENT CONTAINER ONLY) */
    .stMain p,
    .stMain [data-testid="stMarkdownContainer"] p,
    .stAppViewBlockContainer p {{
        color: #FFFFFF !important; /* Forces normal st.write text to be White on background */
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 0.95rem !important;
        letter-spacing: 0.02rem !important;
    }}

    /* 4. SIDEBAR SPECIFIC TEXT: REMAIN SOLID CHARCOAL BLACK */
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {{
        color: #333333 !important; /* Keeps sidebar fonts dark */
        -webkit-text-fill-color: #333333 !important;
        font-family: 'Cormorant Garamond', serif !important;
    }}

    /* 5. CUSTOM PORTRAIT SCROLLABLE STACK (REFINED FOR ELEGANCE) */
    .photo-scroll-container {{
        max-height: 400px !important;          
        overflow-y: scroll !important;         
        overflow-x: hidden !important;         
        border-radius: 16px !important;
        padding: 0.8rem !important;
        background-color: #FCFBF7 !important;  /* Soft Warm White Canvas backdrop */
        border: 1px solid rgba(212, 175, 55, 0.3) !important; /* Ultra-fine gold accent border */
        margin-bottom: 1.5rem !important;
        box-shadow: inset 0px 2px 8px rgba(0, 0, 0, 0.02) !important;
    }}

    /* Style the portrait images inside the stack with smooth transitional physics */
    .portrait-stack-img {{
        width: 100% !important;
        height: auto !important;
        aspect-ratio: 2 / 3 !important;        
        object-fit: cover !important;          
        border-radius: 8px !important;
        margin-bottom: 1rem !important;     
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.04) !important;
        display: block !important;
        transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease !important;
    }}

    /* Delicate lift animation on picture hover */
    .portrait-stack-img:hover {{
        transform: scale(1.02) translateY(-2px) !important;
        box-shadow: 0px 8px 20px rgba(212, 175, 55, 0.15) !important;
    }}

    [data-testid="stSidebar"] {{
        background-image: url('{img_srcp}') !important;
        background-size: contain !important;     
        background-position: top center !important; 
        background-repeat: no-repeat !important;  
        background-attachment: scroll !important; 
        background-color: #FDF6E2 !important;     
    }}

    /* OVERLAY: Makes text highly readable over a busy image background */
    [data-testid="stSidebarUserContent"] {{
        background-color: rgba(255, 255, 255, 0.8) !important; 
        padding: 1.5rem 1.2rem !important; /* DECREASED: Tighter side layout padding */
        border-radius: 12px !important;
        margin: 0.75rem !important;
    }}

    /* Elegant custom scrollbar tailoring for modern web browsers */
    .photo-scroll-container::-webkit-scrollbar {{
        width: 4px !important; /* Sleeker scrollbar track line */
    }}
    .photo-scroll-container::-webkit-scrollbar-track {{
        background: transparent !important;
    }}
    .photo-scroll-container::-webkit-scrollbar-thumb {{
        background: rgba(212, 175, 55, 0.4) !important; /* Subtler gold slider accent */        
        border-radius: 10px !important;
    }}
    
    div[data-testid="stBaseButton-primary"] button,
    div[data-testid="stBaseButton-secondary"] button,
    [data-testid="stAppViewBlockContainer"] button,
    button {{
        background-color: #4A5D4E !important;    
        border: 2px solid #D4AF37 !important;    
        border-radius: 8px !important;           
        font-family: 'Cormorant Garamond', serif !important; 
        padding: 0.35rem 1rem !important;        /* Tighter button body bounds */
        transition: all 0.3s ease !important;    
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1) !important;
    }}

    /* FORCE ALL NESTED TEXT CHANNELS INSIDE BUTTONS TO BE WHITE AND SMALLER */
    div[data-testid="stBaseButton-primary"] button p,
    div[data-testid="stBaseButton-secondary"] button p,
    button p,
    button div,
    button span,
    button [data-testid="stMarkdownContainer"],
    .stApp div[data-testid="stBaseButton-primary"] button p,
    .stApp div[data-testid="stBaseButton-secondary"] button p,
    .stApp button p,
    .stApp button div,
    .stApp button span,
    .stApp button [data-testid="stMarkdownContainer"] {{
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important; 
        font-size: 0.75rem !important;           /* REDUCED: Shrunk from 0.9rem to 0.75rem */
        font-weight: 600 !important;
        letter-spacing: 0.08rem !important;      /* Elegant letter spacing for smaller font sizes */
        text-transform: uppercase !important;    
    }}

    /* Interactive Hover State */
    div[data-testid="stBaseButton-primary"] button:hover,
    div[data-testid="stBaseButton-secondary"] button:hover,
    button:hover {{
        background-color: #3B4B3E !important;    
        border-color: #F3E5AB !important;        
        box-shadow: 0px 6px 15px rgba(214, 175, 55, 0.4) !important; 
        transform: translateY(-1px) !important;              
        cursor: pointer !important;
    }}
    
    /* Ensure smaller text stays white on hover */
    button:hover [data-testid="stMarkdownContainer"],
    button:hover p {{
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }}

    .header-silhouette-box {{
        background-color: rgba(255, 255, 255, 0) !important; /* Premium semi-transparent white backdrop */
        backdrop-filter: blur(12px) !important;                  
        -webkit-backdrop-filter: blur(12px) !important;          
        border-radius: 16px !important;                          
        padding: 2rem 2.5rem !important;                        
        border: 1px solid rgba(255, 255, 255, 0.4) !important; 
        box-shadow: 0px 8px 32px rgba(0, 0, 0, 0.08) !important;  
        margin-bottom: 2.5rem !important;                          
        text-align: center !important;                           
        width: 100% !important;
        box-sizing: border-box !important;
    }}

    /* Target the Title directly inside the custom HTML layout block */
    .header-silhouette-box h1 {{
        color: #D4AF37 !important;
        font-family: 'Pinyon Script', cursive !important;
        font-size: 3.4rem !important;
        margin-top: 0px !important;
        margin-bottom: 0.5rem !important;
        font-weight: normal !important;
    }}

    /* Target the Paragraph Description text directly inside the custom HTML layout block */
    .header-silhouette-box p {{
        color: #2C3E50 !important; /* Crisp high-contrast charcoal reading text */
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        margin: 0px !important;
    }}

    /* 6. FORCE STREAMLIT ALERTS/SUCCESS BOX TEXT TO WHITE ONLY */
    [data-testid="stNotification"] p, 
    [data-testid="stAlert"] p,
    [data-testid="stNotification"] span,
    [data-testid="stAlert"] span,
    div[data-testid="stAlertContainer"] p {{
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
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

st.markdown(
    """
    <div class="header-silhouette-box">
        <h2><span style="font-family: Arial, sans-serif; font-size: 2.2rem; vertical-align: middle; margin-right: 10px;">💍</span>Welcome to Kyle & Cialene's Wedding Page!</h2>
        
    </div>
    """,
    unsafe_allow_html=True
)


# Input Section
search_term = st.text_input("Please enter your name:", placeholder="e.g., Pat, Kyle").strip()
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


