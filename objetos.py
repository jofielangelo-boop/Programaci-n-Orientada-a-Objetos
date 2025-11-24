class Arbol:
    def _init_(self, altura, edad, nombre, longevidad):
        self.altura = altura
        self.edad = edad
        self.nombre = nombre
        self.longevidad = longevidad
        
    def tipo(self):
        pass
    
    def habitat(self):
        pass
    
    def formacion(self):
        pass
    
    def apariencia(self):
        pass
    
class Pelicula:
    def _init_(self, idioma, genero,sinapsis):
        self.idioma = idioma
        self.genero = genero
        self.sinopsis= sinapsis
    
    def escenario(self):
        pass
    
    def ambiente(self):
        pass
    
    def direccion(self):
        pass

    
class Cine:
    def _init_(self, objetivo, planificacion, formato, catalogo):
        self.objetivo = objetivo
        self.planificacion = planificacion 
        self.formato = formato
        self.catalogo = catalogo
    
    def promocion(self):
        pass
    
    def exhibicion(self):
        pass
    
    def entretenimiento(self):
        pass
    
    def equipo(self):
        pass
    
class Coche:
    def __init__(self,tipo,marca,nombre,transmision,placa,cilindraje,):
        self.tipo = tipo
        self.marca = marca
        self.nombre = nombre
        self.transmision = transmision
        self.placa = placa
        self.cilindraje = cilindraje
    def frenar(self):
        pass
    def acelerar(self):
        pass
    def embrague(self):
        pass
    
class Animal:
    def __init__(self,nombre,tamaño,tipo,tipo2,comportamiento,habitat):
        self.nombre = nombre
        self.tamaño = tamaño
        self.tipo = tipo
        self.tipo2 = tipo2
        self.comportamiento = comportamiento
        self.habitat = habitat
    def comer(self):
        pass
    def cazar(self):
        pass
    def ayudar(self):
        pass

class Dispositivos:
    def __init__(self,area,tecnologia,tipo,beneficio,seguridad):
        self.area = area
        self.tecnologia = tecnologia
        self.tipo = tipo
        self.beneficio = beneficio
        self.seguridad = seguridad
    def transmision(self):
        pass
    def costo(self):
        pass
    def desafio(sefl):
        pass  
    
class Robot:
    def __init__(self,altura,color,tipo):
        self.altura=altura
        self.color=color
        self.tipo=tipo
        
    def medico(self):
        pass
    def idustria(self):
        pass
    def azul(self):
        pass
         
class redesociales:
    def __init__(self,social,privacidad,promociones):
        self.social=social
        self.privacidad=privacidad
        self.promociones=promociones
            
    def educativo(self):
        pass
    def seguridad(self):
        pass
    def negocios(self):
        pass 

class antena:
    def __init__(self,tipos,marca,lugar):
        self.marca=marca
        self.lugar=lugar
        self.tipos=tipos
        
    def inalmabrica(self):
        pass
    def cable(self):
        pass
    def rurales(self):
        pass


class Mascota:
    def __init__(self, nombre, especie, edad, color):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.color = color
        
    def tipo(self):
        return self.especie
    
    def habitat(self):
        if self.especie == "Perro" or self.especie == "Gato":
            return "Doméstico"
        else:
            return "Depende de la especie"
    def apariencia(self):
        return self.color

class Libro:
    def __init__(self, titulo, autor, genero, paginas):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.paginas = paginas
        
    def tipo(self):
        return "Libro"
    
    def contenido(self):
        return "Depende del género"
    
    def estilo(self):
        return "Depende del autor"
    
    def longitud(self):
        return self.paginas