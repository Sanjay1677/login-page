import streamlit as st
import base64



page_bg_img=f"""
<style>
.st-emotion-cache-bm2z3a{{
    background-image: url("https://codetheweb.blog/assets/img/posts/css-advanced-background-images/cover.jpg")
    background-size:cover;
}}     
</style>
""" 
st.markdown(page_bg_img,unsafe_allow_html=True)


    
    
def main():
    st.title(":red[Login page]") 
    choice = st.selectbox('Login/Signup',['Login','Signup'])
    if choice=='Login':
        
        username=st.text_input('Email Address')
        password=st.text_input('Password',type='password')
        
        col1, col2 = st.columns(2) 

        with col1:
            if st.button("Submit"):
                if username == "user" and password == "password":                     st.success("Logged in successfully!")
                else:
                    st.error("Incorrect username or password")

        with col2:
            if st.button("Cancel"):
                st.warning("Login process cancelled.")
                st.stop()
        
    else:
        
        username=st.text_input('Email Address')
        password=st.text_input('Password',type='password')
        
        username=st.text_input('Enter your unique username')
        
        st.button('Create my account')
    
main()