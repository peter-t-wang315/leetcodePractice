def find_student_mentors(list_students):
    righti = len(list_students)-1
    lefti = len(list_students)-2
    sorted_students = list_students.copy()
    sorted_students.sort()
    student_mentor_dict = {}

    if(righti >= 1):
        student_mentor_dict[sorted_students[righti]] = sorted_students[lefti]
    while lefti >= 0 and righti >= 0:
        if sorted_students[righti]/2 <= sorted_students[lefti]:
            student_mentor_dict[sorted_students[lefti]] = sorted_students[righti]
            lefti-=1
        else:
            righti-=1
        
        if righti == lefti:
            lefti-=1
            if lefti >=0:
                student_mentor_dict[sorted_students[righti]] = sorted_students[lefti]
        
    for i in range(len(list_students)):
        list_students[i] = student_mentor_dict.get(list_students[i], -1)
    
    return list_students
    


if __name__ == "__main__":
    print(find_student_mentors([3,7,9,4,8,9,1]))

