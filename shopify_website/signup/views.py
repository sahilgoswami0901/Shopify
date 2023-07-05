from django.shortcuts import render
import mysql.connector as sql
i=10000
name=''
s=''
email=''
password=''
# Create your views here.
def signupconn(request):
    global name,s,email,password,i
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
        
        c="insert into Customer Values('{}','{}','{}','{}')".format(i, name, email, password)
        cursor.execute(c)
        mydb.commit()

    return render(request,'signup.html')