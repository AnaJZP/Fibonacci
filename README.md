# 📊 Análisis de Retrocesos de Fibonacci

Este repositorio contiene una aplicación educativa desarrollada en Python para el análisis de retrocesos de Fibonacci en activos financieros. La herramienta está diseñada con fines pedagógicos para ayudar a estudiantes a comprender y aplicar los principios de los retrocesos de Fibonacci en el análisis técnico.


## 📋 Contenido

- [Características](#características)
- [Instalación](#instalación)
  - [Windows](#windows)
  - [macOS](#macos)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Fundamentos Teóricos](#fundamentos-teóricos)
- [Ejercicios Prácticos](#ejercicios-prácticos)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## ✨ Características

- **Descarga y análisis de datos financieros** desde Yahoo Finance
- **Visualización interactiva** de retrocesos de Fibonacci en gráficos de precios
- **Explicaciones didácticas** de conceptos clave (proporción áurea, niveles de retroceso)
- **Configuraciones personalizables** para diferentes activos y períodos de tiempo
- **Análisis para tendencias alcistas y bajistas**
- **Interpretación automática** de resultados
- **Ejercicios prácticos** para estudiantes
- **Interfaz amigable** desarrollada con Streamlit

## 🔧 Instalación

### Requisitos Previos

- Python 3.7+
- pip (gestor de paquetes de Python)
- Git

### Windows

1. **Clonar el repositorio**:
   Abre Git Bash o CMD y ejecuta:
   ```bash
   git clone https://github.com/AnaJZP/Fibonacci.git
   cd Fibonacci
   ```

2. **Configurar entorno virtual** (opcional pero recomendado):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

### macOS

1. **Clonar el repositorio**:
   Abre Terminal y ejecuta:
   ```bash
   git clone https://github.com/AnaJZP/Fibonacci.git
   cd Fibonacci
   ```

2. **Configurar entorno virtual** (opcional pero recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

## 📈 Uso

1. **Iniciar la aplicación Streamlit**:
   ```bash
   streamlit run app.py
   ```

2. **Interfaz de la aplicación**:
   - La aplicación se abrirá automáticamente en tu navegador predeterminado
   - Selecciona un ticker (símbolo de activo financiero)
   - Elige el período de tiempo para análisis
   - Selecciona el tipo de tendencia (alcista o bajista)
   - Haz clic en "Analizar" para generar el análisis

3. **Interpretación de resultados**:
   - Revisa los niveles de retroceso calculados
   - Examina cómo el precio ha interactuado con estos niveles
   - Considera las explicaciones automáticas proporcionadas

## 📁 Estructura del Proyecto

```
Fibonacci/
├── app.py                    # Aplicación principal Streamlit
├── teoria_fibonacci.md       # Documento con fundamentos teóricos
├── ejercicios_fibonacci.py   # Ejercicios prácticos para estudiantes
├── requirements.txt          # Dependencias del proyecto
├── img/                      # Imágenes y recursos visuales
└── README.md                 # Este archivo
```

## 📚 Fundamentos Teóricos

La aplicación se basa en los siguientes conceptos:

- **Secuencia de Fibonacci**: Serie numérica donde cada número es la suma de los dos anteriores (0, 1, 1, 2, 3, 5, 8, 13, 21, ...)
- **Proporción Áurea (φ)**: Aproximadamente 1.618, derivada de la relación entre números consecutivos en la secuencia de Fibonacci
- **Niveles de Retroceso**: Porcentajes derivados de relaciones matemáticas en la secuencia (23.6%, 38.2%, 50%, 61.8%, 78.6%)
- **Aplicación Financiera**: Estos niveles suelen actuar como áreas de soporte/resistencia en movimientos de precio

Para más detalles, consulta el archivo `teoria_fibonacci.md` incluido en este repositorio.

## 🧩 Ejercicios Prácticos

El repositorio incluye ejercicios prácticos para estudiantes, que cubren:

1. **Cálculo manual** de niveles de retroceso
2. **Identificación visual** de retrocesos en gráficos reales
3. **Backtesting** de efectividad histórica
4. **Desarrollo de estrategias** simples basadas en Fibonacci
5. **Programación** de herramientas de análisis en Python

Estos ejercicios están disponibles en el archivo `ejercicios_fibonacci.py`.

## 👨‍💻 Contribuir

Las contribuciones son bienvenidas. Para contribuir:

1. Haz un Fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/amazing-feature`)
3. Realiza tus cambios y haz commit (`git commit -m 'Add some amazing feature'`)
4. Push a la rama (`git push origin feature/amazing-feature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está distribuido bajo la licencia de "Amor a los datos".

## 📧 Contacto

Ana J - [GitHub: AnaJZP](https://github.com/AnaJZP)

Link del proyecto: [https://github.com/AnaJZP/Fibonacci](https://github.com/AnaJZP/Fibonacci)

---

**Nota**: Esta herramienta está diseñada con fines educativos. Las decisiones de inversión no deben basarse únicamente en análisis técnico.
