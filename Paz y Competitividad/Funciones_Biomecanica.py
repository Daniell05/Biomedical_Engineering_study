def csv2strc(FileName):
    # CSV2STRC - Getting 3D data from a csv file

    #csv2strc processes '.csv' files exported from Optitrack's Motive to get  MoCap data as markers 'cloud, markers' labels, time vector, total number  of markers, total number of frames and the frame rate of the MoCap file. This function only works with Markersets and not with Rigid Bodies or Skeletons.


    #This script runs with files exported from Motive 2.1.2 and was tested in Python.

    #For running this, you must upload the '.csv' file to the runtime environment.

    #______________________________________________________________________________________________


    # Input parameters:
        # FileName:  file name without '.csv' extension.

    # Output parameters:
        # Time: Vector with the elapsed time for each frame, starting from zero to the duration of the capture sesion.
        # NFrames: Is the total number of captured frames.
        # NMarkers: Is the total number of markers for each person.
        # Markers_Names: Is the list of markers names without repeating name
        # FrameRate: Is the frame rate of the MoCap system.
        # Sets: Name of all markersets present in the file.
        # Anthropometry: In biomechanics, antrhopometric data for joint centers estimation. This info should be arranged in a different MS Excel file that should be named "Anatomics_MarkersetName.xlsx" where MarkersetName is the name of the declared markerset in Motive. 
        # Markers: Matirx with 3D info (XYZ) for each marker, arranged by the total number of Markersets.

    # Each marker consists in a Frames by 3 matrix, where each column is X, Y and Z axis values for every frame.

    # This software is part of the public domain, and may therefore be distributed freely for any non-commercial use. Contributions, improvements, and especially bug fixes of the code are more than welcome.

    # Daniel Felipe Lasso Mora (danielf.lassom@autonoma.edu.co)
    # Juan Pablo Angel Lopez (jangel@autonoma.edu.co)
    # November, 2022

    import pandas as pd
    import numpy as np

    FullFile = pd.read_csv(FileName+'.csv', delimiter = ',') 
    FrameRate = float(FullFile.columns[7])
    NFrames = int(FullFile.columns[13])

    NoHeaderFile = pd.read_csv(FileName+'.csv', header = 2) 
    NMarkers = int((NoHeaderFile.shape[1]-2)/3)

    Data3D = np.zeros(shape = (NoHeaderFile.shape[1], NFrames))
    ColumnNames = list(NoHeaderFile.columns)

    for i in range(Data3D.shape[0]):
        Data3D[i] = NoHeaderFile[ColumnNames[i]][3:]

    TFrames = Data3D[0]
    Time = Data3D[1]

    Markers = np.zeros(shape = (NFrames, NMarkers, 3))

    x0 = 2
    y0 = 3
    z0 = 4

    for i in range(NMarkers):
        for j in range(NFrames):
            Markers[j][i][0] = Data3D[x0][j]
            Markers[j][i][2] = Data3D[y0][j] #Y de optitrack es Z
            Markers[j][i][1] = -1*Data3D[z0][j] #Z de optitrack es -Y
        x0 = x0+3
        y0 = y0+3
        z0 = z0+3

    DataL = ColumnNames[2:]
    DataL2 = ColumnNames[2:]

    for i in range(len(DataL)):
        tmp = DataL[i].split(':')
        DataL[i] = tmp[0]
        DataL2[i] = tmp[1]

    Sets = [] #Lista Vacía
    for item in DataL:
        if item not in Sets:
            Sets.append(item)
    NSets = len(Sets)

    Labels = ColumnNames[2:]

    for i in Labels:
        if '.1' in i: 
            Labels.remove(i)

    for i in Labels:
        if '.2' in i: 
            Labels.remove(i) #Todas las etiquetas sin repetirse


    for i in DataL2:
        if '.1' in i:
            DataL2.remove(i)

    for i in DataL2:
        if '.2' in i:
            DataL2.remove(i)

    Markers_Names = [] #Lista Vacía
    for item in DataL2:
        if item not in Markers_Names:
            Markers_Names.append(item)

    AntropoFile = [] #Lista vacía
    Anth = [] #Lista vacía

    for i in range(len(Sets)):
        AntropoFile.append(pd.read_excel('Anatomics_'+Sets[i]+'.xlsx'))
        tmp = AntropoFile[i].drop(['Units'], axis=1)
        tmp = tmp.set_index('Variable').T.to_dict('index')
        tmp = tmp['Value']
        Anth.append(tmp)
        

    Markers_Raw = [] #Lista Vacía

    start = 0
    end = int(NMarkers/len(Sets))
    
    for i in range(len(Sets)):
        tmp = Markers[:,start:end,:]
        Markers_Raw.append(tmp)
        start = end
        end = end+int(NMarkers/len(Sets))

    return NMarkers, FrameRate, Markers_Names, NFrames, Time, Sets, Anth, Markers_Raw

def frameref(figure,vi,vj,vk,centro,color,width,tam):
    from colorama import init, Fore, Back, Style

    # frameref - Representación gráfica de un marco de referencia

    #This script runs with files exported from Motive 2.1.2 and was tested in Python.

    #______________________________________________________________________________________________

    # Input parameters:
        # figure:  Figure where the frame of reference will plotted
        # vi: Vector i of the segment
        # vj: Vector j of the segment
        # vk: Vector k of the segment
        # centro: Center of mass that establishes the position of the vectors
        # color: Specifies the color for the representation
        # width: Specifies the arrow width for the representation
        # tam: Vector of sizes for each arrow [X,Y,Z] 

    
    # Daniel Felipe Lasso Mora (danielf.lassom@autonoma.edu.co)
    # Juan Pablo Angel Lopez (jangel@autonoma.edu.co)
    # November, 2022

    if len(vi)>3 or len(vj)>3 or len(vk)>3 or len(tam)>3 or len(centro)>3:
        raise ValueError(Fore.RED+'Alguna de las variables de entrada excede el tamaño')
    else:
        if len(vi)<3 or len(vj)<3 or len(vk)<3 or len(tam)<3 or len(centro)<3:
            raise ValueError(Fore.RED+'Alguna de las variables de entrada no alcanza el tamaño')

    figure.quiver(centro[0], centro[1], centro[2], vi[0], vi[1], vi[2], color = color, linewidths = width, length = tam[0])
    figure.quiver(centro[0], centro[1], centro[2], vj[0], vj[1], vj[2], color = color, linewidths = width, length = tam[1])
    figure.quiver(centro[0], centro[1], centro[2], vk[0], vk[1], vk[2], color = color, linewidths = width, length = tam[2])
