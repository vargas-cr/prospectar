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

# ===== 15 TÉCNICOS AIRE ACONDICIONADO A CONTACTAR =====
TECNICOS = [
    {
        "nombre": "Service Capital",
        "email": "info@service-capital.com.ar",
        "zona": "Capital Federal",
        "asunto": "Service Capital: Tu web + IA + Agente de voz = +80% más clientes"
    },
    {
        "nombre": "TECNICOBSAS",
        "email": "info@tecnicobsas.com",
        "zona": "Capital Federal",
        "asunto": "TECNICOBSAS: Reparación aire acondicionado + IA automática"
    },
    {
        "nombre": "Servicio Oficial",
        "email": "info@servicio-oficial.com.ar",
        "zona": "Capital Federal",
        "asunto": "Servicio Oficial: De 20 a 50+ clientes/semana con web + IA"
    },
    {
        "nombre": "Aires Service",
        "email": "contacto@aires-service.com.ar",
        "zona": "Capital Federal",
        "asunto": "Aires Service: $2M/año en clientes que buscan en Google"
    },
    {
        "nombre": "Service Aire Acondicionado",
        "email": "info@servicedeaireacondicionado.com.ar",
        "zona": "Capital Federal",
        "asunto": "Service Aire: Agente de voz 24/7 que atiende por ti"
    },
    {
        "nombre": "Aireflow",
        "email": "contacto@aireflow.com.ar",
        "zona": "Capital Federal",
        "asunto": "Aireflow: Web + IA + Voz automática = Sin llamadas perdidas"
    },
    {
        "nombre": "Reparación Service Aire",
        "email": "contacto@reparacionsplitencapitalfederal.com.ar",
        "zona": "Capital Federal",
        "asunto": "Reparación Service: +150 clientes/mes con presencia digital"
    },
    {
        "nombre": "BGH Service",
        "email": "contacto@bghservice.com.ar",
        "zona": "Capital Federal",
        "asunto": "BGH Service: Autorizado + IA = Doble ventaja competitiva"
    },
    {
        "nombre": "Servicio Carrier",
        "email": "info@servcarrier.com.ar",
        "zona": "Capital Federal",
        "asunto": "Carrier Service: Especialista + web + IA = Liderazgo"
    },
    {
        "nombre": "Service Aire Técnico",
        "email": "info@service-aire.com.ar",
        "zona": "Capital Federal",
        "asunto": "Service Aire Técnico: De emergencias por teléfono a 40+ clientes/semana"
    },
    {
        "nombre": "AA Service Eléctrico",
        "email": "aaservicioelectrico@gmail.com",
        "zona": "Capital Federal",
        "asunto": "AA Service: Aire + Electricidad + IA = Servicio completo"
    },
    {
        "nombre": "Ansal Refrigeración",
        "email": "info@ansal.com.ar",
        "zona": "Capital Federal",
        "asunto": "Ansal: Refrigeración profesional + IA = Eficiencia máxima"
    },
    {
        "nombre": "Instalación Aires",
        "email": "contacto@instalacion-aires.com.ar",
        "zona": "Capital Federal",
        "asunto": "Instalación Aires: Instaladores + IA + Web = +100% crecimiento"
    },
    {
        "nombre": "Service Aire Central",
        "email": "info@serviceaireacondicionadocentral.com",
        "zona": "Capital Federal",
        "asunto": "Service Aire Central: Centrales + IA + Agente de voz automática"
    },
    {
        "nombre": "Reparación Aires Capital",
        "email": "reparacion@aires-capital.com.ar",
        "zona": "Capital Federal",
        "asunto": "Aires Capital: Técnicos matriculados + IA = Máxima confianza"
    }
]

def obtener_cuerpo_email(nombre, telefono):
    """Retorna el cuerpo del email personalizado"""

    cuerpo = f"""Hola {nombre},

Vi que ofrecen servicio técnico de aire acondicionado en Capital Federal.

El problema: cuando un cliente busca "reparación aire acondicionado CABA" en Google,
¿dónde apareces?

La mayoría de técnicos NO aparecen en Google. Eso significa:
- Clientes nuevos buscan online
- No te encuentran
- Van a la competencia

¿NÚMEROS?
- Búsquedas/mes de "reparación aire acondicionado CABA": ~1,200
- Sin web aparecen: 0%
- Pierden: 1,200 búsquedas/mes

Si solo el 30% se convierte: 360 clientes potenciales PERDIDOS/mes

SOLUCIÓN - WEB + IA + AGENTE DE VOZ:

🌐 Cuando buscan tu servicio:
1. Te encuentran en Google (web optimizada)
2. Ven trabajos realizados y precios
3. Llaman
4. Agente IA contesta: "¿Es emergencia o presupuesto?"
5. Si emergencia → agrega valor
6. Si presupuesto → agenda cita
7. Tú vas y trabajas

SIN PERDER LLAMADAS. SIN HORAS ADMINISTRATIVAS.

IMAGINA:
De 15 clientes/semana a 40+ clientes/semana.
Tu equipo enfocado solo en trabajos, no en llamadas.
Sin perder ni una oportunidad.

¿Vale la pena una llamada de 15 minutos?

📱 Teléfono: {telefono}
📧 Email: argentia.ai@gmail.com
🌐 Web: https://argent-ia.com/
📸 Instagram: @argent.iar"""

    return cuerpo

def enviar_emails():
    """Envía los emails automáticamente"""

    print("="*60)
    print("📧 ENVIANDO EMAILS A TÉCNICOS AIRE ACONDICIONADO")
    print("="*60)

    enviados = 0
    fallidos = 0

    try:
        # Conecta a Gmail
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(TU_EMAIL, TU_PASSWORD)

        # Envía cada email
        for tecnico in TECNICOS:

            print(f"\n📤 Enviando a {tecnico['nombre']} ({tecnico['email']})...")

            try:
                # Crea el mensaje
                mensaje = MIMEMultipart()
                mensaje['From'] = TU_EMAIL
                mensaje['To'] = tecnico['email']
                mensaje['Subject'] = tecnico['asunto']

                # Obtiene el cuerpo personalizado
                cuerpo = obtener_cuerpo_email(tecnico['nombre'], TU_TELEFONO)

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
