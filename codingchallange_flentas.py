import re
from itertools import permutations

test_case_count = int(input(""))
# permutations to be used of the given string to check the matching strings.

for i in range(0, test_case_count):
    pattern = input("")
    para = input("")

    list_of_perm = list(permutations(pattern))
    #permutation of given input string is returned


    regex_str = "("
    for text in list_of_perm:
        regex_str = regex_str + "".join(text) + "|"

    regex_str = regex_str[:len(regex_str) - 1]  + ")"

    regex_pattern = re.compile(regex_str)
    search_result = regex_pattern.search(para)
    #returns a boolean value 

    if (search_result):
        print("YES")
    else:
        print("NO")




