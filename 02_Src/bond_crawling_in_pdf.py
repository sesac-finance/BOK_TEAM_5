import os
from tika import parser

file_list = os.listdir('../채권보고서/')

for i in file_list:
    try:
        data=parser.from_file(f'../채권보고서/{i}')
        content=data["content"].strip()
        name = i[:-4].split('_')
        file_name = f'{name[0]}_{name[1][:2]}-{name[1][3:5]}-{name[1][6:8]}'

        with open(f'../처리후채권보고서/{file_name}.txt','w',encoding='utf-8') as txt:
            print(content,file=txt)
            print(i,file_name,'이(가) 저장되었습니다.')
    
    except Exception as e:
        print('오류 파일 : ','/',i, file_name,e)
        pass