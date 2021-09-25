from Module_check import module_check
from Print_check import print_check
from Common_functions import comment_delete,Indentation
from For_loop import for_loop_check
from While_loop import check_while_present
from Condition_check import Condition_check
from Function_check import function_present


#check for all the variables
#spelling check
#all codes should be in def or main

if __name__=='__main__':
    with open('test3.py') as f:
        codes = [line.rstrip() for line in f]

    errors=0
    codes=comment_delete(codes)
    # print(codes)
    valid,message=Indentation(codes)
    if valid:
        errors+=1
        print(message)
        exit(0)

    for i in range(len(codes)):

        list_of_line=[str(x) for x in codes[i]]

        if ('import' in codes[i].split()):
            module_status, module = module_check([str(x) for x in codes[i].split()])
            if (module_status == 0):
                errors+=1
                print("Module {} is not present".format(module))
                next = input("Wish to continue (YES|NO)?")
                if (next.lower() == 'no'): exit(0)

        if (codes[i].find('print') != -1):
            valid, state = print_check(codes, i)
            if (valid == False):
                errors+=1
                print(state, "at index {}".format(i + 1))
                exit(0)

        if 'for ' in codes[i]:
            valid, message = for_loop_check(i,codes)
            if valid:
                errors+=1
                print(message)
                exit(0)

        valid,message=check_while_present(i,codes)
        if valid:
            errors+=1
            print(message)
            exit(0)

        valid,message=Condition_check(i,codes)
        if valid:
            errors+=1
            print(message)
            exit(0)

        valid, message = function_present(i, codes)
        if valid:
            errors+=1
            print(message)
            exit(0)


    print("executed successfully with {} errors".format(errors))

