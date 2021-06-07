# 프로그래머스 `완주하지 못한 선수`

def solution(participant, completion):
    i = ''
    answer = ''
    malatoner = participant
    
    for i in completion:
        if i in malatoner:
            malatoner.remove(i)
    

    if participant.count(i) != 1:
        answer = f"{malatoner}는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다."
    else:
        answer = f"{malatoner}는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다."
    
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

A = solution(participant, completion)
print(A)
