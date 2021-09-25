#for checking the balanced brackets
import keyword

def bracket_check(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]: stack.append(char)

        else:
            if char not in [")", "}", "]"]: continue
            current_char = stack.pop()
            if current_char == '(':
                if char != ")": return False
            if current_char == '{':
                if char != "}": return False
            if current_char == '[':
                if char != "]": return False

    if stack: return False
    return True

#function to delete the comment
def comment_delete(lines):

    line,n = 0, len(lines)
    lines_to_remove=[]
    while line <n:
        if "'''" in lines[line]:
            j=line+1
            while j<n and "'''" not in lines[j]: j+=1
            lines_to_remove.append((line,min(j,n-1)))
            line=j+1
        else: line+=1

    for i,j in lines_to_remove:
        for k in range(i,j+1): lines[k]=""

    for line in range(len(lines)):
        if '#' in lines[line]: lines[line]=lines[line][:lines[line].index("#")]

    return lines

#variable presence check
def variable_check(ind,codes,var):
    if var.isnumeric(): return True
    if keyword.iskeyword(var): return False

    while(ind):
        if 'def ' in codes[ind] or "if __name__=='__main__':" in codes[ind]:
            return False
        search1 = ' ' + var + '='
        search2 = ',' + var + '='
        if search1 in codes[ind] or search2 in codes[ind]:
            return True
        ind-=1
    return False

#for indentation check
def check(lines,i):
    n=len(lines)
    val = lines[i].rstrip(" ")
    flag=0
    if val[-1] != ':':
        temp=lines[i].find(":")
        if temp==-1:
            flag=1
        else: return 0,"all is well"

    if i == n - 1 and flag==0:
        return 1,"Function definition is not given"
    id = 0
    while (id < len(lines[i]) and lines[i][id] == " "): id += 1

    next_id = 0
    while (next_id < len(lines[i + 1]) and lines[i + 1][next_id] == " "): next_id += 1

    if i<n-1 and lines[i+1]=='': flag=1

    if (flag==1 and id!=next_id) or (flag==0 and id>=next_id):
        # print(flag,id,next_id)
        return 1,"Indentation error at {} please check".format(i + 1)

    return 0,"No error"

def Indentation(lines):
    i=0
    n=len(lines)
    list_tocheck_1=['def','for','else']
    list_tocheck_2=['while','if','elif']
    flag=0
    while(i<n):
        valid=0
        message=""
        for key in list_tocheck_1:
            if key in lines[i].split(" "):
                valid,message=check(lines,i)

        for key in list_tocheck_2:
            if key in lines[i].split(" "):
                valid, message = check(lines, i)
            if key in lines[i]:
                val=lines[i].lstrip(" ")
                ln=len(key)
                if val[:ln]==key and val[ln]=='(':
                    valid, message = check(lines, i)
        i+=1

        if valid: return 1,message

    return 0,"No error"
