# Manual Profesional - Matriz VolumÃ©trica LED
## Escalable de 1.000 a 125.000 LEDs

---

# CapÃ­tulo 1: Arquitectura del Sistema

## 1.1 Diagrama de Red

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                        PC (Control Principal)                   â”‚
â”‚              TouchDesigner / Madrix / xLights / Resolume        â”‚
â”‚                          â–¼ Salida DDP/Art-Net                   â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                           â”‚ UTP Cat6 Ethernet
                           â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                   SWITCH GIGABIT ADMINISTRABLE                  â”‚
â”‚                     (MÃ­nimo 8 puertos)                          â”‚
â”‚                   VLAN separadas: Datos / Control               â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                           â”‚
           â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
           â–¼               â–¼               â–¼               â–¼
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”     â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”     â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”     â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚Control 1 â”‚     â”‚Control 2 â”‚     â”‚Control 3 â”‚     â”‚Control N â”‚
    â”‚16 salidasâ”‚     â”‚32 salidasâ”‚     â”‚16 salidasâ”‚     â”‚32 salidasâ”‚
    â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”˜     â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”˜     â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”˜     â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”˜
         â”‚                â”‚                â”‚                â”‚
    â”Œâ”€â”€â”€â”€â”´â”€â”€â”€â”€â”      â”Œâ”€â”€â”€â”€â”´â”€â”€â”€â”€â”      â”Œâ”€â”€â”€â”€â”´â”€â”€â”€â”€â”      â”Œâ”€â”€â”€â”€â”´â”€â”€â”€â”€â”
    â”‚Tiras    â”‚      â”‚Tiras    â”‚      â”‚Tiras    â”‚      â”‚Tiras    â”‚
    â”‚LED 1-16 â”‚      â”‚LED 1-32 â”‚      â”‚LED 1-16 â”‚      â”‚LED 1-32 â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜      â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜      â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜      â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

## 1.2 Protocolos de ComunicaciÃ³n

| Protocolo | Ancho de Banda | Latencia | Compatibilidad | Recomendado |
|-----------|----------------|----------|----------------|-------------|
| **DDP** | Alto (hasta 1GB/s) | Muy baja | WLED, xLights, Falcon | âœ… SÃ |
| **Art-Net** | Medio | Media | Universal | âœ… SÃ |
| **sACN** | Alto | Baja | Profesional | âœ… SÃ |
| **E1.31** | Medio | Media | Legacy | âš ï¸ Opcional |

### Protocolo DDP (Distributed Display Protocol)
- **Ventajas:** Sin overhead de frame, eficiente, bajo latencia
- **Paquete:** MÃ¡ximo 1460 bytes payload
- **Puerto:** UDP 4048
- **Max LEDs/red:** Sin lÃ­mite teÃ³rico

### Protocolo Art-Net
- **Ventajas:** Universo estÃ¡ndar, amplia compatibilidad
- **LimitaciÃ³n:** 512 canales por universo (170 LEDs RGB)
- **Puerto:** UDP 6454
- **Universos necesarios:** LEDs Ã· 170

### Protocolo sACN (E1.31)
- **Ventajas:** Unicast/Multicast, escalable
- **LimitaciÃ³n:** 512 canales por universo
- **Puerto:** UDP 5568

## 1.3 TopologÃ­a de Red

### Para 1.000 LEDs (10Ã—10Ã—10)
```
PC â†’ Switch 8 puertos â†’ 1-2 Controladores â†’ 100 tiras
```

### Para 8.000 LEDs (20Ã—20Ã—20)
```
PC â†’ Switch 16 puertos â†’ 4-7 Controladores â†’ 400 tiras
```

### Para 27.000 LEDs (30Ã—30Ã—30)
```
PC â†’ Switch 24 puertos â†’ 10-17 Controladores â†’ 900 tiras
```

### Para 64.000 LEDs (40Ã—40Ã—40)
```
PC â†’ Switch Stack â†’ 25-40 Controladores â†’ 1600 tiras
```

### Para 125.000 LEDs (50Ã—50Ã—50)
```
PC â†’ Switch Core â†’ 40-65 Controladores â†’ 2500 tiras
```

---

# CapÃ­tulo 2: Comparativa TÃ©cnica de LEDs

## 2.1 Chips LED Comparativa

| Chip | Hilos | Voltaje | Velocidad | Robustez | Precio | Recomendado |
|------|-------|---------|-----------|----------|--------|-------------|
| **WS2811** | 3/4 | 12V | 800 kHz | Media | $ | âœ… BÃ¡sico |
| **WS2818** | 4 | 12V | 800 kHz | Alta | $$ | âœ… Recomendado |
| **UCS1903** | 3 | 12V | 800 kHz | Media | $ | âš ï¸ Limitado |
| **UCS2904** | 4 | 12V | 1 MHz | Muy Alta | $$$ | âœ… Premium |
| **UCS7604** | 4 | 12V | 1 MHz | Muy Alta | $$$ | âœ… Premium |
| **TM1934** | 4 | 12V | 800 kHz | Alta | $$ | âœ… Bueno |
| **GS8208** | 4 | 12V | 800 kHz | Alta | $$ | âœ… Bueno |
| **SK6812** | 4 | 5V | 800 kHz | Media | $$ | âš ï¸ Solo 5V |
| **WS2812** | 4 | 5V | 800 kHz | Baja | $ | âŒ No recomendado |
| **APA102** | 4 | 5V | SPI | Media | $$$ | âš ï¸ SPI only |

