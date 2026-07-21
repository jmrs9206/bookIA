# Skill: Validar tarea o incremento

## Objetivo

Comprobar que el comportamiento implementado satisface criterios de aceptación de forma reproducible.

## Rol principal

`@qa`.

## Procedimiento

1. Construir una matriz entre requisitos, AC y pruebas.
2. Preparar un entorno aislado y registrar versiones relevantes.
3. Ejecutar las pruebas obligatorias.
4. Añadir pruebas de borde y regresión dentro del alcance.
5. Verificar errores esperados, no solo camino feliz.
6. Comprobar que stubs y mocks están identificados.
7. Registrar comando, resultado, exit code y artefactos.
8. Abrir defectos reproducibles cuando falle.
9. No corregir el código salvo que exista una tarea de rework separada.
10. Emitir `PASS`, `FAIL` o `BLOCKED` por criterio.

## Salidas

- matriz AC→evidencia;
- defectos con pasos de reproducción;
- actualización de `EVIDENCE_LOG.md`;
- estado `NEEDS_APPROVAL`, `NEEDS_REWORK` o `BLOCKED`.

## Prohibiciones

- No cambiar criterios para que pasen.
- No usar datos sensibles.
- No declarar rendimiento sin una prueba definida.
- No confundir una prueba unitaria con validación integral.
- No afirmar “listo para producción”.
