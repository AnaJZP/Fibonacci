import pandas as pd
import streamlit as st
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from PIL import Image
import io
import base64
import os

# Tratamos de importar el módulo de ejemplos
try:
    import ejemplos_fibonacci
    ejemplos_module_available = True
except ImportError:
    ejemplos_module_available = False

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Retrocesos de Fibonacci",
    page_icon="📈",
    layout="wide"
)

# Título y descripción
st.title("📊 Análisis de Retrocesos de Fibonacci")
st.markdown("""
#### Diseñado por Ana Lorena Jiménez Preciado. 
##### SEPI -ESE -IPN
##### DCE - Análisis Bursátil y Métodos Algorítmicos Avanzados

Esta aplicación te permite analizar los retrocesos de Fibonacci para diferentes activos financieros.
Los retrocesos de Fibonacci son una herramienta popular en el análisis técnico que ayuda a identificar
posibles niveles de soporte y resistencia basados en la secuencia de Fibonacci.
""")

# Sección teórica sobre Fibonacci
with st.expander("📚 Fundamentos Teóricos de Fibonacci", expanded=True):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### La Secuencia de Fibonacci
        
        La secuencia de Fibonacci es una serie de números donde cada número es la suma de los dos anteriores:
        
        **0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...**
        
        Matemáticamente:
        - F(0) = 0
        - F(1) = 1
        - F(n) = F(n-1) + F(n-2) para n > 1
        
        ### La Proporción Áurea (Phi)
        
        Cuando dividimos cualquier número de la secuencia por su predecesor, el resultado se aproxima a 1.618 conforme avanzamos en la serie.
        Este número, conocido como Phi (φ), es la proporción áurea:
        
        φ = 1.61803398875...
        
        Y su recíproco:
        
        1/φ = 0.61803398875...
        
        ### Retrocesos de Fibonacci en Finanzas
        
        Los niveles de retroceso de Fibonacci más utilizados son:
        - **0.236 (23.6%)**
        - **0.382 (38.2%)** - Derivado de la proporción 0.382 ≈ 3/8
        - **0.5 (50%)** - Aunque no es estrictamente un número Fibonacci, es incluido por su importancia psicológica
        - **0.618 (61.8%)** - El recíproco de la proporción áurea (1/φ)
        - **0.786 (78.6%)** - La raíz cuadrada de 0.618
        - **1.0 (100%)**
        
        Estos niveles ayudan a identificar posibles puntos de corrección en el precio después de un movimiento significativo.
        """)
    
    with col2:
        # Generamos imagen didáctica de la espiral de Fibonacci
        def create_fibonacci_spiral():
            fig, ax = plt.subplots(figsize=(6, 6))
            
            # Generar secuencia Fibonacci
            fib = [0, 1]
            for i in range(2, 12):
                fib.append(fib[i-1] + fib[i-2])
            
            # Crear espiral
            phi = (1 + 5**0.5) / 2
            theta = np.linspace(0, 8 * np.pi, 1000)
            r = phi ** (theta / (np.pi/2))
            
            ax.plot(r * np.cos(theta), r * np.sin(theta), color='blue')
            ax.set_title('Espiral de Fibonacci')
            ax.axis('equal')
            ax.grid(True)
            ax.set_axis_off()
            
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plt.close(fig)
            return buf
        
        # Mostrar la imagen
        image_buf = create_fibonacci_spiral()
        st.image(image_buf, caption="Espiral de Fibonacci", use_container_width=True)
        
        # Tabla de proporciones relevantes
        st.markdown("### Proporciones Importantes")
        proportions_data = {
            "Nivel": ["0.236", "0.382", "0.5", "0.618", "0.786", "1.0"],
            "Origen": ["Aproximado de F(n+3)/F(n+6)", "Aproximado a 3/8", "Mitad psicológica", "1/φ (inverso de φ)", "√0.618", "Retroceso completo"]
        }
        st.table(pd.DataFrame(proportions_data))

# Sección de la aplicación con múltiples páginas
st.sidebar.title("Navegación")
pages = ["Análisis de Retrocesos", "Ejemplos en Naturaleza y Arte"]
selected_page = st.sidebar.radio("Ir a", pages)

# Función para mostrar ejemplos básicos (respaldo)
def show_basic_examples():
    st.subheader("Ejemplos básicos de Fibonacci")
    st.write("""
    Aquí tienes algunos conceptos básicos sobre Fibonacci:
    
    1. La secuencia de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    2. Cada número es la suma de los dos anteriores
    3. La proporción entre números consecutivos se aproxima a φ = 1.618...
    4. Esta proporción aparece en la naturaleza, arte y mercados financieros
    """)
    
    # Crear una espiral simple como demostración
    def create_simple_spiral():
        fig, ax = plt.subplots(figsize=(8, 8))
        theta = np.linspace(0, 8 * np.pi, 1000)
        a = 0.15
        r = a * np.exp(theta * 0.3)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        ax.plot(x, y, 'b-')
        ax.set_title("Espiral inspirada en Fibonacci")
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_axis_off()
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close(fig)
        return buf
    
    st.image(create_simple_spiral(), caption="Espiral inspirada en la proporción áurea", use_container_width=True)

# Mostrar contenido según la página seleccionada
if selected_page == "Análisis de Retrocesos":
    # Sección de aplicación práctica
    st.header("🔍 Aplicación Práctica")
    
    # Configuración de parámetros
    col1, col2, col3 = st.columns(3)

    with col1:
        # Opción para ingresar ticker directamente
        ticker_default = "AAPL"
        ticker = st.text_input("Ingresa el símbolo del ticker:", ticker_default, 
                              help="Ejemplos: AAPL (Apple), MSFT (Microsoft), AMZN.MX (Amazon México)")
        
        # Sugerencias de tickers populares
        st.caption("Sugerencias: AAPL, MSFT, GOOGL, META, AMZN.MX, BIMBOA.MX, SPY.MX")

    with col2:
        # Período de tiempo
        period_options = {
            "1 mes": 30,
            "3 meses": 90,
            "6 meses": 180,
            "1 año": 252,
            "2 años": 504,
            "5 años": 1260,
            "Máximo disponible": 0  # Valor especial para indicar sin límite
        }
        selected_period = st.selectbox("Selecciona el período:", list(period_options.keys()))
        days = period_options[selected_period]

    with col3:
        # Selección del tipo de análisis
        trend_type = st.radio("Tipo de tendencia para análisis:", ("Alcista", "Bajista"))

    # Cargar datos
    @st.cache_data(ttl=3600)  # Caché de 1 hora
    def load_data(ticker, days):
        end_date = datetime.now()
        
        # No limitamos con días específicos al inicio, solo al final tomaremos los datos necesarios
        start_date = end_date - timedelta(days=days*3)  # Solicitamos el triple para tener suficientes datos
        
        try:
            # Método recomendado con la nueva versión de yfinance
            ticker_obj = yf.Ticker(ticker)
            data = ticker_obj.history(start=start_date)
            
            # Eliminar zona horaria del índice
            if data.index.tzinfo is not None:
                data.index = data.index.tz_localize(None)
            
            # Verificar y eliminar valores nulos
            na_count = data.isna().sum().sum()
            if na_count > 0:
                st.warning(f"Se encontraron {na_count} valores NA en los datos. Se eliminarán automáticamente.")
                data = data.dropna()
            
            if data.empty:
                return None, "No se encontraron datos para el ticker seleccionado."
                
            # Verificar que tenemos suficientes datos
            if len(data) < 30:
                st.warning("ADVERTENCIA: Pocos datos disponibles. Los resultados pueden no ser confiables.")
            
            # Si queremos limitar los días, lo hacemos aquí
            if days > 0:
                data = data.tail(days)  # Nos quedamos con los días solicitados
            
            return data, None
        except Exception as e:
            return None, f"Error al cargar datos: {str(e)}"

    # Función para calcular retrocesos de Fibonacci
    def calculate_fibonacci_levels(data, trend_type):
        try:
            if trend_type == "Alcista":
                # Para tendencia alcista, calculamos retrocesos del punto más bajo al más alto
                min_price = data['Low'].min()
                max_price = data['High'].max()
                min_idx = data['Low'].idxmin()
                max_idx = data['High'].idxmax()
            else:
                # Para tendencia bajista, calculamos retrocesos del punto más alto al más bajo
                max_price = data['High'].max()
                min_price = data['Low'].min()
                max_idx = data['High'].idxmax()
                min_idx = data['Low'].idxmin()
            
            # Verificar cronología para determinar si el análisis es relevante
            # Manejo seguro de la comparación de fechas
            if isinstance(min_idx, pd.Series):
                min_idx_value = min_idx.iloc[0]
            else:
                min_idx_value = min_idx
                
            if isinstance(max_idx, pd.Series):
                max_idx_value = max_idx.iloc[0]
            else:
                max_idx_value = max_idx
            
            if trend_type == "Alcista":
                # Si el máximo ocurre antes que el mínimo en una tendencia alcista, no es válido
                if max_idx_value < min_idx_value:
                    return None, "La cronología de puntos extremos no es adecuada para el tipo de tendencia seleccionada."
            else:  # Bajista
                # Si el mínimo ocurre antes que el máximo en una tendencia bajista, no es válido
                if min_idx_value < max_idx_value:
                    return None, "La cronología de puntos extremos no es adecuada para el tipo de tendencia seleccionada."
            
            # Calcular los niveles de retroceso
            diff = max_price - min_price
            levels = {
                0.0: max_price if trend_type == "Bajista" else min_price,
                0.236: max_price - 0.236 * diff if trend_type == "Bajista" else min_price + 0.236 * diff,
                0.382: max_price - 0.382 * diff if trend_type == "Bajista" else min_price + 0.382 * diff,
                0.5: max_price - 0.5 * diff if trend_type == "Bajista" else min_price + 0.5 * diff,
                0.618: max_price - 0.618 * diff if trend_type == "Bajista" else min_price + 0.618 * diff,
                0.786: max_price - 0.786 * diff if trend_type == "Bajista" else min_price + 0.786 * diff,
                1.0: min_price if trend_type == "Bajista" else max_price
            }
            
            return {
                'levels': levels,
                'min_price': min_price,
                'max_price': max_price,
                'min_idx': min_idx,
                'max_idx': max_idx
            }, None
        except Exception as e:
            return None, f"Error al calcular niveles de Fibonacci: {str(e)}"

    # Configuración avanzada en la barra lateral
    st.sidebar.header("Configuración Avanzada")
    show_volume = st.sidebar.checkbox("Mostrar volumen en gráfico", value=False)
    extended_levels = st.sidebar.checkbox("Mostrar niveles de extensión (1.272, 1.618)", value=False)

    # Cargar datos cuando se hace clic en el botón
    if st.button("Analizar"):
        with st.spinner("Cargando datos y calculando retrocesos..."):
            try:
                data, error = load_data(ticker, days)
                
                if error:
                    st.error(error)
                else:
                    st.subheader(f"Análisis de {ticker} - Últimos {days} días")
                    
                    # Mostrar información básica
                    col1, col2, col3 = st.columns(3)
                    # Corregir el formato de string para evitar el error
                    precio_actual = float(data['Close'].iloc[-1])
                    cambio_precio = float(data['Close'].iloc[-1] - data['Close'].iloc[-2])
                    precio_max = float(data['High'].max())
                    precio_min = float(data['Low'].min())
                    
                    col1.metric("Precio Actual", f"${precio_actual:.2f}", f"{cambio_precio:.2f}")
                    col2.metric("Máximo Período", f"${precio_max:.2f}")
                    col3.metric("Mínimo Período", f"${precio_min:.2f}")
                    
                    # Calcular niveles de Fibonacci
                    fib_data, fib_error = calculate_fibonacci_levels(data, trend_type)
                    
                    if fib_error:
                        st.warning(fib_error)
                    else:
                        # Visualizar con plotly
                        fig = go.Figure()
                        
                        # Preparar datos para el gráfico de velas
                        dates = list(data.index)
                        open_values = list(data['Open'])
                        high_values = list(data['High'])
                        low_values = list(data['Low'])
                        close_values = list(data['Close'])
                        
                        # Agregar gráfico de velas
                        fig.add_trace(go.Candlestick(
                            x=dates,
                            open=open_values,
                            high=high_values,
                            low=low_values,
                            close=close_values,
                            name="Precio",
                            increasing_line_color='green',
                            decreasing_line_color='red'
                        ))
                        
                        # Agregar líneas de retroceso de Fibonacci
                        colors = ['red', 'orange', 'gold', 'green', 'blue', 'purple', 'magenta']
                        levels = fib_data['levels']
                        
                        for i, (ratio, price) in enumerate(levels.items()):
                            # Asegurarse de que 'price' sea un valor escalar
                            if isinstance(price, pd.Series):
                                price_value = float(price.iloc[0])
                            else:
                                price_value = float(price)
                            
                            # Asegurarse de que 'ratio' sea un valor escalar    
                            if isinstance(ratio, pd.Series):
                                ratio_value = float(ratio.iloc[0])
                            else:
                                ratio_value = float(ratio)
                            
                            fig.add_hline(
                                y=price_value,  # Usar el valor escalar
                                line_dash="dash",
                                line_color=colors[i],
                                annotation_text=f"Retroceso {ratio_value*100:.1f}%: ${price_value:.2f}",
                                annotation_position="right"
                            )
                        
                        # Convertir valores extremos a escalares si son Series
                        min_price_value = float(fib_data['min_price']) if isinstance(fib_data['min_price'], pd.Series) else float(fib_data['min_price'])
                        max_price_value = float(fib_data['max_price']) if isinstance(fib_data['max_price'], pd.Series) else float(fib_data['max_price'])
                        
                        # Para los índices, mantenerlos como están si son fechas que Plotly puede manejar
                        min_idx_value = fib_data['min_idx']
                        max_idx_value = fib_data['max_idx']
                        
                        # Resaltar puntos extremos
                        fig.add_trace(go.Scatter(
                            x=[min_idx_value, max_idx_value],
                            y=[min_price_value, max_price_value],
                            mode='markers',
                            marker=dict(size=12, color='red'),
                            name='Puntos Extremos'
                        ))
                        
                        # Configurar gráfico
                        fig.update_layout(
                            title=f"Retrocesos de Fibonacci para {ticker} - Tendencia {trend_type}",
                            xaxis_title="Fecha",
                            yaxis_title="Precio",
                            height=600,
                            xaxis_rangeslider_visible=False,
                            hovermode='x unified',
                            legend=dict(
                                orientation="h",
                                yanchor="bottom",
                                y=1.02,
                                xanchor="right",
                                x=1
                            ),
                            plot_bgcolor='white',
                            xaxis=dict(showgrid=True, gridcolor='lightgray'),
                            yaxis=dict(showgrid=True, gridcolor='lightgray')
                        )
                        
                        # Opcional: mostrar volumen si está activado
                        if show_volume:
                            volume_data = list(data['Volume'])
                            colors = ['green' if close_values[i] > open_values[i] else 'red' 
                                    for i in range(len(close_values))]
                            
                            fig.add_trace(go.Bar(
                                x=dates,
                                y=volume_data,
                                name="Volumen",
                                marker_color=colors,
                                opacity=0.3,
                                yaxis="y2"
                            ))
                            
                            fig.update_layout(
                                yaxis2=dict(
                                    title="Volumen",
                                    overlaying="y",
                                    side="right",
                                    showgrid=False
                                )
                            )
                        
                        # Opcional: mostrar niveles de extensión si está activado
                        if extended_levels:
                            # Añadir niveles de extensión: 1.272 y 1.618
                            extension_levels = {}
                            diff = max_price_value - min_price_value
                            
                            if trend_type == "Alcista":
                                extension_levels[1.272] = min_price_value + 1.272 * diff
                                extension_levels[1.618] = min_price_value + 1.618 * diff
                            else:  # Bajista
                                extension_levels[1.272] = max_price_value - 1.272 * diff
                                extension_levels[1.618] = max_price_value - 1.618 * diff
                            
                            # Añadir las líneas de extensión
                            for ratio, price in extension_levels.items():
                                fig.add_hline(
                                    y=price,
                                    line_dash="dot",
                                    line_color="darkblue",
                                    annotation_text=f"Extensión {ratio:.3f}: ${price:.2f}",
                                    annotation_position="left"
                                )
                        
                        # Mostrar el gráfico
                        st.plotly_chart(fig, use_container_width=True)
                        
                        # Tabla de niveles de retroceso
                        st.subheader("Niveles de Retroceso de Fibonacci")
                        
                        # Crear listas para la tabla asegurando que los valores sean escalares
                        nivel_list = []
                        precio_list = []
                        
                        for ratio, price in levels.items():
                            # Convertir a float para asegurar formateo correcto
                            ratio_value = float(ratio) if isinstance(ratio, pd.Series) else float(ratio)
                            price_value = float(price) if isinstance(price, pd.Series) else float(price)
                            
                            nivel_list.append(f"{ratio_value*100:.1f}%")
                            precio_list.append(f"${price_value:.2f}")
                        
                        # Crear DataFrame con las listas ya formateadas
                        fib_table = pd.DataFrame({
                            "Nivel": nivel_list,
                            "Precio": precio_list
                        })
                        
                        st.table(fib_table)
                        
                        # Explicación de resultados
                        st.subheader("Interpretación de Resultados")
                        
                        # Convertir valores a escalares para evitar problemas de formateo
                        min_price_value = float(fib_data['min_price']) if isinstance(fib_data['min_price'], pd.Series) else float(fib_data['min_price'])
                        max_price_value = float(fib_data['max_price']) if isinstance(fib_data['max_price'], pd.Series) else float(fib_data['max_price'])
                        
                        # Formatear fechas correctamente
                        try:
                            if isinstance(fib_data['min_idx'], pd.Series):
                                min_idx_str = fib_data['min_idx'].iloc[0].strftime('%d/%m/%Y')
                            else:
                                min_idx_str = fib_data['min_idx'].strftime('%d/%m/%Y')
                                
                            if isinstance(fib_data['max_idx'], pd.Series):
                                max_idx_str = fib_data['max_idx'].iloc[0].strftime('%d/%m/%Y')
                            else:
                                max_idx_str = fib_data['max_idx'].strftime('%d/%m/%Y')
                        except Exception as e:
                            # Si hay un error al formatear fechas, usar formato alternativo
                            min_idx_str = str(fib_data['min_idx'])
                            max_idx_str = str(fib_data['max_idx'])
                            st.warning(f"Nota: Formato de fecha simplificado debido a: {str(e)}")
                        
                        st.markdown(f"""
                        ### Análisis para {ticker} - Tendencia {trend_type}
                        
                        En este análisis hemos identificado:
                        
                        - **Punto mínimo**: ${min_price_value:.2f} el {min_idx_str}
                        - **Punto máximo**: ${max_price_value:.2f} el {max_idx_str}
                        
                        #### ¿Cómo interpretar estos niveles?
                        
                        - Los niveles de retroceso de Fibonacci actúan como posibles zonas de soporte (en tendencia alcista) o resistencia (en tendencia bajista)
                        - El nivel 0.618 (61.8%) es especialmente significativo por su relación con la proporción áurea
                        - El nivel 0.5 (50%) tiene importancia psicológica en el mercado
                        - Observa cómo el precio interactúa con estos niveles para confirmar su validez
                        
                        #### Aplicación práctica:
                        
                        - En una **tendencia alcista**, los traders buscan oportunidades de compra en retrocesos hacia estos niveles
                        - En una **tendencia bajista**, los traders buscan oportunidades de venta en rebotes hacia estos niveles
                        - La confluencia con otros indicadores técnicos aumenta la relevancia de un nivel de Fibonacci
                        """)
            except Exception as e:
                st.error(f"Ha ocurrido un error inesperado: {str(e)}")
                st.write("Detalles para depuración:", e)

    # Sección de aplicaciones avanzadas
    with st.expander("🧠 Aplicaciones Avanzadas", expanded=False):
        st.markdown("""
        ### Estrategias Utilizando Retrocesos de Fibonacci
        
        1. **Estrategia de Continuación de Tendencia**:
           - Identificar una tendencia clara
           - Esperar un retroceso a los niveles de Fibonacci (especialmente 0.382, 0.5 o 0.618)
           - Entrar en la dirección de la tendencia original cuando el precio muestre señales de respeto al nivel
        
        2. **Estrategia de Confirmación con Velas Japonesas**:
           - Buscar patrones de velas específicos (como pinzas, martillos, estrellas del atardecer) en los niveles de Fibonacci
           - Estos patrones actúan como confirmación adicional para entradas
        
        3. **Estrategia de Confluencia**:
           - Combinar los niveles de Fibonacci con otros indicadores técnicos como:
             - Medias móviles
             - RSI (Índice de Fuerza Relativa)
             - Soportes/resistencias horizontales
             - Patrones chartistas
        
        4. **Colocación de Stop Loss y Take Profit**:
           - Stop Loss: Justo debajo/encima del nivel de Fibonacci que está siendo probado
           - Take Profit: En el siguiente nivel de extensión de Fibonacci (1.272, 1.618, etc.)
        
        ### Limitaciones a Considerar
        
        - Los retrocesos de Fibonacci funcionan mejor en mercados con tendencias claras
        - Son herramientas de probabilidad, no de certeza
        - Pueden generar falsos positivos, especialmente en mercados laterales
        - El sesgo de confirmación puede llevar a interpretar incorrectamente los resultados
        """)

    # Sección de ejercicios prácticos para estudiantes
    with st.expander("✏️ Ejercicios Prácticos", expanded=False):
        st.markdown("""
        ### Ejercicio 1: Identificación de Niveles
        
        1. Selecciona tres diferentes activos financieros
        2. Identifica una tendencia alcista clara en los últimos 6 meses
        3. Traza los niveles de retroceso de Fibonacci
        4. Responde:
           - ¿Qué nivel de Fibonacci respetó el precio con mayor frecuencia?
           - ¿Cuántos retrocesos completó el precio antes de continuar su tendencia?
        
        ### Ejercicio 2: Comparación de Efectividad
        
        1. Selecciona un activo financiero
        2. Analiza los retrocesos de Fibonacci en tres diferentes períodos de tiempo (1 mes, 6 meses, 1 año)
        3. Compara la efectividad de los niveles en cada período
        4. ¿En qué plazo temporal los niveles de Fibonacci parecen ser más efectivos?
        
        ### Ejercicio 3: Estrategia de Trading
        
        1. Diseña una estrategia de trading simple usando retrocesos de Fibonacci
        2. Define reglas claras para:
           - Entrada
           - Stop Loss
           - Take Profit
        3. Prueba tu estrategia en datos históricos (backtesting manual)
        4. Calcula la relación riesgo/beneficio y la tasa de éxito
        """)

elif selected_page == "Ejemplos en Naturaleza y Arte":
    # Si el módulo de ejemplos está disponible, lo usamos
    if ejemplos_module_available:
        ejemplos_fibonacci.app()
    else:
        # Función alternativa si el módulo no está disponible
        show_basic_examples()

# Información del autor
st.sidebar.header("Información")
st.sidebar.info("""
Esta herramienta didáctica fue diseñada para el aprendizaje de los retrocesos de Fibonacci en mercados financieros.

**Aplicación:**
- Experimenta con diferentes activos y períodos
- Compara resultados entre diferentes mercados
- Complementa tu análisis con otros indicadores técnicos
""")

# Enlaces útiles
st.sidebar.header("Recursos Adicionales")
st.sidebar.markdown("""
- [Teoría de Ondas de Elliott y Fibonacci](https://www.investopedia.com/articles/technical/111401.asp)
- [Patrones de velas japonesas](https://www.investopedia.com/trading/candlestick-charting-what-is-it/)
- [Estrategias de trading con Fibonacci](https://www.babypips.com/learn/forex/fibonacci-retracement)
""")

# Pie de página
st.markdown("""
---
Desarrollado con fines educativos | Ana Lorena Jiménez Preciado
""")