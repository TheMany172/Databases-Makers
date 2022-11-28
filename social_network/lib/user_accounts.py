class UserAccounts():
    def __init__(self, id, username, email_address):
        self.id = id
        self.username = username
        self.email_address = email_address

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"UserAccounts({self.id}, {self.username}, {self.email_address})"