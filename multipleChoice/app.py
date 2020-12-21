from multipleChoice.Questions import Question
questions_prompt = [
    "What color are apples?\na) Red\nb) Green\nc)Purple\n\n",
    "What color are Banana?\na) Red\nb) Yellow\nc) Blue\n\n",
    "What color are Mango?\na) Green\nb) Black\nc) Yellow\n\n"
]

questions = [
    Question(questions_prompt[0], "a"),
    Question(questions_prompt[1], "b"),
    Question(questions_prompt[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)))

run_test(questions)