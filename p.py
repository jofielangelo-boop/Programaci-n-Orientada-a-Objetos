import RPi.GPIO as GPIO
import time

class Robot:
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo

    def encender(self):
        print(self.nombre, "está encendido.")

    def apagar(self):
        print(self.nombre, "está apagado.")

    def estado(self):
        print("Robot:", self.nombre, "Modelo:", self.modelo)

# ----------------------------------------------------------------------

class RobotObrero(Robot):
    PIN_LED = 18 

    def __init__(self, nombre, modelo, tarea):
        super().__init__(nombre, modelo)
        self.tarea = tarea
        GPIO.setup(self.PIN_LED, GPIO.OUT)
        print(f"[{self.nombre}]: GPIO {self.PIN_LED} configurado (LED Obrero).")

    def trabajar(self):
        print(self.nombre, "está realizando la tarea:", self.tarea)

    def controlar_led(self):
        print(f"[{self.nombre}]: Iniciando control de parpadeo. Presiona CTRL+C para detener y pasar al Explorador.")
        while True:
            GPIO.output(self.PIN_LED, True)
            time.sleep(1)
            GPIO.output(self.PIN_LED, False)
            time.sleep(1)

# ----------------------------------------------------------------------

class RobotExplorador(Robot):
    PIN_LED = 18 
    PIN_BUTTON = 25
    _last_state = False 

    def __init__(self, nombre, modelo, zona_exploracion):
        super().__init__(nombre, modelo)
        self.zona_exploracion = zona_exploracion
        
        GPIO.setup(self.PIN_LED, GPIO.OUT) 
        GPIO.setup(self.PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        print(f"[{self.nombre}]: GPIO {self.PIN_LED} (LED) y {self.PIN_BUTTON} (Botón) configurados.")

    def explorar(self):
        print(self.nombre, "está listo para explorar la zona:", self.zona_exploracion)
        print(f"Mantén pulsado el botón en el pin {self.PIN_BUTTON} para EXPLORAR.")
        
        while True:
            current_state = GPIO.input(self.PIN_BUTTON) == GPIO.HIGH
            
            if current_state:
                GPIO.output(self.PIN_LED, False) # ¡CORREGIDO: LED APAGA!
                if current_state != self._last_state:
                    print(self.nombre, "DETENIDO")
                # 🟢 Botón pulsado: Enciende LED y repite EXPLORANDO
                
            else:
                GPIO.output(self.PIN_LED, True) # ¡CORREGIDO: LED ENCIENDE!
                print(self.nombre, "EXPLORANDO.")
                time.sleep(0.5) # Pausa para no saturar el terminal
                # 🔴 Botón suelto: Apaga LED e imprime DETENIDO (solo una vez)
                
                # Pausa normal para el bucle cuando no está pulsado
                time.sleep(0.05)
            
            self._last_state = current_state


# ----------------------------------------------------------------------

def simulacion_robots():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    obrero = RobotObrero("R-Worker", "MK-3", "Control de iluminación")
    explorador = RobotExplorador("R-Explorer", "XJ-9", "Marte")
    
    try:
        # 1. Ejecución del Robot Obrero
        obrero.encender()
        obrero.trabajar()
        obrero.controlar_led()

    except KeyboardInterrupt:
        print("\n--- ¡Transición de Robot! ---")
        print("El Obrero se detiene. Iniciando Robot Explorador.")
        
        explorador.encender()
        try:
            # 2. Ejecución del Robot Explorador
            explorador.explorar()
        except KeyboardInterrupt:
            print("\nExplorador detenido por CTRL+C.")

    finally:
        print("\n--- Fin de Simulación ---")
        GPIO.cleanup()
        print("Pines GPIO liberados. Programa terminado.")


if __name__ == "__main__":
    simulacion_robots()