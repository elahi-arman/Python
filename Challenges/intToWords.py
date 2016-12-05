
# Managed Dictionaries
number_suffixes = ["ten", "hundred", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]
hyphenated_begginings = {0: None, 1:"ten", 2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
teens = {11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
ones = {0: None, 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}


# Given a group of three digits, translates that three digit entity as a single unit
def translateThree(digits):

    translated = ""
    _digits = digits        #method is desctrucive, so don't taint data

    #parse the hundreds digit of this group
    hundreds = ones[_digits/100]
    tens_digits = _digits % 100

    #check the ones place
    if tens_digits%10 != 0:
        #tens place doesn't require hyphenation
        if tens_digits < 20:
            if tens_digits < 10:
                tens = ones[tens_digits%10]
            else:
                tens = teens[tens_digits]
        else:
            tens = hyphenated_begginings[tens_digits/10] + "-" + ones[tens_digits%10]
    else:
        #ones place is zero
        tens = hyphenated_begginings[tens_digits/10]

    if hundreds:
        translated += hundreds + " hundred "

    if tens:
        translated += tens

    print translated

#chunks a number into groups of three
def chunkThree(number):
    _number


translateThree(300)
