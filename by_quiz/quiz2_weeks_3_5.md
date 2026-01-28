# Quiz 2: Weeks 3-5

*24 problems*

## Week Breakdown
- Week 3 (Linear Transformations): 7 problems
- Week 4 (Bases & Coordinates): 9 problems
- Week 5 (Inner Products): 8 problems

---

## Problem Q2-P01

**Week 3** | **Linear Transformations**

Let $T: V \to W$ be a linear transformation between finite-dimensional vector spaces where $\dim(V) = 9$ and $\dim(W) = 4$. 
If the rank of $T$ is $3$, what is the dimension of the coimage $\text{coim}(T)$?

**Choices:**
- (A) 3
- (B) 4
- (C) 5
- (D) 7
- (E) Cannot be determined without additional information

<details>
<summary>Show Answer</summary>

**Correct: (None)**

The coimage is defined as $\text{coim}(T) = V/\ker(T)$.

Using the Rank-Nullity Theorem:
\begin{itemize}
\item $\dim(V) = \text{rank}(T) + \dim(\ker(T))$
\item $9 = 3 + \dim(\ker(T))$
\item Therefore: $\dim(\ker(T)) = 6$
\end{itemize}

The dimension of the coimage:
$$\dim(\text{coim}(T)) = \dim(V) - \dim(\ker(T)) = 9 - 6 = 3$$

**Key Insight:** The coimage "mods out" the kernel, so its dimension equals the rank.

</details>

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

## Problem Q2-P04

**Week 4** | **Bases & Coordinates**

Let $\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2, \mathbf{b}_3\}$ be a basis for $\mathbb{R}^3$, 
and suppose the coordinate vector of $\mathbf{v} \in \mathbb{R}^3$ with respect to $\mathcal{B}$ is 
$[\mathbf{v}]_{\mathcal B} = \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}$.
If we form a new basis ${\mathcal C} = \{2\mathbf{b}_1, \mathbf{b}_2, \mathbf{b}_3\}$, what is the coordinate vector $[\mathbf{v}]_{\mathcal C}$?

**Choices:**
- (A) $\begin{pmatrix} 4 \\ -1 \\ 3 \end{pmatrix}$   :
- (B) $\begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}$   :
- (C) $\begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}$   :
- (D) $\begin{pmatrix} 2 \\ -2 \\ 6 \end{pmatrix}$   :
- (E) $\begin{pmatrix} 1 \\ -\frac{1}{2} \\ \frac{3}{2} \end{pmatrix}$
\end{center}

<details>
<summary>Show Answer</summary>

**Correct: (None)**

Given: $\mathbf{v} = 2\mathbf{b}_1 - \mathbf{b}_2 + 3\mathbf{b}_3$

New basis: $\mathcal{C} = \{2\mathbf{b}_1, \mathbf{b}_2, \mathbf{b}_3\}$

We need to express $\mathbf{v}$ in terms of $\mathcal{C}$:
$$\mathbf{v} = 2\mathbf{b}_1 - \mathbf{b}_2 + 3\mathbf{b}_3 = 1 \cdot (2\mathbf{b}_1) + (-1) \cdot \mathbf{b}_2 + 3 \cdot \mathbf{b}_3$$

Therefore: $[\mathbf{v}]_{\mathcal{C}} = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}$

**Watch Out:**
- The first coordinate changes because we're using $2\mathbf{b}_1$ as our new first basis vector.

</details>

---

## Problem Q2-P05

**Week 4** | **Bases & Coordinates**

Which of the following properties is not necessarily preserved under similarity? (Recall, square matrices $A$ and $B$ are similar if $B = P^{-1}AP$ for some $P$).

**Choices:**
- (A) The rank of the matrix
- (B) The dimension of the kernel
- (C) The determinant
- (D) The column space
- (E) All of the above are preserved

<details>
<summary>Show Answer</summary>

**Correct: (None)**

Similar matrices $B = P^{-1}AP$ preserve:
\begin{itemize}
\item Rank (dimension of image)
\item Nullity (dimension of kernel)
\item Determinant: $\det(B) = \det(P^{-1})\det(A)\det(P) = \det(A)$
\item Trace, eigenvalues, characteristic polynomial
\end{itemize}

NOT preserved:
\begin{itemize}
\item Column space: Changes with basis transformation
\item Row space: Also changes
\item Specific eigenvectors (though eigenspaces are preserved)
\end{itemize}

