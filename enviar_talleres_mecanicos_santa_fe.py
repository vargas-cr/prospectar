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

# ===== 15 TALLERES MECÁNICOS Y ELECTROMECÁNICOS EN SANTA FE Y ROSARIO =====
TALLERES = [
    {
        "nombre": "Electromecánica Fortuna",
        "email": "contacto@tallerfortuna.com.ar",
        "zona": "Rosario",
        "asunto": "Fortuna: Web + IA + Agente de voz = +100% clientes en Rosario"
    },
    {
        "nombre": "Servicio Técnico Mecánico",
        "email": "info@serviciotecnicomecanico.com.ar",
        "zona": "Rosario",
        "asunto": "Servicio Técnico: De 25 a 60+ clientes/semana con IA"
    },
    {
        "nombre": "Electromecánica Santa Fe",
        "email": "contacto@electromecanicasantafe.com.ar",
        "zona": "Santa Fe Capital",
        "asunto": "Electromecánica SF: Reparación + IA + Web profesional"
    },
    {
        "nombre": "Electricidad Automotor Lagos",
        "email": "info@electricidadlags.com.ar",
        "zona": "Rosario",
        "asunto": "Lagos: Arranques + Alternadores + IA + Agente de voz"
    },
    {
        "nombre": "Electricidad Automotor Pellegrini",
        "email": "contacto@electricidadpellegrini.com.ar",
        "zona": "Rosario",
        "asunto": "Pellegrini: Diagnóstico + IA + Web = Eficiencia máxima"
    },
    {
        "nombre": "Electricidad Automotor Francia",
        "email": "info@electricidadfrancia.com.ar",
        "zona": "Rosario",
        "asunto": "Francia: Especializado alternadores + IA automática"
    },
    {
        "nombre": "Taller Mecánico Galicia",
        "email": "contacto@tallergalicia.com.ar",
        "zona": "Santa Fe",
        "asunto": "Galicia: Multimarca + Inyección + IA + Agente de voz"
    },
    {
        "nombre": "Taller Mecánico General Bergrano",
        "email": "info@tallerbergrano.com.ar",
        "zona": "Santa Fe",
        "asunto": "Bergrano: Electricidad automotriz + IA + Web optimizada"
    },
    {
        "nombre": "Servicio Técnico Diesel y Nafta",
        "email": "contacto@serviciodiesnafta.com.ar",
        "zona": "Rosario",
        "asunto": "Diesel y Nafta: Mecánica especializada + IA automática"
    },
    {
        "nombre": "Ingeniería Automotriz PowerInjection",
        "email": "info@powerinjection.com.ar",
        "zona": "Rosario",
        "asunto": "PowerInjection: Inyección electrónica + IA + Voz automática"
    },
    {
        "nombre": "Electricidad Bergrano Rosario",
        "email": "contacto@electricidadbergrano.com.ar",
        "zona": "Rosario",
        "asunto": "Bergrano Rosario: Eléctrica especializada + IA + Web"
    },
    {
        "nombre": "Taller Eléctrico Especializado",
        "email": "info@tallerelectricosantafe.com.ar",
        "zona": "Santa Fe",
        "asunto": "Eléctrico SF: Especializado + IA + Agente de voz automática"
    },
    {
        "nombre": "Servicio Scanner Diagnóstico",
        "email": "contacto@servicioscannerrosario.com.ar",
        "zona": "Rosario",
        "asunto": "Scanner: Diagnóstico avanzado + IA + Web profesional"
    },
    {
        "nombre": "Taller Multimarca Santa Fe",
        "email": "info@tallermultimarcasf.com.ar",
        "zona": "Santa Fe",
        "asunto": "Multimarca SF: Mecánica integral + IA + Cero esperas"
    },
    {
        "nombre": "Electricista Automotriz Independiente",
        "email": "contacto@electricistaauto.com.ar",
        "zona": "Rosario",
        "asunto": "Electricista Auto: Domiciliario + IA + Web = +200% ingresos"
    }
]

