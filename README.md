<h1>📘 Taller del parcial</h1>

<p>
Este repositorio contiene el desarrollo de el 
<strong>taller del parcial </strong> sobre conceptos de 
<b>encapsulación, propiedades, herencia y diseño con POO en Python</b>.
</p>

<strong>Solución</strong></p>

<hr>

<p><strong>Solución completa</strong></p>

<hr>

<h2>Parte A. Conceptos y lectura de código</h2>

<h3>1. Selección múltiple</h3>
<pre><code>class A:
    x = 1
    _y = 2
    __z = 3
a = A()
</code></pre>

<p><strong>Accesibles desde a:</strong> A) a.x ✅, B) a._y ✅, D) a._A__z ✅<br>
C) a.__z ❌ (no existe directamente por name mangling)</p>

<hr>

<h3>2. Salida del programa</h3>
<pre><code>class A:
    def __init__(self):
        self.__secret = 42
a = A()
print(hasattr(a, '__secret'), hasattr(a, '_A__secret'))
</code></pre>

<p><strong>Salida:</strong> <code>False True</code><br>
Explicación: el atributo se renombra a <code>_A__secret</code> por name mangling.</p>

<hr>

<h3>3. Verdadero / Falso</h3>
<p>
a) ❌ El prefijo <code>_</code> no impide el acceso, solo es una convención.<br>
b) ❌ El prefijo <code>__</code> no lo hace inaccesible, solo lo renombra (name mangling).<br>
c) ✅ Sí, el name mangling depende del nombre de la clase.
</p>

<hr>

<h3>4. Lectura de código</h3>
<pre><code>class Base:
    def __init__(self):
        self._token = "abc"
class Sub(Base):
    def reveal(self):
        return self._token
print(Sub().reveal())
</code></pre>

<p><strong>Salida:</strong> <code>abc</code><br>
No hay error porque el guion bajo es una convención, no una restricción real.</p>

<hr>

<h3>5. Name mangling en herencia</h3>
<pre><code>class Base:
    def __init__(self):
        self.__v = 1

class Sub(Base):
    def __init__(self):
        super().__init__()
        self.__v = 2
    def show(self):
        return (self.__v, self._Base__v)

print(Sub().show())
</code></pre>

<p><strong>Salida:</strong> <code>(2, 1)</code></p>

<hr>

<h3>6. Identifica el error</h3>
<pre><code>class Caja:
    __slots__ = ('x',)
c = Caja()
c.x = 10
c.y = 20
</code></pre>

<p><strong>Error:</strong> <code>AttributeError: 'Caja' object has no attribute 'y'</code><br>
Porque <code>__slots__</code> limita los atributos a los definidos (solo “x”).</p>

<hr>

<h3>7. Atributo protegido</h3>
<pre><code>class B:
    def __init__(self):
        self._valor = 99
</code></pre>

<p>El atributo protegido por convención es <code>_valor</code>.</p>

<hr>

<h3>8. Métodos “privados”</h3>
<pre><code>class M:
    def __init__(self):
        self._state = 0
    def _step(self):
        self._state += 1
        return self._state
    def __tick(self):
        return self._step()

m = M()
print(hasattr(m, '_step'), hasattr(m, '__tick'), hasattr(m, '_M__tick'))
</code></pre>

<p><strong>Salida:</strong> <code>True False True</code></p>

<hr>

<h3>9. Acceso a atributos privados</h3>
<pre><code>class S:
    def __init__(self):
        self.__data = [1, 2]
    def size(self):
        return len(self.__data)

s = S()
print(s._S__data)
</code></pre>

<p>Línea correcta: <code>print(s._S__data)</code></p>

<hr>

<h3>10. Comprensión de dir y mangling</h3>
<pre><code>class D:
    def __init__(self):
        self.__a = 1
        self._b = 2
        self.c = 3
d = D()
names = [n for n in dir(d) if 'a' in n]
print(names)
</code></pre>

<p><strong>Aparece:</strong> <code>_D__a</code><br>
El atributo privado se renombra internamente.</p>

<hr>

<h2>Parte B. Encapsulación con @property</h2>

