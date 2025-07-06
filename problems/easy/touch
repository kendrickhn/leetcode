class Solution:
    def romanToInt(self, s: str) -> int:
        x = 0
        a = ''
        if 'IV' in s: 
            x += 4
            x_iv = s.replace('IV','')
        else: 
            x_iv = s
        if 'IX' in s:
            x += 9
            x_ix = x_iv.replace('IX','')
        else: 
            x_ix = x_iv
        if 'XL' in s: 
            x += 40
            x_xl = x_ix.replace('XL','')
        else: 
            x_xl = x_ix
        if 'XC' in s: 
            x += 90
            x_xc = x_xl.replace('XC','')
        else: 
            x_xc = x_xl
        if 'CD' in s: 
            x += 400
            x_cd = x_xc.replace('CD','')
        else: 
            x_cd = x_xc
        if 'CM' in s: 
            x += 900
            x_cm = x_cd.replace('CM','')
        else: 
            x_cm = x_cd

        a = x_cm
        for i in a:
            if i == 'I': 
                x += 1
            elif i == 'V':
                x += 5
            elif i == 'X':
                x += 10
            elif i == 'L': 
                x += 50
            elif i == 'C': 
                x += 100
            elif i == 'D':
                x += 500
            elif i == 'M':
                x += 1000
            else: 
                break
        return x