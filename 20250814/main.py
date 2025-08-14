# # unstructured는 비정형 문서에서 텍스트와 구조화된 데이터를 추출를 위한 라이브러리
# from unstructured.partition.pdf import partition_pdf

# file_name = "SPRi_AI_Brief_8월호_산업동향_F.pdf"

# # PDF 파일에서 요소들을 추출하는 함수 정의
# def extract_pdf_elements(filepath):
#   return partition_pdf(                 # PDF 파일을 분석하여 구조화된 요소들(텍스트,제목 등)을 추출 함수
#     filename=filepath,                  # 분석할 PDF 파일의 경로
#     languages=["kor"],                  # 분석할 PDF의 언어 설정(한국어)
#     extract_images_in_pdf=False,   			# PDF 내 이미지 추출 여부
#     infer_table_structure=False,   			# 표의 구조를 추론 여부
#     chunking_strategy="by_title",   		# 텍스트를 제목 기준으로 나누는 전략 사용
#     max_characters=4000,   							# 각 테스트 청크의 최대 문자 수
#     new_after_n_chars=3000,   					# 하나의 청크가 이 문자 수를 초과하면 새 청크로 분할
#     combine_text_under_n_chars=2000,  	# 이 문자수보다 짧은 청크는 앞뒤 텍스트와 병합
#   )

# # 함수 호출: 특정PDF 파일에서 요소들을 추출
# elements = extract_pdf_elements(file_name)

# # 청크(chunk) 길이 확인
# print(f'chunk : {len(elements)}')

# # 첫번째 내용 출력
# print(f'1 : {elements[0]}')