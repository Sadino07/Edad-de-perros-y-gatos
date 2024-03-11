####
#Desea conocer la edad de un perro o un gato?
#
# 


while True:
    try:
        eleccion = input('Vamos a averiguar la edad de un perro o de un gato en años humanos \n'
                        'Primero debes elegir ... un perro o un gato? ')
        eleccion = eleccion.lower()
#edad de perros
        if (eleccion == 'perro') or (eleccion == 'un perro') or (eleccion == 'de un perro'):
            human_years = input('Buena eleccion! El mejor amigo del hombre! \
                ...y de la mujer tambien porsupuesto \n'
                'Ingrese solo en numeros enteros, cuantos años "humanos" tiene? ')
            humanYears = int(human_years)
            def validar_humanYears(humanYears):
                while humanYears < 1:
                    print ("Los años a ingresar deben ser mayor o igual a 1")
                    humanYears = int(input("Ingrese el numero de años nuevamente: "))
                return humanYears  

            def human_years_cat_years_dog_years(human_years):
                if humanYears > 0:
                    if humanYears <= 1:
                        dogYears = 15
                    elif humanYears == 2:
                        dogYears = 24
                    else:
                        dogYears = ((humanYears - 2) *5) +24
                        return humanYears, dogYears
                else:
                    print('La edad introducida no es valida')

            humanYears, dogYears = human_years_cat_years_dog_years(human_years)

            print(f'En {humanYears} años "humano" \nel perro tiene {dogYears} años de edad')
            seguir_o_terminar = input('Desea iniciar el programa nuevamente? si/no ')
            if (seguir_o_terminar == 'no'):
                break
            else:
                continue
#edad de gatos
        elif (eleccion == 'gato') or (eleccion == 'un gato') or (eleccion == 'de un gato'):
            human_years = input('Purrrfecto!\
                mi hermana los adora, a mi solo me muerden :( \n'
                'Ingrese solo en numeros enteros, cuantos años "humanos" tiene? ')
            humanYears = int(human_years)
            def validar_humanYears(humanYears):
                while humanYears < 1:
                    print ("Los años a ingresar deben ser mayor o igual a 1")
                    humanYears = int(input("Ingrese el numero de años nuevamente: "))
                return humanYears  

            def human_years_cat_years_dog_years(human_years):
                if humanYears > 0:
                    if humanYears <= 1:
                        catYears = 15
                    elif humanYears == 2:
                        catYears = 24
                    else:
                        catYears = ((humanYears - 2) *4) + 24             
                    return humanYears, catYears
                else:
                    print('La edad introducida no es valida')

            humanYears, catYears = human_years_cat_years_dog_years(human_years)

            print(f'En {humanYears} años "humano" \nel gato tiene {catYears} años')
            seguir_o_terminar = input('Desea iniciar el programa nuevamente? si/no ')
            if (seguir_o_terminar == 'no'):
                break
            else:
                continue

        # elif eleccion == 'ambos' or eleccion == 'de ambos':
            human_years = input('años humano: ')
            humanYears = int(human_years)

            def validar_humanYears(humanYears):
                while humanYears < 1:
                    print ("El año debe ser mayor o igual a 1.")
                    humanYears = int(input("Ingrese el año nuevamente: "))
                return humanYears  

            def human_years_cat_years_dog_years(human_years):
                if humanYears > 0:
                    if humanYears <= 1:
                        catYears = 15
                        dogYears = 15
                    elif humanYears == 2:
                        catYears = 24
                        dogYears = 24
                    else:
                        catYears = ((humanYears - 2) *4) + 24 
                        dogYears = ((humanYears - 2) *5) +24
                    
                    return humanYears, catYears, dogYears
                else:
                    print('La edad introducida no es valida')

            humanYears, catYears, dogYears = human_years_cat_years_dog_years(human_years)

            print(f'En {humanYears} años humano \n el perro tiene {dogYears} años \n y el gato tiene {catYears} años')
        else:
            print('Acaba de ingresar un dato no valido, intentemos de nuevo!')
    except ValueError:
        print('Intente nuevamente')
