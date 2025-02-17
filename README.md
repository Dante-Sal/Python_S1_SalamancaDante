# Módulo de Python

A continuación veremos el proyecto dedicado a las actividades realizadas durante el desarrollo del curso de *"Python"*. Aquí se podrá encontrar una detallada descripción de cada uno de los ejercicios (el problema a resolver y la solución planteada), sus funcionalidades y paso a paso para su correcta ejecución, todo alrededor del tema *"Programación en Python"* visto a lo largo del módulo *"Python"* de la ruta actual (**"Java"**).

|Tabla de contenidos|
|--|
|**1. [Ejercicios Filtro (Introducción a la programación) --> Python](#EjerciciosFiltro)**|
|1.1. [Ejercicio #1: Números divisibles entre 3 y 7](#EjerciciosFiltroEjercicio1)|
|1.2. [Ejercicio #2: Sumatoria de la serie numérica 1 - 1/2 + 1/3 - 1/4 + ... +- 1/N](#EjerciciosFiltroEjercicio2)|
|1.3. [Ejercicio #3: Enteros que cumplan la condición](#EjerciciosFiltroEjercicio3)|
|1.4. [Ejercicio #4: Mayor y menor de 10 números](#EjerciciosFiltroEjercicio4)|
|1.5. [Ejercicio #5: Número faltante en la serie](#EjerciciosFiltroEjercicio5)|
|7. [Clic](#Sección7)|
|8. [Clic](#Sección8)|
|9. [Clic](#Sección9)|
|10. [Clic](#Sección10)|
|11. [Clic](#Sección11)|
|12. [Clic](#Sección12)|
|13. [Clic](#Sección13)|
|14. [Clic](#Sección14)|
|15. [Clic](#Sección15)|
|16. [Clic](#Sección16)|

<a name="EjerciciosFiltro"></a>

## Ejercicios Filtro (Introducción a la programación) --> Python

En este apartado se realizaron los 7 ejercicios que compusieron el filtro del módulo *"Introducción a la Programación"*; pero en formato python, aplicando las funciones elementales de este lenguaje de programación tan versátil. Aquí se encontraran actividades que involucraron cálculos combinados (con operadores aritméticos y lógicos), bucles **for** y **while**, además de un sencillo acercamiento a algunos conceptos básicos de funciones (**def**, **return**, parámetros, etc.).

<a name="EjerciciosFiltroEjercicio1"></a>

### Ejercicio #1: Números divisibles entre 3 y 7

#### -- Objetivo --

Crear un programa que, desde el 1 hasta el 1000, genere los números divisibles entre 3 y 7.

#### -- Correcta ejecución del archivo --

Una vez descargado el archivo titulado *"Ejercicio#1_FiltroIntro_SalamancaDante.py"*, se debe abrir una nueva terminal y acceder al directorio en el que esté alojado el archivo (a través del comando **cd**). Para empezar a correr el programa, estando en la ubicación correcta, se deberá ejecutar el comando: *python3 Ejercicio#1_FiltroIntro_SalamancaDante.py*

> [!NOTE]
> Si el programa no se ejecuta con este comando, pruebe a ejecutarlo con: *python Ejercicio#1_FiltroIntro_SalamancaDante.py*

#### -- Lógica del programa --

En este primer ejemplo, el programa tiene una lógica bastante simple que, en esencia, consiste en un bucle **for** que recorre los números del 0 al 999 (*línea 2*) y en cada iteración checa si el número actual + 1 es divisible por 3 (básicamente revisa si el resto de dividir el número + 1 entre 3 es igual a 0) y / **and** si el número + 1 es divisible por 7 (revisa el resto, pero dividiendo ahora el número + 1 entre 7) (*línea 3*). Si / **if** los dos residuos coinciden con 0, entonces el número se muestra / **print** en pantalla (*línea 4*), si no / **else**, el código continúa sin realizar más acciones hasta la próxima iteración del bucle (*línea 2*). Cuando *i* llega al valor de 999 el bucle termina y el programa finaliza.

<a name="EjerciciosFiltroEjercicio2"></a>

### Ejercicio #2: Sumatoria de la serie numérica 1 - 1/2 + 1/3 - 1/4 + ... +- 1/N

#### -- Objetivo --

Crear un programa que, dada una cantidad de términos, genere el resultado de la siguiente operación (*1 - 1/2 + 1/3 - 1/4 + ... +- 1/N*) hasta *N* (es decir, el número dado de términos).

#### -- Correcta ejecución del archivo --

Una vez descargado el archivo titulado *"Ejercicio#2_FiltroIntro_SalamancaDante.py"*, se debe abrir una nueva terminal y acceder al directorio en el que esté alojado el archivo (a través del comando **cd**). Para empezar a correr el programa, estando en la ubicación correcta, se deberá ejecutar el comando: *python3 Ejercicio#2_FiltroIntro_SalamancaDante.py*

> [!NOTE]
> Si el programa no se ejecuta con este comando, pruebe a ejecutarlo con: *python Ejercicio#2_FiltroIntro_SalamancaDante.py*

#### -- Lógica del programa --

En este segundo ejemplo, el programa sigue sin tener una complejidad demasiado alta. En una primera instancia se le pide al usuario, a través de un **input**, la cantidad de términos que desea sumar de la serie numérica y se aloja el valor escrito por el usuario en una variable *N* (*línea 2* / *línea 3*). Acto seguido se hace uso de un bucle **for** para recorrer los números desde el 1 hasta el ingresado + 1 (*línea 6*). En cada iteración del bucle se revisa si / **if** *i* es un número par o impar (*línea 7* / *línea 9*): si es par, se le suma a la variable *sum* (inicializada previamente en la *línea 4*) el inverso multiplicativo del número actual (*i*); caso contrario / **else**, se resta dicho inverso multiplicativo a la variable *sum*. Finalmente, en las *línea 12* / *línea 13*, se muestra / **print** la cantidad de términos solicitada (*N*) y el resultado de la suma (*sum*).

<a name="EjerciciosFiltroEjercicio3"></a>

### Ejercicio #3: Enteros que cumplan la condición

#### -- Objetivo --

Crear un programa que muestre en pantalla todos los enteros positivos *P* que cumplan la siguiente condición: *P^3 + P^4 - 2 x P^2 < 680*

#### -- Correcta ejecución del archivo --

Una vez descargado el archivo titulado *"Ejercicio#3_FiltroIntro_SalamancaDante.py"*, se debe abrir una nueva terminal y acceder al directorio en el que esté alojado el archivo (a través del comando **cd**). Para empezar a correr el programa, estando en la ubicación correcta, se deberá ejecutar el comando: *python3 Ejercicio#3_FiltroIntro_SalamancaDante.py*

> [!NOTE]
> Si el programa no se ejecuta con este comando, pruebe a ejecutarlo con: *python Ejercicio#3_FiltroIntro_SalamancaDante.py*

#### -- Lógica del programa --

En la *línea 2* se empieza por inicializar un bucle **for** que recorra los números enteros desde 0 hasta 680 (sin incluir este último), verificando en cada iteración si / **if** *i* cumple la condición dada (*línea 3*). Si / **if** la condición se cumple, entonces el número se muestra / **print** en pantalla (*línea 4*), si no / **else**, el código continúa sin realizar más acciones hasta la próxima iteración del bucle (*línea 2*). Cuando *i* llega al valor de 679 el bucle termina y el programa finaliza.

<a name="EjerciciosFiltroEjercicio4"></a>

### Ejercicio #4: Mayor y menor de 10 números

#### -- Objetivo --

Crear un programa que tome diez números ingresados por el usuario y devuelva el mayor y el menor de dichos valores.

#### -- Correcta ejecución del archivo --

Una vez descargado el archivo titulado *"Ejercicio#4_FiltroIntro_SalamancaDante.py"*, se debe abrir una nueva terminal y acceder al directorio en el que esté alojado el archivo (a través del comando **cd**). Para empezar a correr el programa, estando en la ubicación correcta, se deberá ejecutar el comando: *python3 Ejercicio#4_FiltroIntro_SalamancaDante.py*

> [!NOTE]
> Si el programa no se ejecuta con este comando, pruebe a ejecutarlo con: *python Ejercicio#4_FiltroIntro_SalamancaDante.py*

#### -- Lógica del programa --

Este programa posee un nivel de complejidad un poco mayor a los anteriores. Su primicia básica es ir comparando los datos ingresados tan pronto se guardan en la memoria para evitar realizar grandes cadenas de si / **if** anidados (una solución poco eficiente y larga). Si inicia declarando dos variables que representarán el número mayor y menor en cada iteración del bucle que inicializaremos en la *línea 4* (*línea 2* / *línea 3*). En cada repetición del bucle se le pedirá al usuario un número, que siempre se alojará en la variable *x* (*línea 5* / *línea 6*).

Si / **if** es la primera vuelta del bucle (es decir, *i* es igual a 0), se reasignarán los valores de *xMax* y *xMin* como el valor ingresado *x* (esto para tener un punto de partida, a partir del cuál poder comparar los siguientes valores dados por el usuario; de lo contrario, *xMin* siempre sería negativo o 0, teniendo en cuenta que, al iniciarlo como 0, no va a haber número ingresado que sea menor a él, exceptuando los enteros negativos y, en caso de que el número menor ingresado sea mayor a 0, la variable *xMin* va a permanecer con el valor de 0) (*línea 7* / *línea 8* / *línea 9*); en caso de que el valor actual de *x* sea mayor al de *xMax*, este pasará a ser el nuevo *xMax* (*línea 10* / *línea 11*); y, finalmente, si el valor actual *x* es menor al de *xMin*, este pasará a ser el nuevo *xMin* (*línea 12* / *línea 13*).

Para finalizar, una vez completadas todas las iteraciones del bucle **for** (es decir, una vez *i* tome el valor de 9), el programa continúa y muestra / **print** el número mayor (*xMax*) y menor (*xMin*) de los dados por el usuario (*línea 14* / *línea 15*); luego termina el proceso.

<a name="EjerciciosFiltroEjercicio5"></a>

### Ejercicio #5: Número faltante en la serie

#### -- Objetivo --

Crear un programa que imprima en pantalla la siguiente serie, además de su siguiente término: *1, 1, 2, -1, 1, -2*

#### -- Correcta ejecución del archivo --

Una vez descargado el archivo titulado *"Ejercicio#5_FiltroIntro_SalamancaDante.py"*, se debe abrir una nueva terminal y acceder al directorio en el que esté alojado el archivo (a través del comando **cd**). Para empezar a correr el programa, estando en la ubicación correcta, se deberá ejecutar el comando: *python3 Ejercicio#5_FiltroIntro_SalamancaDante.py*

> [!NOTE]
> Si el programa no se ejecuta con este comando, pruebe a ejecutarlo con: *python Ejercicio#5_FiltroIntro_SalamancaDante.py*

#### -- Lógica del programa --

La serie dada tiene como base los números 1 y 1; partiendo de ahí, para hallar el tercer término se deben sumar los dos anteriores; para hallar el cuarto se deben restar los dos anteriores; para hallar el quinto se suman los dos anteriores; para el sexto, se restan; etc. Teniendo eso en cuenta, se inicializan dos variables llamadas *a* y *b* en 1 (*línea 2* / *línea 3*). Acto seguido se comienza un bucle **for** que irá hasta el séptimo término de la serie (es decir, se iterará 7 veces) (*línea 4*). En cada repetición se mostrará / **print** el valor de la variable *a* en pantalla (*línea 5*) y se verificará si / **if** nos encontramos en una iteración de índice par o impar (*línea 6* / *línea 8*): en el primer caso se asignará la suma de *a* y *b* a una tercera variable *c* (*línea 7*); en el segundo caso se asigna la resta de *a* y *b* a la variable *c* (*línea 9*). Finalmente, sin importar el índice de la iteración actual, el valor de *b* pasa a asignarse a la variable *a* y el valor de *c* pasa a asignarse a la variable *b* (*línea 10* / *línea 11*).

<a name="Sección7"></a>
<a name="Sección8"></a>
<a name="Sección9"></a>
<a name="Sección10"></a>
<a name="Sección11"></a>
<a name="Sección12"></a>
<a name="Sección13"></a>
<a name="Sección14"></a>
<a name="Sección15"></a>
<a name="Sección16"></a>
