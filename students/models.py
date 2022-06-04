from django.db import models
from django.utils.translation import gettext_lazy as _

from academic.options import *
from academic.validators import *

# Create your models here.
from state.models import State


class Student(models.Model):
    """
    I. IDENTIFICACIÓN DE LA APLICACIÓN
    """
    tipo_exa = models.CharField(
        _('Tipo de examen'),
        null=True,
        blank=True,
        max_length=3
    )  # Tipo de examen

    apli = models.CharField(
        _('Número de aplicación'),
        null=True,
        blank=True,
        max_length=9
    )  # Número de aplicación

    fecha_apli = models.DateField(
        _('Fecha de aplicación'),
        auto_now=True,
        null=True,
        blank=True
    )  # Fecha de aplicación

    """
    II. IDENTIFICACIÓN DE LA INSTITUCIÓN SEDE
    """
    cve_inst = models.CharField(
        _('Clave de la institución en donde se llevó a cabo la aplicación'),
        null=True,
        blank=True,
        max_length=9
    )  # Clave de la institución en donde se llevó a cabo la aplicación

    identifica = models.CharField(
        _('Identificación de la aplicación'),
        null=True,
        blank=True,
        max_length=9
    )  # Identificación de la aplicación

    """
    III. IDENTIFICACIÓN DEL SUSTENTANTE
    """
    folio = models.CharField(
        _('Folio'),
        null=True,
        blank=True,
        max_length=9
    )  # Folio

    matricula = models.CharField(
        _('Clave o matrícula de la institución'),
        unique=True,
        error_messages={
            "unique": _("Ya existe un estudiante con esa matrícula."),
        },
        null=False,
        blank=False,
        max_length=12
    )  # Clave o matrícula de la institución

    """
    IV. CUESTIONARIO DE CONTEXTO
    """
    nombre = models.CharField(
        _('Nombre'),
        null=False,
        blank=False,
        max_length=60,
        validators=[name_validator]
    )  # Nombre(s)

    ape_pat = models.CharField(
        _('Apellido paterno'),
        null=False,
        blank=False,
        max_length=60,
        validators=[name_validator]
    )  # Apellido paterno

    ape_mat = models.CharField(
        _('Apellido materno'),
        null=True,
        blank=True,
        max_length=60,
        validators=[name_validator]
    )  # Apellido materno

    completo = models.CharField(
        _('Nombre completo'),
        null=True,
        blank=True,
        max_length=160,
    )  # Nombre completo

    # Fecha de nacimiento. En los cuadros anota tu fecha de nacimiento (día, mes, año)
    # y rellene los óvalos correspondientes
    dia_nac = models.CharField(
        _('Día de nacimiento'),
        null=False,
        blank=False,
        max_length=2,
        validators=[number_validator, day_validator],
    )  # Día de nacimiento

    mes_nac = models.CharField(
        _('Mes de nacimiento'),
        null=False,
        blank=False,
        max_length=2,
        validators=[number_validator, month_validator],
        choices=MONTHS
    )  # Mes de nacimiento

    ano_nac = models.CharField(
        _('Año de nacimiento'),
        null=False,
        blank=False,
        max_length=4,
        validators=[number_validator, year_validator],
    )  # Año de nacimiento

    sexo = models.CharField(
        _('Sexo'),
        null=False,
        blank=False,
        max_length=1,
        choices=SEX
    )  # Sexo

    enti_nac = models.CharField(
        _('Entidad de nacimiento'),
        null=False,
        blank=False,
        max_length=2
    )  # Entidad de nacimiento

    """
    V. ¿ENFRENTA ALGUNA DE LAS SIGUIENTES CONDICIONES?
    """
    imp_cam = models.CharField(
        _('Enfrenta dificultad para caminar'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Enfrenta dificultad para caminar

    imp_ecu = models.CharField(
        _('Enfrenta dificultad  para escuchar, aun a corta distancia'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Enfrenta dificultad  para escuchar, aun a corta distancia

    imp_ver = models.CharField(
        _('Enfrenta problemas graves para ver, aun con lentes'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Enfrenta problemas graves para ver, aun con lentes

    imp_pan = models.CharField(
        _('Enfrenta problemas de ansiedad'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Enfrenta problemas de ansiedad

    imp_pca = models.CharField(
        _('Problemas para controlar mi agresividad'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Problemas para controlar mi agresividad

    imp_pdp = models.CharField(
        _('Enfrenta problemas de depresión'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Enfrenta problemas de depresión

    imp_pat = models.CharField(
        _('Enfrenta problemas de atención'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Enfrenta problemas de atención

    """
    VI. ¿ENFRENTAS ALGUNA DE LAS SIGUIENTES DISCAPACIDADES?
    """
    dis_sor = models.CharField(
        _('Discapacidad de sordera'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Discapacidad de sordera

    dis_ceg = models.CharField(
        _('Discapacidad de ceguera'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Discapacidad de ceguera

    dis_pps = models.CharField(
        _('Discapacidad de problemas psicomotrices'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Discapacidad de problemas psicomotrices

    """
    VII. EN CASO DE TENER ALGUNA DISCAPACIDAD (SORDERA, CEGUERA O PROBLEMAS PSICOMOTRICES),
    ¿REQUIERES ALGUNO DE LOS SIGUIENTES APOYOS PARA PRESENTAR EL EXAMEN?
    """
    apo_aml = models.CharField(
        _('Apoyo para aplicador con manejo de lenguaje de señas'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Apoyo para aplicador con manejo de lenguaje de señas

    apo_lcu = models.CharField(
        _('Apoyo para lector de cuadernillo'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Apoyo para lector de cuadernillo

    apo_llh = models.CharField(
        _('Apoyo para el llenado de la hoja de respuestas'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Apoyo para el llenado de la hoja de respuestas

    """
    VIII. ¿ALGUNO DE SUS PADRES HABLA UNA LENGUA INDÍGENA O UN DIALECTO?
    """
    li_mad = models.CharField(
        _('Madre'),
        null=False,
        blank=False,
        max_length=1,
        choices=YES_NO_IDK
    )  # Madre

    li_pad = models.CharField(
        _('Padre'),
        null=False,
        blank=False,
        max_length=1,
        choices=YES_NO_IDK
    )  # Padre

    """
    IX. ESTADO DE PROCEDENCIA
    """
    edo_proc = models.ForeignKey(
        State,
        models.CASCADE,
        _('Estado')
    )  # ¿Dónde concluyó el nivel medio superior?

    """
    X. IDENTIFICACIÓN DE LA INSTITUCIÓN DONDE CONCLUYÓ EL NIVEL MEDIO SUPERIOR
    """
    nom_proc = models.CharField(
        _('Nombre completo de la institución donde concluyó el nivel medio superior'),
        null=False,
        blank=False,
        max_length=130,
    )  # Nombre completo de la institución donde concluyó el nivel medio superior

    ciu_proc = models.CharField(
        _('Ciudad donde se ubica la institución'),
        null=False,
        blank=False,
        max_length=50,
    )
    # Nombre de la ciudad donde se ubica la institución en la que concluyó el nivel medio superior;
    # si fue en el extranjero indique el país

    cve_proc = models.CharField(
        _('Clave'),
        null=True,
        blank=True,
        max_length=6
    )  # Clave de la institución en la que concluyó sus estudios de bachillerato

    ano_bac = models.CharField(
        _('Año de conclusión'),
        null=True,
        blank=True,
        max_length=4,
        validators=[number_validator, year_validator]
    )  # ¿En qué año concluyó el nivel medio superior?

    reg_proc = models.CharField(
        _('Régimen de sostenimiento'),
        null=False,
        blank=False,
        max_length=1,
        choices=REG_PROC
    )
    # ¿Cuál es el régimen de sostenimiento de la escuela en la que estudió el último año
    # del nivel medio superior?

    mod_bac = models.CharField(
        _('modalidad'),
        null=False,
        blank=False,
        max_length=1,
        choices=MOD_BAC
    )  # ¿En qué modalidad obtuvo su certificado del bachillerato?

    turno = models.CharField(
        _('Turno'),
        null=True,
        blank=True,
        max_length=255,
        choices=TURNO
    )  # ¿En qué turno estudió el último año del nivel medio superior?

    prom_bac = models.DecimalField(
        _('Promedio final media superior'),
        max_digits=2,
        decimal_places=1,
        default=6.0
    )
    """
    XI. ANOTE SU PROMEDIO FINAL DEL NIVEL MEDIO SUPERIOR EN LOS CUADROS
    Y RELLENE LOS ÓVALOS CORRESPONDIENTES
    """

    # ¿Recibió beca en el nivel medio superior?
    bec_dac = models.CharField(
        _('Beca por alto desempeño'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Por alto desempeño académico

    bec_nec = models.CharField(
        _('Beca por necesidad económica'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Por necesidad económica

    bec_hda = models.CharField(
        _('Beca por habilidad deportiva o artística'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Por habilidad deportiva o artística

    exa_ext = models.CharField(
        _('Exámenes extraordinarios'),
        null=False,
        blank=False,
        max_length=1,
        choices=NONE_ONE_TWO_THREE_FOUR_OR_MORE
    )  # ¿Cuántos exámenes extraordinarios presentó en el nivel medio superior?

    mat_rep = models.CharField(
        _('Materias reprobadas'),
        null=False,
        blank=False,
        max_length=1,
        choices=NONE_ONE_TWO_THREE_FOUR_OR_MORE
    )  # ¿Cuántas materias reprobó en el nivel medio superior?

    """
    XII. ¿CUÁNTAS VECES REALIZÓ LO SIGUIENTE EN EL ÚLTIMO MES QUE CURSÓ EL NIVEL MEDIO SUPERIOR?
    """
    fal_esc = models.CharField(
        _('Faltar a la escuela'),
        null=True,
        blank=True,
        max_length=1,
        choices=ZERO_ONE_TWO_THREE_FOUR_OR_MORE
    )  # Faltar a la escuela

    noe_cla = models.CharField(
        _('No entrar a clases estando en la escuela'),
        null=True,
        blank=True,
        max_length=1,
        choices=ZERO_ONE_TWO_THREE_FOUR_OR_MORE
    )  # No entrar a clases estando en la escuela

    pre_exa = models.CharField(
        _('Presentar un examen sin haber estudiado todos los temas'),
        null=True,
        blank=True,
        max_length=1,
        choices=ZERO_ONE_TWO_THREE_FOUR_OR_MORE
    )  # Presentar un examen sin haber estudiado todos los temas

    noe_tar = models.CharField(
        _('No entregar una tarea'),
        null=True,
        blank=True,
        max_length=1,
        choices=ZERO_ONE_TWO_THREE_FOUR_OR_MORE
    )  # No entregar una tarea

    """
    XIII. ¿QUÉ TANTO DAÑO LE CAUSÓ QUE SUS COMPAÑEROS EN EL NIVEL MEDIO SUPERIOR LO…
    """
    dan_malf = models.CharField(
        _('Golpearan, patearan, cachetearan o maltrataran físicamente'),
        null=True,
        blank=True,
        max_length=1,
        choices=DAN
    )  # Golpearan, patearan, cachetearan o maltrataran físicamente?

    dan_ofi = models.CharField(
        _('Ofendieran con insultos, groserías o apodos hirientes'),
        null=True,
        blank=True,
        max_length=1,
        choices=DAN
    )  # Ofendieran con insultos, groserías o apodos hirientes?

    dan_eir = models.CharField(
        _('Excluyeran, ignoraran o rechazaran'),
        null=True,
        blank=True,
        max_length=1,
        choices=DAN
    )  # Excluyeran, ignoraran o rechazaran?

    dan_reqc = models.CharField(
        _('Robaran, escondieran o quitaran sus cosas'),
        null=True,
        blank=True,
        max_length=1,
        choices=DAN
    )  # Robaran, escondieran o quitaran sus cosas?

    dan_mft = models.CharField(
        _('Molestaran por redes sociales'),
        null=True,
        blank=True,
        max_length=1,
        choices=DAN
    )
    # Molestaran por medio de facebook, twitter,
    # correo electrónico o mensajes de texto por el celular?

    dan_fhc = models.CharField(
        _('Forzaran a hacer cosas que no quería'),
        null=True,
        blank=True,
        max_length=1,
        choices=DAN
    )  # Forzaran a hacer cosas que no quería?

    est_alca = models.CharField(
        _('Cuál es el nivel máximo de estudios que le gustaría alcanzar'),
        null=True,
        blank=True,
        max_length=1,
        choices=LEVEL
    )  # ¿Cuál es el nivel máximo de estudios que le gustaría alcanzar?

    no_uni = models.CharField(
        _('Si no se graduara de una carrera universitaria'),
        null=True,
        blank=True,
        max_length=1,
        choices=MONEY
    )
    # Si no se graduara de una carrera universitaria,
    # ¿qué ingreso mensual promedio esperaría obtener dentro de 10 años?

    si_uni = models.CharField(
        _('Si se graduara de una carrera universitaria'),
        null=True,
        blank=True,
        max_length=1,
        choices=MONEY
    )
    # Si se graduara de una carrera universitaria,
    # ¿qué ingreso mensual promedio esperaría obtener dentro de 10 años?

    si_posg = models.CharField(
        _('Si se graduara de un posgrado'),
        null=True,
        blank=True,
        max_length=1,
        choices=MONEY
    )
    # Si se graduara de un posgrado,
    # ¿qué ingreso mensual promedio esperaría obtener dentro de 10 años?

    """
    XIV. ¿QUÉ TAN HÁBIL ES PARA LEER EN INGLÉS LOS SIGUIENTES CONTENIDOS?
    """
    ing_int = models.CharField(
        _('Información en interne'),
        null=True,
        blank=True,
        max_length=1,
        choices=ABILITY
    )  # Información en interne

    ing_lib = models.CharField(
        _('Libros de esparcimiento'),
        null=True,
        blank=True,
        max_length=1,
        choices=ABILITY
    )  # Libros de esparcimiento

    ing_can = models.CharField(
        _('Letra de canciones'),
        null=True,
        blank=True,
        max_length=1,
        choices=ABILITY
    )  # Letra de canciones

    """
    XV. ¿QUÉ TAN HÁBIL ES PARA REALIZAR LAS SIGUIENTES ACTIVIDADES EN LA COMPUTADORA?
    """
    hab_ptex = models.CharField(
        _('Habilidad en la computadora para crear y editar un documento utilizando un procesador de texto'),
        null=True,
        blank=True,
        max_length=1,
        choices=ABILITY
    )  # Habilidad en la computadora para crear y editar un documento utilizando un procesador de texto

    hab_pres = models.CharField(
        _('Habilidad para utilizar programas para hacer presentaciones'),
        null=True,
        blank=True,
        max_length=1,
        choices=ABILITY
    )  # Habilidad para utilizar programas para hacer presentaciones

    hab_fbas = models.CharField(
        _('Habilidad para emplear funciones básicas en hojas de cálculo'),
        null=True,
        blank=True,
        max_length=1,
        choices=ABILITY
    )
    # Habilidad para emplear funciones básicas en hojas de cálculo
    # (captura de datos, formato, ordenamiento y uso de fórmulas)

    hab_baj = models.CharField(
        _('Habilidad para bajar programas y archivos de internet'),
        null=True,
        blank=True,
        max_length=1,
        choices=ABILITY
    )  # Habilidad para bajar programas y archivos de internet

    """
    XVI. ¿CON QUÉ FRECUENCIA REALIZA LO SIGUIENTE CUANDO TRABAJA EN EQUIPO?
    """
    fre_ppa = models.CharField(
        _('Participo en la planeación de actividades'),
        null=True,
        blank=True,
        max_length=1,
        choices=FREQUENCY
    )  # Participo en la planeación de actividades

    fre_cde = models.CharField(
        _('Colaboro en el desarrollo de estrategias para cumplir con las metas'),
        null=True,
        blank=True,
        max_length=1,
        choices=FREQUENCY
    )  # Colaboro en el desarrollo de estrategias para cumplir con las metas

    fre_tsc = models.CharField(
        _('Intervengo para tratar de solucionar conflictos'),
        null=True,
        blank=True,
        max_length=1,
        choices=FREQUENCY
    )  # Intervengo para tratar de solucionar conflictos

    fre_sme = models.CharField(
        _('Hago sugerencias para mejorar la ejecución del equipo'),
        null=True,
        blank=True,
        max_length=1,
        choices=FREQUENCY
    )  # Hago sugerencias para mejorar la ejecución del equipo

    fre_acp = models.CharField(
        _('Ayudo a mis compañeros a resolver problemas'),
        null=True,
        blank=True,
        max_length=1,
        choices=FREQUENCY
    )  # Ayudo a mis compañeros a resolver problemas

    fre_act = models.CharField(
        _('Apoyo a mis compañeros cuando tienen mucho trabajo'),
        null=True,
        blank=True,
        max_length=1,
        choices=FREQUENCY
    )  # Apoyo a mis compañeros cuando tienen mucho trabajo

    """
    XVII. ¿CON QUÉ FRECUENCIA REALIZA LAS SIGUIENTES ACTIVIDADES?
    """
    act_prio = models.CharField(
        _('Establezco prioridades para determinar el orden en el que debo realizar mis actividades'),
        null=True,
        blank=True,
        max_length=1,
        choices=FREQUENCY
    )  # Establezco prioridades para determinar el orden en el que debo realizar mis actividades

    act_flim = models.CharField(
        _('Me impongo fechas límite para terminar trabajos importantes'),
        null=True,
        blank=True,
        max_length=1,
        choices=FREQUENCY
    )  # Me impongo fechas límite para terminar trabajos importantes

    act_pri = models.CharField(
        _('Termino primero las tareas más importantes antes de empezar con otras tareas'),
        null=True,
        blank=True,
        max_length=1,
        choices=FREQUENCY
    )  # Termino primero las tareas más importantes antes de empezar con otras tareas

    act_gpa = models.CharField(
        _('Me gusta planear mis actividades importantes con anticipación'),
        null=True,
        blank=True,
        max_length=1,
        choices=FREQUENCY
    )  # Me gusta planear mis actividades importantes con anticipación

    fre_eje = models.CharField(
        _('Con qué frecuencia realiza ejercicio'),
        null=True,
        blank=True,
        max_length=1,
        choices=FRE_EJE
    )  # ¿Con qué frecuencia realiza ejercicio?

    int_eje = models.CharField(
        _('Qué tan intenso es el ejercicio que realiza'),
        null=True,
        blank=True,
        max_length=1,
        choices=INT_EJE
    )  # ¿Qué tan intenso es el ejercicio que realiza?

    ses_eje = models.CharField(
        _('Aproximadamente cuánto duran las sesiones de ejercicio que realiza'),
        null=True,
        blank=True,
        max_length=1,
        choices=SES_EJE
    )  # Aproximadamente, ¿cuánto duran las sesiones de ejercicio que realiza?

    """
    XVIII. ¿LE INTERESARÍA RECIBIR ORIENTACIÓN O APOYO SOBRE LOS SIGUIENTES TEMAS?
    """
    ori_aue = models.CharField(
        _('Autoestima'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Autoestima

    ori_cme = models.CharField(
        _('Control de miedos'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Control de miedos

    ori_esx = models.CharField(
        _('Educación sexual'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Educación sexual

    ori_hso = models.CharField(
        _('Habilidades sociales'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Habilidades sociales

    ori_mdp = models.CharField(
        _('Manejo de depresión'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Manejo de depresión

    ori_mes = models.CharField(
        _('Manejo de estrés'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Manejo de estrés

    ori_mag = models.CharField(
        _('Manejo de la agresividad'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Manejo de la agresividad

    ori_nut = models.CharField(
        _('Nutrición'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Nutrición

    hrs_trab = models.CharField(
        _('Horas de trabajo a la semana'),
        null=True,
        blank=True,
        max_length=1,
        choices=HRS_TRAB
    )
    # ¿cuántas horas a la semana dedicó a trabajar durante el nivel medio superior?
    # (considere que su trabajo puede ser asalariado o sin pago,
    # por ejemplo trabajar en un negocio familiar).

    niv_soc = models.CharField(
        _('Nivel socioeconómico de su familia'),
        null=True,
        blank=True,
        max_length=1,
        choices=NIV_SOC
    )  # ¿Cuál considera que es el nivel socioeconómico de su familia?

    esco_mad = models.CharField(
        _('Nivel de estudios de su madre'),
        null=True,
        blank=True,
        max_length=1,
        choices=ESCOLARIDAD
    )  # ¿Cuál es el máximo nivel de estudios de su madre (aunque haya fallecido)?

    esco_pad = models.CharField(
        _('Nivel de estudios de su padre'),
        null=True,
        blank=True,
        max_length=1,
        choices=ESCOLARIDAD
    )  # ¿Cuál es el máximo nivel de estudios de su padre (aunque haya fallecido)?

    cuan_lib = models.CharField(
        _('Cantidad de libros'),
        null=True,
        blank=True,
        max_length=1,
        choices=CUAN_LIB
    )  # ¿Cuántos libros hay en su casa? (no considere revistas, periódicos o libros de texto)

    """ XIX. ¿CUENTA CON LOS SIGUIENTES BIENES Y SERVICIOS EN SU CASA?"""
    ser_tele = models.CharField(
        _('Línea telefónica'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Línea telefónica

    ser_lav = models.CharField(
        _('Lavadora de ropa'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Lavadora de ropa

    ser_ref = models.CharField(
        _('Refrigerador'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Refrigerador

    ser_hor = models.CharField(
        _('Horno de microondas'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Horno de microondas

    ser_inte = models.CharField(
        _('Internet'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Internet

    ser_cabl = models.CharField(
        _('Televisión de paga'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Televisión de paga (cablevisión, sky, etc.)

    ser_tabl = models.CharField(
        _('Tableta'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Tableta (ipad, samsung galaxy, etc.)

    """
    XX. ¿CUÁNTOS DE LOS SIGUIENTES BIENES TIENE EN SU CASA?
    """
    bien_pc = models.CharField(
        _('Computadora'),
        null=True,
        blank=False,
        max_length=1,
        choices=NONE_ONE_TWO_THREE_FOUR_OR_MORE
    )  # Computadora

    ser_tv = models.CharField(
        _('Televisor'),
        null=True,
        blank=False,
        max_length=1,
        choices=NONE_ONE_TWO_THREE_FOUR_OR_MORE
    )  # Televisor

    ser_auto = models.CharField(
        _('Automóvil'),
        null=True,
        blank=False,
        max_length=1,
        choices=NONE_ONE_TWO_THREE_FOUR_OR_MORE
    )  # Automóvil

    ser_bano = models.CharField(
        _('Baños'),
        null=True,
        blank=False,
        max_length=1,
        choices=NONE_ONE_TWO_THREE_FOUR_OR_MORE
    )  # Baños completos

    vac_rm = models.CharField(
        _('Vacaciones'),
        null=True,
        blank=False,
        max_length=1,
        choices=NONE_ONE_TWO_THREE_FOUR_OR_MORE
    )  # ¿Cuántas veces ha salido de vacaciones dentro de la república mexicana en los últimos 2 años?

    con_exao = models.CharField(
        _('Exámenes de opción múltiple'),
        null=True,
        blank=False,
        max_length=1,
        choices=NONE_ONE_TWO_THREE_FOUR_OR_MORE
    )
    # ¿Cuántas veces ha contestado exámenes de opción múltiple en los que rellena círculos (alveolos)
    # en este año escolar?

    """
    XXI. ¿TOMASTE UN CURSO DE PREPARACIÓN PARA EL
    EXAMEN NACIONAL DE INGRESO A LA EDUCACIÓN SUPERIOR (EXANI-II)?
    """
    cur_esc = models.CharField(
        _('En su escuela'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # En su escuela

    cur_ipa = models.CharField(
        _('En una institución particular'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # En una institución particular

    cur_mpa = models.CharField(
        _('Con un maestro particular'),
        null=True,
        blank=True,
        max_length=1,
        choices=YES_NO
    )  # Con un maestro particular

    pre_exa2 = models.CharField(
        _('¿cuántas veces ha presentado el examen nacional de ingreso a la educación superior (exani-ii)?'),
        null=True,
        blank=True,
        max_length=1,
        choices=NONE_ONE_TWO_THREE_FOUR_OR_MORE
    )  # ¿cuántas veces ha presentado el examen nacional de ingreso a la educación superior (exani-ii)?

    """
    VI. CALIFICACIÓN DEL EXAMEN
    """
    pos_sus = models.PositiveBigIntegerField(
        _('Posición alcanzada por el sustentante en el examen de admisión'),
        null=True,
        blank=True
    )  # Posición alcanzada por el sustentante en el examen de admisión

    icne = models.PositiveSmallIntegerField(
        _('Calificación en índice CENEVAL del examen de admisión'),
        null=False,
        blank=False
    )  # Calificación en índice CENEVAL del examen de admisión

    percen = models.DecimalField(
        _('Percentil del examen de admisión'),
        null=True,
        blank=True,
        max_digits=3,
        decimal_places=2
    )  # Percentil del examen de admisión

    porcecne = models.DecimalField(
        _('% > cne del examen de admisión'),
        null=True,
        blank=True,
        max_digits=3,
        decimal_places=2
    )  # % > cne del examen de admisión

    pcne = models.DecimalField(
        _('Calificación en porcentaje de aciertos del examen de admisión'),
        null=True,
        blank=True,
        max_digits=3,
        decimal_places=2
    )  # Calificación en porcentaje de aciertos del examen de admisión

    # Calificación en porcentaje de aciertos del examen de Admisión
    ppma = models.DecimalField(
        _('Calificación de pensamiento matemático en porcentaje de aciertos'),
        null=True,
        blank=True,
        max_digits=3,
        decimal_places=2
    )  # Calificación de pensamiento matemático en porcentaje de aciertos

    ppan = models.DecimalField(
        _('Calificación de pensamiento analítico en porcentaje de aciertos'),
        null=True,
        blank=True,
        max_digits=3,
        decimal_places=2
    )  # Calificación de pensamiento analítico en porcentaje de aciertos

    pele = models.DecimalField(
        _('Calificación de estructura de la lengua en porcentaje de aciertos'),
        null=True,
        blank=True,
        max_digits=3,
        decimal_places=2
    )  # Calificación de estructura de la lengua en porcentaje de aciertos

    pcle = models.DecimalField(
        _('Calificación de comprensión lectora en porcentaje de aciertos'),
        null=True,
        blank=True,
        max_digits=3,
        decimal_places=2
    )  # Calificación de comprensión lectora en porcentaje de aciertos

    # Calificación en índice Ceneval del examen de Admisión
    ipma = models.PositiveSmallIntegerField(
        _('calificación de pensamiento matemático en índice CENEVAL'),
        null=True,
        blank=True
    )  # calificación de pensamiento matemático en índice CENEVAL

    ipan = models.PositiveSmallIntegerField(
        _('calificación de pensamiento analítico en índice CENEVAL'),
        null=True,
        blank=True
    )  # calificación de pensamiento analítico en índice CENEVAL

    iele = models.PositiveSmallIntegerField(
        _('calificación de estructura de la lengua en índice CENEVAL'),
        null=True,
        blank=True
    )  # calificación de estructura de la lengua en índice CENEVAL

    icle = models.PositiveSmallIntegerField(
        _('calificación de comprensión lectora en índice CENEVAL'),
        null=True,
        blank=True
    )  # calificación de comprensión lectora en índice CENEVAL

    # CALIFICACIÓN DEL EXAMEN DE DIAGNÓSTICO (MÓDULO INGENIERÍA Y TECNOLOGÍA)
    # Dictamen del examen de Diagnóstico
    ddd_mg_mat = models.PositiveSmallIntegerField(
        _('Dictamen de matemáticas diagnóstico'),
        null=True,
        blank=True,
        choices=DDD
    )  # Dictamen de matemáticas "diagnóstico"

    ddd_mg_fis = models.PositiveSmallIntegerField(
        _('Dictamen de física'),
        null=True,
        blank=True,
        choices=DDD
    )  # Dictamen de física

    ddd_mg_les = models.PositiveSmallIntegerField(
        _('Dictamen de lenguaje escrito'),
        null=True,
        blank=True,
        choices=DDD
    )  # Dictamen de lenguaje escrito

    ddd_mg_ing = models.PositiveSmallIntegerField(
        _('Dictamen de inglés'),
        null=True,
        blank=True,
        choices=DDD
    )  # Dictamen de inglés

    no_control = models.CharField(
        _('Número de control'),
        null=False,
        blank=False,
        max_length=14
    )

    ingreso = models.CharField(
        _('Ingreso'),
        null=False,
        blank=False,
        max_length=4,
        validators=[number_validator, year_validator]
    )

    ingreso_periodo = models.CharField(
        _('Periodo de ingreso'),
        null=False,
        blank=False,
        max_length=1,
        choices=PERIOD,
        default='2'
    )

    egreso = models.CharField(
        _('Egreso'),
        null=False,
        blank=False,
        max_length=4,
        validators=[number_validator, year_validator]
    )

    egreso_periodo = models.CharField(
        _('Periodo de egreso'),
        null=False,
        blank=False,
        max_length=1,
        choices=PERIOD,
        default='2'
    )

    titulado = models.CharField(
        _('titulado'),
        null=False,
        blank=False,
        max_length=4,
        choices=DEGREE_OPTIONS
    )
