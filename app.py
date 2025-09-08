# Importing the required libraries.
import streamlit as st
import pyqrcode
import io
from PIL import Image

# Web page heading
st.set_page_config(page_title = "QR Code Generator", layout = "wide")

# Page title and description
st.markdown("""<h1 style="text-align:center;">⚙️ QR Code Generator</h1>
    <p style="text-align:center; font-size:18px;"> Please enter a <b>Link Name</b> and <b>Link URL</b> below to generate a QR code.</p>
    <p style="text-align:center; font-size:18px;"> You can preview it on screen and download it as a PNG file.</p> """, unsafe_allow_html = True )

# Separating lines
st.write("---")

# Getting the link name
link_name = st.text_input("🔖 Link Name", placeholder = "e.g. MyWebsite")
# Getting the Url ink
link = st.text_input("🌐 Link URL", placeholder = "https://example.com")

# Separating lines
st.write("---")

# Creating an empty pace holder.
qr_placeholder = st.empty()

# Using buttons.
if st.button("🚀 Generate QR Code", use_container_width = True):
    # Asking the correct name and link.
    if link_name.strip() == "" or link.strip() == "":
        # Warning message.
        st.warning("⚠️ Please enter both a Link Name and a Link URL.")
    # If link name does not start with https then displaying warning message.
    elif not link.startswith("https://"):
        st.error("❌ Please enter a valid URL starting with https://")
    # If all correct then generating the QR Code.
    else:
        # Generating QR Code
        url = pyqrcode.create(link)
        buffer = io.BytesIO()
        url.png(buffer, scale=8)
        buffer.seek(0)

        # Opening the images.
        img = Image.open(buffer)

        # Displaying the success Message.
        st.success("✅ QR Code generated successfully !!")

        # Displaying QR Code
        st.image(img, caption = f"{link_name or 'QRCode'}.png", use_container_width = False)

        # Download QR Code
        st.download_button(
            label = "⬇️ Download QR Code",
            data = buffer,
            file_name = f"{link_name or 'QRCode'}.png",
            mime = "image/png",
            use_container_width = True
        )