Example: $I$ and $P^{-1}IP = I$ are similar but may have different column spaces if viewed as subspaces of $\mathbb{R}^n$ with $P \neq I$.

**Partial Credit:**
- (E) Recognizes that most properties are preserved

</details>

---

## Problem Q2-P06

**Week 3** | **Linear Transformations**

Let $T: V \to V$ be a finite-dimensional linear transformation. If we change from basis $\mathcal{B}$ to basis $\mathcal{C}$, which statement about the matrix representations $[T]_{\mathcal{B}}$ and $[T]_{\mathcal{C}}$ must be true?

**Choices:**
- (A) They have the same column vectors
- (B) They have the same rank
- (C) They have the same entries on the main diagonal
- (D) They represent different linear transformations
- (E) They are equal if $\mathcal{B}$ and $\mathcal{C}$ share at least one basis vector

<details>
<summary>Show Answer</summary>

**Correct: (None)**

$[T]_{\mathcal{B}}$ and $[T]_{\mathcal{C}}$ are similar matrices related by:
$$[T]_{\mathcal{C}} = P^{-1}[T]_{\mathcal{B}}P$$

where $P$ is the change of basis matrix. Similar matrices preserve:
\begin{itemize}
\item Rank (both equal $\dim(\text{im}(T))$)
\item Determinant
\item Trace
\item Eigenvalues
\end{itemize}

They do NOT have:
\begin{itemize}
\item Same column vectors (change with basis)
\item Same diagonal entries (except trace is preserved)
\item They represent the SAME transformation (not different ones)
\end{itemize}

</details>

---

## Problem Q2-P07

**Week 3** | **Linear Transformations**

Let $T: \mathbb{R}^5 \to \mathbb{R}^5$ be a linear transformation. 
Given that $\dim(\ker(T)) = 2$ and $\dim(\text{im}(T)) = 3$, which statement about the cokernel $\text{coker}(T)$ must be true?

**Choices:**
- (A) $\dim(\text{coker}(T)) = 2$ and it is a subspace of $\mathbb{R}^5$
- (B) $\dim(\text{coker}(T)) = 2$ and it is isomorphic to $\ker(T)$
- (C) $\dim(\text{coker}(T)) = 2$ but it need not be isomorphic to $\ker(T)$
- (D) $\dim(\text{coker}(T)) = 2$ and it is isomorphic to $\text{im}(T)$
- (E) $\dim(\text{coker}(T)) = 2$ and it is isomorphic to $\text{coim}(T)$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

The cokernel is $\text{coker}(T) = W/\text{im}(T) = \mathbb{R}^5/\text{im}(T)$.

Dimension calculation:
$$\dim(\text{coker}(T)) = \dim(W) - \dim(\text{im}(T)) = 5 - 3 = 2$$

While both $\ker(T)$ and $\text{coker}(T)$ have dimension 2:
\begin{itemize}
\item $\ker(T)$ is a subspace of the domain $\mathbb{R}^5$
\item $\text{coker}(T)$ is a quotient of the codomain $\mathbb{R}^5$
\item There's no natural isomorphism between them
\item They're abstractly isomorphic as 2D vector spaces but not canonically
\end{itemize}

**Partial Credit:**
- (A) Correct dimension but incomplete understanding

</details>

---

## Problem Q2-P08

**Week 4** | **Bases & Coordinates**

Let $A$ be a square matrix with QR decomposition $A = QR$.
Consider the matrix $B = Q^{-1}AQ$ (similar to $A$ by its own $Q$ factor).
Which of the following equals $B$?

**Choices:**
- (A) $RQ^T$
- (B) $Q^TR^T$
- (C) $QRQ^T$
- (D) $Q^TR$
- (E) $RQ$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

Given $A = QR$ where $Q$ is orthogonal (so $Q^{-1} = Q^T$):

$$B = Q^{-1}AQ = Q^T(QR)Q$$

Simplifying:
$$B = (Q^TQ)RQ = IRQ = RQ$$

Note: This is the key step in the QR algorithm for eigenvalue computation!hich we will learn later!

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

## Problem Q2-P10

**Week 4** | **Bases & Coordinates**

Let $A$ be a square matrix. After performing QR decomposition you compute $A = QR$.
Which statement about this QR decomposition must be true?

**Choices:**
- (A) The matrix $Q^TQ^{-1}$ is the identity matrix
- (B) The diagonal entries of $R$ are all positive
- (C) The columns of $Q$ form an orthonormal basis
- (D) The matrix $R$ is invertible
- (E) More than one statement above is true

