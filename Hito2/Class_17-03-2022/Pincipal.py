from Math_utils import Math_utils

instancia = Math_utils("App Daniel LQ", "0.1", "2022")
instancia.print_app()

print(instancia.generate_serie(1, 10, 1))
print(instancia.generate_serie(2, 10, 2))

instancia.extention_from_ci("10021571LP")

instancia.generate_naturales(15)
instancia.generate_pares(15)