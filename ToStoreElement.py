emails=['abhi@gmail.com','abhir@yahoo.com','abhir@rediffmail.com','prathamesh@gmail.com','prathameshs@rediffmail.com'
        'abhirajurkar@gmail.com','prathameshsawant@gmail.com','prathamesh@yahoo.com','dadaddada','aabbccdd'
        ]

gmail=[]
yahoo=[]
rediff=[]
invalid=[]
for email in emails:
    if email.endswith('@gmail.com'):
        gmail.append(email)
        print(gmail)
    elif email.endswith('@rediffmail.com'):
        rediff.append(email)
        print(rediff)
    elif email.endswith('@yahoo.com'):
        yahoo.append(email)
        print(yahoo)
    else:
        invalid.append(email)    
        print(invalid)
     