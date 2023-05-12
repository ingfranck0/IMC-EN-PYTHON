altura_en_m=float(input('Ingresa el valor de altura en metros: '))
peso_en_kg=float(input('Ingresa el valor de peso en kg: '))
IMC=peso_en_kg/altura_en_m**2
if IMC<16:
    print ('Criterio de ingreso en hospital.')
if IMC>=16 and IMC<17:
    print ('Infrapeso.')
if IMC>=17 and IMC<18:
    print ('Bajo peso.')
if IMC>=18 and IMC<25:
    print ('Peso normal (saludable).')
if IMC>=5 and IMC<30:
    print ('Sobrepeso (obesidad de grado I).')
if IMC>=30 and IMC<35:
    print ('Sobrepeso cr\u00F3nico (obesidad de grado II).')
if IMC>=35 and IMC<40:
    print ('Obesidad prem\u00F3rbida (obesidad de grado III).')
if IMC>=40:
    print ('Obesidad m\u00F3rbida (obesidad de grado IV).')
print ('Valor de IMC: ' + repr (IMC))
print()
