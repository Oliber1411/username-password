def user_pass(user, password):
    if len(user) == 6:
        if len(password) >= 8:
            print('Success!')
        else:
            print('DENIED! Please enter a password of 8 or more characters!')
    else:
        print('DENIED! Please enter a username which is EXACTLY 6 characters!')

