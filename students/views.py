import csv

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from students.forms import *
from students.models import *


# Create your views here.

class StudentListView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ListView
):
    model = Student
    login_url = reverse_lazy('login')
    template_name = 'students/read.html'
    permission_required = 'students.view_student'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de estudiantes'

        return context


class StudentCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    CreateView
):
    model = Student
    form_class = StudentForm
    login_url = reverse_lazy('login')
    template_name = 'students/create.html'
    success_url = reverse_lazy('list_students')
    permission_required = 'students.add_student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear estudiantes'

        return context


class StudentUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UpdateView
):
    model = Student
    form_class = StudentForm
    login_url = reverse_lazy('login')
    template_name_suffix = '_update_form'
    template_name = 'students/update.html'
    success_url = reverse_lazy('list_students')
    permission_required = 'students.change_student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar estudiantes'

        return context


class StudentDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DeleteView
):
    model = Student
    login_url = reverse_lazy('login')
    template_name = 'students/delete.html'
    success_url = reverse_lazy('list_students')
    permission_required = 'students.delete_student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar estudiantes'

        return context


class StudentMassiveCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    TemplateView
):
    login_url = reverse_lazy('login')
    template_name = 'students/massive.html'
    permission_required = 'students.add_student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación masiva de estudiantes'
        context['range'] = range(1900, now().year + 1)
        context['year'] = now().year

        return context

    def post(self, request, *args, **kwargs):
        try:
            file_name = request.FILES['file_name']
            decoded_file = file_name.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            i: int = 0

            for row in reader:
                tipo_exa = row['TIPO_EXA'] if 'TIPO_EXA' in row else None
                apli = row['APLI'] if 'APLI' in row else None
                fecha_apli = row['FECHA_APLI'] if 'FECHA_APLI' in row else None
                cve_inst = row['CVE_INST'] if 'CVE_INST' in row else None
                identifica = row['IDENTIFICA'] if 'IDENTIFICA' in row else None
                folio = row['FOLIO'] if 'FOLIO' in row else None
                matricula = row['MATRICULA'] if 'MATRICULA' in row else row['\ufeffMATRICULA']
                nombre = row['NOMBRE'] if 'NOMBRE' in row else None
                ape_pat = row['APE_PAT'] if 'APE_PAT' in row else None
                ape_mat = row['APE_MAT'] if 'APE_MAT' in row else None
                completo = row['COMPLETO'] if 'COMPLETO' in row else None
                dia_nac = row['DIA_NAC'] if 'DIA_NAC' in row else None
                mes_nac = row['MES_NAC'] if 'MES_NAC' in row else None
                ano_nac = row['ANO_NAC'] if 'ANO_NAC' in row else None
                sexo = row['SEXO'] if 'SEXO' in row else None
                enti_nac = row['ENTI_NAC'] if 'ENTI_NAC' in row else None
                imp_cam = row['IMP_CAM'] if 'IMP_CAM' in row else None
                imp_ecu = row['IMP_ECU'] if 'IMP_ECU' in row else None
                imp_ver = row['IMP_VER'] if 'IMP_VER' in row else None
                imp_pan = row['IMP_PAN'] if 'IMP_PAN' in row else None
                imp_pca = row['IMP_PCA'] if 'IMP_PCA' in row else None
                imp_pdp = row['IMP_PDP'] if 'IMP_PDP' in row else None
                imp_pat = row['IMP_PAT'] if 'IMP_PAT' in row else None
                dis_sor = row['DIS_SOR'] if 'DIS_SOR' in row else None
                dis_ceg = row['DIS_CEG'] if 'DIS_CEG' in row else None
                dis_pps = row['DIS_PPS'] if 'DIS_PPS' in row else None
                apo_aml = row['APO_AML'] if 'APO_AML' in row else None
                apo_lcu = row['APO_LCU'] if 'APO_LCU' in row else None
                apo_llh = row['APO_LLH'] if 'APO_LLH' in row else None
                li_mad = row['LI_MAD'] if 'LI_MAD' in row else None
                li_pad = row['LI_PAD'] if 'LI_PAD' in row else None
                state: str = row['EDO_PROC'] if 'EDO_PROC' in row else '16'
                state.zfill(2)
                edo_proc = State.objects.filter(pk=state).get()
                nom_proc = row['NOM_PROC'] if 'NOM_PROC' in row else None
                ciu_proc = row['CIU_PROC'] if 'CIU_PROC' in row else None
                cve_proc = row['CVE_PROC'] if 'CVE_PROC' in row else None
                ano_bac = row['ANO_BAC'] if 'ANO_BAC' in row else None
                reg_proc = row['REG_PROC'] if 'REG_PROC' in row else None
                mod_bac = row['MOD_BAC'] if 'MOD_BAC' in row else None
                turno = row['TURNO'] if 'TURNO' in row else None
                prom_bac = row['PROM_BAC'] if 'PROM_BAC' in row else None
                bec_dac = row['BEC_DAC'] if 'BEC_DAC' in row else None
                bec_nec = row['BEC_NEC'] if 'BEC_NEC' in row else None
                bec_hda = row['BEC_HDA'] if 'BEC_HDA' in row else None
                exa_ext = row['EXA_EXT'] if 'EXA_EXT' in row else None
                mat_rep = row['MAT_REP'] if 'MAT_REP' in row else None
                fal_esc = row['FAL_ESC'] if 'FAL_ESC' in row else None
                noe_cla = row['NOE_CLA'] if 'NOE_CLA' in row else None
                pre_exa = row['PRE_EXA'] if 'PRE_EXA' in row else None
                noe_tar = row['NOE_TAR'] if 'NOE_TAR' in row else None
                dan_malf = row['DAN_MALF'] if 'DAN_MALF' in row else None
                dan_ofi = row['DAN_OFI'] if 'DAN_OFI' in row else None
                dan_eir = row['DAN_EIR'] if 'DAN_EIR' in row else None
                dan_reqc = row['DAN_REQC'] if 'DAN_REQC' in row else None
                dan_mft = row['DAN_MFT'] if 'DAN_MFT' in row else None
                dan_fhc = row['DAN_FHC'] if 'DAN_FHC' in row else None
                est_alca = row['EST_ALCA'] if 'EST_ALCA' in row else None
                no_uni = row['NO_UNI'] if 'NO_UNI' in row else None
                si_uni = row['SI_UNI'] if 'SI_UNI' in row else None
                si_posg = row['SI_POSG'] if 'SI_POSG' in row else None
                ing_int = row['ING_INT'] if 'ING_INT' in row else None
                ing_lib = row['ING_LIB'] if 'ING_LIB' in row else None
                ing_can = row['ING_CAN'] if 'ING_CAN' in row else None
                hab_ptex = row['HAB_PTEX'] if 'HAB_PTEX' in row else None
                hab_pres = row['HAB_PRES'] if 'HAB_PRES' in row else None
                hab_fbas = row['HAB_FBAS'] if 'HAB_FBAS' in row else None
                hab_baj = row['HAB_BAJ'] if 'HAB_BAJ' in row else None
                fre_ppa = row['FRE_PPA'] if 'FRE_PPA' in row else None
                fre_cde = row['FRE_CDE'] if 'FRE_CDE' in row else None
                fre_tsc = row['FRE_TSC'] if 'FRE_TSC' in row else None
                fre_sme = row['FRE_SME'] if 'FRE_SME' in row else None
                fre_acp = row['FRE_ACP'] if 'FRE_ACP' in row else None
                fre_act = row['FRE_ACT'] if 'FRE_ACT' in row else None
                act_prio = row['ACT_PRIO'] if 'ACT_PRIO' in row else None
                act_flim = row['ACT_FLIM'] if 'ACT_FLIM' in row else None
                act_pri = row['ACT_PRI'] if 'ACT_PRI' in row else None
                act_gpa = row['ACT_GPA'] if 'ACT_GPA' in row else None
                fre_eje = row['FRE_EJE'] if 'FRE_EJE' in row else None
                int_eje = row['INT_EJE'] if 'INT_EJE' in row else None
                ses_eje = row['SES_EJE'] if 'SES_EJE' in row else None
                ori_aue = row['ORI_AUE'] if 'ORI_AUE' in row else None
                ori_cme = row['ORI_CME'] if 'ORI_CME' in row else None
                ori_esx = row['ORI_ESX'] if 'ORI_ESX' in row else None
                ori_hso = row['ORI_HSO'] if 'ORI_HSO' in row else None
                ori_mdp = row['ORI_MDP'] if 'ORI_MDP' in row else None
                ori_mes = row['ORI_MES'] if 'ORI_MES' in row else None
                ori_mag = row['ORI_MAG'] if 'ORI_MAG' in row else None
                ori_nut = row['ORI_NUT'] if 'ORI_NUT' in row else None
                hrs_trab = row['HRS_TRAB'] if 'HRS_TRAB' in row else None
                niv_soc = row['NIV_SOC'] if 'NIV_SOC' in row else None
                esco_mad = row['ESCO_MAD'] if 'ESCO_MAD' in row else None
                esco_pad = row['ESCO_PAD'] if 'ESCO_PAD' in row else None
                cuan_lib = row['CUAN_LIB'] if 'CUAN_LIB' in row else None
                ser_tele = row['SER_TELE'] if 'SER_TELE' in row else None
                ser_lav = row['SER_LAV'] if 'SER_LAV' in row else None
                ser_ref = row['SER_REF'] if 'SER_REF' in row else None
                ser_hor = row['SER_HOR'] if 'SER_HOR' in row else None
                ser_inte = row['SER_INTE'] if 'SER_INTE' in row else None
                ser_cabl = row['SER_CABL'] if 'SER_CABL' in row else None
                ser_tabl = row['SER_TABL'] if 'SER_TABL' in row else None
                bien_pc = row['BIEN_PC'] if 'BIEN_PC' in row else None
                ser_tv = row['SER_TV'] if 'SER_TV' in row else None
                ser_auto = row['SER_AUTO'] if 'SER_AUTO' in row else None
                ser_bano = row['SER_BANO'] if 'SER_BANO' in row else None
                vac_rm = row['VAC_RM'] if 'VAC_RM' in row else None
                con_exao = row['CON_EXAO'] if 'CON_EXAO' in row else None
                cur_esc = row['CUR_ESC'] if 'CUR_ESC' in row else None
                cur_ipa = row['CUR_IPA'] if 'CUR_IPA' in row else None
                cur_mpa = row['CUR_MPA'] if 'CUR_MPA' in row else None
                pre_exa2 = row['PRE_EXA2'] if 'PRE_EXA2' in row else None
                pos_sus = row['POS_SUS'] if 'POS_SUS' in row else None
                icne = row['ICNE'] if 'ICNE' in row else None
                percen = row['PERCEN'] if 'PERCEN' in row else None
                porcecne = row['PORCECNE'] if 'PORCECNE' in row else None
                pcne = row['PCNE'] if 'PCNE' in row else None
                ppma = row['PPMA'] if 'PPMA' in row else None
                ppan = row['PPAN'] if 'PPAN' in row else None
                pele = row['PELE'] if 'PELE' in row else None
                pcle = row['PCLE'] if 'PCLE' in row else None
                ipma = row['IPMA'] if 'IPMA' in row else None
                ipan = row['IPAN'] if 'IPAN' in row else None
                iele = row['IELE'] if 'IELE' in row else None
                icle = row['ICLE'] if 'ICLE' in row else None
                ddd_mg_mat = row['DDD_MG_MAT'] if 'DDD_MG_MAT' in row else None
                ddd_mg_fis = row['DDD_MG_FIS'] if 'DDD_MG_FIS' in row else None
                ddd_mg_les = row['DDD_MG_LES'] if 'DDD_MG_LES' in row else None
                ddd_mg_ing = row['DDD_MG_ING'] if 'DDD_MG_ING' in row else None
                no_control = row['NO DE CONTROL'] if 'NO DE CONTROL' in row else None
                year = request.POST['year'] if 'year' in request.POST else now().year

                if not no_control:
                    ingreso = False
                    egreso = False
                    degree = False

                else:
                    ingreso = row['INGRESO'] if 'INGRESO' in row else None
                    egreso = row['EGRESO'] if 'EGRESO' in row else None
                    degree = row['TITULACION'] if 'TITULACION' in row else None

                student = Student(
                    tipo_exa=tipo_exa,
                    apli=apli,
                    fecha_apli=fecha_apli,
                    cve_inst=cve_inst,
                    identifica=identifica,
                    folio=folio,
                    matricula=matricula,
                    nombre=nombre,
                    ape_pat=ape_pat,
                    ape_mat=ape_mat,
                    completo=completo,
                    dia_nac=dia_nac,
                    mes_nac=mes_nac,
                    ano_nac=ano_nac,
                    sexo=sexo,
                    enti_nac=enti_nac,
                    imp_cam=imp_cam,
                    imp_ecu=imp_ecu,
                    imp_ver=imp_ver,
                    imp_pan=imp_pan,
                    imp_pca=imp_pca,
                    imp_pdp=imp_pdp,
                    imp_pat=imp_pat,
                    dis_sor=dis_sor,
                    dis_ceg=dis_ceg,
                    dis_pps=dis_pps,
                    apo_aml=apo_aml,
                    apo_lcu=apo_lcu,
                    apo_llh=apo_llh,
                    li_mad=li_mad,
                    li_pad=li_pad,
                    edo_proc=edo_proc,
                    nom_proc=nom_proc,
                    ciu_proc=ciu_proc,
                    cve_proc=cve_proc,
                    ano_bac=ano_bac,
                    reg_proc=reg_proc,
                    mod_bac=mod_bac,
                    turno=turno,
                    prom_bac=prom_bac,
                    bec_dac=bec_dac,
                    bec_nec=bec_nec,
                    bec_hda=bec_hda,
                    exa_ext=exa_ext,
                    mat_rep=mat_rep,
                    fal_esc=fal_esc,
                    noe_cla=noe_cla,
                    pre_exa=pre_exa,
                    noe_tar=noe_tar,
                    dan_malf=dan_malf,
                    dan_ofi=dan_ofi,
                    dan_eir=dan_eir,
                    dan_reqc=dan_reqc,
                    dan_mft=dan_mft,
                    dan_fhc=dan_fhc,
                    est_alca=est_alca,
                    no_uni=no_uni,
                    si_uni=si_uni,
                    si_posg=si_posg,
                    ing_int=ing_int,
                    ing_lib=ing_lib,
                    ing_can=ing_can,
                    hab_ptex=hab_ptex,
                    hab_pres=hab_pres,
                    hab_fbas=hab_fbas,
                    hab_baj=hab_baj,
                    fre_ppa=fre_ppa,
                    fre_cde=fre_cde,
                    fre_tsc=fre_tsc,
                    fre_sme=fre_sme,
                    fre_acp=fre_acp,
                    fre_act=fre_act,
                    act_prio=act_prio,
                    act_flim=act_flim,
                    act_pri=act_pri,
                    act_gpa=act_gpa,
                    fre_eje=fre_eje,
                    int_eje=int_eje,
                    ses_eje=ses_eje,
                    ori_aue=ori_aue,
                    ori_cme=ori_cme,
                    ori_esx=ori_esx,
                    ori_hso=ori_hso,
                    ori_mdp=ori_mdp,
                    ori_mes=ori_mes,
                    ori_mag=ori_mag,
                    ori_nut=ori_nut,
                    hrs_trab=hrs_trab,
                    niv_soc=niv_soc,
                    esco_mad=esco_mad,
                    esco_pad=esco_pad,
                    cuan_lib=cuan_lib,
                    ser_tele=ser_tele,
                    ser_lav=ser_lav,
                    ser_ref=ser_ref,
                    ser_hor=ser_hor,
                    ser_inte=ser_inte,
                    ser_cabl=ser_cabl,
                    ser_tabl=ser_tabl,
                    bien_pc=bien_pc,
                    ser_tv=ser_tv,
                    ser_auto=ser_auto,
                    ser_bano=ser_bano,
                    vac_rm=vac_rm,
                    con_exao=con_exao,
                    cur_esc=cur_esc,
                    cur_ipa=cur_ipa,
                    cur_mpa=cur_mpa,
                    pre_exa2=pre_exa2,
                    pos_sus=pos_sus,
                    icne=icne,
                    percen=percen,
                    porcecne=porcecne,
                    pcne=pcne,
                    ppma=ppma,
                    ppan=ppan,
                    pele=pele,
                    pcle=pcle,
                    ipma=ipma,
                    ipan=ipan,
                    iele=iele,
                    icle=icle,
                    ddd_mg_mat=ddd_mg_mat,
                    ddd_mg_fis=ddd_mg_fis,
                    ddd_mg_les=ddd_mg_les,
                    ddd_mg_ing=ddd_mg_ing,
                    no_control=no_control,
                    ingreso=ingreso,
                    egreso=egreso,
                    degree=degree,
                    year=year
                )

                try:
                    student.save()
                    i += 1
                    print(i)
                except Exception as e:
                    print(e.__str__())
                    continue
        except Exception as e:
            print('Error: ' + e.__str__())

        return redirect('list_students')
