import numpy as np
import pandas as pd

save_path = '/content/drive/MyDrive/SSUDA'
data_path = '/content/drive/MyDrive/SSUDA/SSUDA 2022-1 활동 지원 신청서(응답).csv'

df = pd.read_csv(data_path)

df.columns

인원수 = len(df)

공통_질문 = ['SSUDA의 2022-1 신규 멤버인가요?',
            '이름',
            '학번(ex : 2022xxxx -> 22)',
            '학년(2022-1 기준)',
            ]
신규_질문 = ['참여 하고싶은  스터디의 주제를 선택해주세요.(1순위)',
            '참여 하고싶은  스터디의 주제를 선택해주세요.(2순위)',
            '선택한 주제(1순위)를 기준으로 해당되는 경험에 모두 체크해주세요.',
            '원하는 진행방식에 모두 체크해주세요.',
            '함께 하고싶은 <기획 프로그램>에 체크해주세요.',
            ]
기존_질문 = ['참여 하고싶은  스터디의 주제를 선택해주세요.',
            '스터디 주제에 대한 본인의 주관적인 수준을 점수로 나타내어주세요.(스터디에 참여하는 분은 필수적으로 답해주세요.)',
            '원하는 진행방식에 모두 체크해주세요.(스터디에 참여하는 분은 필수적으로 답해주세요.)',
            '함께 하고싶은 <기획 프로그램>에 체크해주세요.',
            ]

def 지원서_함수(프로그램='코딩테스트'):
    """
    input : 프로그램 : str
            프로그램 명칭을 str형식으로 입력하십시오

    output : 지원서 : pandas.DataFrame
            해당 프로그램 지원자들의 공통, 신규, 기존 질문에 대한 답변이 포함된
            pandas.DataFrame 객체입니다.
    """
    지원자_리스트 = []
    지원서 = []

    for i in range(인원수):
        지원자 = df.iloc[i]

        if 프로그램 in 지원자['함께 하고싶은 <기획 프로그램>에 체크해주세요.']:
            지원자_리스트.append(지원자.이름)


    for i in range(인원수):
        지원자 = df.iloc[i]
        
        if 지원자.이름 in 지원자_리스트:
            지원자_지원서 = 지원자.loc[공통_질문 + 신규_질문 + 기존_질문]
            지원서.append(지원자_지원서)

    지원서 = pd.concat(지원서,axis=1)
    return 지원서

지원서_함수('코딩테스트').to_csv(f'{save_path}/코딩테스트_지원서.csv', index=True, encoding='CP949')
지원서_함수('SQL').to_csv(f'{save_path}/SQL_지원서.csv', index=True, encoding='CP949')
지원서_함수('하늘코끼리').to_csv(f'{save_path}/하늘코끼리_지원서.csv', index=True, encoding='CP949')
지원서_함수('데이콘').to_csv(f'{save_path}/데이콘Basics_지원서.csv', index=True, encoding='CP949')