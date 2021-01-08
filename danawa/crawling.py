#-*-coding:utf-8-*-
import time
import sys
import urllib
import requests
from bs4 import BeautifulSoup

def danawaCraw(pcode, page):
    reviewlist1 = []
    reviewlist2 = []
    reviewlist3 = []
    for idx in range(1,page+1):
        headers = {"Referer" : "http://prod.danawa.com/info/", "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
        params = {"t" : 0.2743197359712919, "prodCode" : pcode, "page" : idx, "limit":100, "score":0,"usefullScore":"Y", "_":1609524637300,"sortType":"NEW"}
        #print(idx,'페이지에서', len(divs),'개의 리뷰 크롤링완료')
        res = requests.get("http://prod.danawa.com/info/dpg/ajax/companyProductReview.ajax.php", headers = headers, params = params)
        soup = BeautifulSoup(res.text, "html.parser")
        divs1 = soup.find_all("div", attrs = {"class":"atc"})
        divs2 = soup.find_all("span", attrs = {"class":"date"})
        divs3 = soup.find_all("span", attrs = {"class":"star_mask"})
        #print(idx,'페이지에서', len(divs),'개의 리뷰 크롤링완료')
        for i in range(len(divs1)):
            #reviewlist1.append(" ".join(divs1[i].text.split()))
            reviewlist2.append(" ".join(divs2[i].text.split()))
            reviewlist3.append(" ".join(divs3[i].text.split()))
    return [reviewlist1,reviewlist2,reviewlist3]

def getPcode(page,token):
    tokenURL=urllib.parse.quote(token)
    pCodeList = []
    for i in range(1,page+1):
        print(i,"페이지 입니다")
        headers = {
            "Host": "search.danawa.com",
            "Connection": "keep-alive",
            "Content-Length": "350",
            "Accept": "text/html, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "http://search.danawa.com",
            "Referer": "http://search.danawa.com/dsearch.php?query="+tokenURL+"&tab=main",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            # #"Cookie": "_ga=GA1.2.1983122550.1601479648; OAX=Oo5amF90o+EAB2Ax; ADWEBCOUNTER_UUID2=d333acff-5b7c-202e-9c90-c1b508484b3b; _gac_UA-37762359-14=1.1607190580.CjwKCAiA_Kz-BRAJEiwAhJNY7ytO_RCtYL4pFWv3tcL0IgW1LuJCY2SWpI60bc1nB9tuiZQVlA7OCBoCzoYQAvD_BwE; cookieGuestId=da5bafde802f6b5f5ee54e0e98667c62; danawa-loggingApplicationClient=d4af03b0-2d10-4ab1-97fe-e9624d425e50; __gads=ID=375698ebc1922491-22dc057d06c500b5:T=1607190629:RT=1607190629:S=ALNI_MYf2t5P5Qm5MzVIgCsRwSwcH_ZdyA; dable_uid=40605990.1570384594973; recentProductYN=Y; cookSaveShopInfo=EE715%3A2021-01-02%7CTH201%3A2021-01-03; cookRecentlyPlans=4130; _gid=GA1.2.807643478.1609953780; cPreviousKeyword=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90%20%EC%95%84%EA%B0%80%EC%82%AC%EB%9E%91; cookSaveProdInfo=10%3A2251290%3A312230%7C10%3A5395231%3A468610%7C10%3A9710205%3A209000%7C10%3A9681093%3A210320%7C10%3A12153809%3A1315750%7C10%3A12969596%3A73510%7C10%3A12337631%3A259220%7C10%3A12337646%3A305310%7C10%3A12337544%3A249000%7C10%3A12843428%3A53810%7C10%3A12548558%3A40650%7C10%3A9661122%3A105000%7C10%3A9514443%3A32390%7C10%3A12395729%3A122270%7C10%3A1253525%3A69000; _INSIGHT_CK_8203=3090400cc1c2f02062cfd9b8d2aad124_79650|f1233411ad0631403158d340a5497fb3_53779:1609958699000; wcs_bt=s_3b3fb74948b1:1609956899; cookNewSearchKeyword=%EC%9C%84%EB%8B%89%EC%8A%A4%3E01.07%7C%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90%20%EC%95%84%EA%B0%80%EC%82%AC%EB%9E%91%3E01.07%7C%EA%B3%B5%EA%B8%B0%EC%B2%AD%EC%A0%95%EA%B8%B0%3E12.18"
                }
        params = {
        "query":token,
        "originalQuery": token,
        "previousKeyword": token,
        "marketbrand_name": token,
        "volumeType": "allvs",
        "page": i,
        "limit": "40",
        "sort":  "",
        "list": "list",
        "boost": "true",
        "addDelivery": "N",
        "recommendedSort": "Y",
        "defaultUICategoryCode": "0",
        "defaultPhysicsCategoryCode": "" ,
        "defaultVmTab": "0",
        "defaultVaTab": "0",
        "tab": "main",
        "cate_c1": "118",
        "cate_c2": "11420"
        }
        res = requests.post("http://search.danawa.com/ajax/getProductList.ajax.php", headers = headers, data=params)
        soup = BeautifulSoup(res.text, "html.parser")
        a = soup.findAll("li",{"class":"prod_item"})
        for i in range(len(a)):
            if a[i].has_attr('id') and "_" not in a[i]['id'][11:]:
                pCodeList.append(a[i]['id'][11:])
    print(pCodeList)
    return pCodeList

TotalReview=[]
for p in getPcode(12,"위닉스"):
    print(p)
    TotalReview.append(danawaCraw(p,50))

last={}
for i in range(0,len(TotalReview)):
    for j in range(0,len(TotalReview[i][1])):
        tmp=TotalReview[i][1][j]
        tmp=tmp.split(".")
        tmp=tmp[0]+"-"+tmp[1]
        if tmp not in last:
            last[tmp]=0
        last[tmp]=last[tmp]+1
print(last)
