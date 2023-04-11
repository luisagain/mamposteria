
from msg import Flag

class Losa:
    '''
    La clase Losa sirve para crear el objeto losa y definir sus propiedades.\n
    Se definirán los métodos y atributos necesarios como son:\n
    El área de losa, el peso de la losa de azotea y de entrepiso con carga muerta
    y con carga viva
    '''
    def __init__(self, area_losa: float, peso_losa_m2: float, **kargs) -> None:
        '''
        Parametros
        ---------
        area_losa -> el área total de la losa [m2]\n
        peso_losa_m2 -> [kg/m2]\n
        '''

        #*__________Digitable_________________
        self.__losa_area: float = area_losa
        self.__losa_peso_m2: float = peso_losa_m2
        
        #*________________ Digitables opcionales ________________
        self.__peso_add_m2: float = 0.0
        try:
            if isinstance(kargs["peso_add_m2"], list):
                for peso in kargs["peso_add_m2"]:
                    self.__peso_add_m2 += peso
            elif isinstance(kargs["peso_add_m2"], (float, int)):
                self.__peso_add_m2 = kargs["peso_add_m2"]
        except KeyError:
            pass

        #*________________ Calculable ___________________
        self.peso : float = 0


        #* ________________ Cálculos ________________
        self.updatePeso()

        

        

    def addCvv(self, cv_v: float):
        '''
        Añade el peso de la carga viva vertical
        '''
        self.__peso += self.__losa_area * cv_v
        return self.__peso

    def getPesoM2(self):
        return self.__losa_peso_m2 

    def getPeso(self):
        return self.__peso

    def getPesoCvv(self, cv_v: float):
        '''
        Calcula el peso considerando la carga viva
        '''
        return (self.__losa_peso_m2 + self.__peso_add_m2 + cv_v) * self.__losa_area

    def getPesoCvh(self, cv_h: float):
        '''
        Calcula el peso considerando la carga sísmica
        '''
        return (self.__losa_peso_m2 + self.__peso_add_m2 + cv_h) * self.__losa_area
    
    def getPesoAddM2(self):
        return self.__peso_add_m2

    def updatePeso(self):
        self.__peso = (self.__losa_peso_m2 + self.__peso_add_m2) * self.__losa_area


