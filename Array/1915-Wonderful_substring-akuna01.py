## Extraordinary substring
from collections import defaultdict
def wonderfulSubstrings( word):
    res = 0
    for i in range(len(word)):
        d = defaultdict(lambda: 0)
        for j in range(i, len(word)):
            d[word[j]] += 1

            odd = 0
            for i, (k, v) in enumerate(d.items()):
                if v % 2 != 0:
                    odd += 1
                if odd > 1:
                    break
                if i == len(d) - 1:
                    res += 1

                if i == len(d)-1:
                    res += 1
    return res
if __name__ == '__main__':
    input_str = 'aabb'
    result = wonderfulSubstrings(input_str)
    print(result)
