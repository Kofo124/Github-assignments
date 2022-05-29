# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(str1, str2):
    # [assignment] Add your code here


    str1_anagrams = sorted(str1)
    str2_anagrams = sorted(str2)

    if str1 == str2 :
        return False
    else:
        return True

print(find_anagram("hello","check"))
print(find_anagram("below","elbow"))
    