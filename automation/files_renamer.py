files = ["reporte.txt", "datos.txt", "resumen.txt"]

for file in files:
    with open(file, "w") as f:
        f.write("Archivo creado automáticamente\n")

print("Archivos creados correctamente.")
with open("reporte.txt", "w") as f:
    f.write("Reporte generado automáticamente")

with open("datos.txt", "w") as f:
    f.write("Datos de ejemplo")

with open("resumen.txt", "w") as f:
    f.write("Resumen automático")

print("Archivos creados correctamente")
