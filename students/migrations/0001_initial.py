# Generated by Django 4.0.1 on 2022-06-07 18:30

import academic.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('state', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_exa', models.CharField(blank=True, max_length=3, null=True, verbose_name='Tipo de examen')),
                ('apli', models.CharField(blank=True, max_length=9, null=True, verbose_name='Número de aplicación')),
                ('fecha_apli', models.DateField(auto_now=True, null=True, verbose_name='Fecha de aplicación')),
                ('cve_inst', models.CharField(blank=True, max_length=9, null=True, verbose_name='Clave de la institución en donde se llevó a cabo la aplicación')),
                ('identifica', models.CharField(blank=True, max_length=9, null=True, verbose_name='Identificación de la aplicación')),
                ('folio', models.CharField(blank=True, max_length=9, null=True, verbose_name='Folio')),
                ('matricula', models.CharField(error_messages={'unique': 'Ya existe un estudiante con esa matrícula.'}, max_length=12, unique=True, verbose_name='Clave o matrícula de la institución')),
                ('nombre', models.CharField(max_length=60, validators=[academic.validators.name_validator], verbose_name='Nombre')),
                ('ape_pat', models.CharField(max_length=60, validators=[academic.validators.name_validator], verbose_name='Apellido paterno')),
                ('ape_mat', models.CharField(blank=True, max_length=60, null=True, validators=[academic.validators.name_validator], verbose_name='Apellido materno')),
                ('completo', models.CharField(blank=True, max_length=160, null=True, verbose_name='Nombre completo')),
                ('dia_nac', models.CharField(max_length=2, validators=[academic.validators.number_validator, academic.validators.day_validator], verbose_name='Día de nacimiento')),
                ('mes_nac', models.CharField(choices=[('01', 'Enero'), ('02', 'Febrero'), ('03', 'Marzo'), ('04', 'Abril'), ('05', 'Mayo'), ('06', 'Junio'), ('07', 'Julio'), ('08', 'Agosto'), ('09', 'Septiembre'), ('10', 'Octubre'), ('11', 'Noviembre'), ('12', 'Diciembre')], max_length=2, validators=[academic.validators.number_validator, academic.validators.month_validator], verbose_name='Mes de nacimiento')),
                ('ano_nac', models.CharField(max_length=4, validators=[academic.validators.number_validator, academic.validators.year_validator], verbose_name='Año de nacimiento')),
                ('sexo', models.CharField(choices=[('1', 'Hombre'), ('2', 'Mujer')], max_length=1, verbose_name='Sexo')),
                ('enti_nac', models.CharField(max_length=2, verbose_name='Entidad de nacimiento')),
                ('imp_cam', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Enfrenta dificultad para caminar')),
                ('imp_ecu', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Enfrenta dificultad  para escuchar, aun a corta distancia')),
                ('imp_ver', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Enfrenta problemas graves para ver, aun con lentes')),
                ('imp_pan', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Enfrenta problemas de ansiedad')),
                ('imp_pca', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Problemas para controlar mi agresividad')),
                ('imp_pdp', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Enfrenta problemas de depresión')),
                ('imp_pat', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Enfrenta problemas de atención')),
                ('dis_sor', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Discapacidad de sordera')),
                ('dis_ceg', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Discapacidad de ceguera')),
                ('dis_pps', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Discapacidad de problemas psicomotrices')),
                ('apo_aml', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Apoyo para aplicador con manejo de lenguaje de señas')),
                ('apo_lcu', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Apoyo para lector de cuadernillo')),
                ('apo_llh', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Apoyo para el llenado de la hoja de respuestas')),
                ('li_mad', models.CharField(choices=[('1', 'Sí'), ('2', 'No'), ('3', 'No sé')], max_length=1, verbose_name='Madre')),
                ('li_pad', models.CharField(choices=[('1', 'Sí'), ('2', 'No'), ('3', 'No sé')], max_length=1, verbose_name='Padre')),
                ('nom_proc', models.CharField(max_length=130, verbose_name='Nombre completo de la institución donde concluyó el nivel medio superior')),
                ('ciu_proc', models.CharField(max_length=50, verbose_name='Ciudad donde se ubica la institución')),
                ('cve_proc', models.CharField(blank=True, max_length=6, null=True, verbose_name='Clave')),
                ('ano_bac', models.CharField(blank=True, max_length=4, null=True, validators=[academic.validators.number_validator, academic.validators.year_validator], verbose_name='Año de conclusión')),
                ('reg_proc', models.CharField(choices=[('1', 'Público'), ('2', 'Privado'), ('3', 'Federal por cooperación')], max_length=1, verbose_name='Régimen de sostenimiento')),
                ('mod_bac', models.CharField(choices=[('1', 'Bachillerato general'), ('2', 'Bachillerato tecnológico'), ('3', 'Profesional técnico bachiller'), ('4', 'Bachillerato intercultural (bilingüe indígena)'), ('5', 'Bachillerato internacional'), ('6', 'Acuerdo secretarial 286 Bachillerato'), ('7', 'Preparatoria abierta'), ('8', 'Educación media superior a distancia')], max_length=1, verbose_name='modalidad')),
                ('turno', models.CharField(blank=True, choices=[('1', 'Matutino'), ('2', 'Vespertino'), ('3', 'Nocturno'), ('4', 'Mixto'), ('5', 'Sin turno (Acuerdo 286, sistema abierto, etc.)'), ('6', 'Otro')], max_length=255, null=True, verbose_name='Turno')),
                ('prom_bac', models.FloatField(default=6.0, verbose_name='Promedio final media superior')),
                ('bec_dac', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Beca por alto desempeño')),
                ('bec_nec', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Beca por necesidad económica')),
                ('bec_hda', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Beca por habilidad deportiva o artística')),
                ('exa_ext', models.CharField(choices=[('1', 'Ninguno'), ('2', '1'), ('3', '2'), ('4', '3'), ('5', '4 o más')], max_length=1, verbose_name='Exámenes extraordinarios')),
                ('mat_rep', models.CharField(choices=[('1', 'Ninguno'), ('2', '1'), ('3', '2'), ('4', '3'), ('5', '4 o más')], max_length=1, verbose_name='Materias reprobadas')),
                ('fal_esc', models.CharField(blank=True, choices=[('1', '0'), ('2', '1'), ('3', '2'), ('4', '3'), ('5', '4 o más')], max_length=1, null=True, verbose_name='Faltar a la escuela')),
                ('noe_cla', models.CharField(blank=True, choices=[('1', '0'), ('2', '1'), ('3', '2'), ('4', '3'), ('5', '4 o más')], max_length=1, null=True, verbose_name='No entrar a clases estando en la escuela')),
                ('pre_exa', models.CharField(blank=True, choices=[('1', '0'), ('2', '1'), ('3', '2'), ('4', '3'), ('5', '4 o más')], max_length=1, null=True, verbose_name='Presentar un examen sin haber estudiado todos los temas')),
                ('noe_tar', models.CharField(blank=True, choices=[('1', '0'), ('2', '1'), ('3', '2'), ('4', '3'), ('5', '4 o más')], max_length=1, null=True, verbose_name='No entregar una tarea')),
                ('dan_malf', models.CharField(blank=True, choices=[('1', 'No me sucedió'), ('2', 'Nada de daño'), ('3', 'Poco daño'), ('4', 'Algo de daño'), ('5', 'Mucho daño')], max_length=1, null=True, verbose_name='Golpearan, patearan, cachetearan o maltrataran físicamente')),
                ('dan_ofi', models.CharField(blank=True, choices=[('1', 'No me sucedió'), ('2', 'Nada de daño'), ('3', 'Poco daño'), ('4', 'Algo de daño'), ('5', 'Mucho daño')], max_length=1, null=True, verbose_name='Ofendieran con insultos, groserías o apodos hirientes')),
                ('dan_eir', models.CharField(blank=True, choices=[('1', 'No me sucedió'), ('2', 'Nada de daño'), ('3', 'Poco daño'), ('4', 'Algo de daño'), ('5', 'Mucho daño')], max_length=1, null=True, verbose_name='Excluyeran, ignoraran o rechazaran')),
                ('dan_reqc', models.CharField(blank=True, choices=[('1', 'No me sucedió'), ('2', 'Nada de daño'), ('3', 'Poco daño'), ('4', 'Algo de daño'), ('5', 'Mucho daño')], max_length=1, null=True, verbose_name='Robaran, escondieran o quitaran sus cosas')),
                ('dan_mft', models.CharField(blank=True, choices=[('1', 'No me sucedió'), ('2', 'Nada de daño'), ('3', 'Poco daño'), ('4', 'Algo de daño'), ('5', 'Mucho daño')], max_length=1, null=True, verbose_name='Molestaran por redes sociales')),
                ('dan_fhc', models.CharField(blank=True, choices=[('1', 'No me sucedió'), ('2', 'Nada de daño'), ('3', 'Poco daño'), ('4', 'Algo de daño'), ('5', 'Mucho daño')], max_length=1, null=True, verbose_name='Forzaran a hacer cosas que no quería')),
                ('est_alca', models.CharField(blank=True, choices=[('1', 'Carrera de técnico superior universitario'), ('2', 'Licenciatura'), ('3', 'Posgrado (especialidad, maestría, doctorado)')], max_length=1, null=True, verbose_name='Cuál es el nivel máximo de estudios que le gustaría alcanzar')),
                ('no_uni', models.CharField(blank=True, choices=[('1', '$4,000 o menos'), ('2', '$4,001 a $7,000'), ('3', '$7,001 a $10,000'), ('4', '$10,001 a $15,000'), ('5', '$15,001 a $20,000'), ('6', '$20,001 a $30,000'), ('7', 'Más de $30,000')], max_length=1, null=True, verbose_name='Si no se graduara de una carrera universitaria')),
                ('si_uni', models.CharField(blank=True, choices=[('1', '$4,000 o menos'), ('2', '$4,001 a $7,000'), ('3', '$7,001 a $10,000'), ('4', '$10,001 a $15,000'), ('5', '$15,001 a $20,000'), ('6', '$20,001 a $30,000'), ('7', 'Más de $30,000')], max_length=1, null=True, verbose_name='Si se graduara de una carrera universitaria')),
                ('si_posg', models.CharField(blank=True, choices=[('1', '$4,000 o menos'), ('2', '$4,001 a $7,000'), ('3', '$7,001 a $10,000'), ('4', '$10,001 a $15,000'), ('5', '$15,001 a $20,000'), ('6', '$20,001 a $30,000'), ('7', 'Más de $30,000')], max_length=1, null=True, verbose_name='Si se graduara de un posgrado')),
                ('ing_int', models.CharField(blank=True, choices=[('1', 'No lo sé hacer'), ('2', 'Poco hábil'), ('3', 'Hábil'), ('4', 'Muy hábil')], max_length=1, null=True, verbose_name='Información en interne')),
                ('ing_lib', models.CharField(blank=True, choices=[('1', 'No lo sé hacer'), ('2', 'Poco hábil'), ('3', 'Hábil'), ('4', 'Muy hábil')], max_length=1, null=True, verbose_name='Libros de esparcimiento')),
                ('ing_can', models.CharField(blank=True, choices=[('1', 'No lo sé hacer'), ('2', 'Poco hábil'), ('3', 'Hábil'), ('4', 'Muy hábil')], max_length=1, null=True, verbose_name='Letra de canciones')),
                ('hab_ptex', models.CharField(blank=True, choices=[('1', 'No lo sé hacer'), ('2', 'Poco hábil'), ('3', 'Hábil'), ('4', 'Muy hábil')], max_length=1, null=True, verbose_name='Habilidad en la computadora para crear y editar un documento utilizando un procesador de texto')),
                ('hab_pres', models.CharField(blank=True, choices=[('1', 'No lo sé hacer'), ('2', 'Poco hábil'), ('3', 'Hábil'), ('4', 'Muy hábil')], max_length=1, null=True, verbose_name='Habilidad para utilizar programas para hacer presentaciones')),
                ('hab_fbas', models.CharField(blank=True, choices=[('1', 'No lo sé hacer'), ('2', 'Poco hábil'), ('3', 'Hábil'), ('4', 'Muy hábil')], max_length=1, null=True, verbose_name='Habilidad para emplear funciones básicas en hojas de cálculo')),
                ('hab_baj', models.CharField(blank=True, choices=[('1', 'No lo sé hacer'), ('2', 'Poco hábil'), ('3', 'Hábil'), ('4', 'Muy hábil')], max_length=1, null=True, verbose_name='Habilidad para bajar programas y archivos de internet')),
                ('fre_ppa', models.CharField(blank=True, choices=[('1', 'Nunca o casi nunca'), ('2', 'Algunas veces'), ('3', 'Frecuentemente'), ('4', 'Siempre o casi siempre'), ('1', 'Nunca o casi nunca')], max_length=1, null=True, verbose_name='Participo en la planeación de actividades')),
                ('fre_cde', models.CharField(blank=True, choices=[('1', 'Nunca o casi nunca'), ('2', 'Algunas veces'), ('3', 'Frecuentemente'), ('4', 'Siempre o casi siempre'), ('1', 'Nunca o casi nunca')], max_length=1, null=True, verbose_name='Colaboro en el desarrollo de estrategias para cumplir con las metas')),
                ('fre_tsc', models.CharField(blank=True, choices=[('1', 'Nunca o casi nunca'), ('2', 'Algunas veces'), ('3', 'Frecuentemente'), ('4', 'Siempre o casi siempre'), ('1', 'Nunca o casi nunca')], max_length=1, null=True, verbose_name='Intervengo para tratar de solucionar conflictos')),
                ('fre_sme', models.CharField(blank=True, choices=[('1', 'Nunca o casi nunca'), ('2', 'Algunas veces'), ('3', 'Frecuentemente'), ('4', 'Siempre o casi siempre'), ('1', 'Nunca o casi nunca')], max_length=1, null=True, verbose_name='Hago sugerencias para mejorar la ejecución del equipo')),
                ('fre_acp', models.CharField(blank=True, choices=[('1', 'Nunca o casi nunca'), ('2', 'Algunas veces'), ('3', 'Frecuentemente'), ('4', 'Siempre o casi siempre'), ('1', 'Nunca o casi nunca')], max_length=1, null=True, verbose_name='Ayudo a mis compañeros a resolver problemas')),
                ('fre_act', models.CharField(blank=True, choices=[('1', 'Nunca o casi nunca'), ('2', 'Algunas veces'), ('3', 'Frecuentemente'), ('4', 'Siempre o casi siempre'), ('1', 'Nunca o casi nunca')], max_length=1, null=True, verbose_name='Apoyo a mis compañeros cuando tienen mucho trabajo')),
                ('act_prio', models.CharField(blank=True, choices=[('1', 'Nunca o casi nunca'), ('2', 'Algunas veces'), ('3', 'Frecuentemente'), ('4', 'Siempre o casi siempre'), ('1', 'Nunca o casi nunca')], max_length=1, null=True, verbose_name='Establezco prioridades para determinar el orden en el que debo realizar mis actividades')),
                ('act_flim', models.CharField(blank=True, choices=[('1', 'Nunca o casi nunca'), ('2', 'Algunas veces'), ('3', 'Frecuentemente'), ('4', 'Siempre o casi siempre'), ('1', 'Nunca o casi nunca')], max_length=1, null=True, verbose_name='Me impongo fechas límite para terminar trabajos importantes')),
                ('act_pri', models.CharField(blank=True, choices=[('1', 'Nunca o casi nunca'), ('2', 'Algunas veces'), ('3', 'Frecuentemente'), ('4', 'Siempre o casi siempre'), ('1', 'Nunca o casi nunca')], max_length=1, null=True, verbose_name='Termino primero las tareas más importantes antes de empezar con otras tareas')),
                ('act_gpa', models.CharField(blank=True, choices=[('1', 'Nunca o casi nunca'), ('2', 'Algunas veces'), ('3', 'Frecuentemente'), ('4', 'Siempre o casi siempre'), ('1', 'Nunca o casi nunca')], max_length=1, null=True, verbose_name='Me gusta planear mis actividades importantes con anticipación')),
                ('fre_eje', models.CharField(blank=True, choices=[('1', 'No hago ejercicio'), ('2', 'Menos de 1 vez por semana'), ('3', '1 vez por semana'), ('4', '2 veces por semana'), ('5', '3 veces por semana'), ('6', '4 veces por semana o más')], max_length=1, null=True, verbose_name='Con qué frecuencia realiza ejercicio')),
                ('int_eje', models.CharField(blank=True, choices=[('1', 'No hago ejercicio'), ('2', 'Leve (no se altera mi ritmo cardiaco y respiratorio)'), ('3', 'Moderado (percibo una ligera alteración de mi ritmo cardiaco y respiratorio)'), ('4', 'Intenso - vigoroso (se altera notablemente mi ritmo cardiaco y respiratorio)')], max_length=1, null=True, verbose_name='Qué tan intenso es el ejercicio que realiza')),
                ('ses_eje', models.CharField(blank=True, choices=[('1', 'No hago ejercicio'), ('2', 'Menos de 30 minutos'), ('3', 'De 30 a 59 minutos'), ('4', '1 hora a 1 hora 29 minutos'), ('5', '1 hora 30 minutos a 1 hora 59 minutos'), ('6', '2 horas o más')], max_length=1, null=True, verbose_name='Aproximadamente cuánto duran las sesiones de ejercicio que realiza')),
                ('ori_aue', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Autoestima')),
                ('ori_cme', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Control de miedos')),
                ('ori_esx', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Educación sexual')),
                ('ori_hso', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Habilidades sociales')),
                ('ori_mdp', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Manejo de depresión')),
                ('ori_mes', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Manejo de estrés')),
                ('ori_mag', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Manejo de la agresividad')),
                ('ori_nut', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Nutrición')),
                ('hrs_trab', models.CharField(blank=True, choices=[('1', 'No trabajaba'), ('2', 'Menos de 5 horas'), ('3', 'De 5 a 10 horas'), ('4', 'De 11 a 15 horas'), ('5', 'De 16 a 20 horas'), ('6', 'Más de 20 horas')], max_length=1, null=True, verbose_name='Horas de trabajo a la semana')),
                ('niv_soc', models.CharField(blank=True, choices=[('1', 'Muy bajo'), ('2', 'Bajo'), ('3', 'Medio'), ('4', 'Alto'), ('5', 'Muy alto')], max_length=1, null=True, verbose_name='Nivel socioeconómico de su familia')),
                ('esco_mad', models.CharField(blank=True, choices=[('1', 'No estudió'), ('2', 'Primaria'), ('3', 'Secundaria'), ('4', 'Bachillerato'), ('5', 'Carrera técnica'), ('6', 'Licenciatura'), ('7', 'Posgrado (especialidad, maestría, doctorado)'), ('8', 'No lo sé')], max_length=1, null=True, verbose_name='Nivel de estudios de su madre')),
                ('esco_pad', models.CharField(blank=True, choices=[('1', 'No estudió'), ('2', 'Primaria'), ('3', 'Secundaria'), ('4', 'Bachillerato'), ('5', 'Carrera técnica'), ('6', 'Licenciatura'), ('7', 'Posgrado (especialidad, maestría, doctorado)'), ('8', 'No lo sé')], max_length=1, null=True, verbose_name='Nivel de estudios de su padre')),
                ('cuan_lib', models.CharField(blank=True, choices=[('1', 'Ninguno'), ('2', '1 a 10'), ('3', '11 a 25'), ('4', '26 a 50'), ('5', '51 a 100'), ('6', '101 a 200'), ('7', '201 a 500'), ('8', 'Más de 500')], max_length=1, null=True, verbose_name='Cantidad de libros')),
                ('ser_tele', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Línea telefónica')),
                ('ser_lav', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Lavadora de ropa')),
                ('ser_ref', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Refrigerador')),
                ('ser_hor', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Horno de microondas')),
                ('ser_inte', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Internet')),
                ('ser_cabl', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Televisión de paga')),
                ('ser_tabl', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Tableta')),
                ('bien_pc', models.CharField(choices=[('1', 'Ninguno'), ('2', '1'), ('3', '2'), ('4', '3'), ('5', '4 o más')], max_length=1, null=True, verbose_name='Computadora')),
                ('ser_tv', models.CharField(choices=[('1', 'Ninguno'), ('2', '1'), ('3', '2'), ('4', '3'), ('5', '4 o más')], max_length=1, null=True, verbose_name='Televisor')),
                ('ser_auto', models.CharField(choices=[('1', 'Ninguno'), ('2', '1'), ('3', '2'), ('4', '3'), ('5', '4 o más')], max_length=1, null=True, verbose_name='Automóvil')),
                ('ser_bano', models.CharField(choices=[('1', 'Ninguno'), ('2', '1'), ('3', '2'), ('4', '3'), ('5', '4 o más')], max_length=1, null=True, verbose_name='Baños')),
                ('vac_rm', models.CharField(choices=[('1', 'Ninguno'), ('2', '1'), ('3', '2'), ('4', '3'), ('5', '4 o más')], max_length=1, null=True, verbose_name='Vacaciones')),
                ('con_exao', models.CharField(choices=[('1', 'Ninguno'), ('2', '1'), ('3', '2'), ('4', '3'), ('5', '4 o más')], max_length=1, null=True, verbose_name='Exámenes de opción múltiple')),
                ('cur_esc', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='En su escuela')),
                ('cur_ipa', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='En una institución particular')),
                ('cur_mpa', models.CharField(blank=True, choices=[('1', 'Sí'), ('2', 'No')], max_length=1, null=True, verbose_name='Con un maestro particular')),
                ('pre_exa2', models.CharField(blank=True, choices=[('1', 'Ninguno'), ('2', '1'), ('3', '2'), ('4', '3'), ('5', '4 o más')], max_length=1, null=True, verbose_name='¿cuántas veces ha presentado el examen nacional de ingreso a la educación superior (exani-ii)?')),
                ('pos_sus', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Posición alcanzada por el sustentante en el examen de admisión')),
                ('icne', models.PositiveSmallIntegerField(verbose_name='Calificación en índice CENEVAL del examen de admisión')),
                ('percen', models.FloatField(blank=True, null=True, verbose_name='Percentil del examen de admisión')),
                ('porcecne', models.FloatField(blank=True, null=True, verbose_name='% > cne del examen de admisión')),
                ('pcne', models.FloatField(blank=True, null=True, verbose_name='Calificación en porcentaje de aciertos del examen de admisión')),
                ('ppma', models.FloatField(blank=True, null=True, verbose_name='Calificación de pensamiento matemático en porcentaje de aciertos')),
                ('ppan', models.FloatField(blank=True, null=True, verbose_name='Calificación de pensamiento analítico en porcentaje de aciertos')),
                ('pele', models.FloatField(blank=True, null=True, verbose_name='Calificación de estructura de la lengua en porcentaje de aciertos')),
                ('pcle', models.FloatField(blank=True, null=True, verbose_name='Calificación de comprensión lectora en porcentaje de aciertos')),
                ('ipma', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='calificación de pensamiento matemático en índice CENEVAL')),
                ('ipan', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='calificación de pensamiento analítico en índice CENEVAL')),
                ('iele', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='calificación de estructura de la lengua en índice CENEVAL')),
                ('icle', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='calificación de comprensión lectora en índice CENEVAL')),
                ('ddd_mg_mat', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Sin Dictamen'), (1, 'Insatisfactorio'), (2, 'Satisfactorio')], null=True, verbose_name='Dictamen de matemáticas diagnóstico')),
                ('ddd_mg_fis', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Sin Dictamen'), (1, 'Insatisfactorio'), (2, 'Satisfactorio')], null=True, verbose_name='Dictamen de física')),
                ('ddd_mg_les', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Sin Dictamen'), (1, 'Insatisfactorio'), (2, 'Satisfactorio')], null=True, verbose_name='Dictamen de lenguaje escrito')),
                ('ddd_mg_ing', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Sin Dictamen'), (1, 'Insatisfactorio'), (2, 'Satisfactorio')], null=True, verbose_name='Dictamen de inglés')),
                ('no_control', models.CharField(blank=True, max_length=14, null=True, verbose_name='Número de control')),
                ('year', models.PositiveIntegerField(default=2022, validators=[academic.validators.number_validator, academic.validators.year_validator], verbose_name='Año')),
                ('ingreso', models.BooleanField(blank=True, null=True, verbose_name='Ingreso')),
                ('ingreso_periodo', models.CharField(blank=True, choices=[('1', 'Enero-Junio'), ('2', 'Agosto-Diciembre')], max_length=1, null=True, verbose_name='Periodo de ingreso')),
                ('egreso', models.BooleanField(blank=True, null=True, verbose_name='Egreso')),
                ('egreso_periodo', models.CharField(blank=True, choices=[('1', 'Enero-Junio'), ('2', 'Agosto-Diciembre')], max_length=1, null=True, verbose_name='Periodo de egreso')),
                ('degree', models.BooleanField(verbose_name='Titulado')),
                ('titulado_op', models.CharField(blank=True, choices=[(1, 'Tesis'), (2, 'EGEL'), (3, 'Proyecto de investigación'), (4, 'Dual')], max_length=1, null=True, verbose_name='Opción de titulación')),
                ('edo_proc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Estado', to='state.state')),
            ],
        ),
    ]
