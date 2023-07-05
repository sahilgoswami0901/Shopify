from django.shortcuts import render
import mysql.connector as sql
i=10000
name=''
s=''
email=''
password=''
# Create your views here.

def loginconn(request):
    global name,email,password,i
    if request.method=="POST":
        mydb = sql.connect(
        host="localhost",
        user="root",
        password="Sahil$0901",
        database="shopify"
        )
        cursor=mydb.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Username":
                name=value
            if key=="sex":
                s=value
            if key=="Email":
                email=value
            if key=="Password":
                password=value
                i = i + 1
        
        c="select * from Customer where Customer_Name='{}' and Password='{}'".format(name, password)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        # request.session['u_email'] = em
        # request.session['u_name'] = fn

        if t==():
            return render(request, 'signup.html')
        else:
            # print('you are:', request.session.get('u_name'))
            return render(request, 'home.html')

    return render(request,'signup.html')