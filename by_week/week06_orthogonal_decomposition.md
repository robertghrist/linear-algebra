# Week 6: Orthogonal Decomposition

*10 problems*

## Topics Covered
- Determinants
- FTLA
- Isomorphisms
- Least squares
- Orthogonal decomposition
- Orthogonal projection
- Orthogonal projections
- Pseudoinverse
- QR decomposition
- Quotient spaces
- Subspace properties
- best approximation property
- direct sum
- fundamental theorem
- geometric interpretation
- geometric meaning
- idempotent property
- inverse
- matrix relationships
- normal equations
- overdetermined systems
- projection operators
- scaling
- square matrices

---

## Problem Q3-P04

**Week 6** | **Orthogonal Decomposition**
**Concepts:** Subspace properties

Let $A \in \mathbb{R}^{m \times n}$ with $m > n$ have full column rank. For a vector $\mathbf{b} \in \mathbb{R}^m$, consider the system $A\mathbf{x} = \mathbf{b}$.

The pseudoinverse solution $\hat{\mathbf{x}} = A^{\dagger}\mathbf{b}$ has a special property regarding which fundamental subspace it lies in. Which statement is correct?

**Choices:**
- (A) $\hat{\mathbf{x}} \in \ker(A)$
- (B) $\hat{\mathbf{x}} \in (\ker A)^{\perp}$
- (C) $\hat{\mathbf{x}} \in \text{im}(A^T)$
- (D) $\hat{\mathbf{x}} \in (\text{im}\,A)^\perp$
- (E) Both (B) and (C) are correct

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q3-P05

**Week 6** | **Orthogonal Decomposition**
**Concepts:** Orthogonal projections, projection operators, idempotent property

Let $\Pi_W: V \to V$ be an orthogonal projection operator onto a subspace $W$ of an inner product space $V$. For a particular vector $\mathbf{v} \in V$, the projection satisfies $\Pi_W(\mathbf{v}) = \mathbf{w}$ where $\mathbf{w} \neq \mathbf{0}$.

What is the result of computing $\Pi_W(\mathbf{w})$ ?

**Choices:**
- (A) $\mathbf{0}$
- (B) $2\mathbf{w}$
- (C) $\mathbf{w}$
- (D) $\mathbf{w}/\norm{\mathbf{w}}$
- (E) Not enough information to say

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q3-P07

**Week 6** | **Orthogonal Decomposition**
**Concepts:** Determinants

A nonsingular $n \times n$ matrix $A$ has QR decomposition $A = QR$ where $Q=[Q_{ij}]$ and $R=[R_{ij}]$. 
Which statement about $\det(A)$ must be true?

**Choices:**
- (A) $\det(A) = \det(R)$
- (B) $\det(A) = 1$
- (C) $\det(A) = \pm 1$
- (D) $\det(A) = \pm \prod_{i=1}^n R_{ii}$
- (E) None of the above

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q3-P08

**Week 6** | **Orthogonal Decomposition**
**Concepts:** Pseudoinverse, inverse, square matrices

Let $A$ be a nonsingular matrix. Which statement best represents the relationship between the pseudoinverse $A^{\dagger}$ and the inverse $A^{-1}$?

**Choices:**
- (A) $A^{\dagger} = A^{-1}$
- (B) $A^{\dagger} = (A^{-1})^T$
- (C) $A^{\dagger} = (A^T)^{-1}$
- (D) $A^{\dagger}A^{-1} = I$
- (E) $A^{\dagger}$ is undefined if $A^{-1}$ does not exist

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q3-P12

**Week 6** | **Orthogonal Decomposition**
**Concepts:** Orthogonal decomposition, direct sum, fundamental theorem

Let $V$ be a finite-dimensional inner product space and $W$ a subspace of $V$. The orthogonal complement $W^{\perp}$ consists of all vectors in $V$ that are orthogonal to every vector in $W$.

Which statement about the relationship between $W$ and $W^{\perp}$ is most true?

**Choices:**
- (A) $W \cap W^{\perp} = \{\mathbf{0}\}$ and $V = W + W^{\perp}$
- (B) $W \cap W^{\perp} = W$
- (C) $\dim W = \dim W^{\perp}$
- (D) $\dim(W) + \dim(W^{\perp}) \leq \dim(V)$
- (E) $W<W^{\perp}$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q3-P14

**Week 6** | **Orthogonal Decomposition**
**Concepts:** Orthogonal projection, best approximation property, geometric meaning

