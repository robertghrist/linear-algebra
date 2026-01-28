# Week 10: Singular Value Decomposition

*13 problems*

## Topics Covered
- Dimension of vector spaces
- Eigenvalues vs singular values
- Frobenius norm from singular values
- Geometric foundations of SVD
- Image (range)
- Isomorphisms
- Kernel (null space)
- Pseudoinverse construction via SVD
- Rank-Nullity Theorem
- SVD from geometric picture
- SVD of orthogonal matrices
- Singular values ordering
- Subspace properties
- basic SVD properties
- general square matrices
- geometric interpretation
- left vs right singular vectors
- operations on matrices
- role of A^TA
- singular value conventions
- singular values
- sphere to ellipsoid transformation
- symmetric matrices
- Σ^† formula

---

## Problem Q5-P01

**Week 10** | **Singular Value Decomposition**
**Concepts:** SVD from geometric picture, singular value conventions, left vs right singular vectors

The figure shows how a matrix $A \in \mathbb{R}^{2 \times 2}$ transforms the unit circle to an ellipse, with the singular vectors represented.

\begin{center}
\begin{figure}[h]
\includegraphics[width=6.5in]{2030 Q5 SVD FIG.jpg}

\end{figure}
\end{center}

Based on this figure, which of the following is the most likely SVD of $A = U\Sigma V^T$?

![Figure](../images/2030 Q5 SVD FIG.jpg)

**Choices:**
- (A) $U = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}, \quad \Sigma = \begin{bmatrix} 3/2 & 0 \\ 0 & 1/2 \end{bmatrix}, \quad V = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}$
- (B) $U = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}, \quad \Sigma = \begin{bmatrix} 3/2 & 0 \\ 0 & 1/2 \end{bmatrix}, \quad V = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$
- (C) $U = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}, \quad \Sigma = \begin{bmatrix} 1/2 & 0 \\ 0 & 3/2 \end{bmatrix}, \quad V = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}$
- (D) $U = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}, \quad \Sigma = \begin{bmatrix} 3/2 & 0 \\ 0 & -1/2 \end{bmatrix}, \quad V = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$
- (E) $U = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}, \quad \Sigma = \begin{bmatrix} 3/2 & 0 \\ 0 & 1/2 \end{bmatrix}, \quad V = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P02

**Week 10** | **Singular Value Decomposition**
**Concepts:** Geometric foundations of SVD, sphere to ellipsoid transformation, role of A^TA

A linear transformation $A \in \mathbb{R}^{3 \times 2}$ maps the unit circle in $\mathbb{R}^2$ to an ellipse in $\mathbb{R}^3$. The matrix $A^TA$ has eigenvalues $\lambda_1 = 9$ and $\lambda_2 = 4$ with corresponding orthonormal eigenvectors $\mathbf{v}_1$ and $\mathbf{v}_2$.

Which statement correctly describes the geometric action of $A$?

**Choices:**
- (A) The ellipse in $\mathbb{R}^3$ has semi-axis lengths 9 and 4, aligned with the directions $\mathbf{v}_1$ and $\mathbf{v}_2$.
- (B) The ellipse in $\mathbb{R}^3$ has semi-axis lengths 3 and 2, and the input directions $\mathbf{v}_1$ and $\mathbf{v}_2$ are mapped to these semi-axes.
- (C) The ellipse lies in a 2-dimensional subspace of $\mathbb{R}^3$, with semi-axis lengths $\sqrt{9} = 3$ and $\sqrt{4} = 2$.
- (D) The transformation stretches the direction $\mathbf{v}_1$ by factor 9 and $\mathbf{v}_2$ by factor 4, producing an ellipse with area $36\pi$.
- (E) The eigenvalues of $A$ determine the semi-axis lengths, which are 9 and 4.

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P03

**Week 10** | **Singular Value Decomposition**
**Concepts:** Rank-Nullity Theorem

