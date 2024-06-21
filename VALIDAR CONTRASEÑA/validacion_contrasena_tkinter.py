import tkinter as tk
from tkinter import messagebox

def validar_contrasena(contrasena):
    # Casos de prueba
    largo_valido = 8 <= len(contrasena) <= 10
    almenos_letras = any(c.isalpha() for c in contrasena)
    almenos_mayuscula = any(c.isupper() for c in contrasena)
    almenos_minuscula = any(c.islower() for c in contrasena)
    almenos_numero = any(c.isdigit() for c in contrasena)
    almenos_especial = any(not c.isalnum() for c in contrasena)
    
    # Lista para almacenar mensajes de error específicos
    mensajes_error = []
    
    # Condiciones
    if len(contrasena) > 10:
        mensajes_error.append("La contraseña es demasiado larga.")
    if len(contrasena) < 8:
        mensajes_error.append("La contraseña es demasiado corta.")
    if not largo_valido:
        mensajes_error.append("La contraseña debe tener entre 8 y 10 caracteres.")
    if not almenos_letras:
        mensajes_error.append("La contraseña debe contener al menos una letra.")
    if not almenos_mayuscula:
        mensajes_error.append("La contraseña debe contener al menos una letra mayúscula.")
    if not almenos_minuscula:
        mensajes_error.append("La contraseña debe contener al menos una letra minúscula.")
    if not almenos_numero:
        mensajes_error.append("La contraseña debe contener al menos un número.")
    if not almenos_especial:
        mensajes_error.append("La contraseña debe contener al menos un carácter especial.")
    
    # Mostrar mensajes de error específicos si los hay
    if mensajes_error:
        mensaje_completo = "\n".join(mensajes_error)
        messagebox.showerror("Error de validación", mensaje_completo)
        return False
    else:
        messagebox.showinfo("Éxito", "Contraseña válida.")
        return True

def main():
    # Configuración de la ventana principal
    root = tk.Tk()
    root.title("Validación de Contraseña")
    root.geometry("350x200")  # Tamaño inicial de la ventana

    # Colores y fuentes
    color_fondo = "#f0f0f0"
    color_botones = "#4CAF50"
    color_texto = "#333333"
    font_label = ("Arial", 12)
    font_entry = ("Arial", 12)

    # Configuración de estilo
    root.configure(bg=color_fondo)
    root.resizable(False, False)  # Evita redimensionar la ventana

    # Frame para los widgets
    frame = tk.Frame(root, bg=color_fondo, padx=20, pady=20)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Etiqueta y campo de entrada para la contraseña
    label_contrasena = tk.Label(frame, text="Ingrese su contraseña:", bg=color_fondo, fg=color_texto, font=font_label)
    label_contrasena.grid(row=0, column=0, sticky="w", pady=(0, 10))
    entry_contrasena = tk.Entry(frame, show="*", font=font_entry)
    entry_contrasena.grid(row=1, column=0, pady=(0, 20))

    # Botón para validar la contraseña
    btn_validar = tk.Button(frame, text="Validar Contraseña", bg=color_botones, fg="white", font=font_label, command=lambda: validar_contrasena(entry_contrasena.get()))
    btn_validar.grid(row=2, column=0, pady=(10, 0), ipadx=10, ipady=5)

    # Ejecutar el bucle principal de la interfaz gráfica
    root.mainloop()

if __name__ == "__main__":
    main()