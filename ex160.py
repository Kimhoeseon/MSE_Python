L = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in L:      
    ext = i.split(".")  # 문자열을 split을 이용하여  '.'을 기준으로 나눈다.   
    if (ext[1] == "h") or (ext[1] == "c"):  # intra.h를 예시로 하면 [intra,h]로 나뉘며 [1]로 인해 확장자가 h와c가 맞으면 출력시킨다.
        print(i)
