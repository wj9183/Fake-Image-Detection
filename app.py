import streamlit as st

def main():
    menu = ['Fake Image란', 'Fake Image Detection']
    choice_sidebar = st.sidebar.selectbox('고르세요', menu)




if __name__ == '__main__':
    main()