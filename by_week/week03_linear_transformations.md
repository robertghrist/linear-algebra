# Week 3: Linear Transformations

*16 problems*

## Topics Covered
- Coimage and cokernel
- Dimension of vector spaces
- Image (range)
- Isomorphisms
- Kernel (null space)
- Linear transformation properties
- Matrix representations
- Polynomial vector spaces
- Quotient spaces
- Rank-Nullity Theorem

---

## Problem Q1-P03

**Week 3** | **Linear Transformations**
**Concepts:** Linear transformation properties, Kernel (null space), Matrix representations

Let $T: \mathbb{R}^3 \to \mathbb{R}^3$ be the linear transformation with matrix representation $A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ -1 & -2 & -3 \end{bmatrix}$. What is the dimension of $\ker(T)$?

**Choices:**
- (A) 0
- (B) 1
- (C) 2
- (D) 3
- (E) None of the above

<details>
<summary>Show Answer</summary>

**Correct: (C)**

Observe that all three rows of $A$ are scalar multiples:
\begin{align}
\text{Row 2} &= 2 \times \text{Row 1}\\
\text{Row 3} &= -1 \times \text{Row 1}
\end{align}

Therefore:
\begin{itemize}
\item $\text{rank}(A) = 1$ (only one independent row)
\item By the Rank-Nullity Theorem: $\dim(V) = \text{rank}(T) + \dim(\ker(T))$
\item So: $3 = 1 + \dim(\ker(T))$
\item Therefore: $\dim(\ker(T)) = 2$
\end{itemize}

**Key Insight:** When all rows/columns are proportional, the rank is 1.

**Partial Credit:**
- (B) 1 - shows understanding but miscalculation

</details>

---

## Problem Q1-P05

**Week 3** | **Linear Transformations**
**Concepts:** Rank-Nullity Theorem

Let ${\mathcal D}: \mathcal{P}_3 \to \mathcal{P}_2$ be the differentiation operator taking cubic to quadratic polynomials. 
The rank and nullity of this operator are:

**Choices:**
- (A) rank = 3, nullity = 1
- (B) rank = 2, nullity = 2
- (C) rank = 3, nullity = 0
- (D) rank = 2, nullity = 1
- (E) rank = 4, nullity = 0

<details>
<summary>Show Answer</summary>

**Correct: (A)**

The differentiation operator $\mathcal{D}: \mathcal{P}_3 \to \mathcal{P}_2$ works as:
$$\mathcal{D}(a_0 + a_1x + a_2x^2 + a_3x^3) = a_1 + 2a_2x + 3a_3x^2$$

\begin{itemize}
\item The image is all of $\mathcal{P}_2$ (any quadratic can be obtained), so $\text{rank} = \dim(\mathcal{P}_2) = 3$
\item The kernel consists of constant polynomials (derivatives equal zero), so $\dim(\ker(\mathcal{D})) = 1$
\item Verify: $\dim(\mathcal{P}_3) = 4 = 3 + 1$ ✓
\end{itemize}

**Key Insight:** The derivative of constants is zero, so the kernel is the space of constant polynomials.

</details>

---

## Problem Q1-P07

**Week 3** | **Linear Transformations**
**Concepts:** Image (range), Coimage and cokernel, Kernel (null space), Quotient spaces

Let $T: V \to W$ be a linear transformation. Which statement correctly describes the coimage and cokernel of $T$?

**Choices:**
- (A) $\text{coim } T = \ker T$ and $\text{coker } T = \text{im } T$
- (B) $\text{coim } T = V/\text{im } T$ and $\text{coker } T = W/\ker T$
- (C) $\text{coim } T = V/\ker T$ and $\text{coker } T = W/\text{im } T$
- (D) $\text{coim } T = \text{im } T$ and $\text{coker } T = \ker T$
- (E) $\text{coim } T = W/\ker T$ and $\text{coker } T = V/\text{im } T$

<details>
<summary>Show Answer</summary>

**Correct: (C)**

By definition:
\begin{itemize}
\item \textbf{Coimage:} The quotient of the domain by the kernel: $V/\ker T$
  \begin{itemize}
  \item This "mods out" the part that maps to zero
  \item Results in equivalence classes of vectors that map to the same output
  \end{itemize}
\item \textbf{Cokernel:} The quotient of the codomain by the image: $W/\text{im } T$
  \begin{itemize}
  \item This captures "what's missing" from the image
  \item Measures the failure of surjectivity
  \end{itemize}
