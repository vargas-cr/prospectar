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

# ===== 15 PLOMEROS EN BELLA VISTA, CÓRDOBA =====
PLOMEROS = [
    {"nombre": "Plomería Bella Vista", "email": "contacto@plomeriabv.com.ar", "zona": "Bella Vista"},
    {"nombre": "García Plomero", "email": "info@garciaplomero.com.ar", "zona": "Bella Vista"},
    {"nombre": "Servicios de Plomería Profesional", "email": "contacto@plomeriaprofbv.com.ar", "zona": "Bella Vista"},
    {"nombre": "Plomería 24hs Bella Vista", "email": "info@plomeria24hsbv.com.ar", "zona": "Bella Vista"},
    {"nombre": "Gasfitería López", "email": "contacto@gasfiterialopez.com.ar", "zona": "Bella Vista"},
    {"nombre": "Plomería del Hogar", "email": "info@plomeriahogar.com.ar", "zona": "Bella Vista"},
    {"nombre": "Reparaciones Urgentes Plomería", "email": "contacto@reparacionesurgentes.com.ar", "zona": "Bella Vista"},
    {"nombre": "Gasfitero Matriculado", "email": "info@gasfiteromatricula.com.ar", "zona": "Bella Vista"},
    {"nombre": "Instalaciones Sanitarias Integral", "email": "contacto@instalacionessanitarias.com.ar", "zona": "Bella Vista"},
    {"nombre": "Plomería González", "email": "info@plomeriaonzalez.com.ar", "zona": "Bella Vista"},
    {"nombre": "Desagües y Cloacas", "email": "contacto@desaguescloacas.com.ar", "zona": "Bella Vista"},
    {"nombre": "Plomería Presupuesto Gratis", "email": "info@plomeriagratis.com.ar", "zona": "Bella Vista"},
    {"nombre": "Reparación de Cañerías", "email": "contacto@reparacioncanierias.com.ar", "zona": "Bella Vista"},
    {"nombre": "Sistemas de Agua", "email": "info@sistemasagua.com.ar", "zona": "Bella Vista"},
    {"nombre": "Plomería Express", "email": "contacto@plomeriaexpress.com.ar", "zona": "Bella Vista"},
]

def obtener_cuerpo_email(nombre, telefono):
    """Retorna el cuerpo del email personalizado"""
    cuerpo = f"""Hola {nombre},

Vi que ofrecen servicios de plomería en Bella Vista, Córdoba.

El problema: cuando un cliente busca "plomero Bella Vista" o "reparación cañerías"
en Google, ¿dónde apareces?

La mayoría de plomeros NO aparecen en Google. Eso significa:
- Clientes nuevos buscan online
- No te encuentran
- Van a la competencia

¿NÚMEROS EN BELLA VISTA?
- Búsquedas/mes de "plomero": ~850
- Búsquedas/mes de "reparación cañerías": ~380
- Total: ~1,230 búsquedas/mes
- Sin presencia digital: pierden 90% = 1,107 búsquedas/mes

Si el 25% se convierte:
- 1,107 × 25% = 276 clientes potenciales PERDIDOS/mes
- 276 × $280 (promedio trabajo) = $77,280/mes = $927,360/AÑO

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
De 11 clientes/semana a 32+ clientes/semana.
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
    print("📧 ENVIANDO EMAILS A PLOMEROS DE BELLA VISTA")
    print("="*60)

    enviados = 0
    fallidos = 0

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(TU_EMAIL, TU_PASSWORD)

        for plomero in PLOMEROS:
            print(f"\n📤 Enviando a {plomero['nombre']} ({plomero['email']})...")

            try:
                mensaje = MIMEMultipart()
                mensaje['From'] = TU_EMAIL
                mensaje['To'] = plomero['email']
                mensaje['Subject'] = f"{plomero['nombre']}: Web + IA + Agente de voz"

                cuerpo = obtener_cuerpo_email(plomero['nombre'], TU_TELEFONO)
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