Which of the following provides the best fundamental description of the orthogonal projection $\Pi_W(\mathbf{v})$ of a vector $\mathbf{v}$ onto a subspace $W$?

**Choices:**
- (A) The unique vector in $W$ that minimizes $\|\mathbf{v} - \mathbf{w}\|$ over all $\mathbf{w} \in W$
- (B) A linear operator satisfying $\Pi_W^2 = \Pi_W$ and $\Pi_W^* = \Pi_W$
- (C) The component of $\mathbf{v}$ that lies in $W$ when $\mathbf{v}$ is decomposed as $\mathbf{v} = \mathbf{v}_W + \mathbf{v}_{W^\perp}$
- (D) The vector obtained by applying the matrix $A(A^TA)^{-1}A^T$ to $\mathbf{v}$, where the columns of $A$ span $W$
- (E) The solution to the normal equations $A^TA\mathbf{x} = A^T\mathbf{v}$ when the columns of $A$ form a basis for $W$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q3-P16

**Week 6** | **Orthogonal Decomposition**
**Concepts:** Pseudoinverse, geometric interpretation, FTLA

Consider a matrix $A \in \mathbb{R}^{m \times n}$ with $m > n$ and full column rank. The pseudoinverse $A^{\dagger} = (A^TA)^{-1}A^T$ can be understood geometrically through the Fundamental Theorem of Linear Algebra.

Which of the following best describes the geometric action of $A^{\dagger}$ on a vector $\mathbf{b} \in \mathbb{R}^m$?

**Choices:**
- (A) $A^{\dagger}$ first projects $\mathbf{b}$ onto $\ker(A^T)$, then applies the inverse map
- (B) $A^{\dagger}$ first projects $\mathbf{b}$ onto $\text{im}(A)$, then applies the inverse of $A$ restricted to $(\ker A)^{\perp}$
- (C) $A^{\dagger}$ applies $A^{-1}$ directly when it exists, otherwise returns the zero vector
- (D) $A^{\dagger}$ computes the orthogonal complement of $\mathbf{b}$ in $\text{im}(A)$
- (E) $A^{\dagger}$ finds the unique vector in $\ker(A)$ closest to $\mathbf{b}$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q3-P18

**Week 6** | **Orthogonal Decomposition**
**Concepts:** Least squares, normal equations, overdetermined systems

Consider the overdetermined linear system $A\mathbf{x} = \mathbf{b}$ where $A \in \mathbb{R}^{m \times n}$ with $m > n$ (more equations than unknowns) and $A$ has full column rank. If the system is inconsistent (no exact solution exists), what function does the least squares solution $\hat{\mathbf{x}}$ minimize?

**Choices:**
- (A) $\|A\mathbf{x}\|$
- (B) $\|\mathbf{x}\|$
- (C) $\|A\mathbf{x} - \mathbf{b}\|$
- (D) $|\mathbf{b}^T A \mathbf{x}|$
- (E) $|\mathbf{b}^T\mathbf{x}|$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q3-P20

**Week 6** | **Orthogonal Decomposition**
**Concepts:** QR decomposition, scaling, matrix relationships

Suppose a matrix $A$ has QR decomposition $A = Q_AR_A$. For a positive scalar $c > 0$, what is the QR decomposition of $cA$?

**Choices:**
- (A) $cA = (cQ_A)(R_A)$
- (B) $cA = (Q_A)(cR_A)$
- (C) $cA = (cQ_A)(cR_A)$
- (D) $cA = (Q_A)(R_A)$
- (E) Cannot be determined without knowing $c$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q3-P22

**Week 6** | **Orthogonal Decomposition**
**Concepts:** Quotient spaces, Isomorphisms

Let $V$ be a finite-dimensional inner product space and $W$ a subspace of $V$. Consider the quotient space $V/W$, whose elements are equivalence classes $[\mathbf{v}] = \{\mathbf{v} + \mathbf{w} : \mathbf{w} \in W\}$.

In an inner product space, we can represent each equivalence class $[\mathbf{v}]$ uniquely by a distinguished vector. Which of the following provides the correct geometric characterization of this distinguished representative?

**Choices:**
- (A) The vector in $[\mathbf{v}]$ with maximum norm
- (B) The vector in $[\mathbf{v}]$ that lies in $W$
- (C) The vector in $[\mathbf{v}]$ that lies in $W^{\perp}$
- (D) The vector in $[\mathbf{v}]$ that is closest to the origin
- (E) Both (C) and (D) describe the same vector

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---
