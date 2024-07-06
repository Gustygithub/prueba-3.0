import json
def cargar_usuarios_desde_json(archivo):
    try:
        print(archivo)
        with open(archivo,"r") as file:
            usuarios = json.load(file)
            return usuarios
    except FileNotFoundError:
        print(f"el usuario {archivo} no se encontro")
        return[]
   
def buscar_usuario_por_nombre(lista_usuarios,nombre): 
  for usuarios in lista_usuarios:
    if usuarios["nombre"]:
      return usuarios
  return None 
def guardar_usuario_en_txt(usuario, archivo): 
  try:
    with open(archivo, "w") as file:
      file.write(f"nombre:{usuario["nombre"]}\n")
      file.write(f"edad:{usuario["edad"]}\n")
      file.write(f"email:{usuario["email"]}\n")
    print(f"usuario{usuario["nombre"]}guardado en archivo")  
  except IOError:
    print(f"error no se guarda el archivo:{archivo}no se guardo")  
  
def main():
 archivo_json="C:\\archivogusty\\usuarios.json"  
 usuarios=cargar_usuarios_desde_json(archivo_json)
 
 if usuarios==[]:  
   print("no se pudo cargar el usuario. programa terminado")
   return
 nombre_usuario= input("ingrese el ususario que decea buscar:")
 usuario_encontrado=buscar_usuario_por_nombre(usuarios,nombre_usuario)
 if usuario_encontrado is not None:
   print(f"usuario encontrado:\n nombre:{usuario_encontrado["nombre"]}\n edad:{usuario_encontrado["edad"]}\n email:{usuario_encontrado["email"]}")
   archivo_txt=f"{nombre_usuario}.txt"
   guardar_usuario_en_txt(usuario_encontrado,"C:\\archivogusty\\"+ archivo_txt)
 else:
   print(f"no se encontro el nombre del usuario{nombre_usuario}")  
if __name__=="__main__":
  main()   


  