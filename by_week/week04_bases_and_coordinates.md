# Week 4: Bases & Coordinates

*9 problems*

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
