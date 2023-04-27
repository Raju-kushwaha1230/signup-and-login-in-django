from django.shortcuts import render
import mysql.connector
em=''
passwd=''
# Create your views here.
def loginaction(request):
    global em,passwd
    if request.method=="POST":
        mydb=mysql.connector.connect(host="localhost",
                           user="root",
                           passwd="mighty@098",
                           database='c9',
                           auth_plugin="mysql_native_password"
                           )
        cursor=mydb.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                passwd=value
        
        c="select * from details where email='{}' and password='{}'".format(em,passwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
             return render(request,'error.html')
        else:
            return render(request,"welcome.html")

    return render(request,'login_page.html')
