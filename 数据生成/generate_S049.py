# S049 （S#，SNAME，SEX，BDATE，HEIGHT，DORM）

import random


# 生成学号，从03032000到04000000，随机选取5000个学号，不重复
def generate_S():
    S_list = []
    for i in range(3002000, 4000000):
        S_list.append(i)
    random.shuffle(S_list)
    S_list = S_list[0:5000]
    # 生成学号，转为字符串，每个学号占8位，不足8位前面补0
    S_list = [str(S) for S in S_list]
    S_list = ['0'*(8-len(S)) + S for S in S_list]

    # 存储学号到data/S.txt
    with open('data/S.txt', 'w', encoding='utf-8') as f:
        for S in S_list:
            f.write(S + '\n')

    return S_list


def generate_SNAME():
    with open('data/shuffle_name.txt', 'r', encoding='utf-8') as f:
        name_list = f.readlines()[0:5000]
    return name_list


# 生成5000个男.女
def generate_SEX():
    SEX_list = ['男']*2500 + ['女']*2500
    random.shuffle(SEX_list)
    return SEX_list


# 生成5000个生日，从2001到2005
def generate_BDATE():
    BDATE_list = []
    year = ['2001', '2002', '2003', '2004', '2005']
    month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    day = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
           '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
           '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(5000):
        y = random.choice(year)
        m = random.choice(month)
        if m == '2':
            if int(y) % 4 == 0 and int(y) % 100 != 0 or int(y) % 400 == 0:
                d = random.choice(day[0:29])
            else:
                d = random.choice(day[0:28])
        else:
            d = random.choice(day[0:days_in_month[int(m)-1]])
        BDATE_list.append(y + '-' + m + '-' + d)

    return BDATE_list


# 生成5000个身高，从1.50到1.90，保留两位小数
def generate_HEIGHT():
    HEIGHT_list = []
    for i in range(5000):
        HEIGHT_list.append(round(random.uniform(1.50, 1.90), 2))
    return HEIGHT_list


# 生成5000个宿舍号，东/南/西/北 1-20舍，一舍8层，一层20号
def generate_DORM():
    DORM_list = []
    number = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    for i in range(5000):
        dorm = random.choice(['东', '南', '西', '北']) + str(random.randint(1, 20)) + '舍' + str(random.randint(1, 8)) + random.choice(number)
        DORM_list.append(dorm)
    return DORM_list


if __name__ == '__main__':
    S = generate_S()
    SNAME = generate_SNAME()
    SEX = generate_SEX()
    BDATE = generate_BDATE()
    HEIGHT = generate_HEIGHT()
    DORM = generate_DORM()

    SQL = 'INSERT INTO S049 VALUES'
    with open('S049.txt', 'w', encoding='utf-8') as f:
        f.write(SQL + '\n')
        for i in range(5000):
            SQL = '(\'' + S[i] + '\', \'' + SNAME[i].strip() + '\', \'' + SEX[i] + '\', \'' + BDATE[i] + '\', ' + str(HEIGHT[i]) + ', \'' + DORM[i] + '\')'
            if i != 4999:
                SQL += ','
            else:
                SQL += ';'
            f.write(SQL + '\n')

