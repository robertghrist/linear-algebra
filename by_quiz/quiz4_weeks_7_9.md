# Quiz 4: Weeks 7-9

*22 problems*

## Week Breakdown
- Week 7 (Diagonalization & Dynamics): 2 problems
- Week 8 (Eigenvalue Complexities): 9 problems
- Week 9 (Linear Iterative Systems): 11 problems

---

## Problem Q4-P01

**Week 9** | **Linear Iterative Systems**
**Concepts:** Dominant eigenvalue, spectral radius, convergence rate

A matrix $B$ has eigenvalues $\lambda_1 = 3$, $\lambda_2 = -4$, $\lambda_3 = 0$, and $\lambda_{4,5} = 1 \pm 2i$.

Which eigenvalue is dominant for the purpose of analyzing the convergence behavior of the power iteration $\mathbf{x}_k = B^k\mathbf{x}_0$?

**Choices:**
- (A) $\lambda_1 = 3$
- (B) $\lambda_2 = -4$
- (C) $\lambda_3 = 0$
- (D) $\lambda_{4,5} = 1 \pm 2i$
- (E) There is not necessarily a dominant eigenvalue

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

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

## Problem Q4-P03

**Week 9** | **Linear Iterative Systems**
**Concepts:** Spectral Theorem, symmetric matrices, orthogonal diagonalization

Let $A$ be a real symmetric $n \times n$ matrix with eigenvalues $\lambda_1, \ldots, \lambda_n$ and corresponding orthonormal eigenvectors $\mathbf{q}_1, \ldots, \mathbf{q}_n$. 

For any vector $\mathbf{x} \in \mathbb{R}^n$, we can write $\mathbf{x} = c_1\mathbf{q}_1 + \cdots + c_n\mathbf{q}_n$ where $c_i = \mathbf{q}_i^T\mathbf{x}$.

What is $\|A\mathbf{x}\|^2$ in terms of the eigenvalues and coefficients?

**Choices:**
- (A) $\lambda_1^2 c_1^2 + \cdots + \lambda_n^2 c_n^2$
- (B) $(\lambda_1 c_1 + \cdots + \lambda_n c_n)^2$
- (C) $\lambda_{\max}^2(c_1^2 + \cdots + c_n^2)$
- (D) $c_1^2 + \cdots + c_n^2$
- (E) $|\lambda_1 c_1| + \cdots + |\lambda_n c_n|$

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

## Problem Q4-P07

**Week 9** | **Linear Iterative Systems**
**Concepts:** Stochastic matrices, Markov chains, eigenvalues

A population model tracks the number of individuals in three age groups: juvenile, adult, and senior. The transition matrix $P$ describes how the population distribution changes each year, where column $j$ shows the probability of transitioning into each age group from group $j$.

The matrix $P$ has been found to have eigenvalues $\lambda_1 = 1$, $\lambda_2 = 0.6$, and $\lambda_3 = -0.2$, with corresponding eigenvector for $\lambda_1 = 1$ given by:
$\mathbf{v}_1 = \frac{1}{10}\begin{pmatrix} 2 \\ 5 \\ 3 \end{pmatrix}$

If the population distribution after $k$ years is $\mathbf{x}(k) = P^k\mathbf{x}(0)$, which statement is most accurate about the long-term behavior?

**Choices:**
- (A) As $k \to \infty$, the population distribution converges to $\mathbf{v}_1$
- (B) The dominant eigenvalue $\lambda_1 = 1$ means the total population remains constant over time
- (C) The eigenvalue $\lambda_3 = -0.2$ means the senior population will eventually become negative
- (D) Since $|\lambda_2| = 0.6 > |\lambda_3|$, the convergence is primarily controlled by the adult age group
- (E) As $k \to \infty$, all populations decay to zero because $\lambda_2$ and $\lambda_3$ are both less than 1

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q4-P08

