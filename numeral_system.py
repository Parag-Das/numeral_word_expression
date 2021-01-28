import fire

def figures(number):
    digits = []

    while number > 0:
        digits.append(number%10)
        number = number//10

    digits.reverse()

    #__________ Colors __________
    
    LIGHT_RED = "\033[2;31;47m"
    LIGHT_GREEN = "\033[2;32;47m"
    YELLOW = "\033[2;33;47m"
    LIGHT_BLUE = "\033[2;34;47m"
    LIGHT_PURPLE = "\033[2;35;47m"
    LIGHT_CYAN = "\033[2;36;47m"
    Reset = '\u001b[0m'

    #__________ Arithmetic Nomenclature __________

    once = ('One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')
    eleven_19 = ('Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')
    tenth = ('Ten', 'Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninty')
    bigno = (LIGHT_RED+'Hundred'+Reset, LIGHT_GREEN+'Thousand'+Reset, YELLOW+'Lakh'+Reset, LIGHT_BLUE+'Crore'+Reset, LIGHT_PURPLE+'Arab'+Reset, LIGHT_CYAN+'Kharab'+Reset)

    places = (once, tenth, bigno[0], bigno[1], bigno[1], bigno[2], bigno[2], bigno[3], bigno[3], bigno[4], bigno[4], bigno[5], bigno[5])

    exp = []

    def one_digits(no):
        exp.append(places[0][no[0] - 1])

    def two_digits(no):
        
        if no.count(0) == 1 and no[1] == 0:
            exp.append(places[1][no[0] - 1])
        elif no.count(0) == 0:
            if no[0] == 1 and no[1] > 0:
                exp.append(eleven_19[no[1] - 1])
            else:
                exp.append(places[1][no[0] - 1])
                exp.append(places[0][no[1] - 1])       

    def big_number(no):
        if len(no)%2 == 0:
            one_digits(no[:1])
            exp.append(places[len(no) - 1])
        elif len(no)%2 == 1:
            two_digits(no[:2])
            exp.append(places[len(no) - 2])                

    if len(digits) > len(places):
        print('\tNumber is big i.e {}.'.format(len(digits)),'\n\tPlease enter a number less than {} digits'.format(len(places) + 1))
    else:
        for i in range(len(digits)):
            if digits[i] == 0 :
                i += 1
                continue
            else:
                pass
            if (i > 0 and len(digits[i:]) >= 4) and len(digits[i:])%2 == 0:
                i += 1
                continue
            else :
                pass
    
            if len(digits[i:]) == 1:
                one_digits(digits[i:])
            elif len(digits[i:]) == 2:
                two_digits(digits[i:])
                break  
            elif len(digits[i:]) == 3:
                exp.append(places[0][digits[i] - 1])
                exp.append(places[2])
                if sum(digits[i+1:]) == 0:
                    break
                elif digits[i:].count(0) == 1 and digits[i + 1] == 0:
                    one_digits(digits[-1:])
            elif len(digits[i:]) >= 4:
                big_number(digits[i:])
                if sum(digits[i+1+len(digits[i:])%2:]) == 0 : 
                    break

    stringz = ' '.join(exp)
    return '\tDigits in the number - {}\n\tTotal digits - {}\n\t{}\n'.format(digits, len(digits), stringz)
    del stringz
    del exp

if __name__ == '__main__':
    fire.Fire(figures(int(input('\tEnter a number - '))))
