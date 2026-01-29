# Write a program to find and print all substrings of the string that are palindromes.
#  A substring must contain consecutive characters only.
# Test case 1:
# Input: "racecar"
# Output:
# r
# a
# c
# e
# c
# a
# r
# cec
# aceca
# racecar
def palindrome(a):
    for k in a:
        print(k)
    for i in range(len(a)):
        for j in range(i,len(a)):
            sub = a[i:j+1]
            if sub == sub[::-1]:
                if len(sub)>1:
                    print(sub)
palindrome("racecar")


 