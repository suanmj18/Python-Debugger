from Common_functions import bracket_check,variable_check

def print_check(lines,index):
    ln=len(lines[index])
    check_quote = 0
    left_string=""
    for ck in lines[index]:
        if (ck == '"'): check_quote ^= 1
        if (check_quote): continue
        left_string+=ck

    brac_check=bracket_check(left_string)
    if(brac_check==False):
        return False,"Brackets are not matched"

    str_check=left_string[left_string.index('(')+1:left_string.index(')')]
    all_var=[chr for chr in str_check.split(",")]

    #print(left_string,str_check)

    for var in all_var:
        if var==" " or var=='"': continue
        var=var.replace("(","")
        valid= variable_check(index-1,lines,var)

        if valid==False: return False,"variable {} is not initialized".format(var)

    return True,"all is well"

# with open('fileforcheck.py') as f:
#     lines = [line.rstrip() for line in f]
#
# for i in range(len(lines)):
#     if(lines[i].find('print')!=-1):
#         valid,state=print_check(lines,i)
#         if(valid==False):
#             print(state,"at index {}".format(i+1))
#             next = input("Wish to continue (YES|NO)?")
#             if (next.lower() == 'no'):
#                 exit(0)