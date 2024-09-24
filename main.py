labs_completed_data = int(input("Enter the number of labs completed: "))
quizzes_completed_data = int(input("Enter the number of quizzes completed: "))
assignment_1_grade_data = int(input("Enter the grade for Assignment 1 (%): "))
assignment_2_grade_data = int(input("Enter the grade for Assignment 2 (%): "))
assignment_3_grade_data = int(input("Enter the grade for Assignment 3 (%): "))
assignment_4_grade_data = int(input("Enter the grade for Assignment 4 (%): "))
mid_term_1_grade_data = int(input("Enter the grade for Midterm 1 (%): "))
mid_term_2_grade_data = int(input("Enter the grade for Midterm 2 (%): "))
final_exam_grade_data = int(input("Enter the grade for the Final Exam (%): "))
midterms_final_prep_grade_data = int(input("Enter grade for Midterms and Final Preparation (%): "))

total_labs = 6
total_quizzes = 6

if labs_completed_data > total_labs:
    total_labs = labs_completed_data
if quizzes_completed_data > total_quizzes:
    total_quizzes = quizzes_completed_data

def calculate_final_grade(
        labs_completed: int,
        quizzes_completed: int,
        assignment_1_grade: int,
        assignment_2_grade: int,
        assignment_3_grade: int,
        assignment_4_grade: int,
        mid_term_1_grade: int,
        mid_term_2_grade: int,
        final_exam_grade: int,
        midterms_final_prep_grade: int
) -> float:
    labs_weight = 0.2
    quizzes_weight = 0.15
    assignment_weight = 0.04
    midterms_weight = 0.125
    final_exam_weight = 0.18
    midterms_final_prep_weight = 0.06

    labs_grade_weighted = (labs_completed / total_labs) * 100 * labs_weight
    quizzes_grade_weighted = (quizzes_completed / total_quizzes) * 100 * quizzes_weight
    assignment_1_grade_weighted = assignment_1_grade * assignment_weight
    assignment_2_grade_weighted = assignment_2_grade * assignment_weight
    assignment_3_grade_weighted = assignment_3_grade * assignment_weight
    assignment_4_grade_weighted = assignment_4_grade * assignment_weight
    mid_term_1_grade_weighted = mid_term_1_grade * midterms_weight
    mid_term_2_grade_weighted = mid_term_2_grade * midterms_weight
    final_exam_grade_weighted = final_exam_grade * final_exam_weight
    midterms_final_prep_grade_weighted = midterms_final_prep_grade * midterms_final_prep_weight

    final_grade_result = labs_grade_weighted + quizzes_grade_weighted + assignment_1_grade_weighted + assignment_2_grade_weighted + assignment_3_grade_weighted + assignment_4_grade_weighted + mid_term_1_grade_weighted + mid_term_2_grade_weighted + final_exam_grade_weighted + midterms_final_prep_grade_weighted

    return final_grade_result

final_grade_data = calculate_final_grade(
    labs_completed_data,
    quizzes_completed_data,
    assignment_1_grade_data,
    assignment_2_grade_data,
    assignment_3_grade_data,
    assignment_4_grade_data,
    mid_term_1_grade_data,
    mid_term_2_grade_data,
    final_exam_grade_data,
    midterms_final_prep_grade_data
)

final_grade = round(final_grade_data, 2)

print(f"Your grade is: {final_grade}%")