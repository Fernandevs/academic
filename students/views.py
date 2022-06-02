import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

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
                student = Student(
                    matricula=row['\ufeffMATRICULA'],
                    completo=row['COMPLETO'],
                    nombre=row['NOMBRE'],
                    ape_pat=row['APE_PAT'],
                    ape_mat=row['APE_MAT'],
                    dia_nac=row['DIA_NAC'],
                    mes_nac=row['MES_NAC'],
                    ano_nac=row['ANO_NAC'],
                    sexo=row['SEXO'],
                    enti_nac=row['ENTI_NAC'],
                    imp_cam=row['IMP_CAM'],
                    imp_ecu=row['IMP_ECU'],
                    imp_ver=row['IMP_VER'],
                    imp_con=row['IMP_CON'],
                    imp_pan=row['IMP_PAN'],
                    imp_pca=row['IMP_PCA'],
                    imp_pdp=row['IMP_PDP'],
                    imp_pat=row['IMP_PAT'],
                    imp_pob=row['IMP_POB'],
                    imp_pab=row['IMP_PAB'],
                    li_mad=row['LI_MAD'],
                    li_pad=row['LI_PAD'],
                    edo_proc=row['EDO_PROC'],
                    mes_cur=row['MES_CUR'],
                    ano_cur=row['ANO_CUR'],
                    reg_proc=row['REG_PROC'],
                    mod_bac=row['MOD_BAC'],
                    sis_nms=row['SIS_NMS'],
                    turno=row['TURNO'],
                    prom_bac=row['PROM_BAC'],
                    bec_nec=row['BEC_NEC'],
                    exa_ext=row['EXA_EXT'],
                    mat_rep=row['MAT_REP'],
                    fre_fcl=row['FRE_FCL'],
                    fre_lltm=row['FRE_LLTM'],
                    fre_pdc=row['FRE_PDC'],
                    fre_dte=row['FRE_DTE'],
                    fre_ette=row['FRE_ETTE'],
                    fre_ppa=row['FRE_PPA'],
                    fre_cde=row['FRE_CDE'],
                    fre_tsc=row['FRE_TSC'],
                    fre_sme=row['FRE_SME'],
                    fre_ctr=row['FRE_CTR'],
                    per_hqp=row['PER_HQP'],
                    per_aet=row['PER_AET'],
                    per_arp=row['PER_ARP'],
                    per_ctd=row['PER_CTD'],
                    ide_ese=row['IDE_ESE'],
                    ide_vbm=row['IDE_VBM'],
                    ide_ome=row['IDE_OME'],
                    ide_ppm=row['IDE_PPM'],
                    ide_fam=row['IDE_FAM'],
                    ide_ces=row['IDE_CES'],
                    ide_cec=row['IDE_CEC'],
                    des_desa=row['DES_DESA'],
                    des_esme=row['DES_ESME'],
                    des_term=row['DES_TERM'],
                    des_duro=row['DES_DURO'],
                    soc_ptfg=row['SOC_PTFG'],
                    soc_imc=row['SOC_IMC'],
                    soc_pdc=row['SOC_PDC'],
                    soc_pdm=row['SOC_PDM'],
                    ocu_exv=row['OCU_EXV'],
                    ocu_dde=row['OCU_DDE'],
                    ocu_nep=row['OCU_NEP'],
                    ocu_pcc=row['OCU_PCC'],
                    ocu_pae=row['OCU_PAE'],
                    act_dtd=row['ACT_DTD'],
                    act_eod=row['ACT_EOD'],
                    act_dca=row['ACT_DCA'],
                    act_erc=row['ACT_ERC'],
                    hab_ptae=row['HAB_PTAE'],
                    hab_dam=row['HAB_DAM'],
                    hab_aea=row['HAB_AEA'],
                    hab_tevs=row['HAB_TEVS'],
                    hab_lti=row['HAB_LTI'],
                    hab_eti=row['HAB_ETI'],
                    hab_etiv=row['HAB_ETIV'],
                    hab_mhc=row['HAB_MHC'],
                    hab_oif=row['HAB_OIF'],
                    hab_ioa=row['HAB_IOA'],
                    hab_eto=row['HAB_ETO'],
                    hab_apm=row['HAB_APM'],
                    hab_rel=row['HAB_REL'],
                    hab_sal=row['HAB_SAL'],
                    hab_dap=row['HAB_DAP'],
                    hab_cma=row['HAB_CMA'],
                    est_alca=row['EST_ALCA'],
                    ori_aue=row['ORI_AUE'],
                    ori_cme=row['ORI_CME'],
                    ori_esx=row['ORI_ESX'],
                    ori_hso=row['ORI_HSO'],
                    ori_mdp=row['ORI_MDP'],
                    ori_mes=row['ORI_MES'],
                    ori_mag=row['ORI_MAG'],
                    ori_nut=row['ORI_NUT'],
                    uti_lplr=row['UTI_LPLR'],
                    uti_bite=row['UTI_BITE'],
                    uti_cce=row['UTI_CCE'],
                    dan_malf=row['DAN_MALF'],
                    dan_ofi=row['DAN_OFI'],
                    dan_eir=row['DAN_EIR'],
                    dan_reqc=row['DAN_REQC'],
                    dan_mft=row['DAN_MFT'],
                    dan_fhc=row['DAN_FHC'],
                    hrs_trab=row['HRS_TRAB'],
                    esco_mad=row['ESCO_MAD'],
                    esco_pad=row['ESCO_PAD'],
                    cuan_lib=row['CUAN_LIB'],
                    ser_tele=row['SER_TELE'],
                    ser_lav=row['SER_LAV'],
                    ser_ref=row['SER_REF'],
                    ser_hor=row['SER_HOR'],
                    ser_inte=row['SER_INTE'],
                    ser_cabl=row['SER_CABL'],
                    ser_tabl=row['SER_TABL'],
                    bien_pc=row['BIEN_PC'],
                    ser_tv=row['SER_TV'],
                    ser_auto=row['SER_AUTO'],
                    ser_bano=row['SER_BANO'],
                    vac_rm=row['VAC_RM'],
                    car_foll=row['CAR_FOLL'],
                    car_guia=row['CAR_GUIA'],
                    car_piov=row['CAR_PIOV'],
                    car_ptov=row['CAR_PTOV'],
                    inf_pad=row['INF_PAD'],
                    inf_her=row['INF_HER'],
                    inf_ami=row['INF_AMI'],
                    inf_prf=row['INF_PRF'],
                    inf_poe=row['INF_POE'],
                    uti_gui=row['UTI_GUI'],
                    cur_esc=row['CUR_ESC'],
                    cur_ipa=row['CUR_IPA'],
                    cur_mpa=row['CUR_MPA'],
                    icne=row['ICNE'],
                    percen=row['PERCEN'],
                    porcecne=row['PORCECNE'],
                    pcne=row['PCNE'],
                    ppma=row['PPMA'],
                    ppan=row['PPAN'],
                    pele=row['PELE'],
                    ipma=row['IPMA'],
                    ipan=row['IPAN'],
                    iele=row['IELE'],
                    icle=row['ICLE'],
                    no_control=row['NO DE CONTROL'],
                    ingreso=row['INGRESO'],
                    egreso=row['EGRESO'],
                    titulado=row['TITULADO']
                )

                student.save()

        except Exception as e:
            print('Error: ' + e.__str__())

        return redirect('list_students')
