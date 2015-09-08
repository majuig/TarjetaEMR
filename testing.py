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
    Comun.PagarBoleto(L122,Ahora) #Acá
    Comun.Saldo()
    assert Comun.Saldo() == 878.60
    Comun,PagarBoleto(L122,Ahora)
    assert Comun.Saldo() == 872.85

test_recarga_comun()
test_recarga_medio()
test_pagar_comun()
