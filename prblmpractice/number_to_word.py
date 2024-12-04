

ones=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fouteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]

tens=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]

def number_to_words(num):

    if num==0:

        return "Zero"
    
    def two_digits(num):

        if num<20:

            return ones[num]

        else :

            return tens[num//10]+ (" "+ ones[num%10] if num%10!=0 else "")
        
    def three_digits(num):

        if num<100:

            return two_digits(num)
        
        else:

            return ones[num//100]+ " Hundred" + (" and "+ two_digits(num%100)if num%100!=0 else " ")

    return three_digits(num)


num=int(input("Enter number:"))

print(number_to_words(num))