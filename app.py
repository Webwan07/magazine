import streamlit as st
import time
from datetime import datetime
st.set_page_config("Group 5 T3 MAGAZINE",layout='centered',initial_sidebar_state='auto')

with st.spinner(" "):
    time.sleep(2)
    st.balloons()
    
members = [["Cyrus Regala",
           "Josuan Leonardo S. Hulom",
           "Keith Zacharrie Espenosa",
           "Alexis Sevilleno",
           "Jessriel Metante",
           "Leyan Placer",
           "Lynjon Verdida"],
           ["Emarie Tulod",
           "Hannah Jean Turing"]]

subject = "Mga Anyo ng Kontemporaryong Panitikang Pilipino"
college = "Cebu Roosevelt Memorial College"
group = "Group 5"
option = ["Group members","Subject","Instructor"]

def main():
    try:
        with st.sidebar:
            st.text(f"Submitted by: BSIT 1-A {group}")
            st.text(f"Submitted to: Bb. Maria Claudine Inot")
            st.text(f"Subject: {subject}")
            st.text(f"Date: {datetime.now():%m/%d/%y}")
            st.write(college)

        st.title(f"{group} T3 Magazine")
        st.subheader("Best Tech Gadget")
        st.image("IMG_9218.JPG",output_format='auto',use_column_width='auto')
        st.subheader("Group members")
        col1,col2 = st.columns(2)
        with col1:
            st.experimental_data_editor({"Male members":members[0]})
        with col2:
            st.experimental_data_editor({"Female members":members[1]})
        st.markdown("""<style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """,unsafe_allow_html=True)
    except TypeError as e:
        print(e)
if __name__ == '__main__':
    main()


