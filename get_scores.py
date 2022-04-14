# ID 66454937
from typing import List

def get_scores(data: List[int]) -> int:
    k = data.pop(-1)
    scores = sum(1 for v in data if v <= k * 2)
    return scores

def get_data() -> List[int]:
    k = int(input())
    in_data = []
    for _ in range(4):
        for i in input():
            try:
                in_data += [int(i)]
            except ValueError:
                continue
    out_data = []
    for i in set(in_data):
        out_data += [in_data.count(i)]
    out_data += [k]
    return out_data

if __name__ == '__main__':
    print(get_scores(get_data()))