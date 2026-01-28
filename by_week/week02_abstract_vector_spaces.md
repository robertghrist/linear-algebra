# Week 2: Abstract Vector Spaces

*9 problems*

## Topics Covered
- Basis and dimension
- Dimension of vector spaces
- Linear independence
- Polynomial vector spaces
- Spanning sets
- Subspace properties
- Vector space axioms

---

## Problem Q1-P01

**Week 2** | **Abstract Vector Spaces**
**Concepts:** Polynomial vector spaces, Dimension of vector spaces, Basis and dimension

Consider the vector space $\mathcal{P}_3$ of polynomials of degree at most 3. The dimension of this space is:

**Choices:**
- (A) 2
- (B) 3
- (C) 4
- (D) infinite
- (E) Cannot be determined without additional information

<details>
<summary>Show Answer</summary>

**Correct: (C)**

The space $\mathcal{P}_3$ consists of all polynomials of the form:
$$p(x) = a_0 + a_1x + a_2x^2 + a_3x^3$$

A standard basis is $\{1, x, x^2, x^3\}$, which has 4 elements. Therefore, $\dim(\mathcal{P}_3) = 4$.

**Key Insight:** The subscript in $\mathcal{P}_n$ denotes the maximum degree, not the dimension. The dimension is always $n+1$.

**Watch Out:**
- Students often confuse "degree at most 3" with "exactly degree 3" or think the dimension equals the maximum degree.

</details>

---

## Problem Q1-P04

**Week 2** | **Abstract Vector Spaces**
**Concepts:** Vector space axioms

Consider the following sets with standard addition and scalar multiplication operations. Which one forms a vector space?

**Choices:**
- (A) The set of all $2 \times 2$ matrices with determinant equal to 1
- (B) The set of all continuous functions $f: [0,1] \to \mathbb{R}$ such that $f(0) = f(1) = 0$
- (C) The set of all vectors $(x, y, z) \in \mathbb{R}^3$ such that $x + y + z = 1$
- (D) The set of all $2 \times 2$ matrices $A$ such that $A^2 = A$ (idempotent matrices)
- (E) The set $\{(x, y) \in \mathbb{R}^2 : x \geq 0, y \geq 0\}$ (the first quadrant)

<details>
<summary>Show Answer</summary>

**Correct: (B)**

Let's check each option:

\textbf{(A) Matrices with det = 1:} Fails closure under addition. If $\det(A) = \det(B) = 1$, generally $\det(A+B) \neq 1$.

\textbf{(B) Functions with $f(0) = f(1) = 0$:} ✓ This works!
\begin{itemize}
\item Zero function satisfies the condition
\item If $f(0) = g(0) = 0$ and $f(1) = g(1) = 0$, then $(f+g)(0) = 0$ and $(f+g)(1) = 0$
\item If $f(0) = f(1) = 0$, then $(cf)(0) = cf(0) = 0$ and $(cf)(1) = cf(1) = 0$
\end{itemize}

\textbf{(C) Vectors with $x+y+z=1$:} Not a subspace; doesn't contain zero vector.

\textbf{(D) Idempotent matrices:} Fails closure. If $A^2 = A$ and $B^2 = B$, generally $(A+B)^2 \neq A+B$.

\textbf{(E) First quadrant:} Fails closure under negative scalar multiplication.

**Key Insight:** Always check: (1) Contains zero? (2) Closed under addition? (3) Closed under scalar multiplication?

</details>

---

## Problem Q1-P09

**Week 2** | **Abstract Vector Spaces**
**Concepts:** Linear independence, Dimension of vector spaces, Basis and dimension

Consider the set of Euclidean vectors 
\[
    S = \left\{
    \begin{pmatrix}1\\2\\0\end{pmatrix}, 
    \begin{pmatrix}0\\1\\1\end{pmatrix}, 
    \begin{pmatrix}1\\3\\1\end{pmatrix}
    \right\}
\]
Which statement about $S$ is most correct?

**Choices:**
- (A) $S$ spans $\mathbb{R}^3$
- (B) $S$ is linearly independent but does not span $\mathbb{R}^3$
- (C) $S$ is linearly dependent and does not span $\mathbb{R}^3$
- (D) $S$ is linearly dependent and spans $\mathbb{R}^3$
- (E) $S$ forms a basis for $\mathbb{R}^3$

<details>
<summary>Show Answer</summary>

**Correct: (C)**

