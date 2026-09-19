import streamlit as st

st.set_page_config(page_title="KisanCare AI", page_icon="🌱")
st.title("🌱 KisanCare AI: Farmer Support Portal")

tab1, tab2 = st.tabs(["🍃 Disease Diagnostic", "🌾 Smart Crop Guide"])

with tab1:
    st.header("Upload an infected leaf photo")
    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "png"])
    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)
        # AI model code will go here later

with tab2:
    st.header("Crop Recommendation")
    st.write("Enter soil N-P-K and climate data here.")
    # ML model code will go here later