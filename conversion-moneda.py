# Enlace de Diagrama de flujo
#https://miro.com/welcomeonboard/bnI4dUljVkNIQTBudWl3TDlnN3o3Zi9xc3NnTGF3WTltc1JqVk8wODY4OUJMQlVsVE0yRWlpWmlFSXhNMjEyT2RLOG1EOXdJT0hYc3kyMHRMamRpY012KzY4cG5HdWp5U3B1MXlENUpuMUZWaVkrOFo2WWtRdVIrY0s1eXR0K2chZQ==?share_link_id=899620145357

# Paso 1: Definir el valor actual del Euro y Dolar con respecto al Peso Mexicano

tipo_cambio_eur_a_mxm = 23.70  # en un caso mas realista habria que consumir informacion actualizada de BDD 0 API
tipo_cambio_usd_a_mxm = 20.75  # en un caso mas realista habria que consumir informacion actualizada de BDD 0 API


# Paso 2: Solicitar al usuario el; tipo de conversion(Euro a Mex o Dolar a Mex)

tipo_conversion = input("Ingrese la moneda origen para la conversion(EUR/USD): ")

# Paso 3: Solicitar al usuario el monto a convertir

monto_convertir = float(input("Ingrese el monto a convertir: "))


# Paso 4: Realizar la conversion utilizando el tipo de cambio correspondiente
# Paso 5: Mostrar el resultado de la conversion  al usuario

if tipo_conversion.upper() == "EUR": # en esta linea esta la funcion que convierte a mayuscula
   resultado = monto_convertir * tipo_cambio_eur_a_mxm
   print("El resultado de la conversion de EUR a MXM es:",resultado)
elif tipo_conversion.upper() == "USD":
   resultado = monto_convertir * tipo_cambio_usd_a_mxm
   print("El resultado de la conversion de USD a MXM es:",resultado)
else:
   print("No esta disponible tipo de conversion en el actualmente")
