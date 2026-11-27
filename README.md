# Tecnológico de Monterrey
### Campus Monterrey

# Evidencia 1. Video Individual de Etapas Iniciales

## Reto de Business Intelligence — OT Consulting

**Soporte Analítico para la Toma de Decisiones**  
Grupo 301 | Equipo 3 | Quinto semestre

**Profesoras:**  
Claudia Aja Leyva  
Maria Imelda Valdez

**Alumno:** Juan Manuel Villarreal Moral  
**Matrícula:** A01723446

26 de noviembre de 2026

---

## 1. Justificación y planeación

El objetivo del reto es desarrollar un módulo de Business Intelligence que permita a los gerentes y directores de OT Consulting mejorar la asignación de colaboradores, la planeación de proyectos y la estimación de costos.

### Propuesta de solución

- Tablero de indicadores y disponibilidad de colaboradores.
- Consulta de perfiles y habilidades.
- Simulador de equipos y costos por proyecto.
- Resumen general de proyectos y asignaciones.

[Consultar documento de la etapa 1](Entregas%20Reto/Equipo%203%20-%20Avance%20Reto%20Etapa%201.pdf)

---

## 2. Exploración de datos

Se realizó un proceso de Data Profiling sobre ocho fuentes de información proporcionadas por OT Consulting.

### Fuentes de datos

| Fuente | Registros | Columnas |
|---|---:|---:|
| Colaboradores | 107 | 45 |
| Asignaciones | 31 | 11 |
| Clientes | 12 | 13 |
| Departamentos | 6 | 7 |
| Roles | 55 | 6 |
| Habilidades | 71 | 6 |
| Matriz de habilidades | 54 | 77 |
| Activos | 123 | 11 |
| **Total** | **459** | **176** |

### Principales hallazgos

| Hallazgo | Registros |
|---|---:|
| Colaboradores con puesto pendiente | 48 |
| Asignaciones sin rol definido | 29 de 31 |
| Asignaciones con fecha de fin indefinida | 24 de 31 |
| Equipos asignados a colaboradores dados de baja | 17 |

También se identificaron problemas de integridad referencial, valores faltantes y formatos inconsistentes.

### Preguntas detonadoras

- ¿Qué colaboradores terminarán pronto una asignación?
- ¿Qué colaboradores no tienen proyectos asignados?
- ¿Cuál es el costo por hora de cada colaborador?
- ¿Cuánto cuesta tener colaboradores sin asignación?
- ¿Qué colaboradores tienen las habilidades necesarias para un nuevo proyecto?
- ¿En qué fase se encuentra cada proyecto y cuáles están atrasados?
- ¿Qué equipos siguen asignados a colaboradores dados de baja?

### Indicadores propuestos

| Indicador | Justificación |
|---|---|
| Tasa de utilización | Conocer el aprovechamiento del personal. |
| Colaboradores sin asignación | Identificar recursos potencialmente disponibles. |
| Costo mensual sin asignación | Identificar oportunidades de optimización. |
| Vencimientos a 30, 60 y 90 días | Anticipar la liberación de recursos. |
| Costo de nómina por proyecto | Apoyar la planeación financiera. |
| Proyectos atrasados | Mejorar el seguimiento de proyectos. |
| Cobertura de habilidades | Identificar capacidades y brechas de conocimiento. |

[Consultar documento de la etapa 2](Entregas%20Reto/Equipo%203%20-%20Avance%20Reto%20Etapa%202.pdf)

---

## 3. Tratamiento y acondicionamiento de datos

Se utilizó SQL y MySQL Workbench para preparar las fuentes de información.

### Proceso de acondicionamiento

1. Creación de la base de datos OTC.
2. Creación de ocho tablas de staging.
3. Importación de archivos CSV.
4. Validación de registros mediante COUNT y UNION ALL.
5. Limpieza y estandarización de datos.
6. Generación de tablas acondicionadas con el prefijo clean_.

### Métodos de corrección

- Estandarización de formatos y valores.
- Tratamiento de datos faltantes.
- Conversión de tipos de datos.
- Validación de integridad referencial.
- Generación de atributos de revisión.

