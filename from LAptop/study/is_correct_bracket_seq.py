def is_correct_bracket_seq(input):
    cnt_square = 0
    cnt_round = 0
    cnt_figure = 0
    for s in input:
        if cnt_square < 0 or cnt_round < 0 or cnt_figure < 0:
            return False
        if s == '[':
            cnt_square += 1
        elif s == ']':
            cnt_square -= 1
        elif s == '(':
            cnt_round += 1
        elif s == ')':
            cnt_round -= 1
        elif s == '{':
            cnt_figure += 1
        elif s == '}':
            cnt_figure -= 1
    if cnt_square == 0 and cnt_round == 0 and cnt_figure == 0:
        return True
    else:
        return False
        
# input = input()
input = '[{}()]'
print(is_correct_bracket_seq(input))

# def is_correct_bracket_seq(input):
#     # [], (), {}
#     opening = ('[','(','{')
#     closing = (']',')','}')
#     cnt = 0
#     if input == '':
#         return True
#     for s in input:
#         if cnt < 0:
#             return False
#         if s in opening:
#             cnt += 1
#         elif s in closing:
#             cnt -= 1
#     return True if cnt == 0 else False