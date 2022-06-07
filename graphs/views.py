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
        print(request.POST)
        student_goup = request.POST['grupo']
        if student_goup == '1':
            students = Student.objects.filter(ingreso__in=[0,1]).annotate(cantidad=Count('matricula'))
            #students = Student.objects.aggregate(count(request.POST['procedence_type'])).values(request.POST['procedence_type'])
            print(json.dumps(students))
            return HttpResponse(json.dumps(students), 'application/json')
        else:
            print("ayyyy")
            students = Student.objects.filter(ingreso__in=[0,1]).values().annotate(cantidad=Count('matricula')).values_list('cantidad')
            #students = Student.objects.aggregate(count(request.POST['procedence_type'])).values(request.POST['procedence_type'])
            print(students)
            print(json.dumps(list(students)))
            return HttpResponse(json.dumps(list(students)), 'application/json')\

def getExaExtGraphData(request):
    if request.method == 'POST':
        print(request.POST)
        student_goup = request.POST['grupo']
        period = request.POST['periodo']
        anio = request.POST['ano_cur']
        students = Student.objects.all()
        
        if student_goup == '0':
            students = students.filter(egreso=0)
        elif student_goup == '1':
            students = students.filter(egreso=1) 
        elif student_goup == '2':
            students = students.filter(titulado=1)   

        if period == '0':
            students = students.filter(ingreso__in=[0,1])
        elif period == '2':
            students = students.filter(ingreso=2)  
        if period == '0':
            students = students.filter(ingreso__in=[0,1])
        
        if anio != '0':
            students = students.filter(ano_cur=anio)
        cant = students.count()

        print(students)
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
        print(request.POST)
        student_goup = request.POST['grupo']
        period = request.POST['periodo']
        anio = request.POST['ano_cur']
        students = Student.objects.all()
        
        if student_goup == '0':
            students = students.filter(egreso=0)
        elif student_goup == '1':
            students = students.filter(egreso=1) 
        elif student_goup == '2':
            students = students.filter(titulado=1)   

        if period == '0':
            students = students.filter(ingreso__in=[0,1])
        elif period == '2':
            students = students.filter(ingreso=2)  
        if period == '0':
            students = students.filter(ingreso__in=[0,1])
        
        if anio != '0':
            students = students.filter(ano_cur=anio)
        cant = students.count()

        print(students)
        students8 = students.filter(icne__lte=800).count()
        students9 = students.filter(icne__gte=800).filter(icne__lte=900).count()
        students10 = students.filter(icne__gte=900).filter(icne__lte=1000).count()
        students11 = students.filter(icne__gte=1000).filter(icne__lte=1100).count()
        students12 = students.filter(icne__gte=1100).filter(icne__lte=1200).count()
        students13 = students.filter(icne__gte=1200).filter(icne__lte=1300).count()
        icne = [students8, students9, students10, students11, students12, students13]
        #students = Student.objects.aggregate(count(request.POST['procedence_type'])).values(request.POST['procedence_type'])
        return HttpResponse(json.dumps({'icne':icne, 'cant':cant}), 'application/json')