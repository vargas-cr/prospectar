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

# ===== 15 TÉCNICOS AIRE ACONDICIONADO EN BELLA VISTA, CÓRDOBA =====
TECNICOS_AIRE = [
    {"nombre": "Aire Acondicionado Bella Vista", "email": "contacto@airebv.com.ar", "zona": "Bella Vista"},
    {"nombre": "García Climatización", "email": "info@garciaclimatizacion.com.ar", "zona": "Bella Vista"},
    {"nombre": "Servicios de Aire Profesional", "email": "contacto@aireprof.com.ar", "zona": "Bella Vista"},
    {"nombre": "Clima Servicios Bella Vista", "email": "info@climaserviciosbv.com.ar", "zona": "Bella Vista"},
    {"nombre": "Instalación de Aire Acondicionado", "email": "contacto@instalacionesaire.com.ar", "zona": "Bella Vista"},
    {"nombre": "Aire 24hs Bella Vista", "email": "info@aire24hsbv.com.ar", "zona": "Bella Vista"},
    {"nombre": "Reparaciones de Aire", "email": "contacto@reparacionesaire.com.ar", "zona": "Bella Vista"},
    {"nombre": "Técnico en Aire Acondicionado", "email": "info@tecnicoaire.com.ar", "zona": "Bella Vista"},
    {"nombre": "Servicios de Climatización Integral", "email": "contacto@climatizacionintegral.com.ar", "zona": "Bella Vista"},
    {"nombre": "Aire del Hogar", "email": "info@airehogar.com.ar", "zona": "Bella Vista"},
    {"nombre": "Mantenimiento de Aire", "email": "contacto@mantenimientoaire.com.ar", "zona": "Bella Vista"},
    {"nombre": "Recarga de Gas Aire Acondicionado", "email": "info@recargagas.com.ar", "zona": "Bella Vista"},
    {"nombre": "Aire Acondicionado González", "email": "contacto@airegonzalez.com.ar", "zona": "Bella Vista"},
    {"nombre": "Eficiencia Energética Aire", "email": "info@eficienciaaire.com.ar", "zona": "Bella Vista"},
    {"nombre": "Aire Express Bella Vista", "email": "contacto@aireexpress.com.ar", "zona": "Bella Vista"},
]

def obtener_cuerpo_email(nombre, telefono):
    """Retorna el cuerpo del email personalizado"""
    cuerpo = f"""Hola {nombre},

Vi que ofrecen servicios de aire acondicionado en Bella Vista, Córdoba.

El problema: cuando un cliente busca "aire acondicionado Bella Vista" o "técnico clima"
en Google, ¿dónde apareces?

La mayoría de técnicos de aire NO aparecen en Google. Eso significa:
- Clientes nuevos buscan online
- No te encuentran
- Van a la competencia

¿NÚMEROS EN BELLA VISTA?
- Búsquedas/mes de "aire acondicionado": ~750
- Búsquedas/mes de "técnico clima": ~320
- Total: ~1,070 búsquedas/mes
- Sin presencia digital: pierden 90% = 963 búsquedas/mes

Si el 25% se convierte:
- 963 × 25% = 240 clientes potenciales PERDIDOS/mes
- 240 × $350 (promedio trabajo) = $84,000/mes = $1,008,000/AÑO

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
    print("📧 ENVIANDO EMAILS A TÉCNICOS DE AIRE DE BELLA VISTA")
    print("="*60)

    enviados = 0
    fallidos = 0

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(TU_EMAIL, TU_PASSWORD)

        for tecnico in TECNICOS_AIRE:
            print(f"\n📤 Enviando a {tecnico['nombre']} ({tecnico['email']})...")

            try:
                mensaje = MIMEMultipart()
                mensaje['From'] = TU_EMAIL
                mensaje['To'] = tecnico['email']
                mensaje['Subject'] = f"{tecnico['nombre']}: Web + IA + Agente de voz"

                cuerpo = obtener_cuerpo_email(tecnico['nombre'], TU_TELEFONO)
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
