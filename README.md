# Aseguramiento de la Calidad del Software

Este proyecto tiene como objetivo implementar prácticas y herramientas para garantizar la calidad del software, utilizando técnicas como pruebas unitarias, integración continua y análisis estático de código.

---

## **Parte 1: Aseguramiento de la Calidad del Software**

### **1.1 Sistemas de Control de Calidad**

#### **Objetivo**
Familiarizarse con las prácticas y herramientas utilizadas para garantizar la calidad a lo largo del ciclo de vida del software.

#### **Actividad: Implementación de un Sistema de Control de Calidad**
En esta actividad, se configuró un pipeline de integración continua (CI/CD) utilizando **GitHub Actions** para automatizar tareas clave como:
- Compilar el código.
- Ejecutar pruebas unitarias.
- Realizar análisis estático de código con **SonarCloud**.

#### **Pipeline Configurado**
El pipeline realiza las siguientes tareas:
1. Instala dependencias.
2. Ejecuta pruebas unitarias con cobertura.
3. Ejecuta análisis estático de código con SonarCloud.

**Imágenes sugeridas**:
- Una captura del pipeline configurado en el archivo `build.yml` desde GitHub.
- Una captura del resultado de una ejecución exitosa del pipeline en la pestaña **Actions**.

#### **Flujo de Trabajo**
1. El pipeline se ejecuta automáticamente en los siguientes eventos:
   - Cada `push` a la rama principal (`main`).
   - Cada solicitud de extracción (`pull request`) hacia la rama principal.

2. Resultados generados:
   - Reportes de pruebas unitarias y cobertura.
   - Análisis estático enviado automáticamente a **SonarCloud**.

**Imágenes sugeridas**:
- Una captura de los resultados de **SonarCloud**, mostrando:
  - La cobertura alcanzada.
  - Los problemas detectados (si los hay).

---

### **1.2 Pruebas**

#### **Objetivo**
Realizar diferentes tipos de pruebas para garantizar que el software cumple con los requisitos funcionales y no funcionales.

#### **Actividad: Diseño y Ejecución de Pruebas**
Se diseñó y ejecutó un conjunto de pruebas unitarias utilizando el framework **pytest** para validar la función `calculate_rectangle_area`.

#### **Tareas Realizadas**
1. **Diseño de pruebas**:
   - Las pruebas cubrieron diferentes escenarios funcionales y límites:
     - Valores válidos.
     - Dimensiones cero.
     - Dimensiones negativas.
     - Valores extremos.

2. **Ejecución de pruebas**:
   - Las pruebas se ejecutaron tanto localmente como en el pipeline de CI/CD.

3. **Pruebas de regresión**:
   - Se verificó que los cambios recientes no afectaran funcionalidades ya implementadas.

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
