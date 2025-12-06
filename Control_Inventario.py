# Sistema de Control de Inventario
# Empresa Ricoh del Perú
# Proyecto final - Daniel, Adrián, Gerson, Javier
 
# Listas principales del inventario
lista_codigos = []
lista_nombres = []
lista_categorias = []
lista_cantidades = []
lista_precio_compra = []
lista_precio_venta = []
lista_stock_minimo = []
 
# Moneda global
moneda_global = None
simbolo_moneda = ""
 
def configurar_moneda():
    """Configura la moneda global del sistema: Soles o Dólares."""
    global moneda_global, simbolo_moneda
 
    while True:
        print("Configuración inicial de moneda.")
        print("Seleccione la moneda para todo el inventario:")
        print("S = Soles")
        print("D = Dólares")
        moneda = input("Ingrese S o D: ").strip().upper()
 
        if moneda == "S":
            moneda_global = "S"
            simbolo_moneda = "S/"
            print("Moneda configurada: Soles (S/)")
            break
        elif moneda == "D":
            moneda_global = "D"
            simbolo_moneda = "$"
            print("Moneda configurada: Dólares ($)")
            break
        else:
            print("⚠ Opción inválida. Por favor ingrese S o D.\n")
 
def registrar_productos():
    """Proceso 1: Registro inicial de productos con validación de códigos repetidos."""
    while True:
        print("\n---- Registro de producto ----")
        codigo = input("Código del producto (o 'X' para volver al menú): ").strip().upper()
 
        # Permitir volver al menú sin registrar nada
        if codigo == "X":
            print("↩ Volviendo al menú principal. No se registró un nuevo producto.")
            break
 
        # Validar si el código ya existe
        if codigo in lista_codigos:
            print("⚠ El código ingresado ya está registrado. Intente con uno diferente.")
            continue
 
        nombre = input("Nombre del producto: ").strip()
        categoria = input("Categoría: ").strip()
 
        print(f"Todos los precios se ingresan en: {simbolo_moneda}")
        try:
            cantidad_inicial = int(input("Cantidad inicial: "))
            precio_compra = float(input("Precio de compra: "))
            precio_venta = float(input("Precio de venta: "))
            stock_minimo = int(input("Stock mínimo permitido: "))
        except ValueError:
            print("⚠ Datos numéricos inválidos. Intente nuevamente.")
            continue
 
        # Registro en las listas
        lista_codigos.append(codigo)
        lista_nombres.append(nombre)
        lista_categorias.append(categoria)
        lista_cantidades.append(cantidad_inicial)
        lista_precio_compra.append(precio_compra)
        lista_precio_venta.append(precio_venta)
        lista_stock_minimo.append(stock_minimo)
 
        print("Producto registrado correctamente.")
 
        respuesta = input("¿Desea registrar otro producto? (S/N): ").strip().upper()
        if respuesta == "N":
            break
 
def buscar_posicion_por_codigo(codigo_busqueda):
    """Devuelve la posición del producto según código o -1 si no existe."""
    if codigo_busqueda in lista_codigos:
        return lista_codigos.index(codigo_busqueda)
    return -1
 
def registrar_movimiento():
    """Proceso 2: Actualización del inventario con validaciones y ciclos."""
    if not lista_codigos:
        print("⚠ No hay productos registrados. Use primero la opción 1.")
        return
 
    codigo_busqueda = input("Ingrese código de producto (o 'X' para cancelar): ").strip().upper()
    if codigo_busqueda == "X":
        print("↩ Movimiento cancelado. Volviendo al menú.")
        return
 
    pos = buscar_posicion_por_codigo(codigo_busqueda)
 
    if pos == -1:
        print("⚠ Producto no encontrado.")
        return
 
    tipo_mov = input("Tipo de movimiento (I = ingreso, S = salida): ").strip().upper()
 
    try:
        cantidad_mov = int(input("Cantidad del movimiento: "))
    except ValueError:
        print("⚠ Cantidad inválida.")
        return
 
    if tipo_mov == "I":
        lista_cantidades[pos] += cantidad_mov
        print("Ingreso registrado correctamente.")
    elif tipo_mov == "S":
        if cantidad_mov <= lista_cantidades[pos]:
            lista_cantidades[pos] -= cantidad_mov
            print("Salida registrada correctamente.")
 
            # Alerta de stock crítico después de la salida
            if lista_cantidades[pos] <= lista_stock_minimo[pos]:
                print(">> ⚠ Atención: el producto ha quedado en nivel de stock crítico.")
        else:
            print("⚠ Movimiento inválido: stock insuficiente.")
    else:
        print("⚠ Tipo de movimiento no válido.")
 
def mostrar_stock_critico():
    """Proceso 3: Identificación de productos con stock crítico."""
    if not lista_codigos:
        print("⚠ No hay productos registrados. Use primero la opción 1.")
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
    """Proceso 4: Cálculo del valor económico total del inventario."""
    if not lista_codigos:
        print("⚠ No hay productos registrados. Use primero la opción 1.")
        return
 
    print("\nCalculando valor total del inventario...")
    valor_total = 0.0
 
    for i in range(len(lista_codigos)):
        valor_producto = lista_precio_compra[i] * lista_cantidades[i]
        valor_total += valor_producto
 
    print(f"💰 Valor económico total del inventario: {simbolo_moneda}{valor_total:.2f}")
 
def generar_reporte_general():
    """Proceso 5: Generación de un reporte general del inventario."""
    if not lista_codigos:
        print("⚠ No hay productos registrados. Use primero la opción 1.")
        return
 
    print("\n---- Reporte general de inventario ----")
    for i in range(len(lista_codigos)):
        print("---------------------------------------")
        print(f"Código: {lista_codigos[i]}")
        print(f"Nombre: {lista_nombres[i]}")
        print(f"Categoría: {lista_categorias[i]}")
        print(f"Cantidad actual: {lista_cantidades[i]}")
        print(f"Precio de compra: {simbolo_moneda}{lista_precio_compra[i]:.2f}")
        print(f"Precio de venta: {simbolo_moneda}{lista_precio_venta[i]:.2f}")
        if lista_cantidades[i] <= lista_stock_minimo[i]:
            print(">> ⚠ Advertencia: Producto en stock crítico.")
    print("---------------------------------------")
    print("Fin del reporte.")
 
def menu_principal():
    """Menú principal del sistema (estructura repetitiva + selectivas)."""
    while True:
        print("\n==== MENÚ PRINCIPAL DEL INVENTARIO ====")
        print("1. Registrar productos")
        print("2. Registrar movimiento de inventario (ingreso / salida)")
        print("3. Mostrar productos con stock crítico")
        print("4. Calcular valor total del inventario")
        print("5. Generar reporte general")
        print("6. Salir del sistema")
 
        opcion = input("Seleccione una opción: ").strip()  # se maneja como TEXTO
 
        if opcion == "1":
            registrar_productos()
        elif opcion == "2":
            registrar_movimiento()
        elif opcion == "3":
            mostrar_stock_critico()
        elif opcion == "4":
            print(">> Has seleccionado: Calcular valor total del inventario")
            calcular_valor_total()
        elif opcion == "5":
            print(">> Has seleccionado: Generar reporte general")
            generar_reporte_general()
        elif opcion == "6":
            print("Saliendo del sistema de inventario...")
            break
        else:
            print("⚠ Opción no válida. Intente nuevamente.")
 
if __name__ == "__main__":
    print("=== Sistema de Control de Inventario - Ricoh del Perú ===")
    configurar_moneda()
    menu_principal()
