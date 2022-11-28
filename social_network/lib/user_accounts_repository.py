from lib.user_accounts import *

class UserAccountsRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from user_accounts')
        user_account_list = []
        for row in rows:
            item = UserAccounts(row['id'], row['username'], row['email_address'])
            user_account_list.append(item)
        
        return user_account_list


    def find(self, user_id):
        rows = self._connection.execute(
            "SELECT * FROM user_accounts WHERE id = %s", [user_id]
        )
        row = rows[0]
        return UserAccounts(row["id"], row["username"], row["email_address"])

    def create(self, username, email_address):
        self._connection.execute(
        "INSERT INTO user_accounts (username, email_address) VALUES (%s, %s)", [username, email_address])
        return None
        
    def delete(self, user_id):
        self._connection.execute(
        "DELETE FROM user_accounts WHERE id = %s", [user_id])
        return None

