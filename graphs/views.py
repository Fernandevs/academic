from cProfile import label
from django.shortcuts import render

# Create your views here.
from django.db.models import Count
from django.shortcuts import render, HttpResponse
from students.models import Student
import json

# Create your views here.
def graphs(request):
    return render(request, 'graphs/graph.html')

def getSchoolModalityGraphData(request):
    if request.method == 'POST':
        student_goup = request.POST['grupo']
        period = request.POST['periodo']
        anio = request.POST['ano_cur']
        students = getFilteredData(student_goup, period, anio)
        cant = students.count()

        students1 = students.filter(mod_bac=1).count()
        students2 = students.filter(mod_bac=2).count()
        students3 = students.filter(mod_bac=3).count()
        students4 = students.filter(mod_bac=4).count()
        students5 = students.filter(mod_bac=5).count()
        students6 = students.filter(mod_bac=6).count()
        students7 = students.filter(mod_bac=7).count()
        students8 = students.filter(mod_bac=8).count()
        mod_bac = [students1, students2, students3, students4, students5, students6, students7, students8]
        
        return HttpResponse(json.dumps({'mod_bac':mod_bac, 'cant':cant}), 'application/json')


def getSchoolRegimeGraphData(request):
    if request.method == 'POST':
        student_goup = request.POST['grupo']
        period = request.POST['periodo']
        anio = request.POST['ano_cur']
        students = getFilteredData(student_goup, period, anio)
        cant = students.count()

        students1 = students.filter(reg_proc=1).count()
        students2 = students.filter(reg_proc=2).count()
        students3 = students.filter(reg_proc=3).count()

        reg_proc = [students1, students2, students3]
        return HttpResponse(json.dumps({'reg_proc':reg_proc, 'cant':cant}), 'application/json')

def getSchoolProcedenceGraphData(request):
    if request.method == 'POST':
        student_goup = request.POST['grupo']
        period = request.POST['periodo']
        anio = request.POST['ano_cur']
        students = getFilteredData(student_goup, period, anio)
        cant = students.count()

        students = students.values('nom_proc').order_by('nom_proc').annotate(count=Count('nom_proc'))
        labels = []
        procedence =[]
        for row in students:
            labels.append(row['nom_proc'])
            procedence.append(row['count'])
        labels[0] = 'DESCONOCIDO' if labels[0] == '' else labels[0]

        return HttpResponse(json.dumps({'procedence':procedence, 'cant':cant, 'labels':labels}), 'application/json')

def getProcedenceGraphData(request):
    if request.method == 'POST':
        student_goup = request.POST['grupo']
        period = request.POST['periodo']
        anio = request.POST['ano_cur']
        students = getFilteredData(student_goup, period, anio)
        cant = students.count()

        students = students.values('ciu_proc').order_by('ciu_proc').annotate(count=Count('ciu_proc'))
        labels = []
        procedence =[]
        for row in students:
            labels.append(row['ciu_proc'])
            procedence.append(row['count'])
        labels[0] = 'DESCONOCIDO' if labels[0] == '' else labels[0]

        return HttpResponse(json.dumps({'procedence':procedence, 'cant':cant, 'labels':labels}), 'application/json')


def getExaExtGraphData(request):
    if request.method == 'POST':
        student_goup = request.POST['grupo']
        period = request.POST['periodo']
        anio = request.POST['ano_cur']
        students = getFilteredData(student_goup, period, anio)
        cant = students.count()

        students1 = students.filter(exa_ext=1).count()
        students2 = students.filter(exa_ext=2).count()
        students3 = students.filter(exa_ext=3).count()
        students4 = students.filter(exa_ext=4).count()
        students5 = students.filter(exa_ext=5).count()
        students6 = students.filter(exa_ext=6).count()
        students7 = students.filter(exa_ext=7).count()
        exa_ext = [students1, students2, students3, students4, students5, students6, students7]
        return HttpResponse(json.dumps({'exa_ext':exa_ext, 'cant':cant}), 'application/json')

def getFailedSubjectsGraphData(request):
    if request.method == 'POST':
        student_goup = request.POST['grupo']
        period = request.POST['periodo']
        anio = request.POST['ano_cur']
        students = getFilteredData(student_goup, period, anio)
        cant = students.count()

        students1 = students.filter(mat_rep=1).count()
        students2 = students.filter(mat_rep=2).count()
        students3 = students.filter(mat_rep=3).count()
        students4 = students.filter(mat_rep=4).count()
        students5 = students.filter(mat_rep__gte=5).count()
        mat_rep = [students1, students2, students3, students4, students5]
        return HttpResponse(json.dumps({'mat_rep':mat_rep, 'cant':cant}), 'application/json')

def getICNEGraphData(request):
    if request.method == 'POST':
        student_goup = request.POST['grupo']
        period = request.POST['periodo']
        anio = request.POST['ano_cur']
        students = getFilteredData(student_goup, period, anio)
        cant = students.count()

        students8 = students.filter(icne__lte=799).count()
        students9 = students.filter(icne__gte=800).filter(icne__lte=899).count()
        students10 = students.filter(icne__gte=900).filter(icne__lte=999).count()
        students11 = students.filter(icne__gte=1000).filter(icne__lte=1099).count()
        students12 = students.filter(icne__gte=1100).filter(icne__lte=1199).count()
        students13 = students.filter(icne__gte=1200).filter(icne__lte=1300).count()
        icne = [students8, students9, students10, students11, students12, students13]

        return HttpResponse(json.dumps({'icne':icne, 'cant':cant}), 'application/json')

def getFilteredData(student_goup, period, anio):
    students = Student.objects.all() 
    if student_goup == '0':
        students = students.filter(egreso=0)
    elif student_goup == '1':
        students = students.filter(egreso=1).filter(degree=0)
    elif student_goup == '2':
        students = students.filter(degree=1)   

    if period == '0':
        students = students.filter(ingreso=0)
    elif period == '1':
        students = students.filter(ingreso=1)  
    
    if anio != '0':
        students = students.filter(year=anio)
    return students