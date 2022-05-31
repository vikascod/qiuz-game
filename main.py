permission = input('Do you wanna play a Quiz game type (Y/N) : ').lower()

if permission == 'y':
    name = input("Enter your name : ")
    print("Welcome", name, "to an amazing quiz game")

    quiz = '''What is the full form of HTTP.
    a. HyperText Transaction Permission
    b. HyperText Transfer Permission
    c. HyperText Transfer Protocal
    d. HyperText Transport Protocol'''
    info = 'you can type you answer in series name or full answer'
    print(info)
    print(quiz)
    answer = input('Enter : ')
    if answer == 'a':
        print('Incorrect')
    elif answer == 'b':
        print('Incorrect')
    elif answer == 'c' or 'HyperText Transaction Permission':
        print('Correct')
    elif answer == 'd':
        print('Incorrect')

elif permission == 'n':
    print('Okey')
    quit()
else:
    print('Invalid option')