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

# ===== 17 TALLERES MECÁNICOS Y ELECTROMECÁNICOS EN MENDOZA =====
TALLERES = [
    {
        "nombre": "ELECTRICIDAD AUTOMOTRIZ B.M",
        "email": "contacto@electricidadbm.com.ar",
        "zona": "Las Heras",
        "asunto": "B.M: Web + IA + Agente de voz = +120% clientes en Mendoza"
    },
    {
        "nombre": "Taller JR Mecánica y Electricidad",
        "email": "info@tallerjr.com.ar",
        "zona": "San Rafael",
        "asunto": "JR: Mecánica + Eléctrica + IA + Agente automático"
    },
    {
        "nombre": "Belgrano Service",
        "email": "contacto@belgrano-service.com.ar",
        "zona": "Godoy Cruz",
        "asunto": "Belgrano: Inyección + Electricidad + IA = Excelencia digital"
    },
    {
        "nombre": "Taller ARAYA",
        "email": "info@talleraraya.com.ar",
        "zona": "Maipú",
        "asunto": "ARAYA: Multimarca + IA + Web = De 20 a 55+ clientes/semana"
    },
    {
        "nombre": "Electricidad Godoy",
        "email": "info@electricidadgodoy.com.ar",
        "zona": "Godoy Cruz",
        "asunto": "Godoy: Especializado + IA + Agente de voz 24/7"
    },
    {
        "nombre": "Central Repuestos Eléctricos",
        "email": "contacto@centralrepuestos.com.ar",
        "zona": "San José",
        "asunto": "Central: Bobinados + Eléctrica + IA + Web profesional"
    },
    {
        "nombre": "SOL SERVICENTRO",
        "email": "info@solservicent.com.ar",
        "zona": "Guaymallén",
        "asunto": "SOL: Multimarca + IA + Voz automática = +150% ventas"
    },
    {
        "nombre": "Luis Sánchez Electricidad",
        "email": "contacto@luissanchez-electrico.com.ar",
        "zona": "Las Heras",
        "asunto": "Sánchez: Especializado + IA + Agente automático"
    },
    {
        "nombre": "Electricidad Automotor Benegas",
        "email": "info@electricidadbenegas.com.ar",
        "zona": "Godoy Cruz",
        "asunto": "Benegas: Especializada + IA + Cero llamadas perdidas"
    },
    {
        "nombre": "Electricidad Automotor Terrada",
        "email": "contacto@electricidadterrada.com.ar",
        "zona": "Godoy Cruz",
        "asunto": "Terrada: Servicio completo + IA + Web + Agente de voz"
    },
    {
        "nombre": "Electricidad Automotor P J Ortiz",
        "email": "info@electricidadpjortiz.com.ar",
        "zona": "Las Heras",
        "asunto": "P J Ortiz: Electricidad + IA + Agente automático"
    },
    {
        "nombre": "Electricidad Automotor San Miguel",
        "email": "contacto@electricidadsanmiguel.com.ar",
        "zona": "Las Heras",
        "asunto": "San Miguel: Especializado + IA + Voz automática"
    },
    {
        "nombre": "Marchionni Car Service",
        "email": "info@marchionnicarservice.com",
        "zona": "Mendoza",
        "asunto": "Marchionni: 30 años + IA + Web = Liderazgo digital"
    },
    {
        "nombre": "Centro Mecánico Multimarca",
        "email": "contacto@centromultimarca.com.ar",
        "zona": "Godoy Cruz",
        "asunto": "Centro Multimarca: Integral + IA + Agente de voz"
    },
    {
        "nombre": "Taller San Martín Barrio Infanta",
        "email": "info@tallerinfanta.com.ar",
        "zona": "San Martín",
        "asunto": "Infanta: Taller + IA + Web profesional + Agente automático"
    },
    {
        "nombre": "Taller San Martín Infanta 10",
        "email": "contacto@tallerinfanta10.com.ar",
        "zona": "San Martín",
        "asunto": "Infanta 10: Servicio integral + IA + Voz automática"
    },
    {
        "nombre": "Reparación Tractores y Máquinas Viales",
        "email": "info@reparaciontractores.com.ar",
        "zona": "Godoy Cruz",
        "asunto": "Reparación Máquinas: Especializado + IA + Web optimizada"
    }
]

def obtener_cuerpo_email(nombre, telefono):
    """Retorna el cuerpo del email personalizado"""

    cuerpo = f"""Hola {nombre},

Vi que ofrecen servicio mecánico y electromecánico en Mendoza.

El problema: cuando un cliente busca "taller mecánico Mendoza" o "electricidad automotriz"
en Google, ¿dónde apareces?

La mayoría de talleres NO aparecen en Google. Eso significa:
- Clientes nuevos buscan online
- No te encuentran
- Van a la competencia

¿NÚMEROS EN MENDOZA?
- Búsquedas/mes de "taller mecánico": ~1,800
- Búsquedas/mes de "electricidad automotriz": ~900
- Total: ~2,700 búsquedas/mes
- Sin presencia digital: pierden 90% = 2,430 búsquedas/mes

Si el 25% se convierte:
- 2,430 × 25% = 607 clientes potenciales PERDIDOS/mes
- 607 × $300 (promedio trabajo) = $182,100/mes = $2,185,200/AÑO

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
    print("📧 ENVIANDO EMAILS A TALLERES DE MENDOZA")
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

    if enviados == 17:
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
