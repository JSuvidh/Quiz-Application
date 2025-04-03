class account():

    admin_id = "quiz00"
    admin_password = "1234"

    def __init__(self,id,p):

        self.user_id = id
        self.password = p
        self.high_pythonmarks = 0
        self.high_sqlmarks = 0
        self.high_mememarks = 0

    def __str__(self):

        return self.user_id
    

    