Notice that:
$$\begin{pmatrix}1\\3\\1\end{pmatrix} = \begin{pmatrix}1\\2\\0\end{pmatrix} + \begin{pmatrix}0\\1\\1\end{pmatrix}$$

This shows linear dependence. Since we have only 2 independent vectors in $\mathbb{R}^3$, the set cannot span the entire space.

**Partial Credit:**
- (E) Correctly identifies that only two vectors are independent

**Watch Out:**
- Three vectors in $\mathbb{R}^3$ aren't automatically a basis—check for independence!

</details>

---

## Problem Q1-P10

**Week 2** | **Abstract Vector Spaces**
**Concepts:** Subspace properties

Let $W_1$ and $W_2$ be subspaces of a vector space $V$. Which of the following is always a subspace of $V$?

**Choices:**
- (A) $W_1 \cup W_2$ (the union of $W_1$ and $W_2$)
- (B) $W_1 \cap W_2$ (the intersection of $W_1$ and $W_2$)
- (C) The set of all vectors in $W_1$ but not in $W_2$
- (D) The set of all vectors in $V$ but not in $W_1+W_2$
- (E) The quotient spaces $V/W_1$ and $V/W_2$

<details>
<summary>Show Answer</summary>

**Correct: (B)**

\begin{itemize}
\item \textbf{(A) Union:} Generally NOT a subspace. Example: $x$-axis ∪ $y$-axis in $\mathbb{R}^2$
\item \textbf{(B) Intersection:} Always a subspace! ✓
  \begin{itemize}
  \item Contains zero (in both subspaces)
  \item Closed under addition and scalar multiplication
  \end{itemize}
\item \textbf{(C) Set difference:} Not closed under scalar multiplication
\item \textbf{(D) Complement of sum:} Not closed under operations
\item \textbf{(E) Quotient spaces:} These ARE subspaces but of $V/W_i$, not of $V$
\end{itemize}

**Key Insight:** Intersection preserves all subspace properties; union typically doesn't.

</details>

---

## Problem Q1-P11

**Week 2** | **Abstract Vector Spaces**
**Concepts:** Subspace properties, Dimension of vector spaces, Basis and dimension, Polynomial vector spaces

Let $V$ be the vector space of all $3 \times 3$ symmetric matrices. Which of the following is the dimension of $V$?

**Choices:**
- (A) 2
- (B) 3
- (C) 4
- (D) 6
- (E) None of the above

<details>
<summary>Show Answer</summary>

**Correct: (D)**

A $3 \times 3$ symmetric matrix has the form:
$$\begin{bmatrix} a & b & c \\ b & d & e \\ c & e & f \end{bmatrix}$$

Count the independent parameters:
\begin{itemize}
\item Diagonal: 3 parameters $(a, d, f)$
\item Upper triangle: 3 parameters $(b, c, e)$
\item Total: 6 dimensions
\end{itemize}

Formula: For $n \times n$ symmetric matrices, $\dim = \frac{n(n+1)}{2}$

**Partial Credit:**
- (B) 3 - counts only diagonal

</details>

---

## Problem Q1-P15

**Week 2** | **Abstract Vector Spaces**
**Concepts:** Basis and dimension, Dimension of vector spaces, Spanning sets

Let $V$ be a 4-dimensional vector space. Suppose $S = \{\mathbf{v_1, v_2, v_3, v_4, v_5}\}$ is a set of vectors in $V$ where $\{\mathbf{v_1, v_2, v_3, v_4}\}$ forms a basis for $V$. Which of the following must be TRUE about $\mathbf{v}_5$?

**Choices:**
- (A) $\mathbf{v}_5 = \mathbf{0}$ (the zero vector)
- (B) $\mathbf{v}_5$ can be uniquely written as a linear combination of $\mathbf{v_1, v_2, v_3, v_4}$
- (C) $\mathbf{v}_5$ is linearly independent from any three vectors chosen from $\{\mathbf{v_1, v_2, v_3, v_4}\}$
- (D) The set $\{\mathbf{v_2, v_3, v_4, v_5}\}$ cannot be a basis for $V$
- (E) The set $S$ is linearly independent

<details>
<summary>Show Answer</summary>

**Correct: (B)**

Since $\{\mathbf{v_1, v_2, v_3, v_4}\}$ is a basis for the 4-dimensional space $V$:
\begin{itemize}
\item Every vector in $V$ (including $\mathbf{v}_5$) can be written as a linear combination of the basis
\item This representation is unique (fundamental property of bases)
\item $\mathbf{v}_5$ need not be zero (option A is wrong)
\item The set $S$ is linearly dependent since it has 5 vectors in a 4D space
\end{itemize}