<details>
<summary>Show Answer</summary>

**Correct: (None)**

In QR decomposition:
\begin{itemize}
\item $Q$ has orthonormal columns by definition  
\item $R$ is upper triangular
\item Diagonal entries of $R$ can be negative (depends on algorithm)
\item $R$ is invertible only if $A$ has full rank
\item For orthogonal $Q$: $Q^TQ^{-1} = Q^T(Q^T) = (Q^T)^2 \neq I$ in general
\end{itemize}

Why option (A) is false: Since $Q^{-1} = Q^T$ for orthogonal matrices, we get $Q^TQ^{-1} = (Q^T)^2$, which is NOT the identity matrix unless $Q^T$ is an involution (rare special case).

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

## Problem Q2-P14

**Week 3** | **Linear Transformations**

Let $T: \mathbb{R}^4 \to \mathbb{R}^3$ be a linear transformation with $\text{rank}(T) = 2$. 
Consider the quotient space $\mathbb{R}^4/\ker(T)$ and the image $\text{im}(T)$. 
Which statement about the relationship between these spaces is true?

**Choices:**
- (A) They have the same dimension but are not isomorphic since one lives in $\mathbb{R}^4$ and the other in $\mathbb{R}^3$
- (B) They are isomorphic, and the isomorphism is induced by the transformation $T$ itself
- (C) The quotient space has dimension $3$ while the image has dimension $2$, so they cannot be isomorphic
- (D) They are the same space
- (E) The quotient space is undefined since $\ker(T)$ might not be a proper subspace

<details>
<summary>Show Answer</summary>

**Correct: (None)**

The FTLA states:
$$\mathbb{R}^4/\ker(T) = \text{coim} \cong \text{im}(T)$$

Both spaces have dimension 2:
\begin{itemize}
\item Quotient: $\dim(\mathbb{R}^4/\ker(T)) = 4 - \dim(\ker(T)) = 4 - 2 = 2$
\item Image: $\dim(\text{im}(T)) = \text{rank}(T) = 2$
\end{itemize}

The isomorphism is given by: $[\mathbf{v}]_{\ker(T)} \mapsto T(\mathbf{v})$

This map is well-defined and bijective by the theorem.

**Partial Credit:**
- (A) (small) Recognizes equal dimensions

</details>

---

## Problem Q2-P15

**Week 3** | **Linear Transformations**

Let $T: \mathbb{R}^3 \to \mathbb{R}^3$ be a linear transformation whose matrix representation in the standard Euclidean basis is $A$. 
Which condition is sufficient to guarantee that $T$ preserves all angles between vectors?

**Choices:**
- (A) $A^T = A$ (symmetric matrix)
- (B) $A^TA = I$ (orthogonal matrix)
- (C) $\det(A) = \pm 1$
- (D) All columns of $A$ have the same length
- (E) $A^T = -A$ (skew-symmetric matrix)

<details>
<summary>Show Answer</summary>

**Correct: (None)**

For angle preservation, we need:
$$\cos\theta' = \frac{\langle T\mathbf{u}, T\mathbf{v}\rangle}{\|T\mathbf{u}\|\|T\mathbf{v}\|} = \frac{\langle \mathbf{u}, \mathbf{v}\rangle}{\|\mathbf{u}\|\|\mathbf{v}\|} = \cos\theta$$

This happens if and only if $T$ preserves inner products:
$$\langle T\mathbf{u}, T\mathbf{v}\rangle = \langle \mathbf{u}, \mathbf{v}\rangle$$

For matrix $A$: $\langle A\mathbf{x}, A\mathbf{y}\rangle = \mathbf{x}^TA^TA\mathbf{y} = \mathbf{x}^T\mathbf{y}$ requires $A^TA = I$.

Why others fail:
\begin{itemize}
\item (A): Symmetric matrices don't preserve angles in general
\item (C): Necessary but not sufficient
\item (D): Equal column lengths don't ensure orthonormality
\item (E): Skew-symmetric matrices don't preserve angles
\end{itemize}

</details>

---

## Problem Q2-P16

**Week 4** | **Bases & Coordinates**

Consider the transformation $T: \mathbb{R}^n \to \mathbb{R}^n$ on the standard Euclidean $n$-space
given by $T(\mathbf{x}) = 5\mathbf{x}$ for all $\mathbf{x}$. Which geometric property does this transformation preserve?

