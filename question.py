class Question:

    def __init__(self, q_list):
        self.q_no = 0
        self.score = 0
        self.question_list = q_list
        self.currrent_question = None

    def still_has_question(self):
        return self.q_no < len(self.question_list)

    def next_question(self):
        self.currrent_question = self.question_list[self.q_no]
        self.q_no+=1
        return self.currrent_question[0]
    def check_ans(self, user_ans):
        if user_ans == self.currrent_question[1]:
            self.score +=1
            return True
        else:
            return False
    def score(self):
        return self.score
    def question_number(self):
        return self.q_no