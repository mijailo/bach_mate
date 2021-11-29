{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "39aecec4",
   "metadata": {},
   "source": [
    "# Cálculo de raíces cuadradas\n",
    "\n",
    "Utilizaremos el método de la sucesión convergente para calcular la raíz cuadrada de un número $a\\in\\mathbb{R}$ positivo:\n",
    "\n",
    "\\begin{gather}\n",
    " x_0 \\in \\mathbb{R}: \\; x_0^2\\approx a \\\\\n",
    " x_{n+1} = \\frac{1}{2}\\left( x_n + \\frac{a}{x_n} \\right)\\\\\n",
    " (\\text{Se sabe que}: \\lim_{n\\to\\infty} x_n = \\sqrt{a})\n",
    "\\end{gather}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a1ef6b7f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from fractions import Fraction as F"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "093f1a45",
   "metadata": {},
   "source": [
    "Este módulo es útil para hacer operaciones con fracciones."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "825d8d55",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Fraction(1, 2)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x=F(2,4) # 1/2\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6f8cc383",
   "metadata": {},
   "source": [
    "Una de sus gracias es que las expresa en forma irreducible.\n",
    "\n",
    "> **Nota**: Una fracción $\\frac{a}{b}$ es irreducible cuando $a$ y $b$ son primos relativos (es decir, el máximo común divisor de $a$ y $b$ es 1)."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e738b2ee",
   "metadata": {},
   "source": [
    "Además, podemos obtener la representación decimal (_aproximada_) de esas fracciones."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2350322b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "float(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "98471377",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.6666666666666666"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "float(F(2,3))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8306f6f9",
   "metadata": {},
   "source": [
    "Vamos a definir una función, de forma recursiva, que nos permita obtener el término $x_n$ del listado de números que converge a la raíz de $a$. Para ello, vamos a ejemplificar la definición y uso de las funciones en [`Python 3`](https://www.python.org/)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d910b6b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Vamos a hacer una función que, dados dos números, calcule su suma\n",
    "def raul(a,b): #El nombre de la función es arbitrario\n",
    "    return a+b\n",
    "\n",
    "raul(2,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "847bd9a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def memo(papitas,refresco): #También el nombre de los argumentos es arbitrario (aunque se prefiere algo que )\n",
    "    return papitas*refresco # todavía no haya sido utilizado).\n",
    "\n",
    "memo(5,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f814750e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def raiz(a,x0,n):\n",
    "    \"\"\"\n",
    "    a = número cuya raíz me interesa\n",
    "    x0 = aproximación inicial de la raíz de a (se recomienda un entero o fracción cuyo cuadrado sea casi a)\n",
    "    n = número natural para el que calcularemos x1, x2,..., xn\n",
    "    \"\"\"\n",
    "    y=x0\n",
    "    for i in range(n):\n",
    "        print(f'X({i})={y}\\n     ={float(y)}\\n')\n",
    "        y=F(1,2)*(y+F(a,y)) # Esto codifica la fórmula recursiva definida al inicio\n",
    "    print(f'X({n})={y}\\n     ={float(y)}')\n",
    "    return y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a9b0ad6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "X(0)=3\n",
      "     =3.0\n",
      "\n",
      "X(1)=19/6\n",
      "     =3.1666666666666665\n",
      "\n",
      "X(2)=721/228\n",
      "     =3.162280701754386\n",
      "\n",
      "X(3)=1039681/328776\n",
      "     =3.162277660169842\n",
      "\n",
      "X(4)=2161873163521/683644320912\n",
      "     =3.1622776601683795\n",
      "\n",
      "X(5)=9347391150304592810234881/2955904621546382351702304\n",
      "     =3.1622776601683795\n"
     ]
    }
   ],
   "source": [
    "y=raiz(10,3,5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "70bd6f57",
   "metadata": {},
   "source": [
    "La aproximación obtenida para la raíz de 10 es tal, que el cuadrado _se pasa de 10_ en:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "fa821408",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1/8737372131679261877757908894145308222766638908416\n"
     ]
    }
   ],
   "source": [
    "e=y**2-10\n",
    "print(e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e560cfda",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.1445088808502047e-49"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "float(e)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e96aca31",
   "metadata": {},
   "source": [
    "Este número está expresado en notación científica (computacionalmente):\n",
    "\n",
    "$$ \\text{1.1445088808502047e-49} = 1.1445088808502047 \\times 10^{-49} = \\\\\n",
    "0.00000000000000000000000000000000000000000000000011445088808502047\n",
    "$$\n",
    "\n",
    "> **Nota**: Lo más chiquito que una computadora puede procesar se llama [_épsilon de máquina_](https://en.wikipedia.org/wiki/Machine_epsilon)."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cabbc112",
   "metadata": {},
   "source": [
    "# Cuestionario\n",
    "\n",
    "En equipos, responder (utilizando los cuadernillos de `Jupyter`):\n",
    "\n",
    "1. ¿Cuál es la raíz de 9 a orden 3, 4 y 5 para la aproximación inicial $x_0=4$?\n",
    "2. ¿Qué pasa con la raíz de 25 a órdenes 2, 3 y 4 cuando $x_0=5$?\n",
    "3. ¿Cuál es el error del cuadrado de $x_3$ y $x_5$ para la raíz de 11 cuando $x_0=5$?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a8d57eb6",
   "metadata": {},
   "source": [
    "## <font color='crimson'> Participantes </font>\n",
    "\n",
    "* Angejolie González\n",
    "* José Luis Carrizosa\n",
    "* Omar Santiago Martínez González\n",
    "* Aaron Fernando Del Valle Reyes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cea67b03",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
