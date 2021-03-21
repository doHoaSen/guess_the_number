import random

# write the code
correct = random.randint(1, 20)
cnt = 4

while cnt > 0:
    number = int(input('기회가 {cnt}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: '))
    if number == correct:
        print('축하합니다. {5-cnt}번 만에 숫자를 맞히셨습니다.')
        break
    elif number < correct and 1 <= number <= 20:
        print('up')
        cnt -= 1
    elif number > correct and 1 <= number <= 20:
        print('down')
        cnt -= 1
    else:
        print('올바르지 않은 값입니다. 1-20 사이의 정수를 입력하세요.')
    if cnt == 0:
        print('아쉽군요. 정답은 {correct}입니다. 다시 도전하세요.')
