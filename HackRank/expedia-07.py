## alternating prime sequence
# define the getEfficiency method.
def getEfficiency(li):
    s = sum(li)
    # this is base condition.
    if s % 2:
        return -1
    ele = s // 2
    hash_map = {}
    for i in li:
        if hash_map.get(i):
            hash_map[i] += 1
        else:
            hash_map[i] = 1
    ans = 0
    for i, j in hash_map.items():
        key1 = i
        key2 = ele - i
        if hash_map.get(key2):
            if j == hash_map[key2]:
                ans = ans + j * (key1 * key2)
            else:
                return -1
        else:
            return -1
    # return the ans.
    return ans // 2


# enter the size of list.
n = int(input())
# enter the list.
li = list(map(int, input().split(" ")))
print(getEfficiency(li))



if __name__ == '__main__':
    initial_players = [1,2]
    new_players = [3,4]
    result = getMinimumHealth(initial_players,new_players,2)
    print(result)