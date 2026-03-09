# This is a staircase of size n=4 / display = “#”:
# Input 0 < n <= 30 / display is any character
# Write your code and your test with AAA
#    #
#   ##
#  ###
# ####

def staircase(n,display):
    assert 0 < n <= 30, "n must be between 1 and 30"
    result = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        characters = display * i
        result.append(spaces + characters)
    return '\n'.join(result)
