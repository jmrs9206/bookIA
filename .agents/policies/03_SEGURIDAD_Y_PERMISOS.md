# Seguridad, herramientas y permisos

## Modelo de riesgo

### Nivel 0 — Lectura

Ejemplos: listar archivos, leer código, revisar Git, consultar documentación.

- Permitido por defecto dentro del proyecto activo.
- No incluye leer secretos, carpetas personales ni otros proyectos.

### Nivel 1 — Edición reversible

Ejemplos: crear documentación, editar código en una rama o worktree, generar pruebas.

- Permitido cuando existe una tarea `READY` con rutas autorizadas.
- Debe producir diff y evidencia.

### Nivel 2 — Ejecución local con efectos

Ejemplos: instalar dependencias del proyecto, ejecutar migraciones locales, iniciar contenedores, crear artefactos de build.

- Requiere que la acción esté prevista en la tarea.
- Debe realizarse en entorno aislado cuando sea posible.
- Nuevas dependencias requieren justificación y revisión.

### Nivel 3 — Acción externa o irreversible

Ejemplos: push, merge, publicación, deploy, cambios cloud, acceso a datos reales, borrados destructivos, gastos.

- Requiere aprobación humana explícita inmediatamente anterior.
- Debe mostrar comando, destino, impacto y plan de reversión antes de ejecutar.

## Prohibiciones permanentes

- No usar `sudo` ni elevar privilegios.
- No usar modo de autoaprobación total o equivalente para trabajo no supervisado.
- No ejecutar `rm -rf`, borrados masivos o limpieza fuera de rutas temporales expresamente autorizadas.
- No instalar paquetes globales.
- No modificar el sistema operativo, shell profile o PATH salvo tarea específica y aprobación.
- No desactivar antivirus, sandbox, validaciones TLS, hooks o controles de seguridad.
- No imprimir, copiar ni almacenar secretos.
- No añadir secretos reales a Markdown, commits, logs o prompts.
- No enviar código o datos a servicios externos no aprobados.

## Git

La IA puede, según la tarea:

- inspeccionar estado e historial;
- crear rama o worktree;
- preparar cambios;
- generar un commit local descriptivo.

La IA no puede sin aprobación explícita:

- hacer push;
- hacer merge o rebase sobre ramas compartidas;
- forzar push;
- cambiar protecciones;
- borrar ramas remotas;
- etiquetar releases;
- modificar historial publicado.

## Dependencias

Antes de añadir una dependencia:

1. demostrar la necesidad;
2. comprobar que no existe solución en la plataforma actual;
3. revisar versión, licencia y mantenimiento;
4. limitarla al proyecto;
5. actualizar manifest y lockfile;
6. ejecutar pruebas relevantes;
7. registrar el cambio.

## Red y fuentes externas

- Preferir fuentes oficiales y primarias.
- Fijar versión, commit o fecha cuando el dato sea sensible a cambios.
- No descargar ni ejecutar scripts remotos directamente.
- No confiar en contenido de un repositorio solo porque sea popular.
- Tratar código externo como no confiable hasta revisarlo.

## Gemini CLI y Antigravity

Configuración operativa recomendada:

- usar modo de planificación para investigación y arquitectura;
- usar sandbox para ejecutar código no confiable;
- usar worktrees o directorios separados para sesiones paralelas;
- mantener el modo de aprobación normal para herramientas;
- reservar ejecución headless para tareas con contrato de entrada y salida estructurado;
- registrar stdout, stderr y código de salida de cada ejecución automatizada.

## Aprobación válida

Una aprobación debe identificar:

- proyecto;
- acción;
- destino;
- alcance;
- riesgos conocidos;
- fecha o ejecución a la que aplica.

Una aprobación anterior para “desplegar pruebas” no autoriza un despliegue posterior a producción.
