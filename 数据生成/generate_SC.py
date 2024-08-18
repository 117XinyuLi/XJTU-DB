# SC049 (S, C, GRADE), 生成200000条记录


import random


def read_S():
    with open('S049.txt', 'r', encoding='utf-8') as f:
        # 读取S049.txt文件，返回一个列表
        S_list = f.readlines()
    S_list = S_list[1:]
    S_list = [S[2:10] for S in S_list]
    return S_list

def read_C():
    with open('C049.txt', 'r', encoding='utf-8') as f:
        C_list = f.readlines()
    C_list = C_list[1:]
    C_list = [C[2:7] for C in C_list]
    return C_list

def generate_SC():
    S_list = read_S()
    C_list = read_C()

    # 前5000条记录
    S_list_1 = S_list[:1000]
    C_list_1 = C_list[:100]

    SC_list_1 = []
    S_and_C_1 = []
    for S in S_list_1:
        for C in C_list_1:
            S_and_C_1.append((S.strip(), C.strip()))

    S_and_C_1 = random.sample(S_and_C_1, 20000)
    print('S_and_C_1 generated successfully!')

    for i in range(20000):
        grade = random.randint(40, 100)
        if random.randint(0, 1) == 1 and grade < 100:
            grade += 0.5
        SC_list_1.append((S_and_C_1[i][0], S_and_C_1[i][1], grade))

    print('SC_list_1 generated successfully!')

    # 从中选出200条分数小于60的记录
    less_than_60 = [('01032023', 'CS-01', 55.0), ('03031051', 'EE-02', 58.0)]
    for record in SC_list_1:
        if record[2] < 60 and random.randint(0, 1) == 1 and record not in less_than_60:
            less_than_60.append(record)
        if len(less_than_60) == 200:
            break

    print('less_than_60 generated successfully!')

    SC_list_2 = []
    S_and_C_2 = []
    flag = 0
    for S in S_list:
        for C in C_list:
            if (S.strip(), C.strip()) in S_and_C_1:
                continue
            S_and_C_2.append((S.strip(), C.strip()))
            # print(len(S_and_C_2))
            if len(S_and_C_2) == 180000:
                flag = 1
                break
        if flag == 1:
            break

    print('S_and_C_2 generated successfully!')

    for i in range(180000):
        grade = random.randint(40, 100)
        if random.randint(0, 1) == 1 and grade < 100:
            grade += 0.5
        SC_list_2.append((S_and_C_2[i][0], S_and_C_2[i][1], grade))

    print('SC_list_2 generated successfully!')


    return SC_list_1, SC_list_2, less_than_60


if __name__ == '__main__':
    SC1, SC2, less_than_60 = generate_SC()
    print('SC and less_than_60 generated successfully!')

    with open('SC049_1.txt', 'w', encoding='utf-8') as f:
        SQL = 'INSERT INTO SC049 VALUES\n'
        for i in range(len(SC1)):
            if i == len(SC1) - 1:
                SQL += f"('{SC1[i][0]}', '{SC1[i][1]}', {SC1[i][2]});"
            else:
                SQL += f"('{SC1[i][0]}', '{SC1[i][1]}', {SC1[i][2]}),\n"
        f.write(SQL)

    with open('SC049_2.txt', 'w', encoding='utf-8') as f:
        SQL = 'INSERT INTO SC049 VALUES\n'
        for i in range(len(SC2)):
            if i == len(SC2) - 1:
                SQL += f"('{SC2[i][0]}', '{SC2[i][1]}', {SC2[i][2]});"
            else:
                SQL += f"('{SC2[i][0]}', '{SC2[i][1]}', {SC2[i][2]}),\n"
        f.write(SQL)

    with open('delete_less_than_60.txt', 'w', encoding='utf-8') as f:
        # SQL删除200条分数小于60的记录
        SQL = 'DELETE FROM SC049 WHERE (Sno, Cno, GRADE) IN (\n'
        for i in range(200):
            if i == 199:
                SQL += f"('{less_than_60[i][0]}', '{less_than_60[i][1]}', {less_than_60[i][2]}) );"
            else:
                SQL += f"('{less_than_60[i][0]}', '{less_than_60[i][1]}', {less_than_60[i][2]}),\n"
        f.write(SQL)