## 2.2 CaracterÃ­sticas Detalladas

### WS2811 (3/4 hilos)
- **Protoclo:** One-wire (o backup en 4 hilos)
- **Velocidad:** 800 kbps
- **Color:** RGB 8-bit (256 niveles por canal)
- **Temperatura:** -20Â°C a +60Â°C
- **Caudal de datos:** 30 fps tÃ­pico
- **Ideal para:** Presupuesto ajustado

### WS2818 (4 hilos - Backup Data)
- **Ventaja principal:** LÃ­nea de datos backup (BI)
- **Si falla DI, usa BI automÃ¡ticamente**
- **Protocolo:** Similar a WS2811
- **Ideal para:** Proyectos donde la confiabilidad importa

### UCS2904/UCS7604 (Premium)
- **Velocidad:** 1 MHz (vs 800 kHz)
- **CorrecciÃ³n de error:** Integrada
- **Inmunidad al ruido:** Superior
- **Largo de tira:** Hasta 100m sin inyecciÃ³n
- **Ideal para:** Proyectos profesionales, largas distancias

### TM1934
- **Inmunidad al ruido:** Excelente
- **Backup Data:** SÃ­
- **Estabilidad de color:** Superior
- **Ideal para:** Entornos con interferencia elÃ©ctrica

### GS8208
- **Backup Data:** SÃ­
- **Temperatura:** -40Â°C a +80Â°C
- **Resistencia:** Industrial
- **Ideal para:** Exteriores, condiciones extremas

## 2.3 Formato FÃ­sico - Pebble/Seed Pixel

| EspecificaciÃ³n | Valor Recomendado |
|----------------|-------------------|
| **DiÃ¡metro LED** | 5mm (5050) o 8mm |
| **SeparaciÃ³n** | 10 cm (volumÃ©tricos) |
| **Cable** | 18 AWG o 20 AWG |
| **ProtecciÃ³n** | IP65 (exterior) |
| **Conector** | JST SM 3/4 pines |
| **Rollo** | 1000 LEDs |

---

# CapÃ­tulo 3: Comparativa de Controladores

## 3.1 Controladores Comparativa General

| Controlador | Salidas | Universos | Protocolo | Precio | Ideal Para |
|-------------|---------|-----------|-----------|--------|------------|
| **LINETX LNX-370SP** | 16 | 96 | Ethernet | $$$ | 100-400 tiras |
| **deskontroller Lite V3** | 32 SPI | 32+ | Ethernet | $$ | Starter |
| **Falcon F16V5** | 16 | 64 | Ethernet | $$$ | Medio |
| **Falcon F48V4** | 48 | 192 | Ethernet | $$$$ | Grande |
| **Advatek PixLite Mk3** | 16-32 | Variable | Ethernet | $$$$ | Industrial |
| **Colorlight 5A-75B** | 16 | 64 | Ethernet | $$ | OEM |
| **Colorlight 9913** | 16 | 64 | Ethernet | $$$ | Industrial |
| **NovaStar MCTRL300** | 16 | 64 | Ethernet | $$$$ | LED walls |
| **NovaStar MCTRL4K** | 16 | 256 | Ethernet | $$$$$ | Ultra-res |
| **Huidu HD-WF2** | 16 | 64 | WiFi+Eth | $ | EconÃ³mico |
| **Huidu HD-WF4** | 32 | 128 | WiFi+Eth | $$ | Medio |
| **ESP32 + WLED** | 10-18 | Variable | WiFi/Eth | $ | DIY/Testing |
| **ESP32 + ESPixelStick** | 1-4 | Variable | WiFi/Eth | $ | DIY/Testing |
| **SanDevices E682** | 16 | 64 | Ethernet | $$$ | Legacy |
| **SanDevices E6804** | 4 | 16 | Ethernet | $$ | Legacy |
| **J1Sys ECG-P2** | 16 | 64 | Ethernet | $$$ | Legacy |
| **MeanWell HLG** | N/A | N/A | N/A | $$ | Fuentes |
| **Arduino + shield** | 1-4 | Variable | Serial | $ | Prototipo |
| **Raspberry Pi** | 1-4 | Variable | WiFi/Eth | $ | WLED |
| **K10/K8000** | 8 | 32 | Ethernet | $$$ | Show |
| **PixCon16** | 16 | 64 | Ethernet | $$$ | xLights |

## 3.2 Controladores Detallados

