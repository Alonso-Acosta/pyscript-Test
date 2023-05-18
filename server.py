from flask import Flask, render_template
import subprocess

app = Flask(__name__)

# Ruta para cargar la GUI
@app.route("/gui")
def cargar_gui():
    # Ejecutar el script Python y capturar la salida
    resultado = subprocess.check_output(["python", "GUITESTCONTRASTE.py"])

    # Convertir la salida en una cadena decodificada
    resultado_decodificado = resultado.decode("utf-8")

    return resultado_decodificado

# Ruta para cargar el archivo HTML
@app.route("/")
def cargar_html():
    return render_template("index.html")

if __name__ == "__main__":
    

    # Ejecutar GUITESTCONTRASTE.py
    subprocess.Popen(["python", "GUITESTCONTRASTE.py"])

    # Iniciar la aplicación Flask
    app.run()