\end{itemize}

**Key Insight:** Remember: "co-" operations involve quotients of the corresponding spaces.

**Watch Out:**
- (A) Students might think coimage and cokernel are just alternate names for kernel and image
- (B) Reverses which space gets quotiented by what - a plausible misconception
- (D) Another confusion between the fundamental spaces and their quotients
- (E) Mixes up domain and codomain in the quotient constructions

</details>

---

## Problem Q1-P12

**Week 3** | **Linear Transformations**
**Concepts:** Linear transformation properties, Kernel (null space), Image (range), Rank-Nullity Theorem

Let $T: V \to W$ be a linear transformation between finite-dimensional vector spaces. If $\dim(V) = 5$ and $\dim(W) = 3$, which statement about $T$ must be TRUE?

**Choices:**
- (A) $T$ must be injective
- (B) $T$ must be surjective
- (C) The dimension of $\ker(T)$ is at least 2
- (D) The dimension of $\text{im}(T)$ is 3
- (E) None of the above

<details>
<summary>Show Answer</summary>

**Correct: (C)**

By the Rank-Nullity Theorem:
$$\dim(V) = \dim(\ker T) + \dim(\text{im } T)$$

Since $\text{im}(T) \subseteq W$, we have $\dim(\text{im } T) \leq \dim(W) = 3$.

Therefore:
$$5 = \dim(\ker T) + \dim(\text{im } T) \leq \dim(\ker T) + 3$$

So $\dim(\ker T) \geq 2$.

**Key Insight:** When domain dimension exceeds codomain dimension, there must be a nontrivial kernel.

</details>

---

## Problem Q1-P17

**Week 3** | **Linear Transformations**
**Concepts:** Linear transformation properties

Which one of the following is NOT a linear transformation?

**Choices:**
- (A) $T: \mathbb{R}^2 \to \mathbb{R}^2$ defined by $T(x,y) = (x-y, 0)$
- (B) $S: \mathcal{P}_2 \to \mathcal{P}_2$ defined by $S(p(x)) = xp'(x)$ where $p'$ denotes the derivative
- (C) $R: \mathbb{R}^3 \to \mathbb{R}$ defined by $R(x,y,z) = 2x - 3y + z$
- (D) $F: \mathbb{R}^2 \to \mathbb{R}^3$ defined by $F(x,y) = (x+1, y, x-y)$
- (E) $G: \mathbb{R}^{2\times 2} \to \mathbb{R}$ defined by $G(A) = \text{trace}(A)$ (trace is the sum of diagonal terms)

<details>
<summary>Show Answer</summary>

**Correct: (D)**

For a transformation to be linear, it must satisfy $T(\mathbf{0}) = \mathbf{0}$.

Check $F$: $F(0,0) = (0+1, 0, 0-0) = (1, 0, 0) \neq (0, 0, 0)$

This immediately disqualifies $F$. Additionally, $F$ fails additivity:
$$F(x_1+x_2, y_1+y_2) = (x_1+x_2+1, y_1+y_2, x_1+x_2-y_1-y_2)$$
$$\neq F(x_1,y_1) + F(x_2,y_2) = (x_1+1, y_1, x_1-y_1) + (x_2+1, y_2, x_2-y_2)$$

All other options preserve the zero vector and satisfy linearity.

**Watch Out:**
- (A) Students might think the zero in second component makes it non-linear
- (B) Product of x and p'(x) might seem non-linear, but this IS linear in p
- (C) Students might incorrectly think maps to different dimension can't be linear
- (E) Students unfamiliar with trace might assume it's non-linear

</details>

---

## Problem Q1-P18

**Week 3** | **Linear Transformations**
**Concepts:** Kernel (null space), Polynomial vector spaces

The Fundamental Theorem of Linear Algebra says that for a linear transformation $T:V\to W$

**Choices:**
- (A) The kernel and cokernel are isomorphic
- (B) The domain and codomain are isomorphic
- (C) The coimage and cokernel are isomorphic
- (D) The kernel and image are isomorphic
- (E) None of the above

<details>
<summary>Show Answer</summary>

**Correct: (E)**

The Fundamental Theorem of Linear Algebra states:
$$\text{coim}(T) \cong \text{im}(T)$$

That is, the coimage $V/\ker(T)$ is isomorphic to the image of $T$.

