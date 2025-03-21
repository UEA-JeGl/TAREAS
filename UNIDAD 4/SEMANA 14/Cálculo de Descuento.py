def calcular_descuento(monto_total, porcentaje_descuento=10):

    descuento= monto_total * (porcentaje_descuento/100)

    return (descuento)

# Ejecución del programa

if __name__=="__main__":

        monto1 = 5000
        monto2 = 3500

        ##llamada

        descuento1 = calcular_descuento(monto1)
        print(f"Monto de la compra es: ${monto1}, El descuento es ${descuento1}")

        ##llamada 2

        porcentaje_descuento = 30
        descuento2 = calcular_descuento(monto2, porcentaje_descuento)
        print(f"Monto de la compra es: ${monto2}, El descuento es ${descuento2}")
