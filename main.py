import sys
#建关键字表
list=[]

#print(dict_op,dict_key)
#分别生成小写字母表，大写字母表，数字表
letter_u = [chr(i) for i in range(97, 123)]
letter_s = [chr(i) for i in range(65, 91)]
letter = letter_s+letter_u+['_']
digit = ['0','1','2','3','4','5','6','7','8','9']

flag = 0 #flag用于标记当前item是否位于注释内容中，取0代表不在注释内容中，取1代表在注释内容中
err = 0 #err用于标记当前语法中是否有错误，取0表示无，取1表示有
#pcd=0
# list=['3::=3']
dict_key={
    "break": "Break",
    "continue": "Continue",
    "if": "If",
    "while": "While",
    "else": "Else",
    "return":"Return",
}

dict_op={
    "+": "Plus",
    "*": "Mult",
    "/": "Div",
    "(": "LPar",
    ")": "RPar",
    ";": "Semicolon",
    "{": "LBrace",
    "}": "RBrace",
    "=": "Assign",
    "==":"Eq",
    ">":"Gt",
    "<":"Lt",
}


def deal():
    for item in list:
        # =pcd+1
        # print(pcd)
        token = ''
        flag_t = 0  # 这个变量用来标识当前已读token是标识符还是数字，取0表示当前token为空或者是标识符；取1表示当前token为数字
        i = 0
        while i < len(item):
            # print('i=', i,'token=',token)
            step = 1
            t = item[i]
            # print('t=', t, ',flag=', flag)
            # 1.识别标识符和关键字
            if t in letter and flag == 0:
                # 如果当前token是数字，则先输出token然后置空token
                if flag_t == 1:
                    print('Number(' + token + ')', end='\n', sep='')
                    # , 'OF' if check_of(token) else token
                    token = ''
                    flag_t = 0
                token += t
                if i == len(item) - 1:
                    if token in dict_key.keys():
                        print(dict_key[token], end='\n', sep='')
                    else:
                        print('Ident(', token, ')', end='\n', sep='')
                    token = ''

            elif t in digit and flag == 0:
                if len(token) == 0:
                    flag_t = 1
                token += t

                if i == len(item) - 1 and flag_t == 1:
                    print('Number(', token, ')', end='\n', sep='')
                    token = ''

                if i == len(item) - 1 and flag_t == 0:
                    print('Ident(', token, ')', end='\n', sep='')
                    token = ''

            # 如果识别到运算符
            elif t in dict_op.keys() and flag == 0:
                # print('t=', t)
                # 如果当前token是数字
                if flag_t == 1:
                    print('Number(', token, ')', end='\n', sep='')
                    token = ''

                # 如果当前token是标识符
                elif flag_t == 0 and len(token) != 0:
                    if token in dict_key.keys():
                        print(dict_key[token], end='\n', sep='')
                    else:
                        print('Ident(', token, ')', end='\n', sep='')
                    token = ''

                flag_t = 0
                token = t

                if t == '=' and i <= len(item) - 1 - 1:
                    if item[i + 1] == '=':
                        step = 2
                        print(dict_op["=="], end='\n')
                        token = ''
                    else:
                        print(dict_op[token])
                        token = ''

                else:
                    print(dict_op[token])
                    token = ''




            # 如果识别到了不明物体：
            elif flag == 0:
                # 如果当前token是数字
                if flag_t == 1:
                    print('Number(', token, ')', end='\n', sep='')
                    token = ''

                # 如果当前token是标识符
                if flag_t == 0 and len(token) != 0:
                    print('Ident(', token, ')', end='\n', sep='')
                    token = ''

                else:
                    print('Err\n')
                break

            i += step




for line in sys.stdin:
    list= line.split()
    deal()
    if not line:
        break