<h3>11. Propiedad con validación</h3>
<pre><code>class Cuenta:
    def __init__(self, saldo):
        self._saldo = 0
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        if value &lt; 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = value
</code></pre>

<hr>

<h3>12. Propiedad de solo lectura</h3>
<pre><code>class Termometro:
    def __init__(self, temperatura_c):
        self._c = float(temperatura_c)

    @property
    def temperatura_f(self):
        return self._c * 9/5 + 32
</code></pre>

<hr>

<h3>13. Invariante con tipo</h3>
<pre><code>class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str):
            raise TypeError("El nombre debe ser una cadena")
        self._nombre = value
</code></pre>

<hr>

<h3>14. Vista inmutable</h3>
<pre><code>class Registro:
    def __init__(self):
        self.__items = []
    def add(self, x):
        self.__items.append(x)

    @property
    def items(self):
        return tuple(self.__items)
</code></pre>

<hr>

<h2>Parte C. Diseño y refactor</h2>

<h3>15. Validar con @property</h3>
<pre><code>class Motor:
    def __init__(self, velocidad):
        self.velocidad = velocidad

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, value):
        if not 0 &lt;= value &lt;= 200:
            raise ValueError("La velocidad debe estar entre 0 y 200")
        self._velocidad = value
</code></pre>

<hr>

<h3>16. Cuándo usar _ o __</h3>
<p>
Usa <code>_atributo</code> cuando quieres marcar que es “interno” pero accesible por subclases o usuarios avanzados.<br>
Usa <code>__atributo</code> cuando quieres evitar colisiones en herencia o reforzar la privacidad dentro de la clase.
</p>

<hr>

<h3>17. Fuga de encapsulación</h3>
<pre><code>class Buffer:
    def __init__(self, data):
        self._data = list(data)
    def get_data(self):
        return list(self._data)  # corregido
</code></pre>

<p>Antes devolvía la lista interna directa, lo que permitía modificarla desde fuera.</p>

<hr>

<h3>18. Herencia y mangling</h3>
<pre><code>class A:
    def __init__(self):
        self.__x = 1

class B(A):
    def get(self):
        return self._A__x  # corregido
</code></pre>

<p>Falla porque <code>self.__x</code> en B se convierte en <code>_B__x</code>, no coincide con <code>_A__x</code>.</p>

<hr>

<h3>19. Composición y fachada</h3>
<pre><code>class _Repositorio:
    def __init__(self):
        self._datos = {}
    def guardar(self, k, v):
        self._datos[k] = v
    def _dump(self):
        return dict(self._datos)

class Servicio:
    def __init__(self):
        self.__repo = _Repositorio()

    def guardar(self, k, v):
        return self.__repo.guardar(k, v)
</code></pre>

<p>Solo se expone el método seguro <code>guardar()</code>.</p>

<hr>

<h3>20. Mini-Kata: ContadorSeguro</h3>
<pre><code>class ContadorSeguro:
    def __init__(self):
        self._n = 0

    def inc(self):
        self._n += 1
        self.__log()

    @property
    def n(self):
        return self._n

    def __log(self):
        print("tick")

# Uso:
c = ContadorSeguro()
c.inc()
c.inc()
print("Valor final:", c.n)
</code></pre>

<p><strong>Salida:</strong><br>
<code>tick<br>tick<br>Valor final: 2</code></p>

<p><em>“En Python la privacidad es una convención, no una obligación.”</em></p>

<hr>

<h2>Estructura del repositorio</h2>
<ul>
  <li><code>Taller.pdf</code> → Documento con las respuestas y puntos del taller</li>
  <li><code>PUNTOS/</code> → Carpeta con la solución de cada ejercicio en archivos <code>.py</code>.
    <ul>
      <li><code>punto1.py</code></li>
      <li><code>punto2.py</code></li>
      <li>...</li>
      <li><code>punto20.py</code></li>
    </ul>
  </li>
</ul>

<h2>Autor</h2>
<p>
Desarrollado por <strong>José Luis Cancelado Castro</strong> como parte del curso de 
<b>Programación Orientada a Objetos</b>.
</p>

