import streamlit as st
import mysql.connector
from mysql.connector import Error
import random
import pandas as pd
import numpy as np

def FakeImagesDangerous():

    menu = ['','평범한 사진', '조작된 사진']
    correct = 0

    success_script = '''눈썰미가 좋으십니다..
                      하지만 쉽지는 않으셨으리라 생각합니다.
                      이러한 기술들은 나날이 눈에 띄게 발전해가고 있습니다.
                      이러한 기술들이 보이스 피싱 등의 범죄에 이용된다면, 우리는 어떻게 대응해야할까요?'''

    false_script = '''맞춰보신 바와 같이, 이미지와 영상에 관한 기술은 날이 갈수록 발전하고 있습니다.
                      이러한 기술들이 보이스 피싱 등의 범죄에 이용된다면, 우리는 어떻게 대응해야할까요?'''
    
    try:    #데이터베이스 통해서 가져올 거니까.
        connection = mysql.connector.connect( 
                host = 'database-1.czhazxqfdq7r.us-east-2.rds.amazonaws.com',  
                database = 'FakeImageDetection',
                user = 'test_id',
                password = 'test1234' 
            )
        if connection.is_connected() : #연결됐을 때
            cursor = connection.cursor(dictionary= True)

            query = """ select *
                        from FakeImageDetection_test;"""

            cursor.execute(query)
            results = cursor.fetchall()

            st.title('')
            st.write('이 사진은 평범한 사진일까요, 조작된 사진일까요?')

            # image_id_list = list(range(0, 9+1))

            # number = random.sample(image_id_list,1)[0]
            number = 0
            st.image(results[number]['image_url'])
            solution = ''
            default_select = menu.index('')
            if st.button('평범한 사진', key = 'truth'):
                solution = 0
            if st.button('조작된 사진', key = 'false'):
                solution = 1
            if solution is not '':
                st.write('버튼을 누른 후 solution 값은 현재 : {}'.format(solution))
                if solution == results[number]['solution']:
                    st.success('진짜와 가짜 이미지를 분류해내셨습니다.')
                elif solution != results[number]['solution']:

                    st.warning('진짜와 가짜 이미지 분류에 실패하셨습니다.')
                else:
                    pass


    except Error as e :                     
        print('디비 관련 에러 발생', e)
    
    finally :
        cursor.close()
        connection.close()
        print("MySQL 커넥션 종료")

    # book_id = st.number_input('책 아이디를 입력하세요', image_id_list[0], image_id_list[-1] )


    # if st.button('실행') :
    #     try :
    #         connection = mysql.connector.connect(        # 이 함수를 가장 먼저 호출하고, 괄호 안에 정보를 넣어줘야한다 안그럼 개나소나 다 연결하니까.
    #             host = 'database-1.czhazxqfdq7r.us-east-2.rds.amazonaws.com',  
    #             database = 'yhdb',
    #             user = 'test_id',
    #             password = 'test1234' #원래 이런 정보들 여기에 안쓴다.
    #         )
            
    #         if connection.is_connected() :
    #             # 2. 커서를 가져온다.
    #             cursor = connection.cursor()

    #             # 3. 우리가 원하는거 실행 가능.            
    #             query = """delete from books
    #                         where book_id = %s ;"""

    #             data = (book_id,) 
    #             cursor.execute(query, data)

    #             connection.commit()


                
    #             # 4. 실행 후 커서에서 결과를 빼낸다. 
                
    #             results = cursor.fetchall()

    #             for data in results :
    #                 print(data[1] , data[4])
