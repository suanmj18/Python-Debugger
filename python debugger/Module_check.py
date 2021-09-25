import importlib_metadata
import sys

def module_check(line_in_list):

    module=""
    index_of_import=line_in_list.index('import')

    if(line_in_list[index_of_import+1]!='*'):
        module=line_in_list[index_of_import+1]

    if(index_of_import!=0):
        module=line_in_list[index_of_import-1]

    installed_module=['os'] #to store all the modules which are installed in local system

    in_python_depend=sys.builtin_module_names
    for i in in_python_depend:
        installed_module.append(i.replace("_",""))

    dists = importlib_metadata.distributions()
    for dist in dists:
        name = dist.metadata["Name"]
        installed_module.append(name)
        version = dist.version
        #license = dist.metadata["License"]
        #print(f'found distribution {name}=={version}')

    installed_module.sort()

    l=0
    h=len(installed_module)-1
    present=0
    while(l<=h):
        mid=l+(h-l)//2
        if(installed_module[mid]==module):
            present=1
            break
        elif(installed_module[mid]<module):
            l=mid+1
        else:
            h=mid-1

    return present,module

with open('fileforcheck.py') as f:
    lines = [line.rstrip() for line in f]


# for i in range(len(lines)):
#
#     list_of_line=[str(x) for x in lines[i]]
#
#     if('import' in lines[i].split()):
#         module_status,module=module_check([str(x) for x in lines[i].split()])
#         if(module_status==0):
#             print("Module {} is not present".format(module))
#             next=input("Wish to continue (YES|NO)?")
#             if(next.lower()=='no'):
#                 exit(0)
#         else:
#             print("Module {} is present, checking for others".format(module))