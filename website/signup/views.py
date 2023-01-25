from django.shortcuts import render
import mysql.connector as sql

name = '' #  Nome
em = '' # Email
pwd = '' # Senha

def signaction(request):

    global name, em, pwd

    if request.method=="POST":
        m = sql.connect(host="localhost", user="root", passwd="1234", database="website")   

        cursor = m.cursor()
        
        d = request.POST

        for key, value in d.items():
            if key == "name":
                name = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value
        
        c = "insert into users Values('{}', '{}', '{}')".format(name, em, pwd)

        cursor.execute(c)

        m.commit()
    
    return render(request, 'signup_page.html')


def sobre(request):
    return render(request, 'sobre.html')