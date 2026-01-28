# Quiz 3: Weeks 5-7

*24 problems*

## Week Breakdown
- Week 6 (Orthogonal Decomposition): 10 problems
- Week 7 (Diagonalization & Dynamics): 14 problems

---

## Problem Q3-P01

**Week 7** | **Diagonalization & Dynamics**
**Concepts:** Eigenvalues, eigenvectors, basic definition

If $\mathbf{v}$ is an eigenvector of matrix $A$ with eigenvalue $\lambda = 3$, what is $A(2\mathbf{v})$?

**Choices:**
- (A) $3\mathbf{v}$
- (B) $6\mathbf{v}$
- (C) $2\mathbf{v}$
- (D) $5\mathbf{v}$
- (E) $9\mathbf{v}$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q3-P02

**Week 7** | **Diagonalization & Dynamics**
**Concepts:** Determinants

A $3 \times 3$ matrix $A$ has eigenvalues $\lambda_1 = 2$, $\lambda_2 = -3$, and $\lambda_3$ unknown. 
If $\det(A) = -12$ and $\text{tr}(A) = 1$, what is $\lambda_3$?

**Choices:**
- (A) $\lambda_3 = 2$
- (B) $\lambda_3 = -2$
- (C) $\lambda_3 = 4$
- (D) $\lambda_3 = -4$
- (E) Not enough information to determine

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q3-P03

**Week 7** | **Diagonalization & Dynamics**
**Concepts:** Companion matrix, characteristic polynomial, polynomial differential operators

The second-order differential equation
$$\frac{d^2x}{dt^2} + 3\frac{dx}{dt} - 4x = 0$$
can be written using the polynomial differential operator $p(D) = D^2 + 3D - 4I$ where $D = d/dt$.

This equation is equivalent to a first-order system $\frac{d\mathbf{v}}{dt} = C\mathbf{v}$ where $C$ is the companion matrix. Which statement correctly describes the relationship between $p(D)$ and $C$?

**Choices:**
- (A) The characteristic polynomial of $C$ is $\lambda^2 - 3\lambda + 4$
- (B) The eigenvalues of $C$ are the roots of $p(\lambda)$
- (C) The determinant of $C$ equals $p(1)=0$
- (D) The companion matrix $C$ has trace equal to $p(0)=-4$
- (E) The matrix $C$ is $C = \begin{bmatrix} 0 & 1 \\ 4 & -3 \end{bmatrix}$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

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

## Problem Q3-P06

**Week 7** | **Diagonalization & Dynamics**
**Concepts:** Determinants

Let $A$ be a $3 \times 3$ diagonalizable matrix with eigenvalues $\lambda_1 = 1$, $\lambda_2 = -2$, and $\lambda_3 = 0$. 
What is $\det(e^A)$?

**Choices:**
- (A) $e^{-1}$
- (B) $e^{1}$
- (C) $0$
- (D) $e^{-2}$
- (E) $1$

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

## Problem Q3-P09

**Week 7** | **Diagonalization & Dynamics**
**Concepts:** Basis and dimension

Let $A = \begin{bmatrix} 5 & 2 \\ 2 & 2 \end{bmatrix}$ have eigenvectors $\mathbf{v}_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$ (with eigenvalue $\lambda_1 = 6$) and $\mathbf{v}_2 = \begin{pmatrix} -1 \\ 2 \end{pmatrix}$ (with eigenvalue $\lambda_2 = 1$).

Consider a vector $\mathbf{x}$ whose coordinates in the eigenbasis $\mathcal{B} = \{\mathbf{v}_1, \mathbf{v}_2\}$ are $[\mathbf{x}]_{\mathcal{B}} = \begin{pmatrix} 3 \\ -2 \end{pmatrix}$. 

What are the coordinates of $A\mathbf{x}$ in the eigenbasis $\mathcal{B}$?

**Choices:**
- (A) $\begin{pmatrix} 6 \\ -1 \end{pmatrix}$
$  :  $
- (B) $\begin{pmatrix} 3 \\ -2 \end{pmatrix}$
$  :  $
- (C) $\begin{pmatrix} 6 \\ 1 \end{pmatrix}$
- (D) $\begin{pmatrix} 18 \\ -2 \end{pmatrix}$
$  :  $
- (E) $\begin{pmatrix} 15 \\ -4 \end{pmatrix}$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q3-P10

**Week 7** | **Diagonalization & Dynamics**
**Concepts:** Basis and dimension, Matrix representations

A $3 \times 3$ matrix $A$ has three distinct real eigenvalues. Let $V = [\mathbf{v}_1 \; \mathbf{v}_2 \; \mathbf{v}_3]$ be the matrix whose columns are corresponding eigenvectors, forming an eigenbasis for $\mathbb{R}^3$.

Which statement correctly describes the relationship between $A$ and its diagonal form $\Lambda = \text{diag}(\lambda_1, \lambda_2, \lambda_3)$?

**Choices:**
- (A) $A = \Lambda V$
- (B) $A = V\Lambda$
- (C) $A = V\Lambda V^{-1}$
- (D) $A = V^{-1}\Lambda V$
- (E) $AV = \Lambda$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q3-P11

**Week 7** | **Diagonalization & Dynamics**
**Concepts:** Matrix invertibility