**Choices:**
- (A) Distances between two vectors, since it scales uniformly
- (B) Inner products between vectors, since scaling is linear
- (C) Angles between vectors, since all vectors are scaled equally
- (D) Lengths of vectors, since it is a multiple of the identity $I$
- (E) None of the above geometric properties are preserved

<details>
<summary>Show Answer</summary>

**Correct: (None)**

For $T(\mathbf{x}) = 5\mathbf{x}$:

\begin{itemize}
\item Inner products: $\langle 5\mathbf{u}, 5\mathbf{v}\rangle = 25\langle\mathbf{u}, \mathbf{v}\rangle$ (scaled by 25)
\item Lengths: $\|5\mathbf{u}\| = 5\|\mathbf{u}\|$ (scaled by 5)
\item Distances: $\|5\mathbf{u} - 5\mathbf{v}\| = 5\|\mathbf{u} - \mathbf{v}\|$ (scaled by 5)
\item Angles: $\cos\theta' = \frac{25\langle\mathbf{u}, \mathbf{v}\rangle}{5\|\mathbf{u}\| \cdot 5\|\mathbf{v}\|} = \frac{\langle\mathbf{u}, \mathbf{v}\rangle}{\|\mathbf{u}\|\|\mathbf{v}\|} = \cos\theta$  
\end{itemize}

**Key Insight:** Uniform scaling preserves angles but not distances or inner products.

</details>

---

## Problem Q2-P17

**Week 3** | **Linear Transformations**

Let $T: V \to W$ be a linear transformation. Two vectors $\mathbf{u}, \mathbf{v} \in V$ represent the same equivalence class in the coimage 
$\text{coim}(T)$ if and only if:

**Choices:**
- (A) $\mathbf{u} - \mathbf{v} \in \text{coim}(T)$
- (B) $T(\mathbf{u} - \mathbf{v}) \in \text{im}(T)$
- (C) $\mathbf{u} = \mathbf{v}$
- (D) $T(\mathbf{u}) = T(\mathbf{v})$
- (E) $T(\mathbf{u})-T(\mathbf{v}) \in \text{im}(T)$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

Two vectors $\mathbf{u}, \mathbf{v}$ are in the same equivalence class of $\text{coim}(T) = V/\ker(T)$ if and only if:

$$\mathbf{u} - \mathbf{v} \in \ker(T)$$

This is equivalent to:
$$T(\mathbf{u} - \mathbf{v}) = \mathbf{0}$$
$$T(\mathbf{u}) = T(\mathbf{v})$$

Option (E) states $T(\mathbf{u}) - T(\mathbf{v}) \in \text{im}(T)$, which is always true but doesn't characterize equivalence.

**Partial Credit:**
- (E) True but trivially so, not the defining condition

</details>

---

## Problem Q2-P18

**Week 3** | **Linear Transformations**

For a linear transformation $T:V\to V$, which of the following requires an inner product on $V$?

**Choices:**
- (A) Determining if $T$ is invertible
- (B) Computing the adjoint $T^*$
- (C) Finding the kernel of $T:V\to V$
- (D) Computing a basis for the coimage of $T$
- (E) Constructing the matrix representation of $T$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

The adjoint $T^*$ is defined by the relation:
$$\langle T\mathbf{v}, \mathbf{w}\rangle = \langle\mathbf{v}, T^*\mathbf{w}\rangle$$

This definition explicitly requires an inner product.

Operations NOT requiring inner products:
\begin{itemize}
\item Invertibility: Check if $\ker(T) = \{\mathbf{0}\}$
\item Finding kernel: Solve $T\mathbf{v} = \mathbf{0}$
\item Coimage basis: Purely algebraic quotient construction
\item Matrix representation: Only needs choice of bases
\end{itemize}

**Partial Credit:**
- (E) Matrix representation is easier with inner product but doesn't require it

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

## Problem Q2-P20

**Week 4** | **Bases & Coordinates**

In a document retrieval system, documents are represented as vectors in $\mathbb{R}^{1000}$ 
where the $i^{th}$ coordinate counts the number of times the $i^{th}$ most common word in the dictionary appears in the document.
(For example, the 1st coordinate counts {\em ``the''}...) 
{\bf Fact:} The angle between documents $\mathbf{d}_1$ and $\mathbf{d}_2$ is $\theta_{1,2}=30^\circ$ (thirty degrees). 
If we create a new document by merging the two original docs and obtain $\mathbf{d}_3 = \mathbf{d}_1+\mathbf{d}_2$, 
what can you say about the angles $\theta_{1,3}$ between $\mathbf{d}_1$ and $\mathbf{d}_3$ and $\theta_{2,3}$ between $\mathbf{d}_2$ and $\mathbf{d}_3$?

