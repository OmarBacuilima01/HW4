import sqlite3


#Set Database
conn = sqlite3.connect('test_database.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                    user_ID TEXT PRIMARY KEY,
                    password TEXT
                )''')

conn.commit()


def add_user(user_ID, password):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (user_ID, password) VALUES (?, ?)", (user_ID, password))
        conn.commit()
        print('User: ', user_ID, 'ADDED TO DATABASE')
        return True
    except sqlite3.Error as e:
        print("Error adding user:", e)  # Log the specific error message for debugging
        print('UserID Already Taken')
        return False



def authenticate(user, password):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE user_ID=?", (user,))
        found_user = cursor.fetchone()

        print("User Entered:", user, "Password Entered:", password)
        print("User Found:", found_user)

        if found_user and found_user[1] == password:  # Check if user and password match
            return True
        else:
            return False
    except sqlite3.Error as e:
        print("Error authenticating user:", e)
        return False

    
#INPUT THE USER ID AND PASSWORD
#Test add_user function
print('ADD USER TO DATABASE')
user_input_id = input('Please Type a userID: ')
user_input_password = input('Please Type a password: ')
add_user(user_input_id, user_input_password)
print('')




