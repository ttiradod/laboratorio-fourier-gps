# Fourier por ventanas

Esta fase amplía el análisis global de Fourier para estudiar cómo cambia la cadencia estimada a lo largo del tramo.

En lugar de aplicar la FFT sobre todo el tramo completo, la señal se divide en ventanas temporales solapadas. En cada ventana se calcula la frecuencia dominante dentro de un rango compatible con la cadencia de pasos.

## Objetivo

El objetivo es pasar de una única estimación global:

CSV GPS → tramo completo → FFT → cadencia dominante global

a una estimación temporal:

CSV GPS → ventanas de tiempo → FFT en cada ventana → cadencia estimada a lo largo del tramo

Esto permite observar si la cadencia estimada se mantiene estable o si existen zonas donde la señal GPS no representa bien la periodicidad de los pasos.

## Parámetros utilizados

En las pruebas se han utilizado los siguientes parámetros:

| Parámetro | Valor |
|---|---:|
| Duración de ventana | 8 s |
| Salto entre ventanas | 1 s |
| Frecuencia mínima | 1.3 Hz |
| Frecuencia máxima | 2.5 Hz |
| Rango equivalente | 78 - 150 pasos/min |

La ventana de 8 segundos se eligió porque ofrece un resultado más estable que una ventana más corta de 4 segundos. Sin embargo, también reduce la precisión temporal, ya que cada punto de la gráfica representa una ventana completa y no un instante exacto.

## Gráfica interactiva

El programa genera una gráfica interactiva en HTML llamada:

`cadencia_ventanas.html`

En esta gráfica, cada punto representa la cadencia estimada en una ventana temporal.

Al pasar el ratón sobre cada punto se muestra:

- inicio y fin de la ventana;
- tiempo central de la ventana;
- cadencia estimada;
- frecuencia dominante;
- magnitud del pico dominante.

Es importante tener en cuenta que un punto de la gráfica no representa la cadencia exacta en un instante, sino la cadencia dominante estimada dentro de una ventana de tiempo.

Por ejemplo, un punto con tiempo central 10 s y ventana 6-14 s representa la frecuencia dominante calculada usando los datos comprendidos entre los segundos 6 y 14.

## Resultado en la prueba 1

En la caminata normal, la cadencia estimada por ventanas se mantiene bastante estable alrededor de 104-105 pasos/min.

Este resultado coincide con la referencia observada en Garmin y con el resultado de la Fourier global.

Esto indica que, cuando la señal GPS contiene oscilaciones periódicas claras asociadas a los pasos, el análisis por ventanas puede estimar correctamente la cadencia.

## Resultado en la prueba 2

En la caminata rápida, la cadencia estimada por ventanas es mucho más irregular.

Algunas ventanas muestran valores cercanos a la cadencia esperada según Garmin, alrededor de 126-131 pasos/min. Sin embargo, otras ventanas muestran valores alejados, lo que indica que la frecuencia dominante detectada no siempre corresponde a la cadencia real.

Esto muestra que la cadencia real puede aparecer en algunas ventanas, pero no domina de forma constante la señal de velocidad GPS.

## Conclusión

Fourier por ventanas aporta más información que la Fourier global, porque permite ver cómo evoluciona la frecuencia dominante a lo largo del tramo.

Sin embargo, los resultados muestran que la velocidad GPS no siempre contiene una señal suficientemente clara para estimar la cadencia de forma robusta.

Por tanto, el GPS puede ser útil para analizar velocidad, distancia, parciales, ritmo y evolución del desplazamiento, pero para estimar pasos o paladas de forma fiable parece más adecuado utilizar una IMU.