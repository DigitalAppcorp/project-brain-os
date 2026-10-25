# Recetas de pruebas — frontend/UX

**Estas son plantillas adaptables, NO pruebas ejecutadas ni pruebas completas listas para producción.** Sustituir rutas, identificadores y resultados por los del repositorio; verificar instalación, versiones de Playwright/axe-core y entorno antes de usarlas. Ninguna prueba de ejemplo autoriza conexiones reales de pago, uso de credenciales ni producción.

## 1. Árbol de decisiones: qué probar
1. ¿Es solo texto/estilo? Captura y revisión del estado, contrastes y foco si cambia.
2. ¿Modifica navegación o interacción? E2E de éxito, volver, teclado, viewport y scroll.
3. ¿Depende de una consulta? Prueba de vacío, carga lenta, error y solicitud obsoleta.
4. ¿Modifica datos? Prueba de éxito confirmado, error, reintento, doble envío, permisos e idempotencia.
5. ¿Depende de dispositivo (mapa/GPS/PWA)? Emulación como primer filtro + dispositivo/navegador real cuando determine aceptación.
6. ¿Es evaluacion WCAG formal? Aplicar alcance/muestra/informe de WCAG-EM 2.0; axe solo detecta parte de los fallos.

## 2. Playwright — ruta feliz + error de red
Ejemplo conceptual TypeScript que **asume** una app propia de QA en `/formulario` y un POST a `**/api/solicitudes`. Requiere adaptar el texto visible, API y comportamiento según contrato. No enlazar contra producción.

```ts
import { test, expect } from '@playwright/test';

test('un envío confirmado produce resultado; error recuperable no borra datos', async ({ page }) => {
  let fallar = true;
  await page.route('**/api/solicitudes', async route => {
    if (route.request().method() !== 'POST') return route.continue();
    if (fallar) {
      fallar = false;
      return route.fulfill({ status: 503, contentType: 'application/json', body: '{"error":"unavailable"}' });
    }
    return route.fulfill({ status: 200, contentType: 'application/json', body: '{"id":"qa-1","ok":true}' });
  });

  await page.goto('/formulario');
  await page.getByRole('textbox', { name: 'Nombre' }).fill('Prueba QA');
  await page.getByRole('button', { name: 'Enviar' }).click();
  await expect(page.getByRole('alert')).toContainText(/intenta|reintenta/i);
  await expect(page.getByRole('textbox', { name: 'Nombre' })).toHaveValue('Prueba QA');
  await page.getByRole('button', { name: 'Reintentar' }).click();
  await expect(page.getByText('Solicitud recibida')).toBeVisible();
});
```

## 3. axe-core por pantalla y por estados
```ts
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('no se detectan violaciones automatizables en el estado abierto del diálogo', async ({ page }) => {
  await page.goto('/ejemplo');
  await page.getByRole('button', { name: 'Configuración' }).click();
  const dialog = page.getByRole('dialog');
  await expect(dialog).toBeVisible();
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});
```
**Advertencia**: un resultado vacío no certifica WCAG AA. Revisar manualmente foco, nombres, orden, contenido, gestos y zoom; axe audita el estado actual, no todos los estados ocultos. Referencia: https://playwright.dev/docs/accessibility-testing

## 4. Prueba de carrera y doble clic
Guion sin código específico:
- A: solicitud A lenta, usuario cambia a B y lanza B rápida. **Esperado**: respuesta tardía A no reemplaza el contexto visible B.
- B: dos clics rápidos en mutación. **Esperado**: no se duplica el registro ni se confirma doble cobro; idempotencia backend si aplica.
- C: la UI muestra éxito pero backend rechaza. **Esperado**: rollback/reconciliación y mensaje de recuperación.
- D: refresh a mitad de flujo. **Esperado**: rehidratación desde verdad autoritativa; ninguna suscripción o permiso inventado.
Guardar traza/red/estado final. Fake timers y mocks ayudan, pero completar verificación contra integración real cuando importe.

## 5. Regresión visual
Tomar capturas con mismo viewport, densidad, tema, semilla de datos, fuentes cargadas y animaciones estabilizadas. Comparar sobre referencia aprobada; revisar manualmente diferencias antes de aceptar nueva baseline. No aprobar automáticamente snapshots cuando el diseño cambió sin autorización. Añadir estados vacío, error, modal, scroll bajo barra fija y texto largo.

## 6. Lista manual de accesibilidad
- Usar teclado sin mouse; foco visible y no oculto en todos los controles importantes.
- Ejecutar tareas con lector de pantalla disponible y documentar lector+browser.
- Zoom 200 % y reflow equivalente a 320 CSS px según criterio; probar más zoom cuando riesgo de recorte.
- Contraste con herramienta y fondos dinámicos, targets reales, reduced motion.
- Probar mensaje de error en lector/teclado y mantener valores de formulario.
- Registrar SKIPPED/NOT_TESTED si no hay lector/dispositivo disponible: jamás escribir PASS por inferencia.

## 7. Formato de evidencia
`Prueba | Rama+SHA | URL/entorno | Navegador/version | Viewport | Dataset QA | Comando o guion | Observado | Esperado | PASS/FAIL/NOT_TESTED/INCONCLUSIVE | Prueba vinculada (traza/captura/log) | Fecha`.
Para evidencia sensible, guardar solo identificadores inocuos y no adjuntar tokens, PII ni pagos reales.

## 8. Criterio anti-teatro
- Compilar no implica que se haya ejecutado la app.
- Screenshot no demuestra interacción ni funcionamiento.
- Tests mockeados no demuestran conectividad real.
- No reproducido ≠ arreglado.
- Cero errores reportados ≠ conformidad accesible.
- «Pendiente de medición» no se registra como cero.
