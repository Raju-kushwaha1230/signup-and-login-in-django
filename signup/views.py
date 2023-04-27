from django.shortcuts import render
import mysql.connector 
fn=''
ln=''
s=''
em=''
passwd=''
# Create your views here.
def signaction(request):
    global fn,ln,s,em,passwd
    if request.method=="POST":
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                        passwd="mighty@098",
                                        database="c9",
                                        auth_plugin='mysql_native_password'
                                            )

        cursor=mydb.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="firstname":              
                fn=value
            if key=="lastname":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                passwd=value
        
        c="insert into details Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,passwd)
        cursor.execute(c)
        mydb.commit()

    return render(request,'signup_page.html')
