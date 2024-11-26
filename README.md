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

