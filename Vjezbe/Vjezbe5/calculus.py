import math
import matplotlib.pyplot as plt
import numpy as np
class Calculus:
    def __init__(self, func, dotx, doty, ggranica, dgranica, gmeda, dmeda, n):
        self.func=func
        self.dotx=dotx
        self.doty=doty
        self.ggranica=ggranica
        self.dgranica=dgranica
        self.gmeda=gmeda
        self.dmeda=dmeda
        self.n=n
    
    def derivation(self):
        self.d=(math.cos(self.dotx+0.00001)-math.cos(self.dotx))/0.00001
        return self.d
    
    def gdderivation(self):
        i=self.dgranica
        lista=[]
        while i<=self.ggranica:
            self.d=(math.cos(i+0.00001)-math.cos(i))/0.00001
            lista.append(self.d)
            i=i+0.1
        return lista
    
    def pravokutnaintegracija(self):
        i=self.dmeda
        self.intg=0
        while i<=self.gmeda:
            self.intg=self.intg+math.cos(i)*0.01
            i=i+0.01
        return self.intg
    
    def trapeznaintegracija(self):
        razmak=(self.gmeda-self.dmeda)/self.n
        i=self.dmeda
        self.intg=0
        while i<=self.gmeda:
            self.intg=self.intg+math.cos(i)*razmak/2
            i=i+razmak
        return self.intg

