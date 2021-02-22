import requests
from bs4 import BeautifulSoup


# print(today - last_day)
def crawler(n):
    ## HTTP GET Request
    lotto_url = 'https://dhlottery.co.kr/gameResult.do?method=win720&Round=' + str(n)
    req = requests.get(lotto_url)

    ## BeautifulSoup으로 html소스를 python객체로 변환하기
    res = BeautifulSoup(req.text, 'html.parser')

    data = {}
    ## 필요한 정보만 빼오기
    ### 회차 no / 당첨번호 jo조 numbers /
    no = res.select(
        '#after720 > h4 > strong'
    )[0].text[:-1]
    data['no'] = int(no)

    date = res.select(
        '#after720 > p'
    )[0].text
    data['date'] = date[1:5] + '-' + date[7:9] + '-' + date[11:13]

    jo = res.select(
        '#after720 > div:nth-child(3) > div > div > span'
    )[0].text
    data['jo'] = int(jo)

    nums = res.select(
        '#after720 > div:nth-child(3) > div > span > span'
    )

    for i in range(6):
        data['num' + str(i+1)] = int(nums[i].text)

    bonus = res.select(
        '#after720 > div:nth-child(4) > div > span > span'
    )

    for i in range(6):
        data['bonus' + str(i+1)] = int(bonus[i].text)

    print(data)

    return data

def basic_data():

    # navertv.csv파일을 쓰기모드(w)로 열어줍니다.
    f = open("lotto.csv", "w")
    # 헤더 추가하기
    f.write("회차, 조, 번호1, 번호2, 번호3, 번호4, 번호5, 번호6, , 보너스1, 보너스2, 보너스3, 보너스4, 보너스5, 보너스6" + "\n")

    for n in range(1, 38 + 1):
        res = crawler(n)
        f.write(str(res['no']) + "," + str(res['jo']) + "," + str(res['num1']) + "," + str(res['num2']) + "," + str(res['num3']) +
        "," + str(res['num4']) + "," + str(res['num5']) + "," + str(res['num6']) + "," + "" + "," + str(res['bonus1']) + "," + 
        str(res['bonus2']) + "," + str(res['bonus3']) + "," + str(res['bonus4']) + "," + str(res['bonus5']) + "," + str(res['bonus6']) + "\n")
    
    f.close()

basic_data()