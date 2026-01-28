# Week 5: Inner Products

*8 problems*

---

## Problem Q2-P02

**Week 5** | **Inner Products**

Suppose ${\mathcal S} = \{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ is an orthonormal set in an inner product space $V$. Which of the following must be true?

**Choices:**
- (A) Any linear combination $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3$ has length $\sqrt{c_1^2 + c_2^2 + c_3^2}$
- (B) The vectors ${\mathcal S}$ automatically form a basis for $V$
- (C) The sum $\mathbf{v}_1 + \mathbf{v}_2 + \mathbf{v}_3$ is a unit vector
- (D) The matrix with columns $[\mathbf{v}_1 \mid \mathbf{v}_2 \mid \mathbf{v}_3]$ has determinant $\pm 1$
- (E) None of the above

<details>
<summary>Show Answer</summary>

**Correct: (None)**

For an orthonormal set $\mathcal{S} = \{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$:

$$\left\|c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3\right\|^2 = \sum_{i,j} c_ic_j\langle\mathbf{v}_i, \mathbf{v}_j\rangle$$

Since the vectors are orthonormal: $\langle\mathbf{v}_i, \mathbf{v}_j\rangle = \delta_{ij}$

Therefore: $\|c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3\|^2 = c_1^2 + c_2^2 + c_3^2$

Why other options are wrong:
\begin{itemize}
\item (B): They span a 3D subspace but $V$ could be larger
\item (C): $\|\mathbf{v}_1 + \mathbf{v}_2 + \mathbf{v}_3\|^2 = 1 + 1 + 1 = 3 \neq 1$
\item (D): Only true if we can form a matrix (requires $V = \mathbb{R}^3$)
\end{itemize}

**Partial Credit:**
- (D) True if $V$ is 3-dimensional and we can form a matrix

</details>

---

## Problem Q2-P03

**Week 5** | **Inner Products**

Consider the following statements about the vector space of quadratic polynomials $\mathcal{P}_2$:

I. We can determine whether $\{x, 1+x^2, 1+x+x^2\}$ is a basis 

II. We can argue that $x$ and $x^2$ are orthogonal

III. We can determine the dimension of the subspace spanned by $\{1+x, x+x^2, 1+x^2\}$

Which statements are true {\bf without} specifying an inner product on $\mathcal{P}_2$?

**Choices:**
- (A) I only
- (B) II only
- (C) I and III only
- (D) II and III only
- (E) I, II, and III

<details>
<summary>Show Answer</summary>

**Correct: (None)**

\begin{itemize}
\item \textbf{Statement I (TRUE):} Checking if vectors form a basis only requires:
  \begin{itemize}
  \item Linear independence (solve $c_1(x) + c_2(1+x^2) + c_3(1+x+x^2) = 0$)
  \item Spanning (verify we get all of $\mathcal{P}_2$)
  \item These are purely algebraic operations
  \end{itemize}
\item \textbf{Statement II (FALSE):} Orthogonality requires computing $\langle x, x^2 \rangle$, which needs an inner product definition
\item \textbf{Statement III (TRUE):} Finding dimension only requires checking linear independence via row reduction
\end{itemize}

**Key Insight:** Geometric concepts (angles, orthogonality) need inner products; algebraic concepts (independence, dimension) don't.

**Partial Credit:**
- (A) Recognizes basis checking doesn't need inner product

</details>

---

## Problem Q2-P09

**Week 5** | **Inner Products**

Let $V$ be a 4-dimensional inner product space with orthonormal basis $B = \{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3, \mathbf{v}_4\}$. 
For the vector $\mathbf{w} = 3\mathbf{v}_1 - 2\mathbf{v}_2 + \mathbf{v}_3 - 4\mathbf{v}_4$, which expression gives $\|\mathbf{w}\|^2$?

**Choices:**
- (A) $3^2 + (-2)^2 + 1^2 + (-4)^2 = 30$
- (B) $3 + 2 + 1 + 4 = 10$
- (C) $|3| + |-2| + |1| + |-4| = 10$
- (D) $(3 - 2 + 1 - 4)^2 = 4$
- (E) $(|3| + |-2| + |1| + |-4|)^2 = 100$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

For $\mathbf{w} = 3\mathbf{v}_1 - 2\mathbf{v}_2 + \mathbf{v}_3 - 4\mathbf{v}_4$ with orthonormal basis $B$:

$$\|\mathbf{w}\|^2 = \langle\mathbf{w}, \mathbf{w}\rangle$$

Using orthonormality ($\langle\mathbf{v}_i, \mathbf{v}_j\rangle = \delta_{ij}$):
$$\|\mathbf{w}\|^2 = 3^2\|\mathbf{v}_1\|^2 + (-2)^2\|\mathbf{v}_2\|^2 + 1^2\|\mathbf{v}_3\|^2 + (-4)^2\|\mathbf{v}_4\|^2$$
$$= 9 + 4 + 1 + 16 = 30$$

**Key Insight:** With orthonormal bases, the norm squared equals the sum of squared coefficients.

</details>

---

## Problem Q2-P11

**Week 5** | **Inner Products**

Let $Q$ be an $n \times n$ orthogonal matrix. Which of the following statements is false?

**Choices:**
- (A) $Q$ preserves dot products
- (B) The columns of $Q$ form an orthonormal basis for $\mathbb{R}^n$
- (C) The matrix $Q^T$ is also orthogonal
- (D) All entries of $Q$ must satisfy $|q_{ij}| \leq 1$
- (E) None of the above statements is false

<details>
<summary>Show Answer</summary>

**Correct: (None)**

For an orthogonal matrix $Q$ ($Q^TQ = I$):
\begin{itemize}
\item \textbf{(A) TRUE:} $\langle Qx, Qy \rangle = (Qx)^T(Qy) = x^TQ^TQy = x^Ty = \langle x, y \rangle$
\item \textbf{(B) TRUE:} Columns are orthonormal by definition
\item \textbf{(C) TRUE:} $(Q^T)^TQ^T = QQ^T = I$, so $Q^T$ is orthogonal
\item \textbf{(D) TRUE:} Each column has unit norm, so $|q_{ij}| \leq 1$ for all entries
\end{itemize}

All statements are true!

</details>

---

## Problem Q2-P12

**Week 5** | **Inner Products**

Consider the vector space $C[0,1]$ of continuous functions on $[0,1]$ with the inner product $\langle f, g \rangle = \int_0^1 e^x\,f(x)g(x)\,dx$.
Which of the following statements about this inner product is TRUE?

**Choices:**
- (A) This is not a valid inner product and all choices below are invalid
- (B) The constant function $f(x) = 1$ has norm $\|f\| = e$
- (C) The functions $\sin(x)$ and $\cos(x)$ are orthogonal with respect to this inner product
- (D) The norm induced by this inner product is $\|f\| = \sqrt{\int_0^1 f(x)^2 e^x\,dx}$
- (E) None of the above: all above statements are false

<details>
<summary>Show Answer</summary>

**Correct: (None)**

Given the weighted inner product $\langle f, g \rangle = \int_0^1 e^x f(x)g(x) dx$:

The induced norm is:
$$\|f\| = \sqrt{\langle f, f \rangle} = \sqrt{\int_0^1 e^x f(x)f(x) dx} = \sqrt{\int_0^1 f(x)^2 e^x dx}$$

Why others are wrong:
\begin{itemize}
\item (A): This IS a valid inner product (weight $e^x > 0$)
\item (B): $\|1\|^2 = \int_0^1 e^x dx = e - 1$, so $\|1\| = \sqrt{e-1} \neq e$
\item (C): Orthogonality depends on the specific inner product
\end{itemize}

</details>

---

## Problem Q2-P13

**Week 5** | **Inner Products**

Let $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ be nonzero vectors with angle $\theta$ between them. 
If we define $\mathbf{w} = 2\mathbf{u} - 3\mathbf{v}$, which expression gives the cosine of the angle between $\mathbf{u}$ and $\mathbf{w}$?

**Choices:**
- (A) $\cos\theta$ because scaling does not change angles
- (B) $\displaystyle \frac{2\|\mathbf{u}\|^2 - 3\|\mathbf{v}\|^2}{2\|\mathbf{u}\| \cdot \|\mathbf{w}\|}$
- (C) $\displaystyle \frac{2 - 3\cos\theta}{\sqrt{4 + 9 - 12\cos\theta}} \cdot \frac{\|\mathbf{u}\|}{\|\mathbf{v}\|}$
- (D) $\displaystyle \frac{2\|\mathbf{u}\|^2 - 3\langle\mathbf{u},\mathbf{v}\rangle}{\|\mathbf{u}\| \cdot \|\mathbf{w}\|}$
- (E) $2 - 3\cos\theta$ after normalizing both vectors

<details>
<summary>Show Answer</summary>

**Correct: (None)**

The cosine of the angle between $\mathbf{u}$ and $\mathbf{w} = 2\mathbf{u} - 3\mathbf{v}$ is:

$$\cos\phi = \frac{\langle\mathbf{u}, \mathbf{w}\rangle}{\|\mathbf{u}\|\|\mathbf{w}\|} = \frac{\langle\mathbf{u}, 2\mathbf{u} - 3\mathbf{v}\rangle}{\|\mathbf{u}\|\|\mathbf{w}\|}$$

Computing the numerator:
$$\langle\mathbf{u}, 2\mathbf{u} - 3\mathbf{v}\rangle = 2\langle\mathbf{u}, \mathbf{u}\rangle - 3\langle\mathbf{u}, \mathbf{v}\rangle = 2\|\mathbf{u}\|^2 - 3\langle\mathbf{u}, \mathbf{v}\rangle$$

**Partial Credit:**
- (C) Attempts correct approach but incorrectly simplifies

**Watch Out:**
- Don't confuse norms with inner products in the numerator!

</details>

---

## Problem Q2-P19

**Week 5** | **Inner Products**

Which of the following matrices is orthogonal? {\em Hint:} be strategic and do not do {\em all} the computations...

**Choices:**
- (A) $Q_1 = \begin{bmatrix} 2/3 & 2/3 & 1/3 \\ -2/3 & 1/3 & 2/3 \\ 1/3 & -2/3 & 2/3 \end{bmatrix}$
- (B) $Q_2 = \begin{bmatrix} 1/\sqrt{3} & 1/\sqrt{2} & 1/\sqrt{6} \\ 1/\sqrt{3} & -1/\sqrt{2} & 1/\sqrt{6} \\ 1/\sqrt{3} & 0 & -2/\sqrt{6} \end{bmatrix}$
- (C) $Q_3 = \begin{bmatrix} 1/\sqrt{2} & 1/\sqrt{3} & 1/\sqrt{6} \\ 0 & 1/\sqrt{3} & -2/\sqrt{6} \\ 1/\sqrt{2} & -1/\sqrt{3} & 1/\sqrt{6} \end{bmatrix}$
- (D) $Q_4 = \begin{bmatrix} 1/2 & 1/2 & 1/\sqrt{2} \\ 1/2 & 1/2 & -1/\sqrt{2} \\ -1/\sqrt{2} & 1/\sqrt{2} & 0 \end{bmatrix}$
- (E) None of the above is orthogonal.

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q2-P22

**Week 5** | **Inner Products**

Let $D: \mathcal{P}_3 \to \mathcal{P}_2$ be the differentiation operator on polynomials, where $D(p) = p'$. 
Consider the inner product $\langle f, g \rangle = \int_0^1 f(x)g(x)dx$ on both $\mathcal{P}_3$ and $\mathcal{P}_2$. 
What must be true of the adjoint $D^*: \mathcal{P}_2 \to \mathcal{P}_3$?

**Choices:**
- (A) $D^*$ must map each polynomial to its antiderivative
- (B) $D^* \circ D = I$ where $I$ is the identity
- (C) $D^*$ is integration by parts
- (D) $D \circ D^* = I$ where $I$ is the identity
- (E) For all $p \in \mathcal{P}_3$ and $q \in \mathcal{P}_2$: $\int_0^1 p'(x)q(x)dx = \int_0^1 p(x)(D^*(q))(x)dx$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

The defining property of the adjoint is:
$$\langle D(p), q \rangle = \langle p, D^*(q) \rangle$$

With our inner product $\langle f, g \rangle = \int_0^1 f(x)g(x)dx$:
$$\int_0^1 p'(x)q(x)dx = \int_0^1 p(x)(D^*(q))(x)dx$$

This is exactly what option (E) states.

Note: $D^*$ is NOT simply antidifferentiation due to boundary terms from integration by parts. The actual formula involves both antiderivatives and boundary corrections.

**Key Insight:** The adjoint relationship is the fundamental definition—everything else follows from it.

**Partial Credit:**
- (C) Related to integration by parts but vague

</details>

---
