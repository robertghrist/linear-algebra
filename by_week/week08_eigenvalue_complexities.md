# Week 8: Eigenvalue Complexities

*9 problems*

## Topics Covered
- Basis and dimension
- Jordan canonical form
- Jordan form
- Matrix exponentials
- ODEs
- QR algorithm
- Schur form
- Taylor series
- complex eigenvalues
- convergence
- eigenvalue computation
- eigenvalues
- repeated eigenvalues
- similarity transformations
- stability

---

## Problem Q4-P02

**Week 8** | **Eigenvalue Complexities**
**Concepts:** Basis and dimension

The linear differential equation $\displaystyle \frac{d^3x}{dt^3} + a\frac{d^2x}{dt^2} + b\frac{dx}{dt} + cx = 0$ has companion matrix with eigenvalues $\lambda_1 = 2$ and $\lambda_{2,3} = -1 \pm 3i$.

Which set is the most natural basis for the solution space?

**Choices:**
- (A) $\{e^{2t}, e^{(-1+3i)t}, e^{(-1-3i)t}\}$
- (B) $\{e^{2t}, e^{-t}\cos(3t), e^{-t}\sin(3t)\}$
- (C) $\{e^{2t}, te^{2t}, t^2e^{2t}\}$
- (D) $\{e^{2t}, e^{-t}, \cos(3t), \sin(3t)\}$
- (E) $\{2e^{2t}, -e^{-t}, e^{-t}\cos(3t), e^{-t}\sin(3t)\}$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q4-P04

**Week 8** | **Eigenvalue Complexities**
**Concepts:** Matrix exponentials, Jordan form, repeated eigenvalues

Consider a $4 \times 4$ matrix in Jordan canonical form where all eigenvalues equal 2. Which of the following matrices can be $e^{Jt}$ for some such Jordan form $J$?
\[
\displaystyle
\textbf{I.} \begin{bmatrix} e^{2t} & te^{2t} & 0 & 0 \\ 0 & e^{2t} & 0 & 0 \\ 0 & 0 & e^{2t} & te^{2t} \\ 0 & 0 & 0 & e^{2t} \end{bmatrix}
\quad
\textbf{II.} \begin{bmatrix} e^{2t} & te^{2t} & t^2e^{2t} & 0 \\ 0 & e^{2t} & te^{2t} & 0 \\ 0 & 0 & e^{2t} & 0 \\ 0 & 0 & 0 & e^{2t} \end{bmatrix}
\]
\[
\displaystyle\textbf{III.} \begin{bmatrix} e^{2t} & te^{2t} & \frac{t^2}{2}e^{2t} & 0 \\ 0 & e^{2t} & te^{2t} & 0 \\ 0 & 0 & e^{2t} & 0 \\ 0 & 0 & 0 & e^{2t} \end{bmatrix}
\quad
\textbf{IV.} \begin{bmatrix} e^{2t} & te^{2t} & 0 & 0 \\ 0 & e^{2t} & \frac{t^2}{2}e^{2t} & 0 \\ 0 & 0 & e^{2t} & te^{2t} \\ 0 & 0 & 0 & e^{2t} \end{bmatrix}
\]

**Choices:**
- (A) I and III only
- (B) II and IV only
- (C) I, II, and III only
- (D) III only
- (E) I, II, III, and IV

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q4-P05

**Week 8** | **Eigenvalue Complexities**
**Concepts:** Basis and dimension

A third-order differential equation is given by:
$$\frac{d^3x}{dt^3} - 4\frac{d^2x}{dt^2} + 5\frac{dx}{dt} - 2x = 0$$

This equation can be converted to a first-order system $\frac{d\mathbf{v}}{dt} = C\mathbf{v}$ where $\mathbf{v} = (x, \dot{x}, \ddot{x})^T$ and $C$ is the $3 \times 3$ companion matrix.

Which statement correctly relates the ODE to the matrix $C$?

**Choices:**
- (A) The eigenvalues of $C$ are $-4, 5, -2$ from the ODE coefficients
- (B) The trace of $C$ equals $-4 + 5 + (-2) = -1$
- (C) The characteristic polynomial of $C$ is $\lambda^3 - 4\lambda^2 + 5\lambda - 2 = 0$
- (D) Matrix $C$ must be symmetric because the ODE has real coefficients
- (E) The solution spaces of the ODE and matrix system have different dimensions

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q4-P06

**Week 8** | **Eigenvalue Complexities**
**Concepts:** Jordan canonical form, complex eigenvalues, repeated eigenvalues

Consider the following three $6 \times 6$ matrices. Which of them are in (real) Jordan canonical form?

{\small
\[
\mathcal{M}_1 = \begin{bmatrix}
2 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & -3 & 0 & 0 & 0 \\
0 & 3 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 4 & 1 & 0 \\
0 & 0 & 0 & 0 & 4 & 0 \\
0 & 0 & 0 & 0 & 0 & 4
\end{bmatrix}
\quad
\mathcal{M}_2 = \begin{bmatrix}
2 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 3 & 0 & 0 & 0 \\
0 & -3 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 4 & 1 & 0 \\
0 & 0 & 0 & 0 & 4 & 0 \\
0 & 0 & 0 & 0 & 0 & 5
\end{bmatrix}
\quad
\mathcal{M}_3 = \begin{bmatrix}
1 & -3 & 0 & 0 & 0 & 0 \\
3 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 4 & 1 & 0 & 0 \\
0 & 0 & 0 & 4 & 1 & 0 \\
0 & 0 & 0 & 0 & 4 & 0 \\
0 & 0 & 0 & 0 & 0 & 2
\end{bmatrix}
\]
}

