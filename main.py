from rich.console import Console
from rich.table import Table
import pandas as pd
import richTables as rt
from obj_viv import Planta, Muro, Losa
console = Console()

from msg import Flag

if True:#*Enlistado de variables

    ##RH Cantidad de acero longitudinal y refuerzo transversal
    ##fc´ -> resostemcia a compresión
    ##fy´-> resistencia a compresión del acero
    ##bc -> base del castillo
    ##hc -> lado largo del castillo
    ##s -> separación de los estribos

    ##RH Orden
    #1.-área de losa
    #2.-área libre entre piso
    #3.-espesor de los muros
    #4.-peso de losa asotea
    #5.-peso de losa entre piso
    #6.-longitud total de planta alta y baja
    #7.-peso por metro lineal del muro
 
    pass

if __name__ == "__main__":

    file = pd.read_csv("MAMPOSTERIA\\ExcelTables\\tabladeentrada2.csv")

    frame = pd.DataFrame(file)

    
    muros = []
    muros2 = []

    for index in range(frame.shape[0]):

        

        fy = frame.loc[index,"fy"]
        fyc = frame.loc[index, "fyc"]
        bc =  frame.loc[index, "bc"]
        hc =  frame.loc[index, "hc"]
        fc = frame.loc[index, "fc"]
        

        castillo = Muro.Castillo(fy,fyc,bc,hc,fc,)

        id = frame.loc[index,"ID muro"]
        longitud = frame.loc[index,"longitud"]
        atributaria = frame.loc[index,"Area Tributaria"]
        fe = frame.loc[index,"FE"]
        peso_mc_material = frame.loc[index,"peso pieza"]
        altura_libre = frame.loc[index,"altura libre"]
        pesos_add = frame.loc[index,"peso add"]
        fm = frame.loc[index,"fm"]
        muro = Muro(id,longitud,fe,peso_mc_material,altura_libre,fm,castillo,atributaria,cm_muro=1.3,cv_muro=1.5,)

        muros.append(muro)

    muros2 = muros.copy()
   
    muro

    losa = Losa(80,240, peso_add_m2 = 38+5+40+50) #losa azotea

    planta = Planta(muros,losa,100,70) 

    rt.printTabla1(planta)

    
    
    planta_alta = Planta(muros,losa,100,70) #planta alta


    losa_entrepiso = Losa(80,240,peso_add_m2 = 38+53+2+40) #Losa entrepiso
    planta_baja = Planta(muros2,losa_entrepiso,190,100) #planta baja
    
    rt.printTabla_planta_alta_comp(planta_alta)
    rt.printTabla_planta_baja_comp(planta_baja,planta_alta)
    rt.printTabla_planta_alta_pu(planta_alta)
    rt.printTabla_planta_baja_pu(planta_baja,planta_alta)
    rt.printTabla_planta_alta_cvcm(planta_alta)
    rt.printTabla_planta_bajacvcm(planta_baja,planta_alta)
    rt.printTabla_planta_alta_pesomuro(planta_alta)
    rt.printTabla_planta_baja_pesomuro(planta_baja,planta_alta)
    rt.printTabla_planta_alta_pv(planta_alta)
    rt.printTabla_planta_baja_pv(planta_baja,planta_alta)
        
    
    #_______SEGUNDA PARTE________________
    rt.printTabla_planta_alta_PF(planta_alta)
    rt.printTabla_planta_baja_PF(planta_alta)
    rt.printTabla_planta_alta_VMR(planta_alta)
    rt.printTabla_planta_alta_valoresdeeficiencia(planta_alta)
    rt.printTabla_planta_alta_N(planta_alta)
    rt.printTabla_planta_alta_VSR(planta_alta)
    rt.printTabla_planta_alta_VR(planta_alta)
    rt.printTabla_planta_alta_comp(planta_alta)

    pass