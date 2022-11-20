
import os
from tika import parser

# 저장한 file 명 list화
file_list = os.listdir('../의사록/')

# pdf file 불러와서 parsing 후 txt로 변환
for i in file_list:
    data = parser.from_file(f"../의사록/{i}")
    content = data["content"].strip()
    name = i[:-4].split('.')
    file_name=f"{name[0]}-{name[1]}-{name[2]}"

    with open(f"../처리후의사록/{file_name}.txt", 'w', encoding='utf-8') as txt:
        print(content, file=txt)
