import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    score = [0]*N
    for i in range(N):
        # 입력을 공백으로 구분하여 각 값을 리스트로 저장한다.
        # score 리스트 안에 리스트로 저장된다.
        score[i] = list(map(int,sys.stdin.readline().split()))
    # 서류 심사 성적을 기준으로 오름차순 정렬한다.
    score.sort()
    # 면접 심사 순위가 서류 심사 앞 등수의 사람 면접 심사 순위보다 낮다면 탈락이다.
    min = score[0][1]
    # 서류 심사 1등은 무조건 합격이므로 count를 1로 초기화한다.
    count = 1
    for j in range(1,N):
        if score[j][1] < min:
            min = score[j][1]
            count += 1
    print(count)