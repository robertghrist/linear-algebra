# Quiz 1: Weeks 1-3

*25 problems*

## Week Breakdown
- Week 1 (Solving Linear Systems): 7 problems
- Week 2 (Abstract Vector Spaces): 9 problems
- Week 3 (Linear Transformations): 9 problems

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

## Problem Q1-P02

**Week 1** | **Solving Linear Systems**
**Concepts:** Triangular system solving

For the lower triangular system $L\mathbf{x} = \mathbf{b}$ where $L = \begin{bmatrix} 2 & 0 & 0 \\ 1 & 3 & 0 \\ 4 & -1 & 5 \end{bmatrix}$, which statement about solving this system is most accurate?

**Choices:**
- (A) One should use row reduction to find the solution
- (B) The system may have no solutions, depending on $\mathbf{b}$
- (C) One should solve by forward substitution
- (D) The system may have infinitely many solutions depending on $\mathbf{b}$
- (E) One should solve by backward substitution

<details>
<summary>Show Answer</summary>

**Correct: (C)**

For a lower triangular system $L\mathbf{x} = \mathbf{b}$:
\begin{itemize}
\item Since $L$ has nonzero diagonal entries, it's invertible, so there's always a unique solution
\item Forward substitution is the most efficient method:
  \begin{enumerate}
  \item Solve $2x_1 = b_1$ to get $x_1 = b_1/2$
  \item Substitute into second equation: $x_1 + 3x_2 = b_2$
  \item Continue forward through the system
  \end{enumerate}
\item Backward substitution is for upper triangular systems
\end{itemize}

**Key Insight:** Forward = Lower, Backward = Upper (alphabetical order helps remember!)

**Partial Credit:**
- (A) Row reduction is possible but inefficient

</details>

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

## Problem Q1-P06

**Week 1** | **Solving Linear Systems**
**Concepts:** Elementary row operations, Determinants, Matrix invertibility

Let $E$ be an elementary matrix used for row reduction. Which statement must be TRUE?

**Choices:**
- (A) $\det(E) = 1$
- (B) $\det(E) = \pm 1$
- (C) $\det(E) \neq 0$
- (D) $\det(E^{-1}) = -\det(E)$
- (E) $\det(EA) = \det(A)$ for any matrix $A$

<details>
<summary>Show Answer</summary>

**Correct: (C)**

Elementary matrices correspond to three types of row operations:
\begin{enumerate}
\item Row swaps: $\det(E) = -1$
\item Row scaling by $c$: $\det(E) = c \neq 0$
\item Adding multiple of one row to another: $\det(E) = 1$
\end{enumerate}

All elementary matrices are invertible (operations can be undone), so $\det(E) \neq 0$ always.

**Partial Credit:**
- (E) Only true for row swaps

**Watch Out:**
- (A) Only true for row addition operations
- (B) True for swaps and row additions, but not scaling
- (D) Should be det(E^{-1}) = 1/det(E)
- (E) Only true if det(E) = 1

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

## Problem Q1-P08

**Week 1** | **Solving Linear Systems**
**Concepts:** Permutation matrices, LU decomposition

Consider the permutation matrix $P = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix}$. Which of the following statements about $P$ is TRUE?

**Choices:**
- (A) $P^2 = I$
- (B) $P^3 = I$
- (C) $P^{-1} = -P$
- (D) $P^{-1} = P$
- (E) None of the above

<details>
<summary>Show Answer</summary>

**Correct: (B)**

This permutation matrix cycles rows: $1 \to 2 \to 3 \to 1$.

Computing powers:
\begin{itemize}
\item $P$ maps: row 1 → row 2, row 2 → row 3, row 3 → row 1
\item $P^2$ maps: row 1 → row 3, row 2 → row 1, row 3 → row 2
\item $P^3$ maps: row 1 → row 1, row 2 → row 2, row 3 → row 3 (identity!)
\end{itemize}

For this 3-cycle: $P^{-1} = P^2 \neq P$ (unlike 2-cycles where $P^{-1} = P$).

**Key Insight:** For an $n$-cycle permutation, $P^n = I$.