def obtener_cuerpo_email(nombre, telefono):
    """Retorna el cuerpo del email personalizado"""

    cuerpo = f"""Hola {nombre},

Vi que ofrecen servicio mecánico y electromecánico en Santa Fe/Rosario.

El problema: cuando un cliente busca "taller mecánico Santa Fe" o "electricidad automotriz"
en Google, ¿dónde apareces?

La mayoría de talleres NO aparecen en Google. Eso significa:
- Clientes nuevos buscan online
- No te encuentran
- Van a la competencia

¿NÚMEROS EN SANTA FE/ROSARIO?
- Búsquedas/mes de "taller mecánico": ~1,500
- Búsquedas/mes de "electricidad automotriz": ~800
- Total: ~2,300 búsquedas/mes
- Sin presencia digital: pierden 90% = 2,070 búsquedas/mes

Si el 30% se convierte:
- 2,070 × 30% = 621 clientes potenciales PERDIDOS/mes
- 621 × $300 (promedio trabajo) = $186,300/mes = $2,235,600/AÑO

SOLUCIÓN - WEB + IA + AGENTE DE VOZ:

🌐 Cuando buscan tu servicio:
1. Te encuentran en Google (web optimizada + Google Business)
2. Ven trabajos realizados, precios, horarios
3. Llaman
4. Agente IA contesta: "¿Es mecánica, electricidad o ambos?"
5. Especialidad identificada
6. Agente agenda cita automáticamente
7. Tú vas y trabajas

SIN PERDER LLAMADAS. SIN HORAS ADMINISTRATIVAS.

IMAGINA:
De 20 clientes/semana a 55+ clientes/semana.
Tu taller funcionando a plena capacidad.
Tu equipo enfocado solo en trabajos, no en llamadas.
Sin perder ni una oportunidad de venta.

¿Vale la pena una llamada de 15 minutos?

📱 Teléfono: {telefono}
📧 Email: argentia.ai@gmail.com
🌐 Web: https://argent-ia.com/
📸 Instagram: @argent.iar"""

    return cuerpo

def enviar_emails():
    """Envía los emails automáticamente"""

    print("="*60)
    print("📧 ENVIANDO EMAILS A TALLERES DE SANTA FE Y ROSARIO")
    print("="*60)

    enviados = 0
    fallidos = 0

    try:
        # Conecta a Gmail
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(TU_EMAIL, TU_PASSWORD)

        # Envía cada email
        for taller in TALLERES:

            print(f"\n📤 Enviando a {taller['nombre']} ({taller['email']})...")

            try:
                # Crea el mensaje
                mensaje = MIMEMultipart()
                mensaje['From'] = TU_EMAIL
                mensaje['To'] = taller['email']
                mensaje['Subject'] = taller['asunto']

                # Obtiene el cuerpo personalizado
                cuerpo = obtener_cuerpo_email(taller['nombre'], TU_TELEFONO)

                # Agrega el cuerpo
                mensaje.attach(MIMEText(cuerpo, 'plain', 'utf-8'))

                # Envía
                server.send_message(mensaje)

                print(f"   ✅ Email enviado exitosamente")
                enviados += 1

                # Pausa pequeña para no saturar
                time.sleep(2)

            except Exception as e:
                print(f"   ❌ Error: {e}")
                fallidos += 1

        server.quit()

    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        print("Verifica que tengas credenciales correctas de Gmail")
        return

    # Resumen
    print("\n" + "="*60)
    print(f"✅ ENVIADOS: {enviados}")
    print(f"❌ FALLIDOS: {fallidos}")
    print("="*60)

    if enviados == 15:
        print("\n🎉 ¡TODOS LOS EMAILS ENVIADOS EXITOSAMENTE!")
        print("\nProximos pasos:")
        print("1. Monitorea respuestas en los próximos 2-3 días")
        print("2. Responde rápido (profesionalismo)")
        print("3. Agenda llamadas para presentar propuesta")

if __name__ == "__main__":
    # Verifica credenciales
    if TU_EMAIL == "tu_email@gmail.com":
        print("❌ CONFIGURA TUS CREDENCIALES PRIMERO")
        exit()

    # Envía
    enviar_emails()
