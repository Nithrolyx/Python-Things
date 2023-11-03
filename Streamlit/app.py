import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Web Test", page_icon=":tada:", layout="wide")

# FOR GETTING
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None #IF NO LOTTIE 
    return r.json()

# USING LOCAL CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ASSETS
lottie_coding = load_lottieurl("https://lottie.host/dfd25b95-d1e0-4a92-98af-1dd498c5b8c0/PuxcGId7KI.json")
img_contact_form = Image.open("images/yes.webp")

# HEADER
with st.container():
    st.subheader("Hi, I am Sean :wave:")
    st.title("A Software Engineer from PH")
    st.write("I yearn for gaming and coding")
    st.write("[Learn More >](https://google.com)")

# WHAT I DO
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            - Sed aliquet dolor et ex scelerisque mattis. 
            - Etiam nec est at lorem egestas tincidunt vitae nec est. 
            - In vulputate placerat nulla, eget ultrices nunc vehicula ac
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            """ 
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

#PROJECTS
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1 , 2))
    with image_column:
        # image here
        st.image(img_contact_form)
    with text_column:
        st.subheader("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        st.write(
            """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=RLZ7peL-j_U)")

# CONTACT FORM
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

# FORM SUBMIT
    contact_form = """
        <form action="https://formsubmit.co/nithrolyxneo@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Name" required>
            <input type="email" name="email" placeholder="Email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()
