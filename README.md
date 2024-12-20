# Sistema de CI/CD y Componentes de Código

Este sistema organiza el flujo de trabajo para la integración continua (CI) y el desarrollo continuo (CD), estructurado en tres componentes principales: el pipeline, el código fuente, y la configuración.

![Diagrama del Sistema de CI/CD y Componentes de Código](/images/g4.png)

---
---

## Descripción del Funcionamiento del Pipeline

Este proyecto utiliza un **pipeline de integración continua (CI)** configurado en **GitHub Actions** para ejecutar pruebas automáticas y analizar la calidad del código. A continuación, se explica el flujo completo:

---

### **1. GitHub Actions**
- **Qué hace:** 
  - Automatiza la ejecución de las pruebas y el análisis del código cada vez que haces un cambio (push) o abres/modificas un Pull Request.
- **Cómo lo hace:**
  - El archivo `build.yml` en la carpeta `.github/workflows` define los pasos que se ejecutan:
    1. **Descarga del código:** Clona el repositorio para acceder al código.
    2. **Instalación del entorno:** Configura Python y las dependencias necesarias desde `requirements.txt`.
    3. **Ejecución de pruebas:** Usa `pytest` para verificar que la lógica del código funcione correctamente.
    4. **Análisis estático:** Envía datos a **SonarCloud** para evaluar la calidad del código (como complejidad, errores y cobertura).

---

### **2. Lógica Principal (`module.py`)**
- **Qué hace:** 
  - Contiene la función principal `calculate_rectangle_area` que calcula el área de un rectángulo.
- **Cómo lo hace:**
  - Recibe dos valores (`width` y `height`) y realiza estas validaciones:
    1. Si alguno de los valores es menor o igual a 0, lanza un error (`ValueError`).
    2. Si los valores son válidos, devuelve el área como resultado de multiplicar ancho por altura.

---

### **3. Pruebas Unitarias (`test_module.py`)**
- **Qué hacen:** 
  - Verifican que la función principal (`calculate_rectangle_area`) funcione correctamente en diferentes escenarios.
- **Cómo lo hacen:**
  - Usan `pytest` para ejecutar pruebas con datos específicos. Ejemplos:
    1. Probar con valores válidos (ejemplo: `width=5`, `height=10`).
    2. Verificar que se lanza un error si los valores son negativos o iguales a cero.
    3. Comprobar el resultado con valores grandes o extremos.
    4. Verificar que se lanza un error si el ancho es cero.
    5. Verificar que se lanza un error si la altura es cero.

---

### **4. SonarCloud**
- **Qué hace:** 
  - Analiza el código para detectar posibles problemas de calidad, como:
    1. Errores potenciales.
    2. Complejidad del código.
    3. Cobertura de las pruebas (qué porcentaje del código está probado).
- **Cómo lo hace:**
  - El pipeline envía los resultados de las pruebas y la cobertura a SonarCloud usando las credenciales configuradas en `SONAR_TOKEN`.

---

### **Flujo Completo**
1. Haces un cambio (push) o creas un Pull Request en GitHub.
2. GitHub Actions ejecuta el pipeline:
   - Instala dependencias.
   - Corre las pruebas unitarias con `pytest`.
   - Analiza el código con SonarCloud.
3. Si todo pasa, verás un ✅ verde en "Actions". Si algo falla, verás un ❌ rojo con detalles del error.

---
# Tutorial: Cómo Implementar el Sistema de CI/CD y Configuración del Proyecto
Este tutorial te guiará en la creación de un sistema de integración y entrega continua (CI/CD), pruebas unitarias, análisis estático de código y herramientas de control de configuración para gestionar artefactos del software.

## 1.1 Sistemas de Control de Calidad
**Descripción:** Configurar un pipeline de CI/CD para compilar, ejecutar pruebas y realizar análisis estático de código con herramientas como GitHub Actions y SonarQube.

**Resultado esperado:** Pipeline automatizado que valide la calidad del software en cada commit.

---

## 1.2 Pruebas
**Descripción:** Diseñar y ejecutar pruebas unitarias con frameworks como pytest para verificar funcionalidad, límites y regresión.

