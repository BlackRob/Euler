year = 1901
# given start date is mon, jan 1, 1900;
# make things simpler by moving to first sunday, the seventh
m = 0   # month, index for months
months = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")
day = 6 # actual calendar day number 
fmsundays = 0

while year < 2001:
    #adjust day for next sunday
    day = day + 7

    # if day is greater than days in month, adjust month
    # february
    if m==1:
        # check if leap year
        if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
            if day > 29:
                m = m + 1
                day = day % 29
        else:   # not a leap year
            if day > 28:
                m = m + 1
                day = day % 28
        if day == 1 or day == 0:
            fmsundays += 1
            print(str(year) + " " + months[m] + " " + str(day))
        continue
    # months with 30 days
    elif m==3 or m==5 or m==8 or m==10:
        if day > 30:
            m = m + 1
            day = day % 30
        if day == 1 or day == 0:
            fmsundays += 1
            print(str(year) + " " + months[m] + " " + str(day))
        continue
    # other months (31 days)
    else:
        if day > 31:
            m = m + 1
            day = day % 31
        if m == 12:
            year += 1
            m = 0 
        if day == 1 or day == 0:
            fmsundays += 1
            print(str(year) + " " + months[m] + " " + str(day))
    
   

print(fmsundays)