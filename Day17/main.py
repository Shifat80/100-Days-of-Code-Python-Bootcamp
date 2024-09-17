from question_model import quiz
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=quiz(question_text,question_answer)
    question_bank.append(new_question)


Quiz=QuizBrain(question_bank)


while Quiz.still_has_question():
    Quiz.next_question()
    
    
    