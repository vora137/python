def printList(dic) :
    for key in dic.keys():
        print('{:15} : {}'.format(key,dic[key]))
        
# 파일 > 딕셔너리
# 파일에 읽어오기
file = 'd:\javaedu10\project\python\dictionary.txt'
f = open(file,'r',encoding='UTF8') # r는 읽기모드
dic = {}
if f.readable() :
    for item in f.readlines() :
        list = item.split(':')
        dic[list[0].strip()] = list[1][:-1] # 문자열 슬라이싱
    f.close()
print(dic)

print('>> 영어 단어장 <<')
stop = False 
while not stop : 
    print('메뉴 >> 1.저장 2.검색 3.수정 4.삭제 5.목록 6.통계 7.종료')
    choice = int(input('선택 >> '))

    if choice == 1 : #저장
        print('저장')
        if len(dic.keys()) < 5 :
          word = input('등록할 단어를 입력하세요 >> ')
          meaning = input('뜻을 입력하세요 >> ')
          if word in dic :
              print('이미 등록된 단어입니다')
              dic[word] = meaning
          else : 
              dic[word] = meaning            
        else : 
            print('최대 5개단어만 저장할 수 있습니다')
          
    elif choice == 2 : #검색
        word = input('검색할 단어를 입력하세요 >> ')
        found = False
        for key, value in dic.items():
          if word.lower() in key.lower():
            print('{:15} : {}'.format(key, value))
            found = True
        if not found :
            print('단어를 검색할 수 없습니다')
        pass
    
    elif choice == 3 : #수정
        word = input('수정할 단어를 입력하세요 >> ')
        if word.lower() in dic :
            new_meaning = input('변경할 뜻을 입력하세요 >> ')
            dic[word.lower()] = new_meaning
            print('{}의 뜻이 수정되었습니다'.format(word))
        else :
            for key in dic.keys():
                if word.lower() in key.lower() :
                    new_meaning = input('변경할 뜻을 입력하세요 >> ')
                    dic[key] = new_meaning
                    print('{}의 뜻이 수정되었습니다'.format(key))
                    break
            else : 
                print('단어를 검색할 수 없습니다')
        pass
    
    elif choice == 4 : #삭제
        word = input('삭제할 단어를 입력하세요 >> ')
        if word.lower() in dic :
            del dic[word.lower()]
            print('{} 단어를 삭제하였습니다'.format(word))
        else : 
            print('단어를 검색할 수 없습니다')
        pass
    
    elif choice == 5 : #목록
        word = input('1.오름차순 2.내림차순 >> ')
        if word == '1' :
          print('오름차순 목록')
          sorted_dic = sorted(dic.items(), key=lambda x: x[1])
          for entry in sorted_dic :
              print('{:15}:{}'.format(entry[0],entry[1]))
              
        elif word == '2' :
          print('내림차순 목록')
          sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
          for entry in sorted_dic :
              print('{:15}:{}'.format(entry[0],entry[1]))

        else :
          print('오름차순 or 내림차순중에 선택해주세요')
        
        pass
    
    elif choice == 6 : #통계
        print('1. 저장된 단어 갯수 : ',len(dic),' 개')
        keys = dic.keys()
        rev_key = sorted(keys,key=len,reverse=True)
        print('2. 단어의 문자수가 가장 많은 단어 : {}'.format(rev_key[0]))
        print('3. 단어 글자수 내림차순 출력')
        for ele in rev_key :
            print(ele)

        pass
    
    elif choice == 7 : #종료
        stop = True
        # 파일에 저장하기
        f = open('d:\javaedu10\project\python\dictionary.txt','w',encoding='UTF8')
        if f.writable() :
          for item in dic :
              f.write('{}:{}\n'.format(item, dic[item]))
          f.close()

    else : 
        print('선택한 메뉴가 없음')