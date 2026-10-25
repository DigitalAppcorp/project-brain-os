# Protocolo de medición verificable — UI, UX y accesibilidad

## Objetivo
Un hallazgo medido debe ser reproducible. Separar **norma aplicable**, **valor obtenido**, **cómo se obtuvo** y **alcance de la conclusión**. El protocolo no reemplaza WCAG 2.2, WCAG-EM 2.0 ni guías oficiales, que son la fuente de autoridad. Un caso PASS no certifica todo el producto.

## Registro mínimo por medición
| Campo | Exigencia |
| --- | --- |
| ID/hallazgo | Identificador estable, pantalla, componente y estado concreto |
| Fuente/versión | URL o ruta de archivo, rama/SHA y entorno de ejecución, fecha/hora |
| Dispositivo | Navegador/versión, sistema, viewport, zoom, escala y preferencias pertinentes |
| Tipo de evidencia | `MEASURED` / `REPORTED` / `CODE_INSPECTED` / `ESTIMATED` / `NOT_TESTED` |
| Norma | WCAG 2.2 criterio y nivel, u orientación de plataforma identificada como GUÍA |
| Medida | Valor, unidades, condiciones, herramienta y versión/método |
| Umbral | Valor de referencia, excepciones examinadas, aplicabilidad |
| Resultado | `PASS` / `FAIL` / `INCONCLUSIVE` / `NOT_TESTED`; si reportado, no atribuir prueba propia |
| Evidencia | Captura, traza, selector/DOM, cálculo, registro verificable o URL (sin secretos/PII) |
| Incidente | Severidad S0–S4/SIN_DETERMINAR + estado del incidente + confianza: **tres campos distintos** |
| Reproducción | Pasos, estados, expected/observed, repeticiones y condiciones dinámicas |
| Limitaciones | Qué no se midió o no puede inferirse y prueba propuesta |

Para concisión: en el resumen mostrar ID/resultado/gravedad; en el detalle conservar campos completos. El registro de un tercero se etiqueta `REPORTED` incluso si contiene números.

## Medición de contraste — WCAG 2.2
- **1.4.3 (AA, texto normal):** >= **4.5:1**, con excepciones normativas (p. ej., texto incidental, logotipos, inactivo).
- **1.4.3 (AA, texto grande):** >= **3:1**, según definición normativa de tamaño y peso (aprox. 24 CSS px normal, o 18.66 CSS px en negrita, a zoom/escala CSS ordinaria; confirmar equivalencias pt y contexto).
- **1.4.11 (AA, no textual):** >= **3:1** cuando la información visual necesaria de componentes/objetos gráficos entra en el criterio y no aplica excepción. No extrapolar el umbral 3:1 a todos los pixels o contenedores decorativos.
- Verificar color de primer plano, fondo **real renderizado**, opacidad, composición alfa y estados normal/hover/focus/disabled, cuando aplique. Sobre foto, video, mapas, desenfoque o degradado, probar muestras representativas y situaciones desfavorables. Contraste medido en una zona no prueba legibilidad en toda la superficie.
- Para colores sRGB opacos ya compuestos: linealizar cada canal normalizado `c` con `c / 12.92` si `c <= 0.04045`, o `((c+0.055)/1.055)^2.4` en caso contrario. Luminancia relativa `L = 0.2126 R + 0.7152 G + 0.0722 B`; contraste `(L_mayor + 0.05)/(L_menor + 0.05)`. No calcular valores sobre colores HEX sin resolver transparencia/imagen.
- **Capturas comprimidas/antialias:** medidas derivadas de píxeles pueden aproximar; etiquetar `ESTIMATED` y contrastar con color de texto renderizado y fondo real. No elevar aproximaciones a cumplimiento certificado.
- Si se informa «2.0–2.25:1», registrar ese rango como `REPORTED`, comprobar si el texto es grande y si hay excepciones antes de asignar `FAIL` verificado.

## Objetivos, tamaños y entradas
- **WCAG 2.2 2.5.8 (AA):** objetivo de tamaño mínimo **24×24 CSS px** *o* alternativa de espaciamiento/excepción definida en el criterio. Revisar **hitbox calculada**, no el glyph. Tamaño recomendado de plataforma (p. ej. 44 pt Apple) es **GUÍA**, no requisito web equivalente.
- Medir en escenarios de scroll, tamaños 320/375/430 CSS px según producto, zoom y barras superpuestas. Esos anchos son cobertura interna, no límites legales universales.
- Etiquetas/roles/nombres: comparar DOM accesible y nombre computado (no suponer que un placeholder o atributo `title` satisface todo criterio); ejecutar Tab/Shift+Tab/Enter/Space/Escape, comprobar foco y error.
- Anuncios accesibles: comprobar resultado con lector de pantalla real cuando se pueda; encontrar `role="alert"` en código no prueba lectura en todas las tecnologías.
- Performance: objetivos LCP <=2.5 s, INP <=200 ms, CLS <=0.1 en p75 de visitas reales cuando haya RUM. No usar resultado de laboratorio como si fuera p75 de producción.

## Ejemplo de ficha (sin afirmar ejecución)
```yaml
id: UX-C-001
screen: "bienvenida"
element: "titulo-principal"
state: "fondo-imagen-estatico"
source: { repo: "ejemplo", ref: "rama@sha", environment: "QA" }
device: { browser: "sin medir", viewport_css_px: null, zoom: null }
evidence_type: REPORTED
criterion: { source: "WCAG 2.2", id: "1.4.3", level: "AA" }
observed: { value: "2.0–2.25", unit: "ratio", method: "medicion ajena sin traza" }
threshold: { value: 3.0, unit: "ratio", applicability: "PENDIENTE confirmar texto grande" }
test_result: INCONCLUSIVE
incident: { severity: SIN_DETERMINAR, status: NEEDS_REPRO, confidence: baja }
proof: null
next_test: "Verificar CSS de texto, fondos renderizados y muestras críticas en QA"
```

## No sobregeneralizar
- `FAIL` para un elemento concreto ≠ «toda la web no cumple».
- `PASS` en una pantalla ≠ conformidad WCAG AA del producto.
- Una auditoría formal usa cobertura/muestra según [QUALITY_GATES.md](QUALITY_GATES.md) y WCAG-EM 2.0.
- Preferencias de estética no tienen ratio de conformidad: describir evidencia perceptiva, contexto y revisión de usuarios, no fabricar un número.
- El auditor en [READ_ONLY_AUDIT.md](READ_ONLY_AUDIT.md) **no ejecuta operaciones que alteren el producto para obtener valores**.

## Autoridades oficiales
- [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [W3C — Entender contraste mínimo](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- [W3C — Contraste no textual](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)
- [W3C — Tamaño de objetivos](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- [W3C — WCAG-EM 2.0](https://www.w3.org/TR/wcag-em-2/)
