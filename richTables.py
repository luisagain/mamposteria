from rich.table import Table as tb
from rich.console import Console as cr
from obj_viv import Planta, Muro

from msg import Flag


def printTabla1(planta : Planta):

    # Lista de nombres de columnas
    column_names = ["ID muro", "longitud", "FE","Area Transvesal", "Area Tributaria","fy", "fyc", "f'c","f'm"]

    # Crear una tabla con las columnas
    table = tb(show_header=True, header_style="bold magenta", *column_names,title="\n\nDatos de muros")


    muro : Muro
    # Agregar las filas a la tabla
    for muro in planta.muros:
        
        table.add_row\
            (f"{muro.id}",\
            f"{muro.longitud}",\
            f"{muro.fe}",\
            f"{muro.getAreaTransversal()}", \
            f"{muro.at_muros}",\
            f"{muro.castillo.fy/10000}", \
            f"{muro.castillo.fyc/10000}", \
            f"{muro.castillo.fc/10000}", \
            f"{muro.fm/10000}",)

    # Imprimir la tabla
    console = cr()
    console.print(table)

    pass


#__________________COMPARACION___________________________
def printTabla_planta_alta_comp(planta_alta : Planta):
    muro : Muro
    #Lista de nombres de columnas
    column_names= ["Pu","PR","VER SI CUMPLE"]
    # Crear una tabla con las columnas
    table = tb(show_header=True, header_style="bold magenta",*column_names,title="\n\nComparacion de Pu y PR En Planta Alta")

    
    
    
    for muro in planta_alta.muros:

        
        table.add_row(f"{muro.getPu()}",f"{muro.getPr()}",f"{muro.getCompPrPu()}")

    #Imprimir la tabla
    console = cr()
    console.print(table)

def printTabla_planta_baja_comp(planta_baja : Planta,planta_alta : Planta):

    planta_baja+=planta_alta
    muro : Muro
    #Lista de nombres de columnas
    column_names= ["Pu","PR","VER SI CUMPLE"]
    # Crear una tabla con las columnas
    table = tb(show_header=True, header_style="bold magenta",*column_names,title="\n\nComparacion de Pu y PR En Planta Baja")

    
    
    
    for muro in planta_baja.muros:

        
        table.add_row(f"{muro.getPu()}",f"{muro.getPr()}",f"{muro.getCompPrPu()}")

    #Imprimir la tabla
    console = cr()
    console.print(table)

#_____________________CALCULO DE PU________________________________

def printTabla_planta_alta_pu(planta_alta : Planta):
    muro : Muro
    #Lista de nombres de columnas
    column_names= ["ID Muro","Pu"]
    # Crear una tabla con las columnas
    table = tb(show_header=True, header_style="bold magenta",*column_names,title="\n\nValores de Pu de cada muro de la Planta Alta")

    for muro in planta_alta.muros:

        
        table.add_row(f"{muro.id}",f"{muro.getPu()}")
    #Imprimir la tabla
    console = cr()
    console.print(table)


def printTabla_planta_baja_pu(planta_baja : Planta, planta_alta : Planta):
    planta_baja+= planta_alta
    muro : Muro
    #Lista de nombres de columnas
    column_names= ["ID Muro","Pu"]
    # Crear una tabla con las columnas
    table = tb(show_header=True, header_style="bold magenta",*column_names,title="\n\nValores de Pu de cada muro de la Planta Baja")

    for muro in planta_baja.muros:

        
        table.add_row(f"{muro.id}",f"{muro.getPu()}")
    #Imprimir la tabla
    console = cr()
    console.print(table)


#____________________CARGA VIVA, CARGA MUERTA___________________________________________________
def printTabla_planta_alta_cvcm(planta_alta: Planta):
    muro : Muro 
    #Lista de nombres de columnas
    column_names= ["ID Muro","Carga Muerta","Carga Viva"]
    #Crear Una Tabla Con Columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names,title="\n\nValores de Carga Viva y de Carga Muerta para cada muro de la Planta Alta")
    for muro in planta_alta.muros:

        
        table.add_row(f"{muro.id}",f"{muro.getPesoCm()}",f"{muro.getPesoCv()}")
    #Imprimir la tabla
    console = cr()
    console.print(table)

