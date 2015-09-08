from tarjeta import *

Medio = TarjetaMedioBoleto()
Comun = TarjetaComun()
SinViajes = TarjetaComun()


L122 = Colectivo("Semtur",122,1)
L133 = Colectivo("Las Delicias",133,2)
LK = Colectivo("Semtur","K",2)

DiaAnterior = datetime.strptime("08/09/2015 05:30", "%d/%m/%Y %H:%M")
DiaAnterior2 = datetime.strptime("08/09/2015 05:35", "%d/%m/%Y %H:%M")
HaceUnRatito = datetime.now() - timedelta(minutes=30)
Ahora = datetime.now()


def test_recarga_comun():
    assert Comun.Recarga(-5) == False
    Comun.Recarga(100)
    assert Comun.Saldo() == 100
    Comun.Recarga(200)
    assert Comun.Saldo() == 334
    Comun.Recarga(466)
    assert Comun.Saldo() == 892

def test_recarga_medio():
    assert Medio.Recarga(-5) == False
    Medio.Recarga(100)
    assert Medio.Saldo() == 100
    Medio.Recarga(200)
    assert Medio.Saldo() == 334
    Medio.Recarga(466)
    assert Medio.Saldo() == 892

def test_pagar_comun():
    Comun.PagarBoleto(L122,DiaAnterior)
    assert Comun.Saldo() == 886.25
    Comun.PagarBoleto(L122,HaceUnRatito)
    assert Comun.Saldo() == 880.50
    Comun.PagarBoleto(L122,Ahora)
    assert Comun.Saldo() == 874.75
    Comun.PagarBoleto(L133,Ahora)
    assert Comun.Saldo() == 872.85
    Comun.PagarBoleto(LK,Ahora)
    assert Comun.Saldo() == 867.10
    Comun.PagarBoleto(L122,Ahora)
    assert Comun.Saldo() == 865.2

def test_pagar_medio():
    Medio.PagarBoleto(L122,DiaAnterior) #Horario no estudiantil
    assert Medio.Saldo() == 886.25
    Medio.PagarBoleto(L122,DiaAnterior2) #Transbordo en horario no estudiantil
    assert Medio.Saldo() == 880.50
    Medio.PagarBoleto(L122,HaceUnRatito) #Horario estudiantil
    assert Medio.Saldo() == 877.60
    Medio.PagarBoleto(L133,Ahora) #Transbordo en horario estudiantil
    assert Medio.Saldo() == 876.64
    Medio.PagarBoleto(LK,Ahora) #Tercer colectivo en una hora, medio boleto
    assert Medio.Saldo() == 873.74
    Medio.PagarBoleto(L122,Ahora) #Cuarto colectivo en una hora, transbordo y medio
    assert Medio.Saldo() == 872.78


def test_viajes_comun():
    assert Comun._MisViajes.DevolverListaLinea() == [122,122,122,133,'K',122]
    assert Comun._MisViajes.DevolverListaMonto() == [5.75,5.75,5.75,1.9,5.75,1.9]
    assert Comun.ViajesRealizados() == True
    assert SinViajes.ViajesRealizados() == False
    

test_recarga_comun()
test_recarga_medio()
test_pagar_comun()
test_pagar_medio()
test_viajes_comun()
