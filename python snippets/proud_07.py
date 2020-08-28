from class4quiz import question

questions_prompts =[
    "Who won the UEFA Champions League the most often?\n(a) AC Milan \n(b) FC Liverpool \n(c) Real Madrid \n\n",
    "Who won the UEFA Champions League last year - Season 2018/19? \n(a) AC Milan \n(b) FC Liverpool \n(c) Real Madrid \n\n",
    "Which team is the best?\n(a) AC Milan \n(b) FC Liverpool \n(c) Real Madrid \n\n"
]

question_objects = [
    question(questions_prompts[0],"c"),
    question(questions_prompts[1],"b"),
    question(questions_prompts[2],"a"),
]

def run_quiz(question_objects):
    score = 0
    for question in question_objects:
        answer = input(question.p)
        if answer == question.a:
            score += 1
    print("You got " + str(score) + "/" + str(len(question_objects)) + " correct.")


run_quiz(question_objects)