### LINETX LNX-370SP
- **Salidas:** 16 (RJ45)
- **Universos:** 96 Art-Net/sACN
- **Protocolo:** DDP, Art-Net, sACN
- **AlimentaciÃ³n:** 12V-24V DC
- **Conectividad:** Ethernet 100 Mbps
- **Procesador:** ARM Cortex
- **FW:** Actualizable vÃ­a red
- **Precio:** ~$150-200 USD
- **Link:** https://www.linetx.com/html/product/LNX-370SP_en.php

### deskontroller Lite V3
- **Salidas:** 32 (SPI)
- **Protocolo:** DDP, Art-Net
- **Conectividad:** Ethernet 100 Mbps
- **Ventaja:** FÃ¡cil configuraciÃ³n
- **Precio:** ~$100-150 USD
- **Link:** https://deskontroller.com/lite-v3/

### Falcon F16V5
- **Salidas:** 16
- **Universos:** 64
- **Protocolo:** DDP, Art-Net, sACN
- **Expandible:** SÃ­ (Falcon F48)
- **Precio:** ~$200-250 USD
- **Link:** https://pixelcontroller.com/store/featured/88-f16v5.html

### Falcon F48V4
- **Salidas:** 48
- **Universos:** 192
- **Para:** Grandes instalaciones
- **Precio:** ~$500-600 USD

### Advatek PixLite Mk3
- **Salidas:** 16-32
- **Protocolo:** DDP, Art-Net, sACN, sACN
- **Industrial:** SÃ­
- **Software:** PixLite Advanced
- **Precio:** ~$300-500 USD
- **Link:** https://www.advateklighting.com/products/pixel-control/pixlite-mk3

### Colorlight 5A-75B
- **Salidas:** 16
- **Protocolo:** Art-Net, sACN
- **Precio:** ~$80-120 USD
- **Uso:** ComÃºn en LED walls chinas

### Colorlight 9913
- **Salidas:** 16
- **Industrial:** SÃ­
- **Precio:** ~$200-300 USD

### NovaStar MCTRL300
- **Salidas:** 16
- **Para:** Pantallas LED profesionales
- **Precio:** ~$400-600 USD

### Huidu HD-WF2/HD-WF4
- **Salidas:** 16/32
- **WiFi:** SÃ­ (backup)
- **Precio:** ~$50-100 USD
- **Para:** Presupuesto ajustado

### ESP32 + WLED (DIY)
- **Costo:** ~$5-10 USD por controlador
- **Salidas:** 10-18 tiras
- **Protocolo:** DDP, Art-Net
- **Ideal para:** Testing, prototipos
- **LimitaciÃ³n:** WiFi (no recomendado para producciÃ³n)

## 3.3 CÃ¡lculo de Controladores Necesarios

| LEDs Totales | Tiras (10cm sep.) | Controladores (32 sal.) | Controladores (16 sal.) |
|--------------|-------------------|-------------------------|-------------------------|
| 1.000 | 100 | 4 | 7 |
| 8.000 | 400 | 13 | 25 |
| 27.000 | 900 | 29 | 57 |
| 64.000 | 1.600 | 50 | 100 |
| 125.000 | 2.500 | 79 | 157 |

**FÃ³rmula:** Tiras = LEDs totales Ã· LEDs por tira (tÃ­pico 50-100)

---

# CapÃ­tulo 4: DiseÃ±o ElÃ©ctrico

## 4.1 AlimentaciÃ³n

### CaracterÃ­sticas de la Fuente

| ParÃ¡metro | Valor |
|-----------|-------|
| **Voltaje** | 12V DC (consistente con LEDs) |
| **ProtecciÃ³n** | Cortocircuito, sobrecarga, sobrecalentamiento |
| **CertificaciÃ³n** | UL, CE, FCC |
| **Eficiencia** | >85% |
| **Rippling** | <200mV |

### Marcas Recomendadas
- **Mean Well** (LRS-150-12, LRS-350-12, HLG series)
- **XP Power**
- **TDK-Lambda**

## 4.2 Consumo por Tira

### Consumo TÃ­pico (WS2811 12V, 10cm separaciÃ³n)
- **LEDs por tira:** 50-100
- **Consumo por LED:** 0.3W (30% brillo) a 0.7W (100% brillo)
- **Consumo por tira:** 15W a 70W
- **Corriente por tira:** 1.25A a 5.8A (a 12V)

### Tabla de Consumo

| Brillo | Consumo/LED | Tira 50 LEDs | Tira 100 LEDs |
|--------|-------------|--------------|---------------|
| 10% | 0.07W | 3.5W | 7W |
| 30% | 0.21W | 10.5W | 21W |
| 50% | 0.35W | 17.5W | 35W |
| 70% | 0.49W | 24.5W | 49W |
| 100% | 0.7W | 35W | 70W |

## 4.3 InyecciÃ³n de AlimentaciÃ³n

### Reglas de InyecciÃ³n
1. **MÃ¡ximo 50 LEDs** entre puntos de inyecciÃ³n
2. **Cable de inyecciÃ³n:** 14-18 AWG segÃºn distancia
3. **GND comÃºn** entre todos los sistemas
4. **Fusible por rama** (recomendado 3-5A por rama)

