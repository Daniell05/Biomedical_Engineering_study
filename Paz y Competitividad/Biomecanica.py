# Codigo Laboratorio de biomecanica UAM

import math #Operaciones matematicas
import matplotlib.pyplot as plt #Graficas
import numpy as np #Manejo de arreglos
import os

from Funciones_Biomecanica import csv2strc, frameref

NMarkers, FrameRate, Markers_Names, NFrames, Time, Sets, Anth, Markers = csv2strc('Paola_pasillo_002')

fignum = 1 #Variable para etiquetar figuras

for i in range(len(Sets)):
    # _______________________ Antropometria _______________________

    A0 = Anth[i]['Total Height']/1000
    A1 = Anth[i]['Total Body Mass']
    A2 = Anth[i]['ASIS Breadth']/1000
    A3 = Anth[i]['Right Thigh Length']/1000
    A4 = Anth[i]['Left Thigh Length']/1000
    #A5 = Anth[i]['']
    #A6 = Anth[i]['']
    A7 = Anth[i]['Right Calf Length']/1000
    A8 = Anth[i]['Left Calf Length']/1000
    #A9 = Anth[i]['']
    #A10 = Anth[i]['']
    A11 = Anth[i]['Right Knee Diameter']/1000
    A12 = Anth[i]['Left Knee Diameter']/1000
    A13 = Anth[i]['Right Foot Length']/1000
    A14 = Anth[i]['Left Foot Length']/1000
    A15 = Anth[i]['Right Malleolus Height']/1000
    A16 = Anth[i]['Left Malleolus Height']/1000
    A17 = Anth[i]['Right Malleolus Width']/1000
    A18 = Anth[i]['Left Malleolus Width']/1000
    A19 = Anth[i]['Right Foot Breadth']/1000
    A20 =  Anth[i]['Left Foot Breadth']/1000

    # Inicialización de listas vacías
    #Listas para centros articulares
    R_Hip = []
    L_Hip = []
    R_Knee = []
    L_Knee = []
    R_Ankle = []
    R_Toe = []
    L_Ankle = []
    L_Toe = []

    #Listas para centros de masa de los segmentos
    PelvisCG = []
    R_ThighCG = []
    L_ThighCG = []
    R_CalfCG = []
    L_CalfCG = []
    R_FootCG = []
    L_FootCG = []

    #Listas para los ijk de los segmentos
    Pelvis_i = []
    Pelvis_j = []
    Pelvis_k = []

    R_Thigh_i = []
    R_Thigh_j = []
    R_Thigh_k = []
    L_Thigh_i = []
    L_Thigh_j = []
    L_Thigh_k = []

    R_Calf_i = []
    R_Calf_j = []
    R_Calf_k = []
    L_Calf_i = []
    L_Calf_j = []
    L_Calf_k = []

    R_Foot_i = []
    R_Foot_j = []
    R_Foot_k = []
    L_Foot_i = []
    L_Foot_j = []
    L_Foot_k = []


    #Listas para los ángulos
    R_Hip_alpha = []
    R_Hip_beta = []
    R_Hip_gamma = []
    L_Hip_alpha = []
    L_Hip_beta = []
    L_Hip_gamma = []

    R_Knee_alpha = []
    R_Knee_beta = []
    R_Knee_gamma = []
    L_Knee_alpha = []
    L_Knee_beta = []
    L_Knee_gamma = []

    R_Ankle_alpha = []
    R_Ankle_beta = []
    R_Ankle_gamma = []
    L_Ankle_alpha = []
    L_Ankle_beta = []
    L_Ankle_gamma = []

    # _______________________ Cinematica _______________________

    for f in range(NFrames):
        P1 = Markers[i][f][Markers_Names.index('R_Met')]
        P2 = Markers[i][f][Markers_Names.index('R_Heel')]
        P3 = Markers[i][f][Markers_Names.index('R_Mall')]
        P4 = Markers[i][f][Markers_Names.index('R_Bar2')]
        P5 = Markers[i][f][Markers_Names.index('R_Knee1')]
        P6 = Markers[i][f][Markers_Names.index('R_Bar1')]
        P7 = Markers[i][f][Markers_Names.index('R_Asis')]
        P8 = Markers[i][f][Markers_Names.index('L_Met')]
        P9 = Markers[i][f][Markers_Names.index('L_Heel')]
        P10 = Markers[i][f][Markers_Names.index('L_Mall')]
        P11 = Markers[i][f][Markers_Names.index('L_Bar2')]
        P12 = Markers[i][f][Markers_Names.index('L_Knee1')]
        P13 = Markers[i][f][Markers_Names.index('L_Bar1')]
        P14 = Markers[i][f][Markers_Names.index('L_Asis')]
        P15 = Markers[i][f][Markers_Names.index('Sacrum')]

        # ---------------- Centros Articulares ----------------
        ## ~~~~~~~~~~~~~~~ Pelvis ~~~~~~~~~~~~~~~
        vPelvis = (P14-P7)/np.linalg.norm(P14-P7)
        wPelvis = np.cross(P7-P15,P14-P15)/np.linalg.norm(np.cross(P7-P15,P14-P15))
        uPelvis = np.cross(vPelvis,wPelvis)

        PRHip = P15 + 0.598*A2*uPelvis - 0.344*A2*vPelvis - 0.29*A2*wPelvis
        PLHip = P15 + 0.598*A2*uPelvis + 0.344*A2*vPelvis - 0.29*A2*wPelvis

        R_Hip.append(list(PRHip))
        L_Hip.append(list(PLHip))
        
        ## ~~~~~~~~~~~~~~~ Rodilla derecha ~~~~~~~~~~~~~~~
        vRCalf = (P3-P5)/np.linalg.norm(P3-P5)
        uRCalf = np.cross(P4-P5,P3-P5)/np.linalg.norm(np.cross(P4-P5,P3-P5))
        wRCalf = np.cross(uRCalf,vRCalf)

        PRKnee = P5 + 0.5*A11*wRCalf

        R_Knee.append(list(PRKnee))

        ## ~~~~~~~~~~~~~~~ Rodilla izquierda ~~~~~~~~~~~~~~~
        vLCalf = (P10-P12)/np.linalg.norm(P10-P12)
        uLCalf = np.cross(P10-P12,P11-P12)/np.linalg.norm(np.cross(P10-P12,P11-P12))
        wLCalf = np.cross(uLCalf,vLCalf)

        PLKnee = P12 - 0.5*A12*wLCalf

        L_Knee.append(list(PLKnee))

        ## ~~~~~~~~~~~~~~~ Tobillo derecho ~~~~~~~~~~~~~~~
        uRFoot = (P1-P2)/np.linalg.norm(P1-P2)
        wRFoot = np.cross(P1-P3,P2-P3)/np.linalg.norm(np.cross(P1-P3,P2-P3))
        vRFoot = np.cross(wRFoot,uRFoot)

        PRAnkle = P3 + 0.016*A13*uRFoot + 0.392*A15*vRFoot + 0.478*A17*wRFoot
        PRToe = P3 + 0.742*A13*uRFoot + 1.074*A15*vRFoot - 0.187*A19*wRFoot

        R_Ankle.append(list(PRAnkle))
        R_Toe.append(list(PRToe))

        ## ~~~~~~~~~~~~~~~ Tobillo izquierdo ~~~~~~~~~~~~~~~
        uLFoot = (P8-P9)/np.linalg.norm(P8-P9);
        wLFoot = np.cross(P8-P10,P9-P10)/np.linalg.norm(np.cross(P8-P10,P9-P10));
        vLFoot = np.cross(wLFoot,uLFoot);

        PLAnkle = P10 + 0.016*A14*uLFoot + 0.392*A16*vLFoot - 0.478*A18*wLFoot;
        PLToe = P10 + 0.742*A14*uLFoot + 1.074*A16*vLFoot + 0.187*A20*wLFoot;

        L_Ankle.append(list(PLAnkle))
        L_Toe.append(list(PLToe))

        Centers = [R_Toe, R_Ankle, R_Knee, R_Hip, L_Hip, L_Knee, L_Ankle, L_Toe]

        # ---------------- Centros de Masa ----------------

        ## ~~~~~~~~~~~~~~~ Pelvis ~~~~~~~~~~~~~~~
        PM = (P14+P7)/2
        PelvisCG.append((PM+P15)/2)

        ## ~~~~~~~~~~~~~~~ Muslos ~~~~~~~~~~~~~~~
        R_ThighCG.append(PRHip+0.39*(PRKnee-PRHip))
        L_ThighCG.append(PLHip+0.39*(PLKnee-PLHip))

        ## ~~~~~~~~~~~~~~~ Piernas ~~~~~~~~~~~~~~~
        R_CalfCG.append(PRKnee+0.42*(PRAnkle-PRKnee))
        L_CalfCG.append(PLKnee+0.42*(PLAnkle-PLKnee))

        ## ~~~~~~~~~~~~~~~ Pies ~~~~~~~~~~~~~~~
        PRHeel=P2
        PLHeel=P9

        R_FootCG.append(PRHeel+0.44*(PRToe-PRHeel))
        L_FootCG.append(PLHeel+0.44*(PLToe-PLHeel))

        # ---------------- ijk de los segmentos ----------------

        ## ~~~~~~~~~~~~~~~ Pelvis ~~~~~~~~~~~~~~~
        iPelvis = wPelvis
        jPelvis = uPelvis
        kPelvis = vPelvis

        Pelvis_i.append(iPelvis)
        Pelvis_j.append(jPelvis)
        Pelvis_k.append(kPelvis)

        ## ~~~~~~~~~~~~~~~ Muslo derecho ~~~~~~~~~~~~~~~
        i1 = (PRHip-PRKnee)/np.linalg.norm(PRHip-PRKnee)
        j1 = np.cross(P6-PRHip,PRKnee-PRHip)/np.linalg.norm(np.cross(P6-PRHip,PRKnee-PRHip))
        k1 = np.cross(i1,j1)

        R_Thigh_i.append(i1)
        R_Thigh_j.append(j1)
        R_Thigh_k.append(k1)

        ## ~~~~~~~~~~~~~~~ Muslo izquierdo ~~~~~~~~~~~~~~~
        i2 = (PLHip-PLKnee)/np.linalg.norm(PLHip-PLKnee)
        j2 = np.cross(PLKnee-PLHip,P13-PLHip)/np.linalg.norm(np.cross(PLKnee-PLHip,P13-PLHip))
        k2 = np.cross(i2,j2)

        L_Thigh_i.append(i2)
        L_Thigh_j.append(j2)
        L_Thigh_k.append(k2)

        ## ~~~~~~~~~~~~~~~ Pierna derecha ~~~~~~~~~~~~~~~
        i3 = (PRKnee-PRAnkle)/np.linalg.norm(PRKnee-PRAnkle)
        j3 = np.cross(P4-PRKnee,PRAnkle-PRKnee)/np.linalg.norm(np.cross(P4-PRKnee,PRAnkle-PRKnee))
        k3 = np.cross(i3,j3)

        R_Calf_i.append(i3)
        R_Calf_j.append(j3)
        R_Calf_k.append(k3)

        ## ~~~~~~~~~~~~~~~ Pierna izquierda ~~~~~~~~~~~~~~~
        i4 = (PLKnee-PLAnkle)/np.linalg.norm(PLKnee-PLAnkle)
        j4 = np.cross(PLAnkle-PLKnee,P11-PLKnee)/np.linalg.norm(np.cross(PLAnkle-PLKnee,P11-PLKnee))
        k4 = np.cross(i4,j4)

        L_Calf_i.append(i4)
        L_Calf_j.append(j4)
        L_Calf_k.append(k4)

        ## ~~~~~~~~~~~~~~~ Pie derecho ~~~~~~~~~~~~~~~
        i5 = (P2-PRToe)/np.linalg.norm(P2-PRToe)
        k5 = np.cross(PRAnkle-P2,PRToe-P2)/np.linalg.norm(np.cross(PRAnkle-P2,PRToe-P2))
        j5 = np.cross(k5,i5)

        R_Foot_i.append(i5)
        R_Foot_j.append(j5)
        R_Foot_k.append(k5)

        ## ~~~~~~~~~~~~~~~ Pie izquierdo ~~~~~~~~~~~~~~~

        i6 = (P9-PLToe)/np.linalg.norm(P9-PLToe)
        k6 = np.cross(PLAnkle-P9,PLToe-P9)/np.linalg.norm(np.cross(PLAnkle-P9,PLToe-P9))
        j6 = np.cross(k6,i6)

        L_Foot_i.append(i6)
        L_Foot_j.append(j6)
        L_Foot_k.append(k6)

        # ---------------- Angulos Articulares ----------------

        ## ~~~~~~~~~~~~~~~ Cadera Derecha ~~~~~~~~~~~~~~~
        iRHip = np.cross(kPelvis,i1)/np.linalg.norm(np.cross(kPelvis,i1))
        aRHip = math.acos(np.dot(iRHip,jPelvis))*(np.dot(iRHip,iPelvis)/abs(np.dot(iRHip,iPelvis)))*180/np.pi
        bRHip = math.asin(np.dot(kPelvis,i1))*180/np.pi
        gRHip = -math.acos(np.dot(iRHip,j1))*(np.dot(iRHip,k1)/abs(np.dot(iRHip,k1)))*180/np.pi

        if f == 0: #Offset
            aRHip1 = aRHip
            bRHip1 = bRHip
            gRHip1 = gRHip

        R_Hip_alpha.append(aRHip-aRHip1)
        R_Hip_beta.append(bRHip-bRHip1)
        R_Hip_gamma.append(gRHip-gRHip1)

        ## ~~~~~~~~~~~~~~~ Cadera izquierda ~~~~~~~~~~~~~~~
        iLHip = np.cross(kPelvis,i2)/np.linalg.norm(np.cross(kPelvis,i2))
        aLHip = math.acos(np.dot(iLHip,jPelvis))*(np.dot(iLHip,iPelvis)/abs(np.dot(iLHip,iPelvis)))*180/np.pi
        bLHip = -math.asin(np.dot(kPelvis,i2))*180/np.pi
        gLHip = math.acos(np.dot(iLHip,j2))*(np.dot(iLHip,k2)/abs(np.dot(iLHip,k2)))*180/np.pi

        if f == 0: #Offset
            aLHip1 = aLHip
            bLHip1 = bLHip
            gLHip1 = gLHip

        L_Hip_alpha.append(aLHip-aLHip1)
        L_Hip_beta.append(bLHip-bLHip1)
        L_Hip_gamma.append(gLHip-gLHip1)

        ## ~~~~~~~~~~~~~~~ Rodilla derecha ~~~~~~~~~~~~~~~
        iRKnee = np.cross(k1,i3)/np.linalg.norm(np.cross(k1,i3))
        aRKnee = -math.acos(np.dot(iRKnee,j1))*(np.dot(iRKnee,i1)/abs(np.dot(iRKnee,i1)))*180/np.pi
        bRKnee = math.asin(np.dot(k1,i3))*180/np.pi
        gRKnee = -math.acos(np.dot(iRKnee,j3))*(np.dot(iRKnee,k3)/abs(np.dot(iRKnee,k3)))*180/np.pi

        if f == 0: #Offset
            aRKnee1 = aRKnee
            bRKnee1 = bRKnee
            gRKnee1 = gRKnee

        R_Knee_alpha.append(aRKnee-aRKnee1)
        R_Knee_beta.append(bRKnee-bRKnee1)
        R_Knee_gamma.append(gRKnee-gRKnee1)

        ## ~~~~~~~~~~~~~~~ Rodilla izquierda ~~~~~~~~~~~~~~~ 
        iLKnee = np.cross(k2,i4)/np.linalg.norm(np.cross(k2,i4))
        aLKnee = -math.acos(np.dot(iLKnee,j2))*(np.dot(iLKnee,i2)/abs(np.dot(iLKnee,i2)))*180/np.pi
        bLKnee = -math.asin(np.dot(k2,i4))*180/np.pi
        gLKnee = math.acos(np.dot(iLKnee,j4))*(np.dot(iLKnee,k4)/abs(np.dot(iLKnee,k4)))*180/np.pi

        if f == 0: # Offset
            aLKnee1 = aLKnee
            bLKnee1 = bLKnee
            gLKnee1 = gLKnee
        
        L_Knee_alpha.append(aLKnee-aLKnee1)
        L_Knee_beta.append(bLKnee-bLKnee1)
        L_Knee_gamma.append(gLKnee-gLKnee1)

        ## ~~~~~~~~~~~~~~~ Tobillo derecho ~~~~~~~~~~~~~~~
        iRAnkle = np.cross(k3,i5)/np.linalg.norm(np.cross(k3,i5))
        aRAnkle = -math.asin(np.dot(iRAnkle,j3))*180/np.pi
        bRAnkle = math.asin(np.dot(k3,i5))*180/np.pi
        gRAnkle = math.asin(np.dot(iRAnkle,k5))*180/np.pi

        if f == 0: #Offset
            aRAnkle1 = aRAnkle
            bRAnkle1 = bRAnkle
            gRAnkle1 = gRAnkle

        R_Ankle_alpha.append(aRAnkle-aRAnkle1)
        R_Ankle_beta.append(bRAnkle-bRAnkle1)
        R_Ankle_gamma.append(gRAnkle-gRAnkle1)


        ## ~~~~~~~~~~~~~~~ Tobillo izquierdo #Offset ~~~~~~~~~~~~~~~
        iLAnkle = np.cross(k4,i6)/np.linalg.norm(np.cross(k4,i6))
        aLAnkle = -math.asin(np.dot(iLAnkle,j4))*180/np.pi
        bLAnkle = -math.asin(np.dot(k4,i6))*180/np.pi
        gLAnkle = -math.asin(np.dot(iLAnkle,k6))*180/np.pi
        
        if f == 0: #Offset
            aLAnkle1 = aLAnkle
            bLAnkle1 = bLAnkle
            gLAnkle1 = gLAnkle

        L_Ankle_alpha.append(aLAnkle-aLAnkle1)
        L_Ankle_beta.append(bLAnkle-bLAnkle1)
        L_Ankle_gamma.append(gLAnkle-gLAnkle1)

    # _______________________ Matriz de marcadores _______________________
    Labels = Markers_Names
    MMarkers = np.zeros(shape = (NFrames,NMarkers,3))

    for m in range(int(NMarkers/len(Sets))):
        Marker = Labels[m]
        MMarkers[:,m,0] = Markers[i][:,Labels.index(Marker),0]
        MMarkers[:,m,1] = Markers[i][:,Labels.index(Marker),1]
        MMarkers[:,m,2] = Markers[i][:,Labels.index(Marker),2]

    # _______________________ Matriz de centros _______________________
    Order = ['R_Toe','R_Ankle','R_Knee','R_Hip','L_Hip','L_Knee','L_Ankle','L_Toe']
    MCenters = np.zeros(shape = (NFrames,len(Order),3))

    for c in range(len(Order)):
        Center = Order[c]
        for f in range(NFrames):
            MCenters[f,c,0] = Centers[c][f][0]
            MCenters[f,c,1] = Centers[c][f][1]
            MCenters[f,c,2] = Centers[c][f][2]
    
    # _______________________ Animacion _______________________

    tamlab = 0.3
    tamseg = 0.2

    Xmin = min(np.min(MMarkers[:,:,0]),np.min(MCenters[:,:,0]))
    Xmax = max(np.max(MMarkers[:,:,0]),np.max(MCenters[:,:,0]))

    Ymin = min(np.min(MMarkers[:,:,1]),np.min(MCenters[:,:,1]))
    Ymax = max(np.max(MMarkers[:,:,1]),np.max(MCenters[:,:,1]))

    Zmin = min(np.min(MMarkers[:,:,2]),np.min(MCenters[:,:,2]))
    Zmax = max(np.max(MMarkers[:,:,2]),np.max(MCenters[:,:,2]))+tamseg

    if Zmin > 0 :
        Zmin=0

    escuadra = [tamlab*Xmax,tamlab*Ymax,tamlab*Zmax]
    segmentos = [tamseg*Xmax,tamseg*Xmax,tamseg*Xmax]

    fig = plt.figure(num=fignum)
    ax = fig.add_subplot(projection='3d')
    
    print('Ingrese la velocidad para la animacion:')
    velocidad = input()
    os.system('cls')

    for a in range(0, NFrames, int(velocidad)):
        ax.clear()
        frameref(ax,[1,0,0],[0,1,0],[0,0,1],[0,0,0],'k',3,escuadra)
        # ---------------- Marcadores ----------------
        ax.scatter(MMarkers[a,:,0],MMarkers[a,:,1],MMarkers[a,:,2], color = 'b', marker = 'o', s = 8)
        # ---------------- Centros ----------------
        ax.plot(MCenters[a,:,0],MCenters[a,:,1],MCenters[a,:,2], color = 'k', linestyle='-', marker = '*', markersize = 5)
        # ------------ Vectores unitarios ------------
        frameref(ax,Pelvis_i[a],Pelvis_j[a],Pelvis_k[a],PelvisCG[a],'c',2,segmentos)
        frameref(ax,R_Thigh_i[a],R_Thigh_j[a],R_Thigh_k[a],R_ThighCG[a],'g',2,segmentos)
        frameref(ax,L_Thigh_i[a],L_Thigh_j[a],L_Thigh_k[a],L_ThighCG[a],'r',2,segmentos)
        frameref(ax,R_Calf_i[a],R_Calf_j[a],R_Calf_k[a],R_CalfCG[a],'g',2,segmentos)
        frameref(ax,L_Calf_i[a],L_Calf_j[a],L_Calf_k[a],L_CalfCG[a],'r',2,segmentos)
        frameref(ax,R_Foot_i[a],R_Foot_j[a],R_Foot_k[a],R_FootCG[a],'g',2,segmentos)
        frameref(ax,L_Foot_i[a],L_Foot_j[a],L_Foot_k[a],L_FootCG[a],'r',2,segmentos)
        # ---------------- Entorno ----------------
        ax.axes.set_xlim3d(left=Xmin, right=Xmax) 
        ax.axes.set_ylim3d(bottom=Ymin, top=Ymax) 
        ax.axes.set_zlim3d(bottom=Zmin, top=Zmax)
        ax.set_xlabel('Eje X')
        ax.set_ylabel('Eje Y')
        ax.set_zlabel('Eje Z')
        ax.set_title(str(Sets[i]),size = 25)
        plt.pause(0.1)

    fignum = fignum+1

    # _______________________ Graficas angulos _______________________
    plt.figure(num=fignum)
    plt.subplots_adjust(hspace = 0.5)
    plt.suptitle('Angulos articulares de {}'.format(Sets[i]),size = 25)

    plt.subplot(3,3,1)
    plt.plot(Time,R_Hip_alpha, color = 'g', label = 'Derecha', linewidth = 1)
    plt.plot(Time,L_Hip_alpha, color = 'r', label = 'Izquierda', linewidth = 1)
    plt.axhline(y = 0, color = 'b', linestyle = '--', linewidth = 1)
    plt.title('Sagital', size = 12)
    plt.ylabel('Cadera \n(-)Ext  (+)Flx',fontsize=10)
    plt.grid()

    plt.subplot(3,3,2)
    plt.plot(Time,R_Hip_beta, color = 'g', label = 'Derecha', linewidth = 1)
    plt.plot(Time,L_Hip_beta, color = 'r', label = 'Izquierda', linewidth = 1)
    plt.axhline(y = 0, color = 'b', linestyle = '--', linewidth = 1)
    plt.title('Frontal', size = 12)
    plt.ylabel('(-)Add  (+)Abd',fontsize=10)
    plt.grid()

    plt.subplot(3,3,3)
    plt.plot(Time,R_Hip_gamma, color = 'g', label = 'Derecha', linewidth = 1)
    plt.plot(Time,L_Hip_gamma, color = 'r', label = 'Izquierda', linewidth = 1)
    plt.axhline(y = 0, color = 'b', linestyle = '--', linewidth = 1)
    plt.title('Transversal', size = 12)
    plt.ylabel('(-)RExt  (+)RInt',fontsize=10)
    plt.grid()

    plt.subplot(3,3,4)
    plt.plot(Time,R_Knee_alpha, color = 'g', label = 'Derecha', linewidth = 1)
    plt.plot(Time,L_Knee_alpha, color = 'r', label = 'Izquierda', linewidth = 1)
    plt.axhline(y = 0, color = 'b', linestyle = '--', linewidth = 1)
    plt.title('Sagital', size = 12)
    plt.ylabel('Rodilla \n(-)Ext  (+)Flx',fontsize=10)
    plt.grid()

    plt.subplot(3,3,5)
    plt.plot(Time,R_Knee_beta, color = 'g', label = 'Derecha', linewidth = 1)
    plt.plot(Time,L_Knee_beta, color = 'r', label = 'Izquierda', linewidth = 1)
    plt.axhline(y = 0, color = 'b', linestyle = '--', linewidth = 1)
    plt.title('Frontal', size = 12)
    plt.ylabel('(-)Varo  (+)Valgo',fontsize=10)
    plt.grid()

    plt.subplot(3,3,6)
    plt.plot(Time,R_Knee_gamma, color = 'g', label = 'Derecha', linewidth = 1)
    plt.plot(Time,L_Knee_gamma, color = 'r', label = 'Izquierda', linewidth = 1)
    plt.axhline(y = 0, color = 'b', linestyle = '--', linewidth = 1)
    plt.title('Transversal', size = 12)
    plt.ylabel('(-)RExt  (+)RInt',fontsize=10)
    plt.grid()

    plt.subplot(3,3,7)
    plt.plot(Time,R_Ankle_alpha, color = 'g', label = 'Derecha', linewidth = 1)
    plt.plot(Time,L_Ankle_alpha, color = 'r', label = 'Izquierda', linewidth = 1)
    plt.axhline(y = 0, color = 'b', linestyle = '--', linewidth = 1)
    plt.title('Sagital', size = 12)
    plt.ylabel('Tobillo \n(-)Planti  (+)Dorsi',fontsize=10)
    plt.grid()

    plt.subplot(3,3,8)
    plt.plot(Time,R_Ankle_beta, color = 'g', label = 'Derecha', linewidth = 1)
    plt.plot(Time,L_Ankle_beta, color = 'r', label = 'Izquierda', linewidth = 1)
    plt.axhline(y = 0, color = 'b', linestyle = '--', linewidth = 1)
    plt.title('Frontal', size = 12)
    plt.ylabel('(-)Ever  (+)Inv',fontsize=10)
    plt.grid()

    plt.subplot(3,3,9)
    plt.plot(Time,R_Ankle_gamma, color = 'g', label = 'Derecha', linewidth = 1)
    plt.plot(Time,L_Ankle_gamma, color = 'r', label = 'Izquierda', linewidth = 1)
    plt.axhline(y = 0, color = 'b', linestyle = '--', linewidth = 1)
    plt.title('Transversal', size = 12)
    plt.ylabel('(-)PInt  (+)PExt',fontsize=10)
    plt.grid()

    fignum = fignum+1

plt.show()
