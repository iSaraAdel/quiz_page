from Question import Question

print('choose the correct terminology for the definition')

question_prompts =[
  'An attribute of data that describes a values it can have and how the can be used?\n(a) Data type\n(b) Data structure\n(c) Database\n\n',
  'Data conversion process?\n(a) Object\n(b) collision\n(c) Hashing\n\n',
  'Anytime two inputs produce the same hash value?\n(a) ASCII\n(b) collision\n(c) array\n\n'
]

questions = [
    Question(question_prompts[0], 'a')
    Question(question_prompts[1], 'c')
    Question(question_prompts[2], 'b')
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
          score += 1
    print('You got ' + str(score) + '/' + str(len(questions)) + 'correct')
    
    
run_quiz(questions)
          
          

