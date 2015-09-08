from tarjeta import *

Medio = TarjetaMedioBoleto()
Comun = TarjetaComun()


L122 = Colectivo("Semtur",122,1)
L133 = Colectivo("Las Delicias",133,2)
L144 = Colectivo("Rosario Bus",144,2)
LK = Colectivo("Semtur","K",2)

DiaAnterior = datetime.strptime("08/09/2015 10:30", "%d/%m/%Y %H:%M")
HaceUnRatito = datetime.now() - timedelta(minutes=30)
Ahora = datetime.now()


def test_recarga_Comun():
    assert Comun.Recarga(-5) == False
    Comun.Recarga(100)
    assert Comun.Saldo() == 100
    Comun.Recarga(200)
    assert Comun.Saldo() == 334
    Comun.Recarga(66)
    assert Comun.Recarga(400) == 492

def test_recarga_Medio():
    assert Medio.Recarga(-5) == False
    Medio.Recarga(100)
    assert Medio.Saldo() == 100
    Medio.Recarga(200)
    assert Medio.Saldo() == 334
    Medio.Recarga(66)
    assert Medio.Recarga(400) == 492

def test_Pagar_Comun():
    Comun.PagarBoleto(L122,Ahora)
    assert Comun.Saldo() == 486.25

test_recarga_Comun()
test_recarga_medio()
