students={}


SYSTEM_INFO = ("Edify Technologies", "Student Management System","v1")
ADMIN_INFO = ("9090880","admin@edify.com")

#menu
while True:
    print("choose an option:")
    print("1-Add student")
    print("2-update student")
    print("3-Delete student")
    print("4-list student")
    print("5-Exit system")

    choice=input("enter your choice(1-5):")
    if choice=="1":
        print("Adding  Input Logic")
        student_id=input("enter student id:")
        if student_id in students:
            print("student_id is already exists in system")
        else:
            name=input("enter your name:").title()
        #list of score
            scores=[]
            while True:
                score_input = input("Enter Score or type done: ")
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0 <= score <=100:
                        scores.append(score)
                    else:
                        print("Score Should be 0-100 ")
                else:
                    print("Score Should Numbers Only")
            
            # set for skills
            skills = set()
            while True:
                skill_input = input("Enter Skill or type done: ")
                if skill_input == "done":
                    break
                skills.add(skill_input.title())
            
            # save the student details
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            print("Student Saved")
            
            # for our confirmation
            print(students)
    elif choice =="2":
        print("updating student Logic")
        if student_id in students:
            new_name=input("enter a new name:").title()
            students[student_id]["name"]=new_name
            print("students name updated")
        else:
            print("Id doesn't exist to update")
        print(students)

    elif choice=="3":
        print("Deleting student Logic")
        student_id=input("enter id to remove:")
        if student_id in students:
            remove=students.pop(student_id)
            print(remove)
        else:
            print("ID doesn't exist to delete")
        print(students)
    elif choice=="4":
        
        print("Listing Students Logic")
        for sid, data in students.items():
            name = data["name"]
            scores = data["scores"]
            
            avg = sum(scores)/len(scores)
            high_score = max(scores)
            low_score = min(scores)
            
            skills = data["skills"]
            skills_count = len(skills)
            
            print("="*50)
            print("STUDENT DETAILS")
            print("="*50)
            
            print(f"ID: {sid}")
            print(f"NAME: {name}")
            print(f"ALL SCORES: {scores}")
            print(f"AVG SCORE: {avg}")
            print(f"HIGH SCORE: {high_score}")
            print(f"LOWEST SCORE: {low_score}")
            print(f"ALL SKILLS: {skills}")
            print(f"NO OF SKILLS: {skills_count}")


    elif choice == "5":
        print("Exit System")
        print("="*50)
        print("CONTACT ADMIN FOR MORE INFORMATION")
        print(f"ADMIN CONTACT NO: {ADMIN_INFO[0]}")
        print(f"ADMIN EMAIL ID: {ADMIN_INFO[1]}")
        print("="*50)
        break
    else:
        print("Invalid Option, Only Select (1-5)")   