class Muro:
    '''
    La clase Muro sirve para crear el objeto muro y definir sus propiedades.\n
    Se definirán los métodos y atributos necesarios como son:\n
    La sub clase Castillo, peso por m2, peso por ml y de entrepiso con carga muerta
    y con carga viva
    '''

    class Castillo:
        '''
        La subclase Castillo sirve para crear el objeto castillo y definir sus propiedades.\n
        Se definirán los métodos y atributos necesarios como son:\n
        El área de acero de refuerzo longitudinal necesario, el área de refuerzo transversal, separación de los estribos
        '''
        

        def __init__(self,  fy : float, fyc: float, bc : float, hc : float, fc : float) -> None:
            '''
                Parámetros
                ---------
                fy -> [kg/cm2]\n
                fyh -> [kg/cm2]\n
                bc -> [m]\n
                '''
            
            #*_____________ Digitables _____________

            self.fy : float = fy
            self.fyc : float = fyc
            self.bc : float = bc
            self.hc : float = hc
            self.fc : float = fc

            #TODO: Este valor puede modificarse de constante a calculable, se deberá hacer en futuras versiones
            self.varilla : float = 5.68 #centimetros

            #* _____________ Calculables _____________

            self.__separacion : float = 0
            self.__asc : float = 0
            self.__as : float = 0


            #* _____________ Cálculos _____________

            self.calcAs()

        
        def calcAs(self):

            self.__as = 0.2*self.fc/self.fy*self.bc*self.hc

            pass


        def calcSep(self, espesor_muro : float):
            '''
                Calcula la separación de los estribos
            '''

            if espesor_muro*1.5 < 200/1000:

                self.__separacion = espesor_muro*1.5
            else:
                self.__separacion = 200/1000

            self.__calcAsc()

            pass

        def __calcAsc(self):
            '''
                Calcula el área de refuerzo transversal
            '''
            self.__asc = 10000*self.__separacion/(self.fy*self.hc)

        

        
        ## _____________ Métodos Geter _____________

        def getSep(self):
            return self.__separacion
        
        def getAreaRefTransv(self):
            return self.__asc
        
        def getAs(self):
            return self.__as

    def __init__(self, id : int, longitud : float, fe : float, peso_mc_material : float, altura_libre :float, fm : float, castillo : Castillo,at_muros:float,  **kargs) -> None:
        
        #*_____________ digitable _____________

        self.id : int = id
        self.longitud : float = longitud
        self.fe : float = fe
        self.peso_mc_material : float = peso_mc_material
        self.altura_libre : float = altura_libre
        self.fm : float = fm
        self.castillo : Muro.Castillo = castillo
        self.at_muros: float = at_muros
        self.Ash: float = 0 #TODO VALOR AGREGADO RECIENTEMENTE, CAMBIAR
        self.sht: float = 0 #TODO VALOR AGREGADO RECIENTEMENTE, CAMBIAR 
        #* _____________ Constantes _____________

        self.cm_muro: float = 1.3
        self.cv_muro: float = 1.5
        self.fr : float = 0.6
        self.vm : float = 2 #kg/cm2
        self.frv : float = 0.7
        self.fyh : float = 6000 #kg/cm2
        self.alpha : float = 1/0.045 #kg/cm2
        #*_____________ digitables opcionales _____________

        #Asignación por defecto de espesor
        self.__espesor : float
        try:
            self.__espesor  = kargs["espesor"]
        except KeyError:
            self.__espesor  = 0.15

        #Asignación por defecto de peso de añadidos
        self.__peso_add_m2 : float
        try:
            if type(kargs["peso_add"]) == list:

                for peso in kargs["peso_add"]:

                    self.__peso_add_m2 += peso

            elif type(kargs["peso_add"]) == float or type(kargs["peso_add"]) == int:
                self.__peso_add_m2 = kargs["peso_add"]

        except KeyError:
            self.__peso_add_m2 = 0

        #* _____________constantes _____________

        self.__fr : float = 0.6 #Factor de seguridad que se utiliza al calcular PR

        #* _____________ Calculables _____________

        self.__f : float = 0 #TODO: Se debe utilizar para calcular VMR en futuras versiones
        self.__peso_ml : float = 0
        self.__peso_cm : float = 0
        self.__peso_cv : float = 0
        self.__pu : float = 0
        self.__pr : float = 0
        self.__comparacion : str = ""
        self.__area_transversal: float = round(((self.longitud*self.__espesor)*10000),3)
        self.__VMR : float = 0 #TODO se debe utilizar para calcular VR en futuras versiones
        self.__phVSR : float = 0 #TODO
        self.__k0 : float = 0
        self.__ns : float = 0
        self.__N : float = 0
        self.__VSR : float = 0
        self.__VR : float = 0
        self.__VU : float = 0
        #* _____________ Cálculos de castillo _____________
        castillo.calcSep(self.__espesor)
        
        #* _____________ Cálculos de muro _____________
        self.calcF()
        self.caclPesoML()
        
    def __add__(self, otherInstance):

        self.__pu += otherInstance.__pu
        return self

    
    def calcPU(self):
        
        
        self.__pu = (self.cm_muro*self.__peso_cm) + (self.cv_muro*self.__peso_cv)
        
        
        
    def calcPesoCM(self, losa_peso_mc : float):
        '''
            Calcula el peso de la carga viva para el muro
            Parametros
            ----------
            losa_peso_mc -> [kg/m2]
        '''

        self.__peso_cm = losa_peso_mc*self.at_muros + ((self.__peso_ml*self.longitud)) #kg
        
    def calcPesoCV(self,losa_cv_v : float):
        '''
            Calcula el peso de carga viva del muro
            parametros
            ---------
            losa_cv_v -> carga viva vertical de la losa [kg/m2]
        '''
        self.__peso_cv = losa_cv_v*self.at_muros #kg

    def CompPRPU (self):

        if self.__pr >= self.__pu:
            self.__comparacion = "Sí cumple"
        else:
            self.__comparacion = "No Cumple"

    def calcPR(self): #$ FUNCION AÑADIDA
        '''
            Se calculará la carga que resisten los muros
        '''
        self.__pr = self.fr*self.fe*((self.fm*self.__area_transversal)+(self.castillo.varilla*self.castillo.fy))

    def calcF(self):
        '''
            Calculamos F
        '''

        if self.altura_libre/self.longitud <= 0.2:
            self.__f = 1.5

        elif self.altura_libre/self.longitud >= 1:
            self.__f = 1
        
        else:
            self.__f = 1.625 -0.625*self.altura_libre/self.longitud

        pass
        
    def caclPesoML(self):
        '''
            Calcula el peso por metro lineal
        '''

        self.__peso_ml = ((self.peso_mc_material) + self.__peso_add_m2)*self.altura_libre #kg/m

    def calcVmR(self): #TODO AGREGADO. VERIFICAR
        '''
            Calcula la carga horizontal que resiste la mampostería
        '''
        if self.frv*(0.5*self.vm*self.at_muros+0.3*(1.3*self.__peso_cm+1.5*self.__peso_cv)) >= 1.5*self.frv*self.vm*self.at_muros*self.__f:
            self.__VMR=self.frv*(0.5*self.vm*self.at_muros+0.3*(1.3*self.__peso_cm+1.5*self.__peso_cv))
        elif self.frv*(0.5*self.vm*self.at_muros+0.3*(1.3*self.__peso_cm+1.5*self.__peso_cv)) <= 1.5*self.frv*self.vm*self.at_muros*self.__f:
            self.__VMR= 1.5*self.frv*self.vm*self.at_muros*self.__f
    def calcPhVSR(self):
        '''
        Calcula el valor de Ph usado en la ecuación 5.4.5 de la NTC de mampostería
        '''
        self.__phVSR = self.Ash/self.sht

    def calck0(self): #TODO AGREGAR INTERPOLACION LINEAL PARA EL CASO EN DONDE K0 NO ENTRE EN EL RANGO
        '''
        Calcula el valor de k0 que se utiliza en la expresión 5.4.5
        '''
        if self.altura_libre/self.longitud <= 1.0:
            self.__k0 = 1.5

        elif self.altura_libre/self.longitud >= 1.5:
            self.__k0= 1
        
        else:
            self.__k0 = 1.625 -0.625*self.altura_libre/self.longitud

        pass
    def calccuantiah(self): #TODO VERIFICAR
        '''
        Calcula la cuantia de acero utilizada en el refuerzo horizontal de los muros
        '''
        self.__cuantiah = self.__phVSR*self.fyh
    def calck1(self): #TODO VERIFICAR
        '''
        Calcula el valor de k1 utilizado en la expresion 5.4.5
        '''
        self.__k1= 1-self.alpha*self.__cuantiah

    def calcns (self): #TODO VERIFICAR
        '''
        Calcula el valor de ns utilizado en la expresion 5.4.5
        '''
        if self.fm >= 90:
            self.__ns = 0.75

        elif self.fm <= 60:
            self.__ns= 0.55
        
        else:
            self.__ns = 1.625 -0.625*self.altura_libre/self.longitud #TODO MODIFICAR ESTA INTERPOLACION

    def calcN (self): #TODO VERIFICAR
        '''
        Valor de N utilizado en la expresion 5.4.4
        '''
        self.__N= (self.__VMR/(self.frv*self.__cuantiah*self.at_muros))*(self.__k0*self.__k1-1)+self.__ns
    def calcVSR(self): #TODO AGREGADO RECIENTEMENTE, VERIFICAR
        '''
        Calcula la carga horizontal que resiste el acero de refuerzo
        '''
        self.__VSR= self.frv*self.__cuantiah*self.__N*self.at_muros
    def calcVR(self): #TODO Comprobar que esto sea cierto
        '''
        Calcula la carga resistente total sumando lo que resiste la mampsoteria
        más lo que resiste el acero de refuerzo horizontal
        '''
        self.__VR = self.__VMR+self.__VSR
    def compVRVU (self): #TODO Comprobar
        '''
        Comprobar que VR si es mayor que VU
        '''
        if self.__VR > self.__VU:
            self.__comparacion = "Sí cumple"
        elif self.__VR <= self.__VU:
            self.__comparacion = "No cumple"
    def __str__(self) -> str:
        
        return f"id: {self.id} - len: {self.longitud} - type: {self.fe} - weight: {self.peso_mc_material} - height: {self.altura_libre}"

        pass


    ## _____________ Métodos Getter _____________

    def getF(self):
        return self.__f

    def getPesoML(self):

        return self.__peso_ml

    def getPu(self):
        return self.__pu
    
    def getPesoCm(self):
        return self.__peso_cm
    
    def getPesoCv(self):
        return self.__peso_cv
    
    def getCompPrPu(self):
        return self.__comparacion
    
    def getPr(self):
        return self.__pr

    def getAreaTransversal(self):
        return self.__area_transversal
    
    #$ AGREGADOS EL 11/04/2023  
    def getVR(self):
        return self.__VR

    

