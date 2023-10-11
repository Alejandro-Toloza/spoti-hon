'''
Created on 11 oct. 2023

@author: test
'''

from Functions.Inicializar import Inicializar
#Importamos del archivo Inicializar, a la clase Inicializar
from selenium import webdriver

class Functions(Inicializar): #Le pasamos como parámetro la clase Inicializar
    
    def abrir_navegador(self, URL=Inicializar.URL, navegador=Inicializar.NAVEGADOR): #traemos los datos d Inicilizar
    
        self.ventanas ={} #Porsi tenemos que pasar de ventana en ventana en nuestros TCs
        if navegador == {"CHROME"}:
            self.driver = webdriver.Chrome() #Abrir Chrome
            self.driver.implicitly_wait(10) #Esperamos 10 segundos para continuar (para que se cargue porcompleto)
            self.driver.maximize_window() #Maximizamos la ventana
            return self.driver


    def tearDown(self): #Pasamos a este archivo, el tearDown de los TCs
        self.driver.quit()
    
    