def area(x):
    x=  l * c
    y= l * c * x
    z= 2 * x * l + 2 * x * c
    return x, y, z

x = float(input(' valor da altura:'))
c = float(input('comprimento'))
l = float(input('largura'))
x, y, z = area(x)
print(f'area do piso {x}')
print(f'volume da sala {y}')
print(f'area da parede {z}')
