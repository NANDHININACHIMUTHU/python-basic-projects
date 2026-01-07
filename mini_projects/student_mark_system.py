no=int(input("Enter the number of students:"))
subjects=['tamil','english','maths','science','social']

for i in range(no):
    print(f"\n--- Student {i+1} ---")
    name=input(f"Enter the {i+1} student name:")
    marks=[]
    fail=False
    for sub in subjects:
        m=int(input(f"enter the {sub} marks:"))
        marks.append(m)
        if m<35:
            fail=True
    total=sum(marks)
    avg=total/len(subjects)
    if avg>=90: 
        grade="A+"
    elif avg>=80:
        grade="A"
    elif avg>=70:
        grade="B"
    elif avg>=60:
        grade="C"
    elif avg>=50:
        grade="D"
    else:
        grade="FAIL"



    print("The student name:", name)
    print("student marks:", marks)
    print("Student total:", total)
    print("Student avgerage: ", avg)
    print("student grade:",grade)
    if fail:
        print("RESULT:FAIL")
    else:
        print("RESULT:PASS")

