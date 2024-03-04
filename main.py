class Calculadora():
    def calculaMedia(self, a, b, c):
        soma = a * 2 + b * 3 + c * 5
        media = soma / 10
        return float(media)

classe = Calculadora()

a = float(input())
b = float(input())
c = float(input())

media = classe.calculaMedia(a, b, c)

print("MEDIA =", round(media, 1))