### Nuevos atributos

| Atributo | Descripción |
|---|---|
| costo_por_hora | Sueldo total integrado / 160 horas. |
| revision_sueldo | Identificación de salarios vacíos o en cero. |
| estado_asignacion | Clasificación de colaboradores según su situación de asignación. |
| dias_para_finalizar | Diferencia entre la fecha de fin y la fecha actual. |
| estado_vencimiento | Clasificación de asignaciones según su vencimiento. |
| nivel_numerico | Nivel de habilidad en una escala del 1 al 4. |

### Reglas de negocio

- Relacionar las tablas mediante identificadores únicos.
- Todo colaborador activo debe contar con un rol.
- Las asignaciones deben tener fechas planeadas.
- La dedicación total no debe superar el 100%.
- Conservar el historial salarial.
- Registrar la devolución de activos al finalizar la relación laboral.
- Estandarizar los formatos de captura.

### Evidencias técnicas

- [Código SQL: creación y carga de tablas](Entregas%20Reto/OTC.sql)
- [Tablas acondicionadas](Entregas%20Reto/Databases)
- [Colaboradores](Entregas%20Reto/Databases/clean_colaboradores.csv)
- [Asignaciones](Entregas%20Reto/Databases/clean_asignaciones.csv)
- [Matriz de habilidades transformada](Entregas%20Reto/Databases/clean_matriz_habilidades.csv)

[Consultar documento de la etapa 3](Entregas%20Reto/Equipo%203%20-%20Avance%20Reto%20Etapa%203.pdf)

---

## 4. Diseño del modelo dimensional lógico

Se diseñó un modelo dimensional utilizando la metodología de Kimball.

### Metodología

1. Seleccionar el proceso de negocio.
2. Declarar la granularidad.
3. Identificar las dimensiones.
4. Identificar los hechos y métricas.

### Tablas de hechos

| Tabla | Registros documentados | Granularidad |
|---|---:|---|
| Fact_Asignacion | 31 | Colaborador asignado a un proyecto. |
| Fact_Habilidad_Colaborador | 1,529 | Colaborador y habilidad. |
| Fact_Activo | 123 | Equipo de cómputo y colaborador. |

### Tablas de dimensiones

- Dim_Colaborador
- Dim_Rol
- Dim_Departamento
- Dim_Cliente_Proyecto
- Dim_Habilidad
- Dim_Activo
- Dim_Tiempo

El modelo corresponde a una constelación de hechos, donde Dim_Colaborador funciona como una dimensión conformada y Dim_Tiempo como una dimensión de rol múltiple.

[Consultar modelo dimensional lógico y documentación de la etapa 4](Entregas%20Reto/Equipo%203%20-%20Avance%20Reto%20Etapa%204.pdf)

---

## 5. Demostración de la propuesta

Prototipo del módulo de Business Intelligence desarrollado por el equipo 3.

### Funcionalidades

- Resumen ejecutivo.
- Disponibilidad de colaboradores.
- Análisis de habilidades.
- Simulador de equipos y costos.
- Seguimiento de proyectos.
- Administración de activos.

[**Abrir prototipo de OT Consulting**](https://otc-app-equipo3.netlify.app/#)

---

## 6. Conclusiones y acciones futuras

Las primeras cuatro etapas permitieron identificar las necesidades de OT Consulting, evaluar la calidad de sus datos, acondicionar las fuentes de información y diseñar un modelo dimensional orientado a la toma de decisiones.

### Recomendaciones

- Implementar validaciones desde la captura de datos.
- Estandarizar los identificadores.
- Mantener actualizada la matriz de habilidades.
- Mejorar el seguimiento de las asignaciones.

### Siguientes pasos

- Automatizar el proceso ETL.
- Validar las reglas de negocio y los indicadores.
- Confirmar los supuestos de costos y horas laborales.
- Incorporar los porcentajes de dedicación.
- Continuar validando el tablero y el simulador.
- Evaluar la integración con la plataforma de OT Consulting.