**Week 9** | **Linear Iterative Systems**
**Concepts:** Graph Laplacian, eigenvalues, connected components

Consider a network of six computer servers. The graph Laplacian matrix $L = D - A$ (where $D$ is the degree matrix and $A$ is the adjacency matrix) is computed and found to have eigenvalues:
$$\lambda_1 = 0, \quad \lambda_2 = 0, \quad \lambda_3 = 2, \quad \lambda_4 = 3, \quad \lambda_5 = 4, \quad \lambda_6 = 5$$

A network engineer needs to understand the topology. What can be concluded from this eigenvalue information?

**Choices:**
- (A) The network is fully connected since all servers are represented in the Laplacian
- (B) The presence of $\lambda = 2$ indicates exactly two servers are isolated from the rest
- (C) Exactly two eigenvalues equal zero, indicating a computational error since graph Laplacians should have only one zero eigenvalue
- (D) The network consists of exactly two separate connected components
- (E) The network has six connected components, one for each eigenvalue

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

## Problem Q4-P10

**Week 9** | **Linear Iterative Systems**
**Concepts:** Linear iteration, convergence, long-term behavior

A $3 \times 3$ matrix $A$ has eigenvalues $\lambda_1 = 0.6$, $\lambda_2 = -0.8$, and $\lambda_3 = 0.4$, with corresponding linearly independent eigenvectors $\mathbf{v}_1$, $\mathbf{v}_2$, and $\mathbf{v}_3$.

Consider the iterative sequence $\mathbf{x}_k = A^k\mathbf{x}_0$ where $\mathbf{x}_0 = 2\mathbf{v}_1 + 3\mathbf{v}_2 + 5\mathbf{v}_3$.

Which statement best describes the long-term behavior of $\mathbf{x}_k$ as $k \to \infty$?

**Choices:**
- (A) The sequence converges to zero monotonically
- (B) The sequence converges toward the direction of $\mathbf{v}_1$, since $\lambda_1$ is dominant
- (C) The sequence grows without bound due to positive eigenvalues
- (D) The sequence converges to the direction of $\mathbf{v}_2$, but oscillating signs
- (E) All eigenvalues are real and distinct, so each eigencomponent of $\mathbf{x}_k$ acts independently

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q4-P11

**Week 9** | **Linear Iterative Systems**
**Concepts:** Perron-Frobenius theorem, positive matrices, dominant eigenvalue

Let $A$ be a square matrix with all entries strictly positive, to which the Perron-Frobenius theorem applies. Now consider the matrix $-A$ (all entries strictly negative). Which statement about $-A$ does Perron-Frobenius imply?

**Choices:**
- (A) $-A$ has a dominant real positive eigenvalue with positive eigenvector
- (B) $-A$ has a dominant real negative eigenvalue with positive eigenvector
- (C) $-A$ has a dominant real negative eigenvalue with negative eigenvector
- (D) Perron-Frobenius does not apply to $-A$, so nothing definite can be said about its eigenstructure
- (E) None of the above is entirely accurate

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

## Problem Q4-P13

**Week 9** | **Linear Iterative Systems**
**Concepts:** Power method, convergence rate, eigenvalue ratios

Two matrices have the following eigenvalue structures:

Matrix $A$: eigenvalues $10, 9, 1$

Matrix $B$: eigenvalues $10, 2, 1$

Both matrices are diagonalizable with linearly independent eigenvectors. The power method is applied to each matrix with generic initial conditions (containing components of all eigenvectors).

Which statement about the convergence rates is most accurate?

**Choices:**
- (A) Both converge at the same rate
- (B) Matrix $A$ converges faster
- (C) Matrix $B$ converges faster
- (D) The convergence rate depends on the initial condition, not the eigenvalues
- (E) The power method depends on Perron-Frobenius and may not be applicable here

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q4-P14

**Week 9** | **Linear Iterative Systems**
**Concepts:** Stochastic matrices, Markov chains, stationary distribution applications

