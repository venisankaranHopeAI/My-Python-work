class multiplefunccheck():
    def subfieldsinAI():
        lists=["Sub-fields in AI are:","Machine learning","Neural netwroks","Vision","Robotics","Speech processing","Natural langauage processing"]
        for temp in lists:
            print(temp)
    def OddEven():
        num=int(input("Enter the number:"))
        if(num%2==0):
            print(num, "is an Even number")
            message="Even number"
        else:
            print(num, "is an Odd number")
            message="Odd number"
        return message
    def eligibility():
        gender=input("Enter the gender:")
        age=int(input("Enter the age:"))
        if((gender=="male" and age>=21) or (gender=="female" and age>=18)):
            print("The person is eligible for marriage")
            message="Eligible"
        else:
            print("The person is not eligible for marriage")
            message="Not eligible"
        return message
    def percentage():
        sub1=int(input("Enter the mark for sub1:"))
        sub2=int(input("Enter the mark for sub2:"))
        sub3=int(input("Enter the mark for sub3:"))
        sub4=int(input("Enter the mark for sub4:"))
        sub5=int(input("Enter the mark for sub5:"))
        total=(sub1+sub2+sub3+sub4+sub5)
        percent=(total/5)
        print("The percentage:",percent)
        message="Percentage"
        return message
    def triangle():
        height1=int(input("Enter the height1:"))
        height2=int(input("Enter the height2:"))
        breadth=int(input("Enter the breadth:"))
        area=(height1*breadth)/2
        print("The area is:",area)
        perimeter=height1+height2+breadth
        print("The perimeter is:",perimeter)
        message="Area and Perimeter of a triangle"
        return message