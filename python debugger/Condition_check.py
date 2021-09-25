#only in form of if(condition): or if condition:, codition should have space in between like a <= b
def variable_check(ind,codes,var):
    if var.isnumeric(): return True

    while(ind):
        if 'def ' in codes[ind] or "if __name__=='__main__':" in codes[ind]:
            return False
        search1 = ' ' + var + '='
        search2 = ',' + var + '='
        if search1 in codes[ind] or search2 in codes[ind]:
            return True
        ind-=1
    return False

def operator_check(op):
    valid_word_operators = ['and', 'or', 'not']
    valid_symbols = ['>', '>=', '<', '<=', '==', '!=']
    not_symbol = ['=', '!']

    if op in valid_word_operators or op in valid_symbols: return True
    return False

def check_elif_condition(ind,codes):
    check_cont=""
    if codes[ind][:codes[ind].index(':')].find('(')!=-1:
        st=codes[ind].index('(')
        end=codes[ind].index(')')
        check_cont=codes[ind][st+1:end]
    else:
        st=codes[ind].index("if")
        end=codes[ind].index(':')
        check_cont=codes[ind][st+3:end]

    all_check=[]
    if ' or ' in check_cont and ' and ' in check_cont:
        val=[str(x) for x in check_cont.split('or')]
        l=[]
        for ele in val: l+=[str(x) for x in ele.split("and")]
        all_check+=l
    elif ' or ' in check_cont: all_check=[str(x) for x in check_cont.split("or")]
    elif ' and ' in check_cont: all_check=[str(x) for x in check_cont.split("and")]
    else: all_check=[check_cont]

    for check_content in all_check:

        if check_content.isnumeric():
            return 0,"all is well"
        val=[str(x) for x in check_content.split()]
        valid_var=variable_check(ind-1,codes,val[0])
        valid_op=operator_check(val[1])
        valid_cond=True if val[2].isnumeric() else variable_check(ind-1,codes,val[2])

        if valid_var==False: return 1,'variable {} is not defined on line no {}'.format(val[0],ind+1)
        elif valid_op==False: return 1,'operator {} is not valid on line no {}'.format(val[1],ind+1)
        elif valid_cond==False: return 1,'variable {} is not defined on line no {}'.format(val[2],ind+1)

    return 0,"all is well"

def Condition_check(i,codes):
    if_var1=' if('
    if_var2=' if '

    elif_var1=' elif('
    elif_var2=' elif '

    if if_var2 in codes[i] or if_var2 in codes[i] or elif_var2 in codes[i] or elif_var1 in codes[i]:
        valid,message=check_elif_condition(i,codes)
        if valid: return 1,message

    return 0,'all is well'


# with open('fileforcheck.py') as f:
#     lines = [line.rstrip() for line in f]
# for i in range(len(lines)):
#     print(lines[i])
#     valid,message=Condition_check(i,lines)
#     print(valid,message)
