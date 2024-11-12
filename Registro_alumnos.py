class Alumno:
    def __init__(self, nombre, edad, grado) -> None:
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.listaDeNotas = {}  # Cambiado a diccionario para almacenar notas con asignaturas

    def agregar_nota(self):
        while True:
            asignatura = input('Asignatura (escriba "salir" para terminar): ')
            if asignatura.lower() == 'salir':
                break
            while not asignatura.isalpha():
                print('No se pueden añadir números en el nombre de la asignatura.')
                asignatura = input('Asignatura: ')

            # Bucle para pedir un valor numérico entero
            while True:
                try:
                    nota = int(input('Ingrese nota (0-100): '))
                    if 0 <= nota <= 100:  # Asegurarse de que la nota esté en un rango aceptable
                        break
                    else:
                        print("La nota debe estar entre 0 y 100.")
                except ValueError:
                    print('Solo se puede añadir valores numéricos enteros.')

            print('\n')
            self.listaDeNotas[asignatura] = nota  # Guarda la nota en el diccionario de notas

    def calculo_media(self):
        if self.listaDeNotas:
            promedio = sum(self.listaDeNotas.values()) / len(self.listaDeNotas)
            print(f'Promedio de {self.nombre}: {promedio:.2f}')
            return promedio
        else:
            print(f'No hay notas registradas para {self.nombre}.')
            return None

    def registrar_alumno(self):
        datos_alumno = {}
        datos_alumno[self.nombre] = self
        return datos_alumno        

    def listado_alumno(self):
        # Método para listar detalles del alumno, si es necesario implementarlo en el futuro.
        pass        

# Ejemplo de uso
el_alumno = Alumno('Juan', '15', '2D')
el_alumno.agregar_nota()
el_alumno.calculo_media()
