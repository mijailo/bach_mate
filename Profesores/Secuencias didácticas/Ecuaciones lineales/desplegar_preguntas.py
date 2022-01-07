import json

archivo=input('Ingresar ruta y nombre del cuestionario (`*.json`)')

with open(archivo) as arshivo:
    cuestionario=json.load(arshivo)

respuestas=dict()
for preg in cuestionario.keys():
    respuestas[preg]=widgets.Textarea(
        value='',
        placeholder='(Escribe aquí tu respuesta)',
        description='R:',
        disabled=False
    )
    display(widgets.HBox([widgets.Label(value=cuestionario[preg]), respuestas[preg]]))