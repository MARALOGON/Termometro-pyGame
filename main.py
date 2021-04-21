import pygame, sys
from pygame.locals import *



class Termometro(): #Se crea la clase Termometro por encima de la clase mainApp, porque como esta contiene la variable "termometro", que vamos a igualar a la clase "Termomentro", tiene que estar por encima
    def __init__(self):
        self.custome = pygame.image.load("images/termo1.png")

    def convertir(self, grados, toUnidad):
        resultado = 0
        if toUnidad == "F":
            resultado = grados * 9/5 +32
        elif toUnidad == "C":
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
        
        return "(:10.2f)".format(resultado)
        
    
    
class Selector(): #Tiene un atributo, que es si está en F o en C, y tiene un solo metodo que es el cambio entre ambas.
    __tipoUnidad = None
    
    def __init__(self, unidad = "C"):
        self.__customes = []
        self.__customes.append(pygame.image.load("images/posiF.png"))
        self.__customes.append(pygame.image.load("images/posiC.png"))
        
        self.__tipoUnidad = unidad

    def custome(self): #Este es el metodo que le indica a la clase mainApp que disfraz (F o C) tiene que elegir en funcion de lo que elusuario seleccione
        if self.__tipoUnidad == "F":
            return self.__customes[0]
        else:
            return self.__customes[1]
     
    def unidad(self):
        return self.__tipoUnidad
    
    def change(self):
        if self.__tipoUnidad == "F":
            self.__tipoUnidad == "C"
        else:
            self.__tipoUnidad == "F"
               
               
               

class NumberInput():
    __value = 0 #Este es el valor en numerico que se refleja en el rectangulo de input
    __strValue = "" #Se crea esta cadena con el valor introducido en value porque el metodo textBlock  necesita una cadena para la foto que tirara del valor introducido
    __position = [0, 0]
    __size = [0, 0]
    __pointsCount = 0
    
    
    def __init__(self, value=0): #Estos parametros se pueden utilizar para incializar los atributos de las calse NumberInput
        self.__font = pygame.font.SysFont("Arial", 24)
        self.value(value)
        
        '''
        try:
           self.__value = int(value) 
           self.__strValue = str(value)
        except:
            pass
        '''
        
    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) < 10 or (event.unicode == "." and self.__pointsCount == 0) : #Atributo para que imprima el caracter que se pulsa
               self.__strValue += event.unicode
               self.__value(self.__strValue)
               if event.unicode == '.':
                   self.__pointsCount += 1
                   
            elif event.key == K_BACKSPACE:
               if self.__strValue[-1] == ".":
                   self.__pointsCount -= 1
               self.__strValue = self.__strValue[:-1]
               self.__value(self.__strValue)
            
   
    def render(self): #Se crea este metodo de renderizado que nos devuelve: la foto del texto (en textBlock) y el rectangulo donde se va a posicionar la foto del texto (en rect)
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74)) #Este atributo textBlock sirve para meter el valor de la temperatura que queermos convertir. #La instruccion render sirve para renderizar, refrescar el valor que se introduzca en este input.   #Se le añade el atributo __strValue porque la instrucción espera una cadena, por eso tambien se cera ese atributo en esta clase al principio
        rect = textBlock.get_rect() #Metodo para obtener el rectangulo donde irá el textBlock
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size

        '''
        return {"fondo" : rect,
                 "texto" : textBlock}
        '''
       
        return(rect, textBlock)
    
    
    
    def value(self, val=None):
        if val == None:
            return self.__value
        else:
            val = str(val)
            print(val, "cadena")
            try:
                self.__value = float(val)
                self.__strValue = val
                if "." in self.__strValue:
                    self.pointsCount = 1
                else:
                    self.pointsCount = 0
            
            except:
                pass
  
  
  
    def width(self, val=None):
         if val == None:
            return self.__size[0]
         else:
             try:
                  self.__size[0] = int(val)
             except:
                 pass
    
    
    def height(self, val=None):
         if val == None:
            return self.__size[1]
         else:
             try:
                  self.__size[1] = int(val)
             except:
                 pass
    
              
  
    def size(self, val=None):
        if val == None:
            return self.__size
        else:
            val = str(val)
            try:
                self.__size = [int(val[0]), int(val[1])]
    
            except:
                pass
                
                
    def posX(self, val=None):
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass
        
        
    def posY(self, val=None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass  

    
    def pos(self, val=None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass


class mainApp():
    termometro = None #Atributo de la clase mainApp
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termómetro")
        
    
        self.termometro = Termometro() #Instancia del objeto-clase Termometro
        self.entrada = NumberInput()
        self.entrada.pos((106, 58))
        self.entrada.size((133,28))
        
        self.selector = Selector()

    

    def __on_close(self):
        pygame.quit()
        sys.exit()
    
    
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                    
            
                self.entrada.on_event(event)
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                    self.entrada.value(temperatura)
            
            #Pintammos el fondo de pantalla
            self.__screen.fill((244, 236, 203)) #Tupla de RGB para determianr el color de fondo de la pantalla
            
            #Pintamos el termomentro en su posicion
            self.__screen.blit(self.termometro.custome, (50, 34))
            
            #Pintamos el cuadro de texto
            text = self.entrada.render() #Obtenemos rectangulo blanco y foto del texto y lo asignamos a la variable text
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0]) #Creamos el rectangulo blanco con sus datos(posicion y tamaño) text[0]
            self.__screen.blit(text[1], self.entrada.pos()) #Pintamos la foto del texto (text[1])
           
            #Pintamos el selector
            self.__screen.blit(self.selector.custome(),(112, 153))
            
            
            pygame.display.flip() #Refresco de la pantalla

if __name__ == '__main__':
    pygame.init()
    app = mainApp()
    app.start()
    