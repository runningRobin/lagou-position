# -*- coding:utf-8 -*-

import requests
from openpyxl import Workbook

def get_json(url, page, position):
    data = {'first':'true', 'pn':page, 'kd':position}
    json = requests.post(url, data).json()
    result = json['content']['positionResult']['result']
    info_list = []
    for i in result:
        info = [i['city'], i['district'], i['companyFullName'], i['companyShortName'], i['industryField'], i['education'],
                i['salary']]
        info_list.append(info)
    return info_list


def main():
    url = 'http://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
    position = 'php'
    page = 1
    info_result = []

    while page < 31:
        info = get_json(url, page, position)
        info_result = info_result + info
        page += 1
    wb = Workbook()
    ws = wb.active
    ws.title = position
    for row in info_result:
        ws.append(row)
    wb.save('lagou.xlsx')


if __name__ == '__main__':
    main()

