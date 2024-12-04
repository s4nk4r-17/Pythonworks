
def romanToInt(s:str)->int:
    rom_to_integer={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
        }
    total=0

    for i in range(0,len(s)-1):
                                                        #M    C          C   M                  M   X                  X  C                C  I        I V           V
        if rom_to_integer[s[i]]<rom_to_integer[s[i+1]]: #1000<100=>1000;100<1000=>1000-100=900;1000<10=>900+1000=1900;10<100=>1900-10=1890;100<1=>1990;1<5=1989;1989+5=1994
        
            total=total-rom_to_integer[s[i]]
    
        else:

            total=total+rom_to_integer[s[i]]

    total+=rom_to_integer[s[-1]]


    return total

examples=["III", "LVIII", "MCMXCIV"]

for exp in examples:

    print(f"Input:{exp} --> Output:{romanToInt(exp)}")