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
        #students = Student.objects.aggregate(count(request.POST['procedence_type'])).values(request.POST['procedence_type'])
        return HttpResponse(json.dumps({'exa_ext':exa_ext, 'cant':cant}), 'application/json')

def getICNEGraphData(request):
    if request.method == 'POST':
        student_goup = request.POST['grupo']
        period = request.POST['periodo']
        anio = request.POST['ano_cur']
        students = getFilteredData(student_goup, period, anio)
        cant = students.count()

        students8 = students.filter(icne__lte=800).count()
        students9 = students.filter(icne__gte=800).filter(icne__lte=900).count()
        students10 = students.filter(icne__gte=900).filter(icne__lte=1000).count()
        students11 = students.filter(icne__gte=1000).filter(icne__lte=1100).count()
        students12 = students.filter(icne__gte=1100).filter(icne__lte=1200).count()
        students13 = students.filter(icne__gte=1200).filter(icne__lte=1300).count()
        icne = [students8, students9, students10, students11, students12, students13]
        #students = Student.objects.aggregate(count(request.POST['procedence_type'])).values(request.POST['procedence_type'])
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