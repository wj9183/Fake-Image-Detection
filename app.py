import streamlit as st
from DeepFakeis import DeepFakeis
from FakeImagesDangerous import FakeImagesDangerous as FID
from Fake_Detection import Fake_Detection
import random

def main():
    menu = ['Deep Fake란', 'Fake Image의 위험성', 'Fake Image 판별']
    choice_sidebar = st.sidebar.selectbox('메뉴를 선택하세요.', menu)

    if choice_sidebar == 'Deep Fake란':
        DeepFakeis()

    elif choice_sidebar == 'Fake Image의 위험성':
        FID()


    elif choice_sidebar == 'Fake Image 판별':
        Fake_Detection()

    else:
        st.error('잘못된 접근입니다.')
        pass
        
        






if __name__ == '__main__':
    main()