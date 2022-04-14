def is_palindrome(line: str) -> bool:
    for_check = ''
    for i in line:
        if i.isalpha() or i.isdigit():
            for_check += i
    print(for_check.lower())
    print(for_check[::-1].lower())
    return for_check.lower() == for_check[::-1].lower()


# print(is_palindrome(input().strip()))
# print(is_palindrome('A man, a plan, a canal: Panama'))
# print(is_palindrome('Унес раков и пиво к Арсену.'))
print(is_palindrome('А нам ругала гурманa.'))


# with open('New Text Document.txt', mode="r", encoding="utf-8") as f:
#     lines = f.readlines()
# f.close()

# fw = open("demofile2.txt", "w")

# for line in lines:
#     if line == '\n':
#         continue
#     # print(f'{line} - {is_palindrome(line)}')
#     fw.write(f'{line.strip()} - {is_palindrome(line)}\n')

# fw.close()