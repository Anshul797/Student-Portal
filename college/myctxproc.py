from college.models import Student

st = None
def set_st(s1):
    global st
    st = s1
def ctxproc(request):
    st = None
    stList = Student.objects.filter(user=request.user.id)
    if len(stList)>0:
        st = stList[0]
    return {'student': st}