from django.shortcuts import render
from events.models import customer
import mysql.connector

# for x in mycursor:
#    print(x)

# def home(request):
# 	return render(request, 'events/home.html', {})

def customerconn(request):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sahil$0901",
    database="shopify"
    )

    mycursor1 = mydb.cursor()
    mycursor1.execute("SELECT * FROM Customer")
    customers = mycursor1.fetchall()
    # for x in mycursor:
    #     print(x)

    return render(request,'index.html',{"customers":customers})

def wholesalersconn(request):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sahil$0901",
    database="shopify"
    )

    mycursor2 = mydb.cursor()
    mycursor2.execute("SELECT C.Customer_ID, C.Customer_Name, C.Gender, O.Cart_ID, O.Type_Of_Payment, O.Date_Of_Order FROM Customer AS C INNER JOIN Order_Cart AS O ON C.Customer_ID = O.Customer_ID")
    wholesalers = mycursor2.fetchall()
    
    return render(request, 'index2.html', {"wholesalers":wholesalers})
    
