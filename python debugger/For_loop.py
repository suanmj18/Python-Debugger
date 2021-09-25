from Common_functions import bracket_check,variable_check

def check_for_list(ind,codes,var):
    while (ind):
        if 'def ' in codes[ind] or "if __name__=='__main__':" in codes[ind]:
            return 1,'variable {} not declared '.format(var)
        search1 = ' ' + var + '= ['
        search2 = ' '+var+'=['
        search3=' '+var+'={'
        search4=' '+var+'= {'
        if search1 in codes[ind] or search2 in codes[ind] or search3 in codes[ind] or search4 in codes[ind]:
            return 0,'all is well'
        ind -= 1
    return 1,'List varible "{}" not declared at line {}'.format(var,ind+1)

def for_loop_check(ind,codes):
    if 'range' in codes[ind]:
        if bracket_check(codes[ind]):
            var=codes[ind][codes[ind].index("(")+1:codes[ind].index(")")]
            if variable_check(ind,codes,var) or var.isnumeric():
                return 0,'all is well'
            else: return 1,"Variable {} is not present at line {}".format(var,ind+1)
        else: return 1,"brackets are not balanced at line {}".format(ind+1)
    else:
        temp_list=[str(x) for x in codes[ind].split()]
        var=temp_list[temp_list.index('in')+1]
        var=var.replace(":","")
        return check_for_list(ind,codes,var)

#
# with open('fileforcheck.py') as f:
#     lines = [line.rstrip() for line in f]
# for i in range(len(lines)):
#     if 'for ' in lines[i]:
#         # print(lines[i])
#         valid,message=for_loop_check(i,lines)
#         # print(valid,message)
