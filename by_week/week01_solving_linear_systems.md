# Week 1: Solving Linear Systems

*7 problems*

## Topics Covered
- Determinants
- Elementary row operations
- LU decomposition
- Linear systems
- Matrix invertibility
- Permutation matrices
- Triangular system solving
- pivots
- row reduction

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