**Key Insight:** In an $n$-dimensional space, any set of more than $n$ vectors must be linearly dependent.

</details>

---

## Problem Q1-P20

**Week 2** | **Abstract Vector Spaces**
**Concepts:** Linear independence, Spanning sets, Basis and dimension

Let $V$ be a vector space and $S = \{\mathbf{v_1, v_2, ..., v_n}\}$ be a set of vectors in $V$. If every vector in $V$ can be written as a linear combination of vectors in $S$, then which statement is true by definition?

**Choices:**
- (A) $S$ is a basis for $V$
- (B) $S$ is linearly independent
- (C) The dimension of $V$ is at most $n$
- (D) The dimension of $V$ is exactly $n$
- (E) $S$ spans $V$

<details>
<summary>Show Answer</summary>

**Correct: (E)**

The problem statement exactly describes the definition of "$S$ spans $V$."

\begin{itemize}
\item This doesn't imply $S$ is a basis (need linear independence too)
\item This doesn't imply $S$ is linearly independent
\item While (C) is true (can't span with fewer than $\dim(V)$ vectors), it's a theorem, not the definition
\end{itemize}

**Key Insight:** "Spans" means exactly "every vector can be written as a linear combination."

**Partial Credit:**
- (C) True but not "by definition"

</details>

---

## Problem Q1-P21

**Week 2** | **Abstract Vector Spaces**
**Concepts:** Linear independence, Polynomial vector spaces

In $\mathcal{P}_2$, consider the set $S = \{1+x, x+x^2, 1+x^2\}$. This set is:

**Choices:**
- (A) Linearly independent and spans $\mathcal{P}_2$
- (B) Linearly independent but does not span $\mathcal{P}_2$
- (C) Linearly dependent and spans $\mathcal{P}_2$
- (D) Linearly dependent and does not span $\mathcal{P}_2$
- (E) None of the above

<details>
<summary>Show Answer</summary>

**Correct: (A)**

Check linear independence by setting up:
$$c_1(1+x) + c_2(x+x^2) + c_3(1+x^2) = 0$$

This gives the system:
\begin{align}
c_1 + c_3 &= 0 \quad \text{(constant term)}\\
c_1 + c_2 &= 0 \quad \text{(coefficient of } x\text{)}\\
c_2 + c_3 &= 0 \quad \text{(coefficient of } x^2\text{)}
\end{align}

The only solution is $c_1 = c_2 = c_3 = 0$, so the set is linearly independent.

Since we have 3 independent vectors in the 3-dimensional space $\mathcal{P}_2$, they form a basis.

</details>

---

## Problem Q1-P25

**Week 2** | **Abstract Vector Spaces**
**Concepts:** Subspace properties

Consider the subset $S = \{(x, y, z)^T \in \mathbb{R}^3 : x + y + z = 1\}$. Under standard vector addition and scalar multiplication, which property does $S$ violate to be a subspace?

**Choices:**
- (A) Closure under addition
- (B) Closure under scalar multiplication
- (C) Contains the zero vector
- (D) Both (A) and (C)
- (E) All three: (A), (B), and (C)

<details>
<summary>Show Answer</summary>

**Correct: (E)**

The set $S = \{(x,y,z) : x+y+z = 1\}$ is an affine space (shifted plane).

Check all three properties:
\begin{enumerate}
\item \textbf{Zero vector:} $(0,0,0) \notin S$ since $0+0+0 = 0 \neq 1$ ✗
\item \textbf{Addition:} If $\mathbf{u}, \mathbf{v} \in S$, then sum of coordinates of $\mathbf{u}+\mathbf{v}$ is $1+1 = 2 \neq 1$ ✗
\item \textbf{Scalar multiplication:} If $\mathbf{u} \in S$ and $c \neq 1$, then sum of coordinates of $c\mathbf{u}$ is $c \cdot 1 = c \neq 1$ ✗
\end{enumerate}

All three properties fail!

**Key Insight:** Any affine space (not through origin) fails all subspace properties.

**Partial Credit:**
- (D) Identifies two violations correctly

**Watch Out:**
- (A) Only identifies one violation
- (B) Only identifies one violation
- (C) Only identifies the zero vector issue

</details>

---