**Choices:**
- (A) Only $\mathcal{M}_1$
- (B) Only $\mathcal{M}_2$
- (C) Only $\mathcal{M}_3$
- (D) Only $\mathcal{M}_1$ and $\mathcal{M}_3$
- (E) All of them

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q4-P09

**Week 8** | **Eigenvalue Complexities**
**Concepts:** Matrix exponentials, complex eigenvalues, Taylor series

Consider the $2 \times 2$ real Jordan block corresponding to complex eigenvalues $\alpha \pm i\beta$:
$$A = \begin{bmatrix} \alpha & -\beta \\ \beta & \alpha \end{bmatrix} = \alpha I + \beta J = \begin{bmatrix} \alpha & 0 \\ 0 & \alpha \end{bmatrix} +
\begin{bmatrix} 0 & -\beta \\ \beta & 0 \end{bmatrix}$$

When computing $e^{At}$ one has:
$$e^{At} = e^{\alpha t}\begin{bmatrix} \cos(\beta t) & -\sin(\beta t) \\ \sin(\beta t) & \cos(\beta t) \end{bmatrix}$$

Why do the trigonometric functions $\cos(\beta t)$ and $\sin(\beta t)$ appear in this result?

**Choices:**
- (A) Complex eigenvalues always produce oscillatory behavior, which is mathematically represented by trigonometric functions
- (B) The skew-symmetric part $\beta J$ satisfies $J^2 = -I$, causing the Taylor series to separate into even/odd terms that match the series for $\cos(\beta t)$ and $\sin(\beta t)$
- (C) The matrix $J$ represents a rotation, and rotations are always described by sines and cosines
- (D) Euler's formula $e^{i\beta t} = \cos(\beta t) + i\sin(\beta t)$ is directly applied to the matrix exponential
- (E) The determinant of $A$ equals $\alpha^2 + \beta^2$, which forces the exponential to have magnitude 1, requiring unit circle parameterization via trigonometric functions

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q4-P12

**Week 8** | **Eigenvalue Complexities**
**Concepts:** QR algorithm, similarity transformations, eigenvalue computation

The QR algorithm for computing eigenvalues proceeds iteratively: given $A_k$, we factor $A_k = Q_k R_k$ (QR decomposition), then form $A_{k+1} = R_k Q_k$ (reverse the order).

Why is the reversed multiplication $A_{k+1} = R_k Q_k$  essential for the algorithm to work?

**Choices:**
- (A) $R_k Q_k$ is upper triangular while $Q_k R_k$ is not, allowing eigenvalues to appear on the diagonal
- (B) $R_k Q_k$ uses the fact that matrix multiplication is not commutative to generate new matrices
- (C) $Q_k R_k = A_k$ would just return the original matrix, making no progress toward convergence
- (D) $R_k Q_k$ is similar to $A_k$ via $A_{k+1} = Q_k^T A_k Q_k$, preserving eigenvalues across iterations
- (E) $R_k Q_k$ is symmetric when $A_k$ is symmetric, while $Q_k R_k$ may not be

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q4-P16

**Week 8** | **Eigenvalue Complexities**
**Concepts:** Basis and dimension

The general solution to a third-order linear differential equation 
$$\frac{d^3x}{dt^3} + a\frac{d^2x}{dt^2} + b\frac{dx}{dt} + cx = 0$$
is found to be:
$$x(t) = c_1 e^{-2t} + c_2 e^{3t} + c_3 te^{3t}$$

What can be concluded about the companion matrix $C$ for this differential equation?

**Choices:**
- (A) $C$ has three distinct eigenvalues
- (B) $C$ has eigenvalue $\lambda = 3$ appearing twice in the characteristic polynomial, with a 2-dimensional eigenspace
- (C) $C$ has eigenvalue $\lambda = 3$ appearing twice in the characteristic polynomial, with a 1-dimensional eigenspace
- (D) $C$ has eigenvalue $\lambda = 3$ with a 2-dimensional eigenspace, but only one basis solution because the other eigenvector produces the same exponential
- (E) None of the above can be concluded

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q4-P17

**Week 8** | **Eigenvalue Complexities**
**Concepts:** QR algorithm, convergence, Schur form

A real $5 \times 5$ matrix $A$ has eigenvalues $\lambda_{1,2} = 3$ (sharing an eigenvector), $\lambda_{3,4} = 1 \pm 2i$, and $\lambda_5 = -1$.

When the QR algorithm is applied to $A$ repeatedly, what is the structure of the limiting form?

**Choices:**
- (A) Diagonal with entries $3, 3, -1$ and two complex entries
- (B) Jordan canonical form with appropriate Jordan blocks
- (C) Upper triangular with all five eigenvalues on the diagonal
- (D) Block upper triangular: three $1 \times 1$ blocks and one $2 \times 2$ block
- (E) The algorithm cannot converge due to the repeated eigenvalue

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q4-P22

**Week 8** | **Eigenvalue Complexities**
**Concepts:** ODEs, eigenvalues, stability

A damped harmonic oscillator is described by the second-order differential equation:
$$m\frac{d^2x}{dt^2} + c\frac{dx}{dt} + kx = 0$$

The companion matrix for this system has eigenvalues that depend on $c$, $m$, and $k$. Which eigenvalue pattern corresponds to damped oscillations (decaying oscillatory motion)?

**Choices:**
- (A) Two distinct real negative eigenvalues
- (B) Two complex conjugate eigenvalues with negative real part
- (C) A repeated real negative eigenvalue
- (D) Two distinct real positive eigenvalues
- (E) Two complex conjugate eigenvalues with positive real part

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---
