import re

def solution(new_id:str) -> str:
    new_id = new_id.lower() # 1단계
    new_id = re.sub("[^a-z0-9-_.]","",new_id)   #2단계
    new_id = re.sub("[.{2,}]",".", new_id)

    answer = ''
    return new_id




def main():
    new_id = '"...!@BaT#*..y.abcdefghijklm"'
    answer = solution(new_id)
    print(answer)

if __name__ == '__main__':
    main()