def printTabla_planta_bajacvcm(planta_baja : Planta, planta_alta: Planta):
    planta_baja+planta_alta
    muro : Muro 
    #Lista de nombres de columnas
    column_names= ["ID Muro","Carga Muerta","Carga Viva"]
    #Crear Una Tabla Con Columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names,title="\n\nValores de Carga Viva y de Carga Muerta para cada muro de la Planta Baja")
    for muro in planta_baja.muros:

        
        table.add_row(f"{muro.id}",f"{muro.getPesoCm()}",f"{muro.getPesoCv()}")
    #Imprimir la tabla
    console = cr()
    console.print(table)



#_______________Peso Muro____________________
def printTabla_planta_alta_pesomuro(planta_alta: Planta):
    muro : Muro 
    #Lista de nombres de columnas
    column_names= ["ID Muro","Peso de Muro"]
    #Crear Una Tabla Con Columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names,title="Peso del Muro de Planta Alta")
    for muro in planta_alta.muros:

        
        table.add_row(f"{muro.id}",f"{muro.getPesoML()}")
    #Imprimir la tabla
    console = cr()
    console.print(table)

def printTabla_planta_baja_pesomuro(planta_baja : Planta,planta_alta: Planta):
    planta_baja+= planta_alta
    muro : Muro 
    #Lista de nombres de columnas
    column_names= ["ID Muro","Peso de Muro"]
    #Crear Una Tabla Con Columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names,title="Peso del Muro de Planta Baja")
    for muro in planta_alta.muros:

        
        table.add_row(f"{muro.id}",f"{muro.getPesoML()}")
    #Imprimir la tabla
    console = cr()
    console.print(table)


#_____________PV____________________________
def printTabla_planta_alta_pv(planta_alta: Planta):
    
   
    muro : Muro 
    planta : Planta
    
    #Lista de nombres de columnas
    column_names= ["ID Muro","Pv"]
    #Crear Una Tabla Con Columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names,title="PV")
    for muro in planta_alta.muros:

        
        table.add_row(f"{muro.id}",f"{planta_alta.getPv()}")
    #Imprimir la tabla
    console = cr()
    console.print(table)

def printTabla_planta_baja_pv(planta_baja : Planta,planta_alta: Planta):
    
    planta_baja+= planta_alta
    muro : Muro 
    planta : Planta
    
    #Lista de nombres de columnas
    column_names= ["ID Muro","Pv"]
    #Crear Una Tabla Con Columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names,title="PV de Planta Baja")
    for muro in planta_alta.muros:

        
        table.add_row(f"{muro.id}",f"{planta_baja.getPv()}")
    #Imprimir la tabla
    console = cr()
    console.print(table)

#_______________PH____________________
def printTabla_planta_alta_ph(planta_alta: Planta):
    planta : Planta
    muro : Muro 
    #Lista de nombres de columnas
    column_names= ["ID Muro","Ph"]
    #Crear Una Tabla Con Columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names,title="PH de Planta Alta")
    for muro in planta_alta.muros:

        
        table.add_row(f"{muro.id}",f"{planta_alta.getPh()}")
    #Imprimir la tabla
    console = cr()
    console.print(table)

def printTabla_planta_baja_ph(planta_baja : Planta,planta_alta: Planta):
    planta_baja+= planta_alta
    planta : Planta
    muro : Muro 
    #Lista de nombres de columnas
    column_names= ["ID Muro","Ph"]
    #Crear Una Tabla Con Columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names,title="PH de Planta Baja")
    for muro in planta_alta.muros:

        
        table.add_row(f"{muro.id}",f"{planta_baja.getPh()}")
    #Imprimir la tabla
    console = cr()
    console.print(table)


def printTabla_planta_baja_PF(planta_alta: Planta):
   
    planta : Planta
    muro : Muro

    #Lista de nombres de columnas
    column_names = ["ID Muro","P"]

    #Crear una tabla con las columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names,title="Carga P en la planta baja")
    for muro in planta_alta.muros:

        table.add_row(f"{muro.id}",f"{muro.getP()+muro.getP()}")
    
    #Imprimir tabla

    console = cr()
    console.print(table)