A centered data matrix $X \in \mathbb{R}^{n \times d}$ has SVD $X = U\Sigma V^T$ with singular values $\sigma_1 = 100, \sigma_2 = 50, \sigma_3 = 25, \ldots$ A researcher wants a 2-dimensional representation of the $n$ observations and considers two approaches:

\textbf{Approach 1:} Compute the $n \times 2$ matrix $U_2\Sigma_2$, where $U_2$ contains the first 2 columns of $U$ and $\Sigma_2$ is the $2 \times 2$ upper-left block of $\Sigma$.

\textbf{Approach 2:} Compute the $n \times 2$ matrix $XV_2$, where $V_2$ contains the first 2 columns of $V$ (i.e., project each observation onto the first two principal component directions).

Which statement is most TRUE?

**Choices:**
- (A) Both approaches give identical 2D representations since $U\Sigma = XV$.
- (B) Approach 1 gives the optimal rank-2 approximation to $X$ in Frobenius norm, while Approach 2 gives the 2D representation that maximizes captured variance, but these are different things.
- (C) The approaches yield different matrices: $U_2\Sigma_2 \neq XV_2$ because one uses left singular vectors and the other uses right singular vectors.
- (D) Approach 1 produces vectors in $\mathbb{R}^n$ while Approach 2 produces vectors in $\mathbb{R}^d$, so they cannot be compared.
- (E) Both approaches produce the same $n \times 2$ matrix of 2D observation coordinates, and both optimally capture the variance structure in a 2D subspace.

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P04

**Week 10** | **Singular Value Decomposition**
**Concepts:** Singular values ordering, operations on matrices, basic SVD properties

A matrix $A \in \mathbb{R}^{m \times n}$ has singular values $\sigma_1 = 5$, $\sigma_2 = 3$, $\sigma_3 = 1$, and $\sigma_k = 0$ for $k>3$. 

Which of the following statements is most TRUE?

**Choices:**
- (A) Matrix $2A$ has singular values 10, 6, 2, with all others zero, but they should be reordered as 2, 6, 10 to maintain the SVD convention.
- (B) Matrix $A^T$ has singular values $\sigma_1=1, \sigma_2=3, \sigma_3=5$, with all others zero.
- (C) Matrix $A^TA$ has eigenvalues 25, 9, 1, with the remaining eigenvalues zero.
- (D) The largest singular value of $AA^T$ is 25.
- (E) Matrices $A^TA$ and $AA^T$ have different nonzero eigenvalues.

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P05

**Week 10** | **Singular Value Decomposition**
**Concepts:** Pseudoinverse construction via SVD, Σ^† formula

A matrix $A \in \mathbb{R}^{4 \times 3}$ has singular value decomposition $A = U\Sigma V^T$ where $U \in \mathbb{R}^{4 \times 4}$, $V \in \mathbb{R}^{3 \times 3}$ are orthogonal, and:
$$\Sigma = \begin{bmatrix} 5 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix} \in \mathbb{R}^{4 \times 3}$$

What is the pseudoinverse $A^\dagger$ of this matrix?

**Choices:**
- (A) $A^\dagger = U\Sigma^{-1} V^T$ where $\Sigma^{-1} = \begin{bmatrix} 1/5 & 0 & 0 \\ 0 & 1/2 & 0 \\ 0 & 0 & \text{undefined} \\ 0 & 0 & \text{undefined} \end{bmatrix}$
- (B) $A^\dagger = V\Sigma^T U^T$ where $\Sigma^T = \begin{bmatrix} 5 & 0 & 0 & 0 \\ 0 & 2 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$
- (C) $A^\dagger = V\Sigma^\dagger U^T$ where $\Sigma^\dagger = \begin{bmatrix} 1/5 & 0 & 0 & 0 \\ 0 & 1/2 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$
- (D) $A^\dagger = U^T\Sigma^\dagger V$ where $\Sigma^\dagger = \begin{bmatrix} 1/5 & 0 & 0 & 0 \\ 0 & 1/2 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$
- (E) $A^\dagger = V\Sigma^\dagger U^T$ where $\Sigma^\dagger = \begin{bmatrix} 1/5 & 0 & 0 \\ 0 & 1/2 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P06

