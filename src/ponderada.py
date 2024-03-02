import pydobot

class InteliArm(pydobot.Dobot):
    def __init__(self, port=None, verbose=False):
        super().__init__(port=port, verbose=verbose)
    def movej_to(self, x, y, z, r, wait=False):
        self._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVJ_XYZ, wait=wait)
    def movel_to(self, x, y, z, r, wait=False):
        self._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVL_XYZ, wait=wait)
 
dobot = InteliArm(port="COM6")
print("""Exemplos de possíveis comandos:
       1. home
       2. ligar ferramenta
       3. desligar ferramenta
       4. mover x 10
       5. atual\n
       """)
while True:
     comando = input("Insira o comando desejado: ")
     comando = comando.split()

     match comando[0]:
         case "home":
             print("Indo para home")
             dobot.movej_to(243.84, 5.12, 157.94, 0)
         case "ligar":
             dobot.suck(enable=True)
         case "desligar":
             dobot.suck(enable=False)
         case "mover":
            match comando[1]:
                case "x":
                    dobot.movej_to(int(comando[2]) + dobot.pose()[0], dobot.pose()[1], dobot.pose()[2], 0)
                case "y":
                    dobot.movej_to(dobot.pose()[0], int(comando[2]) + dobot.pose()[1], dobot.pose()[2], 0)
                case "z":
                    dobot.movej_to(dobot.pose()[0], dobot.pose()[1], int(comando[2]) + dobot.pose()[2], 0)
         case "atual":
             print(f'A posição atual do robô é: {dobot.pose()}')

