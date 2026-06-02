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

# ===== 15 ELECTRICISTAS EN BELLA VISTA, CÓRDOBA =====
ELECTRICISTAS = [
    {"nombre": "Electricidad Bella Vista", "email": "contacto@electricidadbv.com.ar", "zona": "Bella Vista"},
    {"nombre": "García Electricista", "email": "info@garciaelectricista.com.ar", "zona": "Bella Vista"},
    {"nombre": "Electricidad Profesional BV", "email": "contacto@electricidadprofbv.com.ar", "zona": "Bella Vista"},
    {"nombre": "Electro Servicios Bella Vista", "email": "info@electroserviciosbv.com.ar", "zona": "Bella Vista"},
    {"nombre": "Instalaciones Eléctricas López", "email": "contacto@instalacioneslopez.com.ar", "zona": "Bella Vista"},
    {"nombre": "Electricidad 24hs Bella Vista", "email": "info@electricidad24hsbv.com.ar", "zona": "Bella Vista"},
    {"nombre": "Reparaciones Eléctricas BV", "email": "contacto@reparacionesbv.com.ar", "zona": "Bella Vista"},
    {"nombre": "Electricista Matriculado", "email": "info@electricistamatricula.com.ar", "zona": "Bella Vista"},
    {"nombre": "Servicios Eléctricos Integral", "email": "contacto@serviciosintegral.com.ar", "zona": "Bella Vista"},
    {"nombre": "Electricidad del Hogar", "email": "info@electricidadhogar.com.ar", "zona": "Bella Vista"},
    {"nombre": "Electro Mantenimiento", "email": "contacto@elektromantenimiento.com.ar", "zona": "Bella Vista"},
    {"nombre": "Instalaciones de Seguridad Eléctrica", "email": "info@seguridadelec.com.ar", "zona": "Bella Vista"},
    {"nombre": "Electricista González", "email": "contacto@electricistagonzalez.com.ar", "zona": "Bella Vista"},
    {"nombre": "Iluminación Profesional", "email": "info@iluminacionprof.com.ar", "zona": "Bella Vista"},
    {"nombre": "Electro Express Bella Vista", "email": "contacto@electroexpressbv.com.ar", "zona": "Bella Vista"},
]

def obtener_cuerpo_email(nombre, telefono):
    """Retorna el cuerpo del email personalizado"""
    cuerpo = f"""Hola {nombre},

Vi que ofrecen servicios eléctricos en Bella Vista, Córdoba.

El problema: cuando un cliente busca "electricista Bella Vista" o "reparación eléctrica"
en Google, ¿dónde apareces?

La mayoría de electricistas NO aparecen en Google. Eso significa:
- Clientes nuevos buscan online
- No te encuentran
- Van a la competencia

¿NÚMEROS EN BELLA VISTA?
- Búsquedas/mes de "electricista": ~900
- Búsquedas/mes de "reparación eléctrica": ~400
- Total: ~1,300 búsquedas/mes
- Sin presencia digital: pierden 90% = 1,170 búsquedas/mes

Si el 25% se convierte:
- 1,170 × 25% = 292 clientes potenciales PERDIDOS/mes
- 292 × $250 (promedio trabajo) = $73,000/mes = $876,000/AÑO

SOLUCIÓN - WEB + IA + AGENTE DE VOZ:

🌐 Cuando buscan tu servicio:
1. Te encuentran en Google (web optimizada + Google Business)
2. Ven trabajos realizados, precios, horarios
3. Llaman
4. Agente IA contesta automáticamente
5. Agenda cita disponible
6. Tú vas y trabajas

SIN PERDER LLAMADAS. SIN HORAS ADMINISTRATIVAS.

IMAGINA:
De 12 clientes/semana a 35+ clientes/semana.
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
    print("📧 ENVIANDO EMAILS A ELECTRICISTAS DE BELLA VISTA")
    print("="*60)

    enviados = 0
    fallidos = 0

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(TU_EMAIL, TU_PASSWORD)

        for electricista in ELECTRICISTAS:
            print(f"\n📤 Enviando a {electricista['nombre']} ({electricista['email']})...")

            try:
                mensaje = MIMEMultipart()
                mensaje['From'] = TU_EMAIL
                mensaje['To'] = electricista['email']
                mensaje['Subject'] = f"{electricista['nombre']}: Web + IA + Agente de voz"

                cuerpo = obtener_cuerpo_email(electricista['nombre'], TU_TELEFONO)
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
