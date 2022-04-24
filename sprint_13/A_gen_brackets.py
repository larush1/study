# def gen_binary(n, prefix):
#     if n == 0:
#         print(prefix)
#     else:
#         gen_binary(n - 1, prefix + '(')
#         gen_binary(n - 1, prefix + ')') 

# gen_binary(3, '')

# -------------WTF------------

# def balanced(testVariable, startIndex = 0, currentIndex = 0) :
#   # Base case1 and 2
#   if startIndex == len(testVariable) : 
#     return currentIndex == 0

#   # Base case3
#   if currentIndex < 0 : # A closing bracket did not find its corresponding opening bracket
#     return False

#   # Recursive case1
#   if testVariable[startIndex] == "(" : 
#     return  balanced(testVariable, startIndex + 1, currentIndex + 1)

#   # Recursive case2
#   elif testVariable[startIndex] == ")" : 
#     return  balanced(testVariable, startIndex + 1, currentIndex - 1)

# # Driver Code
# # testVariable = ["(", "(", ")", ")", "(", ")"]
# testVariable = ["(", ")","(",]
# print(balanced(testVariable))
# def printParenthesis(str, n):
#     if(n > 0):
#         _printParenthesis(str, 0,
#                           n, 0, 0)
#     return
# def _printParenthesis(str, pos, n,
#                       open, close):
#     if(close == n):
#         for i in str:
#             print(i, end="")
#         print()
#         return
#     else:
#         if(open > close):
#             str[pos] = ')'
#             _printParenthesis(str, pos + 1, n,
#                               open, close + 1)
#         if(open < n):
#             str[pos] = '('
#             _printParenthesis(str, pos + 1, n,
#                               open + 1, close)
 
 
# Driver Code
# n = 3
# str = [""] * 2 * n
# printParenthesis(str, n)
 
# This Code is contributed
# by mits.
res = []

def GenParenthesis(str, n):
    if(n > 0):
        _GenParenthesis(str, 0,
                          n, 0, 0)
    return


def _GenParenthesis(str, pos, n,
                      open, close):
    seq = ''
    if(close == n):
        for i in str:
            seq += i
        global res
        res += [seq]
        return
    else:
        if(open > close):
            str[pos] = ')'
            _GenParenthesis(str, pos + 1, n,
                              open, close + 1)
        if(open < n):
            str[pos] = '('
            _GenParenthesis(str, pos + 1, n,
                              open + 1, close)

# Driver Code
n = int(input())
str = [""] * 2 * n
GenParenthesis(str, n)
for i in res[::-1]:
    print(i)
