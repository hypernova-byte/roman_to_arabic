class answer:
    def romanToInt(self, s: str) -> int:
        num = 0
        run = True
        skip = False
        table = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500, 
            "M" : 1000
                }
        for i in range(len(s)):
            skip = False
            print(num)
            if run:
                try:
                    if table[s[i]] < table[s[i+1]]:
                        num += (table[s[i+1]] - table[s[i]])
                        skip = True
                        print(f"i is equal to {i}")
                    else:
                        num += table[s[i]]
                except:
                    num += table[s[i]]
            
            if skip == True:
                run = False
            else:
                run = True
        
        print(num)
        return num

sol = answer()
sol.romanToInt("LVIII") #1994