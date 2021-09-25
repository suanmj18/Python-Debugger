#similar condition as if-else
def variable_check(ind,codes,var):
    # var = codes[ind][codes[ind].index('(') + 1:codes[ind].index(')')]

    while (ind):
        if 'def ' in codes[ind] or "if __name__=='__main__':" in codes[ind] or ind<0:
            return False
        search1 = ' ' + var + '='
        search2 = ',' + var + '='
        if search1 in codes[ind] or search2 in codes[ind]:
            return True
        ind -= 1
    return False

def operator_check(op):
    valid_word_operators = ['and', 'or', 'not']
    valid_symbols = ['>', '>=', '<', '<=', '==', '!=']
    not_symbol = ['=', '!']

    if op in valid_word_operators or op in valid_symbols: return True
    return False

def Check_while(ind,codes):
    check_content = ""
    if codes[ind][:codes[ind].index(':')].find('(') != -1:
        st = codes[ind].index('(')
        end = codes[ind].index(')')
        check_content = codes[ind][st + 1:end]
    else:
        st = codes[ind].index("while")
        end = codes[ind].index(':')
        check_content = codes[ind][st + 6:end]

    if check_content.isnumeric():
        return 0,"all is well"

    val=[str(x) for x in check_content.split()]
    valid_var=variable_check(ind-1,codes,val[0])
    valid_op=operator_check(val[1])
    valid_cond=True if val[2].isnumeric() else variable_check(ind-1,codes,val[2])

    if valid_var & valid_op & valid_cond: return 0,'all is ell'
    else:
        if valid_var==False: return 1,'variable {} is not defined on line no {}'.format(val[0],ind+1)
        if valid_op==False: return 1,'operator {} is not valid on line no {}'.format(val[1],ind+1)
        if valid_cond==False: return 1,'variable {} is not defined on line no {}'.format(val[2],ind+1)

def check_while_present(i,codes):
    find1 = 'while('
    find2 = 'while '
    if find1 in codes[i] or find2 in codes[i]:
        return Check_while(i,codes)

    return 0,"all is well"

# with open('fileforcheck.py') as f:
#     lines = [line.rstrip() for line in f]
#     find1='while('
#     find2='while '
# for i in range(len(lines)):
#     if find1 in lines[i] or find2 in lines[i]:
#         print(lines[i])
#         valid,message=Check_while(i,lines)
#         print(valid,message)


