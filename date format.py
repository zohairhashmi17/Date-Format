print('Zohair Hashmi')
print('18b-127-CS')
print('Program for checking dates with respect to given formats')
date_format=str(input("Enter the date format dd-mm-yy or mm-dd-yy, for dd-mm-yy enter first and for the second one enter second : "))
if date_format =='first':
    for char in range(11):
        date=input("Enter complete date: ")
        dd,mm,yy=date.split('-')
        dd=int(dd)
        mm=int(mm)
        yy=str(yy)
        if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
            max_days=31
        elif(mm==4 or mm==6 or mm==9 or mm==11):
            max_days=30
        elif(mm==2):
            max_days=28
        if(mm<1 or mm>12):
            print("Date is invalid,error in months.")
        elif (len(yy)>2):
            print('year is invalid as per the date format')
        elif(dd<1 or dd>max_days):
            print("Date is invalid,you have entered an invalid day.")
        else:
            print('Date is valid.')
else:
    for char in range(11):
        date=input("Enter the complete date : ")
        
        mm,dd,yy=date.split('-')
        dd=int(dd)
        mm=int(mm)
        yy=int(yy)
        if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
            max_days=31
        elif(mm==4 or mm==6 or mm==9 or mm==11):
            max_days=30
        elif(mm==2):
            max_days=28
        if(mm<1 or mm>12):
            print("Date is invalid,error in months.")
        elif(len(yy)>2):
            print('year is invalid as per the format')
        elif(dd<1 or dd>max_days):
            print("Date is invalid,you have entered an invalid day.")
        else:
            print('Date is valid.')
