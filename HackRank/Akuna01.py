## Extraordinary substring
from collections import defaultdict
def countSubstrings(n):
    # Write your code here
    ## count its total number of non-empty extraordinary substring
    dic = {'ab':1,'cde':2,'fgh':3,'ijk':4,'lmn':5,'opq':6,'rst':7,'uvw':8,'xyz':9}
    all_dic = {}
    for k,v in dic.items():
        for c in k:
            all_dic[c] = v
    res = []
    for i in range(len(n)):
        sumup=0
        substr = ''
        for j in range(i, len(n)):
            sumup+=all_dic[n[j]]
            substr += n[j]
            # print(substr, sumup)
            if sumup%(j-i+1)==0:
                res.append(substr)

    return res

if __name__ == '__main__':
    input_str = 'asdf'
    result = countSubstrings(input_str)
    print(result)
