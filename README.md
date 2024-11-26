# Aseguramiento de la Calidad del Software

Este proyecto tiene como objetivo implementar prácticas y herramientas de calidad de software, siguiendo un enfoque sistemático para garantizar que cumple con los requisitos funcionales y no funcionales.

---

## **Parte 1: Aseguramiento de la Calidad del Software**

### **1.1 Sistemas de Control de Calidad**

#### **Objetivo**
Familiarizarse con las prácticas y herramientas utilizadas para garantizar la calidad a lo largo del ciclo de vida del software.

#### **Actividad: Implementación de un Sistema de Control de Calidad**
En esta actividad se configuró un pipeline de integración continua (CI/CD) utilizando **GitHub Actions**, con los siguientes pasos clave:
- Compilar el código y ejecutar pruebas automáticamente con cada commit.
- Realizar un análisis estático de código con **SonarCloud** para detectar errores y problemas de calidad.

#### **Pipeline Configurado**
El pipeline incluye:
1. Instalación de dependencias.
2. Ejecución de pruebas unitarias y generación de reportes.
3. Análisis estático de código.

![Pipeline](https://via.placeholder.com/800x400.png?text=Ejemplo+de+Pipeline)  
_Imagen ilustrativa del pipeline configurado._

#### **Flujo de Trabajo**
1. El pipeline se activa con cada `push` o solicitud de extracción (`pull request`) a la rama `main`.
2. Ejecuta automáticamente:
   - Las pruebas unitarias usando `pytest`.
   - El análisis estático con **SonarCloud**.

![GitHub Actions](https://via.placeholder.com/800x400.png?text=Resultados+de+GitHub+Actions)  
_Ejemplo de una ejecución exitosa del pipeline._

#### **Resultados**
- **Pruebas exitosas**: Todas las pruebas unitarias se ejecutan correctamente.
- **Cobertura**: Se genera un reporte de cobertura y calidad de código en **SonarCloud**.
- **Análisis estático**: SonarCloud detecta y reporta problemas de calidad en el código fuente.

---

### **1.2 Pruebas**

#### **Objetivo**
Realizar diferentes tipos de pruebas para garantizar que el software cumple con los requisitos funcionales y no funcionales.

#### **Actividad: Diseño y Ejecución de Pruebas**
Se diseñaron y ejecutaron un conjunto de pruebas unitarias utilizando el framework **pytest** para la función `calculate_rectangle_area`.

#### **Tareas Realizadas**
1. **Diseño de pruebas unitarias**:
   - Se cubrieron diferentes escenarios funcionales y de límites:
     - Valores válidos.
     - Dimensiones cero.
     - Dimensiones negativas.
     - Valores extremos.

2. **Ejecución de pruebas**:
   - Las pruebas se ejecutaron tanto localmente como en el pipeline de CI/CD.

3. **Pruebas de regresión**:
   - Se verificó que los cambios recientes no afectaran funcionalidades existentes.

#### **Código de las Pruebas**

Archivo `tests/test_module.py`:
```python
import pytest
from src.module import calculate_rectangle_area

def test_valid_rectangle_area():
    assert calculate_rectangle_area(5, 10) == 50

def test_zero_width():
    with pytest.raises(ValueError):
        calculate_rectangle_area(0, 10)

def test_zero_height():
    with pytest.raises(ValueError):
        calculate_rectangle_area(5, 0)

def test_negative_dimensions():
    with pytest.raises(ValueError):
        calculate_rectangle_area(-5, -10)

def test_large_values():
    assert calculate_rectangle_area(1_000_000, 2_000_000) == 2_000_000_000_000
