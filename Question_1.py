import re

def solution(new_id:str) -> str:
    new_id = new_id.lower() # 1단계
    new_id = re.sub("[^a-z0-9-_.]","",new_id)   #2단계
    new_id = re.sub("\.{2,}", ".", new_id)  # 3단계
    new_id = re.sub("^\.|\.$", "", new_id)  # 4단계
    if len(new_id) == 0:
        new_id = new_id.join('a')
    # new_id = re.sub("","a", new_id)   # 5단계
    if len(new_id) > 15:
        new_id = new_id[:15]
        new_id = re.sub("\.$", "", new_id)
    elif len(new_id) <= 2:
        while True:
            new_id = new_id + new_id[-1]
            if len(new_id) > 2:
                break
    
    answer = new_id
    return new_id




def main():
    new_id = "z-+.^."
    answer = solution(new_id)
    print(answer)

if __name__ == '__main__':
    main()