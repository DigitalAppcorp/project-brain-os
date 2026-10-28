# Gate profesional autónomo — verificación acotada de v0.7

Motivación recuperable: [orden y actualización PAZO147](https://github.com/DigitalAppcorp/pazo-app/issues/147). El caso reveló aplicación insuficiente del método: un reporte interno revisó legibilidad/targets/overflow, no la composición completa a través de los estados. La habilidad anterior ya advertía que ingeniería no basta, pero su ruta general de aprobación trasladaba la aceptación estética de piezas nuevas al PO. Se corrige la decisión de responsabilidad y el gate, sin imponer una estética PAZO al OS.

Cambios mínimos de método: un protocolo central distingue UI nueva autorizada, rediseño dirigido, decisión fuera de alcance y corrección técnica. Exige runtime completo, estados pertinentes, comparación con no añadir nada, crítica adversarial y autocorrección. SKILL, gates, referencias de preview/integridad y plantilla enrutan a esa única política. Ninguna de ellas concede permiso de implementar desde una auditoría, merge, datos, gasto ni lanzamiento. Brain OS raíz1.4.1 permanece intacto.

## Pruebas ejecutadas

Python3.14.8 local, biblioteca estándar, sin servicios ni datos de PAZO:

```text
python -X utf8 -B knowledge/ui-ux-frontend/scripts/test_learning.py
Ran 13 tests — OK
python -X utf8 -B knowledge/ui-ux-frontend/scripts/test_visual_review.py
Ran 11 tests — OK
```

Once contraejemplos: UI nueva completa no requiere voto estético ni obtiene release; build/targets/overflow solos no cierran gate; faltan estados; recorte de componente; captura creada pero no vista; artefacto modificado; rediseño dirigido mantiene gate; aceptación PO sin fuente se rechaza; técnico no visual no necesita paquete artístico; falta juicio de composición; ruta de evidencia externa/ausente.

El validador [visual_review.py](scripts/visual_review.py) comprueba integridad del registro/hashes/cobertura y distingue estados. **RECORD_COMPLETE no significa que una composición sea buena ni que el revisor diga la verdad.** Las imágenes deben inspeccionarse y criticarse; el juicio y la responsabilidad del agente no se automatizan por esta utilidad. Los archivos de tests son fixtures sintéticos etiquetados. No hay puntuaciones de UX ni inferencias de rendimiento/conversión.

Workflow `Design OS evidence and authority contracts` ejecuta ambas suites en cada PR. Ver su resultado del SHA exacto antes de cualquier integración. E01–E25 como comparación independiente de agentes siguen NOT_EVALUATED; no hay una mejora porcentual demostrada del modelo. La prueba situada y sus decisiones viven en el PR del producto. El PO puede revisar voluntariamente el resultado; eso no hace obligatoria su intervención en toda UI nueva.

## Publicación del método

Candidato en rama/PR específico, sin merge automático ni instalación global. La integración requiere los gates aplicables. Release de cada producto continúa siendo otra autorización. No añadir hooks, telemetría, memoria duplicada ni servicios de escucha para aplicar el método.
