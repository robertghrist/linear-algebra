# Week 9: Linear Iterative Systems

*11 problems*

## Topics Covered
- Dominant eigenvalue
- Graph Laplacian
- Linear iteration
- Markov chains
- Perron-Frobenius theorem
- Power method
- Random walks
- Spectral Theorem
- Spectral radius
- Stochastic matrices
- complex eigenvalues
- connected components
- convergence
- convergence rate
- dominant eigenvalue
- eigenvalue magnitudes
- eigenvalue ratios
- eigenvalues
- graph structure
- long-term behavior
- orthogonal diagonalization
- orthogonality of eigenvectors
- positive matrices
- spectral radius
- stationary distribution applications
- symmetric matrices

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
