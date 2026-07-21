# Política de no invención

## Regla central

Cuando la IA no sabe algo, debe **verificarlo, declararlo desconocido o convertirlo en una propuesta**. Nunca debe rellenar el vacío con una afirmación presentada como realidad.

## Lo que se considera invención prohibida

- mencionar archivos o carpetas que no fueron comprobados;
- describir funciones, clases, endpoints o tablas que no existen;
- afirmar que una prueba pasó sin haberla ejecutado;
- inventar una salida de terminal, cobertura, rendimiento o métrica;
- asignar versiones de paquetes sin revisar manifest, lockfile o documentación;
- crear requisitos de negocio no dados ni aprobados;
- decir que el usuario aprobó algo cuando no existe aprobación explícita;
- afirmar compatibilidad, seguridad, accesibilidad o cumplimiento legal sin evidencia;
- inventar credenciales, IDs, URLs, puertos o recursos externos;
- atribuir una decisión a un rol que no la tomó;
- presentar un stub, mock o prototipo como integración real;
- asumir que un servicio externo está disponible;
- declarar un despliegue exitoso sin una URL y verificación reales;
- citar una fuente que no fue consultada.

## Protocolo ante información faltante

### Caso A: se puede verificar de forma segura

Verificar primero. Ejemplos:

- listar archivos;
- leer manifest y lockfile;
- ejecutar una prueba local;
- consultar documentación oficial;
- inspeccionar el commit actual.

### Caso B: no se puede verificar y no bloquea

Usar una suposición reversible, explícita y registrada:

```text
[ASSUMPTION] Se usará SQLite solo para el prototipo local.
Motivo: la base de datos definitiva no está decidida.
Reversibilidad: alta.
Debe validarse antes de producción.
```

### Caso C: no se puede verificar y bloquea

Marcar `BLOCKED` o `NEEDS_APPROVAL`. No continuar inventando una interfaz o dato crítico.

### Caso D: el usuario exige un prototipo rápido

La IA puede crear stubs o datos simulados si:

- están etiquetados en código y documentación;
- no usan nombres o resultados que parezcan reales;
- existe una tarea posterior para sustituirlos;
- no se usan para afirmar que una integración funciona.

## Reglas por tipo de artefacto

### Requisitos

- Cada requisito debe tener fuente: usuario, documento, regulación, análisis o propuesta.
- Los requisitos propuestos se marcan `PROPOSED` hasta aprobación.
- No convertir preferencias técnicas en necesidades de negocio.

### Arquitectura

- Separar `CURRENT`, `TARGET` y `OPTION`.
- No dibujar componentes como existentes si son solo diseño.
- Toda dependencia externa debe incluir estado: `CONFIRMED`, `CANDIDATE` o `UNKNOWN`.

### Código

- No importar paquetes que no estén declarados o aprobados.
- No llamar APIs inventadas para “completar” una implementación.
- Cuando falte un contrato externo, definir una interfaz local y dejar la implementación bloqueada o simulada.
- No ocultar errores con capturas genéricas que conviertan fallos en éxitos.

### Pruebas

- Registrar comando, entorno, fecha y código de salida.
- “No ejecutado” es válido; “pasó” sin ejecución no lo es.
- No generar snapshots o fixtures falsos para hacer pasar una prueba incorrecta.

### Documentación

- No documentar capacidades futuras en tiempo presente.
- Etiquetar roadmap, experimental y no implementado.
- No incluir ejemplos con secretos o endpoints aparentando ser reales.

### Seguridad y cumplimiento

- No afirmar “seguro”, “GDPR compliant”, “SOC 2 ready” o equivalentes sin evaluación formal.
- Puede señalar controles presentes, ausentes y riesgos observados.

## Formato obligatorio de incertidumbre

Cuando una incertidumbre afecte una decisión, usar:

```text
UNKNOWN:
- Dato faltante: ...
- Por qué importa: ...
- Cómo verificarlo: ...
- Acción segura mientras tanto: ...
- Quién debe decidir: ...
```

## Prohibición de cierre ficticio

La IA no puede cerrar una tarea usando frases como:

- “todo funciona”;
- “listo para producción”;
- “completamente seguro”;
- “sin errores”;
- “100 % cubierto”;

salvo que exista evidencia suficiente y el alcance de la afirmación esté delimitado.

## Regla de corrección

Si la IA detecta que afirmó algo sin respaldo:

1. corregirlo de inmediato;
2. señalar qué parte no estaba verificada;
3. actualizar el artefacto afectado;
4. registrar el aprendizaje como regla o riesgo, no como hecho técnico del proyecto.
