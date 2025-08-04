import customtkinter as ctk

class Invoice:
    def __init__(self, questionId, question_text, tags, source):
        self.questionId = questionId
        self.questionImage = "questionFiles/"+questionId+".png"
        self.question_text = question_text
        self.tags = tags
        self.source = source