**Week 10** | **Singular Value Decomposition**
**Concepts:** Subspace properties

A data matrix $A \in \mathbb{R}^{100 \times 50}$ represents measurements where rows are observations and columns are features. The SVD $A = U\Sigma V^T$ reveals that only the first 10 singular values are nonzero: $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_{10} > 0$ and $\sigma_{11} = \cdots = \sigma_{50} = 0$.

An analyst wants to understand the fundamental subspaces. Which statement is most TRUE?

**Choices:**
- (A) The first 10 right singular vectors $\mathbf{v}_1, \ldots, \mathbf{v}_{10}$ span the column space of $A$, capturing the 10 most important patterns in the observations.
- (B) The first 10 left singular vectors $\mathbf{u}_1, \ldots, \mathbf{u}_{10}$ span a 10-dimensional subspace of feature space where all data variation occurs.
- (C) The right singular vectors $\mathbf{v}_{11}, \ldots, \mathbf{v}_{50}$ form a basis for $\ker(A)$, representing 40 redundant feature combinations.
- (D) The left singular vectors $\mathbf{u}_{11}, \ldots, \mathbf{u}_{100}$ span $\ker(A^T)$, representing observation directions that have no correlation with any features.
- (E) Both (C) and (D) are correct.

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P07

**Week 10** | **Singular Value Decomposition**
**Concepts:** Dimension of vector spaces

A machine learning engineer wants to store a compressed representation of matrix $A \in \mathbb{R}^{500 \times 300}$ using its rank-$k$ SVD approximation $A_k = \sum_{i=1}^k \sigma_i \mathbf{u}_i\mathbf{v}_i^T$.

To store $A_k$, they need to save:
\begin{itemize}
\item $k$ singular values $\{\sigma_1, \ldots, \sigma_k\}$
\item $k$ left singular vectors $\{\mathbf{u}_1, \ldots, \mathbf{u}_k\}$
\item $k$ right singular vectors $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$
\end{itemize}

How many total scalar values must be stored, and for which value of $k$ does the storage equal the original matrix $A$?

**Choices:**
- (A) $k(500 + 300 + 1)$ values; storage equals original when $k = 500$
- (B) $k(500 + 300 + 1)$ values; storage equals original when $k = 300$
- (C) $k(500 + 300)$ values; storage equals original when $k = 187$ (approximately)
- (D) $k(500 \cdot 300)$ values; storage never equals original since SVD is always compressed
- (E) $k(500 + 300 + 1)$ values; storage equals original when $k = 187$ (approximately)

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P08

**Week 10** | **Singular Value Decomposition**
**Concepts:** SVD of orthogonal matrices, singular values, geometric interpretation

What can be said about the SVD of an orthogonal matrix $Q \in \mathbb{R}^{n \times n}$?.

**Choices:**
- (A) All singular values equal 1, so $Q = U\Sigma V^T$ where $\Sigma = I$, meaning $Q = UV^T$ is a product of two orthogonal matrices.
- (B) The singular values depend on the specific matrix $Q$; for example, a rotation matrix has different singular values than a reflection matrix.
- (C) All singular values equal 1, and because of this the SVD is not unique.
- (D) Orthogonal matrices do not have a uniquely defined SVD because they preserve lengths, which contradicts the stretching interpretation of singular values.
- (E) The largest singular value is 1, but the other singular values can be less than 1 depending on how much $Q$ ``compresses'' certain directions.

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P11

**Week 10** | **Singular Value Decomposition**
**Concepts:** Subspace properties, Isomorphisms

The SVD $A = U\Sigma V^T$ reveals that $A$ acts as an isomorphism (scaled by singular values) between certain fundamental subspaces. For matrix $A \in \mathbb{R}^{m \times n}$ with rank $r$, which statement is most TRUE?

