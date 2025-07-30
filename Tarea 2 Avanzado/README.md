# Sistema de Análisis de Libros con Programación Orientada a Objetos

Este proyecto implementa un sistema modular para analizar datos de libros utilizando principios de Programación Orientada a Objetos, incluyendo herencia, polimorfismo y encapsulación.

## Estructura del Proyecto

### 1. BookDataManager
Clase responsable de la gestión de datos que:
- Carga datos desde una URL CSV
- Limpia nombres de columnas
- Proporciona métodos de filtrado por género y autor
- Encapsula toda la lógica de manejo de datos

### 2. BaseAnalyzer (Clase Abstracta)
Clase base abstracta que define la interfaz común para todos los analizadores:
- Constructor que recibe una instancia de `BookDataManager`
- Método abstracto `analyze()` que debe ser implementado por las clases hijas
- Método `display_results()` para mostrar resultados de forma clara

### 3. Clases que Heredan de BaseAnalyzer

#### GeneralAnalyzer(BaseAnalyzer)
- **Propósito**: Análisis general del dataset completo
- **Funcionalidad**: Proporciona estadísticas resumidas de todos los libros
- **Métricas incluidas**:
  - Total de libros
  - Rating promedio
  - Precio promedio
  - Total de reseñas
  - Distribución de géneros
  - Rango de años
  - Libros altamente calificados
  - Libros caros

#### GenreAnalyzer(BaseAnalyzer)
- **Propósito**: Análisis específico por género
- **Constructor**: `GenreAnalyzer(data_manager, genre)`
- **Funcionalidad**: Análisis detallado de un género específico
- **Métricas incluidas**:
  - Estadísticas del género seleccionado
  - Libros populares (>20,000 reseñas)
  - Libros altamente calificados
  - Rango de precios
  - Rango de años

#### AuthorAnalyzer(BaseAnalyzer)
- **Propósito**: Análisis específico por autor
- **Constructor**: `AuthorAnalyzer(data_manager, author_name)`
- **Funcionalidad**: Análisis detallado de un autor específico
- **Métricas incluidas**:
  - Estadísticas del autor
  - Mejor libro calificado
  - Libro más reseñado
  - Géneros escritos
  - Rango de años
  - Lista completa de libros

## Características Principales

### Polimorfismo
Todas las clases que heredan de `BaseAnalyzer` implementan el método `analyze()` de manera diferente, permitiendo usar diferentes tipos de análisis de forma intercambiable.

### Encapsulación
- `BookDataManager` encapsula toda la lógica de manejo de datos
- Los métodos privados están protegidos con `_`
- Los datos se acceden a través de métodos públicos

### Herencia
Las clases de análisis heredan de `BaseAnalyzer`, reutilizando el método `display_results()` y forzando la implementación de `analyze()`.

## Uso del Sistema

```python
# 1. Crear el gestor de datos
data_manager = BookDataManager(url)

# 2. Crear analizadores específicos
general_analyzer = GeneralAnalyzer(data_manager)
fiction_analyzer = GenreAnalyzer(data_manager, "Fiction")
author_analyzer = AuthorAnalyzer(data_manager, "J.K. Rowling")

# 3. Ejecutar análisis
general_results = general_analyzer.analyze()
general_analyzer.display_results(general_results)

fiction_results = fiction_analyzer.analyze()
fiction_analyzer.display_results(fiction_results)

author_results = author_analyzer.analyze()
author_analyzer.display_results(author_results)
```

## Ejemplo de Polimorfismo

```python
# Todos los analizadores pueden ser tratados de manera uniforme
analyzers = [
    GeneralAnalyzer(data_manager),
    GenreAnalyzer(data_manager, "Fiction"),
    AuthorAnalyzer(data_manager, "J.K. Rowling")
]

for analyzer in analyzers:
    results = analyzer.analyze()  # Método polimórfico
    analyzer.display_results(results)  # Método heredado
```

## Ventajas del Diseño

1. **Modularidad**: Cada analizador tiene una responsabilidad específica
2. **Extensibilidad**: Fácil agregar nuevos tipos de análisis
3. **Reutilización**: El `BookDataManager` puede ser usado por múltiples analizadores
4. **Mantenibilidad**: Cambios en la lógica de datos no afectan los analizadores
5. **Polimorfismo**: Todos los analizadores pueden ser tratados de manera uniforme
6. **Especialización**: Cada clase se enfoca en un tipo específico de análisis

## Archivos del Proyecto

- `book_analyzer_classes.py`: Contiene las clases principales (BookDataManager, BaseAnalyzer, GeneralAnalyzer, GenreAnalyzer, AuthorAnalyzer)
- `example_usage.py`: Demostración de uso del sistema con las nuevas clases
- `README.md`: Este archivo de documentación 