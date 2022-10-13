## alternating prime sequence
# define the getEfficiency method.
from collections import defaultdict
def pairTeams(skill):
    onegroup = sum(skill)//(len(skill)//2)
    dic = defaultdict(lambda :0)
    for eff in skill:
        dic[eff] += 1

    res = 0
    for key in dic.keys():
        other = onegroup - key
        if other not in dic.keys():
            return -1
        if dic[key] != dic[other]:
            return -1
        res += dic[key] * key * other

    return res//2


if __name__ == '__main__':

    res = pairTeams([5,4,2,1])
    print(res)