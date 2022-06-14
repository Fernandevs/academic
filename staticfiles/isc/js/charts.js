
let myChart;
let myChart_ent;

$('#filter').on('change', function () {
    console.log($(this).val());

    find_chart_sexo($(this).val());

});

find_chart_sexo($('#filter').val());
find_chart_enti_nac($('#filter').val());



function find_chart_sexo(filter) {
    const response = axios.get('/isc/chart-sexo?filter=' + filter).then(res => {
        if (res) {
            generar_chart_sexo(res.data['h'], res.data['m'])
        }
    }).catch((err) => {
        iziToast.error({
            timeout: 4000,
            title: 'Error',
            position: 'center',
            message: 'Ocurrio un error.' + err,
        });
    });
}

function generar_chart_sexo(hombre, mujer) {
    const ctx = document.getElementById('sexo').getContext('2d');
    myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Mujeres', 'Hombres'],
            datasets: [{
                label: 'Sexo',
                data: [mujer, hombre],
                backgroundColor: [
                    '#5E6D8C',
                    '#95A3BF',
                    '#152840',
                ],
                borderWidth: 1,
                borderRadius: 8,
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function find_chart_enti_nac(filter) {
    const response = axios.get('/isc/chart-enti-nac?filter=' + filter).then(res => {
        if (res) {
            console.log(res);
            generar_chart_enti_nac(res.data['ag'], res.data['bc'], res.data['bcs'], res.data['cam'], res.data['coa'], res.data['col'], res.data['chia'], res.data['chih'], res.data['df'], res.data['dur'], res.data['gua'], res.data['gue'], res.data['hid'], res.data['jal'], res.data['edom'], res.data['mich'], res.data['mor'], res.data['nay'], res.data['nl'], res.data['oax'], res.data['pueb'], res.data['que'], res.data['qr'], res.data['slp'], res.data['sin'], res.data['son'], res.data['tab'], res.data['tam'], res.data['tlax'], res.data['ver'], res.data['yuc'], res.data['zac'], res.data['ext'])
        }
    }).catch((err) => {
        iziToast.error({
            timeout: 4000,
            title: 'Error',
            position: 'center',
            message: 'Ocurrio un error.' + err,
        });
    });
}

function generar_chart_enti_nac(ag, bc, bcs, cam, coa, col, chia, chih, df, dur, gua, gue, hid, jal, edom, mich, mor, nay, nl, oax, pueb, que, qr, slp, sin, son, tab, tam, tlax, ver, yuc, zac, ext) {
    const ctx = document.getElementById('enti_nac').getContext('2d');
    myChart_ent = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche', 'Coahuila', 'Colima', 'Chiapas', 'Chihuahua', 'Distrito Federal', 'Durango', 'Guanajuato', 'Guerrero', 'Hidalgo', 'Jalisco', 'Estado de México', 'Michoacán', 'Morelos', 'Nayarit', 'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro', 'Quintana Roo', 'San Luis Potosí', 'Sinaloa', 'Sonora', 'Tabasco', 'Tamaulipas', 'Tlaxcala', 'Veracruz', 'Yucatán', 'Zacatecas', 'Extranjero'],
            datasets: [{
                label: 'Entidad de Nacimiento',
                data: [ag, bc, bcs, cam, coa, col, chia, chih, df, dur, gua, gue, hid, jal, edom, mich, mor, nay, nl, oax, pueb, que, qr, slp, sin, son, tab, tam, tlax, ver, yuc, zac, ext],
                backgroundColor: [
                    '#95A3BF'
                ],
                borderWidth: 1,
                borderRadius: 8,
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}


