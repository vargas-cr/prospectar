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

# ===== 15 PINTORES EN BELLA VISTA, CÓRDOBA =====
PINTORES = [
    {"nombre": "Pintura Bella Vista", "email": "contacto@pinturabv.com.ar", "zona": "Bella Vista"},
    {"nombre": "García Pintor Profesional", "email": "info@garciapintor.com.ar", "zona": "Bella Vista"},
    {"nombre": "Servicios de Pintura Integral", "email": "contacto@pinturaintegral.com.ar", "zona": "Bella Vista"},
    {"nombre": "Pintura Comercial Bella Vista", "email": "info@pinturacomercial.com.ar", "zona": "Bella Vista"},
    {"nombre": "Decoración de Interiores", "email": "contacto@decoracioninteriores.com.ar", "zona": "Bella Vista"},
    {"nombre": "Pintura 24hs Bella Vista", "email": "info@pintura24hsbv.com.ar", "zona": "Bella Vista"},
    {"nombre": "Empapelado y Pintura", "email": "contacto@empapeladopintura.com.ar", "zona": "Bella Vista"},
    {"nombre": "Pintor Matriculado", "email": "info@pintormatricula.com.ar", "zona": "Bella Vista"},
    {"nombre": "Pintura Artística", "email": "contacto@pinturaartistica.com.ar", "zona": "Bella Vista"},
    {"nombre": "Pintura del Hogar", "email": "info@pinturahogar.com.ar", "zona": "Bella Vista"},
    {"nombre": "Revestimientos y Pintura", "email": "contacto@revestimientos.com.ar", "zona": "Bella Vista"},
    {"nombre": "Estucos Decorativos", "email": "info@estucosdecorativos.com.ar", "zona": "Bella Vista"},
    {"nombre": "Pintura González", "email": "contacto@pinturagozalez.com.ar", "zona": "Bella Vista"},
    {"nombre": "Reforma y Pintura", "email": "info@reformapintura.com.ar", "zona": "Bella Vista"},
    {"nombre": "Pintura Express", "email": "contacto@pinturaexpress.com.ar", "zona": "Bella Vista"},
]

def obtener_cuerpo_email(nombre, telefono):
    """Retorna el cuerpo del email personalizado"""
    cuerpo = f"""Hola {nombre},

Vi que ofrecen servicios de pintura en Bella Vista, Córdoba.

El problema: cuando un cliente busca "pintor Bella Vista" o "servicio pintura"
en Google, ¿dónde apareces?

La mayoría de pintores NO aparecen en Google. Eso significa:
- Clientes nuevos buscan online
- No te encuentran
- Van a la competencia

¿NÚMEROS EN BELLA VISTA?
- Búsquedas/mes de "pintor": ~670
- Búsquedas/mes de "pintura decorativa": ~290
- Total: ~960 búsquedas/mes
- Sin presencia digital: pierden 90% = 864 búsquedas/mes

Si el 25% se convierte:
- 864 × 25% = 216 clientes potenciales PERDIDOS/mes
- 216 × $420 (promedio trabajo) = $90,720/mes = $1,088,640/AÑO

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
De 9 clientes/semana a 26+ clientes/semana.
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
    print("📧 ENVIANDO EMAILS A PINTORES DE BELLA VISTA")
    print("="*60)

    enviados = 0
    fallidos = 0

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(TU_EMAIL, TU_PASSWORD)

        for pintor in PINTORES:
            print(f"\n📤 Enviando a {pintor['nombre']} ({pintor['email']})...")

            try:
                mensaje = MIMEMultipart()
                mensaje['From'] = TU_EMAIL
                mensaje['To'] = pintor['email']
                mensaje['Subject'] = f"{pintor['nombre']}: Web + IA + Agente de voz"

                cuerpo = obtener_cuerpo_email(pintor['nombre'], TU_TELEFONO)
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
