from django.urls import path
from myapp import views
# from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',views.home,name="home"),
    path('log',views.loged,name='loged'),
    path('admin',views.admin,name='admin'),
    path('reg',views.addteacher,name='addteacher'),
    path('view',views.viewteacher,name='viewteacher'),
    path('studreg',views.studregistration,name="studregistration"),
    path('studapp',views.studapproval,name="studapproval"),
    path('studhome',views.studenthome,name="studenthome"),
    path('studrej',views.studreject,name="studreject"),
    path('studview',views.studentview,name="studentview"),
    path('edit/<int:id>',views.teacheredit,name="teacheredit"),
    path('updteacher/<int:id>',views.updateteacher,name="updateteacher"),
    path('delete/<int:id>',views.delteteacher,name="delteteacher"),
    path('ed/<int:id>',views.editstudent,name="editstudent"),
    path('updstudent/<int:id>',views.updatestudent,name="updatestudent"),
    path('del/<int:id>',views.deltestudent,name="deltestudent"),
    path('lout',views.logouts,name="logouts"),
    path('profileview/<int:id>',views.profileview,name="profileview"),
    path('edpr/<int:id>',views.editstudprofile,name="editstudprofile"),
    path('updpr/<int:id>',views.updstudprof,name="updstudprof"),
    path('studteach',views.viewstudteacher,name="viewstudteacher"),
    path('teachome',views.teacherhome,name="teacherhome"),
    path('teachproview/<int:id>',views.teacherprofileview,name="teacherprofileview"),
    path('tedpr/<int:id>',views.editteachprofile,name="editteachprofile"),
    path('updtpr/<int:id>',views.updteachprof,name="updteachprof"),
    path('teachstud',views.viewteachstud,name="viewteachstud"),
    # path('logined/', LoginView.as_view(template_name='adminhome.html'), name='logined'),
]