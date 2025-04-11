import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import io
from PIL import Image

def app():
    st.title("🌀 La Proporción Áurea y Fibonacci en la Naturaleza y Arte")
    
    st.markdown("""
    Esta página muestra ejemplos visuales de cómo la secuencia de Fibonacci y la proporción áurea 
    aparecen en la naturaleza, arte, arquitectura y otros contextos. Estos ejemplos ayudan a entender 
    por qué estas proporciones matemáticas tienen un significado tan profundo.
    """)
    
    # Sección 1: Espiral de Fibonacci en la naturaleza
    st.header("🐚 Espirales de Fibonacci en la Naturaleza")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Caracol Nautilus")
        
        # Crear imagen de espiral simulando Nautilus
        def create_nautilus_spiral():
            fig, ax = plt.subplots(figsize=(6, 6), facecolor='#F0F2F6')
            
            # Generar la espiral logarítmica (similar a Fibonacci)
            a = 0.17  # Tasa de crecimiento
            theta = np.linspace(0, 6*np.pi, 1000)
            r = a * np.exp(theta)
            
            # Coordenadas cartesianas
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            
            # Dibujando la espiral
            ax.plot(x, y, color='navy', linewidth=2)
            
            # Añadir líneas de referencia que marcan las cámaras del nautilus
            for i in range(0, 6):
                angle = i * np.pi/2
                line_x = [0, 0.7 * np.exp(angle) * np.cos(angle)]
                line_y = [0, 0.7 * np.exp(angle) * np.sin(angle)]
                ax.plot(line_x, line_y, 'r--', alpha=0.7)
            
            # Personalización
            ax.set_title('Espiral de Nautilus y Proporción Áurea', fontsize=12)
            ax.set_aspect('equal')
            ax.grid(True, alpha=0.3)
            ax.set_xlabel('La espiral del nautilus sigue aproximadamente la proporción áurea')
            ax.set_axis_off()
            
            # Guardar en memoria
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plt.close(fig)
            return buf
        
        nautilus_img = create_nautilus_spiral()
        st.image(nautilus_img, caption="La espiral del Nautilus sigue aproximadamente la proporción áurea")
        
        st.markdown("""
        La concha del Nautilus es uno de los ejemplos más conocidos de la espiral logarítmica en la naturaleza,
        que se aproxima a la espiral de Fibonacci. Cada nueva cámara sigue la proporción áurea con respecto
        a la anterior.
        """)
    
    with col2:
        st.subheader("Distribución de Semillas")
        
        # Crear imagen de distribución de semillas (patrón de girasol)
        def create_sunflower_pattern():
            fig, ax = plt.subplots(figsize=(6, 6), facecolor='#F0F2F6')
            
            # Usando el ángulo áureo (aproximadamente 137.5 grados)
            golden_angle = np.pi * (3 - np.sqrt(5))
            n = 600  # Número de semillas
            
            # Coordenadas polares
            theta = np.arange(n) * golden_angle
            r = np.sqrt(np.arange(n))
            
            # Convertir a coordenadas cartesianas
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            
            # Dibujar puntos (semillas)
            ax.scatter(x, y, s=20, c=theta, cmap='YlOrBr', alpha=0.8)
            
            # Personalización
            ax.set_title('Patrón de Semillas basado en Ángulo Áureo', fontsize=12)
            ax.set_aspect('equal')
            ax.set_axis_off()
            
            # Guardar en memoria
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plt.close(fig)
            return buf
        
        seeds_img = create_sunflower_pattern()
        st.image(seeds_img, caption="Distribución de semillas siguiendo el ángulo áureo (137.5°)")
        
        st.markdown("""
        En girasoles, piñas y muchas otras plantas, las semillas se distribuyen siguiendo el "ángulo áureo" 
        de aproximadamente 137.5 grados. Esta distribución optimiza el espacio y permite que cada semilla 
        reciba la máxima exposición solar y nutrientes.
        """)
    
    # Sección 2: Fibonacci en crecimiento de plantas
    st.header("🌱 Fibonacci en el Crecimiento de las Plantas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Filotaxis: Arreglo de Hojas")
        
        # Crear imagen de filotaxis (arreglo de hojas)
        def create_phyllotaxis():
            fig, ax = plt.subplots(figsize=(6, 6), facecolor='#F0F2F6')
            
            # Simulando un tallo con hojas en patrón de Fibonacci
            stem_height = 10
            golden_angle = 137.5  # En grados
            
            # Tallo
            ax.plot([0, 0], [0, stem_height], 'brown', linewidth=4)
            
            # Hojas
            n_leaves = 8
            leaf_sizes = np.linspace(2, 4, n_leaves)
            
            for i in range(n_leaves):
                angle = i * golden_angle
                height = i * stem_height / (n_leaves - 1)
                
                # Convertir ángulo a radianes para la rotación
                angle_rad = np.radians(angle)
                
                # Dibujar una hoja simple (elipse)
                leaf_x = np.cos(angle_rad) * leaf_sizes[i]
                leaf_y = height
                
                # Crear una elipse que simule una hoja
                ellipse = plt.matplotlib.patches.Ellipse(
                    (leaf_x, leaf_y), 
                    width=leaf_sizes[i], 
                    height=leaf_sizes[i]/2,
                    angle=angle-90,
                    facecolor='green',
                    alpha=0.7
                )
                ax.add_patch(ellipse)
                
                # Línea de tallo a hoja
                ax.plot([0, leaf_x], [height, leaf_y], 'green', linewidth=1)
            
            # Anotación
            ax.text(0, stem_height + 0.5, "Patrón cada 137.5°", 
                   ha='center', fontweight='bold')
            
            # Personalización
            ax.set_title('Filotaxis - Arreglo de Hojas', fontsize=12)
            ax.set_xlim(-5, 5)
            ax.set_ylim(-1, stem_height + 1)
            ax.set_aspect('equal')
            ax.set_axis_off()
            
            # Guardar en memoria
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plt.close(fig)
            return buf
        
        phyllotaxis_img = create_phyllotaxis()
        st.image(phyllotaxis_img, caption="Filotaxis: arreglo de hojas siguiendo ángulos basados en Fibonacci")
        
        st.markdown("""
        La filotaxis es el estudio de la disposición de hojas, ramificaciones y flores en las plantas.
        Muchas plantas arreglan sus hojas en espirales que siguen secuencias de Fibonacci (1/2, 1/3, 2/5, 3/8, 5/13)
        para maximizar la exposición solar y evitar que las hojas se superpongan.
        """)
    
    with col2:
        st.subheader("Ramificación de Árboles")
        
        # Crear imagen de patrón de ramificación usando recursividad
        def create_tree_branching():
            fig, ax = plt.subplots(figsize=(6, 6), facecolor='#F0F2F6')
            
            def draw_branch(x, y, length, angle, depth):
                if depth == 0:
                    return
                
                # Calcular el punto final de la rama
                x2 = x + length * np.cos(np.radians(angle))
                y2 = y + length * np.sin(np.radians(angle))
                
                # Dibujar la rama
                ax.plot([x, x2], [y, y2], 'brown', linewidth=depth/2)
                
                # Proporciones de Fibonacci para las siguientes ramas
                length_ratio = 0.618  # Proporción áurea inversa
                
                # Ramificar recursivamente
                draw_branch(x2, y2, length * length_ratio, angle - 30, depth - 1)
                draw_branch(x2, y2, length * length_ratio, angle + 30, depth - 1)
            
            # Iniciar con el tronco
            draw_branch(0, 0, 2, 90, 8)
            
            # Personalización
            ax.set_title('Patrón de Ramificación siguiendo Proporciones de Fibonacci', fontsize=12)
            ax.set_xlim(-3, 3)
            ax.set_ylim(0, 5)
            ax.set_aspect('equal')
            ax.set_axis_off()
            
            # Guardar en memoria
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plt.close(fig)
            return buf
        
        tree_img = create_tree_branching()
        st.image(tree_img, caption="Patrón de ramificación con proporciones basadas en Fibonacci")
        
        st.markdown("""
        Los árboles y plantas siguen patrones de ramificación que a menudo incorporan proporciones de Fibonacci.
        La proporción entre el grosor de las ramas y el tronco, así como la distribución de las ramas,
        frecuentemente siguen proporciones cercanas a la razón áurea (1.618) para equilibrar estructura y eficiencia.
        """)
    
    # Sección 3: Fibonacci en arte y arquitectura
    st.header("🏛️ La Proporción Áurea en Arte y Arquitectura")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Rectángulo Áureo")
        
        # Crear imagen de rectángulo áureo
        def create_golden_rectangle():
            fig, ax = plt.subplots(figsize=(8, 5), facecolor='#F0F2F6')
            
            # Dimensiones del rectángulo áureo
            width = 1.618
            height = 1
            
            # Dibujar rectángulo áureo
            rectangle = plt.Rectangle((0, 0), width, height, 
                                      fill=False, edgecolor='blue', linewidth=2)
            ax.add_patch(rectangle)
            
            # Dividirlo en un cuadrado y otro rectángulo áureo
            square = plt.Rectangle((0, 0), height, height, 
                                   fill=False, edgecolor='red', linewidth=2)
            ax.add_patch(square)
            
            # Rectángulo áureo más pequeño
            small_rect = plt.Rectangle((height, 0), width-height, height, 
                                      fill=False, edgecolor='green', linewidth=2)
            ax.add_patch(small_rect)
            
            # Anotaciones
            ax.annotate('1', (height/2, -0.1), ha='center')
            ax.annotate('1', (-0.1, height/2), va='center', rotation=90)
            ax.annotate('φ = 1.618', (width/2, -0.2), ha='center')
            ax.annotate('Cuadrado\n1×1', (height/2, height/2), ha='center', color='red')
            ax.annotate('Rectángulo Áureo\n0.618×1', (height+(width-height)/2, height/2), ha='center', color='green')
            
            # Espiral de Fibonacci (aproximada)
            theta = np.linspace(0, np.pi/2, 100)
            spiral_x = height - height * np.cos(theta)
            spiral_y = height * np.sin(theta)
            ax.plot(spiral_x, spiral_y, 'purple', linewidth=2)
            
            theta = np.linspace(0, np.pi/2, 100)
            radius = (width - height)
            spiral_x = height + radius * np.cos(theta + np.pi)
            spiral_y = height - radius * np.sin(theta + np.pi)
            ax.plot(spiral_x, spiral_y, 'purple', linewidth=2)
            
            # Personalización
            ax.set_title('Rectángulo Áureo y Espiral', fontsize=12)
            ax.set_xlim(-0.2, width + 0.2)
            ax.set_ylim(-0.3, height + 0.2)
            ax.set_aspect('equal')
            ax.axis('off')
            
            # Guardar en memoria
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plt.close(fig)
            return buf
        
        golden_rect_img = create_golden_rectangle()
        st.image(golden_rect_img, caption="Rectángulo Áureo y su descomposición")
        
        st.markdown("""
        El rectángulo áureo tiene una proporción de 1:1.618 (la proporción áurea) entre sus lados.
        Esta forma ha sido considerada estéticamente agradable durante siglos y aparece en:
        
        - El Partenón en Atenas
        - Las pinturas de Leonardo da Vinci
        - La arquitectura de Le Corbusier
        - Diseños modernos y logotipos (Apple, Twitter)
        
        Si se quita un cuadrado del rectángulo áureo, el rectángulo resultante también es áureo.
        Esto permite crear una espiral infinita.
        """)
    
    with col2:
        st.subheader("Composición en Arte")
        
        # Crear imagen de regla de tercios y proporción áurea en composición
        def create_composition_guide():
            fig, ax = plt.subplots(figsize=(8, 5), facecolor='#F0F2F6')
            
            # Lienzo
            canvas = plt.Rectangle((0, 0), 1, 1, fill=True, color='#f0f0f0', 
                                  edgecolor='black', linewidth=2)
            ax.add_patch(canvas)
            
            # Dibujar líneas de proporción áurea vertical
            ax.axvline(x=0.382, color='gold', linestyle='--', linewidth=1.5, alpha=0.8)
            ax.axvline(x=0.618, color='gold', linestyle='--', linewidth=1.5, alpha=0.8)
            
            # Dibujar líneas de proporción áurea horizontal
            ax.axhline(y=0.382, color='gold', linestyle='--', linewidth=1.5, alpha=0.8)
            ax.axhline(y=0.618, color='gold', linestyle='--', linewidth=1.5, alpha=0.8)
            
            # Dibujar regla de tercios (en gris)
            ax.axvline(x=0.333, color='gray', linestyle=':', linewidth=1, alpha=0.6)
            ax.axvline(x=0.667, color='gray', linestyle=':', linewidth=1, alpha=0.6)
            ax.axhline(y=0.333, color='gray', linestyle=':', linewidth=1, alpha=0.6)
            ax.axhline(y=0.667, color='gray', linestyle=':', linewidth=1, alpha=0.6)
            
            # Puntos de intersección importantes (proporción áurea)
            for x in [0.382, 0.618]:
                for y in [0.382, 0.618]:
                    ax.plot(x, y, 'o', color='gold', markersize=8)
            
            # Leyenda
            ax.text(0.05, 0.05, "Proporción Áurea (φ)", color='gold', fontweight='bold')
            ax.text(0.05, 0.10, "Regla de Tercios", color='gray')
            
            # Anotaciones
            ax.annotate("0.382", (0.382, -0.05), ha='center', color='gold')
            ax.annotate("0.618", (0.618, -0.05), ha='center', color='gold')
            
            # Personalización
            ax.set_title('Composición basada en Proporción Áurea vs. Regla de Tercios', fontsize=12)
            ax.set_xlim(-0.1, 1.1)
            ax.set_ylim(-0.1, 1.1)
            ax.set_aspect('equal')
            ax.axis('off')
            
            # Guardar en memoria
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plt.close(fig)
            return buf
        
        composition_img = create_composition_guide()
        st.image(composition_img, caption="Proporción Áurea vs. Regla de Tercios en composición artística")
        
        st.markdown("""
        La proporción áurea ha sido utilizada en la composición artística durante siglos:
        
        - Los puntos de intersección de las líneas áureas (38.2% y 61.8%) son considerados
          lugares óptimos para colocar elementos de interés
        - La regla de tercios es una simplificación de la proporción áurea
        - Muchas obras maestras de Leonardo da Vinci, Botticelli, y Salvador Dalí
          utilizan estas proporciones
        - La fotografía moderna sigue utilizando estos principios compositivos
        
        Los elementos clave en una composición bien balanceada a menudo se encuentran
        en estas líneas o en sus intersecciones.
        """)
    
    # Sección 4: Fibonacci en finanzas
    st.header("💹 Fibonacci en Mercados Financieros")
    
    # Crear gráfico de ejemplo de análisis técnico
    def create_technical_analysis():
        fig, ax = plt.subplots(figsize=(10, 6), facecolor='#F0F2F6')
        
        # Simulación simple de datos de precio
        np.random.seed(42)  # Para reproducibilidad
        días = 100
        precio_inicial = 100
        tendencia = 0.5
        volatilidad = 1.5
        
        # Generar movimiento alcista
        precios_alcista = np.zeros(int(días * 0.6))
        precios_alcista[0] = precio_inicial
        for i in range(1, len(precios_alcista)):
            precios_alcista[i] = precios_alcista[i-1] * (1 + np.random.normal(tendencia, volatilidad) / 100)
        
        # Generar retroceso
        precios_retroceso = np.zeros(int(días * 0.25))
        precio_maximo = precios_alcista[-1]
        retroceso_objetivo = precio_inicial + (precio_maximo - precio_inicial) * 0.618
        
        for i in range(len(precios_retroceso)):
            if i == 0:
                precios_retroceso[i] = precio_maximo
            else:
                distancia_al_objetivo = precios_retroceso[i-1] - retroceso_objetivo
                precios_retroceso[i] = precios_retroceso[i-1] - distancia_al_objetivo * 0.15 * (1 + np.random.normal(0, 0.5) / 100)
        
        # Generar continuación de tendencia
        precios_continuacion = np.zeros(int(días * 0.15))
        precio_retroceso = precios_retroceso[-1]
        
        for i in range(len(precios_continuacion)):
            if i == 0:
                precios_continuacion[i] = precio_retroceso
            else:
                precios_continuacion[i] = precios_continuacion[i-1] * (1 + np.random.normal(tendencia, volatilidad) / 100)
        
        # Unir todos los precios
        precios = np.concatenate([precios_alcista, precios_retroceso, precios_continuacion])
        dias_eje = np.arange(len(precios))
        
        # Graficar precios
        ax.plot(dias_eje, precios, 'b-')
        
        # Añadir niveles de Fibonacci
        min_price = precio_inicial
        max_price = precio_maximo
        diff = max_price - min_price
        
        # Calcular niveles de Fibonacci
        fib_levels = {
            0: min_price,
            0.236: min_price + diff * 0.236,
            0.382: min_price + diff * 0.382,
            0.5: min_price + diff * 0.5,
            0.618: min_price + diff * 0.618,
            0.786: min_price + diff * 0.786,
            1.0: max_price
        }
        
        # Dibujar niveles de Fibonacci
        colors = ['red', 'orange', 'gold', 'green', 'blue', 'purple', 'magenta']
        
        for i, (ratio, price) in enumerate(fib_levels.items()):
            ax.axhline(y=price, color=colors[i], linestyle='--', alpha=0.7,
                      label=f"Retroceso {ratio*100:.1f}%: ${price:.2f}")
        
        # Añadir anotaciones
        start_idx = 0
        high_idx = len(precios_alcista)
        retracement_idx = high_idx + len(precios_retroceso)
        
        ax.annotate("Tendencia Alcista", 
                   xy=(start_idx + high_idx//2, (precios_alcista[0] + precios_alcista[-1])/2),
                   xytext=(start_idx + high_idx//2, (precios_alcista[0] + precios_alcista[-1])/2 - diff*0.2),
                   arrowprops=dict(facecolor='green', shrink=0.05),
                   ha='center')
        
        ax.annotate("Retroceso", 
                   xy=(high_idx + len(precios_retroceso)//2, (precios_retroceso[0] + precios_retroceso[-1])/2),
                   xytext=(high_idx + len(precios_retroceso)//2, (precios_retroceso[0] + precios_retroceso[-1])/2 + diff*0.15),
                   arrowprops=dict(facecolor='red', shrink=0.05),
                   ha='center')
        
        ax.annotate("Continuación", 
                   xy=(retracement_idx + len(precios_continuacion)//2, (precios_continuacion[0] + precios_continuacion[-1])/2),
                   xytext=(retracement_idx + len(precios_continuacion)//2, (precios_continuacion[0] + precios_continuacion[-1])/2 - diff*0.15),
                   arrowprops=dict(facecolor='green', shrink=0.05),
                   ha='center')
        
        # Resaltar área de retroceso
        ax.axvspan(high_idx, retracement_idx, alpha=0.1, color='red')
        
        # Personalización
        ax.set_title('Retrocesos de Fibonacci en Análisis Técnico', fontsize=14)
        ax.set_xlabel('Días')
        ax.set_ylabel('Precio ($)')
        ax.grid(True, alpha=0.3)
        ax.legend(loc='upper left')
        
        # Guardar en memoria
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close(fig)
        return buf
    
    technical_img = create_technical_analysis()
    st.image(technical_img, caption="Aplicación de niveles de retroceso de Fibonacci en análisis técnico", use_column_width=True)
    
    st.markdown("""
    ### Relevancia en Análisis Técnico
    
    Los retrocesos de Fibonacci se utilizan en el análisis técnico porque:
    
    1. **Psicología de mercado**: Los traders y algoritmos prestan atención a estos niveles, creando una profecía autocumplida
    
    2. **Puntos de entrada óptimos**: Los niveles 38.2%, 50% y 61.8% a menudo proporcionan puntos de entrada con buena relación riesgo-recompensa
    
    3. **Validación histórica**: Estudios empíricos muestran que los precios tienden a respetar estos niveles con mayor frecuencia que puntos aleatorios
    
    4. **Aplicabilidad universal**: Funcionan en cualquier marco temporal y en cualquier mercado financiero (acciones, forex, criptomonedas)
    
    El nivel 61.8% (la proporción áurea inversa) es considerado por muchos traders como el nivel "perfecto" de retroceso antes de la continuación de una tendencia.
    """)
    
    # Sección 5: Aplicaciones adicionales
    st.header("🧬 Otras Aplicaciones Sorprendentes")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Proporciones Humanas")
        
        # Crear imagen de proporciones humanas
        def create_human_proportions():
            fig, ax = plt.subplots(figsize=(6, 8), facecolor='#F0F2F6')
            
            # Dibujar figura humana simplificada
            # Cabeza
            head = plt.Circle((0, 7), 0.5, fill=False)
            ax.add_patch(head)
            
            # Cuerpo
            ax.plot([0, 0], [6.5, 3], 'k-', linewidth=2)
            
            # Brazos
            ax.plot([-1.5, 0, 1.5], [5.5, 5.5, 5.5], 'k-', linewidth=2)
            
            # Piernas
            ax.plot([0, -0.75], [3, 0], 'k-', linewidth=2)
            ax.plot([0, 0.75], [3, 0], 'k-', linewidth=2)
            
            # Marcas de proporción áurea
            ax.axhline(y=4.33, color='gold', linestyle='--', alpha=0.7)  # Ombligo - división áurea
            ax.text(2, 4.33, "Proporción Áurea", color='gold')
            
            # Proporciones faciales
            # Simplificación de características faciales
            ax.plot([-0.2, 0.2], [7, 7], 'k-', linewidth=1)  # Ojos
            ax.plot([0, 0], [6.9, 6.7], 'k-', linewidth=1)  # Nariz
            ax.plot([-0.2, 0.2], [6.6, 6.6], 'k-', linewidth=1)  # Boca
            
            # Medidas y proporciones
            ax.annotate("", xy=(2, 0), xytext=(2, 7.5), arrowprops=dict(arrowstyle='<->'))
            ax.text(2.2, 3.75, "Altura total", va='center')
            
            ax.annotate("", xy=(-2, 4.33), xytext=(-2, 0), arrowprops=dict(arrowstyle='<->'))
            ax.text(-2.2, 2.16, "0.618 × Altura", va='center', rotation=90)
            
            ax.annotate("", xy=(-2, 7.5), xytext=(-2, 4.33), arrowprops=dict(arrowstyle='<->'))
            ax.text(-2.2, 5.9, "0.382 × Altura", va='center', rotation=90)
            
            # Personalización
            ax.set_title('Proporciones Áureas en el Cuerpo Humano', fontsize=12)
            ax.set_xlim(-3, 3)
            ax.set_ylim(-0.5, 8)
            ax.set_aspect('equal')
            ax.axis('off')
            
            # Guardar en memoria
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plt.close(fig)
            return buf
        
        human_img = create_human_proportions()
        st.image(human_img, caption="Proporciones áureas en el cuerpo humano")
        
        st.markdown("""
        El cuerpo humano exhibe múltiples ejemplos de la proporción áurea:
        
        - La relación entre la altura total y la distancia del ombligo al suelo es aproximadamente φ
        - La proporción entre las falanges de los dedos
        - Las proporciones faciales en rostros considerados atractivos
        - La relación entre el antebrazo y la mano
        
        Leonardo da Vinci exploró estas proporciones en su famoso dibujo del "Hombre de Vitruvio".
        """)
    
    with col2:
        st.subheader("Música y Armonía")
        
        # Crear imagen de proporciones musicales
        def create_music_proportions():
            fig, ax = plt.subplots(figsize=(6, 6), facecolor='#F0F2F6')
            
            # Crear un teclado de piano simplificado
            n_keys = 13  # Una octava (8 teclas blancas, 5 negras)
            white_key_width = 0.8
            black_key_width = 0.5
            black_key_height = 2
            white_key_height = 3
            
            # Dibujar teclas blancas
            for i in range(8):
                rect = plt.Rectangle((i*white_key_width, 0), white_key_width, white_key_height, 
                                    fill=True, color='white', edgecolor='black')
                ax.add_patch(rect)
            
            # Dibujar teclas negras
            black_positions = [0.5, 1.5, 3.5, 4.5, 5.5]
            for pos in black_positions:
                rect = plt.Rectangle((pos*white_key_width-black_key_width/2, white_key_height-black_key_height), 
                                    black_key_width, black_key_height, 
                                    fill=True, color='black')
                ax.add_patch(rect)
            
            # Notas
            notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
            for i, note in enumerate(notes):
                ax.text(i*white_key_width + white_key_width/2, 0.5, note, ha='center')
            
            # Frecuencias y proporciones
            freqs = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]
            
            # Mostrar relaciones de frecuencias
            ax.text(1, 4, "Proporciones entre frecuencias:", fontweight='bold')
            ax.text(1, 4.5, "Octava (C-C): 1:2")
            ax.text(1, 5, "Quinta (C-G): 2:3")
            ax.text(1, 5.5, "Cuarta (C-F): 3:4")
            ax.text(1, 6, "Tercera mayor (C-E): 4:5")
            
            # Destacar relación con Fibonacci
            ax.text(4, 4, "Conexión con Fibonacci:", fontweight='bold', color='purple')
            ax.text(4, 4.5, "Las proporciones 3:5 y 5:8\nson aproximaciones de la\nproporción áurea", color='purple')
            ax.text(4, 6, "Los acordes musicales que\nsiguen proporciones cercanas\na φ suenan armoniosos", color='purple')
            
            # Personalización
            ax.set_title('Proporción Áurea en Armonía Musical', fontsize=12)
            ax.set_xlim(-0.5, 8*white_key_width + 0.5)
            ax.set_ylim(0, 7)
            ax.set_aspect('equal')
            ax.axis('off')
            
            # Guardar en memoria
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plt.close(fig)
            return buf
        
        music_img = create_music_proportions()
        st.image(music_img, caption="Relación entre la proporción áurea y la armonía musical")
        
        st.markdown("""
        La proporción áurea aparece en la música de varias formas:
        
        - Las octavas en música siguen proporciones de frecuencia 1:2
        - La escala pentatónica se basa en proporciones relacionadas con Fibonacci
        - Muchos compositores como Mozart y Beethoven estructuraron sus obras
          usando proporciones cercanas a la proporción áurea
        - Las formas musicales clásicas a menudo siguen patrones donde el clímax
          ocurre aproximadamente al 61.8% de la pieza
        
        Estudios señalan que los sonidos cuyas frecuencias se relacionan en proporciones
        basadas en Fibonacci tienden a ser percibidos como agradables al oído humano.
        """)

    # Sección conclusiva
    st.header("🔄 Conexión Universal")
    st.markdown("""
    ### ¿Por qué aparece Fibonacci en tantos lugares?
    
    La omnipresencia de la proporción áurea y la secuencia de Fibonacci en la naturaleza, el arte, 
    y los mercados financieros no es coincidencia:
    
    - **Eficiencia natural**: Las proporciones de Fibonacci representan distribuciones óptimas 
      para muchos sistemas biológicos y físicos
    
    - **Percepción humana**: Nuestro cerebro está posiblemente "sintonizado" para reconocer 
      estas proporciones como armoniosas debido a su prevalencia en nuestro entorno natural
    
    - **Matemáticas universales**: La proporción áurea emerge naturalmente de sistemas que 
      buscan equilibrio entre crecimiento y estabilidad
    
    - **Psicología colectiva**: En mercados financieros, el reconocimiento compartido de 
      estos patrones crea una dinámica auto-reforzante
    
    Lo que hace especialmente fascinante a la proporción áurea es que parece conectar 
    ámbitos aparentemente no relacionados como la botánica, el arte, las matemáticas, 
    la psicología y las finanzas en un patrón coherente.
    """)

# Función para llamar desde la aplicación principal
if __name__ == "__main__":
    app()