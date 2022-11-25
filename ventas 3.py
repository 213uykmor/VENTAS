nombre=str(input("Ingrese su nombre"));
año_nac=int(input("Ingrese su año de nacimiento"));
edad=2022-año_nac;

if edad>=18:
    semestre1=int(input("Ingrese las ventas del semestre 1"));
    semestre2 = int(input("Ingrese las ventas del semestre 2"));
    ventas=int(semestre1+semestre2);

    if semestre1>semestre2:
        mayor="1ro"
    else:
        mayor="2do";

    if ventas <100000:
        medalla="MEDALLA DE BRONCE";
        premio="UN DIA LIBRE";
    elif ventas >100001 and ventas <500001:
        medalla="PLATA";
        premio="UN DIA LIBRE";
        bono=250;
    elif ventas >500001 and ventas <100000:
        medalla = "ORO";
        premio = "UN DIA LIBRE";
        bono = 500;
    elif ventas > 500001:
        medalla = "DIAMANTE";
        premio = "DOS DIA LIBRE";
        bono = 1000;

    print("VENDEDOR:",nombre)
    print("VENTAS ANUALES:",ventas)
    print("MEJOR SEMESTRE:",mayor)
    print("MEDALLA ACREDITADA:",medalla)
    print("PREMIO:",premio)






else:
    print("Adios eres menor de edad")
