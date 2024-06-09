import streamlit as st
import llm
from file_creator import Create_Doc

model = llm.Model()
invalid_image_text = 'please upload a valid screenshot.'

st.markdown("""
    <style>
    .justified-text {
        text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)


with st.sidebar:
    st.header("ABOUT:")
    
    st.caption("""
        <div class="justified-text">
           Image to Document file Creator is an AI powered app that allows users to effortlessly convert their screenshots into Word documents. Simply upload a screenshot, and the app will generate a Word document based on the image provided, ensuring a seamless and efficient conversion process. Ideal for anyone looking to quickly turn visual content into editable text documents.
        </div>
        """, unsafe_allow_html=True)
    
    for _ in range(17):
        st.write("") 
    st.subheader("Build By:")
    st.write("[Pachaiappan❤️](https://mr-vicky-01.github.io/Portfolio)")
    st.write("contact: [Email](mailto:pachaiappan1102@gamil.com)")

st.title("Image🖼️ - Document📃")
st.text("Upload your screenshot or image to convert it into a Word document.")
uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file)
    
    button = st.button("Generate Document")
    if button:
        with st.spinner("🤖Preparing your Document..."):
            text = model.get_response(uploaded_file)
        st.write(text)
        
        if text.lower().strip() != invalid_image_text:
            doc = Create_Doc()
            doc_buffer = doc.markdown_to_word(text)
            st.download_button(
            label="Download",
            data=doc_buffer,
            file_name="output.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            
