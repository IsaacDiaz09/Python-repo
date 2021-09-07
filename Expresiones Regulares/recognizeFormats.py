import re
# https://www.codeabbey.com/index/task_view/introducing-regexps

"""
· value consisting of digits 0-7 and starting with 0 is octal;
· value consisting of digits 0-9ABCDEF and starting with 0x is hexadecimal;
· hexadecimal could be instead suffixed by h but then it should not start with letter;
· binary could be written as 0b1000101 or 1000101b (though the single letter b is not a number);
· values consisting only of digits 0-9 are considered decimals (but not ones starting with zero - they should be
  regarded as octals and coul only contain digits 0-7).
"""
answer = ""
while True:
    value = input()
    if value == "end":
        print(answer.rstrip())
        break

    # Patron octal
    if re.search(r"^0[0-7]+$",value):
        answer += "oct "

    # Patron hexadecimal
    elif re.search(r"^(0x[\d]|h[\d])+([ABCDEF]+)?",value):
        answer += "hex "

    # Patron binario
    elif re.search(r"^(0b)?[01]+(b)?$",value):
        answer += "bin "

    # Patron decimal
    elif re.search(r"[\d]",value):
        answer += "dec "

"""
Example:

input data:
1347
0x80
013
101b
end

answer:
dec hex oct bin
"""