class Bird:...

class Duck(Bird):
    def quack(self):
        print('Quack!')

def alert(birdie):
    birdie.quack()

def alert_duck(birdie: Duck) -> None:
    birdie.quack()

def alert_bird(birdie: Bird) -> None:
    birdie.quack()

if __name__=='__main__':
    # 1° Exemplo
    daffy = Duck()
    alert(daffy)
    alert_duck(daffy)
    alert_bird(daffy)

    # 2° Exemplo
    woody = Bird()
    try:
        alert(woody)
        alert_duck(woody)
        alert_bird(woody)
    except AttributeError as e:
        print(e)

    # Obs. A vantagem de se utilizar o mypy para verificação estatica dos codigos python está no fato de ele poder previnir futuros bugs
    # ao alertar sobre inconsistencias de tipagem no codigo fonte estatico
    # Ao rodar o comando mypy .\birds.py somos alertados de inconsistencias de tipagem desde o inicio
    # Embora em tempo de execução o primeiro exemplo funcione mesmo o mypy alertando de erros, no segundo caso não!