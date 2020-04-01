

import numpy as np
from numpy.linalg import inv


class FiltroKalman:
    """
    Filtro Simple Kalman
    """

    def __init__(self, X, F, Q, Z, H, R, P, B=np.array([0]), M=np.array([0])):
        """
        Args:
            X: Estimacion  a priori
            P: Covarianza del error a X
            F: transicion de estados
            B: matriz de control
            M: vector de control
            Q: Proceso ruido covarianza
            Z: Medida del estado X
            H: estado de observacion
            R: Observacion de ruido covarianza 
        """
        self.X = X
        self.P = P
        self.F = F
        self.B = B
        self.M = M
        self.Q = Q
        self.Z = Z
        self.H = H
        self.R = R

    def prediccion(self):
        """
        Prediccion del estado futuro 
        Args:
            self.X: estado de estimacion
            self.P: Estimacion de covarianza
            self.B: matriz de control
            self.M: vector de control
        Returns:
            updated self.X
        """
        # Project the state ahead
        self.X = self.F @ self.X + self.B @ self.M
        self.P = self.F @ self.P @ self.F.T + self.Q

        return self.X

    def correccion(self, Z):
        """
        Actualiza el filtro kalma desde una medida
        Args:
            self.X: estado de estimacion
            self.P: Estimacion de covarianza
            Z: esttado de medida
        Returns:
             X actuializado
        """
        K = self.P @ self.H.T @ inv(self.H @ self.P @ self.H.T + self.R)
        self.X += K @ (Z - self.H @ self.X)
        self.P = self.P - K @ self.H @ self.P

        return self.X