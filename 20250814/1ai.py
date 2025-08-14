# import os 
# from langchain_openai import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate
# from langchain.schema import StrOutputParser

# # LM studio API 설정
# # LM studio가 제공하는 로컬 API 엔드포인트 지정
# base_url = "http://192.168.0.46:1234/v1"  #"http://192.168.0.251:1234/v1" <<공용 서버

# # LM studio는 API key가 필수는 아니지만, langchain에서 요구하므로 임의의 값을 넣음
# os.environ["OPENAI_API_KEY"] = "not-needed"

# # ChatOpenAI 객체 초기화
# # openai_api_base를 LM studio의 엔드포인트로 설정
# llm = ChatOpenAI(openai_api_base=base_url, temperature=0.7)

# # LangChain 체인 구축(예시)
# prompt = ChatPromptTemplate.from_template("다음 질문에 대해 1~2 문장으로 답변해줘: {question}") #프롬프트
# output_parser = StrOutputParser()   #결과

# chain = prompt | llm | output_parser

# response = chain.invoke({"question": "인공지능이란 무엇인가요?"})
# print(response)