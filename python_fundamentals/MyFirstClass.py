class Email:
    # constructor
    def __init__(self, email_header, email_body):
        self.header = email_header
        self.body = email_body
        # self is referring to the current 'instance' of the class

    def print_email_body(self):
        print(self.body)



e1 = Email("Greetings Joe", "Dear Joe, This is an email to inform you that you got fired on your first day!")
e2 = Email("You're fired marcus!", "Dear Marcus, We are firing everybody today!")

e1.print_email_body()