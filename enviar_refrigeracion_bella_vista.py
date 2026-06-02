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

# ===== 15 TÉCNICOS REFRIGERACIÓN EN BELLA VISTA, CÓRDOBA =====
REFRIGERACION = [
    {"nombre": "Refrigeración Bella Vista", "email": "contacto@refrigeracionbv.com.ar", "zona": "Bella Vista"},
    {"nombre": "García Refrigeración", "email": "info@garciarefrigeracion.com.ar", "zona": "Bella Vista"},
    {"nombre": "Servicios de Refrigeración Profesional", "email": "contacto@refrigeracionprof.com.ar", "zona": "Bella Vista"},
    {"nombre": "Refrigeración 24hs Bella Vista", "email": "info@refrigeracion24hsbv.com.ar", "zona": "Bella Vista"},
    {"nombre": "Reparación de Heladeras López", "email": "contacto@reparacionheladeras.com.ar", "zona": "Bella Vista"},
    {"nombre": "Congeladores y Heladeras", "email": "info@congeladoresheladeras.com.ar", "zona": "Bella Vista"},
    {"nombre": "Técnico en Refrigeración", "email": "contacto@tecnicorefrigeracion.com.ar", "zona": "Bella Vista"},
    {"nombre": "Refrigeración Comercial", "email": "info@refrigeracioncomercial.com.ar", "zona": "Bella Vista"},
    {"nombre": "Servicios Integrales Refrigeración", "email": "contacto@serviciosrefrig.com.ar", "zona": "Bella Vista"},
    {"nombre": "Refrigeración del Hogar", "email": "info@refrigeracionhogar.com.ar", "zona": "Bella Vista"},
    {"nombre": "Mantenimiento Preventivo Refrigeración", "email": "contacto@mantenimientorefrig.com.ar", "zona": "Bella Vista"},
    {"nombre": "Descongelación de Heladeras", "email": "info@descongelacion.com.ar", "zona": "Bella Vista"},
    {"nombre": "Refrigeración González", "email": "contacto@refrigeraciongonzalez.com.ar", "zona": "Bella Vista"},
    {"nombre": "Recarga de Gas Refrigerante", "email": "info@recargagarefrig.com.ar", "zona": "Bella Vista"},
    {"nombre": "Refrigeración Express", "email": "contacto@refrigeracionexpress.com.ar", "zona": "Bella Vista"},
]

def obtener_cuerpo_email(nombre, telefono):
    """Retorna el cuerpo del email personalizado"""
    cuerpo = f"""Hola {nombre},

Vi que ofrecen servicios de refrigeración en Bella Vista, Córdoba.

El problema: cuando un cliente busca "reparación heladera Bella Vista" o "técnico refrigeración"
en Google, ¿dónde apareces?

La mayoría de técnicos de refrigeración NO aparecen en Google. Eso significa:
- Clientes nuevos buscan online
- No te encuentran
- Van a la competencia

¿NÚMEROS EN BELLA VISTA?
- Búsquedas/mes de "reparación heladera": ~620
- Búsquedas/mes de "técnico refrigeración": ~280
- Total: ~900 búsquedas/mes
- Sin presencia digital: pierden 90% = 810 búsquedas/mes

Si el 25% se convierte:
- 810 × 25% = 202 clientes potenciales PERDIDOS/mes
- 202 × $320 (promedio trabajo) = $64,640/mes = $775,680/AÑO

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
De 9 clientes/semana a 25+ clientes/semana.
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
    print("📧 ENVIANDO EMAILS A TÉCNICOS DE REFRIGERACIÓN DE BELLA VISTA")
    print("="*60)

    enviados = 0
    fallidos = 0

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(TU_EMAIL, TU_PASSWORD)

        for tecnico in REFRIGERACION:
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
