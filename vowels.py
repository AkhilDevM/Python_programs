in_strng=input('enter a string')
in_strng=in_strng.casefold()
vowel="aeiou"
data={}.fromkeys(vowel,0)
for character in in_strng:
    if character in vowel:
        data[character]+=1
        for vowel in data:
            print(vowel,'=>',data[vowel])
            
        
    
