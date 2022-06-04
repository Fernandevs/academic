import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from nullsafe import _

from students.forms import *
from students.models import *


# Create your views here.

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    login_url = reverse_lazy('login')
    template_name = 'students/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de estudiantes'

        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    login_url = reverse_lazy('login')
    template_name = 'students/create.html'
    success_url = reverse_lazy('list_students')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear estudiantes'

        return context


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    login_url = reverse_lazy('login')
    template_name_suffix = '_update_form'
    template_name = 'students/update.html'
    success_url = reverse_lazy('list_students')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar estudiantes'

        return context


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    login_url = reverse_lazy('login')
    template_name = 'students/delete.html'
    success_url = reverse_lazy('list_students')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar estudiantes'

        return context


class StudentMassiveCreateView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'students/massive.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación masiva de estudiantes'

        return context

    def post(self, request, *args, **kwargs):
        try:
            file_name = request.FILES['file_name']
            decoded_file = file_name.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            for row in reader:
                print(_(row['TIPO_EXA']))
                print(_(row['APLI']))
                print(_(row['FECHA_APLI']))
                print(_(row['CVE_INST']))
                print(_(row['IDENTIFICA']))
                print(_(row['FOLIO']))
                print(_(row['MATRICULA']))
                print(_(row['NOMBRE']))
                print(_(row['APE_PAT']))
                print(_(row['APE_MAT']))
                print(_(row['COMPLETO']))
                print(_(row['DIA_NAC']))
                print(_(row['MES_NAC']))
                print(_(row['ANO_NAC']))
                print(_(row['SEXO']))
                print(_(row['ENTI_NAC']))
                print(_(row['IMP_CAM']))
                print(_(row['IMP_ECU']))
                print(_(row['IMP_VER']))
                print(_(row['IMP_PAN']))
                print(_(row['IMP_PCA']))
                print(_(row['IMP_PDP']))
                print(_(row['IMP_PAT']))
                print(_(row['DIS_SOR']))
                print(_(row['DIS_CEG']))
                print(_(row['DIS_PPS']))
                print(_(row['APO_AML']))
                print(_(row['APO_LCU']))
                print(_(row['APO_LLH']))
                print(_(row['LI_MAD']))
                print(_(row['LI_PAD']))
                print(_(row['EDO_PROC']))
                print(_(row['NOM_PROC']))
                print(_(row['CIU_PROC']))
                print(_(row['CVE_PROC']))
                print(_(row['ANO_BAC']))
                print(_(row['REG_PROC']))
                print(_(row['MOD_BAC']))
                print(_(row['TURNO']))
                print(_(row['PROM_BAC']))
                print(_(row['BEC_DAC']))
                print(_(row['BEC_NEC']))
                print(_(row['BEC_HDA']))
                print(_(row['EXA_EXT']))
                print(_(row['MAT_REP']))
                print(_(row['FAL_ESC']))
                print(_(row['NOE_CLA']))
                print(_(row['PRE_EXA']))
                print(_(row['NOE_TAR']))
                print(_(row['DAN_MALF']))
                print(_(row['DAN_OFI']))
                print(_(row['DAN_EIR']))
                print(_(row['DAN_REQC']))
                print(_(row['DAN_MFT']))
                print(_(row['DAN_FHC']))
                print(_(row['EST_ALCA']))
                print(_(row['NO_UNI']))
                print(_(row['SI_UNI']))
                print(_(row['SI_POSG']))
                print(_(row['ING_INT']))
                print(_(row['ING_LIB']))
                print(_(row['ING_CAN']))
                print(_(row['HAB_PTEX']))
                print(_(row['HAB_PRES']))
                print(_(row['HAB_FBAS']))
                print(_(row['HAB_BAJ']))
                print(_(row['FRE_PPA']))
                print(_(row['FRE_CDE']))
                print(_(row['FRE_TSC']))
                print(_(row['FRE_SME']))
                print(_(row['FRE_ACP']))
                print(_(row['FRE_ACT']))
                print(_(row['ACT_PRIO']))
                print(_(row['ACT_FLIM']))
                print(_(row['ACT_PRI']))
                print(_(row['ACT_GPA']))
                print(_(row['FRE_EJE']))
                print(_(row['INT_EJE']))
                print(_(row['SES_EJE']))
                print(_(row['ORI_AUE']))
                print(_(row['ORI_CME']))
                print(_(row['ORI_ESX']))
                print(_(row['ORI_HSO']))
                print(_(row['ORI_MDP']))
                print(_(row['ORI_MES']))
                print(_(row['ORI_MAG']))
                print(_(row['ORI_NUT']))
                print(_(row['HRS_TRAB']))
                print(_(row['NIV_SOC']))
                print(_(row['ESCO_MAD']))
                print(_(row['ESCO_PAD']))
                print(_(row['CUAN_LIB']))
                print(_(row['SER_TELE']))
                print(_(row['SER_LAV']))
                print(_(row['SER_REF']))
                print(_(row['SER_HOR']))
                print(_(row['SER_INTE']))
                print(_(row['SER_CABL']))
                print(_(row['SER_TABL']))
                print(_(row['BIEN_PC']))
                print(_(row['SER_TV']))
                print(_(row['SER_AUTO']))
                print(_(row['SER_BANO']))
                print(_(row['VAC_RM']))
                print(_(row['CON_EXAO']))
                print(_(row['CUR_ESC']))
                print(_(row['CUR_IPA']))
                print(_(row['CUR_MPA']))
                print(_(row['PRE_EXA2']))
                print(_(row['POS_SUS']))
                print(_(row['ICNE']))
                print(_(row['PERCEN']))
                print(_(row['PORCECNE']))
                print(_(row['PCNE']))
                print(_(row['PPMA']))
                print(_(row['PPAN']))
                print(_(row['PELE']))
                print(_(row['PCLE']))
                print(_(row['IPMA']))
                print(_(row['IPAN']))
                print(_(row['IELE']))
                print(_(row['ICLE']))
                print(_(row['DDD_MG_MAT']))
                print(_(row['DDD_MG_FIS']))
                print(_(row['DDD_MG_LES']))
                print(_(row['DDD_MG_ING']))
                print(_(row['NO DE CONTROL']))
                print(_(row['INGRESO']))
                print(_(row['EGRESO']))
                print(_(row['TITULADO']))
        except Exception as e:
            print('Error: ' + e.__str__())

        return redirect('list_students')
