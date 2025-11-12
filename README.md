
## Smart Irrigation System with Predictive Control

### **AI-Powered Precision Agriculture | IoT + Machine Learning + Linear Algebra**

Sistema inteligente de riego que combina sensores IoT, modelos predictivos y control automatizado para optimizar el uso de agua en cultivos.

Este proyecto integra:

| Pilar            | Tecnologías / Conceptos                                  |
| ---------------- | -------------------------------------------------------- |
| IoT Hardware     | ESP32, sensores ambientales, actuadores                  |
| Data Pipeline    | ETL, validación lógica, imputación, normalización        |
| Ciencia de Datos | Feature engineering, correlación, SelectKBest            |
| Machine Learning | Regresión, clasificación, sistema híbrido de reglas + ML |
| Álgebra Lineal   | Matrices, espacios vectoriales, PCA, regresión lineal    |
| Control          | Predicción futura + decisión inteligente automatizada    |
| Testing          | Casos normales, extremos, atípicos y simulación de borde |

---

## Objetivo

Crear un sistema autónomo capaz de:

- Predecir la humedad futura del suelo
- Decidir si activar la bomba antes de que la planta se deshidrate
- Ejecutar el riego vía actuadores IoT en tiempo real

> *“Riego predictivo, no reactivo.”*

Esto lo posiciona dentro de **Agricultura 4.0**, **Smart Farming** e **IoT AI Systems**.

---

## Funcionalidad Principal

### Sensor Data + ETL Inteligente

* Validación lógica (rango físico vs rango biológico)
* Detección de saturación de sensores (0/100)
* Imputación con mediana
* Eliminación de ruido y duplicados
* Transformación temporal avanzada (segmentos del día, fines de semana, tendencia)
* Normalización MinMax

### EDA & Feature Engineering

* Distribuciones, boxplots, estacionalidad
* Heatmap de correlación
* Índice NPK normalizado
* Dummies para ciclos temporales
* Selección de features SelectKBest

### Modelos

| Modelo              | Rol                                    |
| ------------------- | -------------------------------------- |
| Regresión Lineal    | Predecir humedad futura (1 hora)       |
| Regla Inteligente   | Umbral dinámico (basado en predicción) |
| Clasificador ML     | `regar / no regar`                     |
| Matriz de Confusión | Validación de performance              |

> **Sistema híbrido:** Matemática + ML + Regla adaptativa 

---

## Innovación Clave

> **Control Predictivo usando ML + lógica agronómica**
>
> Si la humedad futura < umbral dinámico → activar bomba antes del estrés hídrico

Esto replica enfoques industriales de **Model Predictive Control (MPC)**.

---

## Arquitectura

```
Sensors -> ESP32 -> Data Pipeline -> ML Models -> Decision Engine -> Actuators
```

* Humidity, temperature, water level, NPK
* ESP32 + WiFi + GPIO control
* Python (Pandas, NumPy, Sklearn, Matplotlib)
* Pipeline ETL completo
* Test Lab con valores simulados normales/extremos/anómalos

---

## Laboratorio de Pruebas Integrado

Casos evaluados:

- Condiciones normales
- Suelo extremadamente seco
- Humedad saturada
- Valores fuera de rango del sensor
- Ruido y datos faltantes
- Activación real del actuador vía ESP32

---

## Fundamentación Matemática (Álgebra Lineal)

| Contenido Académico        | Aplicación Real                       |
| -------------------------- | ------------------------------------- |
| Vectores y matrices        | Transformación de datos y features    |
| Sistemas lineales          | Regresión lineal aplicada             |
| Valores y vectores propios | PCA y reducción dimensional           |
| Funciones & gráficos       | EDA, funciones lineales/exponenciales |
| Álgebra computacional      | Python + NumPy + Pandas               |
| Unidad 6 completa          | Aplicaciones reales en Data Science   |

Proyecto supervisado en **Tecnicatura Sup. en Ciencia de Datos e IA — Cátedra Álgebra**

---

## Tecnologías

* Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
* ESP32, sensores DHT22 / humedad / NPK
* GPIO control
* Jupyter Notebook
* Git / CI Ready

---

## Estructura del Proyecto

```
/iot_esp32/      # Código ESP32
/etl/            # Limpieza 
/eda/            # Análisis exploratorio + visualizaciones
/ml/         # Regresión, clasificación, selectKBest. Sistema de riego inteligente. Laboratorio de valores reales + extremos
/readme.md
```

---

## Resultados

* Modelo predictivo estable para humedad futura
* Sistema de riego automatizado con decisión inteligente
* Ahorro de agua potencial vs riego tradicional
* Base para implementación en cultivos reales en Jujuy

---

## Autores:

**Sofia Anahi Viotti**

**Isaias Emanuel Sudañez**

**Katya Maria Nadales**

**Lucas Gonella**


> Desarrollo sistemas de IA aplicados a agricultura con IoT y Machine Learning

Proyecto académico profesionalizado — supervisión docente :

**Victor Palazzesi**
---

## Contribución y Futuro

Próximos pasos:

* Dashboard web tiempo real
* Sensor de caudal e Irrigation KPI
* Versión para invernaderos intensivos
* Edge AI en ESP32 (TinyML)

---





