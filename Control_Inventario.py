# Sistema de Control de Inventario
# Empresa Ricoh del Perú
# Proyecto final - Daniel,Adrián,Gerson,Javier

lista_codigos = []
lista_nombres = []
lista_categorias = []
lista_cantidades = []
lista_precio_compra = []
lista_precio_venta = []
lista_stock_minimo = []

def registrar_productos():
    while True:
        print("\n---- Registro de producto ----")
        codigo = input("Código del producto: ").strip()
        nombre = input("Nombre del producto: ").strip()
        categoria = input("Categoría: ").strip()

        try:
            cantidad_inicial = int(input("Cantidad inicial: "))
            precio_compra = float(input("Precio de compra: "))
            precio_venta = float(input("Precio de venta: "))
            stock_minimo = int(input("Stock mínimo permitido: "))
        except ValueError:
            print("Datos numéricos inválidos. Intente nuevamente.")
            continue

        lista_codigos.append(codigo)
        lista_nombres.append(nombre)
        lista_categorias.append(categoria)
        lista_cantidades.append(cantidad_inicial)
        lista_precio_compra.append(precio_compra)
        lista_precio_venta.append(precio_venta)
        lista_stock_minimo.append(stock_minimo)

        respuesta = input("¿Desea registrar otro producto? (S/N): ").strip().upper()
        if respuesta == "N":
            break

def buscar_posicion_por_codigo(codigo_busqueda):
    if codigo_busqueda in lista_codigos:
        return lista_codigos.index(codigo_busqueda)
    return -1

def registrar_movimiento():
    if not lista_codigos:
        print("No hay productos registrados.")
        return

    codigo_busqueda = input("Ingrese código de producto: ").strip()
    pos = buscar_posicion_por_codigo(codigo_busqueda)

    if pos == -1:
        print("Producto no encontrado.")
        return

    tipo_mov = input("Tipo de movimiento (I = ingreso, S = salida): ").strip().upper()

    try:
        cantidad_mov = int(input("Cantidad del movimiento: "))
    except ValueError:
        print("Cantidad inválida.")
        return

    if tipo_mov == "I":
        lista_cantidades[pos] += cantidad_mov
        print("Ingreso registrado correctamente.")
    elif tipo_mov == "S":
        if cantidad_mov <= lista_cantidades[pos]:
            lista_cantidades[pos] -= cantidad_mov
            print("Salida registrada correctamente.")
        else:
            print("Movimiento inválido: stock insuficiente.")
    else:
        print("Tipo de movimiento no válido.")

def mostrar_stock_critico():
    if not lista_codigos:
        print("No hay productos registrados.")
        return

    print("\n---- Productos con stock crítico ----")
    hay_criticos = False

    for i in range(len(lista_codigos)):
        if lista_cantidades[i] <= lista_stock_minimo[i]:
            hay_criticos = True
            print(
                f"Código: {lista_codigos[i]} | "
                f"Nombre: {lista_nombres[i]} | "
                f"Cantidad: {lista_cantidades[i]} | "
                f"Stock mínimo: {lista_stock_minimo[i]}"
            )

    if not hay_criticos:
        print("No se encontraron productos en stock crítico.")

def calcular_valor_total():
    if not lista_codigos:
        print("No hay productos registrados.")
        return

    valor_total = 0.0
    for i in range(len(lista_codigos)):
        valor_producto = lista_precio_compra[i] * lista_cantidades[i]
        valor_total += valor_producto

    print(f"\nValor económico total del inventario: {valor_total:.2f}")

def generar_reporte_general():
    if not lista_codigos:
        print("No hay productos registrados.")
        return

    print("\n---- Reporte general de inventario ----")
    for i in range(len(lista_codigos)):
        print("---------------------------------------")
        print(f"Código: {lista_codigos[i]}")
        print(f"Nombre: {lista_nombres[i]}")
        print(f"Categoría: {lista_categorias[i]}")
        print(f"Cantidad actual: {lista_cantidades[i]}")
        print(f"Precio de compra: {lista_precio_compra[i]:.2f}")
        print(f"Precio de venta: {lista_preccio_venta[i]:.2f}")
        if lista_cantidades[i] <= lista_stock_minimo[i]:
            print(">> Advertencia: Producto en stock crítico.")
    print("----------------------------------------")

def menu_principal():
    while True:
        print("\n==== MENÚ PRINCIPAL DEL INVENTARIO ====")
        print("1. Registrar productos")
        print("2. Registrar movimiento de inventario")
        print("3. Mostrar productos con stock crítico")
        print("4. Calcular valor total del inventario")
        print("5. Generar reporte general")
        print("6. Salir del sistema")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_productos()
        elif opcion == "2":
            registrar_movimiento()
        elif opcion == "3":
            mostrar_stock_critico()
        elif opcion == "4":
            calcular_valor_total()
        elif opcion == "5":
            generar_reporte_general()
        elif opcion == "6":
            print("Saliendo del sistema de inventario...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    print("=== Sistema de Control de Inventario ===")
    menu_principal()