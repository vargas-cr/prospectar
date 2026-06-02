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

# ===== 5 ELECTRICISTAS A CONTACTAR =====
ELECTRICISTAS = [
    {
        "nombre": "Electricista La Boca",
        "email": "electricidadlgs@yahoo.com.ar",
        "zona": "La Boca",
        "asunto": "Electricista La Boca: $135,000/año en dinero perdido por no tener web"
    },
    {
        "nombre": "VIP Electricidad",
        "email": "vip.electricidad.almagro@gmail.com",
        "zona": "Almagro",
        "asunto": "VIP Electricidad: Recupera $200,000/año con presencia online"
    },
    {
        "nombre": "Electricista Almagro 24hs",
        "email": "electricista.almagro24@hotmail.com",
        "zona": "Almagro",
        "asunto": "Electricista Almagro 24hs: Casi 3x tus ingresos (con web)"
    },
    {
        "nombre": "General Electric Service",
        "email": "info@servicioelectricosanisidro.com.ar",
        "zona": "San Isidro",
        "asunto": "General Electric Service: Aparece en Google (nueva fuente de clientes)"
    },
    {
        "nombre": "AA Service Eléctrico",
        "email": "aaservicioelectrico@gmail.com",
        "zona": "Devoto",
        "asunto": "AA Service: De 40 clientes/mes a 100 clientes/mes (sin más publicidad)"
    }
]

def obtener_cuerpo_email(zona, telefono):
    """Retorna el cuerpo del email según la zona"""

    cuerpos = {
        "La Boca": f"""Hola,

Vi que ofrecen servicios eléctricos de calidad en La Boca.

Pero hay un problema: NO tienen sitio web.

¿Qué significa eso?

AHORA (sin web):
- Clientes buscan "Electricista La Boca" en Google
- Encuentran competidores CON web
- Van con ellos
- Ustedes pierden ese cliente

NÚMEROS EN LA BOCA:
- Búsquedas/mes de "Electricista": ~200
- Sin web pierden: ~40% = 80 búsquedas/mes
- Conversión promedio: 50% = 40 clientes perdidos/mes
- 40 clientes × $330 = $13,200/mes
- $13,200/mes × 12 = $158,400/AÑO

¿Creen que pierden $158,400 al año porque no aparecen en Google?

SOLUCIÓN:
- Sitio web moderno
- Google Business optimizado
- Chatbot WhatsApp
- Email marketing

RESULTADO: +50 clientes nuevos/mes × $330 = $198,000/año en NUEVO revenue

COSTO: $2,000 setup + $400/mes = $6,800/año
ROI: 29x en año 1

¿Podemos hablar 15 minutos sobre cómo hacerlo?

Soy especialista en transformación digital para servicios.

Teléfono: {telefono}
Email: argentia.ai@gmail.com""",

        "Almagro": f"""Hola,

Noté que ofrecen servicios eléctricos en Almagro.

Ubicación estratégica, buenos profesionales.

Pero digitalmente, están desconectados.

PROBLEMA:
- Almagro: ~330 búsquedas/mes de "Electricista"
- Sin web aparecen: 0%
- Competencia con web aparece: 80%+

RESULTADO: pierden ~$200,000/año en clientes que buscan online

COMPARACIÓN:
TÚ (ahora):
❌ Sin sitio web
❌ Sin Google Business
❌ No aparecen en búsquedas

COMPETENCIA (con web):
✅ Web profesional
✅ Google Business optimizado
✅ Fotos antes/después
✅ +60% más clientes

SOLUCIÓN: Web + Google Business + Chatbot
COSTO: $2,000 setup + $400/mes
RESULTADO: +50 clientes/mes × $300 = $180,000/año en nuevo revenue

¿Hablamos 15 minutos?

Soy especialista en Digital para Servicios Técnicos.

Teléfono: {telefono}
Email: argentia.ai@gmail.com""",

        "San Isidro": f"""Hola,

General Electric Service hace buen trabajo en San Isidro.

Service de electrodomésticos, especialización clara.

Pero digitalmente, no están posicionados.

OPORTUNIDAD EN SAN ISIDRO:
- Búsquedas/mes: ~280
- Sin web: no aparecen = 0%
- Con web: podrían aparecer en 70%+

DINERO PERDIDO:
- 280 búsquedas × 70% = 196 potenciales/mes
- 40% se convierte = 78 clientes/mes
- 78 × $400 = $31,200/mes = $374,400/AÑO en dinero perdido

SOLUCIÓN:
- Sitio web
- Google Business
- Chatbot WhatsApp automático
- Email marketing

RESULTADO: +60 clientes nuevos/mes = $240,000/año en NUEVO revenue

COSTO: $2,000 + $400/mes = $6,800/año
ROI: 35x

¿Podemos explorar cómo?

Teléfono: {telefono}
Email: argentia.ai@gmail.com""",

        "Devoto": f"""Hola AA Service,

Vi que ofrecen servicios completos: residencial, comercial, emergencias.

Eso es bueno.

Pero el problema: la mayoría de clientes vienen por referencia, no por Google.

¿QUÉ SIGNIFICA ESO?
- Están atrapados en el 40% de clientes "boca a boca"
- Pierden el 60% que busca online

NÚMEROS DEVOTO/ZONA:
- Búsquedas/mes: ~350
- Sin web optim.: capturan ~20% = 70 búsquedas
- Con web optim.: podrían capturar ~70% = 245 búsquedas
- Diferencia: 175 clientes potenciales/mes perdidos

175 × $350 = $61,250/mes = $735,000/AÑO en oportunidad

PARA CAPTURARLO:
- Web moderna
- Google Business optimizado
- Chatbot responda consultas 24/7
- Email marketing

RESULTADO:
- De 40 a 100 clientes/mes

¿Hablamos 15 minutos?

Especialista en Digital para Servicios Técnicos.

Teléfono: {telefono}
Email: argentia.ai@gmail.com"""
    }

    return cuerpos.get(zona, "")

def enviar_emails():
    """Envía los 5 emails automáticamente"""

    print("="*60)
    print("📧 ENVIANDO 5 EMAILS A ELECTRICISTAS")
    print("="*60)

    enviados = 0
    fallidos = 0

    try:
        # Conecta a Gmail
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(TU_EMAIL, TU_PASSWORD)

        # Envía cada email
        for electricista in ELECTRICISTAS:

            print(f"\n📤 Enviando a {electricista['nombre']} ({electricista['email']})...")

            try:
                # Crea el mensaje
                mensaje = MIMEMultipart()
                mensaje['From'] = TU_EMAIL
                mensaje['To'] = electricista['email']
                mensaje['Subject'] = electricista['asunto']

                # Obtiene el cuerpo personalizado
                cuerpo = obtener_cuerpo_email(electricista['zona'], TU_TELEFONO)

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

    if enviados == 5:
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
