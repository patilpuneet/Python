def anagram(s):
    string_list = []
    for ch in s.lower():
        string_list.append(ch)

    string_dict = {}
    for ch in string_list:
        if ch not in string_dict:
            string_dict[ch] = 1
        else:
            string_dict[ch] = string_dict[ch] + 1

    return string_dict



s1 = "mommy"
s2 = "yommm"

a = anagram(s1)
print (a)
b = anagram(s2)
print (b)

if a == b:
    print ("Anagram")
else:
    print ("Not Anagram")
