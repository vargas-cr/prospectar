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

# ===== 15 EMPRESAS LIMPIEZA EN BELLA VISTA, CÓRDOBA =====
LIMPIEZA = [
    {"nombre": "Limpieza Bella Vista", "email": "contacto@limpiezabv.com.ar", "zona": "Bella Vista"},
    {"nombre": "García Limpieza Profesional", "email": "info@garcialimpieza.com.ar", "zona": "Bella Vista"},
    {"nombre": "Servicios de Limpieza Integral", "email": "contacto@limpiezaintegral.com.ar", "zona": "Bella Vista"},
    {"nombre": "Limpieza Comercial Bella Vista", "email": "info@limpiezacomercial.com.ar", "zona": "Bella Vista"},
    {"nombre": "Limpieza de Cristales", "email": "contacto@limpiezacristales.com.ar", "zona": "Bella Vista"},
    {"nombre": "Limpieza 24hs Bella Vista", "email": "info@limpieza24hsbv.com.ar", "zona": "Bella Vista"},
    {"nombre": "Desinfección y Limpieza", "email": "contacto@desinfeccion.com.ar", "zona": "Bella Vista"},
    {"nombre": "Personal de Limpieza Contratación", "email": "info@personalimpieza.com.ar", "zona": "Bella Vista"},
    {"nombre": "Limpieza Profunda", "email": "contacto@limpiezaprofunda.com.ar", "zona": "Bella Vista"},
    {"nombre": "Limpieza del Hogar", "email": "info@limpiezahogar.com.ar", "zona": "Bella Vista"},
    {"nombre": "Limpieza de Alfombras", "email": "contacto@limpiezaalfombras.com.ar", "zona": "Bella Vista"},
    {"nombre": "Control de Plagas", "email": "info@controlplagas.com.ar", "zona": "Bella Vista"},
    {"nombre": "Limpieza González", "email": "contacto@limpiezagonzalez.com.ar", "zona": "Bella Vista"},
    {"nombre": "Higiene Industrial", "email": "info@higieneind.com.ar", "zona": "Bella Vista"},
    {"nombre": "Limpieza Express", "email": "contacto@limpiezaexpress.com.ar", "zona": "Bella Vista"},
]

def obtener_cuerpo_email(nombre, telefono):
    """Retorna el cuerpo del email personalizado"""
    cuerpo = f"""Hola {nombre},

Vi que ofrecen servicios de limpieza en Bella Vista, Córdoba.

El problema: cuando un cliente busca "limpieza Bella Vista" o "servicio limpieza profesional"
en Google, ¿dónde apareces?

La mayoría de empresas de limpieza NO aparecen en Google. Eso significa:
- Clientes nuevos buscan online
- No te encuentran
- Van a la competencia

¿NÚMEROS EN BELLA VISTA?
- Búsquedas/mes de "limpieza profesional": ~580
- Búsquedas/mes de "servicio limpieza": ~240
- Total: ~820 búsquedas/mes
- Sin presencia digital: pierden 90% = 738 búsquedas/mes

Si el 25% se convierte:
- 738 × 25% = 184 clientes potenciales PERDIDOS/mes
- 184 × $400 (promedio trabajo) = $73,600/mes = $883,200/AÑO

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
De 8 clientes/semana a 22+ clientes/semana.
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
    print("📧 ENVIANDO EMAILS A EMPRESAS DE LIMPIEZA DE BELLA VISTA")
    print("="*60)

    enviados = 0
    fallidos = 0

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(TU_EMAIL, TU_PASSWORD)

        for empresa in LIMPIEZA:
            print(f"\n📤 Enviando a {empresa['nombre']} ({empresa['email']})...")

            try:
                mensaje = MIMEMultipart()
                mensaje['From'] = TU_EMAIL
                mensaje['To'] = empresa['email']
                mensaje['Subject'] = f"{empresa['nombre']}: Web + IA + Agente de voz"

                cuerpo = obtener_cuerpo_email(empresa['nombre'], TU_TELEFONO)
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