class Planta:

    def __init__(self, muros : list, losa : Losa, cv_v : float, cv_h : float) -> None:
        

        #* ___________ Digitables ___________
        self.muros : list = muros
        self.losa : Losa = losa
        self.cv_v : float = cv_v
        self.cv_h : float = cv_h
        

        #* ___________ Constantes ___________

        
        self.fr: float =0.6

        #* ___________ Calculables ___________
        self.__muros_pt : float = 0
        self.__pv : float = 0
        self.__ph :float = 0   
        self.__peso_losa : float = 0

        #* ___________ Cálculos ___________
        self.__calcMurosPT()
        self.losa.addCvv(self.cv_v)
        self.__peso_losa = self.losa.getPeso()
        

        self.calcPv()
        self.calcPh()


        #Calculamos los datos de los muros
        self.calcMurosData()

        pass

    def __calcMurosPT(self):
        
        muro : Muro

        for muro in self.muros:

            self.__muros_pt += muro.getPesoML()*muro.longitud

        pass

    def __add__(self, otherInstance):

        self.__peso_losa += otherInstance.getPesoLosa()
        self.__muros_pt += otherInstance.getMurosPT()
        
        muro : Muro

        ##dsn: ya que ambas plantas van a ocupar muros identicos se debe tener la misma cantidad de muros en ambas plantas
        ##dsn: por lo tanto, vamos a tomar los muros de la primer planta y los muros equivalentes de la segunda
        ##dsn: para sumar ambos valores de pu y pr, con los muros equivalentes
        for index in range(len(self.muros)):

            self.muros[index] += otherInstance.muros[index]
           


        return self

    


    ''' 
    En este apartado se calculan Las Cargas Verticales y Las Cargas Horizontales
    '''
    def calcPv(self):
        '''
            Calcula la carga vertical Pv
        '''

        self.__pv = self.__muros_pt + self.losa.getPesoCvv(self.cv_v)
        


    def calcPh(self):
        '''
            Calcula la carga sísmica Ph
        '''

        self.__ph = self.__muros_pt + self.losa.getPesoCvh(self.cv_h)

    def calcMurosData(self): #$ FUNCION AÑADIDA
        '''
            Calculamos el peso muerto que habrá en la losa ya sea de entrepiso o de azotea
        '''

        muro : Muro

        #recorremos la lista de muros
        for muro in self.muros:

            
            muro.calcPesoCM(self.losa.getPesoM2() + self.losa.getPesoAddM2())
            muro.calcPesoCV(self.cv_v)
            muro.calcPR()
            muro.calcPU()
            muro.CompPRPU()
            
        
            

    
    
    ## ___________ Métodos Getter ___________

    def getMurosPT(self):
        return self.__muros_pt
    
    def getLosaPT(self):
        return self.__peso_losa
    
    def getPT(self):
        return self.__muros_pt + self.losa.getPeso()
    
    def getPv(self):
        return self.__pv
    
    def getPh(self):
        return self.__ph
    
    def getPesoLosa(self): 
        return self.__peso_losa 
    def getPesoCM(self): #$ AÑADIDO
        return self.__peso_cm
    def getPesoCV(self): #$ AÑADIDO
        return self.__peso_cv