students = {
    'Popov': ["A", "B", "A-"],
    'Yesmukhanov': ["B-", "D", "C-"],
    'Shamoi': ["A", "A", "A"],
    'Akshabaev': ["B", "B", "B"]
}

for name, l in students.items():
    GPA = 0
    for grade in l:
        if grade == "A":
            GPA = GPA+4
        elif grade == "A-":
            GPA = GPA+3.67
        elif grade == "B+":
            GPA = GPA+3.33
        elif grade == "B":
            GPA = GPA+3
        elif grade == "B-":
            GPA = GPA+2.67
        elif grade == "C+":
            GPA = GPA+2.33
        elif grade == "C":
            GPA = GPA+2
        elif grade == "C-":
            GPA = GPA+1.67
        elif grade == "D+":
            GPA = GPA+1.33
        elif grade == "D":
            GPA = GPA+1
    GPA = GPA / len(l)
    if GPA > 3:
        print(name)


# students = {
#     'Popov': ["A", "B", "A-"],
#     'Yesmukhanov': ["B-", "D", "C-"],
#     'Shamoi': ["A", "A", "A"],
#     'Akshabaev': ["B", "B", "B"]
# }
# with open('gpa_table.txt','r') as file:
#     line=file.readlines()

# for name, l in students.items():
#     GPA = 0
#     for grade in l:
#         if grade == "A":
#             GPA = GPA + 4
#         elif grade == "A-":
#             GPA = GPA+3.67
#         elif grade == "B+":
#             GPA = GPA+3.33
#         elif grade == "B":
#             GPA = GPA+3
#         elif grade == "B-":
#             GPA = GPA+2.67
#         elif grade == "C+":
#             GPA = GPA+2.33
#         elif grade == "C":
#             GPA = GPA+2
#         elif grade == "C-":
#             GPA=GPA+1.67
#         elif grade == "D":
#             GPA=GPA+1



#     GPA = GPA / len(l)
#     if GPA > 3:
#         print(name)