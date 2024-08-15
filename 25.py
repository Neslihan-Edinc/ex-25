def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()#Bosluk kaldır kucuk donustur
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2): #uzunluklar aynı olmalı!
        return False
    
    # Her iki string'in harflerini sırala ve karşılaştır
    return sorted(str1) == sorted(str2)#harf harf incele esit mi

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")


if are_anagrams(string1, string2):
    print("They are anagrams")
else:
    print("They are not anagrams.")
