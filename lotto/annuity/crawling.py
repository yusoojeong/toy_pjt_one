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

    print(data)

    return data

def basic_data():

    for n in range(1, 5 + 1):
        crawler(n)



basic_data()