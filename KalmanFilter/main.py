
import cv2
import numpy as np

from FiltroKalman import FiltroKalman

TITLE = "Mouse Tracking con Filtro Kalman "
frame = np.ones((800,800,3),np.uint8) * 255


def mousemove(event, x, y, s, p):
    global frame, MedidaActual, PrediccionActual

    MedidaActual = np.array([[np.float32(x)], [np.float32(y)]])
    PrediccionActual = kalman.prediccion()

    cmx, cmy = MedidaActual[0], MedidaActual[1]
    cpx, cpy = PrediccionActual[0], PrediccionActual[1]

    kalman.correccion(MedidaActual)

    frame = np.ones((650,1250,3),np.uint8) * 10
    cv2.putText(frame, "Medidas: ({:.1f}, {:.1f})".format(np.float(cmx), np.float(cmy)),
                (30, 30), cv2.FONT_HERSHEY_DUPLEX, 0.8, (50, 150, 0))

    cv2.putText(frame, "Predicciones: ({:.1f}, {:.1f})".format(np.float(cpx), np.float(cpy)),(30, 60), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 255))

    cv2.putText(frame ,"<--Tierra", (80,640) ,cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255))
    cv2.putText(frame ,"Luna -->", (1080,20) ,cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255))

    cv2.circle(frame, (cmx, cmy), 10, (50, 150, 0), -1)      # punto actual medido
    cv2.circle(frame, (cpx, cpy), 10, (0, 0, 255), -1)      # punto predictido actual
 
    

    cv2.circle(frame,(0,650),80,(250,0,0),-3)
    cv2.circle(frame,(1250,0),40,(150,150,150),-3)

    

    return


cv2.namedWindow(TITLE)
cv2.setMouseCallback(TITLE, mousemove)

MatrizEstado = np.zeros((4, 1), np.float32)  # [x, y, delta_x, delta_y]
CovarianzaEstimada = np.eye(MatrizEstado.shape[0])
MatrizTransicion = np.array([[1, 0, 1, 0],[0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)
ProcesoRuidoCov = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], np.float32) * 0.001
MatrizEstadoMedida = np.zeros((2, 1), np.float32)
MatrizObservacion = np.array([[1,0,0,0],[0,1,0,0]],np.float32)
MedidaRuidoCov = np.array([[1,0],[0,1]], np.float32) * 1

kalman = FiltroKalman(X=MatrizEstado,
                      P=CovarianzaEstimada,
                      F=MatrizTransicion,
                      Q=ProcesoRuidoCov,
                      Z=MatrizEstadoMedida,
                      H=MatrizObservacion,
                      R=MedidaRuidoCov)

while True:
    cv2.imshow(TITLE,frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()