None of the given options correctly state this relationship. This tests precise understanding of the theorem's statement.

**Key Insight:** The key isomorphism is between what's "left after modding out the kernel" and what actually gets mapped to.

</details>

---

## Problem Q1-P19

**Week 3** | **Linear Transformations**
**Concepts:** Isomorphisms, Dimension of vector spaces

Consider an $m$-by-$n$ matrix $A$ and the associated linear transformation $T_A:\mathbb{R}^n\to\mathbb{R}^m$. Which of the following is true?

**Choices:**
- (A) $A$ is nonsingular if $T_A$ is injective
- (B) The column space of $A$ is the coimage of $T_A$
- (C) The null space of $A$ is the kernel of $T_A$
- (D) If $T_A$ is surjective then $A$ is nonsingular
- (E) If $T_A$ is injective then $A$ is singular

<details>
<summary>Show Answer</summary>

**Correct: (C)**

By definition:
\begin{itemize}
\item The null space of $A$ = $\{\mathbf{x} : A\mathbf{x} = \mathbf{0}\}$ = $\ker(T_A)$ ✓
\item The column space of $A$ = image of $T_A$ (not coimage)
\item "Nonsingular" only makes sense for square matrices
\item Options (A), (D), (E) incorrectly relate injectivity/surjectivity to singularity
\end{itemize}

**Partial Credit:**
- (B) Column space equals image, not coimage

</details>

---

## Problem Q1-P22

**Week 3** | **Linear Transformations**
**Concepts:** Image (range), Coimage and cokernel, Quotient spaces

Let $T: \mathbb{R}^5 \to \mathbb{R}^6$ be a linear transformation with $\dim(\ker(T)) = 2$. The cokernel of $T$ is isomorphic to which space?

**Choices:**
- (A) $\mathbb{R}^1$
- (B) $\mathbb{R}^6$
- (C) $\mathbb{R}^4$
- (D) $\mathbb{R}^3$
- (E) $\ker(T)$

<details>
<summary>Show Answer</summary>

**Correct: (D)**

Given: $T: \mathbb{R}^5 \to \mathbb{R}^6$ with $\dim(\ker(T)) = 2$

By Rank-Nullity: $\dim(\text{im}(T)) = 5 - 2 = 3$

The cokernel is $\text{coker}(T) = \mathbb{R}^6/\text{im}(T)$

Therefore: $\dim(\text{coker}(T)) = 6 - 3 = 3$

So coker$(T) \cong \mathbb{R}^3$.

**Key Insight:** The cokernel measures "what's missing" from the image to fill the codomain.

</details>

---

## Problem Q1-P23

**Week 3** | **Linear Transformations**
**Concepts:** Quotient spaces

Let $V = \mathbb{R}^3$ and let $W$ be the subspace defined by the $xy$-plane, i.e., $W = \{(x, y, 0) \mid x, y \in \mathbb{R}\}$. An equivalence relation is defined on $V$ where two vectors $\mathbf{u}$ and $\mathbf{v}$ are equivalent if their difference $\mathbf{u - v}$ is an element of $W$.

Given the vector $\mathbf{v} = (3, 5, 2)^T$, which of the following vectors belongs to the equivalence class $[\mathbf{v}]$?

**Choices:**
- (A) $(3, 5, 0)^T$
- (B) $(6, 10, 4)^T$
- (C) $(-1, -2, 2)^T$
- (D) $(0, 0, 0)^T$
- (E) None of the above

<details>
<summary>Show Answer</summary>

**Correct: (C)**

Two vectors are equivalent if their difference lies in $W$ (the $xy$-plane).

For $\mathbf{v} = (3, 5, 2)^T$, check each option:

\begin{itemize}
\item (A): $(3,5,2) - (3,5,0) = (0,0,2) \notin W$ (has nonzero $z$-component)
\item (B): $(3,5,2) - (6,10,4) = (-3,-5,-2) \notin W$
\item (C): $(3,5,2) - (-1,-2,2) = (4,7,0) \in W$ ✓ (zero $z$-component)
\item (D): $(3,5,2) - (0,0,0) = (3,5,2) \notin W$
\end{itemize}

**Key Insight:** Vectors are equivalent mod $W$ if they differ only by an element of $W$.

**Watch Out:**
- (A) This is the projection of v onto W, a common point of confusion.
- (B) This is a scalar multiple of v; their difference $v - 2v = -v$, which is not in W.

</details>

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
