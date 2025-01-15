from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .models import User,Teacher,Student
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'index1.html')
def loged(request):
    if request.method == 'POST':
        un = request.POST['sname']
        pwd = request.POST['spwd']
        x = authenticate(request,username =un , password = pwd)
        if x is not None and x.is_superuser == 1:
            login(request,x)
            request.session['a_id'] = x.id 
            return redirect(admin)
        elif x is not None and x.usertype == 'student' and x.is_approved == "1":
            login(request,x)
            request.session['s_id'] = x.id
            return redirect(studenthome)
        elif x is not None and x.usertype == 'student' and x.is_approved == "0":
            return HttpResponse("You are not approved by admin")
        elif x is not None and x.usertype == 'teacher':
            login(request,x)
            request.session['t_id'] = x.id
            return redirect(teacherhome)
        else:
            return HttpResponse("Invalid username or password")
    else:
        return render(request,'login.html')
@login_required
def admin(request):
    return render(request,'adminhome.html')

def addteacher(request):
    if request.method == 'POST':
        firstna = request.POST['fname']
        lastna = request.POST['lname']
        userna = request.POST['uname']
        email = request.POST['email']
        cpwd = request.POST['pwd']
        cnfpwd = request.POST['cpwd']
        if cpwd == cnfpwd:
            u = User.objects.create_user(username = userna,password = cpwd,usertype = 'teacher')
            x = Teacher.objects.create(teach = u,firstname = firstna,lastname = lastna,username = userna,emailid = email,password = cpwd)
            x.save()
            return redirect(addteacher)
    else:
        return render(request,'addteacher.html')
def viewteacher(request):
    data = Teacher.objects.all()
    return render(request,'viewteacher.html',{'val':data})
def studregistration(request):
    if request.method == 'POST':
        na = request.POST['fname']
        ag = request.POST['age']
        dep = request.POST['dept']
        ph = request.POST['phone']
        em = request.POST['email']
        user = request.POST['uname']
        spwd = request.POST['pwd']
        scpwd = request.POST['cpwd']
        if spwd == scpwd:
            su = User.objects.create_user(username = user,password = spwd,usertype = 'student',is_approved = "0")
            sx = Student.objects.create(stud = su,name = na,age = ag,
                department = dep,phoneno = ph,emailad = em,studuser = user,studpwd = spwd)
            sx.save()
           
            return redirect(loged)
        else:
            return HttpResponse('Password mismatch')
    else:
        return render(request,'studregister.html')
def studapproval(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        s = User.objects.get(id = user_id)
        s.is_approved = "1"
        s.save()
        return redirect(studapproval)
        # return HttpResponse("approve clicked")
    else:
        student  = User.objects.filter(usertype = 'student',is_approved = "0")
        return render(request,'approvestudent.html',{'value':student})
def studreject(request):
    if request.method == 'POST':
        userid = request.POST['us_id']
        sr = User.objects.get(id = userid)
        srs = Student.objects.get(stud_id = userid)
        srs.delete()
        sr.delete()
        return redirect(studapproval)
@login_required
def studenthome(request):
    stid = request.session['s_id']
    studda = Student.objects.get(stud_id = stid)
    return render(request,'studenthome.html',{'val':studda})
@login_required
def teacherhome(request):
    teachid = request.session['t_id']
    teachda = Teacher.objects.get(teach_id = teachid)
    return render(request,'teacherhome.html',{'val':teachda})

def studentview(request):
    studdata = Student.objects.all()
    return render(request,'studentview.html',{'val':studdata})
def teacheredit(request,id):
    ed = Teacher.objects.get(id = id)
    return render(request,'updateteacher.html',{'val':ed})
def updateteacher(request,id):
    if request.method == 'POST':
        ufna = request.POST['fname']
        ulna = request.POST['lname']
        uuser = request.POST['uname']
        uem = request.POST['email']
        upwd = request.POST['pwd']
        ucpwd = request.POST['cpwd']
        if upwd == ucpwd:
            old = Teacher.objects.get(id = id)
            old.firstname = ufna
            old.lastname = ulna
            old.username = uuser
            old.emailid = uem
            old.password = upwd
            old.teach.username = uuser
            old.teach.set_password(upwd)
            old.save()
            old.teach.save()
        return redirect(viewteacher)
def delteteacher(request,id):
    delte = Teacher.objects.get(id = id)
    delte.teach.delete()
    delte.delete()
    return redirect(viewteacher)
def editstudent(request,id):
    edstud = Student.objects.get(id = id)
    return render(request,'updatestudent.html',{'val':edstud})
def updatestudent(request,id):
    if request.method == 'POST':
        una = request.POST['fname']
        uage = request.POST['age']
        udept = request.POST['dept']
        uph = request.POST['phone']
        uem = request.POST['email']
        uuna = request.POST['uname']
        upwd = request.POST['pwd']
        ucpwd = request.POST['cpwd']
        if upwd == ucpwd:
            old_data = Student.objects.get(id = id)
            old_data.name = una
            old_data.age = uage
            old_data.phoneno = uph
            old_data.department = udept
            old_data.emailad = uem
            old_data.studuser = uuna
            old_data.studpwd = upwd
            old_data.stud.username = uuna
            old_data.stud.set_password(upwd)
            old_data.save()
            old_data.stud.save()
        return redirect(studentview)
def deltestudent(request,id):
    de = Student.objects.get(id = id)
    de.stud.delete()
    de.delete()
    return redirect(studentview)
def logouts(request):
    logout(request)
    return redirect(home)
def profileview(request,id):
    if request.method == 'POST':
        user_id = request.POST['viewid']
        stdata = Student.objects.get(id = user_id)
        return render(request,'studentprofile.html',{'prof':stdata})
def teacherprofileview(request,id):
    if request.method == 'POST':
        user_id = request.POST['tviewid']
        teachda = Teacher.objects.get(id = user_id)
        return render(request,'teacherprofile.html',{'tprof':teachda})
def editstudprofile(request,id):
    if request.method == 'POST':
        edstda = Student.objects.get(id = id)
        return render(request,'updstudprofile.html',{'edprs':edstda})
def editteachprofile(request,id):
    if request.method == 'POST':
        edteachda = Teacher.objects.get(id = id)
        return render(request,'updteachprofile.html',{'tedprs':edteachda})
def updstudprof(request,id):
    if request.method == 'POST':
        ena = request.POST['fname']
        eage = request.POST['age']
        edept = request.POST['dept']
        eph = request.POST['phone']
        eem = request.POST['email']
        oldstuddata = Student.objects.get(id = id)
        oldstuddata.name = ena
        oldstuddata.emailad = eem
        oldstuddata.age = eage
        oldstuddata.department = edept
        oldstuddata.phoneno = eph
        oldstuddata.save()
        return redirect(studenthome)
def updteachprof(request,id):
    if request.method == 'POST':
        efna = request.POST['fname']
        elna = request.POST['lname']
        eem = request.POST['email']
        oldteachdata = Teacher.objects.get(id = id)
        oldteachdata.firstname = efna
        oldteachdata.lastname = elna
        oldteachdata.emailid = eem
        oldteachdata.save()
        return redirect(teacherhome)
def viewstudteacher(request):
    studteach = Teacher.objects.all()
    return render(request,'viewstudteacher.html',{'val':studteach})
def viewteachstud(request):
    teachstud = Student.objects.all()
    return render(request,'viewteachstud.html',{'val':teachstud})
