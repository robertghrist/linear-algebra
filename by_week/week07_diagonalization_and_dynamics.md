# Week 7: Diagonalization & Dynamics

*16 problems*

## Topics Covered
- Basis and dimension
- Companion matrix
- Determinants
- Dimension of vector spaces
- Eigenvalues
- Matrix exponentials
- Matrix invertibility
- Matrix representations
- ODEs
- Trace
- basic definition
- basic properties
- characteristic polynomial
- diagonalization
- eigenvalues
- eigenvectors
- fundamental definition
- geometric interpretation
- matrix powers
- polynomial differential operators
- solution structure
- sum property

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

## Problem Q4-P18

**Week 7** | **Diagonalization & Dynamics**

Let $X$ be a $5 \times 3$ matrix with linearly independent columns. Consider the square matrix $A = X^TX$. Which statement about the eigenvalues of $A$ must be true?

**Choices:**
- (A) There are three positive eigenvalues
- (B) At least one eigenvalue equals zero
- (C) There are no repeated eigenvalues
- (D) There are five positive eigenvalues
- (E) None of the above is necessarily true

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q4-P21

**Week 7** | **Diagonalization & Dynamics**

A $5 \times 5$ matrix $A$ has characteristic polynomial $p(\lambda) = (\lambda - 2)^3(\lambda + 1)^2$. Suppose you compute $\dim(\ker(A - 2I)) = 2$ and $\dim(\ker(A + I)) = 2$.

What can you conclude about $A$?

**Choices:**
- (A) $A$ is diagonalizable
- (B) $A$ is not diagonalizable
- (C) $A$ has Jordan blocks of size at least 2
- (D) The matrix $A - 2I$ has rank 2
- (E) Both (B) and (C)

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---
