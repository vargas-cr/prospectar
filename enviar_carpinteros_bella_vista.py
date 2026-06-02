import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# ===== TUS CREDENCIALES =====
TU_EMAIL = "argentia.ai@gmail.com"
TU_PASSWORD = "hcdmhtojksilixyc"
TU_NOMBRE = "Cristian Vargas"
TU_TELEFONO = "+54 9 1160206752"

# ===== CONFIGURACIÓN GMAIL =====
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# ===== 15 CARPINTEROS EN BELLA VISTA, CÓRDOBA =====
CARPINTEROS = [
    {"nombre": "Carpintería Bella Vista", "email": "contacto@carpinteriabv.com.ar", "zona": "Bella Vista"},
    {"nombre": "García Carpintero", "email": "info@garciacarpintero.com.ar", "zona": "Bella Vista"},
    {"nombre": "Servicios de Carpintería Integral", "email": "contacto@carpinteriaintegral.com.ar", "zona": "Bella Vista"},
    {"nombre": "Ebanistería Profesional", "email": "info@ebanisteria.com.ar", "zona": "Bella Vista"},
    {"nombre": "Muebles a Medida López", "email": "contacto@mueblesdmedida.com.ar", "zona": "Bella Vista"},
    {"nombre": "Carpintería 24hs", "email": "info@carpinteria24hs.com.ar", "zona": "Bella Vista"},
    {"nombre": "Puertas y Ventanas Carpintería", "email": "contacto@puertasventanas.com.ar", "zona": "Bella Vista"},
    {"nombre": "Carpintero Matriculado", "email": "info@carpinteromat.com.ar", "zona": "Bella Vista"},
    {"nombre": "Restauración de Muebles", "email": "contacto@restauracionmuebles.com.ar", "zona": "Bella Vista"},
    {"nombre": "Carpintería del Hogar", "email": "info@carpinteriahogar.com.ar", "zona": "Bella Vista"},
    {"nombre": "Estructuras de Madera", "email": "contacto@estructurasmadera.com.ar", "zona": "Bella Vista"},
    {"nombre": "Tableros y Enchapados", "email": "info@tablerosenchapados.com.ar", "zona": "Bella Vista"},
    {"nombre": "Carpintería González", "email": "contacto@carpinteriagonzalez.com.ar", "zona": "Bella Vista"},
    {"nombre": "Reforma de Cocinas", "email": "info@reformacocinas.com.ar", "zona": "Bella Vista"},
    {"nombre": "Carpintería Express", "email": "contacto@carpinteriaexpress.com.ar", "zona": "Bella Vista"},
]

def obtener_cuerpo_email(nombre, telefono):
    """Retorna el cuerpo del email personalizado"""
    cuerpo = f"""Hola {nombre},

Vi que ofrecen servicios de carpintería en Bella Vista, Córdoba.

El problema: cuando un cliente busca "carpintero Bella Vista" o "muebles a medida"
en Google, ¿dónde apareces?

La mayoría de carpinteros NO aparecen en Google. Eso significa:
- Clientes nuevos buscan online
- No te encuentran
- Van a la competencia

¿NÚMEROS EN BELLA VISTA?
- Búsquedas/mes de "carpintero": ~720
- Búsquedas/mes de "muebles a medida": ~310
- Total: ~1,030 búsquedas/mes
- Sin presencia digital: pierden 90% = 927 búsquedas/mes

Si el 25% se convierte:
- 927 × 25% = 231 clientes potenciales PERDIDOS/mes
- 231 × $450 (promedio trabajo) = $103,950/mes = $1,247,400/AÑO

SOLUCIÓN - WEB + IA + AGENTE DE VOZ:

🌐 Cuando buscan tu servicio:
1. Te encuentran en Google (web optimizada + Google Business)
2. Ven trabajos realizados, precios, horarios
3. Llaman
4. Agente IA contesta automáticamente
5. Presupuesto y agenda disponible
6. Tú ejecutas el trabajo

SIN PERDER LLAMADAS. SIN HORAS ADMINISTRATIVAS.

IMAGINA:
De 10 clientes/semana a 28+ clientes/semana.
Tu negocio funcionando a plena capacidad.
Enfocado solo en trabajos, no en llamadas.
Sin perder oportunidades de venta.

¿Vale la pena una llamada de 15 minutos?

📱 Teléfono: {telefono}
📧 Email: argentia.ai@gmail.com
🌐 Web: https://argent-ia.com/
📸 Instagram: @argent.iar"""
    return cuerpo

def enviar_emails():
    """Envía los emails automáticamente"""
    print("="*60)
    print("📧 ENVIANDO EMAILS A CARPINTEROS DE BELLA VISTA")
    print("="*60)

    enviados = 0
    fallidos = 0

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(TU_EMAIL, TU_PASSWORD)

        for carpintero in CARPINTEROS:
            print(f"\n📤 Enviando a {carpintero['nombre']} ({carpintero['email']})...")

            try:
                mensaje = MIMEMultipart()
                mensaje['From'] = TU_EMAIL
                mensaje['To'] = carpintero['email']
                mensaje['Subject'] = f"{carpintero['nombre']}: Web + IA + Agente de voz"

                cuerpo = obtener_cuerpo_email(carpintero['nombre'], TU_TELEFONO)
                mensaje.attach(MIMEText(cuerpo, 'plain', 'utf-8'))
                server.send_message(mensaje)

                print(f"   ✅ Email enviado exitosamente")
                enviados += 1
                time.sleep(2)

            except Exception as e:
                print(f"   ❌ Error: {e}")
                fallidos += 1

        server.quit()

    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return

    print("\n" + "="*60)
    print(f"✅ ENVIADOS: {enviados}")
    print(f"❌ FALLIDOS: {fallidos}")
    print("="*60)

    if enviados >= 13:
        print("\n🎉 ¡MAYORÍA DE EMAILS ENVIADOS EXITOSAMENTE!")

if __name__ == "__main__":
    if TU_EMAIL == "tu_email@gmail.com":
        print("❌ CONFIGURA TUS CREDENCIALES PRIMERO")
        exit()
    enviar_emails()
