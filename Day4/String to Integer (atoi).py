class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = ""
        sign = ""
        Number_Start = False
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        for i in s:
            if i in numbers:
                Number_Start = True
                r+= i
            elif i == "-":
                if Number_Start:
                    break
                else:
                    Number_Start = True
                if sign == "":
                    sign = "-"
                else:
                    return 0
            elif i == "+":
                if Number_Start:
                    break
                else:
                    Number_Start = True
                if sign == "":
                    sign = "+"
                else:
                    return 0
            elif i == " ":
                if Number_Start:
                    break
                pass
            else:
                break
        if r == "":
            return 0
        if sign == "-":
            sign += r
            if int(sign) <= -2147483648:
                return -2147483648
            return int(sign)
        if int(r) >= 2147483648:
            return 2147483647
        return int(r)