**Choices:**
- (A) $A$ maps $\ker(A)$ isomorphically onto $\ker(A^T)$ by the relationship $A\mathbf{v}_i = \sigma_i \mathbf{u}_i$ for $i > r$.
- (B) $A$ maps $\text{im}(A^T)$ isomorphically onto $\text{im}(A)$, with the isomorphism given by scaling: $A\mathbf{v}_i = \sigma_i \mathbf{u}_i$ for $i \leq r$.
- (C) $A$ maps $\mathbb{R}^n$ isomorphically onto $\mathbb{R}^m$ whenever $m = n$, regardless of rank.
- (D) $A$ maps both $\ker(A)$ and $\text{im}(A^T)$ isomorphically onto $\text{im}(A)$, explaining why $\dim(\ker(A)) + \dim(\text{im}(A^T)) = \dim(\text{im}(A))$.
- (E) The restriction of $A$ to $\ker(A)$ is an isomorphism onto $\ker(A^T)$ because both have dimension $n - r$.

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P14

**Week 10** | **Singular Value Decomposition**
**Concepts:** Subspace properties, Kernel (null space), Image (range)

A matrix $A \in \mathbb{R}^{7 \times 5}$ has rank 3 with SVD $A = U\Sigma V^T$.

Which approach yields a basis for the coimage $\text{coim}(A) = (\ker A)^\perp$?

**Choices:**
- (A) Right singular vectors $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3, \mathbf{v}_4, \mathbf{v}_5\}$
- (B) Left singular vectors $\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\}$
- (C) Right singular vectors $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$
- (D) Left singular vectors $\{\mathbf{u}_4, \mathbf{u}_5, \mathbf{u}_6, \mathbf{u}_7\}$
- (E) Right singular vectors $\{\mathbf{v}_4, \mathbf{v}_5\}$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P15

**Week 10** | **Singular Value Decomposition**
**Concepts:** Eigenvalues vs singular values, symmetric matrices, general square matrices

A $3 \times 3$ matrix $A$ has eigenvalues $\lambda_1 = 5$, $\lambda_2 = -3$, $\lambda_3 = 1$.

Which statement about the singular values of $A$ is most TRUE?

**Choices:**
- (A) The singular values are $5, 3, 1$.
- (B) The singular values are $25, 9, 1$.
- (C) The singular values are $\sqrt{5}, \sqrt{3}, 1$.
- (D) The singular values cannot be determined from eigenvalues alone.
- (E) The singular values of a {\em square} matrix equal the eigenvalues for any square matrix.

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P19

**Week 10** | **Singular Value Decomposition**
**Concepts:** Frobenius norm from singular values

A matrix $A \in \mathbb{R}^{4 \times 3}$ has singular values $\sigma_1 = 6$, $\sigma_2 = 3$, $\sigma_3 = 2$.

What is the Frobenius norm $\|A\|_F$?

**Choices:**
- (A) $11$
- (B) $49$
- (C) $7$
- (D) $\sqrt{11}$
- (E) Not enough information to determine $\|A\|_F$.

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P20

**Week 10** | **Singular Value Decomposition**
**Concepts:** Subspace properties

The figure shows the full SVD $A = U\Sigma V^T$ for a matrix $A \in \mathbb{R}^{12 \times 5}$.
Filled circles represent nonzero singular values; empty circles represent zero singular values.
Vertical lines indicate columns; horizontal lines indicate rows.

\begin{center}
\begin{figure}[h]
\includegraphics[width=7in]{2030 Q5 SVD ICON.jpg}

\end{figure}
\end{center}
Which statement is most TRUE?

![Figure](../images/2030 Q5 SVD ICON.jpg)

**Choices:**
- (A) $\dim(\ker A) = 9$.
- (B) The first three columns of $V$ form an orthonormal basis for $\mathrm{im}(A)$.
- (C) The last 9 columns of $U$ form an orthonormal basis for the codomain of $A$.
- (D) The last two columns of $V$ form an orthonormal basis for $\ker(A)$.
- (E) The rank of $A$ equals $5$.

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---
