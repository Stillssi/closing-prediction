import pandas as pd
def file_maker():
    with open('close-private/재무데이터.txt', 'r', encoding='euc-kr') as f:
        columns = f.readline().split('\t')
        orders = []
        datas = f.readlines()
        for data in datas:
            temp = data.split('\t')
            orders.append(temp)

    df = pd.DataFrame(data=orders, columns=columns)

    df.to_csv('close-private/finance.csv', encoding='euc-kr')

    return 0