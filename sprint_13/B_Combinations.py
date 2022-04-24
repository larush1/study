letters = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}

print(seq)

def get_all_num_seq(seqs, n1, n2, iter):
    if seqs[iter+1]!=
        print(seq1[n1] + seq2[n2] + ' ', end='')
        n2 += 1
        iter += 1
        get_all_num_seq(seq1, seq2, seq3, n1, n2, iter)
    else:
        iter = 0
        n2 = 0
        n1 += 1


seqs={
    'abc',
    'def',
    'ghi',
    0
}
n1 = 0
n2 = 0
iter = 0
if __name__ == '__main__':
    get_all_num_seq(seq1, seq2, seq3, n1, n2, iter)


# def get_all_num_seq(seq1, seq2, n1, n2, iter):
#     if iter < len(seq2):
#         print(seq1[n1] + seq2[n2] + ' ', end='')
#         n2 += 1
#         iter += 1
#         get_all_num_seq(seq1, seq2, n1, n2, iter)
#     else:
#         iter = 0
#         n2 = 0
#         n1 += 1
#         # get_all_num_seq(seq1, seq2, n1, n2, iter)

# seq1 = 'a'
# seq2 = 'def'
# n1 = 0
# n2 = 0
# iter = 0
# if __name__ == '__main__':
#     get_all_num_seq(seq1, seq2, n1, n2, iter)

# def run():
#     num = list(input())
#     seq = list(map(int, num))
#     # for number in seq:
#     #     get_all_num_seq(number, next_number, len(seq))


# def get_all_num_seq(seq, len):
#     if n == len:
#         return
#     for l in letters(n):
#         print(l, end='')
#         get_all_num_seq()



# def run():
#     calls = list(input())
#     deep = len(calls)
#     out_str = ''
#     for i in range(deep - 1):
#         for a in letters[calls[i]]:
#             for b in letters[calls[i+1]]:
#                 out_str += a
#                 out_str += b
#                 out_str += ' '
#     print(out_str)
#     for a in letters[n1]:
#         for b in letters[n2]:
#             out_str += a
#             out_str += b
#             out_str += ' '
#     print(out_str)



