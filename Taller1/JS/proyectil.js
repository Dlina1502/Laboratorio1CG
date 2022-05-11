"use strict"

var v0;
var gravedad;
var tiempo;
var angulo;

var vx;
var vy;

var conActivo;

var cs;
var s;
var m;
var h;

//ejes coordenados

var x = 0;
var y = 0;
var yp = 0;

var colorProyec;

window.onload = setInterval(crono, 10);

function dibuja() {
    var canvas = document.getElementById('screen');
    var ctx = canvas.getContext('2d');
    
    ctx.fillStyle = colorProyec;
    
    ctx.beginPath();
    ctx.arc(x /10, yp / 10, .8, 0, Math.PI * 2, false); 
    ctx.fill();
}

function start() {
    conActivo = true;
    colorProyec = colorAleatorio();
}

function stop() {
    conActivo = false;
}


function colorAleatorio() {
    return "rgb(" + aleatorio(0, 255) + "," + aleatorio(0, 255) + "," + aleatorio(0, 100) + ")";
}

function redondear(numero) {
    var numeroOriginal = parseFloat(numero);
    var numeroRedondeado = Math.round(numeroOriginal * 100) / 100;
    return numeroRedondeado;
}

function gradosaleat() {
    document.forma.grados.value = aleatorio(0, 90);
    comprobar()
}

function aleatorio(inferior, superior) {
    var numPos = superior - inferior;
    var aleat = Math.random() * numPos;
    aleat = Math.floor(aleat);
    return parseInt(inferior) + aleat;
}

function velocidadInicial() {
    v0 = document.formulario.vo.value;
    var aux = v0;
    console.log(aux);
}

function calcularcoordenadas(tiempo) {
    angulo = (parseFloat(document.formulario.grados.value) * Math.PI) / 180;
    gravedad = parseFloat(document.formulario.gravedad.value);
    v0 = parseFloat(document.formulario.vo.value);

    x = ((v0 * tiempo * (Math.cos(angulo))));
    y = ((v0 * tiempo * (Math.sin(angulo))) - (.5) * gravedad * (tiempo * tiempo));
    yp = 1490 - y;

    document.formulario.x.value = redondear(x);
    document.formulario.y.value = redondear(y);

    if (tiempo > 0) {
        if (y <= 0) {
            conActivo = false; 
        }
    }

    dibuja();
}

function crono() {
    
    if (conActivo == true) {
        
        cs = parseFloat(document.formulario.cs.value);
        s = parseFloat(document.formulario.s.value);
        m = parseFloat(document.formulario.m.value);
        h = parseFloat(document.formulario.h.value);
        
        cs++;
        if (cs > 100) {
            s = (s + parseInt(cs / 100));
            cs = cs % 100;
        }

        if (cs == 100) { 
            cs = 0;
            s++; 
        }

        if (s == 60) { 
            s = 0;
            m++; 
        }
       
        if (s > 60) {
            m = m + parseInt(s / 60);
            s = s % 60;
        }

        if (m == 60) { 
            m = 0;
            h++; 
        }

        if (m > 60) {
            h = h + parseInt(m / 60);
            m = m % 60;
        }

        
        tiempo = (h * 3600 + m * 60 + s + cs * 0.01);
        

   
        if (h < 10) { h = '0' + h; }
        if (m < 10) { m = '0' + m; }
        if (s < 10) { s = '0' + s; }
        if (cs < 10) { cs = '0' + cs; }
                       
        document.formulario.cs.value = cs;
        document.formulario.s.value = s;
        document.formulario.m.value = m;
        document.formulario.h.value = h;

        calcularcoordenadas(tiempo);
    }
}