Let $A$ be a square singular matrix with real distinct eigenvalues.

Which statement about the matrix exponential $e^A$ is most true?

**Choices:**
- (A) $e^A$ may or may not be well-defined
- (B) $e^A$ may not be diagonalizable
- (C) $e^A$ is the solution to $d\mathbf{x}/dt=A\mathbf{x}$
- (D) $e^A$ is nonsingular
- (E) The series for $e^A$ terminates after finitely many terms

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

## Problem Q3-P13

**Week 7** | **Diagonalization & Dynamics**
**Concepts:** Eigenvalues, geometric interpretation, fundamental definition

Which of the following provides the best fundamental description of what an eigenvalue $\lambda$ of a matrix $A$ represents?

**Choices:**
- (A) A root of the characteristic polynomial $\det(A - \lambda I) = 0$
- (B) A scalar for which $A - \lambda I$ is singular
- (C) A value that determines the long-term behavior of the system $\frac{d\mathbf{x}}{dt} = A\mathbf{x}$
- (D) The scaling factor by which $A$ stretches vectors in certain invariant directions
- (E) A value such that $\text{tr}(A)$ equals the sum of all eigenvalues

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

## Problem Q3-P15

**Week 7** | **Diagonalization & Dynamics**
**Concepts:** Determinants

Consider a $3 \times 3$ matrix $B$ with eigenvalues $2$, $3$, and $\lambda$. Which of the following statements is most true?

**Choices:**
- (A) If $\text{tr}(B) = 10$, then $\det(B) = 30$
- (B) If $\det(B) = 24$, then $\text{tr}(B) = 10$
- (C) If $\text{tr}(B) = 10$, then $\lambda = 5$ and $\det(B) = 30$
- (D) The trace and determinant provide independent information and cannot determine $\lambda$ uniquely
- (E) If $\det(B) = 0$, then $\text{tr}(B)$ must equal $0$

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

## Problem Q3-P17

**Week 7** | **Diagonalization & Dynamics**
**Concepts:** Matrix exponentials, ODEs, solution structure

Consider the initial value problem $\frac{d\mathbf{x}}{dt} = A\mathbf{x}$ with $\mathbf{x}(0) = \mathbf{x}_0$, where $A$ is an $n \times n$ matrix. The solution is given by $\mathbf{x}(t) = e^{At}\mathbf{x}_0$.

Which property is the most fundamental reason why $e^{At}\mathbf{x}_0$ solves this initial value problem?

**Choices:**
- (A) The matrix exponential $e^{At}$ is always invertible, so we can recover the initial condition
- (B) The matrix exponential satisfies $e^{A \cdot 0} = I$, which gives $\mathbf{x}(0) = \mathbf{x}_0$
- (C) The matrix exponential satisfies $\frac{d}{dt}e^{At} = Ae^{At}$, which yields the differential equation
- (D) For diagonalizable $A$, we have $e^{At} = Ve^{\Lambda t}V^{-1}$ where eigenvalues determine behavior
- (E) The matrix exponential satisfies the flow property $e^{A(t+s)} = e^{At}e^{As}$

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

## Problem Q3-P19

**Week 7** | **Diagonalization & Dynamics**
**Concepts:** Matrix exponentials, basic properties

Which of the following properties holds for the matrix exponential $e^{At}$ where $A$ is an $n \times n$ matrix and $t$ is a scalar?

**Choices:**
- (A) $e^{At}$ is always symmetric
- (B) $e^{A \cdot 0} = 0$
- (C) $e^{At} \cdot e^{As} = e^{A(t+s)}$ for all scalars $t$ and $s$
- (D) $(e^{At})^{-1} = e^{A^{-1}t}$
- (E) None of the above.

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

## Problem Q3-P21

**Week 7** | **Diagonalization & Dynamics**
**Concepts:** Eigenvalues, matrix powers, diagonalization

Suppose a $2 \times 2$ matrix $A$ has eigenvalues $\lambda_1 = 2$ and $\lambda_2 = -1$. What are the eigenvalues of $A^3$?

**Choices:**
- (A) $2$ and $-1$
- (B) $8$ and $-1$
- (C) $6$ and $-3$
- (D) $8$ and $1$
- (E) Cannot be determined without knowing the eigenvectors

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

## Problem Q3-P23

**Week 7** | **Diagonalization & Dynamics**
**Concepts:** Dimension of vector spaces

Consider the linear differential equation
$$\frac{d^3x}{dt^3} + 6\frac{d^2x}{dt^2} + 5x = 0$$
What is the dimension of the solution space to this equation?

**Choices:**
- (A) 1
- (B) 2
- (C) 3
- (D) 4
- (E) More information is needed

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q3-P24

**Week 7** | **Diagonalization & Dynamics**
**Concepts:** Trace, eigenvalues, sum property

A $4 \times 4$ matrix $A$ has eigenvalues $\lambda_1 = 3$, $\lambda_2 = -2$, $\lambda_3 = 5$, and $\lambda_4$ is unknown. If $\text{tr}(A) = 8$, what is $\lambda_4$?

**Choices:**
- (A) $2$
- (B) $-2$
- (C) $6$
- (D) $4$
- (E) Cannot be determined without knowing the matrix $A$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---