**Partial Credit:**
- (D) $P^{-1

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

## Problem Q1-P13

**Week 1** | **Solving Linear Systems**
**Concepts:** LU decomposition

Consider a square matrix $A$ that has an LU decomposition $A = LU$. Which of the following statements is necessarily TRUE?

**Choices:**
- (A) $A$ is nonsingular if and only if all diagonal entries of $L$ are nonzero
- (B) $A$ is singular if and only if the last diagonal entry of $U$ equals zero
- (C) The existence of an LU decomposition guarantees that $A$ is nonsingular
- (D) If $A$ is nonsingular, then both $L$ and $U$ must have positive diagonal entries
- (E) $A$ is nonsingular if and only if all diagonal entries of $U$ are nonzero

<details>
<summary>Show Answer</summary>

**Correct: (E)**

\begin{itemize}
\item In standard LU decomposition, $L$ has 1's on the diagonal (by convention)
\item Therefore, $L$ is always invertible
\item Since $A = LU$ and $\det(A) = \det(L)\det(U) = \det(U)$
\item For triangular matrices: nonsingular ⟺ all diagonal entries nonzero
\item Thus: $A$ nonsingular ⟺ $U$ nonsingular ⟺ all diagonal entries of $U$ are nonzero
\end{itemize}

**Partial Credit:**
- (B) Close but says "last" instead of "all"; (D) Wrong—signs don't matter

</details>

---

## Problem Q1-P14

**Week 1** | **Solving Linear Systems**
**Concepts:** LU decomposition

For a square matrix $A$ with LU decomposition $A = LU$, which statement is always true?

**Choices:**
- (A) The matrix $L$ is invertible
- (B) The matrix $U$ is invertible
- (C) The system $A\mathbf{x} = \mathbf{b}$ has a unique solution for any $\mathbf{b}$
- (D) The reduced row eschelon form (RREF) of $A$ is the identity
- (E) The determinant of $A$ equals the determinant of $L$

<details>
<summary>Show Answer</summary>

**Correct: (A)**

By convention in LU decomposition:
\begin{itemize}
\item $L$ is lower triangular with 1's on the diagonal
\item This guarantees $\det(L) = 1 \neq 0$
\item Therefore, $L$ is always invertible
\item $U$ may have zeros on diagonal (singular case)
\item The other options depend on whether $A$ is singular
\end{itemize}

**Key Insight:** The "L" in LU always has unit diagonal, making it invertible by construction.

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

## Problem Q1-P16

**Week 1** | **Solving Linear Systems**
**Concepts:** Linear systems, row reduction, pivots

Consider the system $A\mathbf{x} = \mathbf{b}$ where $A$ is a $3 \times 3$ matrix. If row reduction of the augmented matrix $[\, A\, |\, \mathbf{b}\, ]$ yields exactly two pivots, which statement must be TRUE?

**Choices:**
- (A) The system has a unique solution
- (B) The system has infinitely many solutions if it has any solution at all
- (C) The system is inconsistent
- (D) The matrix $A$ is invertible
- (E) None of the above

<details>
<summary>Show Answer</summary>

**Correct: (B)**

With 2 pivots in a $3 \times 3$ system:
\begin{itemize}
\item One row lacks a pivot (becomes a zero row or inconsistent row)
\item If the third row is $[0\ 0\ 0\ |\ b_3]$ with $b_3 \neq 0$: inconsistent
\item If the third row is $[0\ 0\ 0\ |\ 0]$: one free variable → infinitely many solutions
\item The system either has no solutions or infinitely many (never unique)
\end{itemize}

**Key Insight:** Number of free variables = number of columns minus number of pivots in coefficient matrix.

**Partial Credit:**
- (E) Ambiguity about pivot location

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

## Problem Q1-P24

**Week 1** | **Solving Linear Systems**
**Concepts:** Elementary row operations

If $B$ is obtained from matrix $A$ by first swapping rows 1 and 2, then adding 2 times row 1 to row 3, which equation correctly relates them?

**Choices:**
- (A) $B = E_2 E_1 A$ where $E_1$ swaps rows 1 and 2, $E_2$ adds 2 times row 1 to row 3
- (B) $B = E_1 E_2 A$ where $E_1$ swaps rows 1 and 2, $E_2$ adds 2 times row 1 to row 3
- (C) $B = A E_1 E_2$ where $E_1$ swaps rows 1 and 2, $E_2$ adds 2 times row 1 to row 3
- (D) $B = (E_2 E_1)^{-1} A$
- (E) None of the above

<details>
<summary>Show Answer</summary>

**Correct: (A)**

Elementary matrices apply from right to left:
\begin{enumerate}
\item First operation: $E_1 A$ swaps rows 1 and 2
\item Second operation: $E_2(E_1 A)$ adds 2 times (new) row 1 to row 3
\end{enumerate}

The key insight: After swapping, "row 1" in the second operation refers to what was originally row 2.

**Watch Out:**
- Matrix multiplication is right-to-left, but we describe operations left-to-right!

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
