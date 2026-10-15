import numpy as np
import matplotlib.pyplot as plt

# Configuración general de estilo con fondo blanco e igualdad de dimensiones
plt.style.use('default')
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.patch.set_facecolor('white')

# -------------------------------------------------------------
# 1. Generación de datos sintéticos base (Curva senoidal con ruido)
# -------------------------------------------------------------
np.random.seed(42)
X = np.linspace(0, 1, 60)
y = np.sin(2 * np.pi * X) + np.random.normal(0, 0.15, len(X))

X_smooth = np.linspace(0, 1, 200)

# -------------------------------------------------------------
# Gráfico 1: Varianza Adecuada (Modelado equilibrado)
# -------------------------------------------------------------
axes[0, 0].scatter(X, y, color='gray', alpha=0.6, s=30)
poly3 = np.polyfit(X, y, 3)
y_poly3 = np.polyval(poly3, X_smooth)
axes[0, 0].plot(X_smooth, y_poly3, color='red', linewidth=2.5, label='Curva de ajuste adecuada')
axes[0, 0].set_title('Varianza Adecuada (Modelo Equilibrado)', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('x')
axes[0, 0].set_ylabel('y')
axes[0, 0].legend(loc='upper right')
axes[0, 0].grid(True, linestyle='--', alpha=0.3)
axes[0, 0].set_facecolor('white')

# -------------------------------------------------------------
# Gráfico 2: Varianza Alta (Sobreajuste - Sin la curva azul)
# -------------------------------------------------------------
axes[0, 1].scatter(X, y, color='gray', alpha=0.6, s=30)
# Se omite intencionalmente la curva de ajuste excesiva (azul) según los requerimientos
axes[0, 1].set_title('Varianza Alta (Sobreajuste - Sin curva)', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('x')
axes[0, 1].set_ylabel('y')
axes[0, 1].grid(True, linestyle='--', alpha=0.3)
axes[0, 1].set_facecolor('white')

# -------------------------------------------------------------
# Datos y modelos para el análisis de Sesgo (Tendencia cuadrática)
# -------------------------------------------------------------
X_b = np.linspace(0, 1, 40)
y_b = 3 * (X_b ** 2) + np.random.normal(0, 0.1, len(X_b))
X_b_smooth = np.linspace(0, 1, 100)

# -------------------------------------------------------------
# Gráfico 3: Sesgo Adecuado (Bajo sesgo / Ajuste polinómico de grado 2)
# -------------------------------------------------------------
axes[1, 0].scatter(X_b, y_b, color='gray', alpha=0.6, s=30)
poly_b2 = np.polyfit(X_b, y_b, 2)
y_b2 = np.polyval(poly_b2, X_b_smooth)
axes[1, 0].plot(X_b_smooth, y_b2, color='saddlebrown', linewidth=2.5, label='Curva de ajuste adecuada')
axes[1, 0].set_title('Sesgo Adecuado (Bajo sesgo)', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('x')
axes[1, 0].set_ylabel('y')
axes[1, 0].legend(loc='upper left')
axes[1, 0].grid(True, linestyle='--', alpha=0.3)
axes[1, 0].set_facecolor('white')

# -------------------------------------------------------------
# Gráfico 4: Sesgo Alto (Subajuste / Ajuste lineal)
# -------------------------------------------------------------
axes[1, 1].scatter(X_b, y_b, color='gray', alpha=0.6, s=30)
poly_b1 = np.polyfit(X_b, y_b, 1)
y_b1 = np.polyval(poly_b1, X_b_smooth)
axes[1, 1].plot(X_b_smooth, y_b1, color='purple', linewidth=2.5, label='Línea de ajuste lineal (Subajuste)')
axes[1, 1].set_title('Sesgo Alto (Subajuste)', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('x')
axes[1, 1].set_ylabel('y')
axes[1, 1].legend(loc='upper left')
axes[1, 1].grid(True, linestyle='--', alpha=0.3)
axes[1, 1].set_facecolor('white')

# Ajuste final de diseño y renderizado
plt.tight_layout()
plt.show()