### Diagrama de InyecciÃ³n
```
                    Fuente 12V 350W
                         â”‚
                    â”Œâ”€â”€â”€â”€â”´â”€â”€â”€â”€â”
                    â”‚  Fusible â”‚
                    â”‚   20A    â”‚
                    â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”˜
                         â”‚
            â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
            â”‚            â”‚            â”‚
       â”Œâ”€â”€â”€â”€â”´â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”´â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”´â”€â”€â”€â”€â”
       â”‚InyecciÃ³nâ”‚  â”‚InyecciÃ³nâ”‚  â”‚InyecciÃ³nâ”‚
       â”‚  Tira 1 â”‚  â”‚  Tira 2 â”‚  â”‚  Tira N â”‚
       â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”˜
            â”‚            â”‚            â”‚
       â”Œâ”€â”€â”€â”€â”´â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”´â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”´â”€â”€â”€â”€â”
       â”‚ Tira    â”‚  â”‚ Tira    â”‚  â”‚ Tira    â”‚
       â”‚ LED 1-50â”‚  â”‚LED 51-100â”‚ â”‚LED 101+ â”‚
       â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### CaÃ­da de TensiÃ³n

**FÃ³rmula:** Vdrop = (2 Ã— L Ã— I Ã— Ï) / A

Donde:
- L = longitud del cable (metros)
- I = corriente (amperios)
- Ï = resistividad del cobre (0.0172 Î©Â·mmÂ²/m)
- A = Ã¡rea del cable (mmÂ²)

### Tabla CaÃ­da de TensiÃ³n (12V)

| Distancia | 18 AWG | 16 AWG | 14 AWG |
|-----------|--------|--------|--------|
| 1m | 0.18V | 0.11V | 0.07V |
| 3m | 0.54V | 0.34V | 0.21V |
| 5m | 0.90V | 0.56V | 0.35V |
| 10m | 1.80V | 1.12V | 0.70V |

**MÃ¡ximo permitido:** 5% (0.6V en 12V)

## 4.4 Protecciones

### Fusibles
- **Por rama:** 3-5A (para 50-100 LEDs)
- **Principal:** 20-30A (para fuente completa)
- **Tipo:** AutomÃ¡ticos o rearmables

### Protecciones Recomendadas
1. **Sobrecorriente:** Fusibles por rama
2. **Sobrevoltaje:** TVS (Transient Voltage Suppressor)
3. **InversiÃ³n de polaridad:** DÃ­odo Schottky
4. **Descargas atmosfÃ©ricas:** Varistores MOV

## 4.5 DistribuciÃ³n de Potencia

### Para 1.000 LEDs
- **Consumo mÃ¡ximo:** 700W (100% brillo)
- **Consumo tÃ­pico:** 210W (30% brillo)
- **Fuente recomendada:** 350W (1 de 350W o 2 de 200W)

### Para 8.000 LEDs
- **Consumo mÃ¡ximo:** 5,600W
- **Consumo tÃ­pico:** 1,680W
- **Fuente recomendada:** 2,000W (4-6 fuentes de 350-500W)

### Para 27.000 LEDs
- **Consumo mÃ¡ximo:** 18,900W
- **Consumo tÃ­pico:** 5,670W
- **Fuente recomendada:** 7,000W (sistema distribuido)

### Para 64.000 LEDs
- **Consumo mÃ¡ximo:** 44,800W
- **Consumo tÃ­pico:** 13,440W
- **Fuente recomendada:** 16,000W (sistema distribuido + monitoreo)

### Para 125.000 LEDs
- **Consumo mÃ¡ximo:** 87,500W
- **Consumo tÃ­pico:** 26,250W
- **Fuente recomendada:** 30,000W (instalaciÃ³n industrial)

---

# CapÃ­tulo 5: DiseÃ±o MecÃ¡nico

## 5.1 Estructuras por TamaÃ±o

### Cubo 10Ã—10Ã—10
- **Dimensiones:** 50cm Ã— 50cm Ã— 50cm (con 5cm margen)
- **Tiras:** 100 tiras de 10 LEDs
- **SeparaciÃ³n:** 5cm entre tiras verticales
- **Material:** Aluminio 2020 o impresiÃ³n 3D PLA/PETG
- **Peso estimado:** 5-8 kg (sin estructura)

### Cubo 20Ã—20Ã—20
- **Dimensiones:** 100cm Ã— 100cm Ã— 100cm
- **Tiras:** 400 tiras de 20 LEDs
- **SeparaciÃ³n:** 5cm entre tiras
- **Material:** Aluminio 3030 o perfiles de acero
- **Peso estimado:** 20-30 kg

### Cubo 30Ã—30Ã—30
- **Dimensiones:** 150cm Ã— 150cm Ã— 150cm
- **Tiras:** 900 tiras de 30 LEDs
- **Estructura:** Marco modular con paneles intercambiables

### Cubo 40Ã—40Ã—40
- **Dimensiones:** 200cm Ã— 200cm Ã— 200cm
- **Tiras:** 1,600 tiras de 40 LEDs
- **Estructura:** Industrial, soporte profesional

### Cubo 50Ã—50Ã—50
- **Dimensiones:** 250cm Ã— 250cm Ã— 250cm
- **Tiras:** 2,500 tiras de 50 LEDs
- **Estructura:** InstalaciÃ³n permanente

## 5.2 Materiales

### Perfiles de Aluminio
| Perfil | Uso | Resistencia |
|--------|-----|-------------|
| 2020 | Cubos pequeÃ±os | Media |
| 3030 | Cubos medianos | Alta |
| 4040 | Cubos grandes | Muy alta |
| 6060 | Industrial | Extrema |

### Soportes para Tiras
- **ImpresiÃ³n 3D:** Clips personalizados
- **Aluminio:** Canaletas con tapa
- **Acero:** Soportes soldados (grandes)

### FijaciÃ³n
- **Tornillos:** M3, M4, M5 (segÃºn perfil)
- **Adhesivo:** 3M VHB o silicona industrial
- **Abrazaderas:** PlÃ¡sticas o metÃ¡licas

## 5.3 DiseÃ±o Zigzag

### Por Capa (Vista Superior)
```
Capa 1 (Z=0):
â”Œâ”€â”€â”€â”¬â”€â”€â”€â”¬â”€â”€â”€â”¬â”€â”€â”€â”¬â”€â”€â”€â”¬â”€â”€â”€â”¬â”€â”€â”€â”
â”‚ 1 â”‚ 2 â”‚ 3 â”‚ 4 â”‚ 5 â”‚ 6 â”‚ 7 â”‚  â† Fila 1 (izq a der)
â”œâ”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¤
â”‚14 â”‚13 â”‚12 â”‚11 â”‚10 â”‚ 9 â”‚ 8 â”‚  â† Fila 2 (der a izq)
â”œâ”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¤
â”‚15 â”‚16 â”‚17 â”‚18 â”‚19 â”‚20 â”‚21 â”‚  â† Fila 3
â”œâ”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¤
â”‚28 â”‚27 â”‚26 â”‚25 â”‚24 â”‚23 â”‚22 â”‚  â† Fila 4
â”œâ”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¤
â”‚29 â”‚30 â”‚31 â”‚32 â”‚33 â”‚34 â”‚35 â”‚  â† Fila 5
â”œâ”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¤
â”‚42 â”‚41 â”‚40 â”‚39 â”‚38 â”‚37 â”‚36 â”‚  â† Fila 6
â”œâ”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¼â”€â”€â”€â”¤
â”‚43 â”‚44 â”‚45 â”‚46 â”‚47 â”‚48 â”‚49 â”‚  â† Fila 7
â””â”€â”€â”€â”´â”€â”€â”€â”´â”€â”€â”€â”´â”€â”€â”€â”´â”€â”€â”€â”´â”€â”€â”€â”´â”€â”€â”€â”˜
```

### Transiciones entre Capas
- **ConexiÃ³n:** De Ãºltimo LED capa N a primero LED capa N+1
- **UbicaciÃ³n:** Esquina trasera (oculta)
- **LEDs perdidos:** 1 por transiciÃ³n (6 en cubo 7Ã—7Ã—7)

---

# CapÃ­tulo 6: Software

## 6.1 Comparativa de Software

| Software | Uso Principal | Protocolo | Precio | Curva Aprendizaje |
|----------|---------------|-----------|--------|-------------------|
| **TouchDesigner** | Contenido generativo | DDP, Art-Net | Gratis/Pro | Alta |
| **Madrix** | Efectos en tiempo real | DDP, Art-Net, sACN | $$$ | Media |
| **xLights** | Secuencias | DDP, Art-Net | Gratis | Baja |
| **Resolume** | Audiovisual | Art-Net, sACN | $$$ | Media |
| **WLED** | Control directo | DDP | Gratis | Baja |
| **Falcon Player** | Secuencias | DDP, Art-Net | Gratis | Baja |
| **QLab** | Shows | Art-Net | $$$ | Media |

## 6.2 TouchDesigner

### InstalaciÃ³n
1. Descargar de https://derivative.ca
2. VersiÃ³n gratuita para uso no comercial
3. Licencia comercial: ~$600 USD

### ConfiguraciÃ³n para LED VolumÃ©trico
```
COMPONENTES:
- DAT: Text DAT para DDP
- CHOP: Audio analysis
- TOP: Render 3D
- SOP: GeometrÃ­a del cubo
- MAT: Material LED

