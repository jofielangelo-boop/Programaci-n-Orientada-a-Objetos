import time
import ledbcm
import ledboard
import ledbbc
import ledbor

def ejecutar():

    ledbcm.b()
    time.sleep(5)
    print (" Se acabo")

def ejecutar2():

    ledboard.b()
    time.sleep(5)
    print ("S")
def ejecutar3():

    ledbbc.b()
    time.sleep(5)
    print ("S")
def ejecutar4():

    ledbor.b()

if __name__ =="__main__":
    ejecutar()
    ejecutar1()
    ejecutar2()
    ejecutar3()
    ejecutar4()




