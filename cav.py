import math
def area_cilindro(radio,altura):
    area = 2*math.pi*radio*(radio+altura)
    return area
def volumen_cilindro(radio,altura):
    volumen = math.pi*(radio**2)*altura
    return volumen



def main():
    radio = float(input())
    altura = float(input())
    
    area = area_cilindro(radio,altura)
    volumen = volumen_cilindro(radio,altura)
    
    print("area=",round(area,2))
    print("volumen=",round(volumen,2))
    
main()
    