#TODO AGREGAR DE AQUI PARA ABAJO LA PLANTA BAJA TAMBIEN EN CADA UNO DE LOS ESPACIOS
#___________________Valores de P y F para cada muro____________________

def printTabla_planta_alta_PF(planta_alta: Planta):
    muro : Muro

    #lista de nombre de las columnas
    column_names= ["ID Muro","Carga P","f"]

    #Crear uuna tabla con columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names, title="Variables necesarias para calcular VMR")
    for muro in planta_alta.muros:
        
        table.add_row(f"{muro.id}",f"{muro.getP()}",f"{muro.getF()}")
    #Imprimir tabla
    console = cr()
    console.print(table)

#___________________________RESISTENCIA A CORTANTE DE LA MAMPOSTERIA ____________________

def printTabla_planta_alta_VMR(planta_alta: Planta):
    planta  : Planta
    muro : Muro

    #Lista de nombre de las columnas
    column_names = ["ID Muro","VMR"]
    
    #Crear una tabla con las columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names, title="RESISTENCIA A CORTANTE DE LA MAMPOSTERIA")
    for muro in planta_alta.muros:


        table.add_row(f"{muro.id}",f"{muro.getVMR()}")
    
    #Imprimir tabla
    console = cr()
    console.print(table)

#___________________Valores para calcular la eficiencia____________________

def printTabla_planta_alta_valoresdeeficiencia(planta_alta: Planta):
    muro : Muro

    #Lista de nombre de las columnas
    column_names = ["ID Muro","k0","k1","ns","cuantía","Área Transversal"]

    #Crear una talba con las columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names, title="Datos necesarios para calcular la eficiencia")
    for muro in planta_alta.muros:

        table.add_row(f"{muro.id}",f"{muro.getk0()}",f"{muro.getk1()}",f"{muro.getns()}",f"{muro.getcuantia()}",f"{muro.getAreaTransversal()}")
    
    #Imprimir tabla
    console = cr()
    console.print(table)


def printTabla_planta_alta_N(planta_alta:Planta):
    muro:Muro

    #Lista de nombre de las columnas
    column_names = ["ID MurO","Factor de Eficiencia"]

    #Crear una tabla con las columnas
    table = tb (show_header=True,header_style="bold magenta",*column_names, title="Valor del factor de eficiencia para cada muro")
    for muro in planta_alta.muros:

        table.add_row(f"{muro.id}",f"{muro.getN()}")
    
    #Imprimir tabla
    console = cr()
    console.print(table)


#______________________ RESISTENCIA A CORTANTE DEL ACERO DE REFUERZO_________________
def printTabla_planta_alta_VSR(planta_alta: Planta):
    muro : Muro

    #Lista de nombre de las columnas
    column_names = ["ID Muro","VSR"]

    #Crear una talba con las columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names, title="Resistencia a cortante del acero de refuerzo")
    for muro in planta_alta.muros:

        table.add_row(f"{muro.id}",f"{muro.getVSR()}")
    
    #Imprimir tabla
    console = cr()
    console.print(table)

#__________________SUMA DE RESISTENCIA DE LA MAMPOSTERIA Y DEL ACERO________________
def printTabla_planta_alta_VR(planta_alta: Planta):
    muro : Muro

    #Lista de nombre de las columnas
    column_names = ["ID Muro","VR"]

    #Crear una talba con las columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names, title="Resistencia total a cortante del muro")
    for muro in planta_alta.muros:

        table.add_row(f"{muro.id}",f"{muro.getVR()}")
    
    #Imprimir tabla
    console = cr()
    console.print(table)


#______________________COMPARACION DE VR CON VU Y VER SI CUMPLE O NO CUMPLE_________
def printTabla_planta_alta_comp(planta_alta: Planta):
    muro : Muro
    column_names = ["ID Muro", "VR", "VU","VER SI CUMPLE"]

    #Crear una tabla con las columnas
    table = tb(show_header=True,header_style="bold magenta",*column_names, title="COMPARACION DE VR Y VU")
    for muro in planta_alta.muros:

        table.add_row(f"{muro.id}",f"{muro.getVR()}",f"{muro.getVU()}",f"{muro.getCompVRVu()}")

    #Imprimir tabla
    console = cr()
    console.print(table)