**Choices:**
- (A) These angles are both $15^\circ$ (fifteen degrees)
- (B) At least one angle is strictly greater than $15^\circ$ (fifteen degrees)
- (C) These angles are both strictly less than $30^\circ$ (fifteen degrees)
- (D) These angles are both strictly greater than $15^\circ$ (fifteen degrees)
- (E) Nothing can be determined without knowing the original vector lengths

<details>
<summary>Show Answer</summary>

**Correct: (None)**

Given $\mathbf{d}_3 = \mathbf{d}_1 + \mathbf{d}_2$ with $\theta_{1,2} = 30°$:

By the parallelogram law, $\mathbf{d}_3$ lies in the interior of the angle between $\mathbf{d}_1$ and $\mathbf{d}_2$ (when viewed from origin).

Both angles $\theta_{1,3}$ and $\theta_{2,3}$ must be:
\begin{itemize}
\item Strictly less than $30°$ (the original angle)
\item Strictly greater than $0°$ (vectors point in same general direction)
\item Equal to $15°$ only if $\|\mathbf{d}_1\| = \|\mathbf{d}_2\|$
\end{itemize}

**Key Insight:** Vector addition creates a "weighted average" direction between the two vectors.

**Partial Credit:**
- (A) Might be exactly $15°$ in special cases
- (E) Can determine bounds without knowing lengths

</details>

---

## Problem Q2-P21

**Week 4** | **Bases & Coordinates**

Let $T: \mathcal{P}_2 \to \mathcal{P}_1$ be the differentiation operator defined by $T(p) = p'$. 
Consider two bases: $\mathcal{B} = \{1, x, x^2\}$ for $\mathcal{P}_2$ and $\mathcal{C} = \{1, x\}$ for $\mathcal{P}_1$.
Let $[T]_{\mathcal{B}}^{\mathcal{C}}$ denote the matrix of $T$ with respect to these bases.
Which statement about this matrix representation is true?

**Choices:**
- (A) The columns of $[T]_{\mathcal{B}}^{\mathcal{C}}$ are the coordinate vectors of $T(1), T(x), T(x^2)$ with respect to $\mathcal{C}$
- (B) The rows of $[T]_{\mathcal{B}}^{\mathcal{C}}$ represent how each basis vector in $\mathcal{B}$ transforms under $T$
- (C) The matrix $[T]_{\mathcal{B}}^{\mathcal{C}}$ is square
- (D) If we change to the basis $\mathcal{B}' = \{1, 1+x, 1+x+x^2\}$, the matrix $[T]_{\mathcal{B}'}^{\mathcal{C}}$ may change rank
- (E) Since $T$ has a non-trivial kernel, we can make $[T]_{\mathcal{B}}^{\mathcal{C}}$ invertible by removing the kernel basis vectors from $\mathcal{B}$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

Computing $[T]_{\mathcal{B}}^{\mathcal{C}}$:

\begin{itemize}
\item $T(1) = 0 = 0 \cdot 1 + 0 \cdot x$ → column 1: $\begin{pmatrix}0\\0\end{pmatrix}$
\item $T(x) = 1 = 1 \cdot 1 + 0 \cdot x$ → column 2: $\begin{pmatrix}1\\0\end{pmatrix}$
\item $T(x^2) = 2x = 0 \cdot 1 + 2 \cdot x$ → column 3: $\begin{pmatrix}0\\2\end{pmatrix}$
\end{itemize}

Therefore: $[T]_{\mathcal{B}}^{\mathcal{C}} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \end{bmatrix}$

The matrix is $2 \times 3$ (not square), and changing basis won't change rank.

**Partial Credit:**
- (E) Related idea but incorrect conclusion

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

## Problem Q2-P23

**Week 4** | **Bases & Coordinates**

About how many hours $H$ in total did you study for this exam? Count time spent in focused study.
[All answers will receive full credit]

**Choices:**
- (A) $H \leq 4$
- (B) $4< H\leq 6$
- (C) $6< H\leq 8$
- (D) $8< H\leq 10$
- (E) $H>10$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q2-P24

**Week 4** | **Bases & Coordinates**

Which was most helpful to you in studying for this exam?
[All answers will receive full credit]

**Choices:**
- (A) The text
- (B) The sample test problems
- (C) The custom GPT
- (D) A NotebookLM
- (E) Other

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---
