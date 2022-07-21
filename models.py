class Producto:
    def __init__(self, codigo, marca, detalle, precio):
        self.codigo = codigo
        self.marca = marca
        self.detalle = detalle
        self.precio = precio

    def __str__(self):
        return "{};{};{};{}\n".format(
            self.codigo, self.marca, self.detalle, self.precio
        )


class Cliente:
    # atributos
    def __init__(self, dni, nombres_apellidos, direccion, telefono, email):
        self.dni = dni
        self.nombres_apellidos = nombres_apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    # metodos
    def __str__(self):
        return "{};{};{};{};{}\n".format(
            self.dni, self.nombres_apellidos, self.direccion, self.telefono, self.email
        )


class Usuario:
    # atributos
    def __init__(
        self, dni, password, tipo, nombres_apellidos, direccion, telefono, email
    ):
        self.dni = dni
        self.password = password
        self.tipo = tipo
        self.nombres_apellidos = nombres_apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    # metodos
    def __str__(self):
        return "{};{};{};{};{};{};{}\n".format(
            self.dni,
            self.password,
            self.tipo,
            self.nombres_apellidos,
            self.direccion,
            self.telefono,
            self.email,
        )
def leer():
    datos=[]
    with open("./archivos/factura.txt","r") as f:
      for linea in f:
          datos.append(linea)
          
          print(datos)