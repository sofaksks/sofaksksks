from PIL import Image
import requests 
import streamlit as st
from streamlit_lottie import st_lottie 

st.set_page_config(page_title="My Webpage",page_icon=":tada:")

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding="https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
img_contact_form=Image.open("images/capybara.webp")
img_lottie_animation=Image.open("images/capybara.webp")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")



with st.container():
    st.subheader("Hi, I am Sofiya")
    st.title("A student from Kazakhstan")
    st.write("I am in 9th grade, learning IT")
    st.write("[Learn more >](https://youtu.be/zTgQ_VnrP_s?si=K9o5zK4RuP52EDFn)")

with st.container():
    st.write("---")
    st.header("My hobbies")
    left_column, right_column=st.columns(2)
    with left_column:
        st.write("##")
        st.write(
            """
            i love playing tennis, i play for 6 years
            """
        )
        st.write("[Link>](https://youtu.be/pxn0wL_uSm4?si=mBTTpXdfaDMV62r7)")
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("Skills")
    st.write("##")
    image_column, text_column=st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.write(
            """
           I cook very well, especially i love to cook spagetti
            """
        )
with st.container():
    st.write("---")
    st.header("Education")
    st.write("##")
    st.write(
        """
        I study in Tamos education, in IT class
        """
    )
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()