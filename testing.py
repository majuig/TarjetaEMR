from tarjeta import *

Medio = TarjetaMedioBoleto()
Comun = TarjetaComun()

Comun.Recarga(20)
Medio.Recarga(7.5)
Comun.Saldo()
Medio.Saldo()

L122 = Colectivo("Semtur",122,1)
L133 = Colectivo("Las Delicias",133,2)
L144 = Colectivo("Rosario Bus",144,2)
LK = Colectivo("Semtur","K",2)

print("Comun paga  5.75")
Comun.PagarBoleto(L133)
print("Medio paga  2.90")
Medio.PagarBoleto(L133)
print("Comun paga  1.90")
Comun.PagarBoleto(LK)
print("Comun paga  5.75")
Comun.PagarBoleto(L144)
print("Medio paga  2.90")
Medio.PagarBoleto(L133)
print("Comun paga  2.90")
Comun.PagarBoleto(L133)
print("Medio paga  0.90")
Medio.PagarBoleto(L122)
Medio.Saldo()
Medio.ViajesRealizados()

def test_recarga():
    assert Comun.Recarga(-5) == "Imposible cargar ese monto"
    assert Comun.Recarga(100) == 
