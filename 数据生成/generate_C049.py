# C049 （C#，CNAME，PERIOD，CREDIT，TEACHER）

import random


def generate_C():
    deps = ['CS', 'EE', 'SC', 'AI', 'SE', 'DS', 'IE', 'ME', 'CE', 'AE',
            'MT', 'PE', 'CH', 'BI', 'MA', 'PH', 'EN', 'HI', 'MU', 'AR']
    # 不能生成重复的课程号
    exist_C = ['CS-01', 'CS-02', 'CS-03', 'CS-04', 'CS-05', 'EE-01', 'EE-02', 'EE-03']
    C_list = []
    for i in range(1000):
        dep = random.choice(deps)
        num = str(random.randint(1, 99)).zfill(2)
        C = dep + '-' + num
        while C in exist_C:
            dep = random.choice(deps)
            num = str(random.randint(1, 99)).zfill(2)
            C = dep + '-' + num
        exist_C.append(C)
        C_list.append(C)

    # 存储课程号到data文件夹
    with open('data/C.txt', 'w', encoding='utf-8') as f:
        for i in range(1000):
            f.write(C_list[i] + '\n')

    return C_list


def generate_CNAME():
    with open('data/clear_course.txt', 'r', encoding='utf-8') as f:
        cname_list = f.readlines()[0:1000]
    return cname_list


def generate_PERIOD():
    PERIOD_list = []
    period = [24, 32, 48, 64, 40, 16, 56, 72, 80, 88, 60, 80, 100]
    for i in range(1000):
        PERIOD_list.append(random.choice(period))
    return PERIOD_list


def generate_CREDIT():
    CREDIT_list = []
    credit = [0.5, 1, 1.5, 2, 2.5, 3, 4, 5]
    for i in range(1000):
        CREDIT_list.append(random.choice(credit))
    return CREDIT_list


def generate_TEACHER():
    with open('data/shuffle_name.txt', 'r', encoding='utf-8') as f:
        # 选后1000个
        name_list = f.readlines()
        TEACHER_list = name_list[len(name_list)-1000:]

    return TEACHER_list


if __name__ == '__main__':
    C = generate_C()
    CNAME = generate_CNAME()
    PERIOD = generate_PERIOD()
    CREDIT = generate_CREDIT()
    TEACHER = generate_TEACHER()

    with open('C049.txt', 'w', encoding='utf-8') as f:
        SQL = 'INSERT INTO C049 VALUES\n'
        for i in range(1000):
            if i == 999:
                SQL += f"('{C[i]}', '{CNAME[i].strip()}', {PERIOD[i]}, {CREDIT[i]}, '{TEACHER[i].strip()}');"
            else:
                SQL += f"('{C[i]}', '{CNAME[i].strip()}', {PERIOD[i]}, {CREDIT[i]}, '{TEACHER[i].strip()}'),\n"
        f.write(SQL)
