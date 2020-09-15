
def basicInfo_list(info_num):
    
    info_dict = {0 : '종목명'
                 , 1 : '결산월'
                 , 2 : '액면가'
                 , 3 : '자본금'
                 , 4 : '상장주식수'
                 , 5 : '신용비율'
                 , 6 : '연중최고'
                 , 7 : '연중최저'
                 , 8 : '시가총액'
                 , 9 : '시가총액비중'
                 , 10 : '외인소진률'
                 , 11 : '대용가'
                 , 12 : 'PER'
                 , 13: 'EPS'
                 , 14 : 'ROE'
                 , 15 : 'PBR'
                 , 16 : 'EV'
                 , 17 : 'BPS'
                 , 18 : '매출액'
                 , 19 : '영업이익'
                 , 20 : '당기순이익'
                 , 21 : '250최고'
                 , 22 : '250최저'
                 , 23 : '시가'
                 , 24 : '고가'
                 , 25 : '저가'
                 , 26 : '상한가'
                 , 27 : '하한가'
                 , 28 : '기준가'
                 , 29 : '예상체결가'
                 , 30 : '예상체결수량'
                 , 31 : '250최고가일'
                 , 32 : '250최고가대비율'
                 , 33 : '최저가일'
                 , 34 : '250최저가대비율'
                 , 35 : '현재가'
                 , 36 : '대비기호'
                 , 37 : '전일대비'
                 , 38 : '등락율'
                 , 39 : '거래량'
                 , 40 : '거래대비'
                 , 41 : '액면가단위'
                 , 42 : '유통주식'
                 , 43 : '유통비율'
                 
                 }
    

    return (info_dict[info_num], len(info_dict))

def data_type(info_num):
    
    data_type  = {0 : 'string'
                 , 1 : 'intiger'
                 , 2 : 'intiger'
                 , 3 : 'intiger'
                 , 4 : 'intiger'
                 , 5 : 'float'
                 , 6 : 'intiger'
                 , 7 : 'intiger'
                 , 8 : 'intiger'
                 , 9 : 'float'
                 , 10 : 'float'
                 , 11 : 'intiger'
                 , 12 : 'float'
                 , 13 : 'float'
                 , 14 : 'float'
                 , 15 : 'float'
                 , 16 : 'float'
                 , 17 : 'float'
                 , 18 : 'float'
                 , 19 : 'float'
                 , 20 : 'float'
                 , 21 : 'intiger'
                 , 22 : 'intiger'
                 , 23 : 'intiger'
                 , 24 : 'intiger'
                 , 25 : 'intiger'
                 , 26 : 'intiger'
                 , 27 : 'intiger'
                 , 28 : 'intiger'
                 , 29 : 'intiger'
                 , 30 : 'intiger'
                 , 31 : 'intiger'
                 , 32 : 'float'
                 , 33 : 'intiger'
                 , 34 : 'float'
                 , 35 : 'intiger'
                 , 36 : 'intiger'
                 , 37 : 'intiger'
                 , 38 : 'float'
                 , 39 : 'intiger'
                 , 40 : 'float'
                 , 41 : 'float'
                 , 42 : 'intiger'
                 , 43 : 'float'
                 
                 }
    

    return (data_type[info_num])

print(data_type(43))
# for i in range(0,43):
#     val1, val2 = basicInfo_list(i)
#     print(val1)
#     print(val2)