A simplified model of customer loyalty tracks subscribers between three streaming services. Each month, customers switch services according to a transition matrix $P$ where column $j$ represents the probability distribution of where service $j$'s customers go:

$$P = \begin{bmatrix} 0.7 & 0.1 & 0.2 \\ 0.2 & 0.8 & 0.3 \\ 0.1 & 0.1 & 0.5 \end{bmatrix}$$

The market starts with 40\

After many months, what will the market share distribution be?

**Choices:**
- (A) 40\
- (B) 45\
- (C) 70\
- (D) Cannot be determined without computing the limit of $P^n$ as $n\to\infty$
- (E) Need to know the dominant eigenvector to determine this

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q4-P15

**Week 9** | **Linear Iterative Systems**
**Concepts:** Random walks, graph structure, symmetric matrices

A robot performs a random walk on a network of four rooms connected by doorways. At each time step, the robot moves to a randomly chosen adjacent room with equal probability. The transition matrix is:

$$P = \begin{bmatrix} 0 & 1/3 & 1/3 & 0 \\ 1/2 & 0 & 1/3 & 1/2 \\ 1/2 & 1/3 & 0 & 1/2 \\ 0 & 1/3 & 1/3 & 0 \end{bmatrix}$$

Assume this has all the nice properties (irreducible, etc) for a stationary distribution to exist (it does!). Note that rooms 1 and 4 have identical rows and columns in $P$. What does this symmetry imply about the long-term behavior?

**Choices:**
- (A) Over time, the robot spends the same time in room 1 as in room 4
- (B) The stationary distribution will have equal terms for rooms 2 and 3
- (C) At each time step, the robot visits rooms 2 and 3 with at least 50\
- (D) Rooms 1 and 4 have the same eigenvalue
- (E) The robot spends more time in rooms (2 and 3) than in rooms (1 and 4)

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

## Problem Q4-P19

**Week 9** | **Linear Iterative Systems**
**Concepts:** Spectral Theorem, orthogonality of eigenvectors, symmetric matrices

Let $A$ be a \textit{symmetric} $3 \times 3$ matrix with eigenvalues $\lambda_1 = 5$, $\lambda_2 = 3$, and $\lambda_3 = 3$. Using the convention that an eigenvector $\mathbf{v}_i$ always goes with the eigenvalue $\lambda_i$, which of the following statements is most correct?

**Choices:**
- (A) The eigenspace for $\lambda = 3$ has dimension 1, so only one of $\mathbf{v}_2$ or $\mathbf{v}_3$ exists
- (B) $\mathbf{v}_1$ must be orthogonal to both $\mathbf{v}_2$ and $\mathbf{v}_3$, but $\mathbf{v}_2$ and $\mathbf{v}_3$ need not be orthogonal since they share the same eigenvalue
- (C) All three eigenvectors exist, but we must apply Gram-Schmidt within the eigenspace for $\lambda = 3$ to make $\mathbf{v}_2$ and $\mathbf{v}_3$ orthogonal
- (D) The repeated eigenvalue means $A$ is not diagonalizable, so we cannot find three linearly independent eigenvectors
- (E) All three $\mathbf{v}_i$ exist and are mutually orthogonal

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q4-P20

**Week 9** | **Linear Iterative Systems**
**Concepts:** Spectral radius, eigenvalue magnitudes, complex eigenvalues

A $4 \times 4$ matrix $A$ has eigenvalues:
$$\lambda_1 = 2, \quad \lambda_2 = -3, \quad \lambda_3 = 1 + 2i, \quad \lambda_4 = 1 - 2i$$

What is the spectral radius $\rho(A)$?

**Choices:**
- (A) $\rho(A) = \sqrt{3}$
- (B) $\rho(A) = 3$
- (C) $\rho(A) = \sqrt{5}$
- (D) $\rho(A) = 5$
- (E) None of the above

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
