Str = "Sarah marshall"
Hld = ""
char = 0

vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

while (char<len(Str)):
    if(Str[char]=="R" or Str[char]=="r"):
        Hld += Str[char] #append Str to Hld 
        char+=1 #next character in string
        while(Str[char]=="a" #while the letters are vowels we keep appending
            or Str[char]=="e" 
            or Str[char]=="i" 
            or Str[char]=="o" 
            or Str[char]=="u" 
            or Str[char]=="A" 
            or Str[char]=="E" 
            or Str[char]=="I" 
            or Str[char]=="O" 
            or Str[char]=="U"):
            Hld += Str[char] #append every vowel
            char+=1 #next character
        Hld += Str[char]#Append the first non vowel character to Hld
        Str = Str.replace(Hld, "rick") #replace the phrase of Hld with rick
        Hld = "" #revert Hld back to normal


    if(Str[char]=="M" or Str[char]=="m"):
        Hld += Str[char]
        char+=1
        while(Str[char]=="a" 
        or Str[char]=="e" 
        or Str[char]=="i" 
        or Str[char]=="o" 
        or Str[char]=="u" 
        or Str[char]=="A" 
        or Str[char]=="E" 
        or Str[char]=="I" 
        or Str[char]=="O" 
        or Str[char]=="U"):
            Hld += Str[char]
            char+=1
        Hld += Str[char]
        Str = Str.replace(Hld, "mort")
        Hld = ""
    char+=1
print(Str)