FLUJO:
Audio/Video â†’ TOP â†’ SOP â†’ DAT â†’ DDP Out â†’ Controladores
```

### Ejemplo de Red DDP
```
1. Crear DAT: text1
2. Script:
   op('text1').text = f'/leds {ddp_data}'
   
3. Out DAT: dat1 â†’ DDP
```

## 6.3 Madrix

### ConfiguraciÃ³n
1. **Patch:** Definir disposiciÃ³n de LEDs
2. **Universos:** Asignar por controlador
3. **Efectos:** Layers con efectos predefinidos
4. **Output:** DDP/Art-Net a controladores

### Pasos
1. Nuevo proyecto â†’ Matrix Wizard
2. Definir dimensiones (X, Y, Z)
3. Importar patch de controladores
4. Asignar universos
5. Output â†’ DDP

## 6.4 xLights

### ConfiguraciÃ³n
1. **Controller Setup:** Agregar controladores
2. **Model Setup:** Definir geometrÃ­a 3D
3. **Sequence:** Crear secuencias
4. **Output:** DDP a controladores

### Modelos 3D
- **Tipo:** Matrix 3D
- **Dimensiones:** XÃ—YÃ—Z
- **String:** Cada tira = 1 string

## 6.5 Resolume

### Para Audiovisual
1. **Layer:** VÃ­deo o generativo
2. **DMX:** Art-Net out
3. **Mapping:** Asignar a LEDs
4. **Sync:** BPM sync con audio

## 6.6 WLED

### ConfiguraciÃ³n
1. Flashear ESP32 con WLED
2. Conectar a red
3. Configurar: Config â†’ LED Preferences
4. Agregar segmentos por tira
5. Efectos en tiempo real

### Ideal Para
- Prototipos
- Testing
- Instalaciones permanentes con ESP32

---

# CapÃ­tulo 7: CÃ¡lculo de Universos

## 7.1 FÃ³rmulas

### Art-Net / sACN
```
Universos = (Total LEDs Ã— 3) Ã· 512
```
*(3 canales por LED RGB, 512 canales por universo)*

### DDP
```
Universos DDP â‰ˆ (Total LEDs Ã— 3) Ã· 1440
```
*(Paquetes mÃ¡s eficientes)*

## 7.2 Tabla de Universos

| LEDs | Art-Net Universos | sACN Universos | DDP (aprox) |
|------|-------------------|----------------|-------------|
| 1.000 | 6 | 6 | 2 |
| 8.000 | 48 | 48 | 17 |
| 27.000 | 159 | 159 | 56 |
| 64.000 | 377 | 377 | 133 |
| 125.000 | 736 | 736 | 260 |

## 7.3 DistribuciÃ³n de Universos por Controlador

### Ejemplo: 8.000 LEDs con deskontroller (32 salidas)
```
Controladores necesarios: 13
LEDs por controlador: ~615
Tiras por controlador: ~31
Universos por controlador: 4 (Art-Net)
```

---

# CapÃ­tulo 8: Lista de Materiales (BOM)

## 8.1 Para 1.000 LEDs (10Ã—10Ã—10)

| Item | Cantidad | Precio Unitario | Total |
|------|----------|-----------------|-------|
| LEDs WS2811 12V 10cm | 10 rollos (1000) | $50 | $500 |
| Controlador LINETX | 7 | $175 | $1,225 |
| Fuente Mean Well 350W | 2 | $45 | $90 |
| Switch Gigabit 8 puertos | 1 | $30 | $30 |
| Cable UTP Cat6 (100m) | 1 | $25 | $25 |
| Cable 18 AWG (50m) | 2 | $20 | $40 |
| Fusibles y portafusibles | 1 kit | $15 | $15 |
| Conectores JST | 50 | $0.50 | $25 |
| Estructura aluminio 2020 | 1 set | $100 | $100 |
| **TOTAL** | | | **$2,050** |

## 8.2 Para 8.000 LEDs (20Ã—20Ã—20)

| Item | Cantidad | Precio Unitario | Total |
|------|----------|-----------------|-------|
| LEDs WS2811 12V 10cm | 80 rollos (8000) | $50 | $4,000 |
| Controlador deskontroller V3 | 13 | $125 | $1,625 |
| Fuente Mean Well 500W | 8 | $65 | $520 |
| Switch Gigabit 16 puertos | 1 | $60 | $60 |
| Cable UTP Cat6 (300m) | 3 | $25 | $75 |
| Cable 18 AWG (200m) | 4 | $20 | $80 |
| Fusibles y portafusibles | 2 kits | $15 | $30 |
| Conectores JST | 400 | $0.50 | $200 |
| Estructura aluminio 3030 | 1 set | $400 | $400 |
| **TOTAL** | | | **$6,990** |

## 8.3 Para 27.000 LEDs (30Ã—30Ã—30)

| Item | Cantidad | Precio Unitario | Total |
|------|----------|-----------------|-------|
| LEDs WS2811 12V 10cm | 270 rollos | $50 | $13,500 |
| Controlador deskontroller V3 | 29 | $125 | $3,625 |
| Fuente Mean Well 500W | 25 | $65 | $1,625 |
| Switch Stack 24 puertos | 2 | $150 | $300 |
| Cable UTP Cat6 (500m) | 5 | $25 | $125 |
| Cable 18 AWG (400m) | 8 | $20 | $160 |
| Fusibles y portafusibles | 4 kits | $15 | $60 |
| Conectores JST | 900 | $0.50 | $450 |
| Estructura aluminio 4040 | 1 set | $1,200 | $1,200 |
| **TOTAL** | | | **$21,045** |

## 8.4 Para 64.000 LEDs (40Ã—40Ã—40)

| Item | Cantidad | Precio Unitario | Total |
|------|----------|-----------------|-------|
| LEDs WS2811 12V 10cm | 640 rollos | $50 | $32,000 |
| Controlador deskontroller V3 | 50 | $125 | $6,250 |
| Fuente Mean Well 500W | 60 | $65 | $3,900 |
| Switch Core 48 puertos | 1 | $500 | $500 |
| Cable UTP Cat6 (1km) | 10 | $25 | $250 |
| Cable 18 AWG (800m) | 16 | $20 | $320 |
| Fusibles y portafusibles | 8 kits | $15 | $120 |
| Conectores JST | 1600 | $0.50 | $800 |
| Estructura aluminio 6060 | 1 set | $3,000 | $3,000 |
| **TOTAL** | | | **$47,140** |

## 8.5 Para 125.000 LEDs (50Ã—50Ã—50)

| Item | Cantidad | Precio Unitario | Total |
|------|----------|-----------------|-------|
| LEDs WS2811 12V 10cm | 1250 rollos | $50 | $62,500 |
| Controlador industrial OEM | 79 | $150 | $11,850 |
| Fuente industrial 1000W | 35 | $120 | $4,200 |
| Switch Core 48 puertos | 2 | $500 | $1,000 |
| Cable UTP Cat6 (2km) | 20 | $25 | $500 |
| Cable 14 AWG (1.5km) | 15 | $30 | $450 |
| Fusibles industriales | 16 kits | $25 | $400 |
| Conectores industriales | 2500 | $0.75 | $1,875 |
| Estructura steel industrial | 1 set | $8,000 | $8,000 |
| **TOTAL** | | | **$90,775** |

---

# CapÃ­tulo 9: EstimaciÃ³n de Costos

## 9.1 Resumen por Escala

| Escala | LEDs | Costo Total | Costo/LED |
|--------|------|-------------|-----------|
| **PequeÃ±o** | 1.000 | $2,050 | $2.05 |
| **Mediano** | 8.000 | $6,990 | $0.87 |
| **Grande** | 27.000 | $21,045 | $0.78 |
| **Industrial** | 64.000 | $47,140 | $0.74 |
| **Masivo** | 125.000 | $90,775 | $0.73 |

### Notas
- Precios estimados en USD (Julio 2026)
- No incluye mano de obra ni instalaciÃ³n
- Descuentos por volumen no considerados
- Precio LED incluye estructura bÃ¡sica

## 9.2 Costos Adicionales

| Concepto | Costo Estimado |
|----------|----------------|
| DiseÃ±o ingenierÃ­a | $500-2,000 |
| InstalaciÃ³n | $1,000-5,000 |
| ProgramaciÃ³n software | $500-3,000 |
| Pruebas y puesta en marcha | $300-1,000 |
| DocumentaciÃ³n | $200-500 |

---

# CapÃ­tulo 10: GuÃ­a de Montaje Paso a Paso

## 10.1 Fase 1: PreparaciÃ³n

### 1.1 Verificar Materiales
- [ ] LEDs recibidos y probados
- [ ] Controladores recibidos
- [ ] Fuentes de poder
- [ ] Cable UTP
- [ ] Cable de potencia
- [ ] Conectores
- [ ] Estructura

### 1.2 Preparar Espacio
- [ ] Mesa de trabajo limpia
- [ ] Herramientas disponibles
- [ ] VentilaciÃ³n adecuada
- [ ] IluminaciÃ³n suficiente

## 10.2 Fase 2: Ensamblaje de Estructura

### 2.1 Armar Marco Base
1. Conectar perfiles de aluminio
2. Verificar esquinas (90Â°)
3. Asegurar tornillerÃ­a

### 2.2 Instalar Soportes
1. Marcar posiciones de tiras
2. Instalar clips o canaletas
3. Verificar alineaciÃ³n

## 10.3 Fase 3: InstalaciÃ³n de LEDs

### 3.1 Preparar Tiras
1. Medir longitud necesaria
2. Cortar si es necesario (en puntos marcados)
3. Soldar conectores (si aplica)

### 3.2 Instalar Tiras
1. Colocar primera tira
2. Verificar direcciÃ³n de datos
3. Asegurar con clips
4. Repetir para todas las tiras

### 3.3 Conectar Tiras
1. Conectar DI a DO de tira anterior
2. Verificar polaridad
3. Dejar holgura para mantenimiento

## 10.4 Fase 4: Cableado ElÃ©ctrico

### 4.1 Cableado de Potencia
1. Distribuir fuentes de poder
2. Conectar inyecciÃ³n cada 50 LEDs
3. Verificar GND comÃºn
4. Instalar fusibles

### 4.2 Cableado de Datos
1. Conectar UTP a controladores
2. Conectar controladores a tiras
3. Verificar numeraciÃ³n de puertos

## 10.5 Fase 5: ConfiguraciÃ³n

### 5.1 Configurar Controladores
1. Asignar IPs estÃ¡ticos
2. Configurar universos
3. Asignar salidas a tiras

### 5.2 Configurar Software
1. Instalar software elegido
2. Importar patch de controladores
3. Definir geometrÃ­a 3D
4. Probar con patrones bÃ¡sicos

## 10.6 Fase 6: Pruebas

### 6.1 Prueba Individual
1. Probar cada tira por separado
2. Verificar colores correctos
3. Identificar LEDs fallados

### 6.2 Prueba Sistema
1. Probar todos los controladores
2. Verificar sincronizaciÃ³n
3. Probar con contenido complejo

### 6.3 Prueba de EstrÃ©s
1. Ejecutar 24 horas continuas
2. Monitorear temperaturas
3. Verificar estabilidad

---

# CapÃ­tulo 11: Referencia de Compra

## 11.1 LEDs - Proveedores Recomendados

### iPixel LED â­â­â­â­â­
- **Web:** https://www.ipixelled.com
- **Especialidad:** LEDs profesionales, volumÃ©tricos
- **Productos:** WS2811, WS2818, UCS2904
- **EnvÃ­o:** Internacional

### Ray Wu (AliExpress)
- **Web:** https://www.aliexpress.com/store/ray-wu
- **Especialidad:** LEDs para WLED, xLights
- **Ventaja:** Calidad consistente, buen precio

### ETOP LED
- **Web:** https://www.etopled.com
- **Especialidad:** Shows, volumÃ©tricos, fachadas
- **ReputaciÃ³n:** Excelente

### BTF-Lighting
- **Web:** https://www.btf-lighting.com
- **Especialidad:** Tiras LED, Seed Pixels
- **Calidad:** Muy buena

### Made-in-China (OEM)
- **Para:** Compras mayores a 500m
- **Precio:** Desde $247 USD/1000 LEDs

## 11.2 Controladores

| Proveedor | Link |
|-----------|------|
| LINETX | https://www.linetx.com/html/product/LNX-370SP_en.php |
| deskontroller | https://deskontroller.com/lite-v3/ |
| Falcon | https://pixelcontroller.com/store/featured/88-f16v5.html |
| Advatek | https://www.advateklighting.com/products/pixel-control/pixlite-mk3 |
| Colorlight | https://www.colorlighting.com |

## 11.3 Fuentes de Poder

| Marca | Modelo Recomendado | Web |
|-------|--------------------|-----|
| Mean Well | LRS-350-12, HLG-320H | https://www.meanwell.com |
| XP Power | Serie ECS | https://www.xppower.com |
| TDK-Lambda | Serie CEB | https://www.tdk-lambda.com |

## 11.4 Cable y Conectores

| Tipo | EspecificaciÃ³n | Proveedor |
|------|----------------|-----------|
| UTP Cat6 | 23 AWG, blindado | Monoprice, Amazon |
| Cable potencia | 18-14 AWG | Local |
| Conectores JST | SM 3/4 pin | Amazon, AliExpress |

---

# CapÃ­tulo 12: Troubleshooting

## 12.1 Problemas Comunes

| SÃ­ntoma | Causa Posible | SoluciÃ³n |
|---------|---------------|----------|
| LEDs no encienden | Sin poder | Verificar fuente y fusibles |
| LEDs parpadean | Datos inestables | Verificar conexiones UTP |
| Colores incorrectos | DirecciÃ³n invertida | Invertir DI/DO |
| Solo encienden algunos | Universo mal configurado | Revisar patch |
| LED muerto | Fallo fÃ­sico | Reemplazar tira |
| Calentamiento excesivo | Sobrecorriente | Reducir brillo, agregar inyecciÃ³n |

## 12.2 Monitoreo

### Temperatura
- **MÃ¡xima LED:** 60Â°C
- **MÃ¡xima fuente:** 70Â°C
- **Ambiente:** <35Â°C

### Consumo
- **Monitorear con:** WattÃ­metro
- **Alerta si:** >80% capacidad de fuente

---

# ApÃ©ndice A: Glosario

| TÃ©rmino | DefiniciÃ³n |
|---------|------------|
| **DDP** | Distributed Display Protocol |
| **Art-Net** | Protocolo DMX sobre Ethernet |
| **sACN** | Streaming ACN (E1.31) |
| **SPI** | Serial Peripheral Interface |
| **WS2811** | Chip LED controlador |
| **Pebble Pixel** | LED encapsulado redondo |
| **Seed Pixel** | LED encapsulado pequeÃ±o |
| **BOM** | Bill of Materials (Lista de Materiales) |
| **GND** | Tierra (Ground) |
| **AWG** | American Wire Gauge |

---

# ApÃ©ndice B: Referencias

1. WLED Documentation: https://kno.wled.ge
2. xLights: https://xlights.org
3. TouchDesigner: https://derivative.ca
4. Madrix: https://www.madrix.com
5. Resolume: https://resolume.com
6. Mean Well: https://www.meanwell.com
7. LINETX: https://www.linetx.com

---

**Manual Profesional - Matriz VolumÃ©trica LED**
**VersiÃ³n:** 1.0
**Fecha:** 25 de Julio 2026
**Autor:** Asistente AI

*Documento de referencia para construcciÃ³n de matrices volumÃ©tricas LED escalables.*
