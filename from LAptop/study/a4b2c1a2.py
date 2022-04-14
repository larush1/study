# def char_counter(input):
#     counter = 0 
#     prev_char = str(input[0:1])
#     output = ''
#     for char in input:
#         if prev_char == char:
#             counter +=1
#             prev_char = char
#         else:
#             output = output + prev_char + str(counter)
#             counter = 1
#             prev_char = char
#     output = output + prev_char + str(counter)
#     return output




# input = 'aaaabbcaa'
# print(char_counter(input))

s = 'фышопфыпоэфыэфыпжлоыыыыы'
l=len(s)
cnt=1
for i in range(l):
    if i==(l-1):
        print(s[i]+str(cnt),end='')
    else:
        if s[i]==s[i+1]:
            cnt=cnt+1
        else:
            print(s[i]+str(cnt),end='')
            cnt=1