**Resultado esperado:** Conjunto de pruebas ejecutadas con resultados documentados.

---

## 1.3 Control de Configuración
**Descripción:** Implementar un flujo de trabajo con Git que incluya ramas, pull requests y revisiones de código para gestionar cambios y versiones.

**Resultado esperado:** Repositorio organizado con control de versiones y flujo de trabajo colaborativo.

---
---
---
---
---
---
# Parte 1.1: Configuración del Repositorio y GitHub Actions

## Paso 1: Crear el repositorio en GitHub

### Accede a GitHub:
- Inicia sesión en tu cuenta en GitHub.

### Crea un nuevo repositorio:
1. Haz clic en el botón verde `New` (ubicado en la esquina superior derecha de tu página principal).
2. Llena los campos necesarios:
   - **Nombre del repositorio**: Por ejemplo, `quality-assurance-project`.
   - **Descripción**: Opcional, pero puedes escribir algo como "Repositorio para práctica de aseguramiento de calidad de software".
   - **Visibilidad**: Elige entre público o privado.
3. Marca la casilla de `Add a README file` para inicializar el repositorio con un archivo `README.md`.

### Crea el repositorio:
- Haz clic en el botón `Create repository`. Esto generará tu repositorio en GitHub.

---

## Paso 2: Configuración de GitHub Actions

### Accede a la pestaña `Actions`:
- En tu repositorio, localiza la pestaña `Actions` en la barra superior (junto a `Code` y `Issues`).

### Crear un workflow:
1. GitHub te sugerirá plantillas predefinidas para diferentes lenguajes y entornos. En nuestro caso:
   - Haz clic en `Set up a workflow yourself`.
   - Esto creará un archivo con el nombre predeterminado `main.yml`.

### Ubicación del archivo del workflow:
- El archivo creado estará en una carpeta llamada `.github/workflows/` dentro de tu repositorio. Si esta carpeta no existe, GitHub la creará automáticamente cuando guardes el archivo.

### Renombrar y configurar tu workflow:
1. Cambia el nombre del archivo a algo más descriptivo, como `ci-sonar.yml`. Para hacerlo:
   - Haz clic en el icono del lápiz (editar) y edita el nombre en la parte superior.
2. Reemplaza el contenido inicial del archivo con el siguiente código base:

```yaml
name: Build, Test, and Analyze

on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  build-and-analyze:
    name: Run Tests and SonarCloud Analysis
    runs-on: ubuntu-latest

    steps:
      # Paso 1: Checkout del repositorio
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Clonar todo el historial para análisis preciso

      # Paso 2: Configuración de Python
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.9"

      # Paso 3: Instalar dependencias
      - name: Install dependencies
        run: pip install -r requirements.txt

      # Paso 4: Ejecutar pruebas unitarias
      - name: Run unit tests
        run: |
          export PYTHONPATH=$PYTHONPATH:$(pwd)/src
          pytest --junitxml=test-results.xml --cov=src --cov-report=xml

      # Paso 5: Ejecutar análisis estático en SonarCloud
      - name: SonarCloud Analysis
        uses: SonarSource/sonarcloud-github-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}  # Token para acceder a datos del repo (PRs, commits)
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}    # Token generado desde SonarCloud



```
### Guardar el workflow:

1. Una vez configurado, haz clic en el botón verde `Start Commit` (ubicado en la parte superior derecha).
2. Selecciona `Commit directly to the main branch`.
3. Haz clic en `Commit new file` para guardar los cambios.

---

### Paso 3: Validar la configuración

#### Verifica que el archivo se haya creado correctamente:
1. Ve a la sección `Code` en tu repositorio.
2. Asegúrate de que exista la carpeta `.github/workflows` y que contenga el archivo `ci-sonar.yml`.

#### Prueba inicial del pipeline:
1. Realiza un commit o un push de cualquier archivo en la rama `main` para activar el workflow.
2. Accede a la pestaña `Actions` en tu repositorio.
3. Verifica que el workflow se ejecute automáticamente y revisa los resultados de la ejecución.
![Act](/images/g10.png)

---

### Paso 4: Configuración de SonarCloud

1. Ve a [SonarCloud](https://sonarcloud.io) y accede a tu cuenta. Si no tienes una, regístrate con tu cuenta de GitHub.
2. En el tablero de SonarCloud, haz clic en el botón `+` (ubicado en la esquina superior derecha) y selecciona `Analyze new project`.
3. Autoriza a SonarCloud a acceder a tus repositorios de GitHub.
4. Selecciona el repositorio que deseas analizar y haz clic en `Set Up`.

---

#### 4.2 Generar un token para el análisis:
1. Durante la configuración, SonarCloud te pedirá que generes un token de acceso:
   - Asigna un nombre descriptivo al token, por ejemplo, `SonarToken`.
   - Haz clic en `Generate` y copia el token generado (guárdalo en un lugar seguro, ya que no podrás verlo nuevamente).

---

#### 4.3 Configurar el token en GitHub:
1. Ve a tu repositorio en GitHub y accede a la pestaña `Settings`.
2. Navega a `Secrets and variables > Actions` y haz clic en `New repository secret`.
3. Añade un nuevo secreto con los siguientes detalles:
   - **Nombre:** `SONAR_TOKEN`
   - **Valor:** Pega aquí el token generado en SonarCloud.
4. Haz clic en `Add secret` para guardar.

---

#### 4.4 Configurar el archivo `sonar-project.properties`:
1. Crea un archivo llamado `sonar-project.properties` en la raíz de tu repositorio.
2. Añade el siguiente contenido, ajustando los valores según tu proyecto:

```properties
# Configuración básica de SonarCloud
sonar.projectKey=your_project_key
sonar.organization=your_organization
sonar.host.url=https://sonarcloud.io

# Opcional: Nombre y versión del proyecto
sonar.projectName=name_proyect
sonar.projectVersion=1.0

# Configuración de rutas
sonar.sources=.
sonar.tests=tests
sonar.test.inclusions=**/tests/**

# Codificación del proyecto
sonar.sourceEncoding=UTF-8


```

---

### 4.5 Validar la integración:
1. Realiza un commit del archivo `sonar-project.properties`:
   ```bash
   git add sonar-project.properties
   git commit -m "Add SonarCloud configuration"
   git push origin main


### Verifica que el workflow de GitHub Actions se ejecute correctamente:

1. Ve a la pestaña `Actions` en tu repositorio de GitHub.
2. Asegúrate de que el workflow complete todos los pasos sin errores:
   - Comprueba los logs de cada paso (instalación, pruebas, análisis estático).
   - Resuelve cualquier error que pueda aparecer.

3. Accede a tu proyecto en [SonarCloud](https://sonarcloud.io).
4. Revisa los resultados del análisis en el tablero:
   - **Cobertura de código**: Verifica el porcentaje de líneas de código cubiertas por las pruebas.
   - **Errores**: Identifica problemas de compilación o configuración en el análisis.
   - **Vulnerabilidades**: Examina posibles riesgos de seguridad en tu código.
  
---

## Parte 1.2: Diseño y Ejecución de Pruebas

### Objetivo
Realizar pruebas unitarias para garantizar que el software cumple con los requisitos funcionales y no funcionales.

---

### Paso 1: Crear la estructura del proyecto

1. **Carpeta `src`**:
   - Dentro de esta carpeta, crea un archivo llamado `module.py`.
   - Este archivo contendrá las funciones principales del proyecto.
   - Ejemplo de contenido en `module.py`:
     ```python
     def calculate_rectangle_area(width, height):
         """
         Calcula el área de un rectángulo.

         :param width: Ancho del rectángulo (debe ser positivo)
         :param height: Altura del rectángulo (debe ser positivo)
         :return: Área del rectángulo
         """
         if width <= 0 or height <= 0:
             raise ValueError("El ancho y la altura deben ser positivos.")
         return width * height
     ```

   

3. **Carpeta `tests`**:
   - Dentro de esta carpeta, crea un archivo llamado `test_module.py`.
   - Este archivo contendrá las pruebas unitarias para las funciones implementadas en `module.py`.
   - Ejemplo de contenido en `calculate_rectangle_area`:
     ```python
     import pytest
     from src.module import calculate_rectangle_area

     def test_valid_rectangle_area():
         """Prueba con valores válidos de ancho y altura."""
         assert calculate_rectangle_area(5, 10) == 50

     def test_zero_width():
         """Prueba cuando el ancho es cero."""
         with pytest.raises(ValueError):
             calculate_rectangle_area(0, 10)

     def test_zero_height():
         """Prueba cuando la altura es cero."""
         with pytest.raises(ValueError):
             calculate_rectangle_area(5, 0)

     def test_negative_dimensions():
         """Prueba con dimensiones negativas."""
         with pytest.raises(ValueError):
             calculate_rectangle_area(-5, -10)

     def test_large_values():
         """Prueba con valores grandes."""
         assert calculate_rectangle_area(1_000_000, 2_000_000) == 2_000_000_000_000
     ```

4. **Archivo `requirements.txt`**:
   - Este archivo debe estar en la raíz del proyecto.
   - Contendrá las dependencias necesarias para el proyecto.
   - Ejemplo de contenido para `requirements.txt`:
     ```
     pytest
     pytest-cov
     ```
### Verificar que todo esté bien

1. **Revisión en GitHub Actions:**
   - Ve a la pestaña `Actions` en tu repositorio.
   - Asegúrate de que el workflow se haya ejecutado correctamente tras el último commit o pull request.
   - Revisa los logs del pipeline para confirmar que las pruebas se ejecutaron sin errores y que la cobertura se reportó correctamente.

2. **Revisión en SonarCloud:**
   - Accede a tu proyecto en [SonarCloud](https://sonarcloud.io).
   - Verifica las métricas del análisis estático, como:
     - **Cobertura de código**: Revisa el porcentaje de líneas cubiertas por pruebas.
     - **Errores y vulnerabilidades**: Asegúrate de que no se detecten problemas críticos en el código.

3. **Confirmación final:**
   - Si todo está correcto en GitHub Actions y SonarCloud, considera este proceso exitoso.
   - Realiza ajustes en el código y repite las pruebas si encuentras errores o áreas de mejora.

---
## Parte 1.3: Control de Configuración

### Objetivo
Aplicar un flujo de control de versiones utilizando **Git** y **GitHub** para gestionar cambios en el software de manera organizada y eficiente.

---

### Paso 1: Crear ramas para nuevas características

1. Utiliza **Git** para crear ramas independientes para cada nueva funcionalidad.
2. Ejemplos de ramas creadas:
   - `feature/add-error-handling`: Para agregar manejo de errores.
   - `feature/improve-coverage`: Para mejorar la cobertura de pruebas.

### Paso 2: Modificar el código y añadir pruebas

1. Realiza los cambios necesarios en el archivo `module.py` para implementar la funcionalidad en la rama correspondiente.
2. Añade o modifica pruebas unitarias en el archivo `test_module.py` para cubrir los nuevos cambios.
3. Verifica que los cambios funcionan correctamente ejecutando las pruebas con el siguiente comando:
   ```bash
   pytest --cov=src

### Paso 3: Crear un Pull Request (PR)

1. Una vez que hayas terminado los cambios en la rama, ve a tu repositorio en GitHub.
2. En la página principal del repositorio, verás un aviso para comparar y crear un Pull Request si has subido una nueva rama.
3. Haz clic en `Compare & pull request`.
4. En la página de creación del Pull Request:
   - Asegúrate de que la rama base sea `main` y que la rama de comparación sea la que contiene tus cambios.
   - Escribe un título descriptivo para el Pull Request.
   - Agrega una descripción detallada explicando los cambios realizados y su propósito.
5. Haz clic en `Create pull request`.

---
# Parte 2 Avtividades Complementarias

---
Descripción: Usa herramientas como SonarQube o Jacoco para obtener métricas de
calidad sobre el código, como la cobertura de código, complejidad ciclomática, y la
densidad de defectos.

Tareas:
- Ejecuta SonarQube sobre tu código y obtén métricas de calidad.
- Analiza las métricas obtenidas y discútelas con el equipo para identificar áreas de
mejora.
- Realiza refactorizaciones en el código basadas en los resultados obtenidos.
## Resultados
Overview con issues
![Overview](/images/g5.PNG)
Coverage
![Coverage](/images/g6.PNG)
Duplicatons
![Duplications](/images/g7.PNG)
  
Los resultados fueron perfectos sin ningun error a corregir por el momento.

---
---
---
## 2.2 Control de Riesgos

### Objetivo
Identificar, evaluar y mitigar los riesgos asociados al desarrollo de software.

### Actividad: Gestión de Riesgos en el Proyecto
#### Descripción
Se realizó un análisis de riesgos para este proyecto, considerando posibles problemas que puedan surgir durante su desarrollo, como cambios en los requisitos, problemas técnicos o fallos en la configuración del pipeline de integración continua (CI/CD).

#### Tareas Realizadas
1. Identificación de riesgos relacionados con el desarrollo y la calidad del software.
2. Evaluación de la probabilidad e impacto de cada riesgo utilizando una matriz de riesgos.
3. Desarrollo de planes de mitigación para los riesgos más críticos.

#### Resultados Esperados
Un documento que describa:
- Los riesgos identificados.
- Su evaluación (probabilidad e impacto).
- Los planes de mitigación.

---

### **Análisis de Riesgos**

#### **Riesgos Identificados**
| **ID** | **Riesgo**                                                                     | **Probabilidad** | **Impacto** | **Categoría**          | **Nivel de Riesgo** |
|--------|--------------------------------------------------------------------------------|------------------|-------------|------------------------|---------------------|
| R1     | Configuración incorrecta de GitHub Actions que impida ejecutar el pipeline.   | Media            | Alta        | CI/CD                 | Alta                |
| R2     | Dependencias faltantes o mal definidas en `requirements.txt`.                  | Baja             | Alta        | Técnico               |Media               |
| R3     | Errores en los tests unitarios debido a cambios en el código base.             | Alta             | Media       | Pruebas               |Alta                |
| R4     | Baja cobertura de pruebas en funcionalidades críticas.                         | Media            | Alta        | Calidad               | Alta                |
| R5     | Dificultades en la integración con SonarCloud por problemas de configuración. | Media            | Media       | Tecnológico           | Media               |

---

### **Planes de Mitigación**

| **Riesgo**               | **Plan de Mitigación**                                                                                          |
|--------------------------|-----------------------------------------------------------------------------------------------------------------|
| R1: Configuración CI/CD  | Validar la configuración del archivo `build.yml` y realizar pruebas locales antes de subir los cambios al repo. |
| R2: Dependencias         | Verificar y actualizar regularmente el archivo `requirements.txt`.                                              |
| R3: Errores en tests     | Implementar pruebas de regresión para detectar errores antes de fusionar cambios.                              |
| R4: Baja cobertura       | Aumentar la cobertura con pruebas adicionales, especialmente para escenarios extremos y casos límite.           |
| R5: Problemas SonarCloud | Revisar la configuración del archivo `sonar-project.properties` y validar la conexión con el servicio.          |

---
---
---
---
---
# 2.3 Revisión
Objetivo: Realizar revisiones de código para mejorar la calidad y detectar errores
tempranamente.

---
## Descripción: Realiza una revisión de código entre dos miembros del equipo para
asegurar que el código sea de alta calidad.
###Tareas:
- Revisa el código de otro miembro del equipo en busca de errores, malas prácticas,
o problemas de diseño.
-Usa herramientas de revisión de código como GitHub Pull Requests o GitLab Merge
Requests para facilitar la revisión.
- Discute las observaciones y propón soluciones de mejora.

---
# Codigo a revisar : 
 ```python
    ################################################################################
# Nombre del Archivo: main.py
# Autor:             Equipo Dinamita
# Fecha:             14/11/2023
# Institución:       Tecnológico Nacional de México (TECNM) - Campus ITT
# Curso:             Sistemas Programables 
#
# Objetivo:
# Crear, programar y desiñar un gps usando raspberry en wokwi
#
# Historial de Revisiones:
# 14/11/2023        Equipo Dinamita - Creado
#
# Enlace a GitHub Repository ó GIST:
# https://github.com/Capi2023/3.0_GPS
#
# Enlace a Wokwi :
# https://wokwi.com/projects/381411706635128833
#
# Licencia:
# Este programa es software libre y puede ser redistribuido y/o modificado bajo los términos de la Licencia Pública General GNU
# como está publicado por la Free Software Foundation, ya sea la versión 3 de la Licencia, o (a tu elección) cualquier versión posterior.
#
# Este programa se distribuye con la esperanza de que sea útil, pero SIN GARANTÍA ALGUNA; incluso sin la garantía implícita de
# COMERCIALIZACIÓN o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la Licencia Pública General GNU para obtener más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.
#
################################################################################
# Importación de módulos necesarios
# from machine import Pin, I2C
# from ssd1306 import SSD1306_I2C
# import framebuf, sys
# import utime
# import random
# from machine import UART

# Definición de funciones
# def init_i2c
# def display_speed
# def get_direction
# def convert_coordinates
#

# Código principal


from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf, sys
import utime
import random
from machine import UART


pix_res_x = 128
pix_res_y = 64


# Initialize GPS module

def init_i2c(scl_pin, sda_pin):
    # Initialize I2C device
    i2c_dev = I2C(1, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=200000)
    i2c_addr = [hex(ii) for ii in i2c_dev.scan()]
    
    if not i2c_addr:
        print('No I2C Display Found')
        sys.exit()
    else:
        print("I2C Address      : {}".format(i2c_addr[0]))
        print("I2C Configuration: {}".format(i2c_dev))
    
    return i2c_dev

##se inicializa el oled
i2c_dev = init_i2c(scl_pin=27, sda_pin=26)

oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev)

plain_bytes = [
 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x03, 0xff, 0xfe, 0x01, 0xff, 0xfc, 
0x78, 0xff, 0xfc, 0xfc, 0xff, 0xf8, 0xfc, 0x7f, 0xf8, 0xfc, 0x7f, 0xf8, 0xfc, 0x7f, 0xfc, 0x78, 
0x7f, 0xfc, 0x30, 0xff, 0xfc, 0x01, 0xff, 0xf8, 0x00, 0xff, 0xf3, 0x01, 0x7f, 0xf3, 0x06, 0x3f, 
0xf6, 0x87, 0x9f, 0xee, 0xc7, 0x5f, 0xe7, 0xfe, 0x8f, 0xec, 0xff, 0xf7, 0xc0, 0x00, 0x03, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
]
# Crea un objeto framebuf para la pantalla OLED
fb = framebuf.FrameBuffer(bytearray(plain_bytes), 24, 24, framebuf.MONO_HLSB)


##limpia la pantalla
oled.fill(0)

oled.show()
oled.fill(0)
   
##se muestra un texto en pantalla
oled.text("Iniciando", 5, 5)
oled.fill(0)
oled.show()


##------------------------------------------------------------------------------
# Función para mostrar la barra de velocidad en la pantalla OLED
def display_speed(speed, lat, lon, sat, direction, time):
    ##se carga el logo en pantalla
    oled.fill(0)
    oled.blit(fb, 0, 0)

    oled.text("{}".format(sat), 0, 28)


    ind = ">"
    if speed > 0.5 and speed < 0.7:
        ind = ">>"
    elif speed > 0.7:
        ind = ">>>"

    altura_barra = 20
    oled.text("{}{}".format(round(speed/100, 3), ind),32,0)

    oled.text("{}".format(lat[:5]), 0,45)
    oled.text("{}".format(lon[:5]), 0,56)

    oled.text("{}".format(time), 85,56)

    oled.text("{}".format(direction), 110,0)

    oled.text("SPEED", 32, 10)
    oled.text("km/h", 63, 38)
    max_speed = 10.0  # Velocidad máxima en m/s (ajusta según tus necesidades)
    bar_width = int(speed / max_speed * 120)
    oled.rect(32, altura_barra, 64, 16, 1)
    oled.fill_rect(32, altura_barra, bar_width, 16, 1)
    oled.show()

def get_direction(latitude, longitude):
    if latitude >= 0:
        lat_direction = 'N'
    else:
        lat_direction = 'S'
    
    if longitude >= 0:
        lon_direction = 'E'
    else:
        lon_direction = 'S'

    return lat_direction + lon_direction

def convert_coordinates(sections):
    if sections[0] == 0:
        return None

    data = sections[0] + (sections[1] / 60.0)

    if sections[2] == 'S':
        data = -data
    if sections[2] == 'W':
        data = -data

    data = '{0:.6f}'.format(data)
    return str(data)


while True:

    # Simula los datos del GPS Neo-6M
    latitude_simulated = random.uniform(40.0, 41.0)
    longitude_simulated = random.uniform(-74.0, -73.0)
    
    latitude_simulated = round(latitude_simulated,2)
    longitude_simulated = round(longitude_simulated,2)

    current_time = "11:24"
    satellites_connected = random.randint(4, 12)  # Cantidad de satélites conectados
    direction = get_direction(latitude_simulated, longitude_simulated)  # Dirección
    speed_kph = random.uniform(0, 0.05)  # Velocidad en km/h

    latitude_sections = [int(latitude_simulated), (latitude_simulated - int(latitude_simulated)) * 60, 'N']
    longitude_sections = [int(longitude_simulated), (longitude_simulated - int(longitude_simulated)) * 60, 'W']

    latitude = convert_coordinates(latitude_sections)
    longitude = convert_coordinates(longitude_sections)

    if latitude is None or longitude is None or current_time is None:
        continue

    print('Latitud: ' + latitude)
    print('Longitud: ' + longitude)
    print('Satelites conectados:', satellites_connected)
    print('Punto cardinal:', direction)
    print('Velocidad (km/h):', speed_kph)
    print('Hora:', current_time)


    speed = random.uniform(0.01, 0.9)

    display_speed(speed, latitude, longitude, satellites_connected, direction, current_time)


```
---


## Correcciones Realizadas

### 1. Manejo de Error al No Encontrar el Dispositivo I2C
- **Problema**: Si no se encuentra un dispositivo I2C, el programa termina abruptamente con `sys.exit()`. Esto no proporciona suficiente información al usuario y no es un manejo adecuado del error.
- **Solución**: Se reemplazó `sys.exit()` con una excepción más descriptiva (`RuntimeError`).

**Antes**:
```python
if not i2c_addr:
    print('No I2C Display Found')
    sys.exit()
```

**Después**:
```python
if not i2c_addr:
    raise RuntimeError("No se encontró ningún dispositivo I2C.")
```

---

### 2. Error en las Direcciones Cardinales
- **Problema**: Las direcciones cardinales (`W` y `S`) estaban intercambiadas al determinar la dirección para la longitud.
- **Solución**: Se corrigió el intercambio para asignar correctamente `W` y `E`.

**Antes**:
```python
if longitude >= 0:
    lon_direction = 'E'
else:
    lon_direction = 'S'  # Esto debería ser 'W'
```

**Después**:
```python
if longitude >= 0:
    lon_direction = 'E'
else:
    lon_direction = 'W'
```

---

### 3. Simulación de Velocidad Irrealmente Baja
- **Problema**: Las velocidades simuladas estaban en un rango extremadamente bajo (`0.05 km/h`), lo cual no tiene sentido práctico.
- **Solución**: Se ajustó el rango de simulación para reflejar valores más realistas.

**Antes**:
```python
speed_kph = random.uniform(0, 0.05)
```

**Después**:
```python
speed_kph = random.uniform(0, 100)  # Ajuste a un rango realista en km/h
```

---

### 4. Falta de Pausa en el Bucle Principal
- **Problema**: El bucle `while True` se ejecuta continuamente sin descanso, lo que puede sobrecargar la CPU.
- **Solución**: Se añadió una pausa de 1 segundo para optimizar el uso de recursos.

**Antes**:
```python
while True:
    # Simulaciones y operaciones
```

**Después**:
```python
while True:
    # Simulaciones y operaciones
    utime.sleep(1)  # Pausa de 1 segundo
```
---
# Se uso la herramientaa de revisión de código GitHub Pull Requests
![image](/images/g8.png)

