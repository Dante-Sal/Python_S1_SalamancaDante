# Módulo de Python

A continuación veremos el proyecto dedicado a las actividades realizadas durante el desarrollo del curso de *"Python"*. Aquí se podrá encontrar una detallada descripción de cada uno de los ejercicios (el problema a resolver y la solución planteada), sus funcionalidades y paso a paso para su correcta ejecución, todo alrededor del tema *"Programación en Python"* visto a lo largo del módulo *"Python"* de la ruta actual (**"Java"**).

|Tabla de contenidos|
|--|
|<br>**1. [Ejercicios Filtro (Introducción a la programación) --> Python](#EjerciciosFiltro)**<br><br>|
|1.1. [Ejercicio #1: Números divisibles entre 3 y 7](#EjerciciosFiltroEjercicio1)|
|1.2. [Ejercicio #2: Sumatoria de la serie numérica 1 - 1/2 + 1/3 - 1/4 + ... +- 1/N](#EjerciciosFiltroEjercicio2)|
|1.3. [Ejercicio #3: Enteros que cumplan la condición](#EjerciciosFiltroEjercicio3)|
|1.4. [Ejercicio #4: Mayor y menor de 10 números](#EjerciciosFiltroEjercicio4)|
|1.5. [Ejercicio #5: Número faltante en la serie](#EjerciciosFiltroEjercicio5)|
|1.6. [Ejercicio #6: Empresa ACME](#EjerciciosFiltroEjercicio6)|
|1.7. [Ejercicio #7: Números amigos](#EjerciciosFiltroEjercicio7)|
|<br>**2. [Python Workshop (1-5)](#PythonWorkshop)**<br><br>|
|2.1. [Ejercicio 1: Conversor de temperatura](#PythonWorkshopEjercicio1)|
|2.2. [Ejercicio 2: Calculadora de interés simple y compuesto](#PythonWorkshopEjercicio2)|
|2.3. [Ejercicio 3: Clasificador de números](#PythonWorkshopEjercicio3)|
|2.4. [Ejercicio 4: Generador de contraseñas](#PythonWorkshopEjercicio4)|
|2.5. [Ejercicio 5: Detector de palíndromos](#PythonWorkshopEjercicio5)|
|15. [Clic](#Sección15)|
|16. [Clic](#Sección16)|

<a name="EjerciciosFiltro"></a>

## Ejercicios Filtro (Introducción a la programación) --> Python

En este apartado se realizaron los 7 ejercicios que compusieron el filtro del módulo *"Introducción a la Programación"*; pero en formato python, aplicando las funciones elementales de este lenguaje de programación tan versátil. Aquí se encontrarán actividades que involucraron cálculos combinados (con operadores aritméticos y lógicos), bucles **for** y **while**, además de un sencillo acercamiento a algunos conceptos básicos de funciones (**def**, **return**, parámetros, etc.).

<a name="EjerciciosFiltroEjercicio1"></a>

### Ejercicio #1: Números divisibles entre 3 y 7

#### -- Objetivo --

Crear un programa que, desde el 1 hasta el 1000, genere los números divisibles entre 3 y 7.

#### -- Correcta ejecución del archivo --

Una vez descargado el archivo titulado *"Ejercicio#1_FiltroIntro_SalamancaDante.py"*, se debe abrir una nueva terminal y acceder al directorio en el que esté alojado el archivo (a través del comando **cd**). Para empezar a correr el programa, estando en la ubicación correcta, se deberá ejecutar el comando: ```python3 Ejercicio#1_FiltroIntro_SalamancaDante.py```

> [!NOTE]
> Si el programa no se ejecuta con este comando, pruebe a ejecutarlo con: ```python Ejercicio#1_FiltroIntro_SalamancaDante.py```

#### -- Lógica del programa --

En este primer ejemplo, el programa tiene una lógica bastante simple que, en esencia, consiste en un bucle **for** que recorre los números del 0 al 999 (*línea 2*) y en cada iteración checa si el número actual + 1 es divisible por 3 (básicamente revisa si el resto de dividir el número + 1 entre 3 es igual a 0) y / **and** si el número + 1 es divisible por 7 (revisa el resto, pero dividiendo ahora el número + 1 entre 7) (*línea 3*). Si / **if** los dos residuos coinciden con 0, entonces el número se muestra / **print** en pantalla (*línea 4*), si no / **else**, el código continúa sin realizar más acciones hasta la próxima iteración del bucle (*línea 2*). Cuando *i* llega al valor de 999 el bucle termina y el programa finaliza.

<a name="EjerciciosFiltroEjercicio2"></a>

### Ejercicio #2: Sumatoria de la serie numérica 1 - 1/2 + 1/3 - 1/4 + ... +- 1/N

#### -- Objetivo --

Crear un programa que, dada una cantidad de términos, genere el resultado de la siguiente operación (*1 - 1/2 + 1/3 - 1/4 + ... +- 1/N*) hasta *N* (es decir, el número dado de términos).

#### -- Correcta ejecución del archivo --

Una vez descargado el archivo titulado *"Ejercicio#2_FiltroIntro_SalamancaDante.py"*, se debe abrir una nueva terminal y acceder al directorio en el que esté alojado el archivo (a través del comando **cd**). Para empezar a correr el programa, estando en la ubicación correcta, se deberá ejecutar el comando: ```python3 Ejercicio#2_FiltroIntro_SalamancaDante.py```

> [!NOTE]
> Si el programa no se ejecuta con este comando, pruebe a ejecutarlo con: ```python Ejercicio#2_FiltroIntro_SalamancaDante.py```

#### -- Lógica del programa --

En este segundo ejemplo, el programa sigue sin tener una complejidad demasiado alta. En una primera instancia se le pide al usuario, a través de un **input**, la cantidad de términos que desea sumar de la serie numérica y se aloja el valor escrito por el usuario en una variable *N* (*línea 2* / *línea 3*). Acto seguido se hace uso de un bucle **for** para recorrer los números desde el 1 hasta el ingresado + 1 (*línea 6*). En cada iteración del bucle se revisa si / **if** *i* es un número par o impar (*línea 7* / *línea 9*): si es par, se le suma a la variable *sum* (inicializada previamente en la *línea 4*) el inverso multiplicativo del número actual (*i*); caso contrario / **else**, se resta dicho inverso multiplicativo a la variable *sum*. Finalmente, en las *línea 12* / *línea 13*, se muestra / **print** la cantidad de términos solicitada (*N*) y el resultado de la suma (*sum*).

<a name="EjerciciosFiltroEjercicio3"></a>

### Ejercicio #3: Enteros que cumplan la condición

#### -- Objetivo --

Crear un programa que muestre en pantalla todos los enteros positivos *P* que cumplan la siguiente condición: *P^3 + P^4 - 2 x P^2 < 680*

#### -- Correcta ejecución del archivo --

Una vez descargado el archivo titulado *"Ejercicio#3_FiltroIntro_SalamancaDante.py"*, se debe abrir una nueva terminal y acceder al directorio en el que esté alojado el archivo (a través del comando **cd**). Para empezar a correr el programa, estando en la ubicación correcta, se deberá ejecutar el comando: ```python3 Ejercicio#3_FiltroIntro_SalamancaDante.py```

> [!NOTE]
> Si el programa no se ejecuta con este comando, pruebe a ejecutarlo con: ```python Ejercicio#3_FiltroIntro_SalamancaDante.py```

#### -- Lógica del programa --

En la *línea 2* se empieza por inicializar un bucle **for** que recorra los números enteros desde 0 hasta 680 (sin incluir este último), verificando en cada iteración si / **if** *i* cumple la condición dada (*línea 3*). Si / **if** la condición se cumple, entonces el número se muestra / **print** en pantalla (*línea 4*), si no / **else**, el código continúa sin realizar más acciones hasta la próxima iteración del bucle (*línea 2*). Cuando *i* llega al valor de 679 el bucle termina y el programa finaliza.

<a name="EjerciciosFiltroEjercicio4"></a>

### Ejercicio #4: Mayor y menor de 10 números

#### -- Objetivo --

Crear un programa que tome diez números ingresados por el usuario y devuelva el mayor y el menor de dichos valores.

#### -- Correcta ejecución del archivo --

Una vez descargado el archivo titulado *"Ejercicio#4_FiltroIntro_SalamancaDante.py"*, se debe abrir una nueva terminal y acceder al directorio en el que esté alojado el archivo (a través del comando **cd**). Para empezar a correr el programa, estando en la ubicación correcta, se deberá ejecutar el comando: ```python3 Ejercicio#4_FiltroIntro_SalamancaDante.py```

> [!NOTE]
> Si el programa no se ejecuta con este comando, pruebe a ejecutarlo con: ```python Ejercicio#4_FiltroIntro_SalamancaDante.py```

#### -- Lógica del programa --

Este programa posee un nivel de complejidad un poco mayor a los anteriores. Su primicia básica es ir comparando los datos ingresados tan pronto se guardan en la memoria para evitar realizar grandes cadenas de si / **if** anidados (una solución poco eficiente y larga). Si inicia declarando dos variables que representarán el número mayor y menor en cada iteración del bucle que inicializaremos en la *línea 4* (*línea 2* / *línea 3*). En cada repetición del bucle se le pedirá al usuario un número, que siempre se alojará en la variable *x* (*línea 5* / *línea 6*).

Si / **if** es la primera vuelta del bucle (es decir, *i* es igual a 0), se reasignarán los valores de *xMax* y *xMin* como el valor ingresado *x* (esto para tener un punto de partida, a partir del cuál poder comparar los siguientes valores dados por el usuario; de lo contrario, *xMin* siempre sería negativo o 0, teniendo en cuenta que, al iniciarlo como 0, no va a haber número ingresado que sea menor a él, exceptuando los enteros negativos y, en caso de que el número menor ingresado sea mayor a 0, la variable *xMin* va a permanecer con el valor de 0) (*línea 7* / *línea 8* / *línea 9*); en caso de que el valor actual de *x* sea mayor al de *xMax*, este pasará a ser el nuevo *xMax* (*línea 10* / *línea 11*); y, finalmente, si el valor actual *x* es menor al de *xMin*, este pasará a ser el nuevo *xMin* (*línea 12* / *línea 13*).

Para finalizar, una vez completadas todas las iteraciones del bucle **for** (es decir, una vez *i* tome el valor de 9), el programa continúa y muestra / **print** el número mayor (*xMax*) y menor (*xMin*) de los dados por el usuario (*línea 14* / *línea 15*); luego termina el proceso.

<a name="EjerciciosFiltroEjercicio5"></a>

### Ejercicio #5: Número faltante en la serie

#### -- Objetivo --

Crear un programa que imprima en pantalla la siguiente serie, además de su siguiente término: *1, 1, 2, -1, 1, -2*

#### -- Correcta ejecución del archivo --

Una vez descargado el archivo titulado *"Ejercicio#5_FiltroIntro_SalamancaDante.py"*, se debe abrir una nueva terminal y acceder al directorio en el que esté alojado el archivo (a través del comando **cd**). Para empezar a correr el programa, estando en la ubicación correcta, se deberá ejecutar el comando: ```python3 Ejercicio#5_FiltroIntro_SalamancaDante.py```

> [!NOTE]
> Si el programa no se ejecuta con este comando, pruebe a ejecutarlo con: ```python Ejercicio#5_FiltroIntro_SalamancaDante.py```

#### -- Lógica del programa --

La serie dada tiene como base los números 1 y 1; partiendo de ahí, para hallar el tercer término se deben sumar los dos anteriores; para hallar el cuarto se deben restar los dos anteriores; para hallar el quinto se suman los dos anteriores; para el sexto, se restan; etc. Teniendo eso en cuenta, se inicializan dos variables llamadas *a* y *b* en 1 (*línea 2* / *línea 3*). Acto seguido se comienza un bucle **for** que irá hasta el séptimo término de la serie (es decir, se iterará 7 veces) (*línea 4*). En cada repetición se mostrará / **print** el valor de la variable *a* en pantalla (*línea 5*) y se verificará si / **if** nos encontramos en una iteración de índice par o impar (*línea 6* / *línea 8*): en el primer caso se asignará la suma de *a* y *b* a una tercera variable *c* (*línea 7*); en el segundo caso se asigna la resta de *a* y *b* a la variable *c* (*línea 9*). Finalmente, sin importar el índice de la iteración actual, el valor de *b* pasa a asignarse a la variable *a* y el valor de *c* pasa a asignarse a la variable *b* (*línea 10* / *línea 11*).

<a name="EjerciciosFiltroEjercicio6"></a>

### Ejercicio #6: Empresa ACME

#### -- Objetivo --

La empresa ACME desea calcular el valor de la nómina de *N* empleados (estos *N* empleados son ingresados por el usuario), tanto el sueldo bruto como el sueldo neto. El sueldo bruto se calcula a partir del valor de la hora y la cantidad de horas trabajadas. A esto se le descuenta el valor de la EPS que es el 4%, el valor de la pensión que es el 4%. El sueldo neto es el sueldo bruto menos los descuentos. Por cada empleado se quiere mostrar, el valor del sueldo bruto, cada uno de los descuentos y el valor del sueldo neto. Para este ejercicio el valor de la hora es $20000.

Al final se debe mostrar una estadística con los totales de los salarios brutos, EPS, pensión y salarios netos. Luego mostrar el empleado que más gana en salario neto (nombre y salario neto), el empleado que menos gana en salario neto (nombre y salario neto) y los promedios de sueldos brutos y sueldos netos.

#### -- Correcta ejecución del archivo --

Una vez descargado el archivo titulado *"Ejercicio#6_FiltroIntro_SalamancaDante.py"*, se debe abrir una nueva terminal y acceder al directorio en el que esté alojado el archivo (a través del comando **cd**). Para empezar a correr el programa, estando en la ubicación correcta, se deberá ejecutar el comando: ```python3 Ejercicio#6_FiltroIntro_SalamancaDante.py```

> [!NOTE]
> Si el programa no se ejecuta con este comando, pruebe a ejecutarlo con: ```python Ejercicio#6_FiltroIntro_SalamancaDante.py```

#### -- Lógica del programa --

En primer lugar, se declaran las variables que alojarán los totales (*línea 2* / *línea 3* / *línea 4*). Justo entonces se le pide al usuario / **input** la cantidad de empleados que trabajan en la empresa (*N*) (*línea 5* / *línea 6*), para luego usar dicha variable como tope para el bucle **for** iniciado en la *línea 7*.

En cada iteración del bucle se le pide al usuario que ingrese el nombre del empleado, las horas trabajadas y se calcula el sueldo bruto y neto a través de la multiplicación de las horas trabajadas por 20000 (es decir, el valor de la hora) y la resta del descuento (el 4% del sueldo bruto) por dos (dado que son dos descuentos que valen exactamente lo mismo), respectivamente (*línea 8* a la *línea 14*).

Tras calcular estos datos, se le añade cada uno a su respectivo total mediante el uso del operador de asignación **+=** (*línea 15* / *línea 16* / *línea 17*). En las siguientes 6 líneas (*línea 18* a la *línea 23*) se muestran / **print** los datos recaudados recién, en pantalla. Siguiendo la misma lógica del Ejercicio #4 (*"Mayor y menor de 10 números"*), se halla el sueldo neto mayor, con el nombre de su correspondiente empleado y el menor: si / **if** es la primera iteración del **for** se les asigna al sueldo mayor (*sueldoMax*) y a su respectivo nombre (*nombreMax*) y al sueldo menor (*sueldoMin*) y a su respectivo nombre (*nombreMin*), los valores que tengan el nombre y el sueldo neto en ese momento (*nombre* / *sueldoNeto*) (*línea 24* a la *línea 28*); si / **if** el sueldo neto es mayor al sueldo mayor, entonces será el nuevo mayor (*línea 29* / *línea 30* / *línea 31*); y si / **if** el sueldo neto es menor que el sueldo menor, este será el nuevo menor (*línea 32* / *línea 33* / *línea 34*).

Finalmente se calculan los promedios de salarios brutos y netos (*línea 35* / *línea 36*), se muestran / **print** los totales de salarios brutos, netos y descuentos (EPS y pensión) (*línea 37* a la *línea 41*), el empleado que más gana con el correspondiente salario neto (*línea 43* / *línea 44*), el empleado que menos gana con su salario neto (*línea 46* / *línea 47*) y los promedios de brutos y netos (*línea 49* / *línea 50*).

<a name="EjerciciosFiltroEjercicio7"></a>

### Ejercicio #7: Números amigos

#### -- Objetivo --

Mostrar en pantalla si dos números enteros positivos n1 y n2 son amigos. Los números amigos son pares de números enteros positivos en los cuales la suma de los divisores propios de cada número es igual al otro número. En otras palabras, dos números amigos cumplen la condición de que la suma de los divisores propios de uno de ellos es igual al otro número, y viceversa. Por ejemplo, el par de números (220, 284) es un par de números amigos. Los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110. Si sumamos estos números, obtenemos 284, que es el segundo número del par. Por otro lado, los divisores propios de 284 son 1, 2, 4, 71 y 142, y si los sumamos, obtenemos 220, que es el primer número del par.

#### -- Correcta ejecución del archivo --

Una vez descargado el archivo titulado *"Ejercicio#7_FiltroIntro_SalamancaDante.py"*, se debe abrir una nueva terminal y acceder al directorio en el que esté alojado el archivo (a través del comando **cd**). Para empezar a correr el programa, estando en la ubicación correcta, se deberá ejecutar el comando: ```python3 Ejercicio#7_FiltroIntro_SalamancaDante.py```

> [!NOTE]
> Si el programa no se ejecuta con este comando, pruebe a ejecutarlo con: ```python Ejercicio#7_FiltroIntro_SalamancaDante.py```

#### -- Lógica del programa --

Para empezar, el programa le solicita al usuario dos números para checar si son amigos o no (*n1* / *n2*) (*línea 2* / *línea 3* / *línea 4*) e inicializa dos variables que representarán la suma de los divisores de *n1* y *n2*, respectivamente *sum1* y *sum2* (*línea 5* / *línea 6*). En los siguientes bucles, se realiza una revisión a través de todos los números desde 1 hasta *n1* (*línea 7*) y desde 1 hasta *n2* (*línea 10*), identificando aquellos números que puedan dividir, sin dar residuo, a *n1* (*línea 8*) y a *n2* (*línea 11*) y añadiéndolos a las variables declaradas en las *línea 5* / *línea 6* (*línea 9* / *línea 12*). Una vez finalizados ambos bucles, si / **if** la suma de los divisores de *n1* es igual a *n2* y / **and** la suma de los divisores de *n2* es igual a *n1*, entonces se imprimirá en pantalla / **print** el mensaje *"Los números son amigos..."* (*línea 13* / *línea 14*); caso contrario / **else**, se imprimirá / **print** el mensaje  *"Los números no son amigos..."* (*línea 15* / *línea 16*)

<a name="PythonWorkshop"></a>

## Python Workshop (1-5)

En este apartado se realizaron 5 de los 11 ejercicios que compusieron el taller de python *"Python Workshop"*, aplicando algunas funciones más avanzadas de este lenguaje. Aquí se encontrarán actividades que involucraron cálculos combinados (con operadores aritméticos y lógicos), bucles **for** y **while**, además de un más profundo acercamiento a los cuatro tipos de funciones, la importación de librerías como **random**, el manejo de arreglos, verificaciones con bucles **while** y métodos de cadenas.

<a name="PythonWorkshopEjercicio1"></a>

### Ejercicio 1: Conversor de temperatura

#### -- Objetivo --

Crear un programa que, a través de una función, pueda convertir grados Celsius a Fahrenheit y viceversa.

#### -- Correcta ejecución del archivo --

Una vez descargado el archivo titulado *"Ejercicio1_SalamancaDante.py"*, se debe abrir una nueva terminal y acceder al directorio en el que esté alojado el archivo (a través del comando **cd**). Para empezar a correr el programa, estando en la ubicación correcta, se deberá ejecutar el comando: ```python3 Ejercicio1_SalamancaDante.py```

> [!NOTE]
> Si el programa no se ejecuta con este comando, pruebe a ejecutarlo con: ```python Ejercicio1_SalamancaDante.py```

#### -- Lógica del programa --

En una primera instancia, se crea la función que convierta de Celsius a Fahrenheit (*línea 2*), aplicando la metodología del desempaquetamiento: el primer valor del arreglo se alojará en la variable *f* (*línea 3*)

<a name="PythonWorkshopEjercicio2"></a>
<a name="PythonWorkshopEjercicio3"></a>
<a name="PythonWorkshopEjercicio4"></a>
<a name="PythonWorkshopEjercicio5"></a>
<a name="Sección15"></a>
<a name="Sección16"></a>
