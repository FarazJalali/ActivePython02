#second_session

print('write username:   ')
username = input()
print('write password:   ')
passw = input()

print( "username: " + username)
print( "password: " + passw)

#write your username and get password
print('write your user name: ')
a = input()
if a == username:
    print('password: ', passw)
else:
    print('username is not match')
input()