import smtplib

server =  smtplib.SMTP('smtp.gmail.com', 465)

server.ehlo()

server.login('yvan.thrimawithana@gmail.com', 'qwertyuivjivdividvndivnddvdivi1234567876543f fbnifgiginf#######$$%^&*gsvdvs&&^$')

print('Login Successful')