from Common_functions import variable_check
import builtins
import types

def check_predefined(i,codes,fun_name):
    pre = [name for name, obj in vars(builtins).items() if isinstance(obj, types.BuiltinFunctionType)]+['while','if']
    if fun_name in pre: return 0
    return 1

def def_present(codes,fun_name):
    n=len(codes)
    flag=1
    for i in range(n):
        if 'def ' in codes[i] and fun_name+'(' in codes[i]:
            if codes[i].index('def')< codes[i].index(fun_name):
                flag=0
                break

    return flag

def function_variable_check(ind,codes,fun_name):
    id1=codes[ind].index('(')
    id2=codes[ind].index(')')
    data_in_brac=codes[ind][id1+1:id2]
    variables=list(data_in_brac.split(","))
    var1=len(variables)
    for var in variables:
        flag=variable_check(ind,codes,var)
        if flag==False: return 1,"Variable {} not present".format(var)

    n = len(codes)
    flag = 1
    var2=0
    for i in range(n):
        if 'def ' in codes[i] and fun_name + '(' in codes[i]:
            if codes[i].index('def') < codes[i].index(fun_name):
                id1 = codes[i].index('(')
                id2 = codes[i].index(')')
                data_in_brac = codes[i][id1 + 1:id2]
                variables = list(data_in_brac.split(","))
                var2 = len(variables)
                break

    if var1!=var2:
        if var1>var2: return 1,"{} function definition can't unpack the variables passed".format(fun_name)
        else: return 1,"{} function call have passed less no of variables".format(fun_name)

    return 0,'all is well'

def return_check(fun_name,codes):
    n = len(codes)
    flag = -1
    for i in range(n):
        if 'def ' in codes[i] and fun_name + '(' in codes[i]:
            if codes[i].index('def') < codes[i].index(fun_name):
                flag = i
                break

    r_present=1
    for i in range(flag+1,n):
        if 'def ' in codes[i] or "if __name__=='__main__':" in codes[i]: break
        if 'return ' in codes[i]:
            r_present=0
            break

    return r_present

def function_present(ind,codes):
    if 'for ' in codes[ind]: return 0,""

    if 'def ' not in codes[ind] and '(' in codes[ind] and ')' in codes[ind] and codes[ind][codes[ind].index(')')]>codes[ind][codes[ind].index('(')]:
        fun_name=""
        if '=' in codes[ind]:
            id1 = codes[ind].index("=")
            id2=codes[ind].index("(")
            fun_name=codes[ind][id1+1:id2]
        else:
            id1 = codes[ind].index("(")
            fun_name=codes[ind][:id1].lstrip()

        predefined=check_predefined(ind,codes,fun_name)
        if predefined:
            function_def_present=def_present(codes,fun_name)
            if function_def_present:
                return 1,"Function definition of {} function is not present".format(fun_name)
            else:
                if '=' in codes[ind]:
                    check_for_return=return_check(fun_name,codes)
                    if check_for_return: return 1,"function {} is not returning anything".format(fun_name)
                valid,message=function_variable_check(ind,codes,fun_name)
                if valid: return valid,message

    return 0,'all is well'

# with open('fileforcheck.py') as f:
#     lines = [line.rstrip() for line in f]
# for i in range(len(lines)):
#     valid,message=function_present(i,lines)
#     if valid == 0: continue
#     print(valid,message)
