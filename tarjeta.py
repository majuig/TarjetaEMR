from datetime import datetime, timedelta

Ahora = datetime.now()

class Colectivo():
    def __init__(self,empresa,linea,interno):
        self._empresa=empresa
        self._linea=linea
        self._interno=interno

class Viaje():
    def __init__(self):
        self._ListaLinea = []
        self._ListaMonto = []
        self._ListaHora = []

    def AgregarViaje(self,linea,monto,hora): #Agrega viajes Medio la lista
        self._ListaLinea.append(linea)
        self._ListaMonto.append(monto)
        self._ListaHora.append(hora)

    def DevolverListaLinea(self):
        return self._ListaLinea

    def DevolverListaMonto(self):
        return self._ListaMonto

    def DevolverListaHora(self):
        return self._ListaHora


class Tarjeta():
    def __init__(self):
        raise NotImplementedError("No se puede crear objetos del tipo Tarjeta")

    def Recarga(self,monto): #Recarga segun parametros

        if(monto <= 0):
            print("Imposible cargar ese monto")
            return False
        elif(monto < 196):
            self._saldo = self._saldo + monto
        elif(monto < 368):
            self._saldo = self._saldo + monto + 34
        else:
            self._saldo = self._saldo + monto + 92

    def Saldo(self): #Muestra el saldo en pesos
        print ("Saldo actual:","$%.2f" % self._saldo)
        return self._saldo

    def ViajesRealizados(self): #Imprimir lineas de los objetos colectivos usados
        if(len(self._MisViajes._ListaLinea) > 0):
            for i in range(0,len(self._MisViajes._ListaLinea)):
                print("Linea:",self._MisViajes._ListaLinea[i],"\tMonto $"+"%.2f"%self._MisViajes._ListaMonto[i],"\tFecha:",str(self._MisViajes._ListaHora[i])[:-7],"\n")
            return True
        else:
            print("No se han realizado viajes con esta tarjeta")
            return False

class TarjetaComun(Tarjeta):
    def __init__(self):
        self._MisViajes = Viaje()
        self._saldo = 0
        self._UltViaje = datetime.strptime("01/01/2000 00:00", "%d/%m/%Y %H:%M")
        self._UltBondi = 0
        self._banderonga = 1


    def PagarBoleto(self,Colectivo,HoraActual):
        DifHS = HoraActual - self._UltViaje

        if(DifHS < timedelta(minutes=60) and self._UltBondi != Colectivo._linea and self._banderonga == 0): #Transbordo o no
            if(self._saldo > 1.90):
                self._saldo = self._saldo - 1.90
                self._MisViajes.AgregarViaje(Colectivo._linea,1.90,HoraActual)
                self._banderonga = 1
                print("Pago de $1.90 realizado en linea" , Colectivo._linea , "el" , str(HoraActual)[:-7])
                self._UltViaje = HoraActual
                self._UltBondi = Colectivo._linea
                return True
            else:
                print("Saldo insuficiente.")
                return False
        else:
            if(self._saldo > 5.75):
                self._saldo = round(self._saldo - 5.75,2)
                self._MisViajes.AgregarViaje(Colectivo._linea,5.75,HoraActual)
                self._banderonga = 0
                print("Pago de $5.75 realizado en linea" , Colectivo._linea , "el" , str(HoraActual)[:-7])
                self._UltViaje = HoraActual
                self._UltBondi = Colectivo._linea
                return True
            else:
                print("Saldo insuficiente.")
                return False


class TarjetaMedioBoleto(Tarjeta):
    def __init__(self):
        self._saldo = 0
        self._UltViaje = datetime.strptime("01/01/2000 00:00", "%d/%m/%Y %H:%M")
        self._MisViajes = Viaje()
        self._UltBondi = 0
        self._Banderonga = 1;


    def PagarBoleto(self,Colectivo,HoraActual):
        DifHS = HoraActual - self._UltViaje


        if(HoraActual.hour > 6 and  HoraActual.hour < 24): #Si es horario escolar, medio boleto
            if(DifHS < timedelta(minutes=60) and self._UltBondi != Colectivo._linea and self._Banderonga == 0):
                if(self._saldo > 0.96):
                    self._saldo = self._saldo - 0.96
                    self._MisViajes.AgregarViaje(Colectivo._linea,0.96,HoraActual)
                    self._UltViaje = HoraActual
                    self._UltBondi = Colectivo._linea
                    self._Banderonga = 1
                    print("Pago de $0.90 realizado en linea" , Colectivo._linea , "el" , str(HoraActual)[:-7])
                    return True
                else:
                    print("Saldo insuficiente.")
                    return False
            else:
                if(self._saldo > 2.90):
                    self._saldo = self._saldo - 2.90
                    self._MisViajes.AgregarViaje(Colectivo._linea,2.90,HoraActual)
                    self._UltViaje = HoraActual
                    self._UltBondi = Colectivo._linea
                    self._Banderonga = 0
                    print("Pago de $2.90 realizado en linea" , Colectivo._linea , "el" , str(HoraActual)[:-7])
                    return True
                else:
                    print("Saldo insuficiente.")
                    return False
        else: #Si no es horario escolar, cobro normal
            if(DifHS < timedelta(minutes=60) and self._UltBondi != Colectivo._linea and self._banderonga == 0):
                if(self._saldo > 1.90):
                    self._saldo = self._saldo - 1.90
                    self._MisViajes.AgregarViaje(Colectivo._linea,1.90,HoraActual)
                    self._banderonga = 1
                    print("Pago de $1.90 realizado en linea" , Colectivo._linea , "el" , str(HoraActual)[:-7])
                    self._UltViaje = HoraActual
                    self._UltBondi = Colectivo._linea
                    return True
                else:
                    print("Saldo insuficiente.")
                    return False
            else:
                if(self._saldo > 5.75):
                    self._saldo = self._saldo - 5.75
                    self._MisViajes.AgregarViaje(Colectivo._linea,5.75,HoraActual)
                    self._banderonga = 0
                    print("Pago de $5.75 realizado en linea" , Colectivo._linea , "el" , str(HoraActual)[:-7])
                    self._UltViaje = HoraActual
                    self._UltBondi = Colectivo._linea
                    return True
                else:
                    print("Saldo insuficiente.")
                    return False
