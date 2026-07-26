# Proyecto LED Cube VolumÃ©trico 7Ã—7Ã—7

## Resumen del Proyecto
Cubo volumÃ©trico de LEDs con patrÃ³n zigzag/vÃ­bora para efecto 3D.

---

## 1. Arquitectura del Sistema

**Objetivo:** Controlar una matriz 3D mediante Ethernet (UTP), sin Wiâ€‘Fi.

**Diagrama lÃ³gico:**
```
PC (TouchDesigner/Madrix/xLights)
â”‚
Switch Gigabit administrable
â”œâ”€ Controlador 1 â†’ Tiras
â”œâ”€ Controlador 2 â†’ Tiras
â””â”€ ...
```

**Protocolos recomendados:** DDP (preferido), Art-Net y sACN para compatibilidad.

---

## 2. LEDs

### EspecificaciÃ³n objetivo
- 12V, 4 hilos (DI+BI / Dual Data/Backup), 50 mm entre LEDs
- Cable transparente, 1000 LEDs por rollo

### Tipos de LED comparativa
| LED | Hilos | CaracterÃ­sticas |
|-----|-------|-----------------|
| WS2811 | 3 | EconÃ³mico |
| WS2818 | 4 | Backup Data, recomendado |
| UCS2904/UCS7604 | 4 | Alta robustez |
| TM1934 | 4 | Buena inmunidad al ruido |

**RecomendaciÃ³n:** 12V, 4 hilos, 50 mm, cable transparente.

### Links de compra LEDs
- https://yourpixelstore.com/product/yps-duo-pebble-seed-pixels-12v-dual-data-4-wire/
- https://www.holidaylighting.shop/product-page/12v-seed-pebble-pixel-1
- https://www.holidaycoro.com/Bulk-Roll-Seed-Pebble-Pixels-p/580.htm
- https://ezrgb-pixels.com/products/seed-pixel-roll

---

## 3. Controladores

### Comparativa
| Controlador | Salidas | Protocolo | Notas |
|-------------|---------|-----------|-------|
| LINETX LNX-370SP | 16 | Ethernet | 96 universos |
| deskontroller Lite V3 | 32 SPI | Ethernet | Buenos para starters |
| Falcon F16V5 | 16 | Ethernet | Expandible |
| Advatek PixLite | Varias | Ethernet | Industrial |
| Colorlight/NovaStar/Huidu | Varias | Ethernet | OEM para proyectos grandes |

### Links de compra controladores
- LINETX: https://www.linetx.com/html/product/LNX-370SP_en.php
- deskontroller: https://deskontroller.com/lite-v3/
- Falcon: https://pixelcontroller.com/store/featured/88-f16v5.html
- Advatek: https://www.advateklighting.com/products/pixel-control/pixlite-mk3

### CÃ¡lculo de controladores necesarios
- 100 tiras: 4 deskontroller o 7 LINETX
- 400 tiras: 13 deskontroller o 25 LINETX

---

## 4. Dimensiones y CÃ¡lculos

### Cubo 7Ã—7Ã—7
| Concepto | Cantidad |
|----------|----------|
| LEDs visibles en el volumen | 343 (7Ã—7Ã—7) |
| LEDs en vueltas (no visibles) | 48 |
| **Total de LEDs necesarios** | **391** |

### Matriz 10Ã—10Ã—10
- 1000 LEDs, 100 tiras de 10 LEDs

### Matriz 20Ã—20Ã—20
- 8000 LEDs, 400 tiras de 20 LEDs

### Dimensiones futuras
- 27000 LEDs y 64000 LEDs: migrar a controladores industriales OEM

---

## 5. Estructura Zigzag

### Por capa (vista superior):
- La tira de LEDs recorre las 49 posiciones en patrÃ³n serpiente:
  - Fila 1: Col1 â†’ Col2 â†’ Col3 â†’ Col4 â†’ Col5 â†’ Col6 â†’ Col7 (izq a der)
  - Fila 2: Col7 â†’ Col6 â†’ Col5 â†’ Col4 â†’ Col3 â†’ Col2 â†’ Col1 (der a izq)
  - Fila 3: Col1 â†’ Col2 â†’ Col3 â†’ Col4 â†’ Col5 â†’ Col6 â†’ Col7
  - Y asÃ­ sucesivamente para las 7 filas

### Conexiones entre columnas:
- De columna impar a par: conexiÃ³n por ABAJO
- De columna par a impar: conexiÃ³n por ARRIBA
- En cada vuelta se pierde 1 LED (no visible)

### Transiciones entre capas:
- 6 transiciones entre capas
- Cada transiciÃ³n tiene mÃºltiples vueltas
- Total: 48 LEDs ocultos

---

## 6. DiseÃ±o ElÃ©ctrico

- Fuentes distribuidas
- GND comÃºn entre controladores y pÃ­xeles
- InyecciÃ³n de alimentaciÃ³n segÃºn consumo real
- Protecciones con fusibles por rama y distribuciÃ³n por bloques

---

## 7. DiseÃ±o MecÃ¡nico

- **10Ã—10Ã—10:** 100 tiras de 10 LEDs
- **20Ã—20Ã—20:** 400 tiras de 20 LEDs
- SeparaciÃ³n propuesta: 50 mm entre LEDs
- Estructura rÃ­gida de aluminio o impresiÃ³n 3D para soportes

---

## 8. Software

| Software | Uso |
|----------|-----|
| TouchDesigner | Contenido generativo |
| Madrix | Efectos en tiempo real |
| xLights | Secuencias |
| Resolume | IntegraciÃ³n audiovisual |

Preferir DDP por eficiencia.

---

## 9. Cableado

- UTP Cat6 para datos Ethernet
- Cables de potencia separados
- Mantener SPI corto entre controlador y tira

---

## 10. Presupuesto Orientativo

| Escala | Componentes |
|--------|-------------|
| 1000 LEDs | LEDs, 4-7 controladores, fuentes, switch |
| 8000 LEDs | 13-25 controladores, mÃºltiples fuentes |
| 27000+ LEDs | Controladores industriales OEM, diseÃ±o modular |

---

## Archivos del Proyecto
- `volumetrico.md` - Este archivo consolidado
- `guia_compra_leds.md` - GuÃ­a de compra y proveedores
- `manual_profesional_matriz_volumetrica_led.md` - Manual profesional completo
- `resumen1.pdf` - Resumen tÃ©cnico (compra rollos LED, controladores)
- `resumen2.pdf` - GuÃ­a completa del proyecto
- `resumen3.pdf` - Manual profesional - Matriz VolumÃ©trica LED
- `info.txt` - Fabricantes, links y consulta para fabricantes
- ImÃ¡genes: `cable1.jpeg`, `cable2.jpeg`, `info1.jpeg`, `info2.jpeg`, `tester.jpeg`, `usb.jpeg`

---

## Estado del Proyecto
- **Fase:** DiseÃ±o / PlanificaciÃ³n
- **PrÃ³ximo paso:** Seleccionar controlador definitivo, definir fuentes, diseÃ±ar mapeo 3D

---
Ãšltima actualizaciÃ³n: 25 de julio 2026
