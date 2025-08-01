# import pandas as pd
# import matplotlib.pyplot as plt

# #한글 해결
# plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] = False

# # #데이터 생성
# # arr = [
# #     [1,2,3,4,5],
# #     [2,4,1,3,5]
# # ]
# # data = pd.DataFrame(arr)

# #데이터 만들기
# data = pd.read_csv('./data1_20220731.csv', index_col=0)

# # 선 차트
# # data.plot()
# #막대 차트
# # data.plot(kind='bar')
# #히스토그램
# # data.plot(kind='hist', y='세대수')
# # 산점도
# # data.plot(kind='scatter', x='남', y='여')
# #원형 그래프
# data.plot(kind='pie', y='세대수',autopct='%1.1f%%')
# plt.show()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# import streamlit as st

# #h1 태그
# st.title("Factos :eyes::+1:")

# #h2 태그
# st.header("headerdes..")

# #h3 태그
# st.subheader("small header des...")

# #p 태그
# st.caption("caption des....")

# #code 태그
# st.code("st.code("",language="")", language="python")

# cd = """
# def 함수():
#     pass
# """

# st.code(cd, language="python")

# #div 태그
# st.text("itpangul des.....")

# #p 태그에서 강조를 위해 strong 적용
# st.markdown("py is mechkucha **HARD**")

# #수식 표현 방법
# st.markdown(":green[$\sqrt{x^2+y^2}=1$]")
# st.latex(r"\sqrt{x^2+y^2}=1")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# st.title("데이터")

# plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] = False

# arr = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# data = pd.DataFrame(arr)

# data = pd.read_csv("./data1_20220731.csv", index_col=0)

# st.dataframe(data)
# st.table(data)

# data.plot(kind='pie', y='세대수',autopct='%1.1f%%')

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# st.title("데이터 시각화")

# plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] = False

# data = pd.read_csv("./data1_20220731.csv", index_col=0)

# # st.dataframe(data)
# # st.table(data)


# #파이 차트를 그리기위한 figure,axis 객체 생성
# fig, ax = plt.subplots()

# #'세대수' 열을 기준으로 파이차트 그리기
# # - labels: 인덱스를 라벨로 사용(data.index)
# # - autopct: 퍼센트 표시 방식 ('%1.1f%%')
# ax.pie(data['세대수'], labels=data.index, autopct='%1.1f%%')

# #원형 차트가 찌그러지지 않도록 축 비율을 동일하게 설정 옵션
# ax.axis('equal')

# #완성된 차트 출력
# st.pyplot(fig)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] = False

# #선택년도 기본값 
# if 'slider_value' not in st.session_state:
# 	st.session_state.silder_value = (2019,2023)
# #차트 기본값
# if 'chart_value' not in st.session_state:
# 	st.session_state.chart_value = pd.DataFrame([])

# # 데이터 1차 전처리
# url = "https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=277002&idx_cd=2770&freq=Y&period=N"
# data = pd.read_html(url)
# df = data[0].drop(0)
# df = df.drop("Unnamed: 1", axis=1)
# # print(df)
# data1 = df.iloc[::2, :].set_index(keys="Unnamed: 0")
# # print(data1)
# # data2 = data1.filter(items=["2023"]).transpose()
# # st.dataframe(data1)
# # st.dataframe(data2)


# def makeData():
# 	# st.dataframe(data1)
# 	#선택한 데이터 전처리
# 	st.text(f"선택한 년도 {st.session_state.slider_value}")
# 	ty = st.session_state.silder_value
# 	arr = []
# 	for y in range(ty[0], ty[1]  +1):
# 		arr.append(str(y))
# 	st.session_state.chart_value = data1.filter(items=arr).transpose()
# 	st.dataframe(st.session_state.chart_value)
# 	# st.dataframe(st.session_state.silder_value)
# 	st.bar_chart(st.session_state.chart_value)


# #선택하는 슬라이더 추가
# sd = st.slider(label="년도 범위를 변경하세요.", min_value=1989, max_value=2023, value=st.session_state.silder_value, step=1)
# if st.button("선택한 범위 확인"):
# 	st.session_state.silder_value = sd
# 	# st.text(f"변경한 년도 {st.session_state.silder_value}")
# 	makeData()


# st.bar_chart(data2)
# st.line_chart(data2)
# fig, ax = plt.subplots()
# ax.pie(data2.squeeze, labels=data.index, autopct='%1.1f%%', stratangle=90)
# ax.axis('equal')
# st.pyplot(fig)



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

#버튼 이벤트
btn = st.button("버튼")
if btn:
    st.write(":blue[버튼] 으악!!!!!")

#데이터
df = pd.DataFrame({
    "첫번째": [1,2,3,4],
    "두번째": [10,20,30,40]
})

#파일 다운로드 버튼 이벤트
st.download_button(
    label="csv 다운로드",
    data=df.to_csv(),
    file_name="샘플.csv",
    mime="text/csv"
)

#submit(요청) 버튼 이벤트
with st.form(key ='me'):
  id = st.text_input("아이디를 입력하세요")
  sbtn = st.form_submit_button("호출")

if sbtn:
  st.success(f"확인 : {id}")
  
#선택 이벤트
r = st.radio(
   label="식사는 하셨어?",
   options=("ㅇ", "ㄴ", "ㅁㄹ"),
   index=1
)
if r == "ㅇ":
   st.text("그럼 죽어!!")
elif r == "ㄴ":
   st.text("그럼죽어")
elif r == "ㅁㄹ":
   st.text("그럼 죽어.")

select = st.selectbox(
   label="죽 어",
   options=("싫", "은", "데"),
   index=2
)
if select == "싫":
   st.text("참수형")
elif select == "은":
   st.text("살았다.")
elif select == "데":
   st.text("교수형")

multi = st.multiselect(
   "좋아하는게뭔데",
   ["#집", "#수면", "#죽음"],
   ["#집"]
)
st.write(f"당신의 선택은: :green[{multi}] 이제 죽어")

#선택이벤4
점심 = st.slider(
    "점심 시간은 언제 좋을까요?",
    min_value=dt(2024, 12, 5, 13, 20),
    max_value=dt(2024, 12, 5, 14, 30),
    value=dt(2024, 12, 5, 13, 30),
    step=datetime.timedelta(minutes=10),
    format="MM/DD/YY HH:mm"
)
st.write("선택한 시간:", 점심)






















































































