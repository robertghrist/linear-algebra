---
title: "Linear Algebra: Essence & Form"
author: Robert Ghrist
publisher: Agenbyte Press
edition: 2nd
isbn: 978-1-944655-12-9
copyright: "(c) 2024-2026 Robert Ghrist. All rights reserved worldwide."
format: markdown-with-latex-math
purpose: >
  Single-file corpus of the complete text, prepared for ingestion by language
  models, course assistants, question generators, and retrieval systems.
  Figures are omitted. All custom LaTeX macros have been expanded to standard
  commands, so this file is self-contained and requires no preamble.
conventions:
  math: "LaTeX, inline as `$...$` and display as `$$...$$`"
  numbering: >
    Theorems, definitions, examples, lemmas, and corollaries share a single
    counter within each chapter, so "Definition 3.12" and "Theorem 3.25" are
    distinct objects in Chapter 3. Cross-references in the text have been
    resolved to these numbers.
  marginalia: >
    The author's margin notes are rendered as blockquotes (lines beginning
    with ">"). They are commentary, questions, and asides, not main-line
    exposition.
  end_marks: "A Definition closes with $\\odot$; an Example closes with $\\otimes$."
  omitted: Figures, diagrams, and the five Blake plate pages.
---

# Linear Algebra: Essence & Form

**Robert Ghrist** · Agenbyte Press · Second edition

> **How to use this file.** This is the complete text of the book in a single
> Markdown document, with all mathematics in LaTeX. It is organised as:
> a table of contents; a notation glossary; a concept index of every numbered
> result; the thirteen chapters with their exercises; and a final appendix of
> brief answers. Chapter and section numbers are the book's own, so any
> citation of the form "Theorem 7.12" or "Section 4.3" refers to exactly the
> object that number names here and in the printed edition.

---

## Contents


*THARMAS — body / material (coimage)*

- **Chapter 1. Solving Linear Systems**
    - 1.1 Solving Equations
    - 1.2 Special Matrices
    - 1.3 Recalling Row Reduction
    - 1.4 Inverse & Invertibility
    - 1.5 Composition & Elimination
    - 1.6 LU Decomposition
    - 1.7 Pivots & Permutations
    - 1.8 Practicalities of Linear Systems
- **Chapter 2. Abstract Vector Spaces**
    - 2.1 Vector Space Axioms
    - 2.2 A Gallery of Vector Spaces
    - 2.3 Subspaces
    - 2.4 Span & Linear Independence
    - 2.5 Towards Dimension
- **Chapter 3. Linear Transformations**
    - 3.1 Euclidean Transformations
    - 3.2 Definitions & Implications
    - 3.3 Isomorphisms
    - 3.4 Image & Kernel
    - 3.5 Rank & Nullity
    - 3.6 Quotients
    - 3.7 Coimage & Cokernel
    - 3.8 The Fundamental Theorem

*URIZEN — reason (image)*

- **Chapter 4. Bases & Coordinates**
    - 4.1 Bases & Spanning Sets
    - 4.2 Coordinates & Components
    - 4.3 Change of Basis
    - 4.4 Matrix Representations
    - 4.5 Coordinate-Free Thought
- **Chapter 5. Inner Products & Orthogonality**
    - 5.1 Dot & Inner Products
    - 5.2 Angles & Orthogonality
    - 5.3 Orthogonal & Orthonormal Bases
    - 5.4 Adjoints & Transposes
    - 5.5 Orthogonal Transformations
    - 5.6 The QR Decomposition
- **Chapter 6. Orthogonal Decomposition & Data**
    - 6.1 Orthogonal Subspaces & Complements
    - 6.2 Projections & Quotients
    - 6.3 The Fundamental Theorem Redux
    - 6.4 The Pseudoinverse
    - 6.5 Least Squares Approximation
    - 6.6 Regularized Least Squares

*LUVAH — passion (kernel)*

- **Chapter 7. Diagonalization & Dynamics**
    - 7.1 The First Order
    - 7.2 Coupled First-Order Systems
    - 7.3 Eigenvalues & Eigenvectors
    - 7.4 Simple Diagonalization
    - 7.5 Matrix Exponentials
    - 7.6 Higher-Order Equations & Basis Solutions
- **Chapter 8. Eigenvalue Complexities**
    - 8.1 Complex Eigenvalues & Oscillation
    - 8.2 Repeated Eigenvalues
    - 8.3 The Jordan Canonical Form
    - 8.4 Computing Eigenvalues
    - 8.5 Back to Basis
- **Chapter 9. Linear Iterative Systems**
    - 9.1 At First Iteration
    - 9.2 Dominance & Convergence
    - 9.3 Positivity & Perron-Frobenius Theory
    - 9.4 Stochastic Matrices & Markov Chains
    - 9.5 Symmetric Matrices & Spectra
    - 9.6 Networked Behavior & Consensus

*URTHONA — imagination (cokernel)*

- **Chapter 10. Singular Value Decomposition**
    - 10.1 The Spectral Theorem
    - 10.2 Spheres, Ellipsoids, & Singular Values
    - 10.3 Constructing the SVD
    - 10.4 Interpreting the SVD
    - 10.5 Invariance & Natural Structure
    - 10.6 Inner Products & the SVD
- **Chapter 11. Principal Components & Low-Rank Structure**
    - 11.1 Covariance & Correlation
    - 11.2 Matrices & Data
    - 11.3 Principal Components
    - 11.4 Optimality Properties
    - 11.5 Judgment
    - 11.6 Completion & Corruption
    - 11.7 Beyond Linear PCA
- **Chapter 12. Probability & High Dimension**
    - 12.1 The Geometry of Expectation
    - 12.2 The Simplex
    - 12.3 High Dimension & Near-Orthogonality
    - 12.4 Random Matrices & the Noise Floor
    - 12.5 Random Projection
    - 12.6 The Randomized SVD

*ALBION — synthesis*

- **Chapter 13. Neural Networks & AI**
    - 13.1 Beyond Linear Transformations
    - 13.2 Network Architecture & Matrix Factorization
    - 13.3 Chains & Backpropagation
    - 13.4 Stochastic Gradient Descent
    - 13.5 Attention & Transformers
    - 13.6 Representation Learning
    - 13.7 Deep Linear Algebra

---

## Notation

The following symbols are used throughout. The "source macro" column records
the author's original LaTeX shorthand, which has been expanded everywhere in
this file; it is listed only to make the correspondence explicit.

| Symbol | Source macro | Meaning |
| --- | --- | --- |
| $\mathbb{R}$ | `\R` | the real numbers; $\mathbb{R}^n$ is real $n$-dimensional coordinate space |
| $\mathbb{C}$ | `\C` | the complex numbers |
| $\mathbb{Z}$ | `\Z` | the integers |
| $\mathbb{N}$ | `\N` | the natural numbers |
| $\mathbf{v}$ | `\vect{v}` | a vector (boldface); components are written $v_i$ |
| $\mathbf{0}$ | `\vect{0}` | the zero vector |
| $\cong$ | `\iso` | isomorphism of vector spaces |
| $<$ | — | between spaces, denotes "is a subspace of" (e.g. $U<V$), NOT a numerical inequality |
| $\mathrm{id}$ | `\id` | the identity transformation |
| $\operatorname{ker} T$ | `\ker` | kernel (null space) of $T$: all inputs sent to $\mathbf{0}$ |
| $\operatorname{im} T$ | `\im` | image of $T$: all attained outputs |
| $\operatorname{coker} T$ | `\coker` | cokernel of $T$, the quotient $W/\operatorname{im} T$ |
| $\operatorname{coim} T$ | `\coim` | coimage of $T$, the quotient $V/\operatorname{ker} T$ |
| $\operatorname{rank} T$ | `\rank` | rank: $\dim\operatorname{im} T$ |
| $\operatorname{null} T$ | `\nullity` | nullity: $\dim\operatorname{ker} T$ |
| $\operatorname{span}$ | `\spanset` | span of a set of vectors |
| $\operatorname{diag}$ | `\diag` | diagonal matrix, or the diagonal of a matrix |
| $\operatorname{tr}$ | `\trace` | trace of a square matrix |
| $\operatorname{row} A$ | `\row` | row space of $A$ |
| $\operatorname{col} A$ | `\column` | column space of $A$ |
| $\mathcal{B}$ | `\basis` | a basis |
| $\mathcal{P}$ | `\poly` | space of polynomials; $\mathcal{P}_n$ has degree at most $n$ |
| $\operatorname{sym}$ | `\sym` | symmetric matrices |
| $\operatorname{skew}$ | `\skewsym` | skew-symmetric matrices |
| $\mathcal{I}$ | `\inertia` | inertia tensor |
| $\boldsymbol{\sigma}$ | `\stress` | stress tensor |
| $\hat{\imath},\hat{\jmath},\hat{k}$ | `\ihat,\jhat,\khat` | standard basis vectors of $\mathbb{R}^3$ |
| $\Pi_U$ | `\proj{U}` | orthogonal projection operator onto $U$ |
| $\oplus$ | `\directsum` | direct sum |
| $\boxplus$ | `\orthosum` | orthogonal direct sum |
| $[C]$ | `\COV` | covariance matrix |
| $\operatorname{cov}$ | `\cov` | scalar covariance |
| $[R]$ | `\CORR` | correlation matrix |
| $\operatorname{corr}$ | `\corr` | scalar correlation |
| $\mathcal{X}$ | `\Data` | a data set / data matrix |
| $\operatorname{cond}$ | `\cond` | condition number |
| $\Psi$ | `\PARAM` | the parameters of a network |
| $\Lambda$ | `\NUMLAY` | the number of layers in a network |
| $\mathcal{L}$ | `\LOSS` | loss (cost) function |
| $\varsigma$ | `\activation` | activation function |
| $\hat{\mathbf{y}}$ | `\netout` | network output ($\mathbf{y}$ is reserved for true values) |
| $\operatorname{softmax},\ \operatorname{softplus}$ | `\softmax,\softplus` | the named nonlinearities |
| $A^T$ | — | transpose |
| $A^\dagger$ | — | pseudoinverse (Moore-Penrose), or conjugate transpose where noted |
| $\langle\cdot,\cdot\rangle$ | — | inner product |
| $\perp$ | — | orthogonality; $U^\perp$ is the orthogonal complement of $U$ |
| $\otimes$ | — | marks the end of an Example |
| $\odot$ | — | marks the end of a Definition |

---

## Concept Index

Every numbered definition, theorem, lemma, corollary, and example in the book,
in order, with a one-line statement. Use this to locate results by content.


### Chapter 1 — Solving Linear Systems

- **Definition 1.1** — Linear System: A **linear system** in variables $x_1,\ldots,x_n$ consists of $m$ equations of the form where the coefficients $a_{ij}$ and constants $b_i$ are real numbers.
- **Example 1.2** — Existence and Obstruction: Consider the system $A\mathbf{x}=\mathbf{b}$ with The task is not to solve the system for a given right-hand side — the row reduction of Section 1.3 dispatches…
- **Definition 1.3** — Permutation: A **permutation matrix** is a square matrix with exactly one $1$ per row and column, having all other entries equal to $0$.
- **Example 1.4** — Hidden Block Structure: Consider the linear system: The structure of this system is obscured, but becomes clear after permuting rows and columns to group related variables.
- **Definition 1.5** — Elementary Row Operations: An **elementary row operation** on a matrix is one of three types: R1: Interchange of any two rows R2: Multiplication of any row by a nonzero scalar R3:
- **Definition 1.6** — Row Echelon Form: A matrix is in **row echelon form** if: 1. All zero rows (if any) appear at the bottom 2.
- **Definition 1.7** — Nonsingularity: A square matrix $A$ is **nonsingular** if any of the following equivalent conditions hold: 1. There exists a matrix $A^{-1}$ such that $AA^{-1}=A^{-1}A=I$ 2.
- **Lemma 1.8** — Neumann Series: Let $A$ be a square matrix whose powers decay, $A^k\to 0$ entrywise as $k\to\infty$.
- **Definition 1.9** — LU Decomposition: An **LU decomposition** of a square matrix $A$ expresses it as a product $A = LU$, where $L$ is lower triangular (with ones on the diagonal) and $U$ is upper…
- **Example 1.10**: For a $3\times 3$ matrix, the $LU$ decomposition takes the form: where the $\ell_{ij}$ are the elimination multipliers.
- **Definition 1.11** — PLU Decomposition: A **PLU decomposition** of a matrix $A$ expresses it as a product $A=P^{-1}LU$ where: 1. $P$ is a permutation matrix 2.
- **Definition 1.12** — Matrix Rank: The **rank** of a matrix is the number of pivots in a row-reduced echelon form.
- **Example 1.13** — Row echelon computation: Consider the matrix *Mirabile dictu:* the $(1,1)$ entry is a perfect pivot. Clearing out the first column leads to a dramatic simplification;
- **Example 1.14**: Not all matrices are created equal in their amenability to computation.

### Chapter 2 — Abstract Vector Spaces

- **Definition 2.1** — Vector Space: A **vector space** consists of two ingredients:
- **Lemma 2.2**: In a vector space $V$, the zero vector is unique. *Proof.* Assume that $z$ and $z'$ are vectors in $V$ which satisfy the zero-property. Then:
- **Example 2.3** — Euclidean space: The space $\mathbb{R}^n$ of ordered $n$-tuples of real numbers is our prototype.
- **Example 2.4** — Matrices: The collection $\mathbb{R}^{m\times n}$ of all $m$-by-$n$ matrices forms a vector space under entry-by-entry addition and scalar multiplication.
- **Example 2.5** — Polynomials: For each nonnegative integer $n$, we have the space $\mathcal{P}_n$ of polynomials of degree at most $n$.
- **Example 2.6** — Function spaces: Consider the space $C([a,b])$ of continuous real-valued functions on an interval $[a,b]$, with addition and scalar multiplication defined pointwise.
- **Example 2.7** — Linear ODEs: The solutions to a linear homogeneous differential equation form a vector space.
- **Example 2.8** — Sequences & Series: Consider the set of formal power series in a variable $x$, as familiar from single-variable calculus.
- **Definition 2.9** — Subspace: A **subspace** of a vector space $V$ is a subset $W\subseteq V$ that is itself a vector space under the operations inherited from $V$.
- **Example 2.10** — Coordinate subspaces: In $\mathbb{R}^n$, the coordinate planes (and their higher-dimensional analogues) provide natural examples of subspaces.
- **Example 2.11** — Null space: The solutions to a linear homogeneous system $A\mathbf{x}=\mathbf{0}$ form a subspace called the **null space** of $A$.
- **Example 2.12** — Column space: Given a matrix $A$, the set of all possible linear combinations of its columns forms a subspace $\operatorname{col}(A)$ of $\mathbb{R}^m$ (where $m$ is the…
- **Definition 2.13** — Span: The **span** of vectors $\mathbf{v}_1,\ldots,\mathbf{v}_k$ in a vector space $V$ is the collection of all their linear combinations:
- **Example 2.14** — Spanning in $\mathbb{R}^2$: In the plane, two nonzero vectors $\mathbf{v}_1,\mathbf{v}_2$ that point in different directions span all of $\mathbb{R}^2$.
- **Example 2.15** — Spanning polynomials: The polynomials $1, x,$ and $x^2$ span the space $\mathcal{P}_2$ — any quadratic polynomial $ax^2 + bx + c$ is a linear combination of these basic building…
- **Definition 2.16** — Linear Independence: A set of vectors $\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}$ in a vector space $V$ is **linearly independent** if the equation has only the trivial solution…
- **Example 2.17** — Dependence in $\mathbb{R}^n$: Three vectors in $\mathbb{R}^2$ are always linearly dependent. This is intuitively clear:
- **Example 2.18** — Polynomial independence: The polynomials $1, x,$ and $x^2$ are linearly independent in $\mathcal{P}_2$. If $a + bx + cx^2 = 0$ for all $x$, then each coefficient $a,b,c$ must be zero.
- **Example 2.19** — Testing independence: Consider the Euclidean vectors $(1,2)^T$ and $(2,4)^T$ in $\mathbb{R}^2$.
- **Lemma 2.20** — Minimality & Independence: A spanning set for a vector space $V$ is minimal if and only if it is linearly independent.
- **Lemma 2.21** — Minimal Spanning Sets: Any two minimal spanning sets of a vector space $V$ have the same size.
- **Corollary 2.22** — Exchange Bound: If $\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}$ spans $V$ and the set $\{\mathbf{w}_1,\ldots,\mathbf{w}_m\}$ in $V$ is linearly independent, then $m\leq k$.
- **Definition 2.23** — Dimension: The **dimension** of a vector space $V$, denoted $\dim V$, is the size of any minimal spanning set for $V$.
- **Example 2.24** — Polynomial dimension: Consider the space $\mathcal{P}_n$ of polynomials of degree at most $n$.
- **Example 2.25** — Function spaces: The space $C([a,b])$ of continuous functions on a closed interval $[a,b]$ with $a<b$ has no finite spanning set.

### Chapter 3 — Linear Transformations

- **Definition 3.1** — Linear Transformation: Let $V$ and $W$ be vector spaces. A **linear transformation** $T:V\to W$ is a function satisfying two properties: 1. Additivity:
- **Lemma 3.2**: A linear transformation $T:V\to W$ satisfies: 1. $T(\mathbf{0})=\mathbf{0}$ 2. $T(-\mathbf{v})=-T(\mathbf{v})$ for all $\mathbf{v}\in V$ 3.
- **Lemma 3.3**: If $T:V\to W$ is linear and $U<V$, then $T(U)<W$. Linear transformations may themselves be combined.
- **Example 3.4** — Differentiation: Consider the differentiation operator $D=d/dx$ from calculus. This satisfies linearity in that $D(f+g)=Df+Dg$ for differentiable functions $f$ and $g$;
- **Example 3.5** — Integration: The definite integration operator $\mathrm{I}:C([a,b])\to\mathbb{R}$ defined by is, like differentiation, linear.
- **Definition 3.6** — Injective and Surjective: A linear transformation $T:V\to W$ is: 1. **injective** (or **one-to-one**) if distinct inputs yield distinct outputs:
- **Lemma 3.7**: For a linear transformation $T:V\to W$: 1. $T$ is injective if and only if it preserves linear independence 2. $T$ is surjective if and only if $T(V)=W$ 3.
- **Definition 3.8** — Isomorphism: Vector spaces $V$ and $W$ are **isomorphic**, denoted $V\cong W$, if there exists an **isomorphism** between them — a linear transformation that is both…
- **Example 3.9** — Coordinate vectors: The transformation $T:\mathbb{R}^2\to\mathcal{P}_1$ sending vectors to linear polynomials via is an isomorphism.
- **Example 3.10** — Polynomial derivatives: The differentiation operator $D:\mathcal{P}_2\to\mathcal{P}_1$ given by is surjective but not injective.
- **Definition 3.11** — Image: The **image** of $T$, denoted $\operatorname{im} T$, is the subspace of the codomain consisting of all possible outputs:
- **Definition 3.12** — Kernel: The **kernel** (or **null space**) of $T$, denoted $\operatorname{ker} T$, is the subspace of the domain consisting of all vectors that vanish under $T$:
- **Example 3.13** — Calculus operators: The differentiation operator $D:C^1([a,b])\rightarrow C([a,b])$ has kernel consisting of all constant functions on $[a,b]$ — these are precisely the functions…
- **Definition 3.14** — Rank & Nullity: The **rank** of a linear transformation $T:V\rightarrow W$ is the dimension of its image: The **nullity** of $T$ is the dimension of its kernel:
- **Example 3.15** — Matrix Rank and Nullity: For a $3\times 4$ matrix $A$ of rank 2, the transformation $T_A:\mathbb{R}^4\rightarrow\mathbb{R}^3$ has: 1.
- **Example 3.16** — Calculus operators: The differentiation operator $D:\mathcal{P}_n\rightarrow\mathcal{P}_{n-1}$ has: 1.
- **Example 3.17** — Integration: Consider the definite integration operator $\mathrm{I}:C([0,1])\rightarrow\mathbb{R}$ defined by $\mathrm{I}(f)=\int_0^1 f(x)dx$.
- **Definition 3.18** — Quotient Space: Let $V$ be a vector space and $U<V$ a subspace.
- **Example 3.19** — Kernel Quotients: Let $T:V\rightarrow W$ be a linear transformation. Two vectors that differ by an element of $\operatorname{ker} T$ are sent to the same output:
- **Example 3.20** — Geometric quotients: Consider first quotienting $\mathbb{R}^3$ by a line $L$ through the origin.
- **Example 3.21** — Integration quotients: Consider the indefinite integral operator (or *antidifferentiation*) $D^{-1}$ acting on continuous functions $C([a,b])$ on an interval.
- **Definition 3.22** — Coimage: Given a linear transformation $T:V\rightarrow W$, the **coimage** of $T$ is the quotient space The coimage packages Example 3.19 into a named space.
- **Definition 3.23** — Cokernel: Given a linear transformation $T:V\rightarrow W$, the **cokernel** of $T$ is the quotient space The cokernel measures the failure of $T$ to reach all of $W$.
- **Example 3.24** — Differential operators: For the derivative operator $D:\mathcal{P}_n\rightarrow\mathcal{P}_{n-1}$: 1. The coimage is $n$-dimensional, as only constants vanish under $D$ 2.
- **Theorem 3.25** — Fundamental Theorem of Linear Algebra: For any linear transformation $T:V\rightarrow W$ between finite-dimensional vector spaces: 1. The domain and codomain decompose as direct sums: 2.
- **Corollary 3.26** — Rank-Nullity: For a linear transformation between finite-dimensional vector spaces, the dimensions balance in complementary pairs:
- **Example 3.27** — Matrix rank: When $T$ is represented by a matrix $A$, these relationships explain why: 1.
- **Example 3.28** — Metamers: The two lamps of the opening differ by a metameric black:
- **Example 3.29** — Three Primaries: A display cannot reproduce a spectrum.
- **Example 3.30** — Ladder Network: Consider a "ladder" network with eight vertices and ten edges arranged and labeled as in the figure, right.

### Chapter 4 — Bases & Coordinates

- **Definition 4.1** — Basis: A **basis** for a vector space $V$ is a set $\mathcal{B}$ of vectors that spans $V$ yet is linearly independent.
- **Example 4.2** — Polynomial bases: The space $\mathcal{P}_2$ of quadratic polynomials admits several natural choices of basis, each providing different advantages: 1.
- **Theorem 4.3** — Basis Extension: Let $V$ be a finite-dimensional vector space and $S \subseteq V$ be a linearly independent set.
- **Example 4.4** — Matrix bases: The space $\mathbb{R}^{2\times 2}$ of $2\times 2$ matrices has the standard basis This basis makes the coordinate structure transparent but obscures other…
- **Corollary 4.5**: Any two bases of a vector space have the same number of vectors. This reveals dimension as an intrinsic property of the space, independent of choice of basis.
- **Example 4.6** — Dimension counting: The following dimensions arise naturally: 1. $\dim(\mathbb{R}^n) = n$ 2. $\dim(\mathcal{P}_n) = n+1$ 3. $\dim(\mathbb{R}^{m\times n}) = mn$ 4.
- **Example 4.7** — Polynomial coordinates: Consider the polynomial $p(x)=6+2x-3x^2$ in $\mathcal{P}_2$.
- **Example 4.8** — Electric Field Components: The electric field $\mathbf{E}$ from a point charge can be measured in different coordinate systems.
- **Definition 4.9** — Change of Basis Matrix: Let $\mathcal{B}=\{\mathbf{b}_1,\ldots,\mathbf{b}_n\}$ and $\mathcal{B}'=\{\mathbf{b}'_1,\ldots,\mathbf{b}'_n\}$ be bases for a vector space $V$.
- **Example 4.10** — Signal Processing: In audio processing, a sound signal naturally begins in the time domain — amplitudes measured at discrete time points.
- **Example 4.11** — Principal Stress: In analyzing the mechanics of a thin planar material, the **stress tensor** recording stress and strain at a point is a symmetric $2\times 2$ matrix…
- **Example 4.12** — Rotation in Different Bases: Consider the counterclockwise rotation by $\pi/2$ in $\mathbb{R}^2$.
- **Example 4.13** — Projection onto a Line: Consider the projection onto the $x$-axis along the $y$-axis in $\mathbb{R}^2$. In standard coordinates, this has matrix representation:
- **Definition 4.14** — Similarity: Two matrices $A$ and $B$ are **similar** if there exists an invertible matrix $P$ such that: We write $A \sim B$ to denote similar matrices.
- **Example 4.15** — Geometric Similarity: Consider the shear that slides each horizontal line by an amount equal to its height. In standard coordinates, this appears as:

### Chapter 5 — Inner Products & Orthogonality

- **Definition 5.1** — Inner Product: An **inner product** on a vector space $V$ is a function $\langle\cdot,\cdot\rangle:V\times V\to\mathbb{R}$ satisfying, for all…
- **Example 5.2** — Weighted Inner Products: On $\mathbb{R}^n$, we need not weight all coordinates equally.
- **Example 5.3** — Matrix Inner Products: The space $\mathbb{R}^{m\times n}$ of matrices admits several natural inner products.
- **Definition 5.4** — Norm: Given an inner product space $V$, the **norm** of a vector $\mathbf{v}\in V$ is defined by:
- **Lemma 5.5** — Cauchy-Schwarz Inequality: For any vectors $\mathbf{u},\mathbf{v}$ in an inner product space, with equality if and only if one vector is a scalar multiple of the other.
- **Example 5.6** — Matrix Alignment: Under the Frobenius inner product, matrices $A,B\in\mathbb{R}^{m\times n}$ form an angle through: This measures how aligned their entries are:
- **Lemma 5.7** — Orthogonal Decomposition: Let $\mathbf{v}_1,\ldots,\mathbf{v}_k$ be mutually orthogonal nonzero vectors. Then they are linearly independent, and for any scalars $c_1,\ldots,c_k$:
- **Example 5.8** — Fourier Series: The functions $\{\sin nx, \cos nx\}_{n=1}^\infty$ form an orthogonal set in $C[-\pi,\pi]$ under the inner product This orthogonality — discovered by Euler and…
- **Example 5.9** — Polynomial Orthogonalization: Consider the space $\mathcal{P}_4$ with inner product $\langle f,g\rangle = \int_{-1}^1 f(x)g(x)\,dx$.
- **Definition 5.10** — Adjoint: Let $V$ and $W$ be finite-dimensional inner product spaces and $T:V\rightarrow W$ a linear transformation.
- **Example 5.11** — Differentiation Adjoint: Consider the differentiation operator $D:\mathcal{P}_2\rightarrow\mathcal{P}_1$ with inner product $\langle f,g\rangle = \int_0^1 f(x)g(x)\,dx$.
- **Example 5.12** — Sum & Copy: Let $A:\mathbb{R}^n\rightarrow\mathbb{R}$ send a vector to the sum of its coordinates, $A\mathbf{x}=\sum_i x_i$; as a matrix, $A=\mathbf{1}^T$.
- **Example 5.13** — The Shift: On $\mathbb{R}^n$ the left shift has for its adjoint the right shift, as one reads off from…
- **Lemma 5.14**: For linear transformations $S$ and $T$ between finite-dimensional inner product spaces, and for any scalar $c$: 1. $(S+T)^* = S^* + T^*$ 2. $(cT)^* = cT^*$ 3.
- **Example 5.15** — An Adjoint That Is Not A Transpose: Weight the coordinates of $\mathbb{R}^n$ as in Example 5.2, and write the resulting inner product as…
- **Example 5.16** — Word Embeddings: Modern language models represent each word as a vector in $\mathbb{R}^n$, with $n$ in the hundreds, learned from patterns of co-occurrence in text.
- **Definition 5.17** — Orthogonal Transformation: A linear transformation $T:V\rightarrow V$ on an inner product space is **orthogonal** if it preserves inner products:
- **Lemma 5.18**: For a linear transformation $T$ on a finite-dimensional inner product space, the following are equivalent: 1. $T$ is orthogonal 2. $T^*T = TT^* = I$ 3.
- **Lemma 5.19**: An orthogonal matrix $Q$ satisfies: 1. Its columns (and rows) form an orthonormal basis 2. Its inverse equals its transpose: $Q^{-1} = Q^T$ 3.
- **Example 5.20** — Rigid Body Motion: The orientation of a rigid body in three-dimensional space is described by an orthogonal transformation.
- **Example 5.21** — Signal Transforms: The Discrete Fourier Transform (DFT) is the same idea over complex scalars, where inner products become conjugate-symmetric and the transformation is called…
- **Definition 5.22** — QR Decomposition: The **QR decomposition** of a matrix $A\in\mathbb{R}^{m\times n}$ with $m\geq n$ expresses it as a product where $Q\in\mathbb{R}^{m\times n}$ has orthonormal…
- **Example 5.23** — Simple QR Form: Consider the matrix Direct computation yields The orthogonal factor $Q$ captures the rotation inherent in $A$, while the triangular factor $R$ represents…
- **Lemma 5.24** — Existence and Uniqueness: Every $A\in\mathbb{R}^{m\times n}$ with $m\geq n$ admits a QR decomposition, with $Q\in\mathbb{R}^{m\times n}$ having orthonormal columns and…
- **Example 5.25** — Handwritten Digits: The MNIST database of handwritten digits provides each image as a $28\times 28$ array of grayscale values, naturally viewed as a vector in $\mathbb{R}^{784}$.
- **Example 5.26** — Color Compression: A color image consists of points in $\mathbb{R}^3$, each an RGB triple.

### Chapter 6 — Orthogonal Decomposition & Data

- **Definition 6.1** — Orthogonal Complement: Two subspaces $U,W$ of an inner product space $V$ are **orthogonal**, denoted $U\perp W$, if every vector in one is orthogonal to every vector in the other:
- **Lemma 6.2**: For $V$ a finite-dimensional inner product space and any $U<V$: 1. $(U^\perp)^\perp = U$ 2. $\dim U + \dim U^\perp = \dim V$ 3.
- **Example 6.3** — Matrix Subspaces: Consider the space $\mathbb{R}^{n\times n}$ with the Frobenius inner product $\langle A,B\rangle = \operatorname{tr}(A^TB)$ from Example 5.3.
- **Definition 6.4** — Orthogonal Projection: Let $W < V$ be a subspace of an inner product space. The **orthogonal projection** onto $W$ is the linear transformation $\Pi_{W}:V\to V$ satisfying: 1.
- **Lemma 6.5** — Best Approximation: For any $\mathbf{v}\in V$ and $\mathbf{w}\in W$: with equality if and only if $\mathbf{w} = \Pi_{W}\mathbf{v}$.
- **Example 6.6** — Signal Processing: Consider the space $V = C([-\pi,\pi])$ of continuous functions on $[-\pi,\pi]$ with the $L^2$ inner product of Example 5.8.
- **Lemma 6.7** — Projection Properties: The orthogonal projection $\Pi_{W}$ onto a subspace of a finite-dimensional inner product space $V$ satisfies: 1. Idempotence: $\Pi_{W}^2 = \Pi_{W}$ 2.
- **Example 6.8** — Data Centering: Consider a collection of vectors $\{\mathbf{x}_1,\ldots,\mathbf{x}_n\}$ in $\mathbb{R}^d$.
- **Theorem 6.9** — Fundamental Theorem of Linear Algebra (Geometric Form): Any linear transformation $T:V\rightarrow W$ between finite-dimensional inner product spaces induces orthogonal decompositions of both domain and codomain:
- **Example 6.10** — Matrix Transformations: For a matrix $A\in\mathbb{R}^{m\times n}$, these decompositions acquire immediate computational significance once we name the concrete realizations of the four…
- **Corollary 6.11** — Rank-Nullity Redux: For a linear transformation $T:V\rightarrow W$ between finite-dimensional inner product spaces: 1.
- **Definition 6.12** — Pseudoinverse: For a linear transformation $T:V\rightarrow W$ between finite-dimensional inner product spaces, the pseudoinverse (or **Moore-Penrose inverse**)…
- **Example 6.13** — A Rank-Deficient Matrix: Neither formula reaches whose rank is $1$: both $A^TA$ and $AA^T$ equal $\begin{bmatrix} 2 & 2 \\ 2 & 2\end{bmatrix}$, and neither is invertible.
- **Example 6.14** — Redundant Manipulators: Chapter 4 left a three-joint planar arm in an interesting predicament.
- **Example 6.15** — Orthogonal Projection: Consider the orthogonal projection $\Pi_{U}:V\to V$ onto a subspace $U<V$. Its fundamental spaces are:
- **Theorem 6.16** — Pseudoinverse Properties: The pseudoinverse $T^{\dagger}$ satisfies: 1. $T^{\dagger}$ maps $\operatorname{im} T$ isomorphically to $(\operatorname{ker} T)^{\perp}$ 2.
- **Theorem 6.17** — Least Squares Solution: For a full-rank matrix $A\in\mathbb{R}^{m\times n}$ with $m>n$, the system $A\mathbf{x}=\mathbf{b}$ has unique least squares solution:
- **Example 6.18** — Linear Regression: Consider fitting a line $y=mx+b$ to points $(x_1,y_1),\ldots,(x_n,y_n)$. This leads to the overdetermined system:
- **Example 6.19** — Polynomial Overfitting: Consider fitting polynomials of increasing degree $d$ to samples of $f(x)=\cos(2\pi x)$ on $[0,1]$ with small random errors.
- **Lemma 6.20** — Ridge Solution: The minimizer of the ridge regression objective satisfies the modified normal equations:

### Chapter 7 — Diagonalization & Dynamics

- **Example 7.1** — Chemical Reaction: Consider two chemical species with concentrations $x_A$ and $x_B$ that interact through a simple reaction network in matrix form:
- **Definition 7.2** — Eigenvalues and Eigenvectors: The **characteristic polynomial** $p_A(\lambda)$ of a square matrix $A$ is the polynomial A scalar $\lambda$ is called an **eigenvalue** of $A$ if it is a root…
- **Example 7.3**: For a concrete example, consider the matrix Its characteristic polynomial is Setting this equal to zero yields eigenvalues $\lambda_1=3$ and $\lambda_2=1$.
- **Lemma 7.4** — Characteristic Polynomials: For any matrix $A\in\mathbb{R}^{n\times n}$, its characteristic polynomial $p_A(\lambda)=\det(A-\lambda I)$ satisfies: 1. The polynomial has degree $n$ 2.
- **Lemma 7.5** — Eigenvalue Relations: Let $A$ be an $n\times n$ matrix and let $\lambda_1,\ldots,\lambda_n$ be the roots of its characteristic polynomial, listed with multiplicity and with complex…
- **Theorem 7.6** — Diagonalization: Let $A$ be an $n\times n$ matrix with $n$ distinct real eigenvalues $\lambda_1,\ldots,\lambda_n$ and corresponding eigenvectors…
- **Definition 7.7** — Diagonalizable: A square matrix $A\in\mathbb{R}^{n\times n}$ is {diagonalizable over $\mathbb{R}$} if there is an invertible $V\in\mathbb{R}^{n\times n}$ and a diagonal…
- **Lemma 7.8** — Eigenbasis Criterion: A matrix $A\in\mathbb{R}^{n\times n}$ is diagonalizable if and only if $\mathbb{R}^n$ possesses a basis consisting of eigenvectors of $A$.
- **Lemma 7.9** — Matrix Powers: If $A$ is diagonalizable, $A=V\Lambda V^{-1}$, then for any nonnegative integer $k$:
- **Definition 7.10** — Matrix Exponential: The **matrix exponential** of a square matrix $A$ is defined by the power series For a time-dependent system we write $e^{At}$ for the matrix exponential of…
- **Lemma 7.11** — Commuting Exponentials: Let $A$ and $B$ be square matrices of the same size with $AB=BA$. Then $e^{A+B}=e^Ae^B$.
- **Lemma 7.12** — Matrix Exponential Solution: For any square matrix $A$ and any vector $\mathbf{x}_0$, the initial value problem has the unique solution $\mathbf{x}(t) = e^{At}\mathbf{x}_0$.
- **Lemma 7.13** — Diagonalizable Matrix Exponential: If $A$ is diagonalizable, $A=V\Lambda V^{-1}$ with $\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$, then where…
- **Example 7.14** — Mass-Spring System: Consider a mass $m$ attached to a spring with constant $k$ and dashpot damping coefficient $c$.
- **Theorem 7.15** — Basis Solutions: Let the eigenvalues $\lambda_1,\ldots,\lambda_n$ of $A$ be real and distinct. Then: 1.

### Chapter 8 — Eigenvalue Complexities

- **Example 8.1** — Complex Eigenvectors: Consider the rotation matrix for angle $\pi/3$:
- **Lemma 8.2** — Complex Normal Form: Any $2\times 2$ matrix $A$ with complex conjugate eigenvalues $\alpha\pm i\beta$ is similar to $\alpha I + \beta J$.
- **Lemma 8.3** — Euler's Theorem Redux: *Proof.* Since $I$ and $J$ commute, we have: Having computed $e^{Jt}$ in Equation (8.2), we conclude: as claimed.
- **Definition 8.4** — Eigenvalue Multiplicities: The **algebraic multiplicity** of an eigenvalue is its multiplicity as a root of the characteristic polynomial.
- **Lemma 8.5** — Generalized Eigenspaces: For a real eigenvalue $\lambda$ of $A$, the sequence of subspaces stabilizes at dimension equal to the algebraic multiplicity of $\lambda$.
- **Example 8.6** — Generalized Eigenvectors: For the matrix the eigenvalue $\lambda=2$ has algebraic multiplicity $3$ but geometric multiplicity $1$.
- **Example 8.7** — Exponentiating a Simple Block: Consider the matrix The matrix $N$ is **nilpotent** — some power of it equals zero — with $N^3=0$ though $N^2\neq 0$.
- **Theorem 8.8** — Jordan Canonical Form: Every real square matrix $A$ is similar, by a real change of basis, to a block diagonal matrix $J$, called its **Jordan canonical form**:
- **Example 8.9** — Jordan Structure: The matrix is already in Jordan form. It has two Jordan blocks: a $2\times 2$ block for eigenvalue $\lambda=2$ and another for $\lambda=3$.
- **Example 8.10** — Full Jordan Decomposition: Consider the matrix Its characteristic polynomial is $-(\lambda-3)^3$: eigenvalue $\lambda=3$ with algebraic multiplicity $3$.
- **Example 8.11** — Jordan Transformation: Consider the $5\times 5$ matrix:
- **Definition 8.12** — QR Algorithm: Given matrix $A_0=A$, the **QR algorithm** generates a sequence through: 1.
- **Example 8.13** — Simple Iteration: Consider the matrix After five iterations we find: Each iterate is an orthogonal similarity of the last, so each is symmetric, as this one visibly is;
- **Theorem 8.14** — Basis Solutions for Repeated Roots: Let $\lambda$ be a root of the characteristic equation $p(\lambda)=0$ with algebraic multiplicity $k$. Then: 1.
- **Example 8.15** — Repeated Real Root: The equation has characteristic polynomial $(\lambda-1)^3=0$.
- **Example 8.16** — Critical Damping: The equation has roots $\lambda = -\gamma \pm \sqrt{\gamma^2-\omega^2}$.
- **Example 8.17** — Repeated Complex Roots: Consider the fourth-order equation whose characteristic polynomial $\lambda^4 + 2\lambda^2 + 1 = (\lambda^2+1)^2$ has root $\lambda=i$ with multiplicity 2.

### Chapter 9 — Linear Iterative Systems

- **Example 9.1** — Six-Sector Economy: Consider an economy with six primary sectors: agriculture, energy, manufacturing, transportation, services, and technology.
- **Definition 9.2** — Spectral Radius and Dominance: The **spectral radius** $\rho_A$ of a matrix $A$ is the maximum magnitude of its eigenvalues:
- **Lemma 9.3** — Dominant Convergence: Let $A$ be diagonalizable with dominant eigenvalue $\lambda_*$ and corresponding eigenvector $\mathbf{v}_*$.
- **Example 9.4** — Fibonacci redux: For the Fibonacci matrix of the previous section, the eigenvalues are $\varphi=(1+\sqrt{5})/2$ and $\psi=(1-\sqrt{5})/2$, with $|\varphi|>1>|\psi|$.
- **Example 9.5** — Economic Convergence: Returning to Example 9.1, the six-sector economy's input-output matrix $A$ has dominant eigenvalue $\lambda_*=\rho_A\approx 1.09$ with corresponding dominant…
- **Theorem 9.6** — Perron-Frobenius: Let $A$ be a square matrix with all entries strictly positive.
- **Example 9.7** — Research Citation Network: Consider six major research areas in computer science, with $b_{ij}$ the fraction of all citations *received by* papers in field $j$ that came *from* papers in…
- **Definition 9.8** — Positivity Conditions: Let $A=[a_{ij}]$ be a square matrix. It is **nonnegative** if $a_{ij}\geq 0$ for all $i,j$, and **positive** if $a_{ij}>0$ for all $i,j$;
- **Theorem 9.9** — Frobenius Extension: Let $A$ be nonnegative and irreducible.
- **Example 9.10** — Catalytic Cycle: Four substrates convert cyclically with rate matrix The characteristic polynomial of $A$ is $\lambda^4-k_1k_2k_3k_4$, so the four eigenvalues lie equally…
- **Definition 9.11** — Markov Chain: A **Markov chain** is a sequence of random variables $\{X_n\}_{n\geq 0}$ taking values in a set of states $S$, satisfying the **Markov property**:
- **Definition 9.12** — Probability Distribution: A vector $\mathbf{x}=(x_1,\ldots,x_n)^T$ is a **probability distribution** if: 1. Nonnegativity: $x_i \geq 0$ for all $i$ 2. Total probability:
- **Definition 9.13** — Stochastic Matrix: A square matrix $P=[p_{ij}]$ is **stochastic** if it satisfies: 1. Nonnegativity: $p_{ij} \geq 0$ for all $i,j$ 2. Column-stochasticity:
- **Example 9.14** — Weather Patterns: Consider a simple model of daily weather transitions among three states: Sunny (S), Cloudy (C), and Rainy (R).
- **Lemma 9.15** — Stochastic Spectral Radius: For any stochastic matrix $P$: 1. $1$ is an eigenvalue of $P$. 2. The spectral radius $\rho_P = 1$. 3. All other eigenvalues satisfy $|\lambda| \leq 1$. 4.
- **Theorem 9.16** — Markov Convergence: Let $P$ be an ergodic stochastic matrix (i.e., irreducible and aperiodic). Then: 1.
- **Example 9.17** — Weather Equilibrium: Returning to our weather model, the matrix $P$ is irreducible (all entries are positive) and aperiodic (e.g., $p_{11}>0$).
- **Example 9.18** — Random Walk on a Graph: Consider a particle moving randomly on an undirected graph with $n$ vertices, where at each step it moves with equal probability to any adjacent vertex.
- **Lemma 9.19** — Orthogonal Diagonalization of Symmetric Matrices: Let $A$ be a real symmetric matrix. Then: 1. All eigenvalues of $A$ are real 2. Eigenvectors corresponding to distinct eigenvalues are orthogonal 3.
- **Example 9.20** — Correlation & Inertia: Given $n$ measurements of $d$ variables, the correlation matrix $[R]=[R_{ij}]$ records standardized relationships between pairs:
- **Example 9.21** — Distance Matrices: Consider a collection of $n$ abstract points with only their pairwise distances known.
- **Lemma 9.22** — Extreme Values: For symmetric $A$, the **Rayleigh quotient** $q(\mathbf{x})=\mathbf{x}^TA\mathbf{x}/\mathbf{x}^T\mathbf{x}$, which on the unit sphere $\|\mathbf{x}\|=1$ is…
- **Definition 9.23** — Graph Laplacian: For an undirected graph with $n$ vertices, the **graph Laplacian** $L=[L_{ij}]$ is an $n\times n$ matrix whose entries are:
- **Example 9.24** — Five Cohorts: Five cohorts on social media — not individuals, but interacting groups with aggregate opinions — pass influence among themselves as shown, groups 1 and 4 the…
- **Theorem 9.25** — Redistribution & Consensus: Let $P$ be an $n\times n$ ergodic stochastic matrix with stationary distribution $\mathbf{\pi}$, and let $W=P^T$, so that $W$ is the averaging matrix whose…
- **Example 9.26** — Robotic Flocking: A swarm of robots aligns its velocities by local averaging, each robot pulled toward whoever is within communication range at time $t$:
- **Example 9.27** — Supply Chain Networks: Returning to the input-output model from Section 9.1, form the weighted graph on the sectors whose edge $\{i,j\}$ carries the symmetrized flow…
- **Example 9.28** — Simple Web: Consider a tiny web of four pages with link structure given by adjacency matrix — a chain of pages, each linking to its neighbors.
- **Example 9.29** — Convergence Behavior: For our four-page example, tracking successive iterates reveals geometric convergence: where $|\lambda_2(P)| < 1$.

### Chapter 10 — Singular Value Decomposition

- **Theorem 10.1** — Spectral Theorem: Let $A$ be a real symmetric matrix. Then: 1. All eigenvalues of $A$ are real 2. Eigenvectors corresponding to distinct eigenvalues are orthogonal 3.
- **Definition 10.2** — Singular Values: Let $A\in\mathbb{R}^{m\times n}$.
- **Example 10.3** — Two Frames, Not One: Consider the $2\times 2$ matrix:
- **Theorem 10.4** — Singular Value Decomposition: Every matrix $A\in\mathbb{R}^{m\times n}$ admits a decomposition where: 1.
- **Definition 10.5** — Matrix Norms: For a matrix $A\in\mathbb{R}^{m\times n}$: 1. The **spectral norm** (or **2-norm**) measures maximal stretching: 2.
- **Lemma 10.6** — Singular Values under Composition: Let $A\in\mathbb{R}^{m\times n}$ and $B\in\mathbb{R}^{n\times q}$, with the singular values of each in descending order.
- **Lemma 10.7** — Singular Values as Distances: Let $M\in\mathbb{R}^{m\times n}$ and let $1\leq k\leq p=\min\{m,n\}$.
- **Definition 10.8** — Condition Number: Let $A$ be nonsingular, so that every singular value is positive. Its **condition number** is the ratio of the largest singular value to the smallest.
- **Example 10.9** — Finite-Dimensional Function Spaces: Consider the space $\mathcal{P}_n$ of polynomials of degree at most $n$, equipped with the $L^2$ inner product on $[0,1]$:
- **Example 10.10** — Scientific Abstract Analysis: Consider analyzing a collection of physics abstracts. Grouping does not begin at the top:
- **Example 10.11** — Temperature Sensor Array: Consider a server room monitored by 100 temperature sensors sampled every minute.

### Chapter 11 — Principal Components & Low-Rank Structure

- **Definition 11.1** — Principal Components: Given a centered data matrix $\mathcal{X}$, its **principal components** are the right singular vectors $\mathbf{v}_1,\ldots,\mathbf{v}_d$ from the SVD…
- **Definition 11.2** — PC Scores: Given a principal component $\mathbf{v}_k$, the corresponding **principal component score** for observation $\mathbf{x}\in\mathbb{R}^d$ is its projection…
- **Example 11.3** — Gene Expression Data: Consider genetic expression measurements across thousands of genes in different cell types.
- **Theorem 11.4** — Principal Component Optimality: The first principal component $\mathbf{v}_1$ maximizes $\mathbf{v}^T[C]\mathbf{v}$ subject to $\|\mathbf{v}\|=1$.
- **Definition 11.5** — Rank-$k$ Approximation: For a matrix $A\in\mathbb{R}^{m\times n}$ and an integer $k\leq\operatorname{rank}(A)$, a {rank-$k$ approximation} to $A$ is any matrix…
- **Theorem 11.6** — Eckart-Young-Mirsky: Let $A\in\mathbb{R}^{m\times n}$ have singular values $\sigma_1\geq\cdots\geq\sigma_r>0$ and let $k<r$.
- **Example 11.7** — Image Compression: A grayscale photograph stored as a $1024\times 1024$ matrix $A$ of pixel intensities is, formally, a matrix of rank near $1024$;
- **Example 11.8** — Scale Effects: For the manufacturing data above, the first principal component under different preprocessing choices reveals starkly different patterns:
- **Definition 11.9** — Mahalanobis Distance: For an observation $\mathbf{x}$ from a collection with mean $\bar{\mathbf{x}}$ and positive definite covariance $[C]$, the **Mahalanobis distance** is:
- **Example 11.10** — Outlier Detection: Returning to our manufacturing data, most observations have Mahalanobis distances between 1.5 and 3 units. However, one measurement:
- **Example 11.11** — Vibration Analysis: Consider acceleration measurements from twenty-eight accelerometers on a bridge structure, yielding singular values with the remaining twenty-five all close to…
- **Example 11.12** — Chemical Process Data: A chemical reactor monitored through eight sensors yields normalized singular values decreasing more gradually:
- **Definition 11.13** — Matrix Completion Problem: Let $M\in\mathbb{R}^{m\times n}$ be an unknown matrix, and let $\Omega\subset\{1,\ldots,m\}\times\{1,\ldots,n\}$ denote a set of observed indices.
- **Definition 11.14** — Nuclear Norm: The **nuclear norm** of a matrix $A$, denoted $\|A\|_*$, equals the sum of its singular values:
- **Theorem 11.15** — Matrix Completion: Let $M\in\mathbb{R}^{m\times n}$ be a rank-$r$ matrix with singular value decomposition $M=U\Sigma V^T$, where $\sigma_r(M)>0$.
- **Definition 11.16** — Robust Principal Component Analysis: The **robust principal component analysis** problem seeks to decompose an observed matrix $M$ as: where:
- **Theorem 11.17** — Principal Component Pursuit: Let $M = L_0 + S_0$, where $L_0$ has rank $r$ and the support of $S_0$ is drawn uniformly at random among sets of its cardinality, the corrupted values…
- **Example 11.18** — Video Surveillance: A fixed camera records a scene where most variation comes from a few moving objects against a static background.

### Chapter 12 — Probability & High Dimension

- **Definition 12.1** — Probability Inner Product: Let $\rho$ be a probability density on $N$ outcomes, with each $\rho_i>0$ and $\sum_i\rho_i=1$.
- **Lemma 12.2** — Markov & Chebyshev Inequalities: Let $t>0$. For a random variable $f\geq 0$, and for arbitrary $f$, *Proof.* Let $A$ be the event $f\geq t$. Outcome-by-outcome, $t\,\mathbf{1}_A \leq f$:
- **Definition 12.3** — Probability Simplex: The **probability simplex** on $N$ outcomes is the set where $\rho\geq 0$ is meant entrywise and the inner product is the standard one.
- **Lemma 12.4** — Stochastic Matrices Preserve the Simplex: A matrix $P\in\mathbb{R}^{N\times N}$ maps $\Delta^{N-1}$ into $\Delta^{N-1}$ if and only if $P$ is column-stochastic in the sense of Definition 9.13:
- **Definition 12.5** — Softmax: The **softmax** map $\operatorname{softmax}:\mathbb{R}^N\rightarrow\Delta^{N-1}$ sends a vector of scores $\mathbf{z}$ to the density where the exponential…
- **Lemma 12.6** — Random Inner Products: For $\mathbf{u}\in\mathbb{R}^n$ a fixed unit vector and $\mathbf{v}$ a random unit vector, *Proof.* Symmetry does nearly all the work.
- **Lemma 12.7** — Union Bound: For any events $A_1,\ldots,A_m$, *Proof.* Outcome-by-outcome, $\mathbf{1}_{A_1\cup\cdots\cup A_m}\leq\mathbf{1}_{A_1}+\cdots+\mathbf{1}_{A_m}$:
- **Definition 12.8** — Random Projection: A **random projection** from $\mathbb{R}^n$ to $\mathbb{R}^k$ is the linear map $\mathbf{x}\mapsto\Phi\mathbf{x}$ given by a matrix…
- **Lemma 12.9** — Random Projections Measure Length: For a fixed vector $\mathbf{x}\in\mathbb{R}^n$ and a random projection $\Phi$ to $\mathbb{R}^k$, *Proof.* The Gaussian density is a function of length alone,…
- **Theorem 12.10** — Johnson-Lindenstrauss: Let $\mathbf{x}_1,\ldots,\mathbf{x}_m$ be any collection of points in $\mathbb{R}^n$, let $0<\epsilon<1$, and let $\Phi$ be a random projection to…
- **Theorem 12.11** — Randomized Range Finder: Let $A\in\mathbb{R}^{n\times d}$, let $k\geq 2$ be a target rank, and let $p\geq 2$ be an oversampling parameter with $k+p\leq\min(n,d)$.

### Chapter 13 — Neural Networks & AI

- **Definition 13.1** — Activation Function: An **activation function** $\varsigma:\mathbb{R}\to\mathbb{R}$ is a nonlinear function applied elementwise to vectors. Common choices include: 1.
- **Lemma 13.2** — Universal Approximation: A neural network with a single hidden layer of sufficient width, using a continuous non-polynomial activation $\varsigma$, can approximate any continuous…
- **Definition 13.3** — Feedforward Neural Network: A **feedforward neural network** is a function $f:\mathbb{R}^n\to\mathbb{R}^m$ parameterized by weight matrices $\{W_\ell\}$ and bias vectors…
- **Definition 13.4** — Error Signal: The **error signal** $[\delta_\ell]$ at layer $\ell$ is the derivative of loss with respect to that layer's pre-activation output:
- **Lemma 13.5** — Backpropagation Rule: Let $\mathcal{L}$ be a scalar loss function of network output.
- **Theorem 13.6** — Backpropagation Complexity: For a network with $\Lambda$ layers each of width at most $n$, backpropagation computes all parameter derivatives in time $O(\Lambda n^2)$ using storage…
- **Definition 13.7** — Stochastic Gradient Descent: Let $\{\Psi_t\}_{t\geq 0}$ denote a sequence of parameter vectors updated iteratively according to:
- **Lemma 13.8** — Mini-batch Properties: Let $\nu^2$ denote the variance of individual gradient estimates. The mini-batch gradient estimator satisfies: 1. Unbiasedness:
- **Example 13.9** — Binary Classification: A network classifying points of $\mathbb{R}^2$ under the logistic loss carries parameters $\mathbf{w}\in\mathbb{R}^2$ and $c\in\mathbb{R}$ and computes For…
- **Definition 13.10** — Smoothness and Strong Convexity: A differentiable function $f:\mathbb{R}^n\to\mathbb{R}$ is: 1. {$L$-smooth} if its gradient is Lipschitz continuous with parameter $L>0$: 2.
- **Theorem 13.11** — SGD Convergence: Let $\mathcal{L}$ be $\mu$-strongly convex and $L$-smooth, and set $\gamma = 2L/\mu$.
- **Definition 13.12** — Attention Mechanism: Given token embeddings assembled as the columns of $X\in\mathbb{R}^{d\times n}$, with learned **projection matrices** $W_Q$, $W_K\in\mathbb{R}^{d_k\times d}$…
- **Theorem 13.13** — Attention Properties: Let $Y=VS$ be the output of the attention mechanism (13.4). Then: 1. $S$ is column-stochastic: each column is a density, entrywise positive with unit sum; 2.
- **Definition 13.14** — Representation: The **representation** of an input $\mathbf{x}$ at depth $\ell$ is the hidden vector $\mathbf{h}_\ell\in\mathbb{R}^{n_\ell}$ produced by the first $\ell$…
- **Theorem 13.15** — Piecewise Linearity: Let $f:\mathbb{R}^{n_0}\to\mathbb{R}^{n_\Lambda}$ be a feedforward network (Definition 13.3) with ReLU activations.
- **Example 13.16** — Word Embeddings: The representation of words shows learned geometry at its most legible.
- **Example 13.17** — Learned Decompositions: Consider an autoencoder compressing data through a narrow hidden layer:

---


# Incipit

**Mathematics is the language** of modern engineering, and linear algebra its American dialect — inelegant, practical, ubiquitous.
This text aims to prepare engineering students for the mathematical aspects of artificial intelligence, data science, dynamical systems, machine learning, and other fields whose advances depend critically on linear algebraic methods.

The reader arrives here having encountered matrices and vectors in calculus courses (at least).
These tools, though already familiar as computational devices, harbor deeper structures worth careful study.
Our task is to build on this computational facility toward an understanding of the abstract frameworks that enable modern methods in contemporary engineering.

This text differs from standard linear algebra courses in its emphasis and pace.
Abstract vector spaces appear early, but always in service of concrete applications.
The singular value decomposition and eigentheory — essential to modern practice — arrive at the midpoint, allowing extended treatment of applications in dynamics and data science alike.
Practical examples appear throughout, acknowledging that theoretical understanding and useful implementation emanate symmetrically.

Systems of linear equations provide an entry point, leading to vector spaces and linear transformations.
Inner products and orthogonality build geometric intuition, and linear ODEs and iterative systems provide an impetus for eigendecompositions.
The singular value decomposition serves as both a culminating theoretical achievement and a bridge to applications: principal component analysis, low-rank approximation, and neural networks.

Though the foundations of linear algebra remain stable, their applications have expanded dramatically.
Today's engineering students require facility with both abstract theory and practical implementation.
Linear algebra is not the endpoint, but rather a first step toward deeper mathematical structures.

## Topics for Review

This text assumes a strong grounding in (single and) multivariable calculus in the context of vectors, matrices, and coordinate-based linear transformations.
Please see the *Calculus Blue Project* for an example.
Before beginning this text the reader should have been exposed to:

1. Basic set-theory and its notation


    > *e.g.,* $\in, \subset, \cup, \cap$

2. Taylor series and exponentials

3. Complex numbers and Euler's formula


    > $e^{i\theta} = \cos\theta + i\sin\theta$

4. Euclidean vectors and vector algebra

5. The dot product and angles between Euclidean vectors


    > $\mathbf{u}\cdot\mathbf{v} = |\mathbf{u}||\mathbf{v}|\cos\theta$

6. Matrices, matrix addition, and matrix multiplication


    > $AB\neq BA$
 $(AB)C=A(BC)$

7. The identity matrix, $I$, and its behavior

8. The transpose $A^T$ of a matrix $A$ and its properties


    > $(A^T)_{ij}=A_{ji}$ and $(AB)^T=B^TA^T$

9. Matrix-vector multiplication

10. Converting linear systems of equations to matrix-vector form


    > $A\mathbf{x}=\mathbf{b}$

11. Row reduction and back-substitution

12. The matrix inverse $A^{-1}$ and its properties


    > $AA^{-1}=I=A^{-1}A$
    >

    > $(AB)^{-1}=B^{-1}A^{-1}$

13. Euclidean linear transformations: rescaling, rotations, shears

14. Trace of a matrix


    > $\operatorname{tr}(A)=\sum_k a_{kk}$

15. Determinants and their properties


    > $\det(AB)=\det(A)\det(B)$
    >
    > $\det(A^T)=\det(A)$

16. Basic differentiation and integration

17. The derivative of a function $f$ as a linear transformation $[Df]$


    > For a scalar field $f$, the gradient is $\nabla f = [Df]^T$

18. The linear ODE $dx/dt = ax$ and its solutions


    > $x(t) = e^{at}x_0$

19. Basic probability: densities, expectation, and variance


    > $\mathbb{E}(X) = \sum_i x_i\,\rho_i$ (disc)
    >

    > $\mathbb{E}(X) =  \int x\,\rho(x)\,dx$ (cont)
    >

    > $\mathbb{V}(X) = \mathbb{E}((X-\mathbb{E}(X))^2)$

## Assumptions

This text, like its author, spans Mathematics & Engineering and tries to strike a balance between the two.
Given the audience and constraints associated with this text, there are a few topics or details included which do not appear in typical linear algebra texts, as well as several interesting mathematical side-paths which are left unexplored.

1. Abstract vector spaces and abstract linear transformations are important, even though coordinate-based linear algebra prevails in applications.
    Thinking without coordinates is an important skill to master.

2. Finite-dimensional vector spaces are the norm.
    When infinite-dimensional spaces are invoked, they are done so without fully detailed justification and with some caveats.

3. The Fundamental Theorem of Linear Algebra is the organizing principle of this text.
    Its usual emanation in terms of orthogonal complements is to be approached only after the primal form (using quotients) is mastered.

4. All vector spaces are over the reals — no finite fields and no complex coefficients.
    This greatly facilitates intuition at the expense of complexity when covering the Jordan Canonical Form and solutions to linear systems of ODEs.

5. Not all applications can be developed slowly via careful exposition.
    Teaching random variables, covariance matrices, stress tensors, neural networks, and other interesting engineering applications is not the direct goal of the text.
    Where an application outruns what these pages can properly develop, it is present for what it reveals about linear algebra and for nothing else.
    The engineering behind it belongs to other courses and other books.

## Acknowledgments

This text is meant for first- and second-year undergraduate students in engineering as a follow-up course to multivariable calculus.
It was created initially to support students in Penn's Artificial Intelligence degree program, but has much broader utility.
The author is grateful to Penn's engineering students.

The writing was assisted throughout by Claude, working from samples of the author's prose and under his direction.
The author is responsible for every line of the result, and claims the mathematics and the mistakes alike.
A hidden schema of puzzles based on a certain work of Wm. Blake & a bit of influence from Aquinas was co-created by the author and Claude, with influences throughout the text.
All artwork is by the author.

The first edition was begun on November 4, 2024 and published on December 28, 2024. This second edition, crafted in August 2026 with, again, the assistance of Claude, fixed many of the errors brought on by such haste.

---


---

> **Part marker.** THARMAS — body / material (coimage)


# Chapter 1. Solving Linear Systems

*"in right lined paths outmeasur'd by proportions of number weight & measure"*

**The story of linear algebra begins** with systems of equations, each line describing a constraint or boundary traced upon abstract space.
These simplest mathematical models of limitation — each equation binding variables in measured proportion — conjoin to shape the realm of possible solutions.
When several such constraints act in concert, their collaboration yields three possible fates: no solution survives their collective force; exactly one point satisfies all bounds; or infinite possibilities trace curves and planes through the space of satisfaction.
This trichotomy — of emptiness, uniqueness, and infinity — echoes through all of linear algebra, appearing in increasingly sophisticated forms as our understanding deepens.

The art lies in recognizing these patterns and discovering efficient paths to their resolution.
Each systematic operation preserves essential structure while bringing clarity to what was obscure.
The methods we develop — though conceived for practical computation — transform a system while preserving the one thing that matters: its solutions.

## 1.1 Solving Equations

**Definition 1.1 (Linear System).** A **linear system** in variables $x_1,\ldots,x_n$ consists of $m$ equations of the form

$$
\begin{array}{rcl}
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n &=& b_1 \\
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n &=& b_2 \\
&\vdots& \\
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n &=& b_m
\end{array}
$$

where the coefficients $a_{ij}$ and constants $b_i$ are real numbers.

Such systems arise naturally in contexts ranging from the distribution of currents in electrical networks to the balance of forces in structures to the flow of traffic in transportation networks.

This system is more efficiently expressed as $A\mathbf{x} = \mathbf{b}$, where:

> *Foreshadowing:* The matrix form $A\mathbf{x}=\mathbf{b}$ is Chapter 3's subject in disguise: $A$ acting on $\mathbf{x}$ is a linear transformation.

$$
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}, \quad
\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}, \quad
\mathbf{b} = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \end{pmatrix}
$$

The matrix $A$ is called the **coefficient matrix** of the system.
The vector $\mathbf{b}$ is the **constant vector**.
Together they completely specify the linear system.

**Example 1.2 (Existence and Obstruction).** Consider the system $A\mathbf{x}=\mathbf{b}$ with

$$
A = \begin{bmatrix}
    -1 & 0 & -1 & 0 \\
    1 & -1 & 0 & 0 \\
    0 & 1 & 1 & 0 \\
    0 & 0 & 0 & -1 \\
    0 & 0 & 0 & 1
    \end{bmatrix}
    \quad : \quad
    \mathbf{b} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \\ b_4 \\ b_5 \end{pmatrix} \;\text{left unspecified}
$$

The task is not to solve the system for a given right-hand side — the row reduction of Section 1.3 dispatches any particular case.
The task is: for which $\mathbf{b}$ does a solution exist at all?
A slight computation reveals that solvability imposes exactly two hidden constraints, $b_1+b_2+b_3=0$ and $b_4+b_5=0$.
Now the harder questions.
What sort of object is the set of all achievable $\mathbf{b}$?
What sort of object is the set of obstructions, and in what space does it live?
Why two constraints and not three?
And when solutions exist, they form a family of dimension one: why?

> *Think:* This matrix has a secret: it records a small network, and the two constraints are conservation laws, one per connected piece.

To answer is to characterize, not to compute.
The achievable right-hand sides form a subspace; the obstructions form a space of their own; the solution family is a translate of a third; and the counts $2$ and $1$ are shadows of a single accounting principle binding all of them together.
*Matrices give birth to multiple spaces.*

## 1.2 Special Matrices

Before engaging with the general solution of linear systems, we examine certain fundamental types of coefficient matrices — primal forms from which more complex patterns emerge.
A system seldom arrives in one of these forms.
Solving one means reducing it to a form on this list, and that reduction is elimination.

The simplest case occurs when $A$ is the **identity matrix** $I$.
The system $I\mathbf{x}=\mathbf{b}$ requires no solving: the solution is immediate, with $\mathbf{x}=\mathbf{b}$.
This seeming triviality is nevertheless valuable: the simpler the matrix, the easier it is to infer a solution.

**Definition 1.3 (Permutation).** A **permutation matrix** is a square matrix with exactly one $1$ per row and column, having all other entries equal to $0$.

> *Example:* a permutation matrix.
>
>

$$
>
> P = \begin{bmatrix}
> 0 & 0 & 0 & 1 & 0 \\
> 1 & 0 & 0 & 0 & 0 \\
> 0 & 0 & 1 & 0 & 0 \\
> 0 & 1 & 0 & 0 & 0 \\
> 0 & 0 & 0 & 0 & 1
> \end{bmatrix}
>
>
$$

Every permutation matrix $P$ is obtained by rearranging the rows (or columns) of the identity matrix.
Such matrices effect a reordering of components: the solution to $P\mathbf{x}=\mathbf{b}$ is a reordering of the entries of $\mathbf{b}$.
This explains why permutation matrices are invertible — their inverse simply undoes the permutation.
Though elementary, these matrices underlie efficient solution methods.

More interesting are **block-diagonal matrices**, having the form

$$
B = \begin{bmatrix}
B_1 & 0 & \cdots & 0 \\
0 & B_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & B_k
\end{bmatrix}
$$

where each $B_i$ is a matrix.
The system $B\mathbf{x}=\mathbf{b}$ decomposes into independent subsystems, one for each block.
This decomposition principle — that some linear systems can be solved by solving smaller independent systems — will recur throughout our development.

> *Example:* The following 4-by-4 matrix
>
>

$$
>
> \begin{bmatrix}
> 2 & 1 & 0 & 0 \\
> 3 & 7 & 0 & 0 \\
> 0 & 0 & 1 & 4 \\
> 0 & 0 & -2 & 3 \\
> \end{bmatrix}
>
>
$$

>
> decomposes into two independent 2-by-2 blocks.

**Example 1.4 (Hidden Block Structure).** Consider the linear system:

$$
\begin{bmatrix}
0 & 0 & 0 & -1 & 3 \\
0 & 0 & 2 & 1 & 0 \\
1 & 2 & 0 & 0 & 0 \\
0 & 0 & -1 & 4 & 0 \\
-1 & 3 & 0 & 0 & 0
\end{bmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5
\end{pmatrix}
=
\begin{pmatrix}
b_1 \\ b_2 \\ b_3 \\ b_4 \\ b_5
\end{pmatrix}
$$

The structure of this system is obscured, but becomes clear after permuting rows and columns to group related variables.
Specifically, after reordering rows (1,2,4) and (3,5), and variables $x_3,x_4,x_5$ and $x_1,x_2$, the system becomes:

$$
\begin{bmatrix}
2 & 1 & 0 & 0 & 0 \\
-1 & 4 & 0 & 0 & 0 \\
0 & -1 & 3 & 0 & 0 \\
0 & 0 & 0 & 1 & 2 \\
0 & 0 & 0 & -1 & 3
\end{bmatrix}
\begin{pmatrix}
x_3 \\ x_4 \\ x_5 \\ x_1 \\ x_2
\end{pmatrix}
=
\begin{pmatrix}
b_2 \\ b_4 \\ b_1 \\ b_3 \\ b_5
\end{pmatrix}
$$

This reveals two independent subsystems: a $3\times 3$ system involving $x_3,x_4,x_5$ and a $2\times 2$ system for $x_1,x_2$.
The block structure, hidden in the original formulation, allows us to solve two smaller systems rather than one large system.

An **upper-triangular matrix** $U$ has all entries below the diagonal equal to zero:

$$
U = \begin{bmatrix}
u_{11} & u_{12} & \cdots & u_{1n} \\
0 & u_{22} & \cdots & u_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & u_{nn}
\end{bmatrix}
$$

The system $U\mathbf{x}=\mathbf{b}$ yields to **back-substitution**: from the last equation, we compute $x_n$; this value substituted into the penultimate equation yields $x_{n-1}$; and so forth.
This process fails only if some diagonal entry $u_{ii}$ vanishes.

Its transpose, a **lower-triangular matrix** $L$, has all entries above the diagonal equal to zero.
The corresponding system $L\mathbf{x}=\mathbf{b}$ succumbs to **forward-substitution**, solving for variables in order from first to last.
These triangular forms will be our stepping stones toward solving general systems.

> *Foreshadowing:* The decomposition of a general matrix into a product of triangular matrices will provide both theoretical insight and practical methods for solving linear systems.

These special cases suggest a strategy: convert a general system into one of these simpler forms through systematic manipulation of equations.

## 1.3 Recalling Row Reduction

The method of solving linear systems by systematic elimination of variables has ancient roots.
The modern approach builds on this by expressing both the coefficient matrix $A$ and constant vector $\mathbf{b}$ as a single object — the **augmented matrix**, written as $[\,A\,|\,\mathbf{b}\,]$.
This augmented matrix combines the system's coefficients with its constants in one array.

The solution of linear systems proceeds through a sequence of operations, each of which transforms the augmented matrix into another representing an equivalent system (having the same solutions).

> *Caveat:* While these three operations seem simple, their order matters greatly.
> A poorly chosen sequence of operations can lead to inconvenience and/or numerical instability.

**Definition 1.5 (Elementary Row Operations).** An **elementary row operation** on a matrix is one of three types:

R1: Interchange of any two rows

R2: Multiplication of any row by a nonzero scalar

R3: Addition of a multiple of one row to another row

Each preserves the solution set of the corresponding linear system.

The first, R1, allows strategic positioning of equations.
The second, R2, enables normalization of coefficients.
The third, R3, is the atomic unit of elimination — the means by which variables are systematically removed from equations.

The purpose of these operations is to convert the augmented matrix into a suitably simple form.

> *Example:* row echelon form.
>
>

$$
>
> \begin{bmatrix}
> \bullet & * & * & * & * \\
> 0 & \bullet & * & * & * \\
> 0 & 0 & 0 & \bullet & * \\
> 0 & 0 & 0 & 0 & 0
> \end{bmatrix}
>
>
$$

**Definition 1.6 (Row Echelon Form).** A matrix is in **row echelon form** if:

1. All zero rows (if any) appear at the bottom

2. The first nonzero entry (the **pivot**) in each nonzero row appears to the right of all pivots in rows above it

3. All entries in a column below a pivot are zero

A matrix in row echelon form whose pivots all equal $1$, and with all entries above pivots also zero, is said to be in **reduced row echelon form**.

The process of achieving row echelon form exposes the structure of the linear system.
Variables corresponding to pivot columns are **bound** — determined by the other variables in the system.
The remaining variables are **free** — they may be chosen arbitrarily, with the bound variables adjusting accordingly to maintain the system's constraints.

> *Foreshadowing:* The distinction between bound and free variables previews a deeper structure we will encounter when studying vector spaces: the relationship between dimension and constraints.

Should one continue the row operations beyond row echelon form, scaling each pivot to $1$ and clearing every entry above it, the result is unique to the matrix — though many different sequences of row operations may arrive at it.
The path to reduced row echelon form may vary; the destination does not.

The dimension of the space of solutions is revealed through this reduction: it equals the number of free variables in the system.

## 1.4 Inverse & Invertibility

For a square matrix $A$, the system $A\mathbf{x}=\mathbf{b}$ takes on special significance as a model of *determined* problems — those with as many equations as unknowns.
The solvability of such systems hinges on a fundamental property:

**Definition 1.7 (Nonsingularity).** A square matrix $A$ is **nonsingular** if any of the following equivalent conditions hold:

1. There exists a matrix $A^{-1}$ such that $AA^{-1}=A^{-1}A=I$

2. The system $A\mathbf{x}=\mathbf{b}$ has a unique solution for every $\mathbf{b}$

3. The system $A\mathbf{x}=\mathbf{0}$ has only the trivial solution $\mathbf{x}=\mathbf{0}$

4. The determinant is nonzero: $\det A\neq 0$

> *Recall:*
>
>

$$
>
> \begin{bmatrix}
> a & b \\ c & d
> \end{bmatrix}^{-1}
> =
>
>
$$

>
>
>

$$
>
> \frac{1}{\det}
> \begin{bmatrix}
> d & -b \\ -c & a
> \end{bmatrix}
>
>
$$

A matrix that is not nonsingular is called **singular**.

When $A$ is nonsingular, its inverse $A^{-1}$ provides an immediate solution $\mathbf{x}=A^{-1}\mathbf{b}$ to the system $A\mathbf{x}=\mathbf{b}$.
Though the determinant offers a theoretical test for nonsingularity, practical computation requires different tools.

> *Foreshadowing:* The geometric interpretation of singular matrices as "compressing space" becomes quantitative with eigenvalues (Chapter 7) and exact with singular values (Chapter 10).

Row reduction provides a systematic approach to finding $A^{-1}$ or proving it does not exist.
Form the augmented matrix $[\,A\,|\,I\,]$ and perform row operations.
If $A$ is nonsingular, this yields $[\,I\,|\,A^{-1}\,]$ — the same operations transforming $A$ to $I$ will transform $I$ to $A^{-1}$.

A singular matrix reveals itself during row reduction through a row of zeros.
Such matrices irretrievably compress space, mapping distinct vectors to the same image.
This compression manifests in the system $A\mathbf{x}=\mathbf{b}$ as either inconsistency (no solutions) or indeterminacy (infinitely many solutions).

> *Example:* row operation matrices and their inverses:
>
> R1:
>
>
> $\begin{bmatrix} > 0&0&1&0 \\ > 0&1&0&0 \\ > 1&0&0&0 \\ > 0&0&0&1 > \end{bmatrix}^{-1} > = > \begin{bmatrix} > 0&0&1&0 \\ > 0&1&0&0 \\ > 1&0&0&0 \\ > 0&0&0&1 > \end{bmatrix}$
>
> R2:
>
>
> $\begin{bmatrix} > 1&0&0&0 \\ > 0&1&0&0 \\ > 0&0&5&0 \\ > 0&0&0&1 > \end{bmatrix}^{-1} > = > \begin{bmatrix} > 1&0&0&0 \\ > 0&1&0&0 \\ > 0&0&\frac{1}{5}&0 \\ > 0&0&0&1 > \end{bmatrix}$
>
> R3:
>
>
> $\begin{bmatrix} > 1&0&0&0 \\ > 0&1&0&0 \\ > 0&0&1&0 \\ > 2&0&0&1 > \end{bmatrix}^{-1} > = > \begin{bmatrix} > 1&0&0&0 \\ > 0&1&0&0 \\ > 0&0&1&0 \\ > -2&0&0&1 > \end{bmatrix}$

Row reduction is not the only road to an inverse: some are summed rather than solved for.

**Lemma 1.8 (Neumann Series).** Let $A$ be a square matrix whose powers decay, $A^k\to 0$ entrywise as $k\to\infty$.
Then $I-A$ is nonsingular, and

$$
(I-A)^{-1} = I + A + A^2 + \cdots
$$

> *Foreshadowing:* The hypothesis is a statement about eigenvalues.
> Chapter 7 raises a diagonalizable matrix to the $k$th power by doing the same to each of its eigenvalues, so the powers decay when every eigenvalue is smaller than $1$ in magnitude; Chapter 9 names that largest magnitude the spectral radius and puts this lemma to work.

*Proof.* Suppose $(I-A)\mathbf{x}=\mathbf{0}$.
Then $A\mathbf{x}=\mathbf{x}$, hence $A^k\mathbf{x}=\mathbf{x}$ for every $k$, and letting $k\to\infty$ leaves $\mathbf{x}=\mathbf{0}$: clause 3 of Definition 1.7, so $I-A$ is nonsingular.
The partial sums telescope,

$$
(I-A)\left(I+A+A^2+\cdots+A^k\right) = I - A^{k+1} ,
$$

giving $I+A+\cdots+A^k = (I-A)^{-1} - (I-A)^{-1}A^{k+1}$, whose trailing term vanishes with $A^{k+1}$. ∎

Each term is one more application of $A$; the inverse is their total.

## 1.5 Composition & Elimination

Row reduction is more than a sequence of operations: it is a composition of linear transformations.
Each elementary row operation can be realized as multiplication on the left by an appropriate **elementary matrix** — obtained by performing that same operation on the identity matrix.

For example, to interchange rows $i$ and $j$ of a matrix $A$, one multiplies on the left by the matrix $E$ obtained by performing R1 on $I$.
To multiply row $i$ by a nonzero constant $c$, one uses the elementary matrix $E$ formed by scaling row $i$ of $I$ by $c$: applying R2 to $I$.
To add $c$ times row $j$ to row $i$, the elementary matrix $E$ comes from performing this R3 operation on $I$.

The salient feature of these elementary matrices is their **invertibility**.
Each row operation can be undone:

- Interchanging rows is its own inverse.

- Scaling a row by $c$ has inverse scaling the same row by $1/c$.

- Adding $c$ times row $j$ to row $i$ has as inverse the same operation with $-c$ instead.

The process of **Gaussian elimination** — the systematic reduction of a matrix to row echelon form — is thus expressible as a composition of these three types of elementary matrices:

$$
E_k\cdots E_2E_1A = R
$$

where $R$ is the row echelon form and each $E_i$ is elementary.
The product $E_k\cdots E_2E_1$ represents the cumulative effect of the row operations.
When $A$ is invertible, this sequence continues until $R=I$, yielding

$$
A^{-1} = E_k\cdots E_2E_1
$$

This perspective on row reduction — as a composition of invertible linear transformations — reveals the algorithmic heart of linear algebra.

## 1.6 LU Decomposition

Our exposition of elementary matrices and Gaussian elimination suggests a deeper structure within matrix factorization.
The sequence of row operations that produces an upper triangular matrix can be reorganized to reveal a natural factorization of the original matrix.

**Definition 1.9 (LU Decomposition).** An **LU decomposition** of a square matrix $A$ expresses it as a product $A = LU$, where $L$ is lower triangular (with ones on the diagonal) and $U$ is upper triangular.

> *Caveat:* The existence of an $LU$ decomposition assumes we can perform elimination without row exchanges.
> When row interchanges are needed, the more general **PLU decomposition** incorporates a permutation matrix $P$: see the next section.

The matrix $U$ is precisely what one obtains from Gaussian elimination without row interchanges; the matrix $L$ captures the multipliers used in the elimination process.

**Example 1.10.** For a $3\times 3$ matrix, the $LU$ decomposition takes the form:

$$
A =
\begin{bmatrix}
1 & 0 & 0 \\
\ell_{21} & 1 & 0 \\
\ell_{31} & \ell_{32} & 1
\end{bmatrix}
\begin{bmatrix}
u_{11} & u_{12} & u_{13} \\
0 & u_{22} & u_{23} \\
0 & 0 & u_{33}
\end{bmatrix}
$$

where the $\ell_{ij}$ are the elimination multipliers.

When we use a multiplier $m$ to eliminate the $(i,j)$ entry using row $j$, that same multiplier appears in the $(i,j)$ position of $L$.
The upper triangular matrix $U$ records the results of these eliminations.
Thus, rather than storing a sequence of elementary matrices, we store their cumulative effect in $L$.

> *Example:* In electrical circuit analysis, one often solves $A\mathbf{x}=\mathbf{b}$ repeatedly with the same network topology ($A$) but different voltage or current sources ($\mathbf{b}$).
> LU decomposition is ideal for such scenarios.

The utility of LU decomposition lies in its efficiency for solving systems of equations.
Once computed, the factors $L$ and $U$ allow us to solve $A\mathbf{x}=\mathbf{b}$ by successive substitution:

1. First solve $L\mathbf{y}=\mathbf{b}$ by forward substitution

2. Then solve $U\mathbf{x}=\mathbf{y}$ by back substitution

The computational advantage becomes clear when solving multiple systems with the same coefficient matrix but different right-hand sides.
The factorization need be computed only once, at a cost of approximately $\frac{2}{3}n^3$ operations for an $n\times n$ matrix.
Each subsequent solution requires only $O(n^2)$ operations for the forward and back substitutions — a significant savings over repeating the full elimination process.

The $LU$ decomposition trades storage for computation — a bargain that every factorization to come will strike in its own terms.

## 1.7 Pivots & Permutations

> *Foreshadowing:* The $LU$ decomposition is but one of several matrix factorizations we shall encounter.
> Each reveals different aspects of a matrix's structure and serves different computational needs.

The process of Gaussian elimination, as described thus far, assumes we can use any nonzero entry as a pivot.
In practice, this is numerically unwise.
Consider elimination in the following system, whose coefficients have been taken from a data set:

$$
\begin{bmatrix}
0.003 & 7.149 \\
2.483 & 3.092
\end{bmatrix}
\begin{pmatrix}
x_1 \\ x_2
\end{pmatrix}
=
\begin{pmatrix}
b_1 \\ b_2
\end{pmatrix}
$$

Using 0.003 as a pivot would require dividing by a small number — multiplying any roundoff errors in other entries by 1000.
Interchanging the rows first yields a more stable elimination.

This suggests a modification to our elimination strategy: before elimination in each column, we first select an appropriate pivot by permuting rows.
Such row interchanges are encoded by permutation matrices.
When we incorporate this pivot selection strategy into our elimination process, we obtain:

**Definition 1.11 (PLU Decomposition).** A **PLU decomposition** of a matrix $A$ expresses it as a product $A=P^{-1}LU$ where:

1. $P$ is a permutation matrix

2. $L$ is lower triangular with ones on the diagonal

3. $U$ is upper triangular

Such a decomposition exists for any nonsingular matrix $A$ and encodes the steps of Gaussian elimination with partial pivoting.

In practice, we permute $A$ first, yielding $PA$; then decompose that into $PA=LU$.
Since $P$ is invertible, we can write $A = P^{-1}LU$.
The system $A\mathbf{x}=\mathbf{b}$ thus becomes

$$
P^{-1}LU\mathbf{x} = \mathbf{b}
\quad \Longrightarrow \quad
LU\mathbf{x} = P\mathbf{b}
$$

which we solve by:

1. Computing $P\mathbf{b}$ (applying the same row interchanges to $\mathbf{b}$ that were used in elimination)

2. Solving $L\mathbf{y}=P\mathbf{b}$ by forward substitution

3. Solving $U\mathbf{x}=\mathbf{y}$ by back substitution

> *Caveat:* Though we write the decomposition as $PA=LU$, in practice we store $P$ either as a permutation vector or as a sequence of row swaps, not as an explicit matrix.

> *BONUS!* This strategic permutation is an example of **preconditioning**.

A row exchange costs a bookkeeping entry in $P$ and buys numerical stability — the cheapest insurance in this chapter.

## 1.8 Practicalities of Linear Systems

Though our development thus far has emphasized the algebraic structure of linear systems — their solution spaces, elimination methods, and matrix factorizations — engineering demands more.
We must determine not just whether solutions exist but whether we can compute them reliably.
This bridge between abstract mathematics and practical computation requires understanding both the geometric meaning of our operations and their sensitivity to the numerical realities of finite-precision arithmetic.

Row reduction to a row echelon form (recall Definition 1.6) reveals not only solutions but also fundamental structure.
The following not-quite-rigorous definition will ascend to central importance in Chapter 3.

**Definition 1.12 (Matrix Rank).** The **rank** of a matrix is the number of pivots in a row-reduced echelon form.

This is a fundamental measure of the matrix's effectiveness at transforming space.
For an $m\times n$ matrix $A$, the rank satisfies

> *Example:* A $3\times 3$ matrix of rank 2 maps $\mathbb{R}^3$ onto a plane, collapsing one dimension.
> The geometric image helps explain why such a matrix cannot be nonsingular.

$$
\text{rank}(A) \leq \min\{m,n\}
$$

with equality implying $A$ has **full rank**.
When $A$ is square, full rank is equivalent to nonsingularity.

Example 1.2 still waits unsolved, but part of its answer now has a name: that $5\times 4$ matrix has rank $3$, and the counts observed there are $2 = 5-3$ constraints and a solution family of dimension $1 = 4-3$.
The rank names the numbers; it does not yet name the spaces.

**Example 1.13 (Row echelon computation).** Consider the matrix

$$
A = \begin{bmatrix}
1 & 2 & 0 & 3 & 1 & 2 & 4 \\
2 & 4 & 0 & 6 & 2 & 5 & 1 \\
3 & 6 & 0 & 9 & 3 & 7 & 5 \\
1 & 2 & 0 & 3 & 1 & 1 & 8 \\
4 & 8 & 0 & 12 & 4 & 9 & 2
\end{bmatrix}
$$

*Mirabile dictu:* the $(1,1)$ entry is a perfect pivot.
Clearing out the first column leads to a dramatic simplification; then clearing out the sixth column (leaving $-3$ and $-7$ in the last column), one final elimination in that last column, and a slight reordering yields the final row-echelon form.

$$
\begin{bmatrix}
1 & 2 & 0 & 3 & 1 & 2 & 4 \\
0 & 0 & 0 & 0 & 0 & 1 & -7 \\
0 & 0 & 0 & 0 & 0 & 1 & -7 \\
0 & 0 & 0 & 0 & 0 & -1 & 4 \\
0 & 0 & 0 & 0 & 0 & 1 & -14
\end{bmatrix}
\quad \Rightarrow \quad
\begin{bmatrix}
1 & 2 & 0 & 3 & 1 & 2 & 4 \\
0 & 0 & 0 & 0 & 0 & 1 & -7 \\
0 & 0 & 0 & 0 & 0 & 0 & -3 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

Several interesting features emerge:

1. The first row operation reveals that rows 2-5 were nearly linearly dependent, differing only in their last two entries

2. The matrix has rank 3, as evidenced by three nonzero rows in echelon form

3. The third column is all zeros, making it unnecessary to perform eliminations there

4. The dependencies among the first five columns become clear only after elimination

*[Margin figure omitted]*

A geometric perspective illuminates these algebraic concepts.
Each equation in a linear system represents an $(n-1)$-dimensional hyperplane in $\mathbb{R}^n$.
The solution set is the intersection of these hyperplanes.
A unique solution corresponds to $n$ hyperplanes mutually meeting at a single point; parallel distinct hyperplanes yield no solution; hyperplanes coinciding or intersecting in a line yield infinitely many solutions.

> *Caveat:* While this geometric view aids intuition in two or three dimensions, beware of relying too heavily on geometric thinking in higher dimensions, where our intuition often fails us.

The practical import of these concepts lies in their ability to predict the behavior of linear systems before attempting to solve them.
The rank determines whether a solution exists; nonsingularity tells us if that solution is unique.
This structural understanding guides our choice of solution methods and helps us interpret the results.

**Example 1.14.** Not all matrices are created equal in their amenability to computation.
Consider solving the system $A\mathbf{x}=\mathbf{b}$ where

$$
A = \begin{bmatrix}
    1 & 0.999 \\
    0 & 0.001
    \end{bmatrix}
$$

Though this matrix is nonsingular, small changes in $\mathbf{b}$ can produce large changes in the solution $\mathbf{x}$.
Such sensitivity to perturbation — whether from measurement error, roundoff in computation, or truncation of decimal places — fundamentally limits our ability to solve linear systems reliably.

This sensitivity has geometric meaning: $A$ maps the unit circle to an extremely eccentric ellipse, stretching space a thousand times more in one direction than another.
The **condition number** of $A$, denoted $\operatorname{cond}(A)$, measures precisely this eccentricity through the ratio of its largest to smallest stretching factors:

> *Foreshadowing:* The formal definition requires concepts from Chapter 10, but the geometric intuition — that some matrices distort space more extremely than others — serves us well even now.

$$
\operatorname{cond}(A) = \frac{\text{maximum stretching}}{\text{minimum stretching}}
$$

For the matrix above, $\operatorname{cond}(A)\approx 2000$, indicating that errors in certain directions may be amplified by a factor of 2000 when solving the system.

The practical significance is immediate: when $\operatorname{cond}(A)$ is large, we call $A$ **ill-conditioned** and treat computed solutions with appropriate skepticism.
When $\operatorname{cond}(A)$ is moderate (say less than 100), we have greater confidence in our numerical results.

The deeper relationship between conditioning and accuracy will emerge in Chapter 6 when we study least squares problems, and again in Chapter 10 where singular value decomposition reveals its geometric essence.
For now, this glimpse of numerical sensitivity serves as a first warning: in the workshop of linear algebra, not all tools are equally sound.

—

## Network Flows: From Graphs to Linear Systems

The world runs on networks.
Supply chains move goods from factories to stores; pipelines carry oil and gas between cities; routers pass packets across the internet.
Beneath the particulars sits one object: locations, routes between them, and a flow obliged to respect what each location produces, consumes, or passes along.
Such obligations are linear equations, and the matrices they generate carry the shape of the network in their entries.

A (directed) **network** (or **graph**) consists of **vertices** (or **nodes**) connected by oriented **edges**.
Think of vertices as locations and edges as pathways between them.

For a more formal approach, one designates a (finite) set $V$ of vertices.
Edges consist of ordered pairs of vertices: $E\subset V\times V$, where the ordering implies orientation.
One usually demands that the two vertices in an edge are distinct.

> *Think:* in a social network, vertices are people, edges are a social relation ("friend" or "follow") between two persons.

Consider a regional distribution network with five locations:

- a factory (node 1) producing 200 units;

- two regional warehouses (nodes 2, 3) that route inventory;

- two retail centers (nodes 4, 5), each requiring 100 units.

The shipping routes form the directed graph shown, with flow variables $x_{ij}$ counting units shipped from node $i$ to node $j$: the factory supplies the warehouses, and the warehouses supply the retail centers.

*[Margin figure omitted]*

Every node imposes one condition: flow in, minus flow out, equals what the node demands.
A retail center demands its hundred units; a warehouse, passing everything along, demands zero; the factory demands the negative of what it produces.
One convention, five nodes, five equations:

$$
\begin{array}{rcl}
-x_{12} - x_{13} &=& -200 \quad\text{(factory supply)} \\
x_{12} - x_{24} - x_{25} &=& 0 \quad\text{(warehouse 2 balance)} \\
x_{13} - x_{34} - x_{35} &=& 0 \quad\text{(warehouse 3 balance)} \\
x_{24} + x_{34} &=& 100 \quad\text{(retail 4 demand)} \\
x_{25} + x_{35} &=& 100 \quad\text{(retail 5 demand)}
\end{array}
$$

In matrix form, $A\mathbf{x}=\mathbf{b}$ with the variables ordered $(x_{12}, x_{13}, x_{24}, x_{25}, x_{34}, x_{35})^T$:

$$
A = \begin{bmatrix}
-1 & -1 & 0 & 0 & 0 & 0 \\
1 & 0 & -1 & -1 & 0 & 0 \\
0 & 1 & 0 & 0 & -1 & -1 \\
0 & 0 & 1 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 & 0 & 1
\end{bmatrix}
\quad : \quad
\mathbf{b} = \begin{pmatrix} -200 \\ 0 \\ 0 \\ 100 \\ 100 \end{pmatrix}
$$

This $A$ earns a name: it is the **incidence matrix** of the graph, with one row per node and one column per edge, each column holding a single $-1$ where its edge departs, a single $+1$ where it arrives, and zeros elsewhere.
This species has appeared before: the $5\times 4$ matrix of Example 1.2 is an incidence matrix, of a network worth reconstructing.

Gaussian elimination proceeds without a single row exchange, yielding $A = LU$ with

$$
L = \begin{bmatrix}
1 & 0 & 0 & 0 & 0 \\
-1 & 1 & 0 & 0 & 0 \\
0 & -1 & 1 & 0 & 0 \\
0 & 0 & -1 & 1 & 0 \\
0 & 0 & 0 & -1 & 1
\end{bmatrix}
\quad
U = \begin{bmatrix}
-1 & -1 & 0 & 0 & 0 & 0 \\
0 & -1 & -1 & -1 & 0 & 0 \\
0 & 0 & -1 & -1 & -1 & -1 \\
0 & 0 & 0 & -1 & 0 & -1 \\
0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

The last row of $U$ is zero.
This matrix has rank $4$, not $5$, and elimination has discovered why: every column of an incidence matrix holds one $+1$ and one $-1$, so the five equations sum to the trivial one.
Whatever enters the network must leave it.

A zero row solves nothing; instead, it interrogates $\mathbf{b}$.
Forward substitution on $L\mathbf{y}=\mathbf{b}$ accumulates running totals, $y_i = b_1 + \cdots + b_i$, and the final equation of $U\mathbf{x}=\mathbf{y}$ reads

$$
0 \,=\, y_5 \,=\, b_1 + b_2 + b_3 + b_4 + b_5 .
$$

A solution exists precisely when the net demands sum to zero — when supply meets demand exactly.
Here $-200 + 100 + 100 = 0$, and all is well.

With rank $4$ and six unknowns, solutions arrive as a family: two variables run free.
Choosing $x_{34}=s$ and $x_{35}=t$, back-substitution delivers

$$
(x_{12},\, x_{13},\, x_{24},\, x_{25},\, x_{34},\, x_{35})^T = (200-s-t,\;\; s+t,\;\; 100-s,\;\; 100-t,\;\; s,\;\; t)^T .
$$

The freedom is rerouting: raising $s$ shifts a unit of retail center 4's supply from warehouse 2 to warehouse 3, and $t$ does the same for center 5.
Every choice keeping all flows nonnegative is a feasible shipping plan; the choice $s=t=50$ splits each delivery evenly.

> *Foreshadowing:* which member of the family is best?
> Chapter 6 develops the optimization principles that select among feasible flows, minimizing cost, congestion, or distance.

A distribution network lives in flux, and a stored factorization is built for exactly that.
Suppose demand migrates: retail center 4 now requires $150$ units, center 5 only $50$.
The totals still balance, so solutions persist; only $\mathbf{b}$ has changed, and forward and back substitution through the stored $L$ and $U$ deliver the new flows in $O(n^2)$ operations, against the $O(n^3)$ of factoring anew.
For the thousands of what-if scenarios a logistics planner runs in a day, the distinction is decisive.

Now suppose the factory, ambitious, raises production to $250$ while the centers still want their hundred apiece.
The factorization accepts the new $\mathbf{b} = (-250, 0, 0, 100, 100)^T$ without complaint until the final equation, which reads $0 = -50$.
No solution exists.
This is no failure of method: fifty units have nowhere to go, and no cleverness of routing can make the network absorb what conservation forbids.
The obstruction of Example 1.2 has stepped out of the abstract and into a warehouse.

A closed warehouse is another matter entirely: deleting a node redraws the graph, rewrites $A$, and demands a fresh factorization.
Structure lives in the matrix; only circumstance lives in $\mathbf{b}$.

Elimination, then, does more than solve a network's equations — it reads the network's laws.
The dependency among the rows is a conservation law; the constraint on $\mathbf{b}$ is its enforcement; the free variables are its loopholes.
*Conservation arrives as a row of zeros.*

—

## Structural Analysis: Forces in Trusses

Buildings stand and bridges span by keeping their forces in balance.
The **truss** is the plainest machine for doing so: rigid members joined at frictionless pins, each carrying pure tension or compression along its own axis.
At every joint the forces must cancel — one equation horizontal, one vertical — so that a truss hands the engineer two linear equations per joint.
The unknowns are the member forces, tension counted positive and compression negative, together with whatever reaction forces the supports contribute.

Consider the five-member truss shown, carrying a load $F$ downward at its apex and a pull $G$ rightward at its tip.

*[Figure omitted]*

Its four joints sit at $(0,0)$, $(2,1)$, $(4,0)$, and $(6,1)$: two triangular panels, each diagonal running two units across for every one unit of rise.
A pin at the leftmost joint contributes reactions $R_x$ and $R_y$; a roller beneath the joint at $(4,0)$ contributes a vertical reaction $S$.
Eight unknowns — three reactions and five member forces — face eight equations, two per joint.

> *Nota bene:* the entries $0.894$ and $0.447$ below are $2/\sqrt{5}$ and $1/\sqrt{5}$: the cosines that a 2:1 diagonal makes with the horizontal and the vertical.

Taking the joints left to right, horizontal equation before vertical, with unknowns ordered as reactions first, equilibrium reads $A\mathbf{x}=\mathbf{b}$:

$$
\begin{bmatrix}
1 & 0 & 0 & 1 & 0.894 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0.447 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & -0.894 & 0.894 & 0 & 1 \\
0 & 0 & 0 & 0 & -0.447 & -0.447 & 0 & 0 \\
0 & 0 & 0 & -1 & 0 & -0.894 & 0.894 & 0 \\
0 & 0 & 1 & 0 & 0 & 0.447 & 0.447 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & -0.894 & -1 \\
0 & 0 & 0 & 0 & 0 & 0 & -0.447 & 0
\end{bmatrix}
\begin{pmatrix}
R_x \\ R_y \\ S \\ x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5
\end{pmatrix}
=
\begin{pmatrix}
0 \\ 0 \\ 0 \\ F \\ 0 \\ 0 \\ -G \\ 0
\end{pmatrix}
$$

The right-hand side records what the members and reactions must cancel: the downward $F$ at the apex in the fourth row, the rightward $G$ at the tip in the seventh.

> *Fact:* sum the four horizontal equations and every member force cancels in pairs, leaving $R_x = -G$; the vertical sum leaves $R_y + S = F$.
> Global balance is the shadow of joint balance.

Before any elimination, the final row speaks: $-0.447\, x_4 = 0$.
With no vertical load applied at the tip, the rightmost diagonal carries nothing at all — what engineers call a **zero-force member**, detected here not by structural intuition but by a row of a matrix.
Elimination dispatches the rest (with row exchanges, as Section 1.7 counsels: the $S$ column keeps its sole entry far below the diagonal), and the solution emerges for arbitrary loads:

$$
\begin{array}{c}
R_x = -G \qquad\quad R_y = \tfrac{F}{2} - \tfrac{G}{4} \qquad\quad S = \tfrac{F}{2} + \tfrac{G}{4} \\
x_1 = F + \tfrac{G}{2} \qquad x_2 = -\tfrac{\sqrt{5}}{4}\left(2F - G\right) \qquad x_3 = -\tfrac{\sqrt{5}}{4}\left(2F + G\right) \qquad x_4 = 0 \qquad x_5 = G
\end{array}
$$

The solution reads like the structure it describes.
The bottom chord stretches in tension; the two diagonals flanking the apex squeeze in compression whenever $F$ dominates; the pull $G$ rides the top chord to the apex and is answered horizontally by the pin alone, $R_x = -G$.
The supports split the vertical load unevenly, $R_y + S = F$, the roller taking the larger share.

That every loading meets exactly one response is the signature of a nonsingular matrix, and it has a name in engineering: such a truss is **statically determinate**.
The network of the preceding pages offered freedom and obstruction; the truss offers neither.
One load in, one force state out.
Since gusting wind and drifting snow change only $\mathbf{b}$, a stored factorization answers each new loading in $O(n^2)$ operations against the $O(n^3)$ of factoring afresh — and a roof endures many storms between changes to its geometry.

Geometry, meanwhile, lives in $A$ itself, and geometry is where the danger hides.
Nearly parallel members write nearly dependent columns.
For the truss as drawn, $\operatorname{cond}(A) \approx 8$: comfortably reliable.
Flatten the truss to one-tenth of its height and the diagonals sink toward the chord: the condition number climbs near $70$, while the load $F$ now drives forces of nearly $10F$ through the flattened diagonals.
At height zero the columns fall into dependence and the matrix goes singular.
That singularity is not a numerical misfortune; it is steel giving way.
An assemblage whose equilibrium matrix loses rank can move without stretching a single member — engineers call it a **mechanism** — and there are loads it cannot answer at all.
Rank deficiency is collapse, written in advance.

> *Example:* for this truss the diagonal forces grow roughly as $1/h$ in the panel height $h$.
> Long before the mechanism at $h=0$, the ill-conditioned matrix has begun to amplify loads and errors alike.

The vocabulary of this chapter was assembled in the quiet of symbol-pushing; a truss puts it under load.
Solvability is standing; conditioning is safety margin.
*What holds the roof up is full rank.*

—

## Exercises: Chapter 1

1. Solve the following systems of linear equations using Gaussian elimination.


$$
\begin{aligned}
        2x + y - z &= 5 \\
        4x - y + 2z &= 0 \\
        -2x + 5y - z &= 9
    \end{aligned}
    \quad : \quad
    \begin{aligned}
        x + 2y + z &= 4 \\
        2x + y - z &= 5 \\
        3x + 3y {{}+ 0z} &= 9
    \end{aligned}
$$

    One of these has a unique solution; the other does not.
    What happens during elimination that tells you which is which, and what does the last row then demand of the right-hand side?

2. Verify whether each of the matrices


$$
A = \begin{bmatrix}
        -1 & 4 & 2\\
         0 & 3 & 0\\
         0 & 2 & -1
    \end{bmatrix}
    \quad : \quad
    B = \begin{bmatrix}
        1 & 3 & 0 & 0 \\
        -1 & -4 & 0 & 0\\
        0 & 0 & 2 & -3\\
        0 & 0 & 1 & -2
    \end{bmatrix}
$$

    is invertible by computing its determinant. If it is invertible, find its inverse.
    Both matrices have block structure.
    Identify it, and explain how it lets you compute each determinant and each inverse from $2\times 2$ blocks alone.

3. Row reduce the matrix


$$
A = \begin{bmatrix}
        1 & 0 & 2 & 0 & 3 \\
        2 & 1 & 3 & 0 & 7 \\
        -1 & 1 & -3 & 1 & 0 \\
        3 & 1 & 5 & 0 & 10
    \end{bmatrix}
$$

    to reduced row echelon form.
    Identify the pivot columns and the free columns, and read off $\operatorname{rank}(A)$.
    A row of zeros appeared: which combination of the original rows produced it?

4. Decompose the following matrix into $LU$ form (without pivoting):


$$
A = \begin{bmatrix}
        2 & 3 & 1 \\
        4 & 7 & -1 \\
        -2 & -1 & 6
    \end{bmatrix}
$$

    Verify your result by reconstructing $A$ from $L$ and $U$.

5. Consider solving $A\mathbf{x}=\mathbf{b}$ where


$$
A = \begin{bmatrix}
        0.0001 & 1 \\
        1 & 1
    \end{bmatrix}
    \quad : \quad
    \mathbf{b} = \begin{pmatrix}
        1 \\ 2
    \end{pmatrix}
$$

    Solve the system exactly.
    Then perform the elimination twice more by hand, rounding every intermediate quantity to three significant digits: once without pivoting, and once after exchanging the two rows.
    Compare both answers against the exact one, and note the size of the multiplier in each case.
    The condition number of this $A$ is under $3$, so the system itself is not ill-conditioned.
    What, then, went wrong, and what general principle about pivoting does this illustrate?

6. Consider an electrical circuit with three nodes connected by resistors.
The conductance matrix is


$$
G = \begin{bmatrix}
        3 & -1 & -2 \\
        -1 & 4 & -3 \\
        -2 & -3 & 5
    \end{bmatrix}
$$



    > *Note:* In electrical networks $G$ is symmetric, and its row sums vanish because only voltage *differences* drive current: adding a constant to every node voltage changes nothing.

    Attempt to find node voltages $\mathbf{v}$ producing currents $\mathbf{i}=(1,0,-1)^T$ by solving $G\mathbf{v}=\mathbf{i}$; you will find that $G$ is singular.
    Show that the system is solvable nevertheless, identify what the current vector must satisfy for this to happen, and describe the full family of solutions.

7. A chemical reactor has three species $A$, $B$, and $C$ that interconvert according to first-order kinetics.
The rate matrix is


$$
K = \begin{bmatrix}
        -2 & 1 & 1 \\
        1 & -2 & 1 \\
        1 & 1 & -2
    \end{bmatrix}
$$

    If initial concentrations are $\mathbf{c}_0=(1,0,0)^T$, find steady-state concentrations by solving $K\mathbf{c}=\mathbf{0}$ subject to mass conservation $\sum_i c_i = 1$.
    Then explain, without computing, why the symmetry of $K$ forces the answer you obtained, and why any other $\mathbf{c}_0$ of the same total mass yields the same steady state.


    > *Note:* Rate matrices have zero *column* sums, which is what holds $\sum_i c_i$ constant in time; here $K$ is symmetric, so the rows sum to zero as well.

8. Let $A$ and $B$ be $n \times n$ matrices and suppose $AB = I$.
    Prove that $A$ and $B$ are invertible and that $B = A^{-1}$.

9. Prove that for any $n$-by-$n$ permutation matrix $P$ there is a positive integer $k$ with $P^k=I$, and that $k=n!$ always works.
    The smallest such $k$ is the **order** of $P$.
    Show by example that the order need not equal $n$: exhibit a $3$-by-$3$ permutation matrix of order $2$, and a $5$-by-$5$ permutation matrix of order $6$.
    What feature of $P$ determines its order?

10. > Such a matrix is called **nilpotent**, as it vanishes (becomes nil) after sufficiently many powers.

    Let $N$ denote a $k$-by-$k$ matrix that is all zeros except for $+1$ on the superdiagonal: that is, $N_{i,j}=1$ for $j=i+1$ and $0$ elsewhere.
    Demonstrate that $N^p$ is nonzero for $p<k$ and zero for $p\geq k$.

11. Consider the matrix


$$
A = \begin{bmatrix}
    1 & 0 \\
    0 & 1-\alpha
    \end{bmatrix}
$$

    where $\alpha$ is a parameter.
    Using $\operatorname{cond}$ as the ratio of maximum to minimum stretching, for what values of $\alpha$ is $A$ well-conditioned ($\operatorname{cond}(A)<10$)?
    For what values is it ill-conditioned ($\operatorname{cond}(A)>100$)?
    What happens at $\alpha=1$, and why does it fall outside both answers?

12. Let


$$
A = \begin{bmatrix}
    \cos\theta & -\sin\theta \\
    \sin\theta & \cos\theta
    \end{bmatrix}
$$

    be a rotation matrix.
    What is its condition number?
    Explain geometrically why this result makes sense.

13. In a structural analysis problem, the stiffness matrix relating forces $\mathbf{f}$ to displacements $\mathbf{u}$ has block form


$$
K = \begin{bmatrix}
        K_{11} & K_{12} \\
        K_{21} & K_{22}
    \end{bmatrix}
$$

    Assume $K$ and $K_{11}$ are both invertible.
    Show that $\mathbf{u}_2$ solves $S\mathbf{u}_2 = \mathbf{f}_2 - K_{21}K_{11}^{-1}\mathbf{f}_1$, where $S=K_{22}-K_{21}K_{11}^{-1}K_{12}$ is the **Schur complement** of $K_{11}$, and that $\mathbf{u}_1$ then follows from $K_{11}\mathbf{u}_1 = \mathbf{f}_1 - K_{12}\mathbf{u}_2$.
    Verify that $\det K = \det K_{11}\cdot\det S$, and deduce that $S$ is automatically invertible.
    This is elimination performed a block at a time: the operation count is unchanged, but the work is reorganized.
    When does that reorganization pay, and what must be true of $K_{11}$ and of $S$ for the process to be numerically trustworthy?

14. The **growth factor** in Gaussian elimination measures how much entries can grow during the process.
For a matrix $A$, it is defined as


$$
\rho(A) = \frac{\max_{i,j,k} |a_{ij}^{(k)}|}{\max_{i,j} |a_{ij}|}
$$

    where $a_{ij}^{(k)}$ denotes the $(i,j)$ entry after $k$ steps of elimination.
For the matrix


$$
A = \begin{bmatrix}
        \epsilon & 1 & 0 \\
        1 & 1 & 1 \\
        0 & 1 & 1
    \end{bmatrix}
$$

    show that the growth factor without pivoting is $(1-\epsilon)/\epsilon$, which is approximately $1/\epsilon$ for small $\epsilon>0$.
    Find a permutation $P$ for which $PA$ has growth factor approximately 1.

15. A real matrix $A$ is called **totally positive** if every minor — the determinant of any square submatrix — is positive.
Show that if $A$ is totally positive, then its LU decomposition exists without need for pivoting.
(Hint: show that the $k$-th pivot is $\Delta_k/\Delta_{k-1}$, the ratio of the leading principal minors of orders $k$ and $k-1$.)
The $5\times 5$ Hilbert matrix $h_{ij}=1/(i+j-1)$ is totally positive; its pivots are $1$, $\frac{1}{12}$, $\frac{1}{180}$, $\frac{1}{2800}$, $\frac{1}{44100}$, and its condition number is roughly $5\times 10^5$.
Distinguish carefully between "elimination introduces no new error" and "the answer is accurate."

16. Consider $n$ masses in a line, connected to one another and to two walls by springs with constants $k_1,\ldots,k_{n+1}$, with an external force $f_i$ applied to mass $i$:


$$
```latex
\begin{tikzcd}
    \text{wall} \arrow[r, "k_1", no head] & m_1 \arrow[r, "k_2", no head] & m_2 \arrow[r, "k_3", no head] & \cdots \arrow[r, "k_n", no head] & m_n \arrow[r, "k_{n+1}", no head] & \text{wall}
\end{tikzcd}
```
$$

    Let $x_i$ denote the displacement of mass $i$ from its rest position.
    Show that the equilibrium displacements satisfy $A\mathbf{x}=\mathbf{f}$, where $A$ is symmetric and tridiagonal with $a_{ii}=k_i+k_{i+1}$ and $a_{i,i+1}=a_{i+1,i}=-k_{i+1}$.
    Work the case $n=2$ explicitly and verify that $\det A = k_1k_2+k_1k_3+k_2k_3$.
    What physical principle explains the symmetry?
    Why does tridiagonality make elimination cost $O(n)$ rather than $O(n^3)$?

17. Recall from the Emanation of this chapter that the **incidence matrix** $A$ of a directed graph has entries $a_{ij}=1$ if edge $j$ enters node $i$, $a_{ij}=-1$ if edge $j$ leaves node $i$, and $a_{ij}=0$ otherwise.
Prove that for any connected graph with $n$ nodes, $\operatorname{rank}(A)=n-1$.
(Hint: one direction sums the rows; the other builds pivots along a spanning tree.)
Then show that a graph with $c$ connected components has $\operatorname{rank}(A)=n-c$, and that solvability of $A\mathbf{x}=\mathbf{b}$ imposes exactly $c$ constraints on $\mathbf{b}$, one per component.
Apply all of this to the $5\times 4$ matrix of Example 1.2: identify its graph, count its components, and recover the two constraints $b_1+b_2+b_3=0$ and $b_4+b_5=0$ that were promised there.

18. Four sensors report on three underlying quantities $x_1,x_2,x_3$ through the system $A\mathbf{x}=\mathbf{b}$, where


$$
A = \begin{bmatrix}
        1 & 0 & 1 \\
        0 & 1 & 2 \\
        1 & 1 & 3 \\
        2 & 1 & 4
    \end{bmatrix}
$$

    Show by elimination that not every reading $\mathbf{b}$ is achievable, and find the two conditions on $b_1,b_2,b_3,b_4$ that an achievable reading must satisfy.
    For $\mathbf{b}=(1,1,2,3)^T$, show that the solution is not unique, and describe the whole family.
    What have the sensors failed to measure?


    > *Note:* Example 1.2 exhibited the same two phenomena in a network, where the constraints were conservation laws. Nothing here is about networks. Naming what these two sets of conditions have in common is the work of Chapters 2 and 3.

19. Consider solving a system of equations $A\mathbf{x}=\mathbf{b}$ where $A$ is **strictly diagonally dominant**: $|a_{ii}| > \sum_{j\neq i} |a_{ij}|$ for all $i$.
Prove that $A$ is nonsingular and that no row exchanges are needed in Gaussian elimination.
Does this mean that pivoting is never worth doing for such a matrix?

20. A page-ranking algorithm scores $n$ web pages from a link matrix $L$ whose columns, once normalized, sum to $1$.
    The scores solve


$$
\mathbf{x} = \alpha L\mathbf{x} + (1-\alpha)\mathbf{1}/n
$$

    with $\alpha=0.85$ and $\mathbf{1}$ the vector of all ones.
    Show that this system always has a unique solution, whatever the link structure.
    (Hint: rewrite it as $(I-\alpha L)\mathbf{x} = (1-\alpha)\mathbf{1}/n$ and apply the previous exercise to the transpose.)
    Show further that the entries of $\mathbf{x}$ sum to $1$, so that the scores form a distribution.
    Why is uniqueness important for web search, and what would go wrong at $\alpha=1$?

---


# Chapter 2. Abstract Vector Spaces

*"in fear & pale dismay he saw the indefinite space beneath"*

**The leap from concrete to abstract** marks the first great challenge in this text.
Having worked extensively with vectors as ordered lists of numbers — whether forces, velocities, or data — we now step back and ask a deeper question: what *is* a vector?
What essential features make something vector-like?

This abstraction earns its keep.
The vectors that arise in modern engineering often transcend simple coordinate lists.
A vector might represent a time-varying signal, a high-dimensional dataset, an image, a polynomial, or a probability distribution.
The operations we perform on these vectors — addition, scaling, dot products — echo those familiar from Euclidean geometry, yet are abstracted away from geometry into pure form.
Such objects are **vectors** in a more general sense — elements of a **vector space**.

*[Margin figure omitted]*

> *Hmmmm...* A vector is an element of a vector space, a space comprised of vectors. *There must be more than this...*

## 2.1 Vector Space Axioms

**Definition 2.1 (Vector Space).** A **vector space** consists of two ingredients: a collection $V$ of objects (called **vectors**) and a field of **scalars** (for our purposes, always the real numbers $\mathbb{R}$).
These are bound together by two fundamental operations:

1. Vector addition: a rule for combining any two vectors $\mathbf{u},\mathbf{v} \in V$ to obtain a new vector $\mathbf{u}+\mathbf{v} \in V$

2. Scalar multiplication: a rule for scaling any vector $\mathbf{v} \in V$ by a real number $c \in \mathbb{R}$ to obtain a new vector $c\mathbf{v} \in V$

These operations must satisfy certain rules — the **vector space axioms**.
For all vectors $\mathbf{u},\mathbf{v},\mathbf{w} \in V$ and all scalars $a,b \in \mathbb{R}$:

> Not all collections of objects with addition and scaling qualify as vector spaces.
> The axioms are essential.

*Vector Addition Axioms:*

1. Commutativity: $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$

2. Associativity: $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$

3. Zero vector: There exists a vector $\mathbf{0} \in V$ such that $\mathbf{v} + \mathbf{0} = \mathbf{v}$ for all $\mathbf{v} \in V$

4. Additive inverses: For each $\mathbf{v} \in V$, there exists a vector $-\mathbf{v} \in V$ such that $\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$

*Scalar Multiplication Axioms:*

1. Distributivity over vector addition: $a(\mathbf{u} + \mathbf{v}) = a\mathbf{u} + a\mathbf{v}$

2. Distributivity over scalar addition: $(a+b)\mathbf{v} = a\mathbf{v} + b\mathbf{v}$

3. Associativity with scalars: $a(b\mathbf{v}) = (ab)\mathbf{v}$

4. Unity: $1\mathbf{v} = \mathbf{v}$

These axioms may seem pedantic — they certainly hold for the familiar vectors in $\mathbb{R}^n$.
Their importance emerges when considering more exotic spaces whose objects do not *look* like vectors, such as functions, polynomials, series, and the solutions of differential equations, all of which follow in the next section.

The power of these axioms lies not in their individual statements but in their collective implication: anything satisfying these rules inherits the fundamental properties of vectors.
This means that techniques developed for one vector space often translate seamlessly to others.
A method for solving systems of linear equations in $\mathbb{R}^n$ might, with minimal modification, solve systems of linear differential equations or find optimal coefficients in a signal processing filter.

> Vector spaces are not just collections of vectors — they are collections of vectors that are rightly structured under addition and scaling.

The axioms also tell us what *is not* a vector space.
The positive real numbers under ordinary addition and scalar multiplication fail: there is no zero vector, and no candidate for $-\mathbf{v}$ (which axioms survive?).
The integers under ordinary addition and multiplication fail because scalar multiplication does not always yield an integer.
Such counterexamples help sharpen our understanding of what makes a vector space work.

Finally, the axiomatic approach allows us to prove results that hold for *all* vector spaces, saving the trouble of verifying things one example at a time.
For example, the following certainly *seems* obvious in Euclidean space, but it is less clear that it holds in all possible worlds.

**Lemma 2.2.** In a vector space $V$, the zero vector is unique.

*Proof.* Assume that $z$ and $z'$ are vectors in $V$ which satisfy the zero-property. Then:

$$
z = z+z' = z' ,
$$

    each equality following from the fact that both $z$ and $z'$ do nothing when added to any vector.
    Thus, they are the same vector. ∎

## 2.2 A Gallery of Vector Spaces

An abstract definition takes on life through examples.
Each of the following illustrates how the vector space axioms manifest in different contexts, from the familiar to the exotic.
Though we shall not verify the axioms explicitly for each (a tedious if straightforward exercise), we shall identify the key components: the vectors themselves, the operations of addition and scaling, and the zero vector.

**Example 2.3 (Euclidean space).**

> Though we live in a seemingly three-dimensional world, the configuration spaces of mechanical systems routinely have higher dimension.
> A robotic arm with multiple rotation joints evolves in a state space of dimension greater than three.

The space $\mathbb{R}^n$ of ordered $n$-tuples of real numbers is our prototype.
Here, vectors are ordered lists of real numbers, acted upon by the familiar operations of componentwise addition and scalar multiplication.
The zero vector is the tuple of all zeros.
This is the space in which classical physics and engineering operate, where $n=2$ or $3$ correspond to physical space.

**Example 2.4 (Matrices).**

> The space of $2\times 2$ matrices is four-dimensional, though this is not immediately obvious from its appearance.
> This theme — that dimension can hide in plain sight — will recur.

The collection $\mathbb{R}^{m\times n}$ of all $m$-by-$n$ matrices forms a vector space under entry-by-entry addition and scalar multiplication.
The zero matrix $Z$ is the "zero" of $\mathbb{R}^{m\times n}$.
Matrix spaces are ubiquitous in engineering, from the transformation matrices of computer graphics to the weight matrices of neural networks.
The operations here echo those of $\mathbb{R}^n$, though the objects themselves are more structured.

**Example 2.5 (Polynomials).** For each nonnegative integer $n$, we have the space $\mathcal{P}_n$ of polynomials of degree at most $n$.
A typical element has the form $p(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0$.
Addition of polynomials and multiplication by scalars operate on the coefficients in the natural way.
The zero polynomial, having all coefficients equal to zero, serves as the zero vector.
These spaces serve as approximations to more complex functions and appear throughout signal processing and control theory.

**Example 2.6 (Function spaces).**

> *Foreshadowing:* this is our first example of an infinite-dimensional vector space.
> The jump from finite to infinite dimensions harbors surprises that will shape our understanding of convergence and approximation.

Consider the space $C([a,b])$ of continuous real-valued functions on an interval $[a,b]$, with addition and scalar multiplication defined pointwise.
The zero function $z(x)=0$ serves as zero vector, since $f+z=f$ for all $f$.
This space contains all the polynomials $\mathcal{P}_n$ (with restricted domain) and serves as a model for signal spaces in engineering.
One uses $C(D)$ to denote the vector space of scalar fields $f:D\to\mathbb{R}$ on a domain $D$.
For functions that have some differentiability (both helpful and familiar from calculus), the following notations for scalar fields are standard:

- $C(D)$ : continuous

- $C^1(D)$ : continuously differentiable

- $C^\infty(D)$ : infinitely differentiable or **smooth**

**Example 2.7 (Linear ODEs).**

> Similar spaces arise from linear recurrence relations and difference equations.

The solutions to a linear homogeneous differential equation form a vector space.
The vectors here are functions $x(t)$ satisfying the equation $p(D)x=0$ for $p(D)$ a polynomial of the differential operator $D$.
The operations of addition and scalar multiplication act pointwise on these solutions $x(t)$, and the constant function $x=0$ is the zero vector.

**Example 2.8 (Sequences & Series).** Consider the set of formal power series in a variable $x$, as familiar from single-variable calculus.
Ignoring convergence, we may regard such power series as vectors.
Given two such series, we can add them termwise (by powers); rescaling happens at the level of coefficients.
The zero series ($c_k=0$ for all $k$) is the zero vector.

> Recall that power series are of the form
>
>

$$
>
> f = \sum_{k=0}^\infty c_k x^k.
>
>
$$

>
> Would the *convergent* power series form a vector space?
> Does absolute versus conditional convergence matter?

There is likewise a vector space structure on the set of sequences.
Consider $a=(a_k)$ for $k\in\mathbb{N}$.
One can add such sequences termwise, and rescaling the sequence means rescaling each term.

> *Foreshadowing:* the notion of sameness or equivalence that is natural in vector spaces (and the rest of mathematics) is called **isomorphism**.
> The vector spaces of sequences and series are **isomorphic**.

The zero-sequence is the zero-vector.
This vector space "feels" like the same vector space as that of power series, though they look different.

As we proceed to subspaces, independence, and bases, these examples will serve as touchstones.

## 2.3 Subspaces

**Definition 2.9 (Subspace).** A **subspace** of a vector space $V$ is a subset $W\subseteq V$ that is itself a vector space under the operations inherited from $V$.
We use the notation $W<V$ for a subspace.

> Closure is the whole test: addition and scaling never lead out of a subspace.

The test for whether a subset $W\subseteq V$ is a subspace reduces to checking three simple properties:

1. The zero vector is in $W$

2. $W$ is closed under addition: if $\mathbf{u},\mathbf{v}\in W$ then $\mathbf{u}+\mathbf{v}\in W$

3. $W$ is closed under scalar multiplication: if $\mathbf{v}\in W$ and $c\in\mathbb{R}$ then $c\mathbf{v}\in W$

> *Foreshadowing:* These three properties are not independent.
> The first is redundant given the third, as $0\mathbf{v}=\mathbf{0}$ for any vector $\mathbf{v}$.
> This hint of redundancy in our description of subspaces previews deeper structural results to come.

**Example 2.10 (Coordinate subspaces).** In $\mathbb{R}^n$, the coordinate planes (and their higher-dimensional analogues) provide natural examples of subspaces.
For instance, in $\mathbb{R}^3$, the $xy$-plane is the subspace $\{(x,y,0): x,y\in\mathbb{R}\}$.
More generally, any plane or line through the origin forms a subspace.
The requirement that subspaces contain $\mathbf{0}$ forces them to pass through the origin — a shifted plane, no matter how close to the origin, is not a subspace.

**Example 2.11 (Null space).** The solutions to a linear homogeneous system $A\mathbf{x}=\mathbf{0}$ form a subspace called the **null space** of $A$.
This is not merely a convenient fact but a consequence of linearity: if $\mathbf{x}_1$ and $\mathbf{x}_2$ satisfy the equation, then

> *Foreshadowing:* we will use the more general term of **kernel** in place of null space when we introduce linear transformations in Chapter 3.
> The one-parameter solution family of Example 1.2 was a translate of just such a null space — the first of its four hidden spaces to acquire a name.

$$
A(c_1\mathbf{x}_1 + c_2\mathbf{x}_2) = c_1A\mathbf{x}_1 + c_2A\mathbf{x}_2 = \mathbf{0}
$$

for any scalars $c_1,c_2$.
This subspace captures the essential structure of the system's solutions.
Note that for $\mathbf{b}\neq\mathbf{0}$, the solutions to $A\mathbf{x}=\mathbf{b}$ do *not* form a subspace.

**Example 2.12 (Column space).**

> *Foreshadowing:* taking all possible combinations of a set of vectors will be known to us soon as a **span**.
> The achievable right-hand sides of Example 1.2 form exactly such a column space; with the row space named alongside it, that problem is down to one nameless space, and it is the one that carried the obstructions.

Given a matrix $A$, the set of all possible linear combinations of its columns forms a subspace $\operatorname{col}(A)$ of $\mathbb{R}^m$ (where $m$ is the number of rows).
This **column space** represents all possible outputs of the linear transformation $A\mathbf{x}=\mathbf{b}$.
There is likewise a **row space**, $\operatorname{row}(A)$  — combinations of the rows — that forms a subspace of $\mathbb{R}^n$ (where $n$ is the number of columns).

The operation of intersection preserves the subspace property: if $W_1$ and $W_2$ are subspaces of $V$, then $W_1\cap W_2$ is also a subspace.
This allows us to build new subspaces by finding the common elements of known ones.
The same is true for arbitrary intersections of subspaces — a fact that becomes important when studying systems of linear constraints.

The sum of two subspaces $W_1$ and $W_2$, defined as

> Think of a direct sum as combining subspaces that point in "independent directions" — like combining the completely distinct real and imaginary axes to build the complex plane $\mathbb{C}$.

$$
W_1 + W_2 = \{\mathbf{w}_1 + \mathbf{w}_2: \mathbf{w}_1\in W_1,\ \mathbf{w}_2\in W_2\}
$$

is always a subspace.
When the subspaces have only the zero vector in common, that is, when $W_1\cap W_2=\{\mathbf{0}\}$, we call this a **direct sum**, denoted $W_1\oplus W_2$.
The direct sum has the key property that every vector in $W_1\oplus W_2$ has a unique representation as a sum $\mathbf{w}_1+\mathbf{w}_2$ with $\mathbf{w}_1\in W_1$ and $\mathbf{w}_2\in W_2$.
For the ordinary sum $W_1+W_2$, such representations need not be unique when the subspaces overlap.

## 2.4 Span & Linear Independence

The simplest subspaces arise from the most elementary vector operation: scaling.
A single nonzero vector $\mathbf{v}$ in a vector space $V$ generates a line through the origin — the collection of all scalar multiples $\{c\mathbf{v}: c\in\mathbb{R}\}$.
This is a one-dimensional subspace of $V$.
When we allow addition as well as scaling, a finite collection of vectors generates a larger subspace.

**Definition 2.13 (Span).** The **span** of vectors $\mathbf{v}_1,\ldots,\mathbf{v}_k$ in a vector space $V$ is the collection of all their linear combinations:

$$
\operatorname{span}(\mathbf{v}_1,\ldots,\mathbf{v}_k)
    =
    \left\{
        c_1\mathbf{v}_1 + \cdots + c_k\mathbf{v}_k : c_i\in\mathbb{R}
    \right\}
$$

A set of vectors **spans** $V$ if every vector in $V$ can be written as a linear combination of vectors in the set.

> The span of a set of vectors is the smallest subspace containing them.
> It contains all vectors that can be built from the given ones using the operations permitted in a vector space.

**Example 2.14 (Spanning in $\mathbb{R}^2$).** In the plane, two nonzero vectors $\mathbf{v}_1,\mathbf{v}_2$ that point in different directions span all of $\mathbb{R}^2$.
Any point in the plane can be reached through an appropriate linear combination.
If the vectors point in the same (or opposite) directions, their span is merely a line through the origin.

**Example 2.15 (Spanning polynomials).** The polynomials $1, x,$ and $x^2$ span the space $\mathcal{P}_2$  — any quadratic polynomial $ax^2 + bx + c$ is a linear combination of these basic building blocks.
The same polynomials do not span $\mathcal{P}_3$, as no linear combination can produce a cubic term.

> Linear dependence means redundancy — one or more vectors could be removed without reducing the span.
> Independence means each vector contributes something genuinely new.

This leads to a fundamental question: when are vectors truly independent of one another?

**Definition 2.16 (Linear Independence).** A set of vectors $\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}$ in a vector space $V$ is **linearly independent** if the equation

$$
c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \mathbf{0}
$$

has only the trivial solution $c_1=c_2=\cdots=c_k=0$.
Otherwise, the vectors are **linearly dependent**.

**Example 2.17 (Dependence in $\mathbb{R}^n$).** Three vectors in $\mathbb{R}^2$ are always linearly dependent.
This is intuitively clear: the plane can be spanned by two vectors, so a third must be redundant.
More generally, if we have more vectors than dimensions, they must be linearly dependent.

**Example 2.18 (Polynomial independence).** The polynomials $1, x,$ and $x^2$ are linearly independent in $\mathcal{P}_2$.
If $a + bx + cx^2 = 0$ for all $x$, then each coefficient $a,b,c$ must be zero.
However, adding the polynomial $x^2+1$ to this collection creates linear dependence, as it can be written as a combination of $1$ and $x^2$.

The concepts of span and linear independence are complementary.
The span tells us what vectors we can build; linear independence tells us when we are building efficiently, without redundancy.
Together, they provide the foundation for understanding the structure of vector spaces and their subspaces.

Testing for linear independence is straightforward in principle: one must determine whether a homogeneous system of equations has only the trivial solution.
In practice, this means investigating whether certain collections of scalars must all be zero.
The following examples illustrate this process.

> *Foreshadowing:* The interplay between spanning and independence leads to the notion of a **basis** — a linearly independent set of vectors that spans the space.
> This fundamental concept will organize our understanding of vector spaces.

**Example 2.19 (Testing independence).** Consider the Euclidean vectors $(1,2)^T$ and $(2,4)^T$ in $\mathbb{R}^2$.
To test for linear independence, we examine

$$
c_1\begin{pmatrix}1\\2\end{pmatrix}
+
c_2\begin{pmatrix}2\\4\end{pmatrix}
=
\mathbf{0}
\quad
\Rightarrow
\quad
\begin{array}{rcl}
c_1 + 2c_2 &=& 0 \\
2c_1 + 4c_2 &=& 0
\end{array}
$$

The second equation is twice the first, yielding $c_1=-2c_2$ for any $c_2$.
Thus, these vectors are linearly dependent — $\mathbf{v}_2$ is twice $\mathbf{v}_1$.

> When testing independence, follow the zero vector.
> The key question is always: what coefficients yield the zero vector, and are they necessarily all zero?

## 2.5 Towards Dimension

The concept of dimension pervades our physical and mathematical worlds.
We speak of three-dimensional space, two-dimensional surfaces, one-dimensional lines.
Engineers routinely work in higher dimensions: a robotic arm with six joints traces paths in a six-dimensional configuration space; a neural network with billions of weights operates in a space beyond plain imagination.

Our task is to extract from these examples a definition of dimension that captures the essential feature: how many independent parameters are needed to specify a vector uniquely?
In $\mathbb{R}^n$, this is clear — we need exactly $n$ coordinates.
For other vector spaces, we must look to spanning sets and linear independence for guidance.

A spanning set for a vector space may be inefficient, containing redundant vectors.
A natural measure of dimension would count the vectors in a spanning set that carries no such redundancy.
Call a spanning set for $V$ **minimal** if no proper subset of it still spans $V$: nothing can be thrown away.

> Minimality is a statement about *this* set and its subsets, not a comparison with all other spanning sets.
> That the two amount to the same thing is what the rest of this section establishes.

Redundancy and dependence turn out to be the same phenomenon.

**Lemma 2.20 (Minimality & Independence).** A spanning set for a vector space $V$ is minimal if and only if it is linearly independent.

*Proof.* Suppose $S=\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}$ spans $V$ and is linearly dependent, so that $\sum_i c_i\mathbf{v}_i=\mathbf{0}$ with some $c_j\neq 0$.
Then

$$
\mathbf{v}_j = -\frac{1}{c_j}\sum_{i\neq j}c_i\mathbf{v}_i ,
$$

so every combination using $\mathbf{v}_j$ may be rewritten without it, and $S\setminus\{\mathbf{v}_j\}$ still spans: $S$ is not minimal.
Conversely, suppose $S$ is independent and that some $S\setminus\{\mathbf{v}_j\}$ still spans $V$.
Then $\mathbf{v}_j$ is a combination of the others, which is a nontrivial dependence — a contradiction. ∎

**Lemma 2.21 (Minimal Spanning Sets).** Any two minimal spanning sets of a vector space $V$ have the same size.

*Proof.* Let $S=\{\mathbf{v}_1,\ldots,\mathbf{v}_m\}$ and $T=\{\mathbf{w}_1,\ldots,\mathbf{w}_n\}$ be minimal spanning sets for $V$.
Since $S$ spans $V$, each $\mathbf{w}_j$ can be written as a linear combination of vectors in $S$:

$$
\mathbf{w}_j = \sum_{i=1}^m c_{ij}\mathbf{v}_i
$$

for some scalars $c_{ij}$.

We claim that $m\geq n$.
If not, then $m<n$, and we can write $n$ vectors ($\mathbf{w}_1,\ldots,\mathbf{w}_n$) as linear combinations of $m$ vectors ($\mathbf{v}_1,\ldots,\mathbf{v}_m$).
This would imply that $\{\mathbf{w}_1,\ldots,\mathbf{w}_n\}$ is linearly dependent.

To see this, consider the homogeneous system

$$
\sum_{j=1}^n x_j\mathbf{w}_j = \mathbf{0}
$$

Substituting the expressions for $\mathbf{w}_j$:

$$
\sum_{j=1}^n x_j\left(\sum_{i=1}^m c_{ij}\mathbf{v}_i\right) = \sum_{i=1}^m\left(\sum_{j=1}^n x_jc_{ij}\right)\mathbf{v}_i = \mathbf{0}
$$

This is a homogeneous system of $m$ equations in $n$ unknowns.
When $m<n$, such a system must have a nontrivial solution, implying that $\{\mathbf{w}_1,\ldots,\mathbf{w}_n\}$ is linearly dependent.
Yet $T$ is minimal, hence independent by Lemma 2.20 — a contradiction.

A symmetric argument, expressing each $\mathbf{v}_i$ in terms of the $\mathbf{w}_j$ and using Lemma 2.20 on $S$, shows that $n\geq m$.
Therefore $m=n$. ∎

The heart of that argument never used minimality of $S$: only that $S$ spans and that $T$ is independent.
That much is worth extracting, being the workhorse of every dimension count to come.

**Corollary 2.22 (Exchange Bound).** If $\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}$ spans $V$ and the set $\{\mathbf{w}_1,\ldots,\mathbf{w}_m\}$ in $V$ is linearly independent, then $m\leq k$.

*Proof.* Expressing each $\mathbf{w}_j$ over the $\mathbf{v}_i$ and running the computation above verbatim: if $m>k$, the homogeneous system of $k$ equations in $m$ unknowns has a nontrivial solution, making $\{\mathbf{w}_1,\ldots,\mathbf{w}_m\}$ dependent — contrary to hypothesis.
Hence $m\leq k$. ∎

> *Fact:* No independent set can outnumber any spanning set.
> Independence limits from below, spanning from above, and dimension is where the two meet.

This result — that all minimal spanning sets of a vector space have the same size — allows us to define dimension without ambiguity.

**Definition 2.23 (Dimension).** The **dimension** of a vector space $V$, denoted $\dim V$, is the size of any minimal spanning set for $V$.
If no finite spanning set exists, we say $V$ is **infinite-dimensional**.

**Example 2.24 (Polynomial dimension).** Consider the space $\mathcal{P}_n$ of polynomials of degree at most $n$.
Any such polynomial has the form

$$
p(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0
$$

A minimal spanning set consists of the monomials $\{1,x,x^2,\ldots,x^n\}$.
Thus $\dim\mathcal{P}_n = n+1$, not $n$  — we must count the constant term.
This subtle distinction reminds us that dimension counts parameters, not highest degree.

**Example 2.25 (Function spaces).** The space $C([a,b])$ of continuous functions on a closed interval $[a,b]$ with $a<b$ has no finite spanning set.
The monomials $1,x,\ldots,x^n$ are independent in it for every $n$, a vanishing combination of them being a polynomial with infinitely many roots and therefore the zero polynomial.
Were some collection of $k$ functions to span $C([a,b])$, Corollary 2.22 would cap every independent set at $k$ members; the monomials do not respect the cap.
Such spaces, lacking finite spanning sets, are called infinite-dimensional.

Finite-dimensional spaces admit complete description through a finite set of parameters; infinite-dimensional spaces resist such reduction.
This dichotomy shapes how we approach problems: finite-dimensional spaces yield to computational methods, while infinite-dimensional spaces often require approximation by finite-dimensional subspaces.

The counts observed in Example 1.2 are dimensions of spaces not yet named; the principle that binds them is one chapter away.
*Dimension is the one number a vector space cannot hide.*

—

## Engineering Signals as Vector Spaces

Engineering rests upon the measurement, analysis, and control of signals — time-varying quantities that encode information about physical systems.
The collection of all possible signals on a time interval forms a natural vector space, though one far removed from the familiar coordinate geometry of $\mathbb{R}^n$.
Understanding signals through vector spaces illuminates both their mathematical structure and practical manipulation.

Consider the collection $S[0,T]$ of all continuous signals $f:[0,T]\to\mathbb{R}$ defined on a fixed time interval $[0,T]$.
Two signals add through pointwise combination, while scalar multiplication scales a signal's amplitude:

$$
(f+g)(t) = f(t) + g(t) \quad : \quad (cf)(t) = c\cdot f(t)
$$

These operations satisfy our vector space axioms with no coordinates in sight.

> *Think:* The zero vector here is the signal that is identically zero at all times — the absence of any signal.
> Its role as additive identity mirrors its physical meaning as silence or darkness.

This space is infinite-dimensional, and inside it sits a natural sequence of subspaces, each of finite dimension.
For each positive integer $n$, let $V_n$ be spanned by $1$ and the first $n$ pairs of periodic signals:

$$
\left\{1,\, \cos\left(\frac{2\pi t}{T}\right), \sin\left(\frac{2\pi t}{T}\right),\, \cos\left(\frac{4\pi t}{T}\right), \sin\left(\frac{4\pi t}{T}\right),\, \ldots\right\}
$$

These subspaces form a **filtration** — a sequence $V_0 < V_1 < V_2 < \cdots < S[0,T]$, each containing more complex periodic patterns than the last.
A signal in $V_n$ combines at most $n$ different periodic components.

> *Historical Note:* Fourier scandalized the Paris Academy with his claim that arbitrary periodic functions could be captured by trigonometric series.
> The vector-space language used here arrived a century after his work on heat flow.

Linear independence takes on special meaning for signals.
Consider the signals $\sin(2\pi t/T)$ and $\cos(2\pi t/T)$ oscillating once over $[0,T]$.
No linear combination

$$
c_1\sin(2\pi t/T) + c_2\cos(2\pi t/T) = 0
$$

exists except the trivial one $c_1=c_2=0$, demonstrating their independence.
Similar independence holds between signals oscillating at different rates, allowing our sequence of subspaces to grow without redundancy.

> *Nota bene:* Though $S[0,T]$ itself is infinite-dimensional, any practical signal can be approximated arbitrarily well by elements from some finite-dimensional $V_n$.
> This principle underlies much of signal processing.

Different engineering contexts reveal other natural subspaces.
Signals that vanish at $t=0$ form a subspace modeling systems starting from rest.
Signals symmetric about $T/2$ form another subspace reflecting temporal symmetry.
Each such subspace captures both mathematical structure and physical meaning.

Signal processing itself becomes the study of transformations between signal spaces.
Filters map input signals to output signals while preserving vector space structure.
That linear combinations of inputs map to the same linear combinations of outputs reflects both mathematical elegance and engineering necessity.
An ideal low-pass filter, for instance, passes every signal in $V_n$ untouched while sending the highest frequencies to zero; the collection of signals it silences is itself a subspace: the *kernel* of the filter, as Chapter 3 will name it.

This perspective — of signals as vectors in an abstract space rather than mere functions of time — reveals structure that coordinates obscure.

—

## Linear Differential Equations

Calculus and linear algebra are married in the theory of linear differential equations.
Consider an equation governing some physical quantity $x(t)$, where multiple derivatives appear linearly:

$$
\frac{d^nx}{dt^n} + a_{n-1}\frac{d^{n-1}x}{dt^{n-1}} + \cdots + a_1\frac{dx}{dt} + a_0x = 0
$$

Though seemingly far from the vector spaces studied in this chapter, a familiar structure surfaces once the right notation is chosen.

Let us adopt the concise notation $D = d/dt$ for the differentiation operator.
Our equation becomes

$$
(D^n + a_{n-1}D^{n-1} + \cdots + a_1D + a_0)x = 0
$$

or more simply $p(D)x = 0$, where $p \in \mathcal{P}_n$ is a polynomial of degree $n$.
This operator notation transforms differential equations into algebraic objects — a first hint of deeper patterns.

The solutions to this equation form a vector space of dimension exactly $n$ — a fact whose proof must wait for later chapters.
That is, there exist $n$ special solutions forming a minimal spanning set, from which all other solutions arise through linear combination.
This single fact organizes the solving of such equations.

> *Foreshadowing:* the solution space consists of exactly those functions that $p(D)$ sends to zero.
> Chapter 3 will name such a set the *kernel*: to solve a linear ODE is to compute $\operatorname{ker} p(D)$.

The structure becomes clearest when $p$ factors completely:

$$
p(D) = (D-\lambda_1)(D-\lambda_2)\cdots(D-\lambda_n)
$$

where $\lambda_1,\ldots,\lambda_n$ are distinct numbers whose meaning will become clear in Chapter 7.
For now, observe that the simplest case $n=1$ yields the equation:

$$
(D-\lambda)x = 0 \quad\Rightarrow\quad \frac{dx}{dt} = \lambda x
$$

whose solution $x(t) = ce^{\lambda t}$ you certainly recall from calculus.

> *Foreshadowing:* Chapter 7 will reveal the deeper meaning of the numbers $\lambda_i$ and provide systematic methods for finding basis solutions even when $p(D)$ does not factor so nicely.

Abstract structures have a way of surfacing where least expected: the vector spaces introduced in this chapter are not formal constructions but natural languages for describing physical systems.

—

## Exercises: Chapter 2

1. Section 2.1 states that the positive reals $\mathbb{R}_{>0}$, under ordinary addition and ordinary scalar multiplication, fail to be a vector space, and asks which of the eight axioms of Definition 2.1 survive: answer the question, and say which of the two operations fails even to return an element of $\mathbb{R}_{>0}$.
Now, on the same set, define instead $x\oplus y=xy$ and $c\odot x=x^c$, and verify all eight.
Identify the zero vector and the additive inverse of $x$, and give a minimal spanning set and the dimension.

    > *Caveat:* The same set $\mathbb{R}_{>0}$ appears twice in this problem, with opposite verdicts.
    > Being a vector space is never a property of the set alone.

2. On the set $\mathbb{R}^2$, keep ordinary addition but define scaling by $c\cdot(a,b)^T=(ca,b)^T$; exactly one of the eight axioms of Definition 2.1 fails, so find it and exhibit scalars and a vector for which its two sides differ.
Lemma 2.2 proves the zero vector unique from the axioms alone; in that style, prove that $0\mathbf{v}=\mathbf{0}$ and that $c\mathbf{0}=\mathbf{0}$, naming the axiom each proof consumes.
The two look like the same proof and are not: test both statements in this $\mathbb{R}^2$, where exactly one survives, and check that your record says in advance which.

3. Consider the following vectors in $\mathbb{R}^3$:


$$
\mathbf{v}_1 = \begin{pmatrix}1\\2\\1\end{pmatrix}, \quad
        \mathbf{v}_2 = \begin{pmatrix}2\\4\\-1\end{pmatrix}, \quad
        \mathbf{v}_3 = \begin{pmatrix}3\\6\\0\end{pmatrix} .
$$

Show that they are linearly dependent by exhibiting scalars, not all zero, whose combination vanishes, and give the dimension of their span.
Find a single linear equation in $x,y,z$ whose solution set is exactly that span.
Use it, without any further elimination, to decide which of $(4,8,1)^T$ and $(1,1,0)^T$ lies in the span, and write that one as a combination of $\mathbf{v}_1$ and $\mathbf{v}_2$.

4. Consider the following matrices in $\mathbb{R}^{2\times 2}$:


$$
A_1 = \begin{bmatrix}1&1\\0&1\end{bmatrix}, \quad
        A_2 = \begin{bmatrix}2&1\\1&0\end{bmatrix}, \quad
        A_3 = \begin{bmatrix}4&3\\1&2\end{bmatrix} .
$$

Show that $A_3$ lies in $\operatorname{span}(A_1,A_2)$ by exhibiting the scalars.
Then find the matrix in $\operatorname{span}(A_1,A_2)$ whose diagonal entries sum to $2$ and whose off-diagonal entries sum to $3$, and explain why there is exactly one.

5. Consider the following vectors in $\mathbb{R}^4$:


$$
\mathbf{v}_1 = \begin{pmatrix}1\\0\\1\\1\end{pmatrix}, \quad
        \mathbf{v}_2 = \begin{pmatrix}2\\1\\0\\-1\end{pmatrix}, \quad
        \mathbf{v}_3 = \begin{pmatrix}1\\2\\-1\\0\end{pmatrix} ,
$$

and write $S=\{\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3\}$.
Show that $S$ is linearly independent, and express $\mathbf{w} = (8,8,-2,-1)^T$ over $S$, explaining why your answer is the only one.
Show that $\mathbf{u} = (8,7,-1,-3)^T$ is *not* in $\operatorname{span}(S)$, so that $S$ does not span $\mathbb{R}^4$.
Could any three vectors span $\mathbb{R}^4$?

6. In the space $\mathcal{P}_2$ of polynomials of degree at most 2, let


$$
q_1(x)=1+x^2, \qquad q_2(x)=x-x^2, \qquad q_3(x)=1+x .
$$

Express $p(x)=3x^2-x+2$ as a linear combination of $q_1,q_2,q_3$ in *two* different ways, and say what this reveals about the set $\{q_1,q_2,q_3\}$.
Give the dimension of $\operatorname{span}(q_1,q_2,q_3)$, and exhibit a polynomial in $\mathcal{P}_2$ that is not in that span.

7. For the matrix


$$
A = \begin{bmatrix}
        1 & 2 & 1 \\
        2 & 4 & -1 \\
        -1 & -2 & 3
        \end{bmatrix}
$$

find a minimal spanning set for $\operatorname{row}(A)$ and one for $\operatorname{col}(A)$.
Show that $\operatorname{col}(A)$ is exactly the set of $\mathbf{b}=(b_1,b_2,b_3)^T$ satisfying a single linear equation, and use that equation — without performing elimination — to decide which of $A\mathbf{x}=(2,1,2)^T$ and $A\mathbf{x}=(1,0,0)^T$ is solvable, then solve the one that is.
Finally, exhibit the combination of the columns of $A$ that equals $\mathbf{0}$, say which column it identifies as redundant, and check that $\operatorname{row}(A)$ and $\operatorname{col}(A)$  — both planes in $\mathbb{R}^3$  — are not the same plane.

8. For each of the following, decide whether it is a subspace of the indicated space, and wherever one of the three conditions of the subspace test fails, give the explicit witness that breaks it: the singular matrices $\{A\in\mathbb{R}^{2\times2}:\det A=0\}$; the polynomials in $\mathcal{P}_2$ all of whose coefficients are integers; the set of $A\in\mathbb{R}^{2\times2}$ with $A(1,1)^T=(0,0)^T$; and the empty set in $\mathbb{R}^3$.
Use two of your verdicts to show that neither closure condition of the test implies the other.
The marginnote at the subspace test claims that condition 1 is redundant given condition 3: say which item on your list shows that this claim requires one further hypothesis, and what that hypothesis is.

9. Let $V<\mathbb{R}^{3\times 3}$ be the set of symmetric matrices ($A^T=A$) and $W<\mathbb{R}^{3\times 3}$ the set of **skew-symmetric** matrices, those with $A^T=-A$.
Show that both are subspaces, and that $\dim V=6$ and $\dim W=3$, by writing down a minimal spanning set for each and proving it independent.
Prove that $\mathbb{R}^{3\times 3}=V\oplus W$, and carry out the decomposition of


$$
M=\begin{bmatrix}2&3&0\\-1&-1&4\\2&0&3\end{bmatrix} .
$$

10. Return to the system of Example 1.2,


$$
A = \begin{bmatrix}
        -1 & 0 & -1 & 0 \\
        1 & -1 & 0 & 0 \\
        0 & 1 & 1 & 0 \\
        0 & 0 & 0 & -1 \\
        0 & 0 & 0 & 1
        \end{bmatrix} ,
$$

where solvability of $A\mathbf{x}=\mathbf{b}$ was found to require $b_1+b_2+b_3=0$ and $b_4+b_5=0$.
Show that the achievable right-hand sides are exactly $\operatorname{col}(A)$, of dimension $\operatorname{rank}(A)=3$.
For $\mathbf{b} = (-1,0,1,-2,2)^T$, find one solution and show the full solution set is a translate of the null space of $A$, not a subspace.
Then find the subspace $\{\mathbf{y}\in\mathbb{R}^5 : \mathbf{y}^TA = \mathbf{0}^T\}$, and identify which of its vectors manufactures which of the two constraints.

    > *Foreshadowing:* Of the four spaces this example conceals, three have names by now — the column space, the row space, and the null space.
    > The fourth, the obstruction space found here, must wait for Chapter 3.

11. A data record is a vector $\mathbf{x}\in\mathbb{R}^5$ of five measurements with **mean** $\bar{x} = \frac{1}{5}(x_1+\cdots+x_5)$; let $\mathbf{1}=(1,1,1,1,1)^T$, let $L=\operatorname{span}(\mathbf{1})$, and let $W$ be the set of **centered** records, those of mean zero.
Show that $W$ is the null space of a $1\times5$ matrix, hence a subspace, and that $\dim W=4$.
Show that $\mathbb{R}^5 = L\oplus W$ and decompose $\mathbf{x}=(4,7,1,5,3)^T$ accordingly; then show that recording the same data against a shifted zero point, $\mathbf{x}+c\mathbf{1}$, changes only the $L$-summand.

12. The marginnote accompanying Definition 2.13 claims that the span of a set of vectors is the smallest subspace containing them.
Make this precise and prove it: for $\mathbf{v}_1,\ldots,\mathbf{v}_k$ in a vector space $V$, show that $S=\operatorname{span}(\mathbf{v}_1,\ldots,\mathbf{v}_k)$ is a subspace, that it contains each $\mathbf{v}_i$, and that $S\subseteq W$ whenever $W<V$ contains every $\mathbf{v}_i$.
Conclude that $S$ is the intersection of all subspaces of $V$ containing $\mathbf{v}_1,\ldots,\mathbf{v}_k$.

13. Let $B=\{\mathbf{b}_1,\ldots,\mathbf{b}_k\}$ be a linearly independent set in a vector space $V$, and let $\mathbf{v}\in V$.
Prove that $\{\mathbf{v},\mathbf{b}_1,\ldots,\mathbf{b}_k\}$ is linearly independent if and only if $\mathbf{v}\notin\operatorname{span}(\mathbf{b}_1,\ldots,\mathbf{b}_k)$.
Deduce that if $U<V$ is a subspace containing $B$ and $\mathbf{v}\notin U$, then $\{\mathbf{v}\}\cup B$ is linearly independent, and give an example showing that the converse of this last statement is false.

14. For vectors $\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3$ in a vector space $V$, prove or disprove: if $\mathbf{v}_1$ and $\mathbf{v}_2$ are linearly independent, and $\{\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3\}$ is linearly dependent, then $\mathbf{v}_3$ must lie in $\operatorname{span}(\mathbf{v}_1,\mathbf{v}_2)$.
Then show that the independence of $\mathbf{v}_1$ and $\mathbf{v}_2$ cannot be dropped, by exhibiting three vectors in $\mathbb{R}^3$ that are linearly dependent with $\mathbf{v}_3\notin\operatorname{span}(\mathbf{v}_1,\mathbf{v}_2)$.

15. In the space $\mathcal{P}_2$, let $U$ be the set of **even** polynomials (those with $p(-x)=p(x)$) and $W$ the set of **odd** polynomials (those with $p(-x)=-p(x)$).
Show that both are subspaces, find a minimal spanning set for each, and prove that $\mathcal{P}_2=U\oplus W$.
Verify that the decomposition your argument produces agrees with


$$
p(x)=\frac{p(x)+p(-x)}{2}+\frac{p(x)-p(-x)}{2} ,
$$

and explain why this second formula proves the same splitting for the space of *all* polynomials, where no coefficient count is available.

16. Let $V = \mathbb{R}^{2\times 2}$, let $U$ be the subspace of upper triangular matrices, $W$ the subspace of lower triangular matrices, and $W_0<W$ the subspace of *strictly* lower triangular matrices.
Show that $V = U\oplus W_0$, and that although $U+W=V$ as well, the sum $U+W$ is not direct — exhibit $U\cap W$ explicitly.
Find a second subspace $W'\neq W_0$ with $V=U\oplus W'$: is the complement of $U$ determined by $U$?
Compute $\dim U$, $\dim W$, $\dim W_0$ and $\dim V$, and say why a sum of subspaces filling up $V$ is not by itself enough to make that sum direct.

17. Let $U$ and $W$ be subspaces of a vector space $V$ with $V = U+W$.
Prove that the following are equivalent: $U\cap W = \{\mathbf{0}\}$, so that $V = U\oplus W$; every $\mathbf{v}\in V$ can be written as $\mathbf{v}=\mathbf{u}+\mathbf{w}$ with $\mathbf{u}\in U$ and $\mathbf{w}\in W$ in exactly one way; and the only way to write $\mathbf{0} = \mathbf{u}+\mathbf{w}$ with $\mathbf{u}\in U$ and $\mathbf{w}\in W$ is $\mathbf{u}=\mathbf{w}=\mathbf{0}$.
Where did you use that $U$ and $W$ are subspaces rather than arbitrary subsets?

18. *(Challenge.)* This chapter defines a direct sum of *two* subspaces by the condition $W_1\cap W_2=\{\mathbf{0}\}$, and one might guess that for three subspaces the right condition is that all three pairwise intersections are trivial.
In $\mathbb{R}^2$, let $U_1=\operatorname{span}\left((1,0)^T\right)$, $U_2=\operatorname{span}\left((0,1)^T\right)$, and $U_3=\operatorname{span}\left((1,1)^T\right)$: verify that $U_i\cap U_j=\{\mathbf{0}\}$ for every $i\neq j$ and that $U_1+U_2+U_3=\mathbb{R}^2$, then exhibit infinitely many ways of writing $(1,1)^T$ as $\mathbf{u}_1+\mathbf{u}_2+\mathbf{u}_3$ with $\mathbf{u}_i\in U_i$.
Show that $U_1\cap U_2=\{\mathbf{0}\}$ together with $(U_1+U_2)\cap U_3=\{\mathbf{0}\}$ *does* force uniqueness — apply Exercise 17 twice — and check that this example fails it.

19. *(Challenge.)* Let $U$ and $W$ be finite-dimensional subspaces of a vector space $V$.
Using Exercise 13 repeatedly, and Corollary 2.22 to see that the process must stop, show that a minimal spanning set for any subspace $X<U$ enlarges to one for $U$.
Enlarge a minimal spanning set for $U\cap W$ in two separate ways, to $B_U$ for $U$ and $B_W$ for $W$, and prove that $B_U\cup B_W$ is a minimal spanning set for $U+W$, so that $\dim(U + W) = \dim U + \dim W - \dim(U\cap W)$  — the arithmetic already seen in Exercises 9 and 16.
Deduce that two distinct planes in $\mathbb{R}^3$ must always meet in a line, however they are placed.

---


# Chapter 3. Linear Transformations

*"he became what he beheld; he became what he was doing; he was himself transform'd"*

**The essence of Mathematics** lies not in objects but in transformations between them.
The vectors and spaces we have thus far studied come alive only when acted upon — rotated, scaled, projected, or otherwise transformed.
Such transformations are the verbs to our nouns.
Linear transformations are those which preserve the fundamental operations of vector spaces: addition and scaling.
This seemingly modest requirement — that our transformations respect vector space structure — leads to a theory whose practical reach the rest of this text measures.

Vector spaces, in isolation, are static collections.
The power of linear algebra emerges when we consider mappings which morph from input signals to output responses, from configurations to forces, from high-dimensional data to low-dimensional representations.
Such mappings, when linear, admit a structure both computable and exact.

The operations of differentiation and integration, though far from geometric, share deep structural features with their matrix cousins.
This abstraction reveals four fundamental spaces associated with any linear transformation — the kernel and image that capture what vanishes and what is attained, the coimage and cokernel that measure efficiency and defect.
These spaces, seemingly distinct, are bound together by the Fundamental Theorem of Linear Algebra, a result that unifies the algebraic, geometric, and dimensional aspects of linear transformations into a single coherent picture.

## 3.1 Euclidean Transformations

Our story begins in familiar territory — with matrices acting on vectors in Euclidean space.
From multivariable calculus, we recall how multiplication by a matrix $A$ transforms vectors in $\mathbb{R}^n$, taking input vector $\mathbf{x}$ to output $A\mathbf{x}$.
Though we performed such operations mechanically, computing products column-by-row, these transformations have rich geometric content worth savoring before abstraction.

The simplest such transformations scale space uniformly.
A matrix $cI$ multiplies each coordinate by the scalar $c$, dilating or contracting space about the origin.
More interesting are matrices that scale different directions differently:

$$
\begin{bmatrix}
2 & 0 \\
0 & 1/2
\end{bmatrix}
\begin{pmatrix}
x \\ y
\end{pmatrix}
=
\begin{pmatrix}
2x \\ y/2
\end{pmatrix}
$$

Such transformations stretch space along one axis while compressing along another — like a funhouse mirror's distortion rendered precise in coordinates.

Rotations in the plane arise from matrices of the form

$$
\begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix}
$$

spinning vectors through angle $\theta$ counterclockwise about the origin.
That such matrices preserve lengths and angles is a consequence of their structure — see Chapter 5.

More subtle are **shear transformations**, such as

$$
\begin{bmatrix}
1 & h \\
0 & 1
\end{bmatrix}
$$

> *Question:* What happens with the transpose of this horizontal shear?

which offset each horizontal line by an amount proportional to its height.
These preserve area while tilting vertical lines — like a deck of cards carefully slid across a table.

These elementary transformations — scaling, rotation, and shear — combine to generate all linear transformations in the plane.
Any $2\times 2$ matrix can be understood as a composition of such basic geometric operations.
This decomposition previews deeper structure to come, when we learn to factor matrices into simpler constituent parts.

What features do these transformations share, beyond their realization through matrix multiplication?
First, they preserve the origin — the zero vector remains fixed.
Second, they respect vector addition: the image of a sum equals the sum of the images.
Third, they interact naturally with scalar multiplication: doubling an input vector doubles its image.
These properties — seemingly obvious in the matrix setting — will form the scaffolding for our abstract theory.

> *Foreshadowing:* The properties we observe in matrix transformations — preservation of vector operations — will define linearity in the abstract setting.

Consider as well what these transformations can destroy.
A rotation preserves distances but changes coordinates.
A shear preserves areas but distorts angles.
A scaling changes both distances and areas, but preserves lines through the origin.
This selective preservation of geometric features hints at deeper invariants — quantities or properties that remain unchanged under certain classes of transformations.

The matrix transformation $A\mathbf{x}$ converts geometric intuition about transforming space into algebraic manipulation of coordinates.
As we lift these ideas to abstract vector spaces, this interplay between geometry and algebra will remain.
Though we may lose the ability to visualize transformations directly, the core ideas — preservation of vector operations, study of invariants, decomposition into simpler parts — will guide our development.

## 3.2 Definitions & Implications

Our experience with Euclidean transformations suggests key features that characterize the essence of linearity: preservation of addition and scaling.
Many important transformations share these algebraic properties while lacking obvious geometric interpretation.
This motivates abstracting away from geometry to study linear transformations between arbitrary vector spaces.

**Definition 3.1 (Linear Transformation).** Let $V$ and $W$ be vector spaces.
A **linear transformation** $T:V\to W$ is a function satisfying two properties:

1. Additivity: $T(\mathbf{v_1}+\mathbf{v_2}) = T(\mathbf{v_1})+T(\mathbf{v_2})$ for all $\mathbf{v_1},\mathbf{v_2}\in V$

2. Homogeneity: $T(c\mathbf{v}) = cT(\mathbf{v})$ for all $c\in\mathbb{R}$ and $\mathbf{v}\in V$

These two properties combine to ensure that linear transformations preserve linear combinations.

**Lemma 3.2.** A linear transformation $T:V\to W$ satisfies:

1. $T(\mathbf{0})=\mathbf{0}$

2. $T(-\mathbf{v})=-T(\mathbf{v})$ for all $\mathbf{v}\in V$

3. $T$ preserves linear combinations


$$
T\left(\sum_{i=1}^nc_i\mathbf{v_i}\right)
    =
    \sum_{i=1}^nc_iT(\mathbf{v_i})
$$

The preservation of linear combinations has an important consequence for subspaces: linear transformations send subspaces to subspaces.

**Lemma 3.3.** If $T:V\to W$ is linear and $U<V$, then $T(U)<W$.

Linear transformations may themselves be combined.
Two transformations $S,T:V\to W$ add pointwise, $(S+T)(\mathbf{v}) = S(\mathbf{v})+T(\mathbf{v})$, and scale pointwise, $(cT)(\mathbf{v}) = c\,T(\mathbf{v})$; both results are again linear, so the collection of all linear transformations $V\to W$ is itself a vector space.
The composition $S\circ T$ of linear transformations is linear as well, and the **identity transformation** $\mathrm{id}_V:V\to V$ leaves every vector where it found it.

### 3.2 Examples of Linear Transformations

The simplest examples of linear transformations are those of the previous section — any matrix $A$ acts on Euclidean vectors via the linear transformation $T_A(\mathbf{x}) = A\mathbf{x}$.
This is so natural that it is hardly worth calling out as anything different than the matrix itself.
However, not all linear transformations are so explicit in coordinates.
Consider the following examples of a less geometric nature.

**Example 3.4 (Differentiation).** Consider the differentiation operator $D=d/dx$ from calculus.
This satisfies linearity in that $D(f+g)=Df+Dg$ for differentiable functions $f$ and $g$; and $D(cf) = c\,Df$ for $c$ a scalar.
As such, it defines a linear transformation from $C^\infty(\mathbb{R})$ to itself.
If finite-dimensional vector spaces are preferred, one can restrict to polynomials, in which case $D:\mathcal{P}_n\to\mathcal{P}_{n-1}$:

> Note that the subspace of constant polynomials is sent to zero.
> What happens to other subspaces of $\mathcal{P}_n$?

$$
D\left(\sum_{i=0}^n c_ix^i\right)
    =
    \left(\sum_{j=1}^{n} jc_jx^{j-1}\right) .
$$

Here we see linearity without geometry — derivatives of sums are sums of derivatives, and constants factor out of derivatives.

**Example 3.5 (Integration).** The definite integration operator $\mathrm{I}:C([a,b])\to\mathbb{R}$ defined by

$$
\mathrm{I}(f) = \int_a^b f(x)dx
$$

is, like differentiation, linear.
What happens when we restrict attention to polynomials and to subspaces of polynomials?

The relationship between linear transformations and linear independence cuts to the heart of their structure.

**Definition 3.6 (Injective and Surjective).** A linear transformation $T:V\to W$ is:

1. **injective** (or **one-to-one**) if distinct inputs yield distinct outputs: $T(\mathbf{v_1})=T(\mathbf{v_2})$ implies $\mathbf{v_1}=\mathbf{v_2}$

2. **surjective** (or **onto**) if every vector in $W$ is the image of some vector in $V$: for each $\mathbf{w}\in W$ there exists $\mathbf{v}\in V$ such that $T(\mathbf{v})=\mathbf{w}$

**Lemma 3.7.** For a linear transformation $T:V\to W$:

1. $T$ is injective if and only if it preserves linear independence

2. $T$ is surjective if and only if $T(V)=W$

3. $T$ is invertible if and only if it is both injective and surjective

> *Caveat:* A linear transformation can fail to be invertible in two distinct ways: by mapping different vectors to the same image (non-injective) or by missing vectors in the target space (non-surjective).

## 3.3 Isomorphisms

When are two vector spaces fundamentally the same?
The geometric vectors in $\mathbb{R}^2$ seem quite different from the linear polynomials $ax+b$, yet both allow the same operations and satisfy the same rules.
Such observations lead us to examine what it means for vector spaces to be indistinguishable from the perspective of linear algebra.

Linear transformations are directed mappings between two vector spaces.
Given $T:V\to W$, we call $V$ the **domain** and $W$ the **codomain**.
To serve as a perfect dictionary between spaces, $T$ must possess both properties introduced in Definition 3.6: it must be both injective and surjective.
Such transformations are called isomorphisms:

> *Terminology:* The use of **codomain** may be unfamiliar, as it stems from category theory.
> Such is also the case with the terms **monomorphism** and **epimorphism** for injective and surjective maps respectively, though we shall not use those particular terms.

**Definition 3.8 (Isomorphism).** Vector spaces $V$ and $W$ are **isomorphic**, denoted $V\cong W$, if there exists an **isomorphism** between them — a linear transformation that is both injective and surjective.

**Example 3.9 (Coordinate vectors).** The transformation $T:\mathbb{R}^2\to\mathcal{P}_1$ sending vectors to linear polynomials via

$$
\begin{pmatrix}a\\b\end{pmatrix} \mapsto a + bx
$$

> *Nota bene:* The same trick gives $\mathbb{R}^{2\times 2}\cong\mathbb{R}^4$  — matrix multiplication is invisible to the vector space structure.

is an isomorphism.
It provides a perfect dictionary between geometric vectors and linear polynomials, preserving all vector space operations.
Addition of vectors corresponds to addition of polynomials; scaling vectors means scaling polynomials.

Not all linear transformations achieve this perfect correspondence.
The projection $\Pi_{}:\mathbb{R}^3\to\mathbb{R}^2$ given by

$$
\Pi_{}\begin{pmatrix}x\\y\\z\end{pmatrix} = \begin{pmatrix}x\\y\end{pmatrix}
$$

is surjective but not injective — it reaches every point in the plane but collapses all points differing only in their $z$-coordinate.
Conversely, the embedding $\iota:\mathbb{R}^2\to\mathbb{R}^3$ given by

$$
\iota\begin{pmatrix}x\\y\end{pmatrix} = \begin{pmatrix}x\\y\\0\end{pmatrix}
$$

is injective but not surjective — it preserves all information about vectors in the plane but misses most of $\mathbb{R}^3$.

> *Question:* Are any two vector spaces with the same dimension in fact isomorphic?

These examples suggest a deep truth: vector spaces of different dimensions cannot be isomorphic.
The projection above shows that a larger space cannot inject into a smaller one without collapsing; the embedding shows a smaller space cannot surject onto a larger one without missing vectors.
This observation — though as yet unproven — hints at the fundamental nature of dimension in linear algebra.

The language of isomorphisms provides more than mere classification — it offers a perspective on what features of vector spaces truly matter.
When spaces are isomorphic, we may freely translate problems between them, choosing whichever representation is most convenient.
The geometric intuition of $\mathbb{R}^n$ becomes available to spaces of polynomials, matrices, or signals, provided we have constructed the right dictionary between them.

**Example 3.10 (Polynomial derivatives).** The differentiation operator $D:\mathcal{P}_2\to\mathcal{P}_1$ given by

$$
D(ax^2 + bx + c) = 2ax + b
$$

is surjective but not injective.
Every linear polynomial is a derivative (surjective), but constants vanish under differentiation (non-injective).

## 3.4 Image & Kernel

The subspaces we encountered in Chapter 2 arose from operations within a single vector space.
Linear transformations generate their own characteristic subspaces — in both domain and codomain.
These subspaces capture the essential features of how the transformation acts, measuring both its effectiveness and its defects.

Fix throughout a linear transformation $T:V\rightarrow W$ between vector spaces.
The first subspace of interest lies in the codomain.

**Definition 3.11 (Image).** The **image** of $T$, denoted $\operatorname{im} T$, is the subspace of the codomain consisting of all possible outputs:

$$
\operatorname{im} T = \{T(\mathbf{v}): \mathbf{v}\in V\} < W
$$

That this is indeed a subspace of $W$ follows readily: the zero vector is certainly in the image (as $T(\mathbf{0})=\mathbf{0}$), and if $T(\mathbf{v_1})$ and $T(\mathbf{v_2})$ are any vectors in the image, then their sum $T(\mathbf{v_1})+T(\mathbf{v_2})=T(\mathbf{v_1}+\mathbf{v_2})$ is also in the image, as is any scalar multiple.
The image measures the "reach" of the transformation — how much of $W$ can be attained as output.

**Definition 3.12 (Kernel).** The **kernel** (or **null space**) of $T$, denoted $\operatorname{ker} T$, is the subspace of the domain consisting of all vectors that vanish under $T$:

$$
\operatorname{ker} T = \{\mathbf{v}\in V: T(\mathbf{v})=\mathbf{0}\} < V
$$

That this too forms a subspace of $V$ is again straightforward: the zero vector is certainly in the kernel; and if $\mathbf{v_1}$ and $\mathbf{v_2}$ are in the kernel, then $T(\mathbf{v_1}+\mathbf{v_2})=T(\mathbf{v_1})+T(\mathbf{v_2})=\mathbf{0}$, with scalar multiples following similarly.
The kernel captures what the transformation cannot "see" — the vectors that disappear under its action.

These abstract definitions crystallize our earlier work with linear systems.
Consider the matrix equation $A\mathbf{x}=\mathbf{b}$ from Chapter 1.
This defines a linear transformation $T_A:\mathbb{R}^n\rightarrow\mathbb{R}^m$ via $T_A(\mathbf{x})=A\mathbf{x}$.
The standard questions about this system now have geometric meaning:

1. Does a solution exist? Yes if and only if $\mathbf{b}\in\operatorname{im} T_A$.

2. Is the solution unique? Yes if and only if $\operatorname{ker} T_A=\{\mathbf{0}\}$.

3. If more than one solution exists, how are they related?
    They differ by elements of $\operatorname{ker} T_A$.

**Example 3.13 (Calculus operators).** The differentiation operator $D:C^1([a,b])\rightarrow C([a,b])$ has kernel consisting of all constant functions on $[a,b]$  — these are precisely the functions that vanish under differentiation.
Its image consists of all continuous functions that arise as derivatives, a proper subspace of $C([a,b])$ (not every continuous function is a derivative).

The definite integration operator $\mathrm{I}:C([a,b])\rightarrow\mathbb{R}$ defined by $\mathrm{I}(f)=\int_a^b f(x)dx$ has (very large) kernel consisting of all functions whose integral over $[a,b]$ vanishes.
Its image is all of $\mathbb{R}$  — any real number can be realized as the integral of some continuous function.

> *Foreshadowing:* The relationship between the dimensions of kernel and image will prove fundamental to understanding linear transformations.
> This balance between what vanishes and what is attained is captured in the Fundamental Theorem at the end of this chapter.

These subspaces provide the first tools for analyzing the structure of linear transformations.
A transformation is one-to-one precisely when its kernel contains only the zero vector; it is onto when its image is the entire codomain.
The interplay between these subspaces — how their dimensions balance, how they decompose the spaces involved — leads to the deeper theory ahead.

## 3.5 Rank & Nullity

The dimension of a vector space captures its size and complexity.
For a linear transformation, we seek similar measures of size and complexity — not of a single space, but of how the transformation acts between spaces.
These measures arise naturally from the dimensions of image and kernel.

**Definition 3.14 (Rank & Nullity).** The **rank** of a linear transformation $T:V\rightarrow W$ is the dimension of its image:

$$
\operatorname{rank} T = \dim(\operatorname{im} T)
$$

The **nullity** of $T$ is the dimension of its kernel:

$$
\operatorname{null} T = \dim(\operatorname{ker} T)
$$

This abstracts the pedestrian notion of matrix rank from Definition 1.12.
When $T$ is represented by a matrix $A$, the abstract and concrete ranks coincide.

> *Think:* light through crystal — rank counts the directions transmitted; nullity, the directions absorbed.

**Example 3.15 (Matrix Rank and Nullity).** For a $3\times 4$ matrix $A$ of rank 2, the transformation $T_A:\mathbb{R}^4\rightarrow\mathbb{R}^3$ has:

1. $\operatorname{rank} T_A = 2$, meaning $\operatorname{im} T_A$ is a plane in $\mathbb{R}^3$

2. $\operatorname{null} T_A = 2$, as solving $A\mathbf{x}=\mathbf{0}$ yields a two-dimensional solution space

3. $\dim(\operatorname{ker} T_A) + \dim(\operatorname{im} T_A) = \dim(\mathbb{R}^4) = 4$

This last observation hints at a deeper relationship between rank and nullity.

**Example 3.16 (Calculus operators).** The differentiation operator $D:\mathcal{P}_n\rightarrow\mathcal{P}_{n-1}$ has:

1. $\operatorname{rank} D = n$, as every polynomial in $\mathcal{P}_{n-1}$ is a derivative

2. $\operatorname{null} D = 1$, as only constant functions vanish under differentiation

3. $\dim(\operatorname{ker} D) + \dim(\operatorname{im} D) = \dim(\mathcal{P}_n) = n+1$

Again we see the dimensions balance.

**Example 3.17 (Integration).** Consider the definite integration operator $\mathrm{I}:C([0,1])\rightarrow\mathbb{R}$ defined by $\mathrm{I}(f)=\int_0^1 f(x)dx$.
Though $C([0,1])$ is infinite-dimensional:

1. $\operatorname{rank} \mathrm{I} = 1$, as the image is all of $\mathbb{R}$

2. $\operatorname{null} \mathrm{I}$ is infinite, the kernel containing all functions whose integral vanishes

3. The dimensional balance sets one infinity against another and settles nothing

What infinite dimension destroys here is the arithmetic, and only the arithmetic.
The constant functions meet $\operatorname{ker}\mathrm{I}$ in the zero function alone, no nonzero constant having zero integral, and together with $\operatorname{ker}\mathrm{I}$ they fill $C([0,1])$, since every $f$ is its own average over $[0,1]$ plus a remainder of zero integral.
On the constants $\mathrm{I}$ is a bijection onto $\mathbb{R}$, exactly as in the finite case.
The correspondence survives; the subtraction does not.

> *Caveat:* The relationship between rank and nullity becomes more subtle in infinite dimensions, where the equation stops counting anything.
> The examples here are meant to build intuition in the finite-dimensional case.

These examples suggest deep connections between rank, nullity, and the dimensions of domain and codomain.

## 3.6 Quotients

Linear transformations reveal structure not only through what they preserve, but through what they collapse.
The manner in which different vectors map to identical outputs suggests a natural organization — grouping vectors that transform identically.
This insight leads to the quotient space — the construction on which the Fundamental Theorem will turn.

**Definition 3.18 (Quotient Space).** Let $V$ be a vector space and $U<V$ a subspace.
The **quotient space** $V/U$ is the vector space whose elements are equivalence classes of vectors in $V$, where vectors $\mathbf{v}_1,\mathbf{v}_2\in V$ are equivalent if and only if their difference lies in $U$:

$$
\mathbf{v}_1 \sim \mathbf{v}_2 \iff \mathbf{v}_1-\mathbf{v}_2 \in U
$$

The equivalence class of $\mathbf{v}\in V$, denoted $[\mathbf{v}]$, consists of all vectors equivalent to $\mathbf{v}$:

$$
[\mathbf{v}] = \{\mathbf{w}\in V : \mathbf{w}-\mathbf{v}\in U\} = \mathbf{v}+U
$$

Vector operations on $V/U$ are defined through representatives: $[\mathbf{v}_1]+[\mathbf{v}_2]=[\mathbf{v}_1+\mathbf{v}_2]$ and $c[\mathbf{v}]=[c\mathbf{v}]$ for scalar $c$.

These operations are well-defined — independent of the representatives chosen — precisely because $U$ is a subspace.

> The properties of subspaces ensure $\sim$ defines a proper equivalence relation: reflexive ($\mathbf{v}\sim\mathbf{v}$), symmetric ($\mathbf{v}_1\sim\mathbf{v}_2$ implies $\mathbf{v}_2\sim\mathbf{v}_1$), and transitive ($\mathbf{v}_1\sim\mathbf{v}_2$ and $\mathbf{v}_2\sim\mathbf{v}_3$ implies $\mathbf{v}_1\sim\mathbf{v}_3$).

Electrical networks supply physical intuition for quotient spaces.
Consider a circuit with $n$ nodes, where we measure voltage differences between pairs of nodes.
Though each node has its own voltage potential, the physically meaningful measurements are always differences — adding a constant voltage to every node leaves all measurements unchanged.
This observation reveals the fundamental role of quotients in physics.

Let $V=\mathbb{R}^n$ be the vector space of voltage assignments to nodes.
Let $U<V$ be the line of constant assignments $(c,c,\ldots,c)^T$.
The quotient map sending each voltage configuration to its equivalence class under constant shifts,

$$
\Pi_{}:V\to V/U \quad : \quad \mathbf{v} \mapsto [\mathbf{v}]
$$

has kernel exactly $U$, and $V/U$ captures the physically meaningful voltage states, stripped of their artificial dependence on reference potential.

**Example 3.19 (Kernel Quotients).** Let $T:V\rightarrow W$ be a linear transformation.
Two vectors that differ by an element of $\operatorname{ker} T$ are sent to the same output:

$$
T(\mathbf{v_1}) = T(\mathbf{v_2}) \iff \mathbf{v_1}-\mathbf{v_2}\in\operatorname{ker} T
$$

The quotient space $V/\operatorname{ker} T$ naturally represents the "effective" input space of $T$  — it identifies inputs that $T$ cannot distinguish.

> *Foreshadowing:* When we introduce inner products, each equivalence class will have a unique representative orthogonal to the subspace being quotiented.
> For now, we work with the classes themselves.

**Example 3.20 (Geometric quotients).** Consider first quotienting $\mathbb{R}^3$ by a line $L$ through the origin.
Two points $\mathbf{p},\mathbf{q}\in\mathbb{R}^3$ belong to the same equivalence class precisely when their difference $\mathbf{p}-\mathbf{q}$ lies in $L$  — that is, when they differ by some vector parallel to $L$.
Each equivalence class is therefore a *line* parallel to $L$: the class of $\mathbf{p}$ is the translate $\mathbf{p}+L$, and sliding along $L$ never leaves it.
The quotient space $\mathbb{R}^3/L$ is the collection of all such parallel lines.
That family is two-parameter — a line parallel to $L$ is pinned down by where it crosses any plane transverse to $L$  — and indeed $\dim(\mathbb{R}^3/L) = 3-1 = 2$.

Now consider instead quotienting $\mathbb{R}^3$ by a plane $P$ through the origin.
The equivalence classes are now *planes* parallel to $P$, the class of $\mathbf{p}$ being $\mathbf{p}+P$.
Stacked parallel planes form a one-parameter family, so $\mathbb{R}^3/P$ is one-dimensional: $3-2=1$.
A concrete label for a class is the value on it of any linear map $\mathbb{R}^3\to\mathbb{R}$ whose kernel is exactly $P$; two points are equivalent precisely when that map agrees on them.

For $V$ finite-dimensional, the dimension of a quotient space reflects both the dimension of the original space and that of the subspace being quotiented:

$$
\dim(V/U) = \dim V - \dim U
$$

**Example 3.21 (Integration quotients).** Consider the indefinite integral operator (or *antidifferentiation*) $D^{-1}$ acting on continuous functions $C([a,b])$ on an interval.
An antiderivative always exists (thanks to the FTIC) but is well-defined only up to a constant.

> { You did not forget the $+C$ did you?}

To make this a linear transformation of vector spaces requires using a quotient space for the codomain.
Let $U<C([a,b])$ denote the subspace of constant functions on the interval.
Then the quotient $C([a,b])/U$ consists of classes of functions whose differences are constants.
Indefinite integration is now a linear transformation

$$
D^{-1} : C([a,b]) \to C([a,b])/U .
$$

Quotient spaces provide a formal way to identify vectors that behave similarly under certain operations.
When we quotient a domain by the kernel of a transformation, we obtain a space that faithfully represents how the transformation acts, stripped of redundancy.

## 3.7 Coimage & Cokernel

The image and kernel of a linear transformation tell only half the story.
Just as quotient spaces reveal structure by identifying vectors that behave similarly, we can illuminate the action of a linear transformation by examining quotients in both domain and codomain.
This leads to two additional spaces that complete our structural understanding.

**Definition 3.22 (Coimage).** Given a linear transformation $T:V\rightarrow W$, the **coimage** of $T$ is the quotient space

$$
\operatorname{coim} T = V/\operatorname{ker} T
$$

The coimage packages Example 3.19 into a named space.
The projection $\Pi_{}:V\rightarrow \operatorname{coim} T$ sends each vector to its equivalence class modulo $\operatorname{ker} T$.

> *Example:* For a rank-2 matrix $A:\mathbb{R}^4\rightarrow\mathbb{R}^3$, the coimage is 2-dimensional, representing the two independent input directions that affect the output.

Our fourth fundamental space is the most hidden and obscure:

**Definition 3.23 (Cokernel).** Given a linear transformation $T:V\rightarrow W$, the **cokernel** of $T$ is the quotient space

$$
\operatorname{coker} T = W/\operatorname{im} T
$$

The cokernel measures the failure of $T$ to reach all of $W$.
When $T$ is surjective, $\operatorname{coker} T$ is trivial; otherwise, it captures the "invisible" space in the codomain.

> *Foreshadowing:* The dimensions of these four spaces are not independent; their accounting is the Fundamental Theorem.

**Example 3.24 (Differential operators).** For the derivative operator $D:\mathcal{P}_n\rightarrow\mathcal{P}_{n-1}$:

1. The coimage is $n$-dimensional, as only constants vanish under $D$

2. The cokernel is trivial, as every polynomial in $\mathcal{P}_{n-1}$ is a derivative

For integration $\mathrm{I}:C([0,1])\rightarrow\mathbb{R}$:

1. The coimage is one-dimensional: two functions are identified precisely when their integrals agree

2. The cokernel is trivial, as every real number is an integral

## 3.8 The Fundamental Theorem

Four spaces have accumulated around a single transformation.
One theorem binds them.

Consider a linear transformation $T:V\rightarrow W$ between finite-dimensional vector spaces.
From our explorations, we have uncovered four fundamental subspaces:

1. The image $\operatorname{im} T$, capturing all possible output

2. The kernel $\operatorname{ker} T$, containing all inputs that vanish

3. The coimage $\operatorname{coim} T$, encoding independent input directions

4. The cokernel $\operatorname{coker} T$, measuring the failure to surject

> *Example:* For the projection $T:\mathbb{R}^3\rightarrow\mathbb{R}^2$ onto the $xy$-plane, the kernel is the $z$-axis, the image is $\mathbb{R}^2$, the coimage identifies inputs differing only in $z$, and the cokernel is trivial.

These spaces, seemingly distinct, are bound together by a theorem that explains not only how they relate but why they must.
This is the Fundamental Theorem of Linear Algebra:

**Theorem 3.25 (Fundamental Theorem of Linear Algebra).** For any linear transformation $T:V\rightarrow W$ between finite-dimensional vector spaces:

1. The domain and codomain decompose as direct sums:


$$
V \cong \operatorname{ker} T \oplus \operatorname{coim} T
        \quad\text{and}\quad
        W \cong \operatorname{im} T \oplus \operatorname{coker} T
$$

2. The coimage and image are naturally isomorphic: $\operatorname{coim} T \cong \operatorname{im} T$

The second statement is the shorter and the more basic: it is proved in Exercise 11, and needs nothing beyond the definitions of kernel and quotient — in particular, no finiteness of dimension.
The first is of a different character.
Splitting $V$ requires choosing a complement to the kernel, a construction that waits on Chapter 4; and the $\oplus$ there pairs a subspace with a quotient rather than two subspaces of one space.
The corollary below is not hostage to that deferral: its two identities are the dimension count for a quotient together with the second statement above.

*[Figure omitted]*

> *"Four Mighty Ones are in every Man; a Perfect Unity"*

When translated to dimensions, the Fundamental Theorem is sometimes called the *Rank-Nullity Theorem*:

**Corollary 3.26 (Rank-Nullity).** For a linear transformation between finite-dimensional vector spaces, the dimensions balance in complementary pairs:


$$
\dim V = \dim(\operatorname{ker} T) + \dim(\operatorname{coim} T)
$$



$$
\dim W = \dim(\operatorname{im} T) + \dim(\operatorname{coker} T)
$$

Furthermore, the rank connects domain and codomain:


$$
\dim(\operatorname{coim} T) = \operatorname{rank}(T) = \dim(\operatorname{im} T)
$$

Otherwise said:


$$
\dim V = \operatorname{null}(T) + \operatorname{rank}(T)
$$

**Example 3.27 (Matrix rank).** When $T$ is represented by a matrix $A$, these relationships explain why:

1. The nullity $\operatorname{null}(A)$ plus the rank $\operatorname{rank}(A)$ equals the number of columns of $A$

2. The **row rank** ($=\dim\operatorname{row}(A)$) and the **column rank** ($=\dim\operatorname{col}(A)$) are equal to $\operatorname{rank}(A)$

Each entry of $A\mathbf{x}$ pairs a row of $A$ against $\mathbf{x}$, so $\operatorname{ker} A$ is what all the rows annihilate: two inputs fall in the same class of $\operatorname{coim} A$ exactly when no row can separate them.
The image is the column space outright; the coimage is a quotient, and matches $\operatorname{row}(A)$ in dimension alone until Chapter 6 makes the two one space.
These familiar facts from matrix algebra are manifestations of the deeper structural relationships guaranteed by the Fundamental Theorem.

The theorem has immediate practical implications.
When solving a linear system $T\mathbf{x}=\mathbf{b}$, we now understand that:

1. A solution exists if and only if $\mathbf{b}\in\operatorname{im} T$

2. When a solution exists, others differ by elements of $\operatorname{ker} T$

3. Any solution can be uniquely decomposed into parts from $\operatorname{coim} T$ and $\operatorname{ker} T$

4. The obstruction to existence lies in $\operatorname{coker} T$

These four statements answer, at last, the four questions of Example 1.2; the application closing this chapter finishes that story, and shows what the $5\times 4$ matrix was drawn from.

> *Foreshadowing:* When we introduce inner products, these decompositions will provide the foundation for finding optimal approximate solutions when exact solutions do not exist.

*Every linear transformation keeps balanced books: the rank is entered twice, once in each space.*

—

## Color & the Space of Light

Two lamps hang side by side.
One burns a broad, even band of the spectrum; the other spikes at three narrow wavelengths and is dark everywhere between.
A spectrometer reports them as utterly different distributions of energy.
The eye reports them as the same white.
This everyday coincidence — distinct lights that no observer can tell apart — is the signature of a linear transformation carrying an enormous kernel.

Light entering the eye is described by its **spectral power distribution**: a function $s(\lambda)$ assigning to each visible wavelength $\lambda\in[\lambda_0,\lambda_1]$ the radiant power carried there.
Physical spectra are nonnegative, yet they inhabit the vector space $C([\lambda_0,\lambda_1])$ of all continuous functions on the visible band, where addition superposes two lights and scaling dims or brightens one.
This is a vast space, infinite-dimensional, holding far more distinctions than any eye was built to draw.

The retina samples it through three channels.
Three classes of cone cell — long, medium, and short — absorb incoming light, each according to its own sensitivity curve $c_1$, $c_2$, $c_3$.
The signal a cone returns is the total light it absorbs, its spectrum weighted by that sensitivity and summed across all wavelengths:

$$
\Phi(s) = \left(\int_{\lambda_0}^{\lambda_1}\! s(\lambda)c_1(\lambda)\,d\lambda \ ,\
    \int_{\lambda_0}^{\lambda_1}\! s(\lambda)c_2(\lambda)\,d\lambda \ ,\
    \int_{\lambda_0}^{\lambda_1}\! s(\lambda)c_3(\lambda)\,d\lambda \right)^{\!T}
    \in\mathbb{R}^3 .
$$

Each coordinate is a definite integral, and definite integration, as this chapter has already insisted, is linear.
The map $\Phi:C([\lambda_0,\lambda_1])\to\mathbb{R}^3$ is therefore a linear transformation, collapsing the infinite catalogue of possible lights onto a mere three numbers.
Everything a human will ever see of color is $\Phi(s)$.

> *Nota bene:* the kernel here is infinite-dimensional while the coimage is a mere three.
> The dimensional bookkeeping of rank-nullity fails in this infinite setting, yet the isomorphism $\operatorname{coim}\Phi\cong\operatorname{im}\Phi$ of the Fundamental Theorem survives untouched.

Consider what $\Phi$ cannot see.
Its kernel consists of every spectrum whose three cone integrals all vanish — light assembled from real wavelengths that nonetheless registers as pure darkness.
Such a spectrum must take negative values somewhere, and so is no physical light itself; it is the **difference** of two physical lights the eye deems identical.
These invisible differences carry the old name **metameric black**, and two spectra differing by one are called **metamers**.

**Example 3.28 (Metamers).** The two lamps of the opening differ by a metameric black: their spectra are unequal as functions, yet subtracting one from the other yields a spectrum in $\operatorname{ker}\Phi$.
A ripe tomato viewed under noon sunlight and under fluorescent tubes sends the eye two genuinely different spectra, and may match the very same swatch of printed ink under a third.
Metamerism is not a rare accident; it is the working principle of every screen, print, and dye in existence.

What, then, is color?
Two lights look alike precisely when they differ by a metameric black — that is, when they occupy the same coset of $\operatorname{ker}\Phi$.
Perceived color is thus not a spectrum but an equivalence class of spectra, an element of the coimage

$$
\operatorname{coim}\Phi = C([\lambda_0,\lambda_1])\,/\,\operatorname{ker}\Phi .
$$

The Fundamental Theorem (3.25) identifies this quotient with the image: $\operatorname{coim}\Phi\cong\operatorname{im}\Phi=\mathbb{R}^3$.
Three numbers name a color completely — not because light is three-dimensional, for it is boundlessly richer, but because the *quotient* is.

**Example 3.29 (Three Primaries).** A display cannot reproduce a spectrum.
Its pixels emit only weighted combinations of three fixed primary lights $p_1$, $p_2$, $p_3$ — red, green, blue — so every color it can show is $\Phi(a_1p_1+a_2p_2+a_3p_3)$ for nonnegative weights $a_i$.
To reproduce a target color $\mathbf{v}\in\mathbb{R}^3$ is to solve

$$
a_1\Phi(p_1) + a_2\Phi(p_2) + a_3\Phi(p_3) = \mathbf{v} ,
$$

matching not the original light but its coset.
Because the coimage is three-dimensional, three primaries whose images are independent reach every color in their span.
The screen and the sunset it depicts agree on color while sharing not a single wavelength — the same class, met through different representatives.

> *BONUS!* A camera integrates light against *its* own three curves $d_1$, $d_2$, $d_3$, defining a second linear map $\Psi:C([\lambda_0,\lambda_1])\to\mathbb{R}^3$ with its own kernel.
> Two lights the eye calls identical can differ to the camera, and conversely, unless $\operatorname{ker}\Psi=\operatorname{ker}\Phi$. Equivalently, unless each $d_i$ is a linear combination of the cone curves.
> This is the **Luther condition**; its violation is why a photograph sometimes betrays a color the eye had accepted.

That color mixing obeys the laws of a linear map was discovered before the vector space had a name to lend it.
Hermann Grassmann, whose *Ausdehnungslehre* of 1844 first set down the algebra of vector spaces, wrote in 1853 the laws of color mixing: that a match survives scaling, and that matches may be added.
These are exactly the additivity and homogeneity with which Section 3.2 opened — the definition of linearity, tested not on paper but in the eye.
The abstract structure of this chapter appeared, in one of its earliest forms, as a fact about light.

The retina discards almost everything, an infinite kernel of distinctions no human will ever draw, and keeps three numbers.
*Color is not a property of light, but of the quotient.*

—

## Dimensional Analysis & the Drag on a Sphere

A sphere of diameter $d$ moves through a fluid at speed $U$.
What drag force $F$ does it feel?
The force can depend on the size $d$, the speed $U$, and two properties of the fluid: its density $\rho$ and its viscosity $\mu$.
Five quantities in all, bound together by unwritten physical law.
Before any experiment, and without solving a single equation of motion, linear algebra fixes the *shape* that law must take.

The key is to read each quantity not by its magnitude but by its **dimensions** — its expression in mass $M$, length $L$, and time $T$:

$$
\begin{array}{c|ccccc}
      & F & U & d & \rho & \mu \\
\hline
M     & 1 & 0 & 0 & 1 & 1 \\
L     & 1 & 1 & 1 & -3 & -1 \\
T     & -2 & -1 & 0 & 0 & -1
\end{array}
$$

Under the dictionary that turns multiplication into addition — logarithms — these dimensions form a vector space, and each quantity is named by its column of exponents in $\mathbb{R}^3$.
Multiplying two quantities adds their vectors; raising one to a power scales its vector.

Gather the five columns into the **dimension matrix** $D$, a $3\times 5$ array.
A product $F^{x_1}U^{x_2}d^{x_3}\rho^{x_4}\mu^{x_5}$ is **dimensionless** — a pure number, the same in every system of units — exactly when its total exponent vector vanishes:
$D\mathbf{x} = \mathbf{0}.$ The dimensionless combinations are precisely $\operatorname{ker} D$.

Here the abstract machinery of this chapter returns a concrete dividend.
The number of independent dimensionless groups is $\dim\operatorname{ker} D=\operatorname{null} D$, and rank-nullity (3.26) counts it without labor:

$$
\operatorname{null} D = 5 - \operatorname{rank} D = 5 - 3 = 2 .
$$

> *Nota bene:* $\operatorname{rank} D=3$ because mass, length, and time each genuinely appear among the variables — the three rows are linearly independent.
> Were two dimensions to march in lockstep, the rank would drop and a group would be gained.

Two numbers, and no more, govern the drag.
This is the {Buckingham $\pi$ theorem}: a law relating $n$ physical quantities across dimensions reduces to a law among $n-\operatorname{rank} D$ dimensionless groups.
The theorem is nothing other than rank-nullity, read on the dimension matrix.

A basis for the kernel is easy to name.
One vector is the **Reynolds number**

$$
\mathrm{Re} = \frac{\rho U d}{\mu} ,
$$

the ratio of inertial to viscous effects; the other is a dimensionless drag,

$$
\Pi = \frac{F}{\rho U^2 d^2} .
$$

Every dimensionless group is a product of powers of these two.
The unknown drag law must therefore be expressible through them alone: $\Pi = \varphi(\mathrm{Re})$ for a single function $\varphi$ of one variable.
Five quantities have collapsed onto one curve.

That curve is the same for a marble sinking in honey and a balloon rising in a gale.
In the creeping-flow limit $\mathrm{Re}\to 0$ it is known exactly, $\Pi = 3\pi/\mathrm{Re}$, which is Stokes' law $F = 3\pi\mu U d$; at large $\mathrm{Re}$ it levels off, the drag settling into proportionality with $\rho U^2 d^2$.
Because $\varphi$ depends on $\mathrm{Re}$ alone, an engineer need not test at full scale: a small model, run in a fluid and at a speed chosen so that its Reynolds number matches the real one, sits at the same point of the curve and so reports the true drag.

What dimensional analysis cannot supply is the function $\varphi$ itself.
The kernel is found by counting; the curve within it is won only by experiment or by solving the flow.
Rank-nullity says how many numbers matter, and which combinations they are — no small thing, when it turns a five-variable fog into a single graph.

—

## Graph Topology & Network Structure

When a city's power grid fails, engineers must quickly identify which neighborhoods remain connected and where backup pathways exist.
Similar questions arise across networks: Can a signal reach all neurons in a circuit?
Will information flow reliably through a social network?
Does a computer network contain redundant paths to route around failures?
These practical concerns about connectivity and resilience share one mathematical structure, and a single matrix carries it.

Consider a finite directed graph $G=(V,E)$ with vertex set $V=\{v_1,\ldots,v_n\}$ and edge set $E=\{e_1,\ldots,e_m\}$.
Each edge $e$ has a specified orientation, with starting vertex $e^-$ and ending vertex $e^+$.
From this discrete structure we construct two fundamental vector spaces:

- $C_0(G)$: the vector space with basis elements the vertices $V$

- $C_1(G)$: the vector space with basis elements the oriented edges $E$

These spaces have dimensions $n$ and $m$ respectively.
Though their elements can be interpreted as assignments of numbers to vertices or edges (like voltages or currents), viewing them as abstract vector spaces clarifies their fundamental structure.

The relationship between these spaces emerges through a natural transformation called the **boundary operator** $\partial:C_1(G)\to C_0(G)$.
On basis elements, this operator acts by:

$$
\partial(e) = e^+ - e^-
$$

extending linearly to all of $C_1(G)$.
Though defined using edge orientations, its fundamental properties — captured through kernel and cokernel — prove independent of these choices.

**Example 3.30 (Ladder Network).** Consider a "ladder" network with eight vertices and ten edges arranged and labeled as in the figure, right.

*[Margin figure omitted]*

Its boundary operator is an $8\times 10$ matrix, one column per edge, each column carrying a single $+1$ and a single $-1$ and nothing else.
The network contains many cycles, yet there are but three that can be chosen to be *independent*.
One simple representative follows the top square $e_2+e_4-e_3-e_1$, where the minus signs indicate traversing an edge opposite its orientation.
This, together with the other two obvious squares, forms a basis for $\operatorname{ker}\partial$.

Such **cycles** — elements of $\operatorname{ker}(\partial)$ — represent closed paths through the network where the "flow" in equals flow out at each vertex.
Not every element of $\operatorname{ker}(\partial)$ corresponds to a simple cycle; some represent combinations of cycles.
The dimension of this kernel, denoted $\beta_1$, counts the number of **independent** cycles — those that cannot be expressed as combinations of smaller cycles.
A power grid with larger $\beta_1$ offers more backup paths; a neural circuit with independent cycles can sustain more complex recurrent patterns.

> *Notation:* The symbol $\beta$ stands for *Betti number*, a fundamental object of study in algebraic topology.

The cokernel of $\partial$ reveals complementary structure through its quotient space $C_0(G)/\operatorname{im}(\partial)$.
This space effectively identifies vertices that can be reached from each other through network paths.
Its dimension $\beta_0$ counts the network's connected components.
A power grid with $\beta_0 > 1$ has disconnected regions requiring immediate attention; a neural network with multiple components represents independent processing modules.

These numbers are bound by a single relation:

$$
\beta_1 - \beta_0 = m - n
$$

That is, the number of independent cycles minus the number of connected components equals the excess between edge count and vertex count.
This equation — simultaneously the rank-nullity theorem for $\partial$ and a combinatorial invariant of the graph — expresses a fundamental balance between cycles and components.
Adding edges tends to create cycles ($\beta_1$ increases) while joining components ($\beta_0$ decreases).

The reader has carried an example of this balance since the opening pages.
The $5\times 4$ matrix of Example 1.2 is the boundary operator of a small network: five vertices and four oriented edges, with edges $e_1$, $e_2$, $e_3$ running $1\to 2$, $2\to 3$, and $1\to 3$ among the first three vertices, and a lone edge $e_4$ from vertex $4$ to vertex $5$.

> *FIGURE:* [Draw the graph: a triangle carrying $e_1:1\to2$, $e_2:2\to3$ and the chord $e_3:1\to3$, with the disjoint edge $e_4:4\to5$ set off to one side. Two components, one cycle.]

Its four questions now answer to their names, in order.
The achievable right-hand sides form $\operatorname{im}\partial$, a subspace of dimension $3$.
The obstructions live in $\operatorname{coker}\partial = C_0(G)/\operatorname{im}\partial$, of dimension $\beta_0 = 2$: one conservation law per connected piece, $b_1+b_2+b_3=0$ for the triangle and $b_4+b_5=0$ for the lone edge — two constraints and not three because the network has two components and not three.
The solution family is a translate of $\operatorname{ker}\partial$, spanned by the single independent cycle $e_1+e_2-e_3$, whence its dimension $\beta_1=1$.
And the single principle binding the counts — glimpsed in Chapter 1 — is rank-nullity itself: $4 = 1+3$ over the edges, $5 = 3+2$ over the vertices.
*The matrix was never hiding numbers; it was hiding a shape.*

—

## Exercises: Chapter 3

1. Let $T,S:\mathbb{R}^2\to\mathbb{R}^2$ be given by $T(x,y) = (2x+y,\,x-y)$ and $S(x,y) = (2x+y,\,4x+2y)$.
For each, find the kernel and the image, and decide whether the map is injective, surjective, both, or neither.
Find the rank, the nullity, and the dimension of the cokernel of each, and verify Corollary 3.26.

2. For $\mathbf{v}\in\mathbb{R}^n$, define $T_{\mathbf{v}}:\mathbb{R}^n\to\mathbb{R}$ by $T_{\mathbf{v}}(\mathbf{x}) = \mathbf{v}\cdot\mathbf{x}$.
Prove that this defines a linear transformation, and find its kernel and image, treating $\mathbf{v}=\mathbf{0}$ separately.
Show that $T_{\mathbf{v}} = T_{\mathbf{w}}$ only if $\mathbf{v}=\mathbf{w}$.

3. Consider the differentiation operator $D:\mathcal{P}_2\to\mathcal{P}_1$ defined by $D(ax^2 + bx + c) = 2ax + b$.
Find *all* linear transformations $S:\mathcal{P}_1\to\mathcal{P}_2$ satisfying $D\circ S = \mathrm{id}_{\mathcal{P}_1}$.
Show that none of them satisfies $S\circ D = \mathrm{id}_{\mathcal{P}_2}$.

4. Define $T:\mathcal{P}_4\to\mathbb{R}^2$ by $T(p) = \big(p(1),\,p(-1)\big)^T$.
Show that $T$ is linear and surjective, and find $\operatorname{ker} T$ and its dimension.
Then name all four of the spaces of Theorem 3.25 for this $T$.

5. Let $T_A:\mathbb{R}^4\to\mathbb{R}^5$ be $T_A(\mathbf{x}) = A\mathbf{x}$, where

    > *Caveat:* This is not the matrix of Example 1.2, and it is no network's boundary operator; the lesson is the same, so the lesson is not about networks.
    > Chapter 1 could ask when $A\mathbf{x}=\mathbf{b}$ is solvable and Chapter 2 could name the obstructions.
    > Only here do they become a space, with coordinates.

$$
A = \begin{bmatrix}
    1 & 1 & 0 & 0 \\ 1 & 0 & -1 & 0 \\ 0 & 0 & 1 & 1 \\ 1 & 1 & 1 & 1 \\ 1 & 0 & 0 & 1
    \end{bmatrix} .
$$

Find $\operatorname{rank} T_A$ and $\dim\operatorname{coker} T_A$, and show that the classes of $\mathbf{e}_4$ and $\mathbf{e}_5$ are a minimal spanning set for $\operatorname{coker} T_A = \mathbb{R}^5/\operatorname{im} T_A$.
Then express $[\mathbf{b}]$ in terms of them, and say what $[\mathbf{b}]=[\mathbf{0}]$ means about solving $A\mathbf{x}=\mathbf{b}$.

6. Let $V=\mathbb{R}^2$, let $\mathbf{a}=(1,1)^T$, and call $\mathbf{u},\mathbf{v}\in V$ equivalent when they differ by a multiple of $\mathbf{a}$.
Sketch the equivalence class of $(2,-1)^T$.
Show that $\varphi(x,y) = x-y$ has kernel $\operatorname{span}(\mathbf{a})$, and use it to write down an explicit isomorphism $V/\operatorname{span}(\mathbf{a})\to\mathbb{R}$.

7. Let $V=\mathbb{R}^{2\times 2}$, and define $T,S:V\to V$ by $T(A) = A^T$ and $S(A) = A-A^T$.
Prove that both are linear, and conclude from $T\circ T=\mathrm{id}_V$ alone that $T$ is an isomorphism.
Find $\operatorname{ker} S$ and $\operatorname{im} S$, and verify Corollary 3.26.

8. Let $T:V\to W$ be linear with $V$ and $W$ finite-dimensional, let $\mathbf{v}_1,\ldots,\mathbf{v}_k$ be linearly independent, and set $U = \operatorname{span}(\mathbf{v}_1,\ldots,\mathbf{v}_k)$.
Apply Corollary 3.26 to the restriction of $T$ to $U$ to prove that $\dim T(U) = \dim U - \dim(U\cap\operatorname{ker} T)$.
Deduce that the list $T(\mathbf{v}_1),\ldots,T(\mathbf{v}_k)$ is linearly independent if and only if $U\cap\operatorname{ker} T=\{\mathbf{0}\}$, and that this is the forward half of Lemma 3.7(1) when $\operatorname{ker} T=\{\mathbf{0}\}$.
Then find a $T$ and an independent pair $\mathbf{v}_1,\mathbf{v}_2$ with $T(\mathbf{v}_1),T(\mathbf{v}_2)$ both nonzero yet dependent.

9. Let $V$ be finite-dimensional and $T:V\to V$ linear.
Prove that $T$ is invertible if and only if $\operatorname{ker} T = \{\mathbf{0}\}$.
Then show that finite-dimensionality is not decoration: on the space of all polynomials, give a linear $T$ that is injective but not surjective, and one that is surjective but not injective.

10. Let $S,T:V\to W$ be linear transformations.
Prove that any two of the three subspaces $\operatorname{ker} S$, $\operatorname{ker} T$, $\operatorname{ker}(S+T)$ have the same intersection, and deduce that $\operatorname{ker} S\cap\operatorname{ker} T<\operatorname{ker}(S+T)$.
Give an example where the containment is strict.

11. Let $T:V\to W$ be a linear transformation.
Prove that the quotient space $V/\operatorname{ker} T$ is isomorphic to $\operatorname{im} T$ by explicitly constructing an isomorphism and verifying it is well-defined.
This is the second statement of Theorem 3.25; where, if anywhere, did you use finite-dimensionality?

12. Let $U<V$ be a subspace, and let $\Pi_{}:V\to V/U$ be the quotient map $\Pi_{}(\mathbf{v}) = [\mathbf{v}]$.
Prove that $\Pi_{}$ is a linear transformation, that it is surjective, and that $\operatorname{ker}\Pi_{} = U$.
Definition 3.12 says that every kernel is a subspace; deduce the converse, that every subspace is a kernel.

13. Let $U<V$, and let $T:V\to W$ be linear with $U<\operatorname{ker} T$.
Prove that there is a unique linear $\overline{T}:V/U\to W$ with $T = \overline{T}\circ\Pi_{}$, where $\Pi_{}$ is the quotient map of Exercise 12.
Show by example that this can fail when $U$ is not contained in $\operatorname{ker} T$.

14. Let $N:\mathbb{R}^2\to\mathbb{R}^2$ be given by the matrix $\begin{bmatrix}0&1\\0&0\end{bmatrix}$.
Show that $\operatorname{ker} N = \operatorname{im} N$, so that these two subspaces neither meet trivially nor together fill $\mathbb{R}^2$.
Reconcile this with the first statement of Theorem 3.25.

15. Let $S,T:V\to W$ be linear with $\operatorname{ker} S = \operatorname{ker} T$.
Prove that there is an isomorphism $\varphi:\operatorname{im} S\to\operatorname{im} T$ satisfying $\varphi(S\mathbf{v}) = T\mathbf{v}$ for every $\mathbf{v}\in V$.
Then show that the converse fails: find $S,T:\mathbb{R}^2\to\mathbb{R}^2$ with $\operatorname{im} S = \operatorname{im} T$ as the same subspace, but $\operatorname{ker} S\neq\operatorname{ker} T$.

16. Take $V=\mathbb{R}$ and let $U=\mathbb{Z}$, the integers, which is not a subspace.
Declaring $x\sim y$ when $x-y\in U$ still gives an equivalence relation; attempt the operations of Definition 3.18 on its classes.
Show that $[x]+[y]=[x+y]$ is well-defined but that $c[x]=[cx]$ is not, and name the property of $U$ that each operation consumes.

17. A rod occupies $[0,L]$ with linear density $f\in C([0,L])$, so that its mass is $M(f)=\int_0^L f(x)\,dx$ and its center of mass is $X(f) = M(f)^{-1}\int_0^L x f(x)\,dx$.
Prove that $M$ is a linear transformation and that it is surjective, and exhibit a nonzero $f\in\operatorname{ker} M$.
Then show that $X$ is not a linear transformation — indeed, that it is not a function on $C([0,L])$ at all.

18. A reactor holds the five species $\mathrm{CO}$, $\mathrm{O}_2$, $\mathrm{CO}_2$, $\mathrm{H}_2$, $\mathrm{H}_2\mathrm{O}$, and a vector in $\mathbb{R}^5$ records the change in the amount of each.
Running the reactions $2\,\mathrm{CO}+\mathrm{O}_2\to 2\,\mathrm{CO}_2$, $\ 2\,\mathrm{H}_2+\mathrm{O}_2\to 2\,\mathrm{H}_2\mathrm{O}$, and $\mathrm{CO}+\mathrm{H}_2\mathrm{O}\to\mathrm{CO}_2+\mathrm{H}_2$ to extents $\mathbf{x}\in\mathbb{R}^3$ changes the composition by $S\mathbf{x}$, where

$$
S = \begin{bmatrix} -2 & 0 & -1 \\ -1 & -1 & 0 \\ 2 & 0 & 1 \\ 0 & -2 & 1 \\ 0 & 2 & -1 \end{bmatrix} .
$$

Find $\operatorname{ker} S$ and $\dim\operatorname{coker} S$, and say what each means for the chemistry.
Exhibit $\dim\operatorname{coker} S$ independent linear conditions holding for every achievable composition change, and name what each one conserves.

19. *(Challenge.)* Let $S,T:V\to W$ be linear, of finite rank.
Prove that $\operatorname{im}(S+T)<\operatorname{im} S+\operatorname{im} T$, and deduce that $\operatorname{rank}(S+T)\leq\operatorname{rank} S+\operatorname{rank} T$.
Taking $S(t)=(t,0)^T$ and $T(t)=(0,t)^T$ on $\mathbb{R}$, check that $\operatorname{im} S\cap\operatorname{im} T=\{\mathbf{0}\}$ does not by itself force equality; then prove, using Exercise 19, that equality holds if and only if $\operatorname{im} S\cap\operatorname{im} T=\{\mathbf{0}\}$ *and* $\operatorname{im}(S+T)=\operatorname{im} S+\operatorname{im} T$.

20. *(Challenge.)* Let $U<W<V$ with $V$ finite-dimensional.
Show that $W/U$ is a subspace of $V/U$, and that $[\mathbf{v}]_U\mapsto[\mathbf{v}]_W$ is a well-defined surjective linear map $V/U\to V/W$ whose kernel is $W/U$.
Conclude from Exercise 11 that $(V/U)/(W/U)\cong V/W$, and check that the dimensions agree.

---


---

> **Part marker.** URIZEN — reason (image)


# Chapter 4. Bases & Coordinates

*"fixing them firm on their base, the bellows began to blow"*

**The passage from abstract to concrete** is as important as its inverse.
Having dwelt in the realm of abstract vector spaces and transformations, we now seek to make these concepts precise and measurable through coordinates and computations.

The concepts are familiar from geometric intuition: we routinely describe points in space using coordinates relative to chosen axes.
These coordinates transform an abstract point into a concrete list of numbers that we can manipulate.
Yet this simple idea — that we can systematically assign numbers to abstract vectors — contains surprising depth.
The choice of coordinate system, seemingly arbitrary, can dramatically affect how easily we solve problems or understand structures.

This tension between intrinsic properties and their coordinate representations lies at the heart of linear algebra.
A vector space exists independent of any particular way we choose to measure it, yet we cannot compute without making such choices.
A linear transformation acts geometrically, yet we encode it as a matrix only after choosing bases for its domain and codomain.
These choices — of bases and the coordinates they induce — form the bridge between abstract understanding and concrete computation.

Our task is to build this bridge carefully, ensuring it carries both theoretical insight and practical utility across the gap.
We begin with the notion of a basis — a set of vectors that both spans a space and does so efficiently.
These bases provide coordinate systems, allowing us to translate abstract vectors into concrete lists of numbers.
The interplay between different bases leads us to change of coordinates formulas, revealing how geometric objects appear from different perspectives.

## 4.1 Bases & Spanning Sets

> *Example:* Even for something as simple as $\mathbb{R}^2$, there are infinitely many choices of basis.
> The standard basis $\{\hat{\imath}, \hat{\jmath}\}$ is merely one convenient choice among many.

From Chapter 2, recall that a spanning set for a vector space may contain redundant vectors, while a linearly independent set may fail to reach all vectors in the space.
The notion of a basis synthesizes these concepts, providing a set of vectors that spans efficiently — without redundancy and without gaps.

**Definition 4.1 (Basis).** A **basis** for a vector space $V$ is a set $\mathcal{B}$ of vectors that spans $V$ yet is linearly independent.

The economy of this definition belies its power.
A basis provides a minimal spanning set — minimal in the sense that removing any vector from the basis leaves a set that no longer spans $V$.
Equivalently, it provides a maximal linearly independent set — maximal in that adding any vector creates linear dependence.

**Example 4.2 (Polynomial bases).** The space $\mathcal{P}_2$ of quadratic polynomials admits several natural choices of basis, each providing different advantages:

> *BONUS!* The monomial basis reveals the degree structure; the Lagrange basis simplifies interpolation by constructing polynomials that equal 1 at one interpolation point and 0 at the others; the Newton basis facilitates recursive computation through its nested structure.

1. The monomial basis $\{1, x, x^2\}$

2. The Lagrange basis for interpolation points $\{-1,0,1\}$:


$$
\left\{\frac{x(x+1)}{2}, -x^2+1, \frac{x(x-1)}{2}\right\}
$$

3. The Newton basis with nodes $d$ and $e$ $(d\neq e)$:


$$
\{1, (x-d), (x-d)(x-e)\}
$$

To illustrate, consider the polynomial $p(x) = x^2 + x + 1$.
In the monomial basis, it is already in standard form:

$$
p(x) = 1\cdot 1 + 1\cdot x + 1\cdot x^2
$$

In the Lagrange basis at points $\{-1,0,1\}$, writing out the expansion:

$$
p(x) = 3\cdot\frac{x(x+1)}{2} + 1\cdot(-x^2+1) + 1\cdot\frac{x(x-1)}{2} = x^2 + x + 1
$$

The coefficients are simply the values $p(1)$, $p(0)$, $p(-1)$  — which is the whole point of a Lagrange basis.
This demonstrates how different bases can represent the same polynomial in ways that are advantageous for different computational purposes.

> *Foreshadowing:* Different bases reveal different aspects of a space's structure.
> In Chapter 7, we shall discover bases that illuminate the action of linear differential equations.

Every finite-dimensional vector space has a basis, and cheaply: it has a finite spanning set, from which vectors may be discarded until none can be, and by Lemma 2.20 such a minimal spanning set is linearly independent.
More is true — any independent set can be grown into one:

**Theorem 4.3 (Basis Extension).** Let $V$ be a finite-dimensional vector space and $S \subseteq V$ be a linearly independent set.
Then $S$ can be extended to a basis of $V$ by adding finitely many vectors.
Moreover, if $\dim V = n$ and $|S| = k \leq n$, then exactly $n-k$ vectors need to be added.

> The theorem generalizes to infinite-dimensional spaces using Zorn's Lemma, though the extension process becomes non-constructive.

*Proof.* Suppose $S$ is independent but does not span $V$.
Then some $\mathbf{v}\in V$ lies outside $\operatorname{span}(S)$, and by Exercise 13 of Chapter 2 the enlarged set $S\cup\{\mathbf{v}\}$ is again independent.
Repeat.
By Corollary 2.22 no independent set in $V$ outnumbers a spanning set, so the process halts — and it can halt only at a spanning set, which is then a basis.
By Lemma 2.21 every basis of $V$ has the same size $n$, so exactly $n-k$ were added. ∎

> *Caveat:* The process of extending to a basis or extracting one from a spanning set is not unique — different choices yield different bases.

This constructive proof reveals a fundamental principle: we can build bases either by extension (adding vectors until we span) or by reduction (removing vectors until independence).
Both processes terminate because of finite-dimensionality — a crucial hypothesis that fails in infinite-dimensional spaces.

**Example 4.4 (Matrix bases).** The space $\mathbb{R}^{2\times 2}$ of $2\times 2$ matrices has the standard basis

$$
E_{11}=\begin{bmatrix}1&0\\0&0\end{bmatrix},\
E_{12}=\begin{bmatrix}0&1\\0&0\end{bmatrix},\
E_{21}=\begin{bmatrix}0&0\\1&0\end{bmatrix},\
E_{22}=\begin{bmatrix}0&0\\0&1\end{bmatrix}
$$

This basis makes the coordinate structure transparent but obscures other properties.
For example, the basis

$$
\begin{bmatrix}1&0\\0&1\end{bmatrix},\
\begin{bmatrix}0&1\\1&0\end{bmatrix},\
\begin{bmatrix}0&-1\\1&0\end{bmatrix},\
\begin{bmatrix}1&0\\0&-1\end{bmatrix}
$$

better reveals the decomposition into symmetric and skew-symmetric parts.

A key property of bases is that they all have the same size, thanks to Lemma 2.21:

**Corollary 4.5.** Any two bases of a vector space have the same number of vectors.

This reveals dimension as an intrinsic property of the space, independent of choice of basis.

**Example 4.6 (Dimension counting).** The following dimensions arise naturally:

1. $\dim(\mathbb{R}^n) = n$

2. $\dim(\mathcal{P}_n) = n+1$

3. $\dim(\mathbb{R}^{m\times n}) = mn$

4. $\dim(\operatorname{sym}_n) = \frac{1}{2}n(n+1)$

> Recall, $\mathcal{P}_n$ is the space of polynomials of degree $\leq n$ and $\operatorname{sym}_n$ denotes the space of symmetric $n$-by-$n$ matrices.

Each counts the minimal number of parameters needed to specify an element of the space.

Bases provide our first systematic way to measure vector spaces.
The choice of basis — which is always somewhat arbitrary — trades the intrinsic nature of the space for concrete computability.
This tension between coordinate-free properties and coordinate-dependent calculations will be a recurring theme as we develop the machinery of linear algebra.

## 4.2 Coordinates & Components

The existence of a basis provides more than a spanning set for a vector space — it enables a systematic translation of abstract vectors into concrete lists of numbers.
This translation is the keystone of computational linear algebra.
It bridges the gap between geometric intuition and algorithmic manipulation.

The crucial observation is that any vector in a space can be written uniquely as a linear combination of basis vectors.
Given a basis $\{\mathbf{b}_1,\ldots,\mathbf{b}_n\}$ for a vector space $V$, each vector $\mathbf{v}\in V$ has a unique expression:

$$
\mathbf{v} = c_1\mathbf{b}_1 + c_2\mathbf{b}_2 + \cdots + c_n\mathbf{b}_n
$$

The scalars $c_1,\ldots,c_n$ are called the **coordinates** of $\mathbf{v}$ relative to this basis.
The ordered list of these coordinates, written as a column vector

> *Caveat:* The notation $[\mathbf{v}]_{\mathcal{B}}$ emphasizes that coordinates depend on choice of basis.
> A vector has different coordinates in different bases, though the vector itself remains unchanged.

$$
[\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{pmatrix}
$$

is the **coordinate vector** of $\mathbf{v}$ with respect to the basis $\mathcal{B}=\{\mathbf{b}_1,\ldots,\mathbf{b}_n\}$.
A basis was defined as a set, but a column of coordinates needs an order; from here on a basis is understood to carry a fixed ordering of its vectors.

**Example 4.7 (Polynomial coordinates).** Consider the polynomial $p(x)=6+2x-3x^2$ in $\mathcal{P}_2$.
In the monomial basis $\mathcal{M}=\{1,x,x^2\}$, its coordinate vector is

$$
[p]_{\mathcal{M}} = \begin{pmatrix} 6 \\ 2 \\ -3 \end{pmatrix}
$$

In the Newton basis $\mathcal{N}=\{1,\ x-1,\ (x-1)(x+1)\}$ with nodes $1$ and $-1$, the same polynomial has different coordinates:

$$
[p]_{\mathcal{N}} = \begin{pmatrix} 5 \\ 2 \\ -3 \end{pmatrix}
$$

The polynomial remains unchanged; only its description varies.

The passage from vector to coordinates preserves the vector space operations.
If $\mathbf{v}$ and $\mathbf{w}$ have coordinate vectors $[\mathbf{v}]_{\mathcal{B}}$ and $[\mathbf{w}]_{\mathcal{B}}$ respectively, along with scalar $c$, then:

1. $[\mathbf{v}+\mathbf{w}]_{\mathcal{B}} = [\mathbf{v}]_{\mathcal{B}} + [\mathbf{w}]_{\mathcal{B}}$

2. $[c\mathbf{v}]_{\mathcal{B}} = c[\mathbf{v}]_{\mathcal{B}}$

This preservation of structure means that coordinate vectors themselves form a vector space isomorphic to the original space.

> *Foreshadowing:* The preservation of vector space operations under the passage to coordinates explains why matrix multiplication encodes composition of linear transformations.

The uniqueness of coordinate representations — guaranteed by the linear independence of basis vectors — allows us to test equality through coordinates.
Two vectors are equal if and only if their coordinate vectors relative to any basis are equal.
This reduces abstract vector equality to numerical comparison.

> This reduction of geometric or algebraic properties to numerical tests exemplifies how coordinates enable computation.
> Everything then turns on choosing coordinates that make the desired computations simple.

We have thus established a dictionary between abstract vectors and concrete lists of numbers.
This dictionary depends critically on our choice of basis — a choice we are free to make and change as computational needs dictate.

## 4.3 Change of Basis

The right coordinate system can transform a complex problem into a simple one.
An oscillating spring-mass system, described by coupled equations in Cartesian coordinates, reduces to independent motions when viewed in its natural modes.
A robotic arm's motion, intricate to specify in workspace coordinates, might follow elementary paths in joint angles.
The acceleration of a particle, complicated in rectangular coordinates, could simplify dramatically in polar coordinates.
These transformations of perspective — these changes of basis — are not mere mathematical conveniences but essential tools for understanding and controlling physical systems.

Consider a vector space $V$ with two different bases, $\mathcal{B}$ and $\mathcal{B}'$.
A vector $\mathbf{v}\in V$ exists independently of how we describe it, just as climbing a mountain is equally difficult whether we measure its height in meters or feet.
Yet to work with a vector — to compute with it, to transform it, to understand its relationship to other vectors — we must choose coordinates.
The same vector has different coordinate representations in different bases:

$$
\mathbf{v} = \sum_{i=1}^n c_i\mathbf{b}_i = \sum_{i=1}^n c'_i\mathbf{b}'_i
$$

where $[\mathbf{v}]_{\mathcal{B}} = (c_1,\ldots,c_n)^T$ and $[\mathbf{v}]_{\mathcal{B}'} = (c'_1,\ldots,c'_n)^T$ are its coordinate vectors in bases $\mathcal{B}$ and $\mathcal{B}'$ respectively.

**Example 4.8 (Electric Field Components).** The electric field $\mathbf{E}$ from a point charge can be measured in different coordinate systems.
Near a charge $q$ at the origin, we might express $\mathbf{E}$ in Cartesian coordinates:

$$
\mathbf{E} = E_x\hat{\imath} + E_y\hat{\jmath} + E_z\hat{k}
$$

or in spherical coordinates:

$$
\mathbf{E} = E_\rho\hat{\mathbf{e}}_\rho + E_\theta\hat{\mathbf{e}}_\theta + E_\phi\hat{\mathbf{e}}_\phi
$$

> This orthogonal transformation represents a change of basis that proves especially useful in analyzing radially symmetric fields, where the spherical components often reveal patterns obscured in Cartesian coordinates.
> The transformation matrix follows the mathematicians' convention where $\theta$ represents the azimuthal angle in the $xy$-plane from the $x$-axis (0 to $2\pi$) and $\phi$ denotes the polar angle from the $z$-axis (0 to $\pi$).

The transformation between these descriptions at any point $(x,y,z)$ with spherical coordinates $(\rho,\theta,\phi)$ is given by:

$$
\begin{pmatrix}
    E_\rho \\ E_\theta \\ E_\phi
    \end{pmatrix}
    =
    \begin{bmatrix}
    \sin\phi\cos\theta & \sin\phi\sin\theta & \cos\phi \\
    -\sin\theta & \cos\theta & 0 \\
    \cos\phi\cos\theta & \cos\phi\sin\theta & -\sin\phi
    \end{bmatrix}
    \begin{pmatrix}
    E_x \\ E_y \\ E_z
    \end{pmatrix}
$$

Note that this matrix varies from point to point: the spherical frame is not one basis for one vector space but a field of bases.

The key to understanding basis changes lies in expressing the new basis vectors in terms of the old, using a matrix to do so.

**Definition 4.9 (Change of Basis Matrix).** Let $\mathcal{B}=\{\mathbf{b}_1,\ldots,\mathbf{b}_n\}$ and $\mathcal{B}'=\{\mathbf{b}'_1,\ldots,\mathbf{b}'_n\}$ be bases for a vector space $V$.
The **change of basis matrix** from $\mathcal{B}'$ to $\mathcal{B}$, written $P_{\mathcal{B}\leftarrow\mathcal{B}'}$, is the matrix $P=[p_{ij}]$ whose entries are determined by the unique representations:

$$
P = [p_{ij}] \quad : \quad
   \mathbf{b}'_j = \sum_{i=1}^n p_{ij}\mathbf{b}_i \tag{4.1}
$$

The $j$th column of $P$ contains the $\mathcal{B}$-coordinates of $\mathbf{b}'_j$, encoding how to express each new basis vector in terms of the old basis; since those columns are a basis written in coordinates, $P$ is invertible.

The arrow is the whole of the notation.
One reads $P_{\mathcal{B}\leftarrow\mathcal{B}'}$ from right to left, as one reads a function: it accepts $\mathcal{B}'$ and returns $\mathcal{B}$, which is the direction it actually converts.
The full name is a burden to carry through a computation, so whenever the two bases are fixed and no confusion threatens we abbreviate it to $P$  — with the understanding that the subscripts are still there, and that any dispute about direction is settled by restoring them.

> *Think:* the inner labels cancel, exactly as units cancel in a physical computation,
>
>

$$
>
> P_{\mathcal{A}\leftarrow\mathcal{B}}\,P_{\mathcal{B}\leftarrow\mathcal{C}}
> = P_{\mathcal{A}\leftarrow\mathcal{C}} ,
>
>
$$

>
> and a product whose inner labels disagree is not a change of basis at all.
> The notation reports the error before the arithmetic does.

**Example 4.10 (Signal Processing).** In audio processing, a sound signal naturally begins in the time domain — amplitudes measured at discrete time points.
For analysis and filtering, we often transform to the frequency domain using the Discrete Fourier Transform (DFT).
This is precisely a change of basis, where our new basis vectors are complex exponentials:

$$
\mathbf{b}'_k = \frac{1}{\sqrt{n}}\begin{pmatrix}
    1 \\ e^{-2\pi i k/n} \\ e^{-4\pi i k/n} \\ \vdots \\ e^{-2\pi i k(n-1)/n}
    \end{pmatrix}
$$

> *Foreshadowing:* the change of basis matrix $P$ in this case is **unitary** (complex analogues of orthogonal matrices), reflecting the conservation of energy between time and frequency domains.

Given the change of basis matrix $P$, we can convert coordinates systematically:

$$
[\mathbf{v}]_{\mathcal{B}} = P[\mathbf{v}]_{\mathcal{B}'}
$$

This is what the name records: $P$ converts coordinates in $\mathcal{B}'$ into coordinates in $\mathcal{B}$.
To go the other way, we solve:

$$
[\mathbf{v}]_{\mathcal{B}'} = P^{-1}[\mathbf{v}]_{\mathcal{B}}
$$

Two claims about $P$ have now been made in passing, and they are one claim; it deserves the standing of a rule.
The columns of $P$ are the vectors of the new basis $\mathcal{B}'$ written in the coordinates of the old basis $\mathcal{B}$; therefore $P$ carries new coordinates to old, and $P^{-1}$ carries old to new.
These agree because they are one act and not two: building $\mathbf{b}'_j$ out of the old basis and rewriting a coordinate vector are both the operation of reading a $\mathcal{B}'$-description in $\mathcal{B}$-terms, and a matrix is nothing more than what it does to the columns of the identity.
The consequence is the one needed whenever a conjugation appears.

> "`latex
> tikzcd
> R^n [r, "B"] [d, "P"'] & R^n [d, "P"]

> R^n [r, "A"'] & R^n
> tikzcd
> "`
>
>
>
> The top row carries $\mathcal{B}'$-coordinates and the bottom row $\mathcal{B}$-coordinates; the square commutes precisely when $B=P^{-1}AP$.

To apply $A$ to a vector presented in new coordinates, one converts to old coordinates with $P$, applies $A$ there, and converts back with $P^{-1}$; read right to left, as one reads a composition of functions, that is $P^{-1}AP$.
*The columns name the new basis in old terms, and the matrix does the same to every vector.*

**Example 4.11 (Principal Stress).** In analyzing the mechanics of a thin planar material, the **stress tensor** recording stress and strain at a point is a symmetric $2\times 2$ matrix $\boldsymbol{\sigma}\in\operatorname{sym}_2$ relative to chosen coordinate axes:

$$
\boldsymbol{\sigma} = \begin{bmatrix}
    \sigma_{xx} & \tau_{xy} \\
    \tau_{xy} & \sigma_{yy}
    \end{bmatrix}
$$

There always exists a convenient basis — the principal stress directions — in which the stress tensor is diagonal:

$$
\boldsymbol{\sigma}' = \begin{bmatrix}
    \sigma_1 & 0 \\
    0 & \sigma_2
    \end{bmatrix}
$$

Finding this basis, achieved through eigendecomposition (Chapter 7), is crucial for predicting material failure.
The change of basis matrix $P$ here consists of unit vectors along the principal stress directions.

Changing perspective neither creates nor destroys information: we may work in whatever coordinate system best suits the problem at hand, confident that the results translate back to any other.

The true significance of basis changes emerges when we consider linear transformations, whose matrix representations depend critically on our choice of coordinates.
This relationship — between bases, transformations, and their matrix representations — leads us to the fundamental notion of similarity.

## 4.4 Matrix Representations

A geometric transformation exists independently of how we measure it: a rotation by 90 degrees clockwise remains the same rotation whether we describe it in Cartesian or polar coordinates.
Yet to compute with transformations — to combine them, to apply them to vectors, to analyze their effects — we must express them in coordinates through matrices.
The relationship between the abstract transformation and its various matrix representations reveals both the power and limitations of coordinate-based computation.

Let $T:V\rightarrow W$ be a linear transformation between vector spaces with chosen bases $\mathcal{B}=\{\mathbf{b}_1,\ldots,\mathbf{b}_n\}$ for $V$ and $\mathcal{B}'=\{\mathbf{b}'_1,\ldots,\mathbf{b}'_m\}$ for $W$.

> *Think:* In $[T]_{\mathcal{B}'}^{\mathcal{B}}$, the bottom basis $\mathcal{B}'$ is where we measure outputs (codomain), while the top basis $\mathcal{B}$ is where we measure inputs (domain).
> The matrix converts $\mathcal{B}$-coordinates to $\mathcal{B}'$-coordinates, reading from right to left just like function composition.

To construct a matrix representation of $T$, we need only record how it acts on basis vectors:

$$
T(\mathbf{b}_j) = \sum_{i=1}^m a_{ij}\mathbf{b}'_i
$$

The coefficients $a_{ij}$ form an $m\times n$ matrix $[T]_{\mathcal{B}'}^{\mathcal{B}}$ called the **matrix representation** of $T$ relative to bases $\mathcal{B}$ and $\mathcal{B}'$.
The entry $a_{ij}$ gives the $i$th coordinate of $T(\mathbf{b}_j)$ in basis $\mathcal{B}'$.

**Example 4.12 (Rotation in Different Bases).** Consider the counterclockwise rotation by $\pi/2$ in $\mathbb{R}^2$.
In the standard basis $\mathcal{B}=\{\hat{\imath},\hat{\jmath}\}$, this transformation has the familiar matrix representation:

$$
[T]_{\mathcal{B}}^{\mathcal{B}} = \begin{bmatrix}
    0 & -1 \\
    1 & 0
    \end{bmatrix}
$$

Let $\mathcal{B}'$ be the basis consisting of vectors $\mathbf{v}_1=(1,1)^T$ and $\mathbf{v}_2=(-1,2)^T$.
The change of basis matrix from $\mathcal{B}'$ to $\mathcal{B}$ is:

$$
P = \begin{bmatrix}
    1 & -1 \\
    1 & 2
    \end{bmatrix}
$$

In this new basis, the same rotation transformation appears as:

$$
[T]_{\mathcal{B}'}^{\mathcal{B}'} = P^{-1}\begin{bmatrix}
    0 & -1 \\
    1 & 0
    \end{bmatrix}P = \frac{1}{3}\begin{bmatrix}
    -1 & -5 \\
    2 & 1
    \end{bmatrix}
$$

Though the matrices appear quite different, they represent the identical geometric transformation of rotating vectors counterclockwise by $\pi/2$.

The matrix $[T]_{\mathcal{B}'}^{\mathcal{B}}$ converts input coordinates to output coordinates through standard matrix multiplication:

$$
[T(\mathbf{v})]_{\mathcal{B}'} = [T]_{\mathcal{B}'}^{\mathcal{B}}[\mathbf{v}]_{\mathcal{B}}
$$

This formula encapsulates how linear transformations interact with coordinates: first express the input in $\mathcal{B}$-coordinates, then multiply by the matrix representation to obtain $\mathcal{B}'$-coordinates of the output.

**Example 4.13 (Projection onto a Line).** Consider the projection onto the $x$-axis along the $y$-axis in $\mathbb{R}^2$.
In standard coordinates, this has matrix representation:

$$
[\Pi]_{\mathcal{B}}^{\mathcal{B}} = \begin{bmatrix}
    1 & 0 \\
    0 & 0
    \end{bmatrix}
$$

If we rotate our coordinate system by angle $\theta$, obtaining a new basis $\mathcal{B}'=\{(\cos\theta,\sin\theta)^T,(-\sin\theta,\cos\theta)^T\}$, the same projection appears more complicated:

> *Example:* When $\theta=\pi/4$, the basis vectors of $\mathcal{B}'$ are $(\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2})^T$ and $(-\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2})^T$.
> The projection matrix in these coordinates becomes
>
>

$$
>
> [\Pi]_{\mathcal{B}'}^{\mathcal{B}'} = \frac{1}{2}\begin{bmatrix}
> 1 & -1 \\
> -1 & 1
> \end{bmatrix}
>
>
$$

$$
[\Pi]_{\mathcal{B}'}^{\mathcal{B}'} = \begin{bmatrix}
    \cos^2\theta & -\cos\theta\sin\theta \\
    -\cos\theta\sin\theta & \sin^2\theta
    \end{bmatrix}
$$

The geometric action remains the same — we simply view it through different coordinate lenses.

When bases change, matrix representations transform systematically.
Suppose $T$ is known in the bases $\mathcal{C}'$ and $\mathcal{D}'$ and wanted in $\mathcal{C}$ and $\mathcal{D}$; the arrow notation writes the conversion for us, and the inner labels cancel:

$$
[T]_{\mathcal{D}}^{\mathcal{C}}
    = P_{\mathcal{D}\leftarrow\mathcal{D}'}\,[T]_{\mathcal{D}'}^{\mathcal{C}'}\,P_{\mathcal{C}'\leftarrow\mathcal{C}}
$$

This relationship reveals how different matrix representations of the same transformation differ: by an invertible change of coordinates on each side.
When domain and codomain share one basis, it becomes the similarity of the next section.

If a poor choice of bases can disguise a simple transformation, a shrewd choice can disrobe a complicated one — and the Fundamental Theorem of Linear Algebra (Theorem 3.25) tells us exactly how far the simplification can go.
There are always bases in which the transformation shows its true form:

$$
[T]_{\mathcal{B}'}^{\mathcal{B}} = \begin{bmatrix} I & 0 \\ 0 & 0 \end{bmatrix}
$$

where the identity block is $r\times r$ with $r=\operatorname{rank} T$: an isomorphism carrying coimage to image, framed by zeros that record the kernel and the cokernel.
*Every linear transformation, in the right pair of bases, is an identity block bordered by zeros.*
The Fundamental Theorem is not only a census of four subspaces; it is a normal form.
Exercise 7 builds those bases in general, and Theorem 4.3 is exactly what makes the construction possible — which is why Chapter 3 had to defer it.

Yet the simplification is bought with a basis: what one choice of coordinates makes plain, another hides.

## 4.5 Coordinate-Free Thought

Our development of coordinates and matrix representations presents a fundamental paradox.
We study linear transformations first as abstract mappings between vector spaces, understanding their properties independent of any particular measuring system.
Yet to compute with these transformations — to apply them to vectors, to compose them, to analyze their effects — we must choose coordinates and work with matrices.
A transformation is one thing; its matrices are many. Holding both truths at once is the discipline this chapter teaches.
Consider data drawn from some high-dimensional measurement process — perhaps gene expression levels across thousands of cells, or activation patterns across layers of a neural network.
The underlying biological or computational structure exists independent of how we choose to measure it.
Different experimental protocols or network architectures may yield different representations of the same fundamental patterns.
This suggests a deeper question: when are two apparently different representations truly equivalent?

> Some find the equivalent expression
>
>

$$
> AP = PB
>
$$

>
> to be more memorable and evocative.

**Definition 4.14 (Similarity).** Two matrices $A$ and $B$ are **similar** if there exists an invertible matrix $P$ such that:

$$
B = P^{-1}AP
$$

We write $A \sim B$ to denote similar matrices.

This algebraic relationship captures precisely when two matrices represent the same linear transformation viewed through different coordinate systems.
The matrix $P$ encodes the change of basis that transforms one view into another; it is the change of basis matrix of Definition 4.9, and the shared letter is not an accident.
An isomorphism $\varphi:V\rightarrow W$ has an **inverse** $\varphi^{-1}:W\rightarrow V$, sending each $\mathbf{w}$ to the unique $\mathbf{v}$ with $\varphi(\mathbf{v})=\mathbf{w}$; injectivity makes that $\mathbf{v}$ unique, surjectivity makes it exist, and a two-line check shows $\varphi^{-1}$ is itself linear.
With that in hand, we say two linear transformations $S,T:V\rightarrow V$ are **similar** if there exists an isomorphism $\varphi:V\rightarrow V$ such that $S = \varphi^{-1}T\varphi$.
When expressed in coordinates, this abstract notion manifests as matrix similarity.

> The term *conjugate* is more common in mathematics, but *similar* will do nicely.
>
>
>
>
> "`latex
> tikzcd
> V [r, "S"] [d, ""'] & V [d, ""]

> V [r, "T"'] & V
> tikzcd
> "`
>
>
>
> This diagram commutes when $S = \varphi^{-1}T\varphi$, illustrating similarity as conjugation by the isomorphism $\varphi$.

Two quantities in what follows deserve a word, since neither has been defined so far.
The **trace** of a square matrix is the sum of its diagonal entries, $\operatorname{tr} A=\sum_i a_{ii}$; a one-line computation with the sums shows that $\operatorname{tr}(XY)=\operatorname{tr}(YX)$ for any $X,Y$ of compatible sizes, and that innocuous identity is the whole reason trace survives a change of basis.
The **determinant** we take as known from multivariable calculus, along with its multiplicativity $\det(XY)=\det X\det Y$.

**Example 4.15 (Geometric Similarity).** Consider the shear that slides each horizontal line by an amount equal to its height.
In standard coordinates, this appears as:

$$
A = \begin{bmatrix}
    1 & 1 \\
    0 & 1
    \end{bmatrix}
$$

If we measure vectors instead using the basis $\{\mathbf{v}_1,\mathbf{v}_2\}$ where:

$$
\mathbf{v}_1 = \begin{pmatrix}2\\1\end{pmatrix}, \quad
    \mathbf{v}_2 = \begin{pmatrix}1\\1\end{pmatrix}
    \quad
    \Rightarrow
    \quad
    P = \begin{bmatrix}
    2 & 1 \\
    1 & 1
    \end{bmatrix}
$$

then the same shear has matrix:

$$
B = P^{-1}AP
    =
    \begin{bmatrix}
    2 & 1 \\
    -1 & 0
    \end{bmatrix}
$$

Nothing about $B$ announces a shear: it is not triangular, and its diagonal is not $1,1$.
Yet $A\sim B$ by construction, and the invariants agree: $\det B = 1$ and $\operatorname{tr} B = 2$, matching $A$, as the list below requires.
One writes $A\sim B$ to record exactly this — that the two matrices differ by a choice of coordinates and by nothing else.

Similar matrices share certain properties that are intrinsic to the transformation they represent:

1. They have the same determinant

2. They have the same rank

3. They have the same trace

> *Foreshadowing:* In Chapter 7, we will discover that similar matrices also share eigenvalues — another intrinsic property of the transformation they represent.

These **coordinate invariants** belong to the transformation itself rather than to any particular matrix representation.
They form a fingerprint that distinguishes genuinely different transformations from merely different coordinate views of the same map.

> *Foreshadowing:* In Chapter 11, we will see how Principal Component Analysis discovers coordinate systems that reveal intrinsic low-dimensional structure in high-dimensional data.

Yet we must remain mindful of the difference between a transformation and its various representations.
Matrices are tools for computation — powerful and necessary tools, but not the whole story.
The true objects of study are the transformations themselves, existing independent of how we choose to measure them.
The art lies in knowing when to reason coordinate-free and when to harness well-chosen coordinates: an art practiced, in the chapters ahead, on everything from differential equations to neural networks.

—

## Robotic Arm Kinematics

The mathematics of robotic manipulation provides a compelling demonstration of how different coordinate systems illuminate different aspects of the same physical system.
A robotic arm's motion can be described through multiple bases, each revealing different aspects of its behavior.
These coordinate choices — and the transformations between them — exemplify the fundamental principles developed throughout this chapter.

Consider a planar robotic arm with two revolute joints connecting two rigid links of lengths $L_1$ and $L_2$.
The configuration of this arm admits two natural coordinate systems:

1. Joint space coordinates $(\theta_1,\theta_2)$, measuring the angles of each joint

2. Task space coordinates $(x,y)$, giving the position of the end-effector

These spaces come equipped with natural bases: joint space has basis vectors corresponding to infinitesimal rotations of each joint, while task space inherits the standard Cartesian basis of the plane.
The transformation between these coordinates is given by:

$$
F(\theta_1,\theta_2) =
    \begin{pmatrix}
    L_1\cos\theta_1 + L_2\cos(\theta_1+\theta_2) \\
    L_1\sin\theta_1 + L_2\sin(\theta_1+\theta_2)
    \end{pmatrix}
$$

Though this transformation $F$ is nonlinear, its derivative $[DF]$ at any configuration provides a linear map between the tangent spaces — a change of basis matrix relating infinitesimal motions:

$$
\begin{pmatrix} \dot{x} \\ \dot{y} \end{pmatrix} =
    [DF]_{(\theta_1,\theta_2)}
    \begin{pmatrix} \dot{\theta}_1 \\ \dot{\theta}_2 \end{pmatrix}
$$

where:

$$
[DF]_{(\theta_1,\theta_2)} = \begin{bmatrix}
    -L_1\sin\theta_1 - L_2\sin(\theta_1+\theta_2) & -L_2\sin(\theta_1+\theta_2) \\
    L_1\cos\theta_1 + L_2\cos(\theta_1+\theta_2) & L_2\cos(\theta_1+\theta_2)
    \end{bmatrix}
$$

The columns of this matrix express the task-space velocities generated by unit joint velocities — they form a configuration-dependent basis for achievable end-effector motions.

> *Recall:* The Inverse Function Theorem from calculus guarantees that when $[DF]$ is invertible at a configuration (i.e., when $\det[DF]\neq 0$), $F$ has a local inverse — we can solve uniquely for small changes in joint angles needed to achieve desired end-effector motions.
> When $[DF]$ fails to be invertible, as happens when the arm is fully extended, certain instantaneous motions become impossible.

More complex manipulators illuminate additional aspects of coordinate relationships.
Consider extending our arm to three joints while maintaining planar end-effector motion.
Now joint space has basis vectors $\{\partial/\partial\theta_1, \partial/\partial\theta_2, \partial/\partial\theta_3\}$ while task space remains two-dimensional with basis $\{\partial/\partial x, \partial/\partial y\}$.
The derivative becomes a linear transformation $[DF]:\mathbb{R}^3\to\mathbb{R}^2$ between these spaces, with:

$$
[DF]_{(\theta_1,\theta_2,\theta_3)} =
    \begin{bmatrix}
    \displaystyle\frac{\partial x}{\partial \theta_1} &
    \displaystyle\frac{\partial x}{\partial \theta_2} &
    \displaystyle\frac{\partial x}{\partial \theta_3} \\
    \displaystyle\frac{\partial y}{\partial \theta_1} &
    \displaystyle\frac{\partial y}{\partial \theta_2} &
    \displaystyle\frac{\partial y}{\partial \theta_3}
    \end{bmatrix}
$$

This matrix has a nontrivial kernel — reflecting joint velocities that instantaneously leave the end-effector fixed.
Such self-motions exemplify the fundamental kernel-image relationship studied in Chapter 3, now emerging naturally in a concrete mechanical system.

The practical significance of these coordinate relationships manifests in trajectory planning.
A straight-line motion of the end-effector, though elegant in task coordinates, may demand intricate joint-space choreography.
Conversely, simple joint trajectories can trace complex paths through task space.
For the three-joint arm, redundancy enriches this relationship further — the same end-effector trajectory admits infinitely many joint space realizations, corresponding to different paths through the kernel of $[DF]$.

> *Foreshadowing:* Infinitely many joint motions achieve the same task; which should the controller choose?
> Chapter 6 constructs the operator that selects one — and Example 6.14 returns to this very arm.

This duality between representations reflects a deeper truth: no single coordinate system captures all aspects of a complex system with equal clarity.
The art of engineering lies not merely in choosing appropriate coordinates but in moving fluently between different representations as the problem demands.
Joint coordinates render questions of dynamics and joint limits transparent, while task coordinates simplify motion specification.
The mathematical framework developed in this chapter transforms this art from intuitive craft to systematic science, providing the tools needed to work effectively with multiple coordinate representations of the same underlying reality.

—

## Computer Graphics & Coordinate Systems

Modern computer graphics illuminates the practical power of coordinate transformations.
A virtual object — perhaps a spacecraft in a flight simulator — exists simultaneously in multiple coordinate systems, each chosen to simplify particular aspects of the simulation.
Understanding how these bases relate through the transformations of Section 4.3 converts complex geometric problems into systematic matrix computations.

Consider our virtual spacecraft.
Its geometry begins life in **body coordinates**, where the natural basis $\mathcal{B}_b=\{\mathbf{b}_1,\mathbf{b}_2,\mathbf{b}_3\}$ aligns with the craft's structure: $\mathbf{b}_1$ points through the nose, $\mathbf{b}_2$ along the right wing, and $\mathbf{b}_3$ downward.
In these coordinates, the craft's symmetries become apparent and control surfaces align with coordinate planes.
A point $\mathbf{p}$ on the spacecraft has coordinate vector $[\mathbf{p}]_{\mathcal{B}_b}$ relative to this body basis.

Yet our spacecraft moves through a virtual world with its own coordinate system.
The **world basis** $\mathcal{B}_w=\{\mathbf{w}_1,\mathbf{w}_2,\mathbf{w}_3\}$ typically aligns $\mathbf{w}_3$ with vertical, while $\mathbf{w}_1$ and $\mathbf{w}_2$ span the ground plane.
Following Section 4.3, the coordinate transformation from body to world basis follows from the change of basis matrix:

$$
[\mathbf{p}]_{\mathcal{B}_w} = P[\mathbf{p}]_{\mathcal{B}_b}
$$

This transformation matrix $P$ has columns expressing body basis vectors in world coordinates, exactly as prescribed by Definition 4.9:

$$
P = \begin{bmatrix}
    | & | & | \\
    [\mathbf{b}_1]_{\mathcal{B}_w} & [\mathbf{b}_2]_{\mathcal{B}_w} & [\mathbf{b}_3]_{\mathcal{B}_w} \\
    | & | & |
    \end{bmatrix}
$$

Each column shows how one body basis vector decomposes in world coordinates.
Like the rotation matrices studied in Section 3.1, this change of basis preserves lengths and angles — a crucial property for rigid objects.

A virtual camera introduces yet another basis.
The **camera basis** $\mathcal{B}_c=\{\mathbf{c}_1,\mathbf{c}_2,\mathbf{c}_3\}$ places the virtual lens at the origin with $\mathbf{c}_3$ pointing along the viewing direction and $\mathbf{c}_2$ aligned with the image's vertical axis.
Points transform to these coordinates through composition with another change of basis matrix $Q$:

$$
[\mathbf{p}]_{\mathcal{B}_c} = Q[\mathbf{p}]_{\mathcal{B}_w}
$$

The composition of these transformations — from body to world to camera coordinates — embodies the core algebraic insight of Section 4.3: changes of basis compose through matrix multiplication.
A point's coordinates transform as:

$$
[\mathbf{p}]_{\mathcal{B}_c} = QP[\mathbf{p}]_{\mathcal{B}_b}
$$

This matrix product captures the complete change of coordinates, though we often maintain separate transformations for clarity and efficiency.

Each basis in this sequence serves a specific purpose: body coordinates for physics simulation, world coordinates for scene composition, camera coordinates for visibility and rendering.
The transformations between them, though apparently complex, follow directly from our precise understanding of coordinates and bases developed in Section 4.2.
This exemplifies a broader principle: challenging problems often become tractable when viewed in appropriate coordinates.

> *Example:* When a spacecraft pitches upward 30°, its body basis vectors expressed in world coordinates become columns of the change of basis matrix $P$:
>
>

$$
>
> \begin{bmatrix}
> \sqrt{3}/2 & 0 & -1/2 \\
> 0 & 1 & 0 \\
> 1/2 & 0 & \sqrt{3}/2
> \end{bmatrix}
>
>
$$

>
> These columns are mutually orthogonal since $P$ represents rigid rotation.

The practical significance extends far beyond graphics.
In robotics, similar coordinate changes relate joint angles to end-effector position through the transformation matrices studied in Section 4.4.
In computer vision, camera and world bases must align to enable augmented reality.
In spacecraft guidance, body and inertial coordinates interplay in navigation algorithms.
Each application builds on the same mathematical foundation: the careful construction of bases and transformations between them.

This cascade of coordinate systems illustrates a final key insight from Section 4.5: bases should be chosen to match the natural structure of our problems.
Body coordinates respect vehicle symmetries; world coordinates align with gravity and terrain; camera coordinates match viewing geometry.
Each stage of the pipeline has its own best basis, and no one of them serves the rest; the careful matrix algebra developed in this chapter is what holds the cascade together.

—

## Exercises: Chapter 4

1. Let $\mathcal{B}=\{\mathbf{v}_1,\mathbf{v}_2\}$ be the basis of $\mathbb{R}^2$ with $\mathbf{v}_1=(1,2)^T$ and $\mathbf{v}_2=(1,-1)^T$.
Find the change of basis matrix $P$ from $\mathcal{B}$ to the standard basis, and explain why its columns are $\mathbf{v}_1$ and $\mathbf{v}_2$.
Then find $[\mathbf{w}]_\mathcal{B}$ for $\mathbf{w}=(5,1)^T$, and say which of $P$ and $P^{-1}$ you used and why.

2. Find $[\mathbf{v}]_\mathcal{B}$ for $\mathbf{v}=(2,1,-1)^T$ and $\mathcal{B}=\{(1,1,0)^T,(0,1,1)^T,(1,0,1)^T\}$.
Then find $[p]_{\mathcal{B}'}$ for $p(x)=x^2-2x+1$ and $\mathcal{B}'=\{1+x^2,\ x-x^2,\ 1-x\}$ in $\mathcal{P}_2$.
Each answer has a zero entry; say in each case what that zero means about the vector and the basis.

3. Show that $\{1,\ 1+x,\ 1+x+x^2\}$ is a basis of $\mathcal{P}_2$, and express each of $1$, $x$, $x^2$ in terms of it.
Write down the change of basis matrix from this basis to $\{1,x,x^2\}$, and check that your three expressions are its inverse read column by column.

4. Let $T:\mathcal{P}_2\to\mathcal{P}_2$ be differentiation, $T(p)=p'$.
Find $[T]_\mathcal{B}^\mathcal{B}$ for $\mathcal{B}=\{1,x,x^2\}$, and find $\operatorname{rank} T$ and $\operatorname{null} T$ from the matrix.
Then find a basis in which the matrix of $T$ is $\begin{bmatrix}0&1&0\\0&0&1\\0&0&0\end{bmatrix}$, and explain why no basis makes it diagonal.

5. Let $T:\mathbb{R}^2\to\mathbb{R}^2$ rotate counterclockwise by $\pi/4$.
Find its matrix in the standard basis and in $\mathcal{B}'=\{(1,1)^T,(-1,1)^T\}$, and observe that they are equal.
Explain what is special about $\mathcal{B}'$ that causes this, and find a basis of $\mathbb{R}^2$ in which the matrix of $T$ is *not* the standard one.

6. Decide whether $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$ and $B=\begin{bmatrix}5&-2\\-3&0\end{bmatrix}$ are similar, naming the invariant that settles it and the one that does not.
Then show that $A'=\begin{bmatrix}3&1\\1&3\end{bmatrix}$ and $B'=\begin{bmatrix}4&0\\0&2\end{bmatrix}$ *are* similar by exhibiting a $P$ with $B'=P^{-1}A'P$.
Is your $P$ the only one?

7. Let $T:V\to W$ be linear between finite-dimensional spaces, with $r=\operatorname{rank} T$.
Using Theorem 4.3, choose a subspace $U<V$ with $V=\operatorname{ker} T\oplus U$, prove that $T$ restricted to $U$ is an isomorphism onto $\operatorname{im} T$, and prove $\dim U=r$.
Now take for $V$ a basis listing $\mathbf{u}_1,\ldots,\mathbf{u}_r$ of $U$ *first* and a basis of $\operatorname{ker} T$ after, and for $W$ a basis beginning $T(\mathbf{u}_1),\ldots,T(\mathbf{u}_r)$; show that $[T]$ is then the block form $\begin{bmatrix}I&0\\0&0\end{bmatrix}$ of Section 4.4.

8. Let $V$ be a vector space with basis $\mathcal{B}=\{\mathbf{v}_1,\ldots,\mathbf{v}_n\}$.
Prove that a linear transformation $T:V\to W$ is completely determined by the vectors $T(\mathbf{v}_1),\ldots,T(\mathbf{v}_n)$, and that these may be prescribed arbitrarily.
Conclude that $V\cong\mathbb{R}^n$, and that any two real vector spaces of the same finite dimension are isomorphic.

9. Let $\mathcal{B}$ and $\mathcal{B}'$ be bases of $V$ with change of basis matrix $P$ from $\mathcal{B}'$ to $\mathcal{B}$.
Prove that $P$ is invertible, and that $P^{-1}$ is the change of basis matrix in the other direction.
Then let $\mathcal{B}''$ be a third basis, and prove that the change of basis matrices compose in the order you would expect.

10. Prove that similarity is an equivalence relation on $n\times n$ matrices.
Prove also that if $A\sim B$ then $A^k\sim B^k$ for every $k\geq 1$, and that $A$ is invertible if and only if $B$ is.
Where in each argument did you use that $P$ is invertible rather than merely nonzero?

11. Prove that similar matrices have the same determinant and the same trace.
Then show that the converse fails for $3\times3$ matrices, by exhibiting two that agree on both and are not similar.

12. Let $T:V\to V$ be linear and $\mathcal{B}$ a basis of $V$.
Prove that $[T]_\mathcal{B}^\mathcal{B}$ is diagonal if and only if every vector of $\mathcal{B}$ is sent by $T$ to a scalar multiple of itself, and that the diagonal entries are exactly those scalars.

13. Prove that a matrix similar to a diagonal matrix is similar to the diagonal matrix with the same entries in *any* order.
Then show that sharing a diagonal is not by itself enough: exhibit two $2\times2$ matrices with the same diagonal entries that are not similar.

14. The matrix $\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ is a quarter turn, and $\begin{bmatrix}-3&-5\\2&3\end{bmatrix}$ is similar to it.
Nothing in the second matrix's entries suggests a rotation, yet applying it four times returns every vector.
What, then, is a similarity class a description of, and why is "what does this matrix look like" the wrong question to ask of it?

15. Chapter 3 produced four spaces attached to a linear transformation, none of which mentioned a basis.
This chapter produces a matrix, which mentions nothing else.
Explain how both can be faithful descriptions of one transformation, and say precisely which features of a matrix are properties of the transformation and which are artifacts of the basis.

16. Fix a transformation $T:V\to V$ and a basis $\mathcal{B}$.
Characterize the change of basis matrices $P$ that leave $[T]$ unchanged, in terms of how $P$ interacts with $[T]_\mathcal{B}^\mathcal{B}$.
Then say what this makes a matrix representation: not a description of $T$, but a description of what?

17. The columns of $P$ express the vectors of $\mathcal{B}'$ in terms of $\mathcal{B}$, and $P$ also carries coordinates in the direction $\mathcal{B}'\to\mathcal{B}$.
Explain why these two directions must agree — why building the new basis vectors and rewriting coordinates are one act, not two.
Then say what would go wrong had $P$ been defined by rows instead of columns.

18. Two equal masses on a line are joined to each other and to two walls by three identical springs, so that the restoring forces are given by $K=\begin{bmatrix}2&-1\\-1&2\end{bmatrix}$ acting on the displacements $(x_1,x_2)^T$.
Find $[K]$ in the basis $\{(1,1)^T,(1,-1)^T\}$, and interpret the two diagonal entries physically.
Verify that $\det K$ and $\operatorname{tr} K$ are unchanged, and say what each of those numbers means for the system.

19. Two accelerometers lie in a plane, the first along the $x$-axis and the second at angle $\theta$ to it; idealize them so that their pair of readings is the coordinate vector of the true acceleration in the sensor basis $\mathcal{B}$.
Show that the change of basis matrix from $\mathcal{B}$ to the standard basis is $P=\begin{bmatrix}1&\cos\theta\\0&\sin\theta\end{bmatrix}$, so that $\mathbf{a}=P[\mathbf{a}]_\mathcal{B}$ recovers the acceleration.
Compute $\det P$, and explain why $\operatorname{cond}(P)\to\infty$ as $\theta\to 0$ means an error small *relative to the readings* becomes an error large *relative to* $\mathbf{a}$  — a badly chosen basis is a badly conditioned matrix.

20. A four-pixel greyscale strip is the vector $\mathbf{x}=(6,4,2,0)^T$, and a compression scheme re-expresses it in the basis

$$
\mathcal{B}=\left\{(1,1,1,1)^T,\ (1,1,-1,-1)^T,\ (1,-1,0,0)^T,\ (0,0,1,-1)^T\right\} ,
$$

whose vectors record average brightness, then coarser and finer differences.
Find $[\mathbf{x}]_\mathcal{B}$, then discard the last two coordinates and report the strip that survives, together with the error.
Compression keeps the leading coordinates; say what property of a basis makes that a sensible thing to do, and why no choice of basis loses anything if all four are kept.

21. *(Challenge.)* Prove that there are no $n\times n$ matrices $A$ and $B$ with $AB-BA=I$.
Then explain why the argument says nothing about the differentiation and multiplication operators on the space of all polynomials, which do satisfy this relation.

22. *(Challenge.)* Suppose $T:V\to V$ has a diagonal matrix in *every* basis of $V$.
Prove that $T$ is a scalar multiple of the identity.

---


# Chapter 5. Inner Products & Orthogonality

*"others triangular right angled course maintain. others obtuse acute scalene, in simple paths"*

**The spaces we inhabit possess** structure beyond mere addition and scaling.
Vectors carry more than direction: each has a length, and any two meet at a definite angle.
These geometric notions — of length and perpendicularity, of measure and relation — emerge not from arbitrary convention but from careful definition of how vectors interact through inner products.

The essence of geometric measurement — of lengths, angles, and orthogonality — carries far beyond the Euclidean setting in which it arose.
The familiar dot product of vectors served well in calculus, yet it represents merely one instance of a deeper structure.
Inner products provide the machinery to impose geometric order on abstract vector spaces, enabling us to measure and compare vectors in ways that respect their intrinsic nature.

This geometric perspective transforms our understanding of linear algebra.
Orthogonal vectors, previously understood through coordinate calculations, emerge as a fundamental organizing principle.
Orthogonal bases offer optimal frameworks for computation.
Orthogonal matrices preserve the geometric structure we construct.
Through inner products, the abstract vector spaces of previous chapters acquire shape and substance.

The choice of inner product shapes our view of a vector space, highlighting certain features while obscuring others.
Different inner products induce different notions of length and angle, each suited to particular applications.
Some arise naturally from physical principles, others from statistical considerations, still others from computational convenience.
The trick is an inner product that highlights what matters and preserves what must survive.

Our development proceeds from the concrete to the abstract and back again.
The familiar dot product guides our intuition as we ascend axiomatically.
Though we shall occasionally glimpse infinite-dimensional spaces through carefully chosen examples, our focus remains on finite-dimensional spaces where the theory achieves its purest form.

## 5.1 Dot & Inner Products

The dot product pushes out from its first appearance in calculus.
Two vectors $\mathbf{u},\mathbf{v}\in\mathbb{R}^n$ combine through coordinate-wise multiplication and addition:

$$
\mathbf{u}\cdot\mathbf{v} = \sum_{i=1}^n u_iv_i
$$

This operation, though defined through coordinates, reveals fundamental geometric features: length through $\|\mathbf{v}\| = \sqrt{\mathbf{v}\cdot\mathbf{v}}$, angle via $\mathbf{u}\cdot\mathbf{v} = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$, and orthogonality when $\mathbf{u}\cdot\mathbf{v}=0$.
That such a simple formula encodes so much geometric content suggests deeper structure at play.

Consider what properties make the dot product geometrically meaningful.
First, it treats vectors symmetrically: $\mathbf{u}\cdot\mathbf{v} = \mathbf{v}\cdot\mathbf{u}$.
Second, it is linear in each factor: $(c\mathbf{u}+\mathbf{w})\cdot\mathbf{v} = c(\mathbf{u}\cdot\mathbf{v}) + \mathbf{w}\cdot\mathbf{v}$.
Third, it ensures positive length: $\mathbf{v}\cdot\mathbf{v} \geq 0$, with equality only when $\mathbf{v}=\mathbf{0}$.
These properties — not the specific formula — enable geometric measurement.

This insight suggests generalizing beyond $\mathbb{R}^n$.
Consider the space $C([0,1])$ of continuous functions on the unit interval.
Though these vectors are curves rather than arrows, we might still wish to measure angles between them or test their orthogonality.
The integral formula

$$
\langle f,g\rangle = \int_0^1 f(t)g(t)\,dt
$$

provides exactly such a measurement.
It shares the key properties that made the dot product geometric: symmetry, linearity, and positivity.
Two functions are now "orthogonal" when their product integrates to zero — a concept familiar from calculus (and, later, Fourier analysis).

> *Example:* The functions $\sin(n\pi x)$ and $\sin(m\pi x)$ are orthogonal for distinct positive integers $n,m$ under this inner product, explaining the independence of Fourier sine series terms.

These examples motivate the abstract definition that captures their common essence:

**Definition 5.1 (Inner Product).** An **inner product** on a vector space $V$ is a function $\langle\cdot,\cdot\rangle:V\times V\to\mathbb{R}$ satisfying, for all $\mathbf{u},\mathbf{v},\mathbf{w}\in V$ and $c\in\mathbb{R}$:

1. Symmetry: $\langle \mathbf{u},\mathbf{v}\rangle = \langle \mathbf{v},\mathbf{u}\rangle$

2. Linearity: $\langle c\mathbf{u}+\mathbf{w},\mathbf{v}\rangle = c\langle \mathbf{u},\mathbf{v}\rangle + \langle \mathbf{w},\mathbf{v}\rangle$

3. Positive Definiteness: $\langle \mathbf{v},\mathbf{v}\rangle \geq 0$, with equality if and only if $\mathbf{v}=\mathbf{0}$

A vector space equipped with an inner product is called an **inner product space**.

This austere definition distills the essential features that enable geometric measurement.
Each property plays a vital role: symmetry ensures angles are well-defined; linearity connects geometry to vector space structure; positive definiteness guarantees meaningful notions of length and distance.

**Example 5.2 (Weighted Inner Products).** On $\mathbb{R}^n$, we need not weight all coordinates equally.
Given positive weights $a_1,\ldots,a_n$, the formula

$$
\langle \mathbf{u},\mathbf{v}\rangle_{\mathbf{a}} = \sum_{i=1}^n a_iu_iv_i
$$

defines an inner product that emphasizes certain components over others.
Such weighted measurements arise naturally in statistics, where the weights might reflect measurement uncertainty, or in mechanics, where they encode mass distribution.

**Example 5.3 (Matrix Inner Products).** The space $\mathbb{R}^{m\times n}$ of matrices admits several natural inner products.
The **Frobenius inner product**,

$$
\langle A,B\rangle_F = \operatorname{tr}(A^TB) = \sum_{i,j} a_{ij}b_{ij}
$$

treats a matrix as a long vector of entries.
Other inner products might weight different matrix entries according to their positions or statistical significance.

Each inner product imposes its own geometry on a vector space, determining how angles and lengths are measured.
The dot product is merely first among equals — the most elementary inner product on $\mathbb{R}^n$.

> *Foreshadowing:* The choice of inner product shapes everything from optimization algorithms to data analysis.
> We shall see its influence grow throughout this text.

The most fundamental consequence of an inner product is its induced notion of length.

**Definition 5.4 (Norm).** Given an inner product space $V$, the **norm** of a vector $\mathbf{v}\in V$ is defined by:

$$
\|\mathbf{v}\| = \sqrt{\langle \mathbf{v},\mathbf{v}\rangle}
$$

This induced norm measures the length of vectors in a way compatible with the inner product structure.

Though many norms exist on vector spaces, those arising from inner products possess special geometric properties.

## 5.2 Angles & Orthogonality

In physical space, vectors meet at angles.
This seemingly elementary observation — that two directions can be more or less aligned — extends far beyond geometry.
Two functions can be more or less correlated; two matrices can be more or less aligned.
In each case, the inner product reveals this angular relationship through a formula first glimpsed in calculus.

Our development requires first a fundamental inequality — one that ensures angles make sense in any inner product space.

**Lemma 5.5 (Cauchy-Schwarz Inequality).** For any vectors $\mathbf{u},\mathbf{v}$ in an inner product space,

$$
|\langle \mathbf{u},\mathbf{v}\rangle| \leq \|\mathbf{u}\|\|\mathbf{v}\|
$$

with equality if and only if one vector is a scalar multiple of the other.

*Proof.* For any real number $t$, positive-definiteness of the inner product requires:

$$
0 \leq \|\mathbf{u} + t\mathbf{v}\|^2 = \|\mathbf{u}\|^2 + 2t\langle \mathbf{u},\mathbf{v}\rangle + t^2\|\mathbf{v}\|^2
$$

This quadratic in $t$ must be nonnegative for all $t$, possible only if its discriminant is nonpositive:

$$
4\langle \mathbf{u},\mathbf{v}\rangle^2 \leq 4\|\mathbf{u}\|^2\|\mathbf{v}\|^2
$$

The case of equality follows by examining when this quadratic has exactly one root. ∎

It ensures that the ratio of inner product to product of norms cannot exceed unity in absolute value — exactly what we need to define angles through the familiar cosine relationship.

The **angle** between nonzero vectors $\mathbf{u}$ and $\mathbf{v}$ in an inner product space is the unique number $\theta \in [0,\pi]$ satisfying:

$$
\cos\theta = \frac{\langle \mathbf{u},\mathbf{v}\rangle}{\|\mathbf{u}\|\|\mathbf{v}\|}
$$

When this angle is $\pi/2$, we say the vectors are **orthogonal** and write $\mathbf{u} \perp \mathbf{v}$.
Engineers and data scientists know the quantity $\cos\theta$ by another name: the **cosine similarity** of $\mathbf{u}$ and $\mathbf{v}$ — a name this chapter will earn.

> *Example:* The functions $\sin x$ and $\cos x$ are orthogonal on $[-\pi,\pi]$ under the integral inner product $\langle f,g\rangle=\int_{-\pi}^{\pi}fg\,dx$  — a fact crucial to Fourier analysis.
> See Example 5.8.

Angles now exist in every inner product space — between functions, between matrices, between data — and the Euclidean properties persist wholesale: orthogonal vectors have inner product zero; small angles mean near-parallel; obtuse angles mean a negative inner product.

**Example 5.6 (Matrix Alignment).** Under the Frobenius inner product, matrices $A,B\in\mathbb{R}^{m\times n}$ form an angle through:

$$
\cos\theta = \frac{\operatorname{tr}(A^TB)}{\|A\|_F\|B\|_F}
$$

This measures how aligned their entries are: the Frobenius inner product vanishes when the entrywise products sum to nothing, whether because the two matrices are supported in different positions or because agreement in some is paid for by disagreement in others.
Such geometric interpretation of matrix relationships reveals structure hidden in algebraic formulas.

Orthogonality proves especially powerful in decomposing vectors.
When $\mathbf{u}\perp\mathbf{v}$, the Pythagorean theorem generalizes:

$$
\|\mathbf{u} + \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2
$$

This additivity of squared norms for orthogonal vectors enables decomposition of complex vectors into simpler orthogonal components — a principle that will guide our study of orthogonal bases and projections.

**Lemma 5.7 (Orthogonal Decomposition).** Let $\mathbf{v}_1,\ldots,\mathbf{v}_k$ be mutually orthogonal nonzero vectors.
Then they are linearly independent, and for any scalars $c_1,\ldots,c_k$:

$$
\left\|\sum_{i=1}^k c_i\mathbf{v}_i\right\|^2 = \sum_{i=1}^k c_i^2\|\mathbf{v}_i\|^2
$$

> *Foreshadowing:* This decomposition principle will reach its full power when we construct orthonormal bases, enabling optimal approximations and computational methods.

The proof follows from the distributive property of inner products and the vanishing of cross terms between orthogonal vectors.
More significant is the implication: orthogonal vectors combine independently, their contributions to any sum measurable separately without interference.
This independence principle — that orthogonal components can be analyzed separately — pervades modern applications from signal processing to quantum mechanics.

We close with a subtle observation: while every inner product induces a norm, not every norm arises from an inner product.
The $\ell^1$ and $\ell^\infty$ norms on $\mathbb{R}^n$, for instance, lack the geometric structure that inner products provide.
The special character of inner product norms lies in how they encode angles — a capability we shall exploit as we develop the theory of orthogonal bases and transformations.

## 5.3 Orthogonal & Orthonormal Bases

The bases we have thus far encountered arose from convenience or custom — coordinates chosen more by habit than principle.
Yet some bases are intrinsically better than others, measuring vectors in ways that respect the inner product structure we have so carefully constructed.
Such bases emerge from the concept of orthogonality, providing optimal frameworks for both theoretical understanding and practical computation.

A set of nonzero vectors $\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}$ in an inner product space is **orthogonal** if each vector is perpendicular to all others:

$$
\langle \mathbf{v}_i,\mathbf{v}_j\rangle = 0 \quad \text{for all }i\neq j
$$

When these vectors also have unit length, so that $\|\mathbf{v}_i\|=1$ for all $i$, we call the set **orthonormal**.
Such collections combine the geometric elegance of perpendicularity with the computational convenience of unit vectors.

> *Example:* The standard basis $\{\hat{\imath}, \hat{\jmath}, \hat{k}\}$ for $\mathbb{R}^3$ is orthonormal under the dot product — a fact so familiar we often forget its significance.

The power of orthogonal vectors lies in how they decompose the space they span.
When $\mathbf{v}_1,\ldots,\mathbf{v}_k$ are orthogonal, any vector in their span has a unique representation:

$$
\mathbf{x} = \sum_{i=1}^k c_i\mathbf{v}_i \quad\text{where}\quad c_i = \frac{\langle \mathbf{x},\mathbf{v}_i\rangle}{\|\mathbf{v}_i\|^2}
$$

The coefficients are read off from the inner product — no system of equations need be solved.
When the vectors are orthonormal, this simplifies further to $c_i = \langle \mathbf{x},\mathbf{v}_i\rangle$, the inner product itself revealing the coordinates directly.
Note what these orthonormal coefficients are: each $c_i$ is a cosine similarity, scaled by the length of $\mathbf{x}$.
That coordinates are inner products and that similarity is an inner product are the same fact, wearing different hats.

**Example 5.8 (Fourier Series).** The functions $\{\sin nx, \cos nx\}_{n=1}^\infty$ form an orthogonal set in $C[-\pi,\pi]$ under the inner product

$$
\langle f,g\rangle = \int_{-\pi}^\pi f(x)g(x)\,dx
$$

This orthogonality — discovered by Euler and exploited by Fourier — explains why trigonometric series decompose periodic functions so effectively.
The Fourier coefficients arise naturally as inner products, without need for integration by parts or other technical devices.

An orthogonal or orthonormal set that spans a space forms a basis of particular elegance.
Every vector has unique coordinates computable through inner products; the Pythagorean theorem holds for all linear combinations; geometric and algebraic properties align perfectly.
Yet we cannot simply wish such bases into existence — we must construct them systematically.

The **Gram-Schmidt process** provides such construction.
Beginning with any basis $\{\mathbf{b}_1,\ldots,\mathbf{b}_n\}$, we build an orthogonal basis $\{\mathbf{v}_1,\ldots,\mathbf{v}_n\}$ spanning the same space:

$$
\begin{array}{rcl}
\mathbf{v}_1 &=& \mathbf{b}_1 \\
\mathbf{v}_2 &=& \mathbf{b}_2 - \Pi_{\mathbf{v}_1}\mathbf{b}_2 \\
\mathbf{v}_3 &=& \mathbf{b}_3 - \Pi_{\mathbf{v}_1}\mathbf{b}_3 - \Pi_{\mathbf{v}_2}\mathbf{b}_3 \\
&\vdots& \\
\mathbf{v}_k &=& \mathbf{b}_k - \sum_{i=1}^{k-1}\Pi_{\mathbf{v}_i}\mathbf{b}_k
\end{array}
$$

where $\Pi_{\mathbf{v}}\mathbf{u} = \frac{\langle \mathbf{u},\mathbf{v}\rangle}{\|\mathbf{v}\|^2}\mathbf{v}$ denotes orthogonal projection.
Each new vector is made orthogonal to all previous ones by subtracting away its components in their directions.
The display is one idea written down $n$ times: subtract what the earlier vectors already account for, and keep whatever is left over.

**Example 5.9 (Polynomial Orthogonalization).** Consider the space $\mathcal{P}_4$ with inner product $\langle f,g\rangle = \int_{-1}^1 f(x)g(x)\,dx$.
Starting with the monomial basis $\{1,x,x^2,x^3,x^4\}$, Gram-Schmidt produces (up to scaling) the **Legendre polynomials**:

$$
\begin{array}{rcl}
P_0(x) &=& 1 \\
P_1(x) &=& x \\
P_2(x) &=& \frac{1}{2}(3x^2-1) \\
P_3(x) &=& \frac{1}{2}(5x^3-3x) \\
P_4(x) &=& \frac{1}{8}(35x^4-30x^2+3)
\end{array}
$$

> These polynomials play a fundamental role not only in gravitational theory but also in quantum mechanics, where they describe angular momentum states, and in numerical integration, where they provide optimal quadrature points.

These orthogonal polynomials, discovered by Legendre in studying gravitational potential, arise naturally from imposing orthogonality on the simplest polynomial basis.
The increasing complexity of coefficients reflects how each new polynomial must maintain orthogonality to all previous ones — a constraint leading to ever more intricate balancing of terms.

> *Foreshadowing:* Gram-Schmidt, run on the columns of a matrix, is a factorization in disguise — Section 5.6.

The Gram-Schmidt process, though elegant in theory, can suffer numerical instability in practice.
Each projection accumulates computational errors that can destroy orthogonality in the final basis.
A more stable approach — **modified Gram-Schmidt** — applies the projections sequentially rather than simultaneously.
Though mathematically equivalent, this version better preserves orthogonality in finite-precision arithmetic.

No numerical library computes a dense QR factorization by Gram-Schmidt.
Production QR factorizations are computed by **Householder reflections**, which are stabler and cheaper, and which this book will name without developing.
The process is kept here for two reasons, neither of them speed: it is the only proof of existence available to us, both for orthonormal bases and for the factorization of Section 5.6, and it is the one orthogonalization a person can carry out by hand.

Having constructed orthogonal bases, we might ask which are best suited to particular problems.
The answer depends on what structure we wish to preserve or illuminate:

1. For differential equations, bases of eigenfunctions reveal dynamical behavior

2. In signal processing, Fourier bases expose frequency content

3. In data analysis, principal component bases optimize variance capture

The choice of orthogonal basis shapes our view of the space and its vectors — a theme we shall explore more deeply when studying eigenvalues and singular values.

> *BONUS!* While every finite-dimensional inner product space admits an orthonormal basis, infinite-dimensional spaces may resist such complete orthogonalization.
> What survives there, and at what cost, is the business of **functional analysis**.

## 5.4 Adjoints & Transposes

The familiar operation of matrix transpose harbors deeper structure than first appears.
When we write $A^T$ for a matrix $A$, we do more than reflect entries across the diagonal — we encode a fundamental relationship between linear transformations and inner products.
This relationship, abstracted from its matrix origins, provides the key to understanding how transformations interact with geometric structure.

Consider first the matrix transpose in $\mathbb{R}^n$ with its standard inner product.
For any matrix $A$, its transpose $A^T$ satisfies a crucial property: for all vectors $\mathbf{x}$ and $\mathbf{y}$,

$$
\langle A\mathbf{x},\mathbf{y}\rangle = \langle \mathbf{x},A^T\mathbf{y}\rangle
$$

This seemingly innocent equation reveals more than notation: the transpose $A^T$ is not merely a matrix operation but the unique linear transformation that preserves inner product relationships with $A$.

One slogan governs everything that follows: the adjoint is the transpose without a basis.
A transpose is bookkeeping performed on an array of numbers; the adjoint is what that bookkeeping means.
Nor is the identity above chosen so much as forced, since out of $A$, $\mathbf{x}$ and $\mathbf{y}$ there is one scalar to be built — namely $\langle A\mathbf{x},\mathbf{y}\rangle$  — and the adjoint is whatever map allows that scalar to be read the other way round.

**Definition 5.10 (Adjoint).** Let $V$ and $W$ be finite-dimensional inner product spaces and $T:V\rightarrow W$ a linear transformation.
The **adjoint** of $T$ is the unique linear transformation $T^*:W\rightarrow V$ satisfying:

$$
\langle T\mathbf{v},\mathbf{w}\rangle_W = \langle \mathbf{v},T^*\mathbf{w}\rangle_V
$$

for all $\mathbf{v}\in V$ and $\mathbf{w}\in W$.

> *Caveat:* Finite-dimensionality is not decoration.
> On the space of all polynomials with $\langle f,g\rangle=\int_0^1 fg$, the operator $D$ has no adjoint at all: no polynomial can represent the functional $f\mapsto f(1)$.

The coordinate formula of Section 5.3 handles both claims.
Fix an orthonormal basis $\{\mathbf{e}_i\}$ of $V$ and set $T^*\mathbf{w}=\sum_i\langle T\mathbf{e}_i,\mathbf{w}\rangle_W\,\mathbf{e}_i$; the coordinate formula then gives $\langle \mathbf{v},T^*\mathbf{w}\rangle_V = \sum_i\langle \mathbf{v},\mathbf{e}_i\rangle\langle T\mathbf{e}_i,\mathbf{w}\rangle_W = \langle T\mathbf{v},\mathbf{w}\rangle_W$, which is existence, and $T^*$ is linear in $\mathbf{w}$ because each coefficient $\langle T\mathbf{e}_i,\cdot\rangle_W$ is.
For uniqueness, if $T_1^*$ and $T_2^*$ both satisfy the equation then $\langle \mathbf{v},(T_1^*-T_2^*)\mathbf{w}\rangle=0$ for every $\mathbf{v}$; take $\mathbf{v}$ to be that difference and positive definiteness finishes it.

**Example 5.11 (Differentiation Adjoint).** Consider the differentiation operator $D:\mathcal{P}_2\rightarrow\mathcal{P}_1$ with inner product $\langle f,g\rangle = \int_0^1 f(x)g(x)\,dx$.
Its adjoint $D^*:\mathcal{P}_1\rightarrow\mathcal{P}_2$ satisfies:

$$
\int_0^1 (Df)(x)g(x)\,dx = \int_0^1 f(x)(D^*g)(x)\,dx
$$

Integration by parts turns the left side into $-\int_0^1 f g' + f(1)g(1) - f(0)g(0)$, so $D^*$ is $-D$ corrected by the two boundary evaluations — and since $\mathcal{P}_2$ is finite-dimensional, each of those evaluations is itself represented by a polynomial.
Nothing is left over: in the monomial bases,

$$
[D^*] = \begin{bmatrix} -6 & 2 \\ 12 & -24 \\ 0 & 30\end{bmatrix} ,
    \qquad D^*(1) = 12x-6 , \qquad D^*(x) = 30x^2-24x+2 .
$$

The adjoint of a differentiation operator is an ordinary polynomial map, not an integral one — a relationship fundamental to both differential equations and variational principles in mechanics.

**Example 5.12 (Sum & Copy).** Let $A:\mathbb{R}^n\rightarrow\mathbb{R}$ send a vector to the sum of its coordinates, $A\mathbf{x}=\sum_i x_i$; as a matrix, $A=\mathbf{1}^T$.
Since $\langle A\mathbf{x},t\rangle = t\sum_i x_i = \langle \mathbf{x},t\mathbf{1}\rangle$, the adjoint $A^*:\mathbb{R}\rightarrow\mathbb{R}^n$ is $t\mapsto t\mathbf{1}$.
Summing forward, copying backward.
A network that accumulates a single gradient over a batch of examples is summing; the correction it then hands back to every example alike is the adjoint copying.

**Example 5.13 (The Shift).** On $\mathbb{R}^n$ the left shift has for its adjoint the right shift,

$$
S(x_1,\ldots,x_n)^T = (x_2,\ldots,x_n,0)^T
    \qquad
    S^*(y_1,\ldots,y_n)^T = (0,y_1,\ldots,y_{n-1})^T ,
$$

as one reads off from $\langle S\mathbf{x},\mathbf{y}\rangle = \sum_{i=1}^{n-1}x_{i+1}y_i = \langle \mathbf{x},S^*\mathbf{y}\rangle$.
The adjoint is visibly the undoing direction and just as visibly not the inverse: $S^*S = \operatorname{diag}(0,1,\ldots,1)$ deletes the first coordinate while $SS^* = \operatorname{diag}(1,\ldots,1,0)$ deletes the last, so that both composites are projections and neither is $I_n$.
Section 5.5 meets the same phenomenon in its one-sided form, where a composite that *is* the identity certifies injectivity; $S$, being neither injective nor surjective, is denied that certificate on both sides.

The adjoint operation respects the algebraic structure of linear transformations while reversing their direction:

> *Foreshadowing:* The theory of adjoints extends to infinite-dimensional spaces, but requires additional machinery from functional analysis including completeness and boundedness of operators.

**Lemma 5.14.** For linear transformations $S$ and $T$ between finite-dimensional inner product spaces, and for any scalar $c$:

1. $(S+T)^* = S^* + T^*$

2. $(cT)^* = cT^*$

3. $(ST)^* = T^*S^*$

4. $(T^*)^* = T$

> *Example:* For a rotation matrix $R$ in $\mathbb{R}^2$, the adjoint $R^*$ corresponds to rotation in the opposite direction — explaining why $R^T R = I$.

When we choose orthonormal bases for our spaces, the matrix of $T^*$ is the transpose of the matrix of $T$.
This explains our notation: the abstract adjoint operation generalizes matrix transpose to arbitrary inner product spaces.
The matrix transpose is merely the adjoint operation expressed in coordinates.

**Example 5.15 (An Adjoint That Is Not A Transpose).** Weight the coordinates of $\mathbb{R}^n$ as in Example 5.2, and write the resulting inner product as $\langle \mathbf{x},\mathbf{y}\rangle_M = \mathbf{x}^TM\mathbf{y}$ for a symmetric positive-definite $M$.
The defining identity reads $\mathbf{x}^TA^TM\mathbf{y} = \mathbf{x}^TMA^*\mathbf{y}$ for every $\mathbf{x}$ and $\mathbf{y}$, which forces $MA^* = A^TM$, and hence $A^* = M^{-1}A^TM$.
Taking $M=\operatorname{diag}(1,4)$, so that the second coordinate counts four times as heavily as the first,

$$
A = \begin{bmatrix} 1 & 1\\ 0 & 1\end{bmatrix}
    \qquad\Longrightarrow\qquad
    A^* = \begin{bmatrix} 1 & 0\\ 0 & \tfrac14\end{bmatrix}
          \begin{bmatrix} 1 & 0\\ 1 & 1\end{bmatrix}
          \begin{bmatrix} 1 & 0\\ 0 & 4\end{bmatrix}
        = \begin{bmatrix} 1 & 0\\ \tfrac14 & 1\end{bmatrix} ,
$$

which is manifestly not $A^T$.
Change the inner product and the transpose stops being the answer, which is why the adjoint deserves a name of its own.

The definition also earns its keep in the census of subspaces.
A transformation and its adjoint pair the four fundamental spaces two by two: $T$ carries the coimage onto the image, $T^*$ carries the image back onto the coimage, $T$ annihilates the kernel and $T^*$ annihilates the cokernel — once Chapter 6 realizes those two quotients as the honest subspaces $(\operatorname{ker} T)^{\perp}$ and $(\operatorname{im} T)^{\perp}$.
Read that way the adjoint is the involution making four separate spaces into two couples, and the definition, arbitrary-looking on the page, becomes the only one that could have been written down.

> *Foreshadowing:* The adjoint is the key that unlocks the geometry of the Fundamental Theorem in Chapter 6.
> Watch what $\operatorname{im} A^T$ turns out to be — and what stands perpendicular to it.

The transpose also packages inner products wholesale.
For vectors $\mathbf{x}_1,\ldots,\mathbf{x}_k$ assembled as the columns of a matrix $X$, the **Gram matrix**

$$
G = X^TX , \qquad g_{ij} = \langle \mathbf{x}_i,\mathbf{x}_j\rangle ,
$$

records every pairwise inner product at once.
When the $\mathbf{x}_i$ are unit vectors, $G$ is precisely the matrix of pairwise cosine similarities.

> *Foreshadowing:* Remember the Gram matrix.
> It will return three times in disguise: as a correlation matrix in Chapters 9 and 11, as a kernel matrix in Chapter 11, and as an attention matrix in Chapter 13.

**Example 5.16 (Word Embeddings).** Modern language models represent each word as a vector in $\mathbb{R}^n$, with $n$ in the hundreds, learned from patterns of co-occurrence in text.
Meaning becomes geometry: words of similar use point in similar directions, unrelated words sit nearly orthogonal, and cosine similarity is the measure of semantic nearness.
The geometry records relations as differences, so that

$$
\textrm{king} - \textrm{man} + \textrm{woman} \simeq \textrm{queen}
$$

holds to within a small angle.
The same geometry serves whole documents: assemble their vectors as the columns of $X$, and the Gram matrix $X^TX$ tabulates every pairwise similarity at once; semantic search is reading off its largest entries.

The relationship between a transformation and its adjoint illuminates the geometry of linear mappings.
An operator $T:V\rightarrow V$ that equals its own adjoint, $T=T^*$, is **self-adjoint**; others satisfy $T^*=-T$.
Self-adjointness is a condition on the inner product and not on an array of numbers: in an orthonormal basis it reads $A=A^T$, while the weighted product of Example 5.15 turns it into $MA=A^TM$, symmetry of $MA$ rather than of $A$.
Most operators lie between the extremes, their deviation from self-adjointness measuring how they distort the inner product structure.
Self-adjoint operators have real eigenvalues and orthogonal eigenvectors — the spectral half of the story, waiting in Chapters 9 and 10.

## 5.5 Orthogonal Transformations

The transformations worth singling out preserve geometric structure.
A rotation changes perspective while maintaining shape; a reflection inverts orientation while preserving angles.
Such transformations — those respecting the inner product structure we have so carefully built — arise throughout engineering, from rigid body mechanics to signal processing to data analysis.
Their power lies in a fusion of geometric intuition and algebraic precision.

> *Note:* The term "orthogonal" here connotes preservation of all inner products, not merely orthogonality relations.
> A more accurate (though less traditional) name might be "inner-product-preserving" or "orthonormal."

**Definition 5.17 (Orthogonal Transformation).** A linear transformation $T:V\rightarrow V$ on an inner product space is **orthogonal** if it preserves inner products:

$$
\langle T\mathbf{u},T\mathbf{v}\rangle = \langle \mathbf{u},\mathbf{v}\rangle
$$

for all vectors $\mathbf{u},\mathbf{v}\in V$.

An orthogonal transformation preserves lengths and angles: for all $\mathbf{u}$ and $\mathbf{v}$,

$$
\|T\mathbf{v}\| = \|\mathbf{v}\|
    \quad : \quad
    \cos\theta = \frac{\langle T\mathbf{u},T\mathbf{v}\rangle}{\|T\mathbf{u}\|\|T\mathbf{v}\|} = \frac{\langle \mathbf{u},\mathbf{v}\rangle}{\|\mathbf{u}\|\|\mathbf{v}\|}
$$

These geometric constraints have powerful algebraic consequences, connecting our work here to the theory of adjoints developed in the previous section:

**Lemma 5.18.** For a linear transformation $T$ on a finite-dimensional inner product space, the following are equivalent:

1. $T$ is orthogonal

2. $T^*T = TT^* = I$

3. $T^* = T^{-1}$

*Proof.* Suppose (1).
For all $\mathbf{u},\mathbf{v}$,

$$
\langle T^*T\mathbf{u},\mathbf{v}\rangle = \langle T\mathbf{u},T\mathbf{v}\rangle = \langle \mathbf{u},\mathbf{v}\rangle = \langle \mathrm{id}_V\mathbf{u},\mathbf{v}\rangle ,
$$

so $\langle (T^*T-\mathrm{id}_V)\mathbf{u},\mathbf{v}\rangle=0$ for every $\mathbf{v}$; taking $\mathbf{v}=(T^*T-\mathrm{id}_V)\mathbf{u}$ and applying positive definiteness gives $T^*T=\mathrm{id}_V$.
Then $T$ is injective, hence invertible since domain and codomain have equal dimension, and $T^{-1}=T^*$, which is (3); multiplying on the left by $T$ returns $TT^*=\mathrm{id}_V$ and so (2).
Conversely (2) gives $\langle T\mathbf{u},T\mathbf{v}\rangle = \langle T^*T\mathbf{u},\mathbf{v}\rangle = \langle \mathbf{u},\mathbf{v}\rangle$, which is (1); and (3) gives (2) at once, since $T^*=T^{-1}$ says exactly that both products are the identity.
Throughout, $I$ in the statement of the lemma is $\mathrm{id}_V$. ∎

When we choose orthonormal bases for our space, orthogonal transformations have particularly elegant matrix representations.
A square matrix $Q$ is **orthogonal** if

$$
Q^TQ = I = QQ^T
$$

The set of all $n\times n$ orthogonal matrices is denoted $O(n)$.

Drop the requirement that $Q$ be square and one property survives intact.
A matrix $Q\in\mathbb{R}^{m\times n}$ with $m\geq n$ and $Q^TQ=I_n$  — orthonormal columns and nothing more — is an **isometry**: since $\|Q\mathbf{x}\|^2 = \mathbf{x}^TQ^TQ\mathbf{x} = \|\mathbf{x}\|^2$, it preserves every length, and with it every inner product and every angle, so that nothing but $\mathbf{0}$ is sent to $\mathbf{0}$ and $Q$ is injective.
It cannot, however, undo itself from the other side.
A matrix taller than it is wide has no inverse, and $QQ^T$ is the orthogonal projection of $\mathbb{R}^m$ onto $\operatorname{im} Q$ rather than the identity: it fixes each column of $Q$ and annihilates everything perpendicular to all of them, which is the whole description of a projection and is developed as such in Chapter 6.
The square matrices are the case in which the isometry is onto as well as injective, the projection exhausts $\mathbb{R}^m$, and the two composites coincide; that case, and only that case, is $O(n)$.
The pattern outlives the chapter.
For a map between spaces of different dimension there are two composites to be formed, and *which side is the identity records whether the map is injective or surjective.*

Orthogonal matrices repay their cost in computation:

> *Foreshadowing:* The power of orthogonal matrices in computation will become even clearer when we study the Singular Value Decomposition in Chapter 10, where they provide optimal coordinate transformations for a variety of purposes.

**Lemma 5.19.** An orthogonal matrix $Q$ satisfies:

1. Its columns (and rows) form an orthonormal basis

2. Its inverse equals its transpose: $Q^{-1} = Q^T$

3. It preserves lengths: $\|Q\mathbf{x}\| = \|\mathbf{x}\|$

4. It preserves inner products, and hence angles: $(Q\mathbf{x})^T(Q\mathbf{y}) = \mathbf{x}^T\mathbf{y}$

5. Its determinant is $\pm 1$

**Example 5.20 (Rigid Body Motion).** The orientation of a rigid body in three-dimensional space is described by an orthogonal transformation.
Its matrix representation $R$ in any orthonormal basis satisfies $R^TR=RR^T=I$, with $\det R = \pm 1$.
When $\det R = 1$, the transformation represents a pure rotation; when $\det R = -1$, it includes a reflection.

> These mechanical constraints — preservation of distances and angles — arise from the physical principle that rigid bodies maintain their shape under motion.
> The orthogonality of $R$ encodes this fundamental geometric requirement algebraically.

This geometric structure explains why different physical quantities transform differently under rotation.
Position vectors transform by $R$; so does angular momentum, but with a sign: $\mathbf{L}\mapsto(\det R)\,R\mathbf{L}$, so that a reflection reverses it where a rotation does not.
Quantities that behave this way are called *pseudovectors*, and the $\det R$ is the whole of the difference.

**Example 5.21 (Signal Transforms).** The Discrete Fourier Transform (DFT) is the same idea over complex scalars, where inner products become conjugate-symmetric and the transformation is called *unitary* rather than orthogonal.
Normalized so that its basis vectors are unit vectors, it satisfies Parseval's identity — the conservation of signal energy between time and frequency domains:

$$
\sum_{n=0}^{N-1} |x[n]|^2 = \sum_{k=0}^{N-1} |X[k]|^2 ,
    \qquad X[k] = \frac{1}{\sqrt{N}}\sum_{n=0}^{N-1} x[n]\,e^{-2\pi ikn/N}
$$

> *Nota bene:* A reader who has not met the discrete Fourier transform can take this example on trust: orthonormality of its basis is the whole of the content.

where $x[n]$ is the time-domain signal and $X[k]$ its frequency-domain transform.
This conservation arises precisely because the normalized DFT basis vectors form an orthonormal set; drop the $1/\sqrt{N}$ and each basis vector has length $\sqrt{N}$, which is where the familiar factor of $1/N$ in the identity comes from.

The composition of orthogonal transformations is orthogonal, and the inverse of an orthogonal transformation is orthogonal.
This closure under composition and inversion hints at deeper algebraic structure — the orthogonal transformations form a group under composition, though we shall not pursue this abstraction further.

> *Caveat:* The term "group" here has precise mathematical meaning, describing a set closed under an associative operation, with identity and inverses.

Orthogonal transformations provide the mathematical framework for rigid motion in mechanics, preserve energy in wave equations, and offer optimal coordinate changes for data analysis.
Their ubiquity in engineering practice — from robotics to signal processing to machine learning — is no accident: the most useful transformations are those that preserve structure.

## 5.6 The QR Decomposition

Our development of orthogonality through Section 5.3 provides the foundation for another fundamental matrix factorization.
The Gram-Schmidt process transforms any basis into an orthogonal one through systematic projection — a process that itself defines a natural decomposition of the original matrix.
This factorization, called the QR decomposition, expresses a matrix as a product of one with orthonormal columns and an upper triangular one.

**Definition 5.22 (QR Decomposition).** The **QR decomposition** of a matrix $A\in\mathbb{R}^{m\times n}$ with $m\geq n$ expresses it as a product

$$
A = QR
$$

where $Q\in\mathbb{R}^{m\times n}$ has orthonormal columns, so that $Q^TQ=I_n$, and $R\in\mathbb{R}^{n\times n}$ is upper triangular.
When the columns of $A$ are independent, the decomposition is unique if we require the diagonal entries of $R$ to be positive.

> *Caution:* When $m>n$ the factor $Q$ is not square, and belongs to $O(n)$ only in the case $m=n$.
> What it is in every case is an isometry in the sense of Section 5.5: its columns are orthonormal, so $Q^TQ=I_n$, while $QQ^T$ is the orthogonal projection onto $\operatorname{im} Q$.

> *Terminology:* Every matrix with at least as many rows as columns has a QR decomposition; what varies is the shape.
> The **reduced** (or **thin**) form is the one defined here, with $Q$ of size $m\times n$ and $R$ of size $n\times n$; the **full** form pads $Q$ out to an $m\times m$ orthogonal matrix and $R$ down with $m-n$ rows of zeros.
> Software will return whichever form it was asked for, so ask.

Consider how this decomposition arises from orthogonalizing $A$'s columns.
Writing $A = [\mathbf{a}_1\;\cdots\;\mathbf{a}_n]$, the Gram-Schmidt process produces orthonormal vectors $\{\mathbf{q}_1,\ldots,\mathbf{q}_n\}$ where each $\mathbf{q}_k$ emerges from $\mathbf{a}_k$ by subtracting its projections onto previous vectors.
The coefficients of these projections, together with the normalization factors, assemble naturally into an upper triangular matrix $R$.
This construction reveals both why the columns of $Q$ must be orthonormal and why $R$ assumes triangular form — each column of $A$ expresses through the $\mathbf{q}_i$ only up to its own index.

**Example 5.23 (Simple QR Form).** Consider the matrix

$$
A = \begin{bmatrix}
    3 & -4 \\
    4 & 3
    \end{bmatrix}
$$

Direct computation yields

$$
Q = \begin{bmatrix}
    0.6 & -0.8 \\
    0.8 & 0.6
    \end{bmatrix}
    \quad\text{and}\quad
    R = \begin{bmatrix}
    5 & 0 \\
    0 & 5
    \end{bmatrix}
$$

The orthogonal factor $Q$ captures the rotation inherent in $A$, while the triangular factor $R$ represents scaling.
This geometric decomposition — into pure rotation followed by scaling — exemplifies how matrix factorizations reveal underlying structure.

The QR decomposition provides more than mere factorization — it reveals the matrix's action through natural stages.
Like the eigendecomposition of Chapter 7 and the singular value decomposition of Chapter 10, both to come, QR decomposes a transformation into simpler, geometrically meaningful operations:

1. The factor $Q$ provides an orthonormal basis for the column space of $A$

2. The triangular factor $R$ describes coordinates in this basis

3. Their product $QR$ reconstructs the original transformation

**Lemma 5.24 (Existence and Uniqueness).** Every $A\in\mathbb{R}^{m\times n}$ with $m\geq n$ admits a QR decomposition, with $Q\in\mathbb{R}^{m\times n}$ having orthonormal columns and $R\in\mathbb{R}^{n\times n}$ upper triangular.
It is unique, with positive diagonal entries in $R$, exactly when the columns of $A$ are independent — in particular whenever $A$ is square and nonsingular.
When the columns of $A$ are dependent the decomposition still exists but is no longer unique, and the failure can be discrete or continuous: for $\begin{bmatrix}1&0\\0&0\end{bmatrix}$ only four choices of $Q$ serve, while for $\begin{bmatrix}0&1\\0&0\end{bmatrix}$ every orthogonal $Q$ does.
Rank alone does not decide which happens; both of those matrices have rank one.

Gram-Schmidt proves the independent-column case and stalls on the other, a dependent column being left with nothing to normalize.
What covers the general statement is the Householder procedure named in Section 5.3, which assembles $Q$ by reflections chosen from $A$ rather than by dividing each column by a length that may be zero.

This factorization provides powerful tools for both theoretical analysis and practical computation.
Systems of equations yield naturally to solution through QR factors: if $A\mathbf{x}=\mathbf{b}$, then $R\mathbf{x}=Q^T\mathbf{b}$ reduces to back-substitution.
The orthogonal factor $Q$ preserves lengths and angles while $R$ implements a simple triangular transformation.

—

## Clustering & $K$-Means

Data arrives unlabeled.
A million customer profiles, a warehouse of sensor traces, sixty thousand handwritten digits: nobody has marked which belongs with which.
**Clustering** is the recovery of categories the data never declared — and in an inner product space, "belongs with" acquires a meaning one can compute: nearness in the induced norm.

Given vectors $\{\mathbf{x}_1,\ldots,\mathbf{x}_N\}\subset V$ and a number $K$ of clusters, the {$K$-means} problem seeks cluster centers $\{\mathbf{c}_1,\ldots,\mathbf{c}_K\}$ minimizing the total squared distance from each point to its nearest center:

$$
\sum_{i=1}^N \min_{j=1,\ldots,K} \|\mathbf{x}_i - \mathbf{c}_j\|^2 ,
$$

distances measured in the norm induced by the inner product (Definition 5.4).
The standard algorithm, due to Lloyd, alternates two moves: hold the centers fixed and assign each point to its nearest; hold the assignments fixed and move each center to the mean of its points.

"`latex
algorithm

{Vectors $\{\mathbf{x}_1,\ldots,\mathbf{x}_N\}\subset V$, number of clusters $K$}
{Cluster centers $\{\mathbf{c}_1,\ldots,\mathbf{c}_K\}$ and assignments}
Initialize $\mathbf{c}_1,\ldots,\mathbf{c}_K$ randomly from the data
not converged{
    {$i\leftarrow 1$  $N$}{
        Assign $\mathbf{x}_i$ to nearest center using norm from inner product
    }
    {$j\leftarrow 1$  $K$}{
        Update $\mathbf{c}_j$ to mean of points assigned to cluster $j$
    }
}
{$K$-means Clustering}

algorithm
"`

> *Think:* There is a geometry inside this algebra.
> Stack the cluster into one long vector in the product space $V^M$ and consider the subspace of constant tuples $(\mathbf{c},\ldots,\mathbf{c})$ — the diagonal.
> The identity says the closest constant tuple is $(\bar{\mathbf{x}},\ldots,\bar{\mathbf{x}})$: the mean is the orthogonal projection of the data onto the diagonal.

Why the mean?
Because the mean is what the norm demands.
For a cluster $\mathbf{x}_1,\ldots,\mathbf{x}_M$ with mean $\bar{\mathbf{x}}$ and any candidate center $\mathbf{c}$, expanding $\|\mathbf{x}_i - \mathbf{c}\|^2 = \|(\mathbf{x}_i - \bar{\mathbf{x}}) + (\bar{\mathbf{x}} - \mathbf{c})\|^2$ and summing gives

$$
\sum_{i=1}^M \|\mathbf{x}_i - \mathbf{c}\|^2 \;=\; \sum_{i=1}^M \|\mathbf{x}_i - \bar{\mathbf{x}}\|^2 \;+\; M\,\|\bar{\mathbf{x}} - \mathbf{c}\|^2 ,
$$

the cross terms vanishing because deviations from the mean sum to zero.
The right side is smallest exactly at $\mathbf{c} = \bar{\mathbf{x}}$: no other center can do better.

Each of Lloyd's moves lowers the objective — assignment by the definition of "nearest," update by the identity above — so the algorithm descends monotonically; and since only finitely many assignments of points to clusters exist, it must halt.
What it halts at is a local minimum of the objective, not always the best one: $K$-means is greedy descent, its destiny fixed by its starting centers.
Practitioners run it from several random starts and keep the winner.

> *Question:* how might one determine the number of clusters $K$ when it is not known a priori?
> This becomes a crucial issue in exploratory data analysis.

**Example 5.25 (Handwritten Digits).** The MNIST database of handwritten digits provides each image as a $28\times 28$ array of grayscale values, naturally viewed as a vector in $\mathbb{R}^{784}$.
Running $K$-means with $K=10$ produces cluster centers that resemble "prototype" digits, recovered by purely geometric means with no labels supplied.
The recovery is partial, and instructively so: some digits claim two prototypes while others are merged, because the geometry groups what *looks* alike, and a $1$ and a narrow $8$ can occupy neighboring regions of $\mathbb{R}^{784}$.

> *Foreshadowing:* in Chapter 10, the Singular Value Decomposition provides optimal low-dimensional representations of data, enabling more efficient clustering in very high dimensions.

**Example 5.26 (Color Compression).** A color image consists of points in $\mathbb{R}^3$, each an RGB triple.
Applying $K$-means with $K=16$ reduces the image to sixteen representative colors while preserving its essential features, the palette selected by the geometric distribution of the image's pixels in RGB space.

> *Foreshadowing:* eigenvectors of the graph Laplacian — Chapter 9 — split a network into natural groups that $K$-means, working from coordinates alone, might miss.

Nothing here required labels, gradients, or probability — only a norm, and behind the norm an inner product silently canceling the cross terms.
*Every average is an orthogonal projection.*

—

## Deep Networks & The Isometry of Depth

At the center of every layer of a neural network sits a matrix.
A layer is more than that matrix — it adds a constant vector, then bends the result through a nonlinear function applied one coordinate at a time — but the nonlinearity is fixed in advance, while the matrices are what must be filled with numbers before anything can be learned.
Those weight matrices, named in passing in Chapter 2, act as the linear transformations of Chapter 4 act: each takes the vector of numbers produced by the layer beneath it and returns the vector handed to the layer above.
The matrices of a network of depth $\Lambda$ thus assemble into a long product

$$
W_\Lambda W_{\Lambda-1}\cdots W_2 W_1 ,
$$

and it is this product that initialization sets.
Before any training, it holds nothing but random numbers.
The question of how to choose those numbers looks like a question about statistics and is in fact a question about isometry.

Consider the oldest recipe: fill each $W\in\mathbb{R}^{n\times n}$ with independent entries of mean zero and variance $1/n$.
The variance is not arbitrary.
For a unit vector $\mathbf{x}$, the $i$th coordinate of $W\mathbf{x}$ is the inner product of $\mathbf{x}$ with the $i$th row $\mathbf{w}_i$, a quantity of mean zero and variance $1/n$, so that summing over the $n$ coordinates gives

$$
\mathbb{E}\|W\mathbf{x}\|^2 \;=\; \sum_{i=1}^n \mathbb{E}\langle \mathbf{w}_i,\mathbf{x}\rangle^2 \;=\; n\cdot\frac{1}{n} \;=\; \|\mathbf{x}\|^2 .
$$

A layer so initialized preserves length on average.
That is the whole of what it does.

Averages conceal, and this one conceals a great deal.
Take $n=64$ and ask of a single such matrix for the longest and the shortest image of a unit vector.
In a typical draw some unit vector is stretched to length $1.93$ while some other is crushed to length $0.0063$.
The map preserves length on average and does nothing of the kind in any particular direction.

Compose such matrices and the disparity compounds, for the directions one factor favors are not the directions the next favors.
Longest and shortest images of a unit vector under the product, at width $64$, each figure the median of twenty independent draws:

$$
\begin{array}{r|ccc}
        \Lambda & 1 & 5 & 10 \\ \hline
        \text{longest} & 1.93 & 3.49 & 4.26 \\
        \text{shortest} & 6.3\times 10^{-3} & 1.5\times 10^{-7} & 5.9\times 10^{-14}
    \end{array}
$$

> *Think:* Why should the gap widen so fast?
> Each factor stretches some directions and shrinks others, and a direction shrunk by one is not spared by the next.
> The logarithms of the extreme stretches accumulate as a sum of independent contributions — a random walk — so the ratio grows geometrically in the depth.

Nothing has gone wrong with any individual factor: each $W_\ell$ is invertible, with probability one, and none is remarkable.
Yet by depth ten the longest and shortest images differ by a factor near $10^{14}$, and by depth twenty the shortest has fallen below what double-precision arithmetic can even report.
At width $256$ the collapse arrives sooner: at depth ten the shortest image is already past the resolution of the machine.
In exact arithmetic the product remains invertible.
In any computation it does not.
*Depth manufactures a kernel out of factors that have none.*

There is an alternative, and Section 5.5 has already proved that it works.
Let each $W_\ell$ be an orthogonal matrix.
Then every unit vector has unit image (Lemma 5.19), and since the composition of orthogonal transformations is orthogonal, the same holds of the product — at every depth, for every direction, exactly.
Run the experiment again and both rows of the table read $1.000000000000$ at every $\Lambda$, not approximately and not by luck, but because $O(n)$ is closed under multiplication.
Depth, so initialized, disturbs nothing.

An orthogonal layer is the extreme case about which the Fundamental Theorem has nothing to report: kernel trivial, image everything, no defect anywhere.
The absence is the useful property, since a map that loses nothing may be repeated without limit.

A layer that narrows cannot be so fortunate.
Suppose $W\in\mathbb{R}^{64\times 256}$ with $WW^T=I_{64}$, so that its rows $\mathbf{w}_1,\ldots,\mathbf{w}_{64}$ are orthonormal, and extend them to an orthonormal basis of $\mathbb{R}^{256}$.
Lemma 5.7 then reads every length twice over:

$$
\|\mathbf{x}\|^2 = \sum_{i=1}^{256}\langle \mathbf{w}_i,\mathbf{x}\rangle^2
    \quad : \quad
    \|W\mathbf{x}\|^2 = \sum_{i=1}^{64}\langle \mathbf{w}_i,\mathbf{x}\rangle^2
$$

> *Foreshadowing:* $\operatorname{span}\{\mathbf{w}_1,\ldots,\mathbf{w}_{64}\}$ and $\operatorname{ker} W$ stand perpendicular, one the whole of what survives and the other the whole of what is lost.
> Chapter 6 names that pairing and finds it everywhere.

The first $64$ coefficients are kept and the remaining $192$ discarded, so that $\|W\mathbf{x}\|\leq\|\mathbf{x}\|$, with equality exactly when $\mathbf{x}$ lies in the span of the rows; the other $192$ basis vectors span $\operatorname{ker} W$.
No choice of $W$ avoids this, orthonormal rows or not: $192$ dimensions must go somewhere.
What orthonormality guarantees is not that nothing is lost but that nothing else is: lengths survive undiminished on the directions that survive at all.

Manufacturing a random orthogonal matrix is a use for the chapter's last factorization.
Fill $G\in\mathbb{R}^{n\times n}$ with independent normal entries and factor $G=QR$ (Definition 5.22); the factor $Q$ is orthogonal, and $G$ is nonsingular with probability one, so Lemma 5.24 applies.
One correction is required, and it is the very normalization under which that lemma asserts uniqueness.
A factorization routine returns the diagonal of $R$ with whatever signs its own arithmetic produced; multiply $Q$ on the right by $\operatorname{diag}(\operatorname{sign} r_{ii})$ to force those signs positive, and the result is distributed uniformly over $O(n)$.
Neglect the correction and the sampling inherits the routine's private conventions instead.

> *Nota bene:* This is what the standard software means by orthogonal initialization: a Gaussian matrix, a QR factorization, a sign convention enforced.
> The practice and its analysis are due to Saxe, McClelland & Ganguli (2014), who called the property *dynamical isometry*.

None of it survives contact with the nonlinearity, and none of it was meant to.
Between the matrices sits a function whose slope varies from coordinate to coordinate; whatever it contributes to the product is not orthogonal, and training moves every $W_\ell$ off the orthogonal group at the first step.
Isometry here is a condition of birth rather than a state of grace.

> *Caveat:* Some activations are more destructive than others.
> A rectifier, which zeroes about half of what it is handed, cannot be repaired by any choice of matrix; practitioners multiply $Q$ by a gain factor, restoring in scale what has been surrendered in geometry.

> *Foreshadowing:* Training computes its corrections by sweeping a derivative backward through this same product, transposed — and transposition is adjunction (Definition 5.10), since $(AB)^T=B^TA^T$.
> An orthogonal factor is its own inverse there as well, so a geometry chosen to protect the forward signal protects the backward one too.
> Chapter 13 makes that sweep explicit.

What the orthogonal start secures is not a trained network but a trainable one.
At birth no direction of the input has already been lost, and none of the correction that must travel back through the same matrices has been lost either.
Everything afterward depends on what the layers learn.
*What one layer distorts, depth compounds.*

—

## Exercises: Chapter 5

1. Consider the inner product on $\mathcal{P}_2$ given by $\langle f,g\rangle = \int_0^1 f(x)g(x)\,dx$.
Find the norm of $p(x)=1+2x+x^2$.
Factor $p$ before integrating.

2. Let $V$ be the space of $2\times 2$ matrices with the Frobenius inner product of Example 5.3.
Find the angle between $A=\begin{bmatrix}1 & 0\\0 & 1\end{bmatrix}$ and $B=\begin{bmatrix}1 & -1\\1 & 1\end{bmatrix}$.

3. Let $\mathbf{u}=(1,2,2)^T$ and $\mathbf{v}=(3,3,0)^T$.
Find an orthonormal basis for $\operatorname{span}\{\mathbf{u},\mathbf{v}\}$ by Gram-Schmidt.
Extend it to an orthonormal basis of $\mathbb{R}^3$ by solving $\mathbf{u}^T\mathbf{w}=\mathbf{v}^T\mathbf{w}=0$ and normalizing.
Your $\mathbf{w}$ is fixed only up to sign; choose the sign making $\det Q=1$ for the resulting matrix $Q$, and verify $Q^TQ=I$.

4. Let $C([0,2\pi])$ carry $\langle f,g\rangle = \int_0^{2\pi} f(x)g(x)\,dx$.
Show that $\{1,\cos x,\sin x\}$ is orthogonal but not orthonormal, and find the scalings that make it orthonormal.
Example 5.8 asserts a larger orthogonality on $[-\pi,\pi]$ without proving any of it; prove the part that falls to the symmetry of the interval alone, namely that $\cos(mx)\perp\sin(nx)$ for all integers $m\geq 0$ and $n\geq 1$.
Why must $n=0$ be excluded?

5. Find the QR decomposition of

$$
A = \begin{bmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{bmatrix}
$$

by Gram-Schmidt on its columns, and verify $A=QR$ and $Q^TQ=I_2$.
Then compute $QQ^T$ and observe that it is not $I_3$.
Say in one sentence why $Q$ is nonetheless the factor Definition 5.22 asks for.

6. Find an orthonormal basis $\{B_1,B_2,B_3\}$ for the space $\operatorname{sym}_2$ of symmetric $2\times2$ matrices under the Frobenius inner product.
Expand $A=\begin{bmatrix}3 & 1\\1 & -2\end{bmatrix}$ in it using $c_i = \langle A,B_i\rangle$, and confirm that $\|A\|^2 = c_1^2+c_2^2+c_3^2$.

7. Show that $\langle f,g\rangle = f(0)g(0) + f(1)g(1)$ is an inner product on $\mathcal{P}_1$, and find a polynomial orthogonal to $p(x)=x$.
Then show that the same formula is *not* an inner product on $\mathcal{P}_2$, and account for the failure by comparing $\dim\mathcal{P}_2$ with the number of evaluation points.

8. Lemma 5.5 claims equality exactly when one vector is a scalar multiple of the other, and its proof disposes of that claim in a single sentence.
Supply the argument: assuming $\mathbf{v}\neq\mathbf{0}$ and equality, show that $q(t)=\|\mathbf{u}+t\mathbf{v}\|^2$ has a repeated root, identify the root, and conclude.
Then take $\mathbf{v}=\mathbf{0}$ and show that this argument says nothing there, though equality holds — which is why the lemma reads "one vector is a multiple of the other" rather than $\mathbf{u}=c\mathbf{v}$.

9. Let $Q$ be a $2\times 2$ orthogonal matrix.
Its first column is a unit vector, and in $\mathbb{R}^2$ exactly two unit vectors are perpendicular to a given one.
Conclude that $Q$ is either $\begin{bmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{bmatrix}$ or $\begin{bmatrix}\cos\theta & \sin\theta\\ \sin\theta & -\cos\theta\end{bmatrix}$, according to the sign of $\det Q$, and find the line the second one fixes.

10. Let $\mathbf{v}\in\mathbb{R}^n$ be nonzero.
Show that the projection $\Pi_{\mathbf{v}}\mathbf{u} = \frac{\langle \mathbf{u},\mathbf{v}\rangle}{\|\mathbf{v}\|^2}\mathbf{v}$ of Section 5.3 is given by the matrix $\mathbf{v}\mathbf{v}^T/\mathbf{v}^T\mathbf{v}$, and deduce that it is symmetric and that projecting twice is the same as projecting once.
Then prove symmetry a second time without coordinates, by verifying that $\Pi_{\mathbf{v}}$ is its own adjoint.

11. The Gram matrix of vectors $\mathbf{v}_1,\ldots,\mathbf{v}_n$ in an inner product space has entries $g_{ij}=\langle \mathbf{v}_i,\mathbf{v}_j\rangle$.
Show that $G$ is symmetric, and that $G$ is singular if and only if the $\mathbf{v}_i$ are linearly dependent.
Positive definiteness is used in exactly one of the two directions; say which, and then exhibit a pairing on $\mathbb{R}^2$ that has the other two axioms but not this one, together with two independent vectors for which the claim fails.

12. Show that $\langle f,g\rangle = \int_0^1 f'(x)g'(x)\,dx$ is not an inner product on $\mathcal{P}_3$ by exhibiting a nonzero $f$ with $\langle f,f\rangle = 0$; as in Exercise 7, the axiom that fails is the third.
Show that it *is* an inner product on $W=\{f\in\mathcal{P}_3 : f(0)=0\}$, and find the polynomial in $W$ orthogonal to both $x$ and $x^2$.
Is it unique up to scaling?

    > *Compare:* The derivative of your answer is the Legendre polynomial $P_2$ of Section 5.3, rescaled from $[-1,1]$ to $[0,1]$.
    > Orthogonality under $\int f'g'$ is ordinary orthogonality of the derivatives.

13. Show that rotation by $\pi/2$ in $\mathbb{R}^2$ satisfies $\langle T\mathbf{v},\mathbf{v}\rangle = 0$ for every $\mathbf{v}$ without being the zero transformation.
Now let $T$ act on a finite-dimensional inner product space and prove that $\langle T\mathbf{v},\mathbf{v}\rangle = 0$ for all $\mathbf{v}$ exactly when $T^*=-T$, by expanding $\langle T(\mathbf{u}+\mathbf{v}),\mathbf{u}+\mathbf{v}\rangle$.
Deduce that the only such $T$ that is also self-adjoint is $T=0$.

    > *Nota bene:* over complex scalars the counterexample disappears and the naive claim $T=0$ becomes a theorem.
    > The whole difference is that a real inner product sees only the symmetric part of $T$.

14. Prove that the norm induced by any inner product satisfies $\|\mathbf{u}+\mathbf{v}\|^2 + \|\mathbf{u}-\mathbf{v}\|^2 = 2(\|\mathbf{u}\|^2+\|\mathbf{v}\|^2)$, and say which of the three axioms of Definition 5.1 you used.
Now evaluate both sides at $\mathbf{u}=(1,0)^T$ and $\mathbf{v}=(0,1)^T$ in $\mathbb{R}^2$, first under $\|\mathbf{w}\|_1 = |w_1|+|w_2|$ and then under $\|\mathbf{w}\|_\infty = \max(|w_1|,|w_2|)$.
Conclude that neither norm comes from an inner product — the claim Section 5.2 closes with and does not argue.

15. Section 5.2 observes that orthogonal vectors obey $\|\mathbf{u}+\mathbf{v}\|^2 = \|\mathbf{u}\|^2+\|\mathbf{v}\|^2$.
Prove the converse over $\mathbb{R}$: whenever that identity holds, $\mathbf{u}\perp\mathbf{v}$.
Then explain why Lemma 5.7 insists its vectors be nonzero, by producing a set for which the norm identity survives and linear independence does not.

16. Under $\langle f,g\rangle = \int_0^1 fg\,dx$ the functions $f(x)=x$ and $g(x)=1-x$ meet at exactly $60^\circ$.
Find the angle between them on $C^1([0,1])$ under $\langle f,g\rangle = \int_0^1 (fg + f'g')\,dx$ instead, and observe that it is now obtuse.
Say what the derivative term is measuring that reverses the verdict.

17. Two struts meet at a joint, and the loads they carry solve

$$
\begin{bmatrix}2 & 1\\2 & 3\end{bmatrix}\mathbf{x} = \begin{bmatrix}4\\8\end{bmatrix} .
$$

Factor the matrix as $QR$ by Gram-Schmidt, then solve $R\mathbf{x}=Q^T\mathbf{b}$ by back-substitution instead of by elimination.
Explain why the inverse of $Q$ never has to be computed, and why that is the whole appeal of the method when the same joint must be re-solved for many loads.

18. Three documents are encoded as the unit vectors $\frac{1}{\sqrt2}(1,1,0,0)^T$, $\frac{1}{\sqrt2}(1,0,1,0)^T$ and $\frac{1}{\sqrt2}(0,0,1,1)^T$ over a four-word vocabulary.
Assemble them as the columns of $X$ and compute the Gram matrix $G=X^TX$ of Exercise 11.
Identify the pair sharing no vocabulary, and the two pairs that are equally aligned.
Say why the entries of $G$ are cosine similarities here but would not be if the columns were left unnormalized.

19. Three instruments measure the same quantity with standard deviations $1$, $2$ and $5$ in their own units.
Weighting the $i$th coordinate by $1/\sigma_i^2$ produces a weighted inner product as in Example 5.2.
Show that the residuals $(0,0,5)^T$ and $(1,0,0)^T$ have Euclidean lengths in the ratio $5:1$ but identical lengths under this inner product, and find the three unit vectors lying along the positive coordinate axes.
Which of the two norms should decide whether a fit is good?

20. A depot placed at $\mathbf{c}$ serves sites $\mathbf{x}_1,\ldots,\mathbf{x}_M$ at a cost of $\sum_i \|\mathbf{x}_i - \mathbf{c}\|^2$, and the clustering discussion later in this chapter shows the mean $\bar{\mathbf{x}}$ is the best $\mathbf{c}$.
Show that the resulting minimum cost is $\sum_i\|\mathbf{x}_i\|^2 - M\|\bar{\mathbf{x}}\|^2$, and evaluate it for the four sites $(0,0)$, $(2,0)$, $(0,2)$, $(2,2)$.
Then show that squaring is doing real work: for the three sites $0$, $1$, $10$ on a line, the mean does *not* minimize the unsquared total $\sum_i|x_i-c|$.

21. (Challenge.) For a nonzero $\mathbf{a}$ in a real inner product space, define $T\mathbf{x} = \mathbf{x} - 2\Pi_{\mathbf{a}}\mathbf{x}$.
Prove that $T$ preserves inner products, that $T\mathbf{a}=-\mathbf{a}$ while $T$ fixes everything perpendicular to $\mathbf{a}$, and that on $\mathbb{R}^n$ its matrix is $I - \frac{2}{\|\mathbf{a}\|^2}\mathbf{a}\mathbf{a}^T$.
Then show that every $2\times2$ orthogonal matrix of negative determinant arises this way, closing the second case of Exercise 9.

22. (Challenge.) Prove the uniqueness half of Lemma 5.24: a nonsingular $A$ has exactly one QR decomposition whose $R$ has positive diagonal entries.
Reduce this to showing that a matrix which is orthogonal, upper triangular, and positive on the diagonal must be the identity, and prove that by working down the columns.

---


# Chapter 6. Orthogonal Decomposition & Data

*"quadrangular the building rose the heavens squared by a line"*

**The marriage of geometry and algebra** reaches its first culmination in the notion of orthogonality.
The inner product structure we have built transforms our understanding of the fundamental spaces and operations from Chapter 3.
What was mere algebra — kernels and images, quotients and complements — acquires geometric meaning through perpendicularity.
This geometric perspective not only illuminates the theory but guides computation, leading to optimal methods for solving systems and fitting data.

Our task is to reexamine the foundations of earlier chapters, now with a right angle in hand.
The kernel of a transformation stands perpendicular to its coimage.
Quotient spaces induce orthogonal decompositions.
The Fundamental Theorem itself expresses not merely dimensional accounting but geometric splitting of domain and codomain into perpendicular factors.

> *Foreshadowing:* The orthogonal projections studied here form the theoretical foundation for dimensionality reduction in machine learning, where high-dimensional data is projected onto lower-dimensional subspaces that capture essential features.

This geometric reinterpretation bears immediate practical fruit.
When exact solutions to linear systems do not exist, orthogonal projections provide best approximations under natural measures of error.
Data corrupted by noise finds clean representation through projection onto suitable subspaces.
The abstract machinery of inner products descends from theory to practice, offering optimal methods for a host of engineering problems.

The path ahead revisits familiar territory with new eyes: the four fundamental spaces reinterpreted through orthogonality, projection operators as the workhorses of decomposition, the Fundamental Theorem as the expression of orthogonal splitting.
The machinery then turns practical, yielding optimal solutions of overdetermined systems through least squares.

## 6.1 Orthogonal Subspaces & Complements

The vector spaces we have studied thus far acquire richer structure through the inner product geometry of Chapter 5.
Just as individual vectors may stand perpendicular to one another, entire subspaces can be orthogonal, leading to natural geometric decompositions.

**Definition 6.1 (Orthogonal Complement).** Two subspaces $U,W$ of an inner product space $V$ are **orthogonal**, denoted $U\perp W$, if every vector in one is orthogonal to every vector in the other:

$$
\langle \mathbf{u},\mathbf{w}\rangle = 0 \quad\text{for all }\mathbf{u}\in U,\ \mathbf{w}\in W
$$

The **orthogonal complement** of a subspace $U<V$, denoted $U^\perp$, is the subspace of all vectors orthogonal to $U$:

$$
U^\perp = \{\mathbf{v}\in V : \langle \mathbf{v},\mathbf{u}\rangle = 0\text{ for all }\mathbf{u}\in U\}
$$

That $U^\perp$ is indeed a subspace follows readily from properties of the inner product: the zero vector is certainly orthogonal to all of $U$, and linear combinations of vectors orthogonal to $U$ remain orthogonal to $U$.

Complementarity and orthogonality together deserve a symbol of their own: when subspaces $U$ and $W$ are both complementary ($V=U\oplus W$) and orthogonal ($U\perp W$), we write $V=U\boxplus W$ and speak of an **orthogonal direct sum**.

**Lemma 6.2.** For $V$ a finite-dimensional inner product space and any $U<V$:

1. $(U^\perp)^\perp = U$

2. $\dim U + \dim U^\perp = \dim V$

3. $U\cap U^\perp = \{\mathbf{0}\}$

4. $V = U\boxplus U^\perp$

*Proof.* Choose an orthonormal basis $\{\mathbf{u}_1,\ldots,\mathbf{u}_k\}$ for $U$ and extend it to a basis of $V$, which Gram-Schmidt renders orthonormal without disturbing the first $k$ vectors.
Any $\mathbf{v}\in V$ expands as $\mathbf{v}=\sum_i\langle\mathbf{v},\mathbf{u}_i\rangle\mathbf{u}_i$, and $\mathbf{v}\perp U$ holds precisely when the first $k$ coefficients vanish; hence $U^\perp=\operatorname{span}\{\mathbf{u}_{k+1},\ldots,\mathbf{u}_n\}$, which is property 2.
Property 3 is immediate, since a vector orthogonal to itself is $\mathbf{0}$, and property 4 follows by splitting that same expansion at index $k$.
For property 1, the inclusion $U\subseteq(U^\perp)^\perp$ is clear from the definitions, while applying property 2 to $U^\perp$ gives $\dim(U^\perp)^\perp = \dim V - \dim U^\perp = \dim U$; a subspace containing $U$ and of the same finite dimension is $U$. ∎

The last property is especially significant: every vector in $V$ decomposes uniquely into orthogonal components lying in $U$ and $U^\perp$.
This $\boxplus$-decomposition will prove fundamental to our development of projection operators in the next section.

**Example 6.3 (Matrix Subspaces).** Consider the space $\mathbb{R}^{n\times n}$ with the Frobenius inner product $\langle A,B\rangle = \operatorname{tr}(A^TB)$ from Example 5.3.
The subspace $\operatorname{sym}_n$ of symmetric matrices and the subspace $\operatorname{skew}_n$ of skew-symmetric matrices are orthogonal complements:

$$
\mathbb{R}^{n\times n} = \operatorname{sym}_n \boxplus \operatorname{skew}_n
$$

$$
\operatorname{sym}_n = \{A : A^T = A\} \quad\text{and}\quad \operatorname{skew}_n = \{A : A^T = -A\}
$$

This orthogonal decomposition reveals that any matrix $A$ splits uniquely into symmetric and skew-symmetric parts:

$$
A = \frac{A + A^T}{2} + \frac{A - A^T}{2}
$$

This decomposition has important applications in mechanics, where symmetric matrices often represent stress and strain.

The geometric perspective offered by orthogonal complements will transform our understanding of the fundamental subspaces from Chapter 3.
What appeared there as purely algebraic constructions — kernels and images, quotients and duals — will acquire new geometric meaning through orthogonality.

## 6.2 Projections & Quotients

The concept of projection pervades mathematics and engineering.
A shadow cast by sunlight projects three-dimensional objects onto the plane; a surveyor's map projects the curved surface of Earth onto flat paper; a statistician projects high-dimensional data onto informative lower-dimensional summaries.
These diverse examples share a common mathematical essence: the approximation of complex objects by simpler ones through systematic dimension reduction.

The inner product structure we have built transforms this intuitive notion into precise mathematics.
Given a subspace $W < V$, we seek to approximate arbitrary vectors in $V$ by their "shadows" in $W$  — vectors that minimize the distance to the original while lying entirely in $W$.
This geometric problem leads directly to orthogonal projection, a concept that unifies the theoretical structure of Chapter 3 with the computational methods of modern data analysis.

**Definition 6.4 (Orthogonal Projection).** Let $W < V$ be a subspace of an inner product space.
The **orthogonal projection** onto $W$ is the linear transformation $\Pi_{W}:V\to V$ satisfying:

1. $\Pi_{W}\mathbf{v} \in W$ for all $\mathbf{v}\in V$ (projects onto $W$)

2. $\mathbf{v} - \Pi_{W}\mathbf{v} \perp W$ for all $\mathbf{v}\in V$ (projects orthogonally)

> *Nota bene:* The projection $\Pi_{W}$ is uniquely determined by these properties.
> Though other transformations might map vectors into $W$, only orthogonal projection maintains perpendicularity of the error.

This abstract definition encodes a powerful optimization principle: $\Pi_{W}\mathbf{v}$ provides the best approximation to $\mathbf{v}$ within $W$ under the natural distance measure induced by the inner product.

**Lemma 6.5 (Best Approximation).** For any $\mathbf{v}\in V$ and $\mathbf{w}\in W$:

$$
\|\mathbf{v} - \Pi_{W}\mathbf{v}\| \leq \|\mathbf{v} - \mathbf{w}\|
$$

with equality if and only if $\mathbf{w} = \Pi_{W}\mathbf{v}$.

*Proof.* For any $\mathbf{w}\in W$, the error vector $\mathbf{v} - \mathbf{w}$ decomposes into orthogonal components:

$$
\mathbf{v} - \mathbf{w} = (\mathbf{v} - \Pi_{W}\mathbf{v}) + (\Pi_{W}\mathbf{v} - \mathbf{w})
$$

where the first term is orthogonal to $W$ and the second lies in $W$.
By the Pythagorean theorem:

$$
\|\mathbf{v} - \mathbf{w}\|^2 = \|\mathbf{v} - \Pi_{W}\mathbf{v}\|^2 + \|\Pi_{W}\mathbf{v} - \mathbf{w}\|^2
$$

The right term vanishes precisely when $\mathbf{w} = \Pi_{W}\mathbf{v}$. ∎

When $W$ has an orthonormal basis $\{\mathbf{w}_1,\ldots,\mathbf{w}_k\}$, the projection collapses to a formula:

$$
\Pi_{W}\mathbf{v} = \sum_{i=1}^k \langle \mathbf{v},\mathbf{w}_i\rangle\mathbf{w}_i
$$

These are the orthonormal coordinates of Chapter 5, read off rather than solved for.
This formula reveals projection as a type of spectral decomposition, extracting from $\mathbf{v}$ precisely those components aligned with $W$'s basis vectors.

**Example 6.6 (Signal Processing).** Consider the space $V = C([-\pi,\pi])$ of continuous functions on $[-\pi,\pi]$ with the $L^2$ inner product of Example 5.8.
The subspace $W$ spanned by $\{1,\cos x,\sin x\}$ captures the DC and first harmonic components of signals.
The projection $\Pi_{W}$ implements a basic low-pass filter, approximating arbitrary signals by their first Fourier components.
The error $\mathbf{v} - \Pi_{W}\mathbf{v}$ represents higher-frequency content filtered out by the projection.

Projection operators possess several properties that illuminate their geometric and algebraic character:

**Lemma 6.7 (Projection Properties).** The orthogonal projection $\Pi_{W}$ onto a subspace of a finite-dimensional inner product space $V$ satisfies:

1. Idempotence: $\Pi_{W}^2 = \Pi_{W}$

2. Self-adjointness: $\Pi_{W}^* = \Pi_{W}$

3. Complementarity: $\mathrm{id}_V - \Pi_{W} = \Pi_{W^\perp}$

where $W^\perp$ denotes the orthogonal complement of $W$.

*Proof.* By Lemma 6.2 each $\mathbf{v}\in V$ splits uniquely as $\mathbf{v}=\mathbf{v}_W+\mathbf{v}_\perp$ with $\mathbf{v}_W\in W$ and $\mathbf{v}_\perp\in W^\perp$, and Definition 6.4 says precisely that $\Pi_{W}\mathbf{v}=\mathbf{v}_W$.
A vector $\mathbf{w}\in W$ has splitting $\mathbf{w}+\mathbf{0}$, so $\Pi_{W}\mathbf{w}=\mathbf{w}$; applying this to $\mathbf{w}=\Pi_{W}\mathbf{v}$ gives idempotence.
For complementarity, $\mathbf{v}-\Pi_{W}\mathbf{v}=\mathbf{v}_\perp$, and since $(W^\perp)^\perp=W$ the splitting of $\mathbf{v}$ relative to $W^\perp$ is $\mathbf{v}_\perp+\mathbf{v}_W$, whence $\mathbf{v}_\perp=\Pi_{W^\perp}\mathbf{v}$.
For self-adjointness, the cross terms drop out of

$$
\langle\Pi_{W}\mathbf{u},\mathbf{v}\rangle = \langle\mathbf{u}_W,\mathbf{v}_W+\mathbf{v}_\perp\rangle = \langle\mathbf{u}_W,\mathbf{v}_W\rangle = \langle\mathbf{u}_W+\mathbf{u}_\perp,\mathbf{v}_W\rangle = \langle\mathbf{u},\Pi_{W}\mathbf{v}\rangle .
$$

 ∎

These properties reflect the geometric nature of projection — applying it twice has no additional effect; it respects the inner product structure; and it decomposes space into orthogonal pieces.
The last property provides particular insight: projection onto $W$ and projection onto $W^\perp$ split any vector into complementary components.

> *Foreshadowing:* This decomposition principle will reach its full power in Chapter 10, where the Singular Value Decomposition provides an optimal sequence of orthogonal projections for approximating data.

This splitting illuminates our earlier study of quotient spaces.
When we quotient a finite-dimensional $V$ by a subspace $U$, each equivalence class consists of vectors differing by elements of $U$.
Orthogonality lets us represent each class by its projection onto $U^\perp$  — the unique member of that class of least norm.
The projection $\Pi_{U^\perp}$ therefore descends to an isomorphism $V/U\cong U^\perp$, inverse to the composite $U^\perp\hookrightarrow V\rightarrow V/U$ that includes and then quotients.

> *Nota bene:* finite-dimensionality is not decoration here.
> In a function space a coset can contain no shortest vector at all; the exercises exhibit a subspace of $C([0,1])$ whose orthogonal complement is trivial.

Quotient spaces and orthogonal complements are thus two presentations of one object: the effective domain of a linear transformation.

**Example 6.8 (Data Centering).** Consider a collection of vectors $\{\mathbf{x}_1,\ldots,\mathbf{x}_n\}$ in $\mathbb{R}^d$.
The subspace $U$ spanned by $\mathbf{1} = (1,\ldots,1)^T$ represents uniform translations.
Projecting onto $U^\perp$ centers the data by subtracting means — a fundamental preprocessing step in data analysis.
The quotient $\mathbb{R}^d/U$ captures the intrinsic shape of the data cloud independent of its absolute position.

The power of orthogonal projection extends far beyond these elementary examples.
When exact solutions to linear systems do not exist, projection onto appropriate subspaces yields optimal approximations.
When data contains noise, projection onto signal subspaces enables filtering and compression.
When complex systems require simplified models, projection onto lower-dimensional spaces balances accuracy and complexity.
These applications, and many more, spring from the simple geometric principle encoded in Definition 6.4.

## 6.3 The Fundamental Theorem Redux

The Fundamental Theorem of Linear Algebra, when viewed in finite-dimensional inner product spaces, reveals deeper structure through the lens of orthogonality.
What first appeared as a collection of dimensional relationships now emerges in its true form: a statement about the geometric splitting of spaces.
This geometric understanding, though restricted to the finite-dimensional setting, transforms our perspective on linear transformations, providing both theoretical insight and practical methods for computation.

Recall the orthogonal direct sum notation $\boxplus$ of Section 6.1.

**Theorem 6.9 (Fundamental Theorem of Linear Algebra (Geometric Form)).** Any linear transformation $T:V\rightarrow W$ between finite-dimensional inner product spaces induces orthogonal decompositions of both domain and codomain:

$$
V = \operatorname{ker} T \boxplus (\operatorname{ker} T)^\perp \qquad\text{and}\qquad W = \operatorname{im} T \boxplus (\operatorname{im} T)^\perp \tag{6.1}
$$

These decompositions are connected by the following:

> *Terminology:* The term **naturally isomorphic** here means that the isomorphisms arise from the geometric structure itself.

1. The restriction of $T$ to $(\operatorname{ker} T)^\perp$ gives an isomorphism $(\operatorname{ker} T)^\perp \cong \operatorname{im} T$

2. The coimage $V/\operatorname{ker} T$ is naturally isomorphic to $\operatorname{im} T$

3. The cokernel $W/\operatorname{im} T$ is naturally isomorphic to $(\operatorname{im} T)^\perp$

4. $T\Pi_{(\operatorname{ker} T)^\perp} = T = \Pi_{\operatorname{im} T}T$: discarding an input's kernel component changes nothing, and the output was already in the image

*Proof.* The two decompositions are Lemma 6.2 applied to $\operatorname{ker} T<V$ and to $\operatorname{im} T<W$.
For clause 1, the restriction of $T$ to $(\operatorname{ker} T)^\perp$ has kernel $(\operatorname{ker} T)^\perp\cap\operatorname{ker} T=\{\mathbf{0}\}$, hence is injective; and it is onto $\operatorname{im} T$, since any $T\mathbf{v}$ equals $T$ of the $(\operatorname{ker} T)^\perp$-component of $\mathbf{v}$.
Clause 4 records that last observation and its companion, that $T\mathbf{v}$ lies in $\operatorname{im} T$, where $\Pi_{\operatorname{im} T}$ acts as the identity.
Clause 2 is the isomorphism $V/\operatorname{ker} T\cong(\operatorname{ker} T)^\perp$ of the previous section composed with clause 1, and clause 3 is the same construction applied to $\operatorname{im} T<W$: the projection $\Pi_{(\operatorname{im} T)^\perp}$ descends to $W/\operatorname{im} T$.
Naturality in each case means only that no choice of basis was made. ∎

These decompositions illuminate the four fundamental subspaces through geometry rather than algebra.
The kernel represents vectors invisible to $T$; its orthogonal complement captures the effective inputs.
The image contains all possible outputs; its orthogonal complement measures the transformation's deficiency.
Each complementary pair provides a complete view of how $T$ acts on its domain and codomain.

**Example 6.10 (Matrix Transformations).** For a matrix $A\in\mathbb{R}^{m\times n}$, these decompositions acquire immediate computational significance once we name the concrete realizations of the four spaces.
The coimage $(\operatorname{ker} A)^\perp$ is realized as $\operatorname{row}(A)$ (classically the **row space**, the span of the rows) — which is precisely $\operatorname{im}(A^T)$: the adjoint of Chapter 5, standing perpendicular to the kernel, exactly as promised; the image is $\operatorname{col}(A)$ (classically the **column space**); and the cokernel $(\operatorname{im} A)^\perp$ is realized as $\operatorname{ker}(A^T)$ (classically the **left null space**).

1. $\mathbb{R}^n = \operatorname{ker}(A) \boxplus \operatorname{row}(A)$ splits the input space into kernel and coimage

2. $\mathbb{R}^m = \operatorname{col}(A) \boxplus \operatorname{ker}(A^T)$ splits the output space into image and cokernel

3. The projections $\Pi_{\operatorname{row}(A)}$ and $\Pi_{\operatorname{col}(A)}$ provide optimal approximate solutions when exact solutions do not exist

> *Recall:* The orthogonal complements appearing here recall the orthogonal matrices of Chapter 5, where entire transformations preserve perpendicularity.

These geometric splittings yield the algebraic relationships of Chapter 3 as corollaries:

**Corollary 6.11 (Rank-Nullity Redux).** For a linear transformation $T:V\rightarrow W$ between finite-dimensional inner product spaces:

1. $\dim V = \dim\operatorname{ker} T + \dim\operatorname{im} T$

2. $\dim W = \dim\operatorname{im} T + \dim\operatorname{coker} T$

3. $\dim\operatorname{im} T = \dim(\operatorname{ker} T)^\perp$

Each is a dimension count on a decomposition already established.
Clause 3 is clause 1 of the theorem, an isomorphism forcing equal dimensions; clause 1 then follows by substituting it into $\dim V=\dim\operatorname{ker} T+\dim(\operatorname{ker} T)^\perp$, which is Lemma 6.2(2); and clause 2 is the same argument in $W$, since clause 3 of the theorem identifies $\operatorname{coker} T$ with $(\operatorname{im} T)^\perp$, of dimension $\dim W-\dim\operatorname{im} T$.
What before seemed like mysterious algebraic coincidences now emerge as natural consequences of geometric splitting.

This geometric perspective guides computation. When solving $T\mathbf{v}=\mathbf{w}$:

1. Project $\mathbf{w}$ onto $\operatorname{im} T$ to test solvability

2. If solvable, find a particular solution in $(\operatorname{ker} T)^\perp$

3. If unsolvable, project onto $\operatorname{im} T$ for best approximation

Chapter 4 read the Fundamental Theorem as a normal form; the inner product reads it as a geometry: four subspaces, two perpendicular splittings, one isomorphism between them.

## 6.4 The Pseudoinverse

The Fundamental Theorem of Linear Algebra revealed how any linear transformation induces four fundamental subspaces, connected through orthogonal decomposition of domain and codomain.
This structure suggests a natural question: can we define a reverse transformation that somehow undoes the action of our original map while respecting these geometric relationships?

The Fundamental Theorem has already answered this, though not in these words.
Theorem 6.9 says that $T$, once the directions it destroys are set aside, restricts to an isomorphism $(\operatorname{ker} T)^{\perp}\cong\operatorname{im} T$  — the coimage, in the realization that theorem supplies; whatever a linear map does beyond annihilating and failing to reach happens there and nowhere else.
Run that isomorphism backwards and extend it by zero on the cokernel — which the same theorem realizes as $(\operatorname{im} T)^{\perp}$  — and one obtains a map $W\rightarrow V$ that undoes $T$ wherever undoing is possible and does nothing where it is not.
That map is the **pseudoinverse**.
The four conditions below are this sentence written in algebra, and what they add is uniqueness: no other map satisfies all four.
{ $T^{\dagger}$ inverts the isomorphism at the heart of $T$ and forgets the rest.}

**Definition 6.12 (Pseudoinverse).** For a linear transformation $T:V\rightarrow W$ between finite-dimensional inner product spaces, the pseudoinverse (or **Moore-Penrose inverse**) $T^{\dagger}:W\rightarrow V$ is the unique linear transformation satisfying all of the following conditions:

1. $TT^{\dagger}T = T$   (First consistency condition)

2. $T^{\dagger}TT^{\dagger} = T^{\dagger}$   (Second consistency condition)

3. $(TT^{\dagger})^* = TT^{\dagger}$   (First adjoint condition)

4. $(T^{\dagger}T)^* = T^{\dagger}T$   (Second adjoint condition)

where $^*$ denotes the adjoint operation with respect to the inner products on $V$ and $W$.

Each condition records a piece of the geometry just described.
Set against the Fundamental Theorem, the pseudoinverse is assembled from orthogonal projections onto the four fundamental subspaces:

*[Figure omitted: $T$ projects onto $(\operatorname{ker} T)^{\perp}$, then maps isomorphically onto $\operatorname{im} T$; $T^{\dagger}$ reverses both steps, projecting onto $\operatorname{im} T$ and mapping isomorphically back.]*

For matrices, the pseudoinverse can be written in closed form.
When $A$ has full column rank, its pseudoinverse is:

$$
A^{\dagger} = (A^TA)^{-1}A^T
$$

This formula connects directly to the orthogonal projections studied earlier in this chapter.
The invertibility of $A^TA$ is exactly the condition that $A$ have full column rank, because $\operatorname{ker}(A^TA)=\operatorname{ker} A$; Exercise 8 proves this and builds the projection $A(A^TA)^{-1}A^T$ from it.
When $A$ has full row rank, the pseudoinverse becomes:

$$
A^{\dagger} = A^T(AA^T)^{-1}
$$

These formulas illustrate how the pseudoinverse generalizes the concept of matrix inversion to rectangular matrices, providing the best possible approximate inverse when an exact inverse does not exist.

**Example 6.13 (A Rank-Deficient Matrix).** Neither formula reaches

$$
A = \begin{bmatrix} 1 & 1 \\ 1 & 1\end{bmatrix} ,
$$

whose rank is $1$: both $A^TA$ and $AA^T$ equal $\begin{bmatrix} 2 & 2 \\ 2 & 2\end{bmatrix}$, and neither is invertible.
The geometry is untroubled.
Here $\operatorname{coim} A = \operatorname{span}\{(1,1)^T\}$ and $\operatorname{im} A = \operatorname{span}\{(1,1)^T\}$ are the same line, and on it $A$ acts by $A(1,1)^T = (2,2)^T$: multiplication by $2$.
Hence $A^{\dagger}$ multiplies that line by $\tfrac{1}{2}$ and annihilates the cokernel $\operatorname{span}\{(1,-1)^T\}$, which leaves only

$$
A^{\dagger} = \tfrac{1}{4}\begin{bmatrix} 1 & 1 \\ 1 & 1\end{bmatrix} .
$$

Test this against Definition 6.12: both composites come out as

$$
A^{\dagger}A = AA^{\dagger} = \tfrac{1}{2}\begin{bmatrix} 1 & 1 \\ 1 & 1\end{bmatrix} .
$$

The identity does not appear, and should not; what appears is the orthogonal projection onto $\operatorname{span}\{(1,1)^T\}$, symmetric by the adjoint conditions and idempotent by the consistency conditions, which is precisely what the definition asks of a map inverting $A$ only where $A$ is invertible.
The four subspaces were legible here at a glance.
When they are not, one needs a machine.

Return to the full-row-rank formula: it is not idle.
An underdetermined system — more unknowns than equations, with $A$ of full row rank — is solvable for every $\mathbf{b}$, embarrassingly so: the solutions form a translate of $\operatorname{ker} A$, an entire affine subspace of them.
Which to take?
The pseudoinverse answers: $A^{\dagger}\mathbf{b}$ is the unique **minimum-norm solution**, the one solution lying in $(\operatorname{ker} A)^{\perp}$, from which every other is obtained by adding motion in the kernel.
The section ahead poses the mirror problem — no exact solution at all — and the same operator answers both: where solutions are too many, $A^{\dagger}$ takes the nearest; where they are too few, the best.

**Example 6.14 (Redundant Manipulators).** Chapter 4 left a three-joint planar arm in an interesting predicament.
Its kinematics differentiate to $[DF]:\mathbb{R}^3\rightarrow\mathbb{R}^2$, three joint velocities producing two end-effector velocities, and the kernel of $[DF]$ — generically one-dimensional — consists of the **self-motions**: joint velocities that leave the hand instantaneously fixed.
Given a desired hand velocity $\mathbf{v}$, the system $[DF]\,\dot{\mathbf{\theta}} = \mathbf{v}$ is underdetermined, and the pseudoinverse selects

$$
\dot{\mathbf{\theta}} = [DF]^{\dagger}\,\mathbf{v} ,
$$

the joint motion of least total speed that honors the hand's command; every other choice differs from this one by a self-motion.
Roboticists spend that difference deliberately, steering along the kernel to dodge obstacles and joint limits without disturbing the task.
*The kernel is not a defect of the arm; it is the arm's freedom.*

**Example 6.15 (Orthogonal Projection).** Consider the orthogonal projection $\Pi_{U}:V\to V$ onto a subspace $U<V$.
Its fundamental spaces are:

- $\operatorname{ker}(\Pi_{U}) = U^{\perp}$

- $\operatorname{im}(\Pi_{U}) = U$

The pseudoinverse $\Pi_{U}^{\dagger}$ equals $\Pi_{U}$ itself, as projection already satisfies all four pseudoinverse conditions.
Indeed, projection is its own pseudoinverse precisely because it is idempotent ($\Pi_{U}^2 = \Pi_{U}$) and self-adjoint ($\Pi_{U}^* = \Pi_{U}$) — and, by Exercise 7, those two properties characterize orthogonal projection among all linear maps.

**Theorem 6.16 (Pseudoinverse Properties).** The pseudoinverse $T^{\dagger}$ satisfies:

1. $T^{\dagger}$ maps $\operatorname{im} T$ isomorphically to $(\operatorname{ker} T)^{\perp}$

2. $T^{\dagger}$ annihilates $(\operatorname{im} T)^{\perp}$; indeed $\operatorname{ker} T^{\dagger} = (\operatorname{im} T)^{\perp}$

3. $TT^{\dagger}$ is the orthogonal projection onto $\operatorname{im} T$

4. $T^{\dagger}T$ is the orthogonal projection onto $(\operatorname{ker} T)^{\perp}$

5. If $T$ is invertible, then $T^{\dagger} = T^{-1}$

6. $(T^{\dagger})^{\dagger} = T$

7. $(T^*)^{\dagger} = (T^{\dagger})^*$

Clauses 1 through 4 restate the picture above and can be read off the four defining conditions; Exercise 6 checks the third of them on a concrete matrix.
The remaining three are cheapest once the singular value decomposition is in hand, and are proved in Chapter 10.

In the general case where $A$ is neither full row nor full column rank, the construction of the pseudoinverse becomes more involved.
One approach uses the orthogonal projections onto the fundamental subspaces.
First, we project onto the image space $\operatorname{im}(A)$ using the projection operator $P_{\operatorname{im}(A)}$.
Then, we apply the isomorphism between $\operatorname{im}(A)$ and $(\operatorname{ker} A)^{\perp}$, followed by the inclusion map back into the domain.
In Chapter 10, the singular value decomposition will resolve this construction into a single explicit formula, $A^{\dagger} = V\Sigma^{\dagger}U^T$, valid for any matrix whatsoever.

## 6.5 Least Squares Approximation

The pseudoinverse transforms abstract decompositions into practical computational tools.
For systems where exact solutions fail to exist, it navigates the fundamental subspaces to provide optimal approximations.
This optimality — finding the best possible approximate solution under natural measures of error — lies at the heart of least squares approximation.
The geometric structure revealed through the Fundamental Theorem guides both the theory and the computation of data fitting.

Consider the system $A\mathbf{x}=\mathbf{b}$ where $A:\mathbb{R}^n\to\mathbb{R}^m$ with $m>n$.
Such systems typically arise when fitting models to data: each row represents an observation, each column a parameter to be determined.
Though $\mathbf{b}$ rarely lies in $\operatorname{im} A$, the orthogonal decomposition of the codomain $\mathbb{R}^m$ guides us to the optimal approximation:

$$
\mathbb{R}^m = \operatorname{im} A \boxplus (\operatorname{im} A)^\perp
$$

The vector $\mathbf{b}$ thus splits uniquely as $\mathbf{b} = \mathbf{b}_1 + \mathbf{b}_2$ where $\mathbf{b}_1 \in \operatorname{im} A$ and $\mathbf{b}_2 \in (\operatorname{im} A)^\perp$.
Since $\mathbf{b}_1$ lies in $\operatorname{im} A$, there exists $\hat{\mathbf{x}}$ with $A\hat{\mathbf{x}} = \mathbf{b}_1$, and Lemma 6.5 forbids any other $\mathbf{x}$ from bringing $A\mathbf{x}$ nearer to $\mathbf{b}$.
Square that distance and the quantity being minimized stands exposed:

$$
\|\mathbf{b}-A\mathbf{x}\|^2 \;=\; \sum_{i=1}^m \bigl(b_i - (A\mathbf{x})_i\bigr)^2 ,
$$

one squared residual per observation.
An $\mathbf{x}$ minimizing that sum is a **least squares solution** of $A\mathbf{x}=\mathbf{b}$: squares, since each observation is charged the square of its own error; least, since no other $\mathbf{x}$ pays less in total.

**Theorem 6.17 (Least Squares Solution).** For a full-rank matrix $A\in\mathbb{R}^{m\times n}$ with $m>n$, the system $A\mathbf{x}=\mathbf{b}$ has unique least squares solution:

$$
\hat{\mathbf{x}} = A^{\dagger}\mathbf{b} = (A^TA)^{-1}A^T\mathbf{b}
$$

This solution minimizes $\|\mathbf{b}-A\mathbf{x}\|$ over all $\mathbf{x}\in\mathbb{R}^n$.

*Proof.* The error vector $\mathbf{b}-A\mathbf{x}$ must be orthogonal to $\operatorname{im} A$ at the minimum, else we could reduce its length through projection.
This orthogonality condition means:

$$
\langle \mathbf{b}-A\hat{\mathbf{x}},A\mathbf{v}\rangle = 0 \quad\text{for all }\mathbf{v}\in\mathbb{R}^n
$$

Therefore $A^T(\mathbf{b}-A\hat{\mathbf{x}})=\mathbf{0}$, yielding the **normal equations**:

> *Caveat:* The formula names the solution; it does not recommend the computation.
> Forming $A^TA$ squares the condition number of $A$, doubling the digits a solve will lose (Exercise 12 of Chapter 10).
> Numerical practice reaches $\hat{\mathbf{x}}$ by QR or by the singular value decomposition instead.

$$
A^TA\hat{\mathbf{x}} = A^T\mathbf{b}
$$

When $A$ has full column rank, $\operatorname{ker}(A^TA)=\operatorname{ker} A=\{\mathbf{0}\}$, so $A^TA$ is invertible, giving the stated solution.
This solution equals $A^{\dagger}\mathbf{b}$ by the definition of the pseudoinverse for full-column rank matrices.

To confirm this minimizes the error, note that for any $\mathbf{x}$:

$$
\|\mathbf{b} - A\mathbf{x}\|^2 = \|\mathbf{b} - A\hat{\mathbf{x}} + A\hat{\mathbf{x}} - A\mathbf{x}\|^2 = \|\mathbf{b} - A\hat{\mathbf{x}}\|^2 + \|A\hat{\mathbf{x}} - A\mathbf{x}\|^2
$$

since $(\mathbf{b} - A\hat{\mathbf{x}}) \perp \operatorname{im} A$ by construction.
The second term vanishes precisely when $\mathbf{x} = \hat{\mathbf{x}}$, confirming optimality. ∎

> *Terminology:* The term "normal equations" reflects geometric normality — the error vector stands perpendicular to the solution space.

The normal equations emerge from projecting $\mathbf{b}$ onto $\operatorname{im} A$.
Indeed, the matrix product $A(A^TA)^{-1}A^T$ implements precisely this orthogonal projection.
Through the pseudoinverse, we connect the geometric structure of the Fundamental Theorem directly to computational methods for data fitting.
This connection transforms abstract subspaces into practical tools for approximation.

**Example 6.18 (Linear Regression).** Consider fitting a line $y=mx+b$ to points $(x_1,y_1),\ldots,(x_n,y_n)$.
This leads to the overdetermined system:

$$
\begin{bmatrix}
    x_1 & 1 \\
    x_2 & 1 \\
    \vdots & \vdots \\
    x_n & 1
    \end{bmatrix}
    \begin{pmatrix}
    m \\ b
    \end{pmatrix}
    =
    \begin{pmatrix}
    y_1 \\ y_2 \\ \vdots \\ y_n
    \end{pmatrix}
$$

The least squares solution minimizes the sum of squared vertical distances from points to the line — a criterion the Euclidean inner product dictates.

For specific values $(x_1,y_1)=(1,2)$, $(x_2,y_2)=(2,3)$, and $(x_3,y_3)=(3,5)$, we form:

$$
A = \begin{bmatrix}
    1 & 1 \\
    2 & 1 \\
    3 & 1
    \end{bmatrix}
    \quad\text{and}\quad
    \mathbf{b} = \begin{pmatrix}
    2 \\ 3 \\ 5
    \end{pmatrix}
$$

Computing $A^TA$ and $A^T\mathbf{b}$:

$$
A^TA = \begin{bmatrix}
    14 & 6 \\
    6 & 3
    \end{bmatrix}
    \quad\text{and}\quad
    A^T\mathbf{b} = \begin{pmatrix}
    23 \\ 10
    \end{pmatrix}
$$

The normal equations yield:

$$
\begin{bmatrix}
    14 & 6 \\
    6 & 3
    \end{bmatrix}
    \begin{pmatrix}
    m \\ b
    \end{pmatrix}
    =
    \begin{pmatrix}
    23 \\ 10
    \end{pmatrix}
$$

Solving, we find $m=\frac{3}{2}$ and $b=\frac{1}{3}$, giving $y=\frac{3}{2}x+\frac{1}{3}$ as our best-fit line.

The least squares method extends naturally beyond simple curve fitting.
When the columns of $A$ represent basis functions, we obtain general linear models:

$$
f(x) = c_1\phi_1(x) + c_2\phi_2(x) + \cdots + c_n\phi_n(x)
$$

The coefficients $c_i$ emerge from the least squares solution, providing optimal approximation in the chosen basis.
Different choices of basis functions $\phi_i$ yield different approximation schemes:

- Polynomials for smooth functions

- Trigonometric functions for periodic data

- Wavelets for localized features

- Splines for piecewise smooth approximation

The full power of this approach emerges through the explicit connection to the four fundamental subspaces.
When $A$ has full column rank the least squares solution is unique; in general the minimizers form the affine set $\hat{\mathbf{x}}+\operatorname{ker} A$, and $A^{\dagger}\mathbf{b}$ is the one member lying in $(\operatorname{ker} A)^{\perp}$  — the minimum-norm least squares solution.
The residual $\mathbf{b} - A\hat{\mathbf{x}}$ lies in $(\operatorname{im} A)^{\perp}$, giving it the geometric interpretation as the component of $\mathbf{b}$ that cannot be represented in the model space.
This orthogonal decomposition:

$$
\mathbf{b} = A\hat{\mathbf{x}} + (\mathbf{b} - A\hat{\mathbf{x}})
$$

expresses precisely the projection onto the fundamental subspaces guaranteed by the Fundamental Theorem.
The pseudoinverse $A^{\dagger}$ transforms this abstract decomposition into concrete computational methods for finding optimal approximations.

> *Foreshadowing:* The Singular Value Decomposition in Chapter 10 will provide an even more powerful framework for analyzing and solving least squares problems, revealing the full geometric structure of approximate solutions.

## 6.6 Regularized Least Squares

Real data harbors noise.
The framework of least squares approximation, though mathematically complete, can prove fragile when confronted with measurement errors and uncertainty.
Consider fitting a polynomial to noisy samples — increasing the degree improves the fit to our data points but may produce wild oscillations between them.
This tension between fidelity to measurements and smoothness of solutions suggests a modification to our geometric framework, one that tames such instabilities while preserving the essential character of orthogonal projection.

The source of trouble lies in our unconstrained pursuit of minimal error.
Given noisy measurements, the least squares solution may achieve a deceptively small residual by contorting itself to match the noise rather than the underlying signal.
We require some means of favoring simpler, more stable solutions — a preference that we can encode through geometry.

**Example 6.19 (Polynomial Overfitting).** Consider fitting polynomials of increasing degree $d$ to samples of $f(x)=\cos(2\pi x)$ on $[0,1]$ with small random errors.
The design matrix is a Vandermonde matrix,

$$
A = \begin{bmatrix}
    x_1^d & \cdots & x_1 & 1 \\
    \vdots & & \vdots & \vdots \\
    x_n^d & \cdots & x_n & 1
    \end{bmatrix} ,
$$

and the least squares solution tracks the data points with increasing precision as $d$ grows, but at the cost of violent oscillations between samples.
Though each fit minimizes squared error, higher-degree solutions appear increasingly unstable.

> *Foreshadowing:* This balance between fitting data and maintaining simplicity appears throughout mathematics and engineering.
> We shall encounter it again when studying data analysis in later chapters.

Ridge regression answers with a single added term, penalizing large coefficients alongside the error $\|A\mathbf{x}-\mathbf{b}\|^2$:

$$
\min_{\mathbf{x}}\left(\|A\mathbf{x}-\mathbf{b}\|^2 + \lambda\|\mathbf{x}\|^2\right)
$$

where $\lambda>0$ controls the strength of regularization.
This augmented objective retains the geometric character of our previous development — it measures not just distance to the data but also distance from the origin in the solution space.

From a theoretical perspective, ridge regression replaces the pseudoinverse $A^{\dagger}$ with the **regularized pseudoinverse** $(A^TA + \lambda I)^{-1}A^T$, which sacrifices exact optimality for improved stability and conditioning.
What this replacement actually does is best said in the language of singular values — the natural scaling factors $\sigma_i$ of a matrix, constructed in Chapter 10, where this identity is derived:

$$
\begin{gathered}
(A^TA+\lambda I)^{-1}A^T \;=\; V\,\operatorname{diag}\!\left(\frac{\sigma_i}{\sigma_i^2+\lambda}\right)U^T \\
    \text{as compared with}\\
    A^\dagger \;=\; V\,\operatorname{diag}\!\left(\frac{1}{\sigma_i}\right)U^T
\end{gathered}
$$

where in the second display the reciprocal is taken over the nonzero $\sigma_i$ only.

> *Foreshadowing:* The matrices $U$ and $V$ here are orthonormal bases adapted to $A$  — the singular value decomposition of Chapter 10.
> The derivation and the full story of such **filtered** pseudoinverses await there.

Along directions where $\sigma_i$ is large relative to $\sqrt{\lambda}$, the factor $\sigma_i/(\sigma_i^2+\lambda)\approx 1/\sigma_i$, and ridge inverts just as the pseudoinverse does; along directions where $\sigma_i$ is small, the factor falls to $\sigma_i/\lambda\approx 0$ instead of erupting as $1/\sigma_i$ would.
Ridge regression is the pseudoinverse with its most fragile directions damped.
That is what $\lambda$ buys: stability exactly where inversion is least trustworthy, at the price of a bias toward a smaller solution vector and a larger residual.

**Lemma 6.20 (Ridge Solution).** The minimizer of the ridge regression objective satisfies the modified normal equations:

$$
(A^TA + \lambda I)\mathbf{x} = A^T\mathbf{b}
$$

The minimizer is unique for every $\lambda>0$, even when $A^TA$ is singular; its norm is no larger, and its residual no smaller, than that of any least squares solution.

*Proof.* Stacking turns the penalty into more data:

$$
\|A\mathbf{x}-\mathbf{b}\|^2 + \lambda\|\mathbf{x}\|^2
    = \left\| \begin{bmatrix} A \\ \sqrt{\lambda}\,I\end{bmatrix}\mathbf{x}
      - \begin{pmatrix} \mathbf{b} \\ \mathbf{0}\end{pmatrix} \right\|^2 .
$$

The stacked matrix has full column rank whatever $A$ may be, since $\sqrt{\lambda}\mathbf{x}=\mathbf{0}$ already forces $\mathbf{x}=\mathbf{0}$.
Theorem 6.17 therefore supplies a unique minimizer, and the normal equations of the stacked system are exactly $(A^TA+\lambda I)\mathbf{x}=A^T\mathbf{b}$.
For the comparison, let $\mathbf{x}_\lambda$ be that minimizer and $\hat{\mathbf{x}}$ any least squares solution.
Each minimizes its own objective, so

$$
\|A\mathbf{x}_\lambda-\mathbf{b}\|^2+\lambda\|\mathbf{x}_\lambda\|^2
\leq \|A\hat{\mathbf{x}}-\mathbf{b}\|^2+\lambda\|\hat{\mathbf{x}}\|^2,
\qquad
\|A\hat{\mathbf{x}}-\mathbf{b}\|^2\leq\|A\mathbf{x}_\lambda-\mathbf{b}\|^2 ,
$$

and adding the two leaves $\lambda\|\mathbf{x}_\lambda\|^2\leq\lambda\|\hat{\mathbf{x}}\|^2$. ∎

Note what is and is not claimed: the solution *vector* shrinks, in norm.
Individual coefficients may perfectly well grow, or change sign, as $\lambda$ increases.

The choice of regularization parameter $\lambda$ embodies the fundamental tradeoff between fitting data and maintaining stability.
Small values yield solutions close to pure least squares; large values force solutions toward zero.
No universal choice exists — the appropriate balance depends on noise levels, problem structure, and ultimate purpose.

> *Example:* In polynomial fitting, larger $\lambda$ values increasingly suppress higher-degree terms, effectively limiting the complexity of the fitted function regardless of formal degree.

—

## Signal & Image Processing: Denoising & Inpainting

Every sensor lies a little.
A thermocouple in a reactor, an electrode on a chest, a photosite in a camera: each returns the truth plus a tremor, $\mathbf{y} = \mathbf{s} + \mathbf{n}$, signal corrupted by noise.
The engineer's first task is not to compute with the data but to decide which part of the data deserves belief — and that decision, made honestly, is the choice of a subspace.

The working assumption of signal processing is that truth is smoother than error.
Across a short window of time a temperature does not leap; it drifts, bends, settles; noise, by contrast, jitters at every sample.
Let the model say so: within a window of $2w+1$ consecutive samples, the true signal is approximately a polynomial of low degree $d$.
Collecting the sampled basis $\{1, t, t^2, \ldots, t^d\}$ as the columns of a design matrix $A$, the modeled signals form the subspace $\operatorname{im} A$, and the best approximation to the windowed data $\mathbf{y}$ is the orthogonal projection

$$
\hat{\mathbf{s}} \;=\; A A^{\dagger}\mathbf{y} \;=\; A(A^TA)^{-1}A^T\mathbf{y} ,
$$

the pseudoinverse of Section 6.4 doing exactly what it was built to do.
The smoothed value at the window's center is a single entry of this projection — a fixed linear combination of the raw samples.
For a five-point window and quadratic fit, the recipe is

$$
\hat{s}_0 \;=\; \tfrac{1}{35}\left(-3\, y_{-2} + 12\, y_{-1} + 17\, y_0 + 12\, y_1 - 3\, y_2\right),
$$

computed once and slid along the data stream.

> *Nota bene:* engineers and chemists know this scheme as the **Savitzky-Golay filter**.
> The weights depend only on the window and the degree, never on the data: local least squares becomes a fixed convolution.

> *BONUS!* by the symmetry of the window, these five weights recover not only quadratics but cubics exactly at the center: an odd-degree gift.

Because projection fixes $\operatorname{im} A$ pointwise, the filter transmits any true quadratic trend untouched, while discarding the component of the noise perpendicular to the model.
Note the negative weights at the window's edges: a projection is more cunning than a moving average.

Which distinctions does the filter erase?
Two windows receive identical smoothed fits precisely when they differ by an element of $\operatorname{ker}(AA^{\dagger}) = (\operatorname{im} A)^{\perp}$, the fit being the whole projection $AA^{\dagger}\mathbf{y}$.
What the smoother sees is not $\mathbb{R}^n$ but the quotient $\mathbb{R}^n / (\operatorname{im} A)^{\perp}$ — and this is the point: the subspace of discarded differences was chosen by the modeler to be where noise lives and signal does not.
*(The single centre value discards more still, since it reads off only one coordinate of the fit.)*
Choose it wrongly and the projection is just as decisive, deleting truth with the same serene efficiency.

An image is the same story with two indices.
At each pixel $(i,j)$, a neighborhood of intensities forms the data vector, the bivariate monomials

$$
\{\, (x-i)^k (y-j)^\ell \,:\, k+\ell \leq d \,\}
$$

form the columns of the design matrix, and the identical projection smooths the patch — the same fit, one dimension up.
Where the model strains, the method shows its limits: at an edge, where intensity genuinely leaps, a polynomial fit blurs what it should preserve.
The ridge-regularized fit $(A^TA + \lambda I)^{-1}A^T$ of Section 6.6 damps the overshoot but cannot repeal the blur; sharp boundaries are not polynomials, and no choice of $\lambda$ makes them so.
Keep the distinction straight: $A^{\dagger}$ itself does no balancing — it minimizes the residual outright and, among the minimizers, takes the smallest; the trade between fidelity and tameness is ridge's alone, set by $\lambda$.

Now delete pixels instead of doubting them.
Dust on a scan, a scratch on a photograph, a dead element in a sensor array: some entries of the patch are simply gone, and the problem shifts from **denoising** to **inpainting** — reconstruction of the missing.
The design matrix responds by losing rows, since only observed pixels contribute equations, and the same machinery pivots from approximation to reconstruction: fit the polynomial to the pixels that survive, then evaluate it where they do not.
With many observations the fit is overdetermined and least squares governs.
With few — a rich basis, a small crowd of survivors — the system turns underdetermined, and $A^{\dagger}$ selects the minimum-norm coefficients: the tamest polynomial consistent with every surviving pixel.
Where solutions are too many, the pseudoinverse of Section 6.4 takes the nearest; here that choice acquires a face — the flattest, least dramatic patch that honors all the evidence.

Vectors become matrices and nothing essential changes: pressure fields over an aircraft wing, spectral bands of a satellite image — the same projections, one index heavier.
What must be chosen, always, is the subspace: wide enough to hold the truth, narrow enough to exclude the tremor.
*What the filter cannot distinguish, it was built to forget.*

—

## Support Vector Machines: Geometry of Optimal Separation

Classification is the engineer's other great fitting problem.
Points $\{\mathbf{x}_i\}_{i=1}^n$ in $\mathbb{R}^d$ carry labels $y_i = \pm 1$: intact or cracked, benign or malignant, normal or failing.
Sought is a rule that labels points not yet seen.
The linear answer is a hyperplane $\{\mathbf{x} : \mathbf{w}^T\mathbf{x} + b = 0\}$ with normal vector $\mathbf{w}$, splitting feature space into two halfspaces; a new point is classified by the sign of $\mathbf{w}^T\mathbf{x} + b$, and its distance to the boundary,

$$
d(\mathbf{x}) = \frac{|\mathbf{w}^T\mathbf{x} + b|}{\|\mathbf{w}\|} ,
$$

measures how confidently.

> *Example:* in quality control, sensor measurements classify products as acceptable or defective.
> A wide margin keeps the decision stable when the measurements themselves wobble.

The machinery of this chapter already yields such a rule.
Treat the labels as targets and regress: minimizing $\sum_i (\mathbf{w}^T\mathbf{x}_i + b - y_i)^2$ is least squares, solved in closed form by the pseudoinverse of Section 6.4, and adding $\lambda\|\mathbf{w}\|^2$ brings the steadiness of Section 6.6.
This works, and is used.
It has, however, one strange habit: squared loss punishes points for being too correct.
A scan far inside the healthy halfspace drags the boundary toward itself as surely as an error does, because the square grows in both directions.

The **support vector machine** keeps the regularizer and changes the loss.
Its principle is the **margin**: among all separating hyperplanes, choose the one whose distance to the nearest training point is greatest.
After rescaling $\mathbf{w}$ and $b$ so that the nearest points satisfy $y_i(\mathbf{w}^T\mathbf{x}_i + b) = 1$, the margin equals $1/\|\mathbf{w}\|$, and maximizing it means minimizing $\|\mathbf{w}\|^2$ subject to $y_i(\mathbf{w}^T\mathbf{x}_i + b) \geq 1$ for all $i$.
When no hyperplane separates the classes, slack variables measure each point's violation:

$$
\min_{\mathbf{w},b,\boldsymbol{\xi}} \;\frac{1}{2}\|\mathbf{w}\|^2 + C\sum_{i=1}^n \xi_i
    \quad\text{subject to}\quad y_i(\mathbf{w}^T\mathbf{x}_i + b) \geq 1 - \xi_i , \;\; \xi_i \geq 0 .
$$

At the optimum, $\xi_i = \max\left(0,\, 1 - y_i(\mathbf{w}^T\mathbf{x}_i + b)\right)$: the **hinge loss**, zero for every point comfortably on its correct side, growing linearly for the rest.
The two classifiers now stand side by side, and their kinship is substance, not metaphor: ridge classification minimizes squared misfit plus $\lambda\|\mathbf{w}\|^2$; the SVM minimizes hinge misfit plus a multiple of the same $\|\mathbf{w}\|^2$.
The difference is a loss indifferent to surplus correctness.

> *Caveat:* The hinge is not differentiable at its corner, so no normal equations exist: the SVM is solved as a quadratic program.
> The closed-form comfort of the pseudoinverse is exactly what the sharper loss surrenders.

That indifference is where the geometry sharpens.
Points beyond the margin contribute nothing to the hinge, so the optimal $\mathbf{w}$ is built from only the points on or inside the margin — the **support vectors**.
Delete any other training point and the boundary does not move.
In medical classification, where each scan becomes a point whose coordinates are intensities, textures, and shapes, the support vectors are the diagnostically ambiguous cases: the classifier is made of precisely the examples that were hardest to call.

The same geometry monitors the built world.
Vibration sensors on a bridge stream acceleration data; extracted features become points; the SVM's hyperplane divides normal from worrisome.
The margin supplies tolerance against sensor noise and weather, and the points that land near it — the structure's borderline states — are exactly the ones an engineer should go look at.

A trained classifier ends as a decomposition of feature space: $\mathbb{R}^d = \operatorname{span}\{\mathbf{w}\} \boxplus \mathbf{w}^{\perp}$.
The score $\mathbf{w}^T\mathbf{x} + b$ varies only along $\operatorname{span}\{\mathbf{w}\}$: the directions parallel to the separating hyperplane are exactly $\mathbf{w}^{\perp}$, the kernel of the linear part of the score, invisible to the decision by construction.
Of the $d$ dimensions painstakingly measured, $d-1$ are discarded, and everything depends on choosing well the one that remains.
*Classification is projection onto a single well-chosen line.*

—

## Exercises: Chapter 6

1. Let $U<\mathbb{R}^3$ be spanned by $\mathbf{u}_1=(1,1,0)^T$ and $\mathbf{u}_2=(0,1,1)^T$, and let $\mathbf{v}=(2,1,3)^T$.
Find a basis for $U^\perp$, and compute $\Pi_{U}\mathbf{v}$ by projecting onto that line and subtracting.

2. Equip $\mathcal{P}_2$ with $\langle f,g\rangle = \int_0^1 f(x)g(x)\,dx$.
Verify that $1$ and $x-\frac{1}{2}$ are orthogonal, then apply Gram-Schmidt to $x^2$ against them to complete an orthogonal basis.
The vector you subtracted is $\Pi_{\operatorname{span}\{1,\,x-1/2\}}x^2$; explain why Definition 6.4 forces that identification rather than its being an accident of these polynomials.

3. Let $A = \begin{bmatrix}2 & -1 & -1\\-1 & 2 & -1\\-1 & -1 & 2\end{bmatrix}$.
Find bases for $\operatorname{ker} A$ and $\operatorname{row}(A)$, and confirm by direct computation that each vector of one is orthogonal to each vector of the other.
Here $A$ is symmetric, so $\operatorname{row}(A)=\operatorname{col}(A)$ and the kernel is perpendicular to the image as well — a coincidence of symmetry, not a general fact.

4. Fit the line $y=mx+b$ to $(0,1)$, $(1,3)$, $(2,2)$ by the normal equations.
Compute the residual $\mathbf{b}-A\hat{\mathbf{x}}$ and check it against both columns of $A$.
Confirm that $\|\mathbf{b}\|^2 = \|A\hat{\mathbf{x}}\|^2 + \|\mathbf{b}-A\hat{\mathbf{x}}\|^2$.

5. Solve the underdetermined system $A\mathbf{x}=\mathbf{b}$ for $A = \begin{bmatrix}1 & 1 & 1\\1 & -1 & 0\end{bmatrix}$ and $\mathbf{b}=(3,1)^T$, using the full-row-rank pseudoinverse $A^{\dagger}=A^T(AA^T)^{-1}$.
Compute $\operatorname{ker} A$, confirm that $A^{\dagger}\mathbf{b}$ is orthogonal to it, and check that $A^{\dagger}\mathbf{b}$ does solve the system.
Every other solution is $A^{\dagger}\mathbf{b}$ plus an element of that kernel; say which one a robot arm would spend, and on what.

6. Let $A = \begin{bmatrix}1 & 0\\1 & 1\\1 & 2\end{bmatrix}$ and compute $A^{\dagger}=(A^TA)^{-1}A^T$.
Verify all four conditions of Definition 6.12 for your answer.
Then confirm that $AA^{\dagger}$ is the orthogonal projection onto $\operatorname{col}(A)$ promised by Theorem 6.16, and exhibit a nonzero vector it annihilates.

7. Lemma 6.7 shows that an orthogonal projection is idempotent and self-adjoint.
Prove the converse: if $P:V\to V$ satisfies $P^2=P$ and $P^*=P$ on a finite-dimensional inner product space, then $P=\Pi_{\operatorname{im} P}$.
Deduce that $\|P\mathbf{v}\|\leq\|\mathbf{v}\|$ for every $\mathbf{v}$, with equality exactly when $\mathbf{v}\in\operatorname{im} P$.

8. Let $A\in\mathbb{R}^{m\times n}$.
Prove that $\operatorname{ker}(A^TA)=\operatorname{ker} A$ by expanding $\langle A^TA\mathbf{x},\mathbf{x}\rangle$, and conclude that $A^TA$ is invertible exactly when $A$ has full column rank.
In that case verify both clauses of Definition 6.4 directly for $P=A(A^TA)^{-1}A^T$, which the chapter asserts to be the projection onto $\operatorname{col}(A)$ but nowhere checks.

9. Let $T:V\to W$ be a linear transformation between finite-dimensional inner product spaces.
Prove that $\operatorname{ker} T = (\operatorname{im} T^*)^\perp$, and deduce the orthogonal splitting $V = \operatorname{ker} T \boxplus \operatorname{im} T^*$.
Applying the same identity to $T^*$ in place of $T$, show that $\mathbf{x}$ satisfies $T^*T\mathbf{x}=T^*\mathbf{b}$ precisely when $T\mathbf{x}=\Pi_{\operatorname{im} T}\mathbf{b}$; conclude that the normal equations are always solvable, and that they agree with $T\mathbf{x}=\mathbf{b}$ exactly when $\mathbf{b}\in\operatorname{im} T$.

10. Let $U$ be a subspace of an inner product space $V$.
Show that $\mathbf{v}$ minimizes the norm among all vectors of its coset $\mathbf{v}+U$ if and only if $\mathbf{v}\perp U$, and that the minimizer is then unique.

11. Let $A\in\mathbb{R}^{m\times n}$ and let $A'=[\,A\mid\mathbf{c}\,]$ adjoin one further column.
Prove that the least squares residual can only shrink: $\min_{\mathbf{x}'}\|\mathbf{b}-A'\mathbf{x}'\| \leq \min_{\mathbf{x}}\|\mathbf{b}-A\mathbf{x}\|$.
Show that equality holds exactly when $\mathbf{c}$ is orthogonal to the residual $\mathbf{b}-\Pi_{\operatorname{im} A}\mathbf{b}$.
Conclude that a shrinking residual is never by itself an argument for enlarging a model.

12. Let $P$ and $Q$ be the orthogonal projections onto subspaces $U$ and $W$ of a finite-dimensional inner product space.
Show that $PQ$ is itself an orthogonal projection if and only if $PQ=QP$, and identify the subspace onto which it then projects.

13. Give $\mathbb{R}^{n\times n}$ the Frobenius inner product of Example 5.3.
Using Example 6.3 and Lemma 6.5, prove that the symmetric matrix nearest to a given $A$ is $\frac{1}{2}(A+A^T)$, and that the distance to it is the Frobenius norm of the skew part.
Compute both for $A=\begin{bmatrix}1&5\\-1&3\end{bmatrix}$.

14. Let $V=C([0,1])$ with $\langle f,g\rangle=\int_0^1 f(x)g(x)\,dx$, and let $U<V$ consist of those $f$ with $f(0)=f(1)$.
Prove that $U^\perp=\{\mathbf{0}\}$ by testing an arbitrary $g\in U^\perp$ against the function $x(1-x)g(x)$, which lies in $U$.
Since $U$ is the kernel of $f\mapsto f(0)-f(1)$ it is not all of $V$, so $(U^\perp)^\perp\neq U$.

    > *Compare:* In $\mathbb{R}^n$ the analogous subspace $\{\mathbf{x}:x_1=x_n\}$ has $U^\perp = \operatorname{span}\{\mathbf{e}_1-\mathbf{e}_n\}$.
    > The transported answer here would be a pair of point masses at $0$ and $1$, which is no function at all; an integral cannot see a two-point condition.

15. Let $\mathbf{v}_1=(1,1,1)^T$, $\mathbf{v}_2=(1,2,-1)^T$, and let $\mathbf{w}$ be nonzero and orthogonal to both.
Expand $\mathbf{v}=(2,3,1)^T$ in the basis $\{\mathbf{v}_1,\mathbf{v}_2,\mathbf{w}\}$ by solving the resulting system, then compute instead the three quotients $\langle\mathbf{v},\mathbf{v}_i\rangle/\|\mathbf{v}_i\|^2$ and $\langle\mathbf{v},\mathbf{w}\rangle/\|\mathbf{w}\|^2$.
Exactly one of the three agrees with the true coordinate; say which, and why that one and no other.
State the hypothesis on a basis under which the second recipe is valid at all.

16. For invertible matrices $(AB)^{-1}=B^{-1}A^{-1}$.
Show that the pseudoinverse loses this, by computing both $(AB)^{\dagger}$ and $B^{\dagger}A^{\dagger}$ for $A=\begin{bmatrix}1&0\\0&0\end{bmatrix}$ and $B=\begin{bmatrix}1&1\\1&1\end{bmatrix}$.
Identify which of the four conditions of Definition 6.12 the wrong candidate fails, and say what goes wrong geometrically when $\operatorname{im} B$ fails to lie in $(\operatorname{ker} A)^\perp$.

17. Temperature $T$ and energy use $E$ (in kWh) from a building's HVAC system give

$$
(T,E) = \{(68,42),\ (72,45),\ (75,48),\ (71,44),\ (69,43),\ (74,47)\}
$$

The third and sixth readings are four-hour averages, with one quarter the error variance of the others.
Fit $E=aT+b$ by minimizing $\sum_i w_i(E_i-aT_i-b)^2$ with each $w_i$ inversely proportional to that reading's variance, and verify that the residual $\mathbf{r}$ satisfies $A^TW\mathbf{r}=\mathbf{0}$ for the design matrix $A$ and $W=\operatorname{diag}(w_1,\ldots,w_6)$.

18. Measurements $y_i = s(t_i) + a\cos(\omega t_i) + b\sin(\omega t_i) + \epsilon_i$ carry periodic interference at a known frequency $\omega$.
Let $N<\mathbb{R}^n$ be spanned by the sampled vectors $(\cos\omega t_i)$ and $(\sin\omega t_i)$, and estimate the interference by $\Pi_{N}\mathbf{y}$.
Prove that if the errors vanish and the sampled $s$ is orthogonal to $N$, then $\mathbf{y}-\Pi_{N}\mathbf{y}$ is exactly the sampled signal.
Then take $t_i=0,1,\ldots,7$ with $\omega=\pi/2$ and exhibit a nonzero $s$ that this same subtraction destroys completely.

19. (Challenge.) Let $\mathbf{x}_\lambda$ minimize $\|A\mathbf{x}-\mathbf{b}\|^2+\lambda\|\mathbf{x}\|^2$ for $\lambda>0$.
Comparing the objective at $\mathbf{x}_\lambda$ with its value at $\mathbf{0}$, prove $\|\mathbf{x}_\lambda\|\leq\|\mathbf{b}\|/\sqrt{\lambda}$, so that $\mathbf{x}_\lambda\to\mathbf{0}$ as $\lambda\to\infty$.
Now pair the modified normal equations of Lemma 6.20 with an arbitrary $\mathbf{z}\in\operatorname{ker} A$ to show $\mathbf{x}_\lambda\in(\operatorname{ker} A)^\perp$ for every $\lambda$.
Writing $\mathbf{x}^+=A^{\dagger}\mathbf{b}$ and $\mathbf{d}=\mathbf{x}_\lambda-\mathbf{x}^+$, derive $\|A\mathbf{d}\|^2+\lambda\|\mathbf{d}\|^2 = -\lambda\langle\mathbf{x}^+,\mathbf{d}\rangle$ and conclude from Theorem 6.9 that $\mathbf{x}_\lambda\to\mathbf{x}^+$ as $\lambda\to 0^+$.
The last step needs the inverse of $T$ restricted to $(\operatorname{ker} T)^\perp$ to be a fixed linear map, not merely a bijection.

---


---

> **Part marker.** LUVAH — passion (kernel)


# Chapter 7. Diagonalization & Dynamics

*"how is it that all things are chang'd even as in ancient times"*

**A transformation in perpetual action** reveals patterns hidden from static view.
A mass-spring system oscillates with characteristic frequencies; a population grows or declines at intrinsic rates; a network's influence flows along preferred channels.
These seemingly distinct phenomena share a common mathematical essence: certain directions remain invariant under repeated transformation, while vectors along these special directions experience pure scaling.
Such fixed directions and their associated scaling factors — **eigenvectors** and **eigenvalues** — govern how linear transformations act over time.

Consider a simple linear recurrence modeling population growth: each generation's size is a fixed multiple of the last.
The population either grows exponentially or decays to extinction, depending on whether this multiplier exceeds unity.
Though elementary, this example contains the seed of a deeper truth: the long-term behavior of linear systems often reduces to pure scaling along special directions.

The search for such invariant directions leads us to **characteristic polynomials** — equations whose roots reveal the natural scaling factors of a transformation.
These eigenvalues, together with their associated **eigenvectors**, provide a new perspective on linear transformations.
We seek coordinates aligned with intrinsic scaling; when such exist, the transformation assumes its most primal diagonal form.

This diagonalization — this alignment of coordinates with natural directions — does more than simplify computation.
It reveals the essence of how transformations act, decomposing complex motion into simpler components.
The vibration of a drum becomes a superposition of pure tones; the flow of heat resolves into independent decay modes.
What is complicated in one basis is elementary in another; diagonalization is the change of view.

## 7.1 The First Order

The simplest differential equation from calculus serves as prototype for all continuous-time linear systems.
Consider the equation

$$
\frac{dx}{dt} = \lambda x \tag{7.1}
$$

> *Notation:* Using the differential operator $D=d/dt$ will prove advantageous later.

where $\lambda$ is a constant.
From calculus, we know the general solution is an exponential:

$$
x(t) = x_0 e^{\lambda t}
$$

where $x_0$ is a constant interpretable as the **initial condition** $x_0 = x(0)$.
This elementary equation already carries structure: the solutions to (7.1) are closed under addition and scalar multiplication.
As such, the simple solution $e^{\lambda t}$ serves as a basis for the 1-dimensional solution space to $(7.1)$.

Note the centrality of the constant $\lambda$ in determining the qualitative behavior of all the solutions in the solution space:

- When $\lambda > 0$, solutions grow exponentially

- When $\lambda < 0$, solutions decay exponentially

- When $\lambda = 0$, solutions remain constant

> *Think:* The solution corresponding to $x_0=0$ is special, in that even when other solutions grow or shrink, it remains constant.
> Such **equilibrium** solutions are central objects of study in dynamical systems.

This structure — exponential solutions parametrized by a characteristic number $\lambda$  — will recur throughout this and the following two chapters.
More complex systems will decompose into collections of such fundamental solutions, each growing or decaying at its own characteristic rate.
The art lies in finding these natural modes of behavior.
It is not initially obvious, but such $\lambda$ values are connected at the deepest levels to the algebra of matrices and linear transformations.

## 7.2 Coupled First-Order Systems

Real systems rarely evolve in isolation.
A predator population depends on its prey; stock prices move with market sectors; neurons fire in vast interconnected networks.
Even the simplest model tends to track at least two interacting variables.
Consider $x(t)$ and $y(t)$ whose evolution depends linearly on a combination of present states:

$$
\displaystyle\frac{dx}{dt} = ax + by \quad : \quad \displaystyle\frac{dy}{dt} = cx + dy
$$

where $a,b,c,d$ are constants.
Unlike the scalar case, no obvious solution presents itself.
Writing this linear system in matrix form reveals a familiar pattern:

$$
\displaystyle\frac{d}{dt}\begin{pmatrix}x\\y\end{pmatrix} =
\begin{bmatrix}a & b \\ c & d\end{bmatrix}
\begin{pmatrix}x\\y\end{pmatrix}
$$

This matrix form suggests a special case worth examining.
Suppose the matrix were diagonal:

$$
\displaystyle\frac{d}{dt}\begin{pmatrix}x\\y\end{pmatrix} =
\begin{bmatrix}\lambda_1 & 0 \\ 0 & \lambda_2\end{bmatrix}
\begin{pmatrix}x\\y\end{pmatrix}
\quad \Leftrightarrow \quad
\frac{dx}{dt} = \lambda_1 x
\,\, : \,\,
\frac{dy}{dt} = \lambda_2 y
$$

each solvable by the methods of the previous section.
The solution would be pure exponential growth or decay along each coordinate axis:

$$
\begin{pmatrix}x(t)\\y(t)\end{pmatrix}
=
\begin{pmatrix}c_1e^{\lambda_1 t}\\c_2e^{\lambda_2 t}\end{pmatrix}
$$

where $c_1$ and $c_2$ are determined by initial conditions.

This observation — that diagonal systems decompose into independent scalar equations — suggests a strategy.
If we could somehow transform our original system into diagonal form, its solution would reduce to pure exponentials: we seek coordinates that reveal the hidden diagonal structure lurking within coupled systems.

**Example 7.1 (Chemical Reaction).** Consider two chemical species with concentrations $x_A$ and $x_B$ that interact through a simple reaction network in matrix form:

$$
\frac{d}{dt}\begin{pmatrix}x_A\\x_B\end{pmatrix}
=
\begin{bmatrix}-k_1 & k_2 \\ k_1 & -k_2\end{bmatrix}
\begin{pmatrix}x_A\\x_B\end{pmatrix}
$$

where $k_1,k_2 > 0$ are reaction rate constants.
A curious change of coordinates reveals hidden simplicity.
Set $(x_A,x_B)^T = P(u,v)^T$ for the invertible

$$
P = \begin{bmatrix}k_2 & 1 \\ k_1 & -1\end{bmatrix} ,
\qquad \det P = -(k_1+k_2) \neq 0 .
$$

Differentiating and multiplying through by $P^{-1}$ converts the system by a similarity transformation, and the product is diagonal:

$$
P^{-1}
\begin{bmatrix}-k_1 & k_2 \\ k_1 & -k_2\end{bmatrix}
P
=
\begin{bmatrix}0 & 0 \\ 0 & -k_1-k_2\end{bmatrix}
$$

This diagonal matrix has diagonal entries $0$ for $u$ and $-(k_1+k_2)<0$ for $v$.
Thus $u$ remains constant while $v$ decays exponentially.
The solution in original coordinates is computed as:

$$
\begin{pmatrix}x_A\\x_B\end{pmatrix}
=
\begin{bmatrix}k_2 & 1 \\ k_1 & -1\end{bmatrix}
\begin{pmatrix}u\\ v\end{pmatrix}
=
\begin{pmatrix}
    c_1k_2+c_2e^{-(k_1+k_2)t} \\
    c_1k_1-c_2e^{-(k_1+k_2)t}
\end{pmatrix}
$$

where $c_1$ and $c_2$ depend on initial conditions.
The columns of the reaction matrix sum to zero, so $x_A+x_B$ is constant along every solution: here it equals $c_1(k_1+k_2)$, and the transient $c_2e^{-(k_1+k_2)t}$ merely shuttles material from one species to the other.
What survives is the state $(c_1k_2,\,c_1k_1)$ in which $k_1x_A=k_2x_B$ — forward and reverse reactions running at equal rate, which is what chemists call detailed balance.
This "magical" change of coordinates anticipates deeper structure: the zero on the diagonal is the conservation of mass, and the line of equilibria it produces is exactly the direction the transient cannot touch.

Many coupled systems admit such a transformation to diagonal form; those that resist will demand the subtler analysis of Chapter 8.

## 7.3 Eigenvalues & Eigenvectors

The general linear system of ordinary differential equations takes the form

$$
\frac{d\mathbf{x}}{dt} = A\mathbf{x} \tag{7.2}
$$

where $A$ is a square matrix and $\mathbf{x}(t)$ is a vector-valued function of time.
Were $A$ a scalar $\lambda$, Section 7.1 would already be the whole answer, $\mathbf{x}(t)=e^{\lambda t}\mathbf{x}_0$.
So ask: is there a 1-d subspace on which $A$ acts just like scalar multiplication?
That means a vector $\mathbf{v}\neq\mathbf{0}$ with

$$
A\mathbf{v} = \lambda\mathbf{v} \tag{7.3}
$$

for some scalar $\lambda$.
Such a subspace $\operatorname{span}(\mathbf{v})$ would be **invariant** under $A$, and on it the ODE collapses to the trivial 1-d case.

> *Caution:* The restriction $\mathbf{v}\neq\mathbf{0}$ is crucial.
> The zero vector satisfies $A\mathbf{0}=\lambda\mathbf{0}$ for any $\lambda$, but tells us nothing about the transformation's behavior.

Rewrite equation (7.3) as

$$
(A-\lambda I)\mathbf{v} = \mathbf{0} .
$$

A nonzero solution $\mathbf{v}$ exists exactly when $A-\lambda I$ has nontrivial kernel — exactly when it fails to be invertible, and its determinant vanishes: $\det(A-\lambda I) = 0$.

For all but finitely many values of $\lambda$, the transformation $A-\lambda I$ is invertible, with trivial kernel and full image; the exceptional values of $\lambda$ at which $A-\lambda I$ acquires a kernel are precisely the interesting ones.
That kernel, $\operatorname{ker}(A-\lambda I)$, is called the **eigenspace** of $\lambda$: it consists of all the eigenvectors for $\lambda$ together with the zero vector, and it is a fundamental subspace in the sense of Chapter 3, subject to all the accounting the Fundamental Theorem enforces, so that whatever dimension the kernel gains at an exceptional $\lambda$, the image must surrender.
*Every eigenspace is a kernel.*

**Definition 7.2 (Eigenvalues and Eigenvectors).** The **characteristic polynomial** $p_A(\lambda)$ of a square matrix $A$ is the polynomial

$$
p_A(\lambda) = \det(A-\lambda I) \tag{7.4}
$$

A scalar $\lambda$ is called an **eigenvalue** of $A$ if it is a root of the characteristic polynomial: $p_A(\lambda)=0$.
For each eigenvalue $\lambda$, any nonzero vector $\mathbf{v}$ satisfying

$$
A\mathbf{v} = \lambda\mathbf{v} \tag{7.5}
$$

is called an **eigenvector** corresponding to eigenvalue $\lambda$.

> *Nota bene:* Eigenvalues and eigenvectors are paired — though uniqueness is not implied.

**Example 7.3.** For a concrete example, consider the matrix

$$
A = \begin{bmatrix}
    2 & 1 \\
    1 & 2
    \end{bmatrix}
$$

Its characteristic polynomial is

$$
\det(A-\lambda I) = \begin{vmatrix}
    2-\lambda & 1 \\
    1 & 2-\lambda
    \end{vmatrix}
    = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3
$$

Setting this equal to zero yields eigenvalues $\lambda_1=3$ and $\lambda_2=1$.
For $\lambda_1=3$, we solve $(A-3I)\mathbf{v}=\mathbf{0}$:

$$
\begin{bmatrix}
    -1 & 1 \\
    1 & -1
    \end{bmatrix}
    \begin{pmatrix}
    v_1 \\ v_2
    \end{pmatrix}
    = \mathbf{0}
    \quad\Rightarrow\quad
    \mathbf{v}_1 = \begin{pmatrix}
    1 \\ 1
    \end{pmatrix}
$$

Similarly, for $\lambda_2=1$ we find $\mathbf{v}_2=(1,-1)^T$.
Each eigenvector reveals a direction in which $A$ acts by simple scaling: vectors along $\mathbf{v}_1$ are stretched by a factor of $3$, while those along $\mathbf{v}_2$ are left unchanged (rescaled by $1$).

The search for eigenvalues and eigenvectors thus reduces to:

1. Form the characteristic polynomial $\det(A-\lambda I)$

2. Find its roots (the eigenvalues)

3. For each eigenvalue $\lambda$, solve $(A-\lambda I)\mathbf{v}=\mathbf{0}$ for nonzero $\mathbf{v}$

> *Terminology:* The set of eigenvalues of a square matrix is its *spectrum*.
> The spectra of a system can encode information about growth, stability, or variance, depending on the context.

As to what type and how many eigenvalues a system has, the following consequence of the Fundamental Theorem of Algebra settles the question.

**Lemma 7.4 (Characteristic Polynomials).** For any matrix $A\in\mathbb{R}^{n\times n}$, its characteristic polynomial $p_A(\lambda)=\det(A-\lambda I)$ satisfies:

1. The polynomial has degree $n$

2. It has $n$ roots (over $\mathbb{C}$, counted with multiplicity)

3. Its coefficients are real, and any complex roots occur in conjugate pairs

The characteristic polynomial encodes more than just eigenvalues — its coefficients reveal fundamental invariants of the transformation.
Most striking are the relationships between eigenvalues and two elementary matrix measurements: trace and determinant.

**Lemma 7.5 (Eigenvalue Relations).** Let $A$ be an $n\times n$ matrix and let $\lambda_1,\ldots,\lambda_n$ be the roots of its characteristic polynomial, listed with multiplicity and with complex roots included, as in Lemma 7.4.
Then:

> *Example:* For a $2\times 2$ matrix $A$, the characteristic polynomial $p_A(\lambda)=\lambda^2-\operatorname{tr}(A)\lambda+\det(A)$ makes these relationships transparent.

1. The determinant equals their product: $\det(A) = \prod_{i=1}^n \lambda_i$

2. The trace equals their sum: $\operatorname{tr}(A) = \sum_{i=1}^n \lambda_i$

*Proof.* Expand $\det(A-\lambda I)$ as a signed sum over permutations of products $\prod_i m_{i\sigma(i)}$, where $m_{ij}=a_{ij}-\lambda\delta_{ij}$.
Since $\lambda$ sits only on the diagonal, the term for $\sigma$ has $\lambda$-degree equal to the number of fixed points of $\sigma$: the identity contributes $\prod_i(a_{ii}-\lambda)$, of degree $n$ with leading term $(-\lambda)^n$, and every other permutation moves at least two indices, so contributes degree at most $n-2$.
Thus $p_A$ has leading coefficient $(-1)^n$ and, having $n$ roots over $\mathbb{C}$ by Lemma 7.4, factors as

$$
p_A(\lambda) = (-1)^n\prod_{i=1}^n(\lambda-\lambda_i) .
$$

Setting $\lambda=0$ gives $\det(A)=p_A(0)=(-1)^n\prod_i(-\lambda_i)=(-1)^{2n}\prod_i\lambda_i=\prod_i\lambda_i$, which is (1).

For (2), read the coefficient of $\lambda^{n-1}$ off each side.
Expanding the factored form gives $(-1)^{n-1}\sum_i\lambda_i$; on the matrix side every non-identity permutation has degree at most $n-2$, so the coefficient comes from $\prod_i(a_{ii}-\lambda)$ alone and equals $(-1)^{n-1}\operatorname{tr}(A)$.
Equating the two readings gives $\operatorname{tr}(A)=\sum_i\lambda_i$. ∎

## 7.4 Simple Diagonalization

When a linear transformation possesses $n$ distinct real eigenvalues, a great simplification becomes possible.
Change coordinates to align with the eigenvectors — those directions of pure scaling — and the transformation stands stripped of coupled complexity.
This is **diagonalization**.

Begin with $A\mathbf{v}_1 = 3\mathbf{v}_1$ and $A\mathbf{v}_2 = \mathbf{v}_2$ of Example 7.3.
These two equations combine into one by arranging the eigenvectors as columns of a matrix:

$$
A[\mathbf{v}_1\;\mathbf{v}_2] = [\mathbf{v}_1\;\mathbf{v}_2]\begin{bmatrix}3 & 0 \\ 0 & 1\end{bmatrix}
$$

Writing in terms of square matrices $V=[\mathbf{v}_1\;\mathbf{v}_2]$ and $\Lambda=\operatorname{diag}(3,1)$, this becomes simply

$$
AV = V\Lambda \tag{7.6}
$$

> { Think: if you have internalized the equation $A\mathbf{v}=\lambda\mathbf{v}$, you may find the matrix form of this equation to be easily memorable.
> Just be sure to convince yourself as to the ordering of the terms...}

When $V$ is invertible (as it must be when the eigenvalues are distinct), we obtain the diagonalization
$V^{-1}AV = \Lambda$. This observation generalizes to arbitrary dimension:

**Theorem 7.6 (Diagonalization).** Let $A$ be an $n\times n$ matrix with $n$ distinct real eigenvalues $\lambda_1,\ldots,\lambda_n$ and corresponding eigenvectors $\mathbf{v}_1,\ldots,\mathbf{v}_n$.
Then:

1. The eigenvectors form a basis for $\mathbb{R}^n$

2. The matrix $V=[\mathbf{v}_1\;\cdots\;\mathbf{v}_n]$ is invertible

3. $V^{-1}AV = \Lambda$ where $\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$

*Proof.* Everything rests on the linear independence of the eigenvectors, and that is proved by induction on $n$.
For $n=1$ the set $\{\mathbf{v}_1\}$ is independent, an eigenvector being nonzero by definition.
Assume the claim for any $n-1$ eigenvectors belonging to distinct eigenvalues, and suppose

$$
\sum_{i=1}^n c_i\mathbf{v}_i = \mathbf{0} .
$$

Applying $A$ to both sides gives a second relation,

$$
\mathbf{0} = A\left(\sum_{i=1}^n c_i\mathbf{v}_i\right) = \sum_{i=1}^n c_i\lambda_i\mathbf{v}_i ,
$$

and subtracting $\lambda_1$ times the first from the second eliminates $\mathbf{v}_1$:

$$
\sum_{i=2}^n c_i(\lambda_i-\lambda_1)\mathbf{v}_i = \mathbf{0} .
$$

Here $\mathbf{v}_2,\ldots,\mathbf{v}_n$ are $n-1$ eigenvectors with distinct eigenvalues, hence independent by the inductive hypothesis, so every coefficient $c_i(\lambda_i-\lambda_1)$ vanishes.
Since $\lambda_i\neq\lambda_1$ for $i\geq 2$, this forces $c_2=\cdots=c_n=0$.
The original relation collapses to $c_1\mathbf{v}_1=\mathbf{0}$, and $\mathbf{v}_1\neq\mathbf{0}$ gives $c_1=0$.
The induction is complete.

An independent set of $n$ vectors in $\mathbb{R}^n$ must also span, since any vector outside its span would enlarge it to $n+1$ independent vectors in a space spanned by $n$, which Corollary 2.22 forbids, no independent set being larger than a spanning one; the eigenvectors are therefore a basis, which is (1).
The columns of $V$ are then independent and $V$ is invertible, which is (2).
Multiplying $AV=V\Lambda$ on the left by $V^{-1}$ gives (3). ∎

> *Nota bene:* Everything here is over $\mathbb{R}$: both $V$ and $\Lambda$ are required to be real.
> A matrix may fail this test and still succumb over $\mathbb{C}$, as the rotation $J$ beside Lemma 7.4 does; Chapter 8 takes up that distinction.

Distinct eigenvalues are a sufficient condition, not a necessary one, and it is the conclusion rather than the hypothesis that deserves a name.

**Definition 7.7 (Diagonalizable).** A square matrix $A\in\mathbb{R}^{n\times n}$ is {diagonalizable over $\mathbb{R}$} if there is an invertible $V\in\mathbb{R}^{n\times n}$ and a diagonal $\Lambda\in\mathbb{R}^{n\times n}$ with

$$
A = V\Lambda V^{-1} .
$$

The definition is stated in matrices; its content is geometric.
Nothing new has been introduced by the letter: $V$ is the change of basis matrix of Definition 4.9, its columns the vectors of the new basis written in the coordinates of the old, and here the new basis is one of eigenvectors.
In the notation of Chapter 4 the equation $A=V\Lambda V^{-1}$ says $A\sim\Lambda$, so that the whole of diagonalization is the question of which matrices are similar to a diagonal one.

**Lemma 7.8 (Eigenbasis Criterion).** A matrix $A\in\mathbb{R}^{n\times n}$ is diagonalizable if and only if $\mathbb{R}^n$ possesses a basis consisting of eigenvectors of $A$.
In that case the columns of $V$ are such a basis and the diagonal entries of $\Lambda$ are the corresponding eigenvalues, listed in the same order.

*Proof.* Both directions are a single reading of $AV=V\Lambda$.
Let $V$ have columns $\mathbf{v}_1,\ldots,\mathbf{v}_n$ and $\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$.
The $j$th column of $AV$ is $A\mathbf{v}_j$; the $j$th column of $V\Lambda$ is $\lambda_j\mathbf{v}_j$.
So $AV=V\Lambda$ says exactly that each column $\mathbf{v}_j$ is an eigenvector with eigenvalue $\lambda_j$ — nonzero, an invertible matrix having no zero column — while invertibility of $V$ says exactly that those columns are a basis of $\mathbb{R}^n$.
Multiplying by $V^{-1}$ passes between $AV=V\Lambda$ and $A=V\Lambda V^{-1}$ in either direction. ∎

Theorem 7.6 now reads: a matrix with $n$ distinct real eigenvalues is diagonalizable.
The converse fails, and instructively so — the identity is diagonalizable though its $n$ eigenvalues are all the same one — which is why the criterion, and not the theorem, is the working test.

The power of diagonalization lies in how it simplifies computation of matrix powers.
When $A=V\Lambda V^{-1}$, repeated multiplication becomes mere diagonal scaling:

**Lemma 7.9 (Matrix Powers).** If $A$ is diagonalizable, $A=V\Lambda V^{-1}$, then for any nonnegative integer $k$:

$$
A^k = V\Lambda^k V^{-1}
$$

> *Think:* how hard is it to compute powers of the diagonal matrix $\Lambda$?

*Proof.* For $k=0$ both sides equal $I$, since $\Lambda^0=I$ and $VIV^{-1}=I$.
Assuming $A^k=V\Lambda^kV^{-1}$, the inner factors cancel:

$$
A^{k+1} = A^kA = \left(V\Lambda^kV^{-1}\right)\left(V\Lambda V^{-1}\right) = V\Lambda^k\left(V^{-1}V\right)\Lambda V^{-1} = V\Lambda^{k+1}V^{-1} .
$$

The result follows by induction. ∎

Each eigenspace is scaled by its eigenvalue once per application, and $V$, $V^{-1}$ merely translate between our coordinates and those eigenspaces.
The limit $k\to\infty$ is thereby controlled entirely by the magnitudes $|\lambda_i|$  — see Chapter 9.
Similar matrices are one transformation seen in two coordinate systems; when the coordinates are an eigenbasis, the matrix is diagonal, and there is nothing simpler to be had.

## 7.5 Matrix Exponentials

Recall from Section 7.3 the general linear system of differential equations (7.2):

$$
\frac{d\mathbf{x}}{dt} = A\mathbf{x} \tag{7.7}
$$

where $A$ is a square matrix.
The scalar equation of Section 7.1 settles the case $A=\lambda I$ at once, componentwise, with solutions $\mathbf{x}(t)=e^{\lambda t}\mathbf{x}_0$.
Such exponentials indeed generate solutions in the general case.
The following definition is key.

**Definition 7.10 (Matrix Exponential).** The **matrix exponential** of a square matrix $A$ is defined by the power series

$$
e^A = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \cdots = \displaystyle\sum_{k=0}^\infty \frac{A^k}{k!} \tag{7.8}
$$

For a time-dependent system we write $e^{At}$ for the matrix exponential of the matrix $At$, so that $e^{At}=\sum_{k=0}^\infty t^kA^k/k!$.

> The series converges, and absolutely, as exponentials do...

This formal series inherits many properties of the scalar exponential, though not all of them, and one must be established before the others can be used.
The scalar law $e^{a+b}=e^ae^b$ survives exactly to the extent that the matrices commute.

**Lemma 7.11 (Commuting Exponentials).** Let $A$ and $B$ be square matrices of the same size with $AB=BA$.
Then $e^{A+B}=e^Ae^B$.

> *Think:* The induction proving the binomial theorem for numbers works verbatim for matrices; it needs only that $B$ move past $A$.

*Proof.* Both series converge absolutely, so their product may be rearranged into the Cauchy product, collecting all pairs of indices with a fixed sum:

$$
e^Ae^B = \left(\sum_{j=0}^\infty\frac{A^j}{j!}\right)\left(\sum_{k=0}^\infty\frac{B^k}{k!}\right)
    = \sum_{m=0}^\infty\frac{1}{m!}\sum_{j=0}^m\binom{m}{j}A^jB^{m-j} .
$$

Because $A$ and $B$ commute, the binomial theorem holds for them, so the inner sum is $(A+B)^m$ and the whole is $\sum_m(A+B)^m/m!=e^{A+B}$. ∎

Two consequences are immediate and will both be used.
A matrix commutes with itself, so $A$ and $-A$ commute, giving

> *Nota bene:* Commutativity is not decorative.
> For $A=\begin{bmatrix}0&1\\0&0\end{bmatrix}$ and $B=\begin{bmatrix}0&0\\1&0\end{bmatrix}$ the two sides differ.
> Exercise 9 goes further and shows that commutativity is not merely sufficient but necessary.

$$
e^{At}e^{-At} = e^{0} = I \tag{7.9}
$$

for every $t$: the matrix exponential is always invertible, with $\left(e^{At}\right)^{-1}=e^{-At}$.
And $A$ commutes with every power of $A$, hence with the partial sums of the series, hence with $e^{At}$ itself.

**Lemma 7.12 (Matrix Exponential Solution).** For any square matrix $A$ and any vector $\mathbf{x}_0$, the initial value problem

$$
\frac{d\mathbf{x}}{dt} = A\mathbf{x}, \quad \mathbf{x}(0)=\mathbf{x}_0
$$

has the unique solution $\mathbf{x}(t) = e^{At}\mathbf{x}_0$.

*Proof.* Each entry of $e^{At}$ is a power series in $t$ convergent for all $t$; differentiate term by term, as calculus permits:

$$
\frac{d}{dt}e^{At} = \sum_{k=1}^\infty\frac{kt^{k-1}}{k!}A^k = Ae^{At} .
$$

So $\mathbf{x}(t)=e^{At}\mathbf{x}_0$ solves the equation, with $\mathbf{x}(0)=\mathbf{x}_0$.

For uniqueness, let $\mathbf{y}(t)$ be any solution and set $\mathbf{z}(t)=e^{-At}\mathbf{y}(t)$.
The same computation with $A$ replaced by $-A$ gives $\frac{d}{dt}e^{-At}=-Ae^{-At}$, so by the product rule

$$
\mathbf{z}' = -Ae^{-At}\mathbf{y} + e^{-At}\mathbf{y}' = -Ae^{-At}\mathbf{y} + e^{-At}A\mathbf{y} = \mathbf{0} ,
$$

the last step because $A$ commutes with $e^{-At}$.
Thus $\mathbf{z}$ is constant, equal to $\mathbf{z}(0)=\mathbf{y}(0)=\mathbf{x}_0$.
Multiplying $\mathbf{z}=e^{-At}\mathbf{y}$ on the left by $e^{At}$ and invoking (7.9),

$$
\mathbf{y}(t) = e^{At}\mathbf{z}(t) = e^{At}\mathbf{x}_0 ,
$$

so the solution just exhibited is the only one. ∎

> *Caveat:* While the formula resembles the scalar case, computing $e^{At}$ directly from the series is rarely practical.
> The art lies in finding more efficient methods based on the structure of $A$.

The simplest case occurs when $A$ is diagonal.
For $A=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$, the matrix exponential is simply $e^{At} = \operatorname{diag}(e^{\lambda_1t},\ldots,e^{\lambda_nt})$: each component evolves independently, growing or decaying at the rate of its own diagonal entry.

**Lemma 7.13 (Diagonalizable Matrix Exponential).** If $A$ is diagonalizable, $A=V\Lambda V^{-1}$ with $\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$, then

$$
e^{At} = Ve^{\Lambda t}V^{-1}
$$

where $e^{\Lambda t}=\operatorname{diag}(e^{\lambda_1t},\ldots,e^{\lambda_nt})$.

*Proof.* By Lemma 7.9, for every $k\geq 0$, $A^k = V\Lambda^k V^{-1}$.
Therefore in the power series defining $e^{At}$:

$$
e^{At} = I + At + \frac{(At)^2}{2!} + \cdots = \sum_{k=0}^\infty \frac{t^k}{k!}A^k = \sum_{k=0}^\infty \frac{t^k}{k!}V\Lambda^k V^{-1}
$$

Each partial sum factors, $\sum_{k=0}^N\frac{t^k}{k!}V\Lambda^kV^{-1} = V\left(\sum_{k=0}^N\frac{t^k}{k!}\Lambda^k\right)V^{-1}$, by linearity alone; letting $N\to\infty$:

$$
e^{At} = V\left(\sum_{k=0}^\infty \frac{t^k}{k!}\Lambda^k\right)V^{-1} = Ve^{\Lambda t}V^{-1}
$$

where the middle term reduces to $\operatorname{diag}(e^{\lambda_1t},\ldots,e^{\lambda_nt})$ by the scalar exponential series. ∎

This decomposition reveals how eigenvalues control the long-term behavior of solutions: each eigendirection experiences exponential growth or decay at a rate determined by its eigenvalue.
Two interacting populations governed by the matrix of Example 7.3 read off at once: symmetric growth, both populations increasing in proportion at rate $e^{3t}$, and asymmetric growth, their difference evolving more slowly at $e^{t}$.
Any initial condition excites a combination of the two, the symmetric mode eventually dominating.

This connection between eigenvalues and the qualitative behavior of solutions — growth, decay, or oscillation — exemplifies how the algebraic structure of a matrix determines the geometric character of its flow.

One extension remains, and it recenters everything.
Engineered systems rarely relax to the origin; they relax to a set-point sustained by constant input, so that the honest model is $\dot{\mathbf{x}} = A\mathbf{x}+\mathbf{b}$ and the equilibria are the solutions of $A\mathbf{x}_* = -\mathbf{b}$.
When $A$ is invertible the equilibrium is unique, $\mathbf{x}_* = -A^{-1}\mathbf{b}$, and the substitution $\mathbf{y}=\mathbf{x}-\mathbf{x}_*$ restores the homogeneous system already solved, so that every trajectory reads $\mathbf{x}(t) = \mathbf{x}_* + e^{At}\left(\mathbf{x}_0-\mathbf{x}_*\right)$: the dynamics are as before, merely recentered on the rest state.
When $A$ is singular, the Fundamental Theorem describes what remains.
An equilibrium exists only if $\mathbf{b}$ lands in $\operatorname{im} A$; failing that, the system has no rest state at all, and the unreachable component of $\mathbf{b}$ drives perpetual motion.
When rest is possible, it is not unique: the equilibria form the affine family

$$
\mathbf{x}_* \,\in\, -A^{\dagger}\mathbf{b} + \operatorname{ker} A ,
$$

a minimum-norm equilibrium selected by the pseudoinverse of Chapter 6, translated by an entire kernel of alternatives.
Along $\operatorname{ker} A$ the dynamics are indifferent: a line or plane of rest states among which the initial condition, not the system, decides.

> *Example:* A network of chemical reservoirs exchanging contents conserves total mass, which is the statement that the columns of $A$ sum to zero: it is $A^T$, not $A$, that kills the uniform direction, $A^T\mathbf{1}=\mathbf{0}$.
> The conservation law lives in $\operatorname{ker} A^T$ and the equilibria in $\operatorname{ker} A$, and every level of the conserved total supplies its own equilibrium.
> The two kernels coincide only when the exchange is symmetric.
> The kernel is the memory of the initial condition that mixing cannot erase.

## 7.6 Higher-Order Equations & Basis Solutions

A simple mass-spring system requires tracking both position and velocity; a circuit with inductance and capacitance needs current and charge; a chemical reaction network may depend on concentrations and their rates of change.
Such systems lead naturally to second-order (or higher) differential equations.
Though seemingly more complex than the first-order systems studied thus far, these equations succumb to the same eigenvalue methods through a systematic reduction to matrix form.

Chapter 2 wrote a linear homogeneous equation of order $n$ as

$$
p(D)x = \left(D^n + a_{n-1}D^{n-1} + \cdots + a_1D + a_0I\right)x = 0 ,
$$

with $D=d/dt$ and constant coefficients $a_k$, and promised a meaning for the roots of $p$.

> *Terminology:* The matrix has a special structure — zeros everywhere except for $1$'s on the superdiagonal and the coefficients $-a_k$ in the last row.
> Such matrices are called **companion matrices**.

 Introduce a new variable for each derivative: $x_1=x$, $x_2=\dot{x}$, and onward to $x_n = d^{n-1}x/dt^{n-1}$.
The single equation of order $n$ becomes a first-order system in matrix form:

$$
\frac{d}{dt}\begin{pmatrix}x_1\\x_2\\x_3\\\vdots\\x_n\end{pmatrix} =
    \begin{bmatrix}
    0 & 1 & 0 & \cdots & 0 \\
    0 & 0 & 1 & \cdots & 0 \\
    0 & 0 & 0 & \cdots & 0 \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    -a_0 & -a_1 & -a_2 & \cdots & -a_{n-1}
    \end{bmatrix}
    \begin{pmatrix}x_1\\x_2\\x_3\\\vdots\\x_n\end{pmatrix}
$$

Here is the connection promised.
The eigenvalues of this companion matrix $C$ are precisely the roots of the **characteristic equation** $p(\lambda)=0$, obtained by substituting $\lambda$ for $D$ in the operator.

> *Think:* This is worth checking rather than believing.
> Expand $\det(C-\lambda I)$ along the first column: the entry $-\lambda$ in position $(1,1)$ leaves the companion matrix of $\lambda^{n-1}+a_{n-1}\lambda^{n-2}+\cdots+a_1$, and the entry $-a_0$ in position $(n,1)$ leaves a lower triangular minor with $1$'s down the diagonal, of determinant $1$.
> Induction on $n$ then gives
>
>

$$
>
> \det(C-\lambda I) = (-1)^n p(\lambda) ,
>
>
$$

>
> so the characteristic polynomial of $C$ is $p$ up to a sign that never disturbs the roots.

When these eigenvalues are real and distinct (as we assume throughout this chapter), the solution follows directly from our previous work on matrix exponentials.

**Example 7.14 (Mass-Spring System).** Consider a mass $m$ attached to a spring with constant $k$ and dashpot damping coefficient $c$.
Newton's second law yields

$$
m\frac{d^2x}{dt^2} + c\frac{dx}{dt} + kx = 0
$$

where $x(t)$ measures displacement from equilibrium.
Dividing by $m$ and setting $\omega_0=\sqrt{k/m}$ (the natural frequency) and $\gamma=c/m$ (the damping rate), we obtain

$$
\frac{d^2x}{dt^2} + \gamma\frac{dx}{dt} + \omega_0^2x = 0
$$

This transforms to first-order form by setting $x_1=x$ and $x_2=\dot{x}$:

$$
\frac{d}{dt}\begin{pmatrix}x_1\\x_2\end{pmatrix} =
    \begin{bmatrix}
    0 & 1 \\
    -\omega_0^2 & -\gamma
    \end{bmatrix}
    \begin{pmatrix}x_1\\x_2\end{pmatrix}
$$

For concrete values $\omega_0^2=2$ and $\gamma=3$, the companion matrix

$$
A = \begin{bmatrix}
    0 & 1 \\
    -2 & -3
    \end{bmatrix}
$$

has characteristic equation $\lambda^2 + 3\lambda + 2 = 0$ with roots $\lambda_1=-1$ and $\lambda_2=-2$.
The corresponding eigenvectors are

$$
\mathbf{v}_1 = \begin{pmatrix}1\\-1\end{pmatrix} \quad\text{and}\quad
    \mathbf{v}_2 = \begin{pmatrix}1\\-2\end{pmatrix}
$$

The matrix is diagonalizable, so Lemma 7.13 supplies $e^{At}=Ve^{\Lambda t}V^{-1}$ with $V=[\mathbf{v}_1\;\mathbf{v}_2]$ and $\Lambda=\operatorname{diag}(-1,-2)$, and $\mathbf{x}(t)=e^{At}\mathbf{x}(0)$ for any initial condition.
The position $x(t)=x_1(t)$ decays to equilibrium as $t\to\infty$, at rates set by the eigenvalues $-1$ and $-2$.
The scalar solution $x(t) = c_1e^{-t}+c_2e^{-2t}$ is the first component of the vector solution, as it must be.

This example illustrates how eigenvalue analysis illuminates physical behavior.
The eigenvalues $-1$ and $-2$ being real and negative indicates pure exponential decay without oscillation — characteristic of an overdamped system.
Different parameter values might yield underdamped oscillations or critical damping, cases we shall explore in Chapter 8.

Both formulations — the system $\dot{\mathbf{x}}=A\mathbf{x}$ and the scalar equation $p(D)x=0$  — have solution sets that are kernels of linear operators, hence subspaces: solutions add, and solutions scale.
What remains is to produce a basis, and the eigenvalues do it.

> *Recall:* Chapter 2 identified the solutions of $p(D)x=0$ as $\operatorname{ker} p(D)$, and Chapter 3 makes every kernel a subspace.
> The same reading serves the system, whose solutions are the kernel of $\frac{d}{dt}-A$.

**Theorem 7.15 (Basis Solutions).** Let the eigenvalues $\lambda_1,\ldots,\lambda_n$ of $A$ be real and distinct. Then:

1. For the system $D\mathbf{x}=A\mathbf{x}$ with eigenvectors $\mathbf{v}_1,\ldots,\mathbf{v}_n$, a basis for the solution space is given by:


$$
\mathbf{\phi}_i(t) = e^{\lambda_i t}\mathbf{v}_i, \quad i=1,\ldots,n
$$

2. For the scalar equation $p(D)x=0$, where $p(\lambda)$ is the characteristic polynomial, a basis is:


$$
\phi_i(t) = e^{\lambda_i t}, \quad i=1,\ldots,n
$$

*Proof.* For the system, direct substitution verifies each $\mathbf{\phi}_i$ is a solution:

$$
\frac{d}{dt}\mathbf{\phi}_i = \lambda_i e^{\lambda_i t}\mathbf{v}_i = e^{\lambda_i t}(A\mathbf{v}_i) = A\mathbf{\phi}_i
$$

Their linear independence follows from that of the eigenvectors.

For the scalar equation, $p(D)e^{\lambda t} = p(\lambda)e^{\lambda t}$: when $\lambda$ is a root of $p$, the exponential $e^{\lambda t}$ is a solution.
For independence, suppose $\sum_i c_ie^{\lambda_i t}=0$ for all $t$ and differentiate $k$ times, $k=0,1,\ldots,n-1$:

$$
\sum_{i=1}^n c_i\lambda_i^k e^{\lambda_i t} = 0 .
$$

Evaluated at $t=0$, these $n$ equations are a linear system in the $c_i$ whose matrix is Vandermonde in the distinct $\lambda_i$ — entries $v_{ij}=\lambda_i^{\,j-1}$, determinant vanishing only when two of the $\lambda_i$ coincide, as Exercise 14 shows.
Hence every $c_i=0$. ∎

General solutions take parallel forms:

$$
\mathbf{x}(t) = \sum_{i=1}^n c_i e^{\lambda_i t}\mathbf{v}_i \quad\text{and}\quad x(t) = \sum_{i=1}^n c_i e^{\lambda_i t}
$$

The coefficients $c_i$ are determined by initial conditions — either $\mathbf{x}(0)$ for the system or $x(0),x'(0),\ldots,x^{(n-1)}(0)$ for the scalar equation.

> *Foreshadowing:* When eigenvalues coincide, both formulations require modification.
> The solutions acquire polynomial factors multiplying the exponentials — a complication we shall explore in Chapter 8.

The choice between scalar and system form is a matter of convenience.
The mathematics — exponential solutions built from eigenvalues — is the same either way.

—

## Multi-Zone Building Temperature Control

A building conducts a slow argument with the weather, and every wall is a term in the equations.
Consider a building with multiple rooms, each maintained at a controlled temperature through a combination of HVAC input and heat exchange with neighboring spaces.
How fast the whole settles — and which imbalances linger — is a question about eigenvalues.

*[Margin figure omitted]*

Consider three adjacent rooms sharing walls but with different exterior exposures.
Let $T_i(t)$ denote the temperature of room $i$ at time $t$.
The rate of temperature change in each room depends on heat exchange with neighboring rooms (proportional to temperature differences), heat loss to the exterior (proportional to difference from ambient temperature), and HVAC input (controlled heating or cooling).

Applying Newton's law of cooling and conservation of energy leads to a system of coupled differential equations:

$$
c_1\frac{dT_1}{dt} = k_{12}(T_2-T_1) + k_{13}(T_3-T_1) - h_1(T_1-T_a) + u_1
$$

$$
c_2\frac{dT_2}{dt} = k_{12}(T_1-T_2) + k_{23}(T_3-T_2) - h_2(T_2-T_a) + u_2
$$

$$
c_3\frac{dT_3}{dt} = k_{13}(T_1-T_3) + k_{23}(T_2-T_3) - h_3(T_3-T_a) + u_3
$$

where $c_i$ represents the thermal mass of room $i$, $k_{ij}$ the thermal conductance between rooms $i$ and $j$, $h_i$ the heat transfer coefficient to ambient temperature $T_a$, and $u_i$ the HVAC input power to room $i$.

To analyze this system, first consider the unforced response ($u_i=0$) relative to ambient temperature.
Let $x_i = T_i-T_a$ denote the temperature deviation in room $i$.
Taking realistic values for a modern office building section with equal thermal masses ($c_1=c_2=c_3=1$), symmetric coupling between adjacent rooms ($k_{12}=k_{23}=1$, $k_{13}=0.5$), and varying exterior exposure ($h_1=2$, $h_2=0.5$, $h_3=1.5$), we obtain the system matrix:

$$
A = \begin{bmatrix}
-3.5 & 1.0 & 0.5 \\
1.0 & -2.5 & 1.0 \\
0.5 & 1.0 & -3.0
\end{bmatrix}
$$

The eigenvalues of $A$ determine the natural thermal modes of the building.
Computing these reveals three distinct real eigenvalues: $\lambda_1 \approx -4.14$, $\lambda_2 \approx -3.67$, and $\lambda_3 \approx -1.19$.
Three distinct real eigenvalues mean a complete modal decomposition, with no need for the finer analysis of Chapter 8; three negative ones mean asymptotic stability — every room returns to ambient after any disturbance.

The fastest mode, associated with $\lambda_1$, equilibrates a temperature imbalance between rooms 1 and 2; the intermediate mode balances room 3 against its neighbors; the slowest mode captures the gradual cooling of the building as a whole.

The diagonalization of Section 7.5 then gives the complete temperature response: $e^{At}=Qe^{\Lambda t}Q^T$, with $\Lambda=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)$ and $Q$ the matrix of eigenvectors.
Note the outer factors: each is the transpose of the other, so $Q$ is orthogonal.
This is the symmetry of $A$ at work — shared walls conduct equally in both directions, and the rooms share a common thermal mass — so the three eigenspaces are mutually perpendicular lines in $\mathbb{R}^3$, and resolving a temperature profile into modes is orthogonal projection onto each in turn, geometry that Chapter 9 will make systematic.

This decomposition guides control.
The fast modes equilibrate on their own, so the effort belongs to the slowest, and the sensors belong where that mode is loudest.
Insulation and thermal mass are, in this language, instruments for moving the spectrum.

> *Example:* A well-designed building might have its slowest eigenvalue around $-2.0$ hr$^{-1}$, meaning the slowest thermal mode decays with a half-life of about 20 minutes.

None of this is special to three rooms: a floor of thirty offices yields a $30\times 30$ system with the same structure, its thermal life resolved into thirty modes and thirty decay rates, sensors placed to watch the slow ones.
Turn on a single heater and every mode stirs.
*A wall between two rooms is no wall to an eigenvector.*

—

## Transient Growth in Shear Flows

A fluid between two plates, one gliding steadily past the other, is the plainest shear there is — and by every eigenvalue it is calm.
Linearize the flow of plane Couette at any Reynolds number and the spectrum of the governing operator lies wholly in the left half-plane: every mode decays, the flow is stable, and the theorem saying so is old and correct.
Run the experiment, and near a Reynolds number of a few hundred the flow goes turbulent anyway.
The eigenvalues are unanimous, and they are wrong about the thing that matters.

> *Terminology:* A real matrix is **normal** when $A^TA=AA^T$; symmetric matrices are normal, and a real symmetric matrix has an *orthonormal* basis of eigenvectors (Lemma 9.19).
> The spectral norm $\|M\|_2=\max_{\|\mathbf{x}\|=1}\|M\mathbf{x}\|$ is the greatest stretching $M$ can do to a unit vector, and for symmetric $A$ with $t\geq 0$ it obeys $\|e^{At}\|_2 = e^{\lambda_{\max}t}$ exactly; without symmetry the two part company — below, by a factor growing with the Reynolds number.

The resolution is a matter of *when*.
An eigenvalue governs the fate of a mode as $t\to\infty$; the flow, however, lives in finite time, and the two need not agree.
When the operator is symmetric and its eigenvalues are all negative, the disagreement cannot arise.
Symmetry supplies an *orthonormal* basis of eigenvectors $\mathbf{q}_1,\ldots,\mathbf{q}_n$ — this is Lemma 9.19, stated in Chapter 9 and proved in Chapter 10 — so every solution reads $\mathbf{x}(t)=\sum_ic_ie^{\lambda_it}\mathbf{q}_i$ with $\|\mathbf{x}(t)\|^2=\sum_ic_i^2e^{2\lambda_it}$, orthonormality having removed all the cross terms.
Each summand decays, so the norm falls monotonically to zero and there is no interval in which to misbehave.
Strip away symmetry, let the eigenvectors lean toward one another, and a solution certain to vanish can first grow, sometimes enormously, before it obeys its eigenvalues.

> The matrix is a two-mode caricature of an operator that lives in infinitely many dimensions.

To see the mechanism with nothing hidden, reduce the flow to two modes: a slender streamwise vortex, and the **streak** it lifts into being by dragging slow fluid across the shear.
Writing $u$ for the streak amplitude and $v$ for the vortex, a faithful caricature of the linearized dynamics is

$$
\frac{d}{dt}\begin{bmatrix} u \\ v \end{bmatrix}
=
\begin{bmatrix} -1/\mathrm{Re} & 1 \\ 0 & -2/\mathrm{Re} \end{bmatrix}
\begin{bmatrix} u \\ v \end{bmatrix},
$$

where $\mathrm{Re}$ is the Reynolds number and the off-diagonal $1$ is the lift-up: the vortex feeds the streak, the streak does not feed back.
The eigenvalues are $-1/\mathrm{Re}$ and $-2/\mathrm{Re}$ — real, distinct, negative.
Every tool of this chapter applies, and every one of them promises decay.

Starting from a unit vortex and no streak, the matrix exponential gives

$$
u(t) = \mathrm{Re}\,\bigl(e^{-t/\mathrm{Re}} - e^{-2t/\mathrm{Re}}\bigr),
$$

which departs from zero, climbs to a maximum of $\mathrm{Re}/4$ at time $t=\mathrm{Re}\,\ln 2$, and only then subsides.
A disturbance guaranteed to vanish first swells by a factor of order $\mathrm{Re}$.
At the Reynolds numbers where Couette flow actually breaks, that is a hundredfold in amplitude and ten-thousandfold in energy — room enough for the nonlinearity we linearized away to seize the flow and never return it.
The linear operator does not cause turbulence; it merely lifts the perturbation high enough that something else can.

> *Example:* The optimal transient energy growth in plane shear scales as $\mathrm{Re}^{2}$, the amplitude as $\mathrm{Re}$ — the caricature's $\mathrm{Re}/4$ is the real operator's law, shorn of its constants.

The source of the swell is geometric, and it is written in the fundamental subspaces.
Each eigenspace is a kernel, $\operatorname{ker}(A-\lambda I)$; here they are $\operatorname{span}(1,0)$ and $\operatorname{span}(-\mathrm{Re},1)$, and as $\mathrm{Re}$ grows these two lines close toward one.
To write a modest vortex in so slanted a basis demands large and nearly cancelling coordinates — the two modal pieces of $u$ enter as $+\mathrm{Re}$ and $-\mathrm{Re}$, annihilating each other at $t=0$.
As the modes decay at their two different rates the cancellation comes apart, and the bulge is the invoice for an ill-conditioned basis.
When the matrix was symmetric — when every wall conducted both ways — the eigenspaces were perpendicular and no such conspiracy could form.
*Symmetry was never a convenience; it was the whole of the peace.*

—

## Exercises: Chapter 7

1. Let $A = \begin{bmatrix}1 & 2\\2 & -2\end{bmatrix}$.
Find its eigenvalues and eigenvectors, and use Lemma 7.13 to compute $e^{At}$.
Solve $\dot{\mathbf{x}} = A\mathbf{x}$ with $\mathbf{x}(0)=(3,-1)^T$, which is not an eigenvector and so excites both modes, one growing and one decaying.

2. Compute the eigenvalues and eigenvectors of

$$
B = \begin{bmatrix}3 & -2 & 0\\0 & 2 & 0\\-4 & 1 & 1\end{bmatrix}
$$

Exhibit the matrices $V$ and $\Lambda$ for which $V^{-1}BV=\Lambda$, as Theorem 7.6 promises.
Check your eigenvalues against $\operatorname{tr} B$ and $\det B$ by Lemma 7.5.

3. A matrix $A$ has characteristic polynomial $p_A(\lambda) = \lambda^4 - 2\lambda^3 - \lambda^2 + 2\lambda$.
Find its eigenvalues and determine whether $A$ is necessarily diagonalizable.
Then say exactly which initial conditions give solutions of $\dot{\mathbf{x}} = A\mathbf{x}$ that remain bounded as $t\to\infty$: the answer is a $2$-dimensional subspace, nameable without knowing a single entry of $A$.

4. Consider the third-order equation $\dddot{x} + 2\ddot{x} - \dot{x} - 2x = 0$.
Find a basis for its solution space by Theorem 7.15 and write the general solution.
Then determine for which initial conditions $x(0)$, $\dot{x}(0)$, $\ddot{x}(0)$ the solution remains bounded as $t\to\infty$; exactly one of your three coefficients must be made to vanish, and the resulting condition cuts a plane out of the space of initial conditions.

5. The **Cayley-Hamilton theorem** states that every square matrix satisfies its own characteristic equation: $p_A(A)$ is the zero matrix.
It is asserted here, not proved; Exercise 10 proves the $2\times2$ case.
Verify it for $A = \begin{bmatrix}3 & 1\\2 & 4\end{bmatrix}$ by computing $p_A(\lambda)$ and then $A^2-7A+10I$ by hand.
Since $p_A(\lambda)=(\lambda-2)(\lambda-5)$, what you have shown is that $(A-2I)(A-5I)$ is the zero matrix; deduce that every nonzero column of $A-5I$ is an eigenvector for $\lambda=2$, and say which eigenvector the other shift produces.

6. Let $A = \begin{bmatrix}1 & 1\\0 & 1\end{bmatrix}$ and show by induction that $A^k = \begin{bmatrix}1 & k\\0 & 1\end{bmatrix}$.
Sum the series of Definition 7.10 in closed form to obtain $e^{At}$ exactly, using $\sum_k t^k/k! = e^t$ and $\sum_k k\,t^k/k! = te^t$; no diagonalization is involved.
Now attempt the computation a second way: find $\operatorname{ker}(A-I)$, and observe that it is too small to supply the matrix $V$ of eigenvectors that Lemma 7.13 calls for.
Name the hypothesis of Theorem 7.6 that has failed.

7. Prove that the eigenvalues of a triangular matrix are precisely its diagonal entries, counted with multiplicity.
The qualification is not decoration: $A = \begin{bmatrix}2 & 5 & 7\\0 & 2 & 3\\0 & 0 & 3\end{bmatrix}$ has diagonal entries $2,2,3$ but only two distinct eigenvalues, and Definition 7.2 counts roots of $p_A$, not the values they take.
Deduce that a triangular matrix with distinct diagonal entries is diagonalizable over $\mathbb{R}$ in the sense of Definition 7.7.

    > *Recall:* the determinant of a triangular matrix is the product of its diagonal entries.
    > Expand an upper triangular matrix along its first column, a lower triangular one along its first row, and induct on the size either way.

8. Show that if $A$ is diagonalizable over $\mathbb{R}$ with every eigenvalue negative, then $\lim_{t\to\infty}e^{At} = 0$; use Lemma 7.13 and pass to the limit one diagonal entry at a time.
Deduce from Lemma 7.12 that every solution of $\dot{\mathbf{x}}=A\mathbf{x}$ tends to $\mathbf{0}$.
Then compute $e^{Rt}$ for $R = \begin{bmatrix}0 & -2\\2 & 0\end{bmatrix}$, whose eigenvalues are not real, and observe that the limit fails to exist.

9. Lemma 7.11 gives $e^{(A+B)t}=e^{At}e^{Bt}$ whenever $AB=BA$.
Prove the converse: if the identity holds for *every* $t$ then $A$ and $B$ commute, since expanding both sides by Definition 7.10 leaves coefficients of $t^2$ differing by $\frac{1}{2}(BA-AB)$.
Then take $A=\begin{bmatrix}1 & 0\\0 & -1\end{bmatrix}$ and $B=\begin{bmatrix}0 & 1\\1 & 0\end{bmatrix}$: as $A+B$ is symmetric so is $e^{(A+B)t}$, while $e^{At}e^{Bt}$ transposes to $e^{Bt}e^{At}$ and is not.

10. For any $2\times 2$ matrix $A$, show by direct computation with the entries that $A^2 - \operatorname{tr}(A)A + \det(A)I = 0$; no eigenvalue theory is needed here, and none should be used.
Then identify the left side as $p_A(A)$, using the $2\times 2$ characteristic polynomial recorded alongside Lemma 7.5.
You have proved the Cayley-Hamilton theorem in this case: a matrix satisfies its own characteristic equation.

11. A rotation matrix on $\mathbb{R}^n$ is an orthogonal matrix of determinant $1$.
For any orthogonal $Q$, use Lemma 5.19 and the identity $\det M^T = \det M$ to derive $\det(Q-I) = \det(Q)\det(I-Q^T) = (-1)^n\det(Q)\det(Q-I)$, and conclude that $1$ is an eigenvalue whenever $(-1)^n\det Q \neq 1$: every rotation of $\mathbb{R}^3$ fixes an axis, and so does every orthogonal $2\times 2$ of determinant $-1$.
Exhibit an even-dimensional rotation with no eigenvalue $1$; the matrix $J$ beside Lemma 7.4 will serve.

12. Let $A\mathbf{v}=\lambda\mathbf{v}$ with $\mathbf{v}\neq\mathbf{0}$.
Show from Definition 7.10 that $e^A\mathbf{v}=e^\lambda\mathbf{v}$, using no diagonalizability whatever.
Now let $A$ have $n$ distinct real eigenvalues, and argue from the injectivity of $\exp$ on $\mathbb{R}$ and Lemma 7.4 that $e^{\lambda_1},\ldots,e^{\lambda_n}$ are *all* the eigenvalues of $e^A$.
Conclude by Lemma 7.5 that $\det e^A = e^{\operatorname{tr} A}$, and check this against the invertibility already recorded in (7.9).

13. Let $A$ be $2\times 2$ with distinct eigenvalues $\lambda_1,\lambda_2$, and set $P_1 = \frac{A-\lambda_2I}{\lambda_1-\lambda_2}$ and $P_2 = \frac{A-\lambda_1I}{\lambda_2-\lambda_1}$.
Verify $P_1+P_2=I$ and $\lambda_1P_1+\lambda_2P_2=A$ by algebra alone: these hold for any two distinct scalars and say nothing yet about eigenvalues.
Now derive $P_1P_2=0$ and $P_i^2=P_i$ from the factored identity $(A-\lambda_1I)(A-\lambda_2I)=0$, which is the $2\times 2$ Cayley-Hamilton theorem of Exercise 10 with the characteristic polynomial factored.
Conclude that every nonzero column of $P_i$ is an eigenvector for $\lambda_i$, found without solving a system.

14. For real numbers $x_1,\ldots,x_n$, the **Vandermonde matrix** $V$ has entries $v_{ij}=x_i^{\,j-1}$:

$$
V = \begin{bmatrix}
1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\
1 & x_2 & x_2^2 & \cdots & x_2^{n-1} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_n & x_n^2 & \cdots & x_n^{n-1}
\end{bmatrix}
$$

Show that $\det V = x_2-x_1$ when $n=2$, and prove that $\det V = (x_2-x_1)(x_3-x_1)(x_3-x_2)$ when $n=3$.
State the general formula these two suggest, and confirm that it vanishes exactly when two of the $x_i$ coincide — the only fact about $\det V$ that the proof of Theorem 7.15 consumes.

    > *Nota bene:* the nodes are a set, but the matrix demands an ordering of them.
    > Reorder and $\det V$ merely changes sign; the spectrum of $V$ changes outright.
    > It is an invariant of the list, not of the data.

15. Let $A$ be a real $2\times2$ matrix with $\operatorname{tr} A = 0$ and two distinct real eigenvalues.
Show that the eigenvalues are $\pm\lambda$ with $\lambda^2 = -\det A$, so that $\det A<0$ is forced, and describe the phase portrait of $\dot{\mathbf{x}} = A\mathbf{x}$.
Then compute $\det e^{At}$ from Lemma 7.13 and say what its value asserts about the way the flow moves areas.

16. Suppose $A$ is a $3\times3$ matrix with $\det(\lambda I - A) = \lambda^3 - 7\lambda^2 + 14\lambda - 8$, which is $-p_A(\lambda)$ in the sign convention of Definition 7.2 and has the same roots.
Without computing any matrix operations, determine $\operatorname{tr} A$ and $\det A$, and give an expression for $A^3$ in terms of lower powers of $A$.
The roots here are distinct and real, so the last of these needs no appeal to Cayley-Hamilton: justify it from Lemma 7.9 by verifying the identity on $\Lambda$ one diagonal entry at a time.

17. Solute circulates among three stirred tanks: tank $1$ feeds tank $2$ at rate $1$, tank $2$ feeds tanks $1$ and $3$ at rate $2$ each, and tank $3$ returns to tank $2$ at rate $1$, giving $\dot{\mathbf{x}}=A\mathbf{x}$ with $A = \begin{bmatrix}-1 & 2 & 0\\1 & -4 & 1\\0 & 2 & -1\end{bmatrix}$.
Zero column sums say $A^T(1,1,1)^T=\mathbf{0}$; prove $\det(A^T-\lambda I)=\det(A-\lambda I)$ and deduce that $0$ is an eigenvalue of $A$ too, no determinant computed.
Compute $\operatorname{ker} A$ and $\operatorname{ker} A^T$, and say which is a conservation law and which a family of equilibria.
Then find $\lim_{t\to\infty}\mathbf{x}(t)$ from $\mathbf{x}(0)=(10,0,0)^T$.
Finally, let a single probe report $y=x_2$ alone, and use Theorem 7.15 to prove that the initial profiles it can never see are exactly $\operatorname{ker}(A+I)$: one whole eigenspace, and nothing besides.

18. Deviations from a stirred-tank reactor's operating point obey $\dot{\mathbf{x}}=A\mathbf{x}$ with $A = \begin{bmatrix}4 & -2\\1 & 1\end{bmatrix}$ in $\textrm{hr}^{-1}$; raising the dilution rate to $D$ replaces $A$ by $A-DI$.
Find the eigenvalues and eigenvectors, then give the $D$ for which every deviation decays.
Show that $(A-DI)-\lambda I = A-(\lambda+D)I$: dilution shifts the spectrum rigidly and moves no eigenvector, buying rates and never shapes.
At $D=3$ the matrix is singular and the equilibria of Section 7.5 fill a line; identify it.

19. (Challenge.) Let $A$ have $n$ distinct real eigenvalues with eigenvectors $\mathbf{v}_1,\ldots,\mathbf{v}_n$, and let $W<\mathbb{R}^n$ satisfy $AW\subseteq W$.
For $\mathbf{w}=\sum_i c_i\mathbf{v}_i$ in $W$, the vectors $\mathbf{w},A\mathbf{w},\ldots,A^{n-1}\mathbf{w}$ lie in $W$ and express the $c_i\mathbf{v}_i$ through the Vandermonde matrix of Exercise 14 in the eigenvalues; invert it to place each $c_i\mathbf{v}_i$ in $W$.
Conclude that every invariant subspace is spanned by a subset of the eigenvectors, so there are exactly $2^n$ of them, against a continuum for $A=I$.

20. (Challenge.) Let $\lambda_1,\ldots,\lambda_m$ be the distinct real eigenvalues of $A\in\mathbb{R}^{n\times n}$, diagonalizable or not.
Suppose $\mathbf{u}_1+\cdots+\mathbf{u}_m=\mathbf{0}$ with each $\mathbf{u}_i\in\operatorname{ker}(A-\lambda_iI)$, and apply the commuting product $\prod_{j\neq i}(A-\lambda_jI)$, which kills every $\mathbf{u}_j$ with $j\neq i$ and scales $\mathbf{u}_i$ by $\prod_{j\neq i}(\lambda_i-\lambda_j)\neq 0$.
Deduce that the eigenspaces form a direct sum, so that $\sum_i\dim\operatorname{ker}(A-\lambda_iI)\leq n$: the whole family $A-\lambda I$ has only $n$ dimensions of kernel to spend.
Exhibit an $A$ making the inequality strict.

---


# Chapter 8. Eigenvalue Complexities

*"with songs of sweetest cadence to the turning spindle & reel"*

**Reality transcends real exponentials.** The theory of the previous chapter — with its real eigenvalues generating pure growth and decay — must confront a deeper truth: the world pulses with rhythm.
Heart cells oscillate in synchronized waves; animal populations surge and collapse; markets breathe between boom and bust.
This ubiquitous periodicity seems to defy our carefully constructed framework of eigenvalues and exponential solutions.

Yet mathematics bends rather than breaks.
The introduction of complex eigenvalues resolves our crisis of description, revealing oscillation as natural as growth or decay.
When eigenvalues coincide, still richer patterns emerge — polynomial terms multiplying our exponentials.
What appears first as complication reveals itself as essential structure, demanded by the very phenomena we seek to understand.
These complexities lead us beyond simple diagonalization to the best possible world of the Jordan canonical form, in which nearly identical eigenvalues can produce radically different behavior.

## 8.1 Complex Eigenvalues & Oscillation

The simple harmonic oscillator — a mass on a spring without damping — provides our first encounter with behavior that transcends real eigenvalues.
The equation of motion

$$
\frac{d^2x}{dt^2} + \omega^2x = 0
$$

has well-known solutions involving sines and cosines:

$$
x(t) = c_1\cos(\omega t) + c_2\sin(\omega t)
$$

Yet these solutions seem to conflict with our theory from Chapter 7, where all solutions emerged as combinations of real exponentials.
Converting to first-order form via $x_1=x$ and $x_2=\dot{x}$ yields

$$
\frac{d}{dt}\begin{pmatrix}x_1\\x_2\end{pmatrix} =
    \begin{bmatrix}
    0 & 1 \\
    -\omega^2 & 0
    \end{bmatrix}
    \begin{pmatrix}x_1\\x_2\end{pmatrix}
$$

The characteristic polynomial $\det(A-\lambda I) = \lambda^2 + \omega^2$ has roots $\lambda = \pm i\omega$  — our first encounter with complex eigenvalues.

**Example 8.1 (Complex Eigenvectors).** Consider the rotation matrix for angle $\pi/3$:

$$
R = \begin{bmatrix}
    \cos(\pi/3) & -\sin(\pi/3) \\
    \sin(\pi/3) & \cos(\pi/3)
    \end{bmatrix}
    =
    \begin{bmatrix}
    1/2 & -\sqrt{3}/2 \\
    \sqrt{3}/2 & 1/2
    \end{bmatrix}
$$

The characteristic equation is $\lambda^2 - \lambda + 1 = 0$, yielding eigenvalues $\lambda = \frac{1}{2} \pm i\frac{\sqrt{3}}{2} = e^{\pm i\pi/3}$.
For $\lambda = \frac{1}{2} + i\frac{\sqrt{3}}{2}$, we solve $(R-\lambda I)\mathbf{v}=\mathbf{0}$:

$$
-\frac{\sqrt{3}}{2}
    \begin{bmatrix}
    i & 1 \\
    -1 & i
    \end{bmatrix}
    \begin{pmatrix}
    v_1 \\ v_2
    \end{pmatrix}
    = \mathbf{0}
$$

yielding eigenvector $\mathbf{v} = (1,-i)^T$.
Though this eigenvector is complex, the matrix $R$ maps real vectors to real vectors.
The seeming paradox resolves by noting that $\mathbf{v}$ and its complex conjugate $\overline{\mathbf{v}}=(1,i)^T$ span $\mathbb{C}^2$, while their real and imaginary parts, $(1,0)^T$ and $(0,-1)^T$, span $\mathbb{R}^2$ over the reals.

Far from invalidating our theory, these complex eigenvalues illuminate it.
Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ reveals that our trigonometric solutions are simply complex exponentials in disguise:

$$
c_1\cos(\omega t) + c_2\sin(\omega t) =
    \Re\left(z_1e^{i\omega t} + z_2e^{-i\omega t}\right)
$$

for appropriate complex constants $z_1$ and $z_2$.
The oscillatory motion emerges from exponential solutions with purely imaginary exponents.

This insight generalizes through study of the fundamental $2\times 2$ matrix

$$
J = \begin{bmatrix}0 & -1 \\ 1 & 0\end{bmatrix} \tag{8.1}
$$

> *Nota bene:* The matrix $J=\sqrt{-I}$ is the matrix analogue of $i$ in complex arithmetic.

Direct computation gives $J^2=-I$.
Indeed, the matrix exponential $e^{Jt}$ can be computed directly from its series definition:

$$
\begin{array}{rcl}
    e^{Jt} &=& I + tJ + \frac{t^2}{2!}J^2 + \frac{t^3}{3!}J^3 + \frac{t^4}{4!}J^4 + \cdots \\
    &=& \left(I - \frac{t^2}{2!}I + \frac{t^4}{4!}I - \cdots\right) + \left(tJ - \frac{t^3}{3!}J + \frac{t^5}{5!}J - \cdots\right) \\
    &=& (\cos t)I + (\sin t)J
\end{array} \tag{8.2}
$$

This matrix-valued analog of Euler's formula explains the geometric action of $J$  — pure rotation in the plane.

More generally, consider a matrix $A$ with complex conjugate eigenvalues $\alpha\pm i\beta$. This matrix — like $J$ — cannot be diagonalized over the reals, but we can reduce it to a simplest form.

> Such matrices arise frequently in applications — the real part $\alpha$ controlling growth or decay while the imaginary part $\beta$ determines oscillation frequency.

**Lemma 8.2 (Complex Normal Form).** Any $2\times 2$ matrix $A$ with complex conjugate eigenvalues $\alpha\pm i\beta$ is similar to $\alpha I + \beta J$. That is, there exists an invertible matrix $P$ such that

$$
P^{-1}AP = \alpha I + \beta J
$$

*Proof.* Let $\mathbf{v} = \mathbf{u} + i\mathbf{w}$ be an eigenvector for eigenvalue $\alpha + i\beta$. Then

$$
A\mathbf{v} = (\alpha + i\beta)\mathbf{v} \implies A(\mathbf{u} + i\mathbf{w}) = (\alpha + i\beta)(\mathbf{u} + i\mathbf{w})
$$

Equating real and imaginary parts:

$$
A\mathbf{u} = \alpha\mathbf{u} - \beta\mathbf{w} \quad\text{and}\quad A\mathbf{w} = \beta\mathbf{u} + \alpha\mathbf{w}
$$

Set $P = [\mathbf{u}\;\;{-\mathbf{w}}]$.
This is invertible: were $\mathbf{u}$ and $\mathbf{w}$ dependent over $\mathbb{R}$, then $\mathbf{v}$ would be a complex multiple of a single real vector $\mathbf{p}$, and $A\mathbf{p}=(\alpha+i\beta)\mathbf{p}$ with $A$ and $\mathbf{p}$ real would force $\beta=0$.
Reading the two displayed equations as columns,

$$
AP = [\alpha\mathbf{u} - \beta\mathbf{w}\;\;\;{-\beta\mathbf{u}} - \alpha\mathbf{w}] = P(\alpha I + \beta J)
$$

yielding the desired similarity.
The order of the columns is not cosmetic: $[\mathbf{u}\;\mathbf{w}]$ delivers $\alpha I-\beta J$ instead, and with it a rotation running the wrong way. ∎

This **normal form** is the simplest possible presentation of a 2-by-2 matrix with complex eigenvalues.
Based on how similar matrices behave under exponentiation, our strategy for exponentiating $A$ is to change coordinates, exponentiate $\alpha I + \beta J$, then change coordinates back.
Euler's Theorem once again emerges.

**Lemma 8.3 (Euler's Theorem Redux).**

$$
e^{(\alpha I + \beta J)t} = e^{\alpha t}(\cos(\beta t)I + \sin(\beta t)J) \tag{8.4}
$$

*Proof.* Since $I$ and $J$ commute, we have:

$$
e^{(\alpha I + \beta J)t} = e^{\alpha t I + \beta t J} = e^{\alpha t I}e^{\beta t J}
$$

Having computed $e^{Jt}$ in Equation (8.2), we conclude:

$$
e^{(\alpha I + \beta J)t} = e^{\alpha t}I(\cos(\beta t)I + \sin(\beta t)J) = e^{\alpha t}(\cos(\beta t)I + \sin(\beta t)J)
$$

as claimed. ∎

This decomposition reveals how complex eigenvalues generate spiraling motion — exponential growth or decay modulated by rotation.

## 8.2 Repeated Eigenvalues

Not all transformations keep their eigenspaces distinct.
When eigenvalues coincide, the corresponding eigenvectors may merge or proliferate in subtle ways.
This collision of eigenspaces — this failure of perfect separation — leads to behavior richer than pure scaling, yet still simpler than complex oscillation.
Understanding such behavior requires carefully distinguishing between how often an eigenvalue appears and how many independent directions it controls.

Consider the matrices

$$
A_1 = \begin{bmatrix}2 & 0\\0 & 2\end{bmatrix}
    \quad\text{and}\quad
    A_2 = \begin{bmatrix}2 & 1\\0 & 2\end{bmatrix}
$$

Both have characteristic polynomial $(\lambda-2)^2$, yielding eigenvalue $\lambda=2$ with algebraic multiplicity 2.
Yet these matrices behave quite differently: $A_1$ acts by pure scaling in all directions, while $A_2$ combines scaling with shear.
This distinction emerges from the geometric multiplicity — the dimension of the eigenspace $\operatorname{ker}(A-2I)$.

**Definition 8.4 (Eigenvalue Multiplicities).** The **algebraic multiplicity** of an eigenvalue is its multiplicity as a root of the characteristic polynomial.
The **geometric multiplicity** is the dimension of its eigenspace $\operatorname{ker}(A-\lambda I)$.

For $A_1$ above, both multiplicities equal $2$ — every nonzero vector is an eigenvector with eigenvalue $2$.
For $A_2$, the algebraic multiplicity is $2$ but the geometric multiplicity is only $1$, as only multiples of $(1,0)^T$ are eigenvectors.
This deficiency of eigenvectors signals deeper structure that pure diagonalization cannot capture.

> The geometric multiplicity never exceeds the algebraic multiplicity.
> Theorem 8.8 will make this visible for a real $\lambda$: its blocks number the first and total the second.

When geometric and algebraic multiplicities differ, eigenvectors alone cannot span the space.
We require **generalized eigenvectors** — vectors $\mathbf{w}$ satisfying $(A-\lambda I)^k\mathbf{w}=\mathbf{0}$ for some $k>1$.
These vectors generate solutions involving polynomial terms multiplied by exponentials.

**Lemma 8.5 (Generalized Eigenspaces).** For a real eigenvalue $\lambda$ of $A$, the sequence of subspaces

$$
\operatorname{ker}(A-\lambda I) < \operatorname{ker}(A-\lambda I)^2 < \operatorname{ker}(A-\lambda I)^3 < \cdots
$$

stabilizes at dimension equal to the algebraic multiplicity of $\lambda$.

This is asserted here and earned later: Exercise 7 deduces it in three lines from the canonical form of Section 8.3, which is itself asserted.

> *BONUS!* This nesting of generalized eigenspaces — or any sequence of nested subspaces — is called a **filtration**.
> Filtrations are important in approximating large complicated spaces by graded low-dimensional entities, *cf.* Taylor polynomials, Fourier series, etc.

Note the language in which all of this transpires: each generalized eigenspace is a kernel, $\operatorname{ker}(A-\lambda I)^k$, just as each eigenspace is the kernel $\operatorname{ker}(A-\lambda I)$.
The failure of diagonalization is thereby measured by the Fundamental Theorem of Linear Algebra (Theorem 3.25) itself: as $k$ grows, the kernel of $(A-\lambda I)^k$ inflates, one power at a time, until it stabilizes at the algebraic multiplicity.
What the kernel gains, the image forfeits — $\operatorname{im}(A-\lambda I)^k$ deflates in step, rank-nullity fixing the sum of their dimensions at every $k$.
{ Diagonalizability over $\mathbb{R}$ is the statement that every eigenvalue is real and every such filtration stops at the first step.}
Both clauses are needed, and Exercise 8 shows that neither can be dropped.

**Example 8.6 (Generalized Eigenvectors).** For the matrix

$$
A = \begin{bmatrix}2 & 1 & 0\\0 & 2 & 1\\0 & 0 & 2\end{bmatrix}
$$

the eigenvalue $\lambda=2$ has algebraic multiplicity $3$ but geometric multiplicity $1$.
The chain of generalized eigenvectors

$$
\mathbf{w}_1 = \begin{pmatrix}1\\0\\0\end{pmatrix}, \quad
    \mathbf{w}_2 = \begin{pmatrix}0\\1\\0\end{pmatrix}, \quad
    \mathbf{w}_3 = \begin{pmatrix}0\\0\\1\end{pmatrix}
$$

satisfies

$$
(A-2I)\mathbf{w}_1 = \mathbf{0}, \quad
    (A-2I)\mathbf{w}_2 = \mathbf{w}_1, \quad
    (A-2I)\mathbf{w}_3 = \mathbf{w}_2
$$

This richer structure — generalized eigenvectors forming chains of increasing length — provides the key to understanding transformations with repeated eigenvalues.
Though such transformations resist diagonalization, their behavior remains comprehensible through careful analysis of how the generalized eigenspaces interact.

**Example 8.7 (Exponentiating a Simple Block).** Consider the matrix

$$
R = \begin{bmatrix}
    2 & 1 & 0 \\
    0 & 2 & 1 \\
    0 & 0 & 2
    \end{bmatrix}
    = 2I + N
    \quad : \quad
    N = \begin{bmatrix}
    0 & 1 & 0 \\
    0 & 0 & 1 \\
    0 & 0 & 0
    \end{bmatrix}
$$

The matrix $N$ is **nilpotent** — some power of it equals zero — with $N^3=0$ though $N^2\neq 0$.
Since $I$ commutes with anything, $e^{Rt} = e^{2It}e^{Nt} = e^{2t}e^{Nt}$, and nilpotency truncates the exponential series after three terms: $e^{Nt} = I + Nt + \frac{N^2t^2}{2!}$.
Computing $N^2$ and evaluating yields:

$$
e^{Rt}
    = e^{2t}
    \begin{bmatrix}
    1 & t & \frac{t^2}{2} \\
    0 & 1 & t \\
    0 & 0 & 1
    \end{bmatrix}
$$

The exponential growth $e^{2t}$ is modulated by polynomial terms in $t$  — the signature of a repeated eigenvalue.
The nilpotent part $N$ creates a cascade of influence up the superdiagonal, with each level inheriting the dynamics of those below it.

## 8.3 The Jordan Canonical Form

Repeated eigenvalues and their polynomial-exponential solutions point toward a deeper unity.
The Jordan canonical form is, at bottom, a census of kernels: one block for each **chain** of generalized eigenvectors — a list $\mathbf{v}_1,\ldots,\mathbf{v}_\ell$ with $(A-\lambda I)\mathbf{v}_1=\mathbf{0}$ and $(A-\lambda I)\mathbf{v}_{i+1}=\mathbf{v}_i$ — with the number of blocks of size at least $k$ for a *real* eigenvalue $\lambda$ equal to the increment $\dim\operatorname{ker}(A-\lambda I)^{k}-\dim\operatorname{ker}(A-\lambda I)^{k-1}$ in the filtration of the previous section.
*The filtration determines the form; the form remembers the filtration.*

**Theorem 8.8 (Jordan Canonical Form).** Every real square matrix $A$ is similar, by a real change of basis, to a block diagonal matrix $J$, called its **Jordan canonical form**:

$$
A = VJV^{-1} = V\begin{bmatrix}
    J_1 & 0 & \cdots & 0 \\
    0 & J_2 & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & J_m
    \end{bmatrix}V^{-1}
$$

where each **Jordan block** $J_i$ has one of two forms:

> This block structure mirrors that of the real case, with the superdiagonal $I$ matrices playing the role of the nilpotent matrix of ones, connecting a chain of $2\times 2$ complex blocks $C$.

1. For each chain of length $k$ at a real eigenvalue $\lambda$, the Jordan block is the $k$-by-$k$ matrix:


$$
J_i = \lambda I + N = \begin{bmatrix}
        \lambda & 1 & 0 & \cdots & 0 \\
        0 & \lambda & 1 & \cdots & 0 \\
        0 & 0 & \lambda & \ddots & \vdots \\
        \vdots & \vdots & \ddots & \ddots & 1 \\
        0 & 0 & \cdots & 0 & \lambda
        \end{bmatrix}
$$

2. For each chain of length $k$ at a conjugate pair $\alpha \pm i\beta$, with the convention $\beta>0$, the Jordan block is the $2k$-by-$2k$ block matrix

$$
J_i =
    \begin{bmatrix}
    C & I & 0 & \cdots & 0 \\
    0 & C & I & \cdots & 0 \\
    0 & 0 & C & \ddots & \vdots \\
    \vdots & \vdots & \ddots & \ddots & I \\
    0 & 0 & \cdots & 0 & C
    \end{bmatrix}
    \quad : \quad
    C =
    \begin{bmatrix}
    \alpha & -\beta \\
    \beta & \alpha
    \end{bmatrix}
    \quad : \quad
    I =
    \begin{bmatrix}
    1 & 0 \\
    0 & 1
    \end{bmatrix}
$$

where each entry is a 2-by-2 block.

An eigenvalue may carry several chains and therefore several blocks: for a real $\lambda$ the number of blocks is its geometric multiplicity and their sizes total its algebraic multiplicity, while a conjugate pair of multiplicity $k$ spends $2k$ real dimensions among its blocks.
With the convention $\beta>0$ in every complex block, the form $J$ is unique up to the ordering of blocks.

The columns of $V$ are the basis in which $A$ takes this form, written in the original coordinates: the change of basis matrix of Definition 4.9 once more, wearing the letter Chapter 7 gave it, and the $P$ of Lemma 8.2 under yet another.

> It would have been simpler to use the complex-valued Jordan form; only one type of block is needed.
> Given our motivation in working with solutions to ODEs, we have chosen to keep things real.

Each Jordan block corresponds to an eigenvalue (real or complex) and its associated generalized eigenvectors.
The size of the block equals the length of the longest chain of generalized eigenvectors for that eigenvalue.
When all eigenvalues are real and distinct (or real but with independent eigenvectors), each block is $1\times 1$ and we recover the diagonal form of Chapter 7.

The structure within each block illuminates the transformation's action.
For real eigenvalues, the matrix $N$ having ones on the superdiagonal and zeros elsewhere is nilpotent.
This nilpotence explains the finite polynomial terms we saw emerge in solutions.
For complex eigenvalues, the $2\times 2$ blocks encode rotation as seen in Section 8.1.

**Example 8.9 (Jordan Structure).** The matrix

$$
A = \begin{bmatrix}
    2 & 1 & 0 & 0 \\
    0 & 2 & 0 & 0 \\
    0 & 0 & 3 & 1 \\
    0 & 0 & 0 & 3
    \end{bmatrix}
$$

is already in Jordan form.
It has two Jordan blocks: a $2\times 2$ block for eigenvalue $\lambda=2$ and another for $\lambda=3$.
The generalized eigenvector chains have lengths 2 and 2 respectively.
Solutions will involve terms like $te^{2t}$ and $te^{3t}$ from each block's nilpotent part.

Powers and exponentials pass through the Jordan decomposition block by block.
Since $J$ is block diagonal, its exponential is also block diagonal:

$$
e^{At} = Ve^{Jt}V^{-1} = V\begin{bmatrix}
    e^{J_1t} & 0 & \cdots & 0 \\
    0 & e^{J_2t} & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & e^{J_mt}
    \end{bmatrix}V^{-1}
$$

For each real Jordan block $J_i = \lambda I + N$, we have:

$$
e^{J_it} = e^{\lambda t}e^{Nt} = e^{\lambda t}\left(I + Nt + \frac{N^2t^2}{2!} + \cdots + \frac{N^{k-1}t^{k-1}}{(k-1)!}\right)
$$

where $k$ is the size of that block, the length of its chain.
The series terminates because $N^k=0$.
A complex block splits the same way, and its exponential likewise carries $e^{Ct}$ along the diagonal with polynomial multiples of it above.
Exercise 3 carries this out.

**Example 8.10 (Full Jordan Decomposition).** Consider the matrix

$$
A = \begin{bmatrix}
    7 & -4 & 3 \\
    4 & -1 & 4 \\
    0 & 0 & 3
    \end{bmatrix}
$$

Its characteristic polynomial is $-(\lambda-3)^3$: eigenvalue $\lambda=3$ with algebraic multiplicity $3$.
Since $A-3I$ has rank $2$, the geometric multiplicity is $1$: one chain, one block.

$$
A = V\begin{bmatrix}
    3 & 1 & 0 \\
    0 & 3 & 1 \\
    0 & 0 & 3
    \end{bmatrix}V^{-1}
$$

where $V$ contains the generalized eigenvectors.
The single Jordan block indicates all generalized eigenvectors form one chain.
Solutions will involve terms $e^{3t}$, $te^{3t}$, and $t^2e^{3t}/2$.

> *Caveat:* Computing the generalized eigenvectors that effect the coordinate transformation $V$ is not always straightforward, as the following shows.

Assembling $V$ is another matter entirely.
Each chain starts at an eigenvector $\mathbf{v}_1$ and grows by solving $(A-\lambda I)\mathbf{v}_{i+1}=\mathbf{v}_i$; the filtration says how many chains there are and how long, but the vectors themselves must still be found one at a time.

**Example 8.11 (Jordan Transformation).** Consider the $5\times 5$ matrix:

$$
A = \begin{bmatrix}
    3 & 2 & 1 & 0 & 2 \\
    0 & 3 & -1 & 0 & 3 \\
    0 & 0 & 3 & 0 & -4 \\
    0 & 0 & 0 & 2 & 0 \\
    0 & 0 & 0 & 0 & 2
    \end{bmatrix}
$$

The characteristic polynomial $-(\lambda-3)^3(\lambda-2)^2$ reveals eigenvalues $\lambda_1=3$ with algebraic multiplicity 3 and $\lambda_2=2$ with algebraic multiplicity 2.
Let us systematically construct the Jordan decomposition.

For $\lambda_1=3$, it is clear that $\operatorname{ker}(A-3I) = \operatorname{span}(1, 0, 0, 0, 0)^T$, showing geometric multiplicity $1$.
Two more vectors are required to complete this chain.
Solving

$$
(A-3I)\mathbf{v}_2 = \begin{pmatrix}1\\0\\0\\0\\0\end{pmatrix}
    \quad\Rightarrow\quad
    \mathbf{v}_2 = \begin{pmatrix}a\\1/2\\0\\0\\0\end{pmatrix}
$$

(where $a$ is a free parameter) and then

$$
(A-3I)\mathbf{v}_3 = \begin{pmatrix}a\\1/2\\0\\0\\0\end{pmatrix}
    \quad\Rightarrow\quad
    \mathbf{v}_3 = \begin{pmatrix}b\\a/2+1/4\\-1/2\\0\\0\end{pmatrix}
$$

(where $b$ is another free parameter) provides our first chain $\mathbf{v}_3\mapsto\mathbf{v}_2\mapsto\mathbf{v}_1\mapsto\mathbf{0}$, each arrow an application of $A-3I$.

For $\lambda_2=2$, the kernel of $A-2I$ is two-dimensional, so geometric and algebraic multiplicity agree, with independent eigenvectors

$$
\mathbf{v}_4 = \begin{pmatrix}0\\0\\0\\1\\0\end{pmatrix}
    \quad : \quad
    \mathbf{v}_5 = \begin{pmatrix}-8\\1\\4\\0\\1\end{pmatrix}
$$

The transformation matrix $V$ assembles the chains as columns, longest chain first and each chain written from its eigenvector outward:

$$
V = [\mathbf{v}_1\;\mathbf{v}_2\;\mathbf{v}_3\;\mathbf{v}_4\;\mathbf{v}_5]
$$

No choice of $a$ or $b$ is needed: $\det V = -1/4$ whatever they are, and every choice produces the same Jordan form,

> *Caveat:* Uniqueness belongs to the form, not to the basis: $V$ is never determined by $A$, and the two free parameters here are only the visible part of that freedom.
> Exercise 17 counts how much of it there is.

$$
J = V^{-1}AV = \begin{bmatrix}
    3 & 1 & 0 & 0 & 0 \\
    0 & 3 & 1 & 0 & 0 \\
    0 & 0 & 3 & 0 & 0 \\
    0 & 0 & 0 & 2 & 0 \\
    0 & 0 & 0 & 0 & 2
    \end{bmatrix}
$$

The structure of $J$ reflects both the algebraic multiplicities of eigenvalues and the lengths of generalized eigenvector chains discovered in our systematic decomposition.
Reverse a chain and the ones fall below the diagonal instead of above it; the order within a chain is the one piece of bookkeeping that is not a convention.

Build chains only from eigenvectors lying in $\operatorname{im}(A-\lambda I)$; the rest head chains of length one.
The chain equation $(A-\lambda I)\mathbf{v}_{i+1}=\mathbf{v}_i$ is *not* always solvable, and for $A=\operatorname{diag}(2,2,2)+N$ with a single superdiagonal one, the eigenvector $\mathbf{e}_3$ heads no chain of length greater than one.
Choosing the right eigenvector to build from is the whole difficulty; once a solution exists it carries free parameters, and those never matter.

The Jordan form reveals that every linear transformation, viewed in the right coordinates, acts through a combination of:

1. Pure scaling (diagonal entries)

2. Rotation (complex conjugate blocks)

3. Cascading influence (superdiagonal ones)

## 8.4 Computing Eigenvalues

A practical question remains: how does one compute eigenvalues in practice?
Not from the characteristic polynomial.
A 100-by-100 matrix yields a degree-100 polynomial, far beyond the reach of standard root-finding, and merely expanding $\det(A-\lambda I)$ costs astronomical numbers of operations with catastrophic error growth.
Yet software returns the eigenvalues of a thousand-by-thousand matrix in seconds.
The resolution is iteration in place of solution, built on a factorization already in hand and on the one invariant we trust: similar matrices share eigenvalues.

**Definition 8.12 (QR Algorithm).** Given matrix $A_0=A$, the **QR algorithm** generates a sequence through:

1. Factor $A_k = Q_kR_k$ where $Q_k$ is orthogonal and $R_k$ is upper triangular with nonnegative diagonal

2. Form $A_{k+1} = R_kQ_k$ (reverse multiply)

Each iterate maintains similarity: $A_{k+1} = Q_k^TA_kQ_k$.

Though simple in description, this process harbors surprising properties.
When the eigenvalues have distinct magnitudes the sequence $\{A_k\}$ converges to upper triangular form, with eigenvalues appearing on the diagonal.
Ties in magnitude are not a technicality: on an orthogonal matrix the iteration stalls completely, never moving at all (Exercise 12).
Complex conjugate pairs, whose magnitudes are equal by construction, therefore never separate; they emerge instead as 2-by-2 blocks, while repeated eigenvalues maintain their multiplicities.
The algorithm effectively performs simultaneous power iteration on all eigenspaces, with the numerical stability that orthogonal transformations guarantee.

**Example 8.13 (Simple Iteration).** Consider the matrix

$$
A_0 = \begin{bmatrix}
    2 & 1 & 0 \\
    1 & 2 & 1 \\
    0 & 1 & 2
    \end{bmatrix}
$$

After five iterations we find:

$$
A_5 \approx \begin{bmatrix}
    3.4009 & 0.1367 & 0.0000 \\
    0.1367 & 2.0133 & 0.0043 \\
    0.0000 & 0.0043 & 0.5858
    \end{bmatrix}
$$

Each iterate is an orthogonal similarity of the last, so each is symmetric, as this one visibly is; the off-diagonal entries are what decay.
The diagonal entries are converging to $2+\sqrt2\approx 3.4142$, $2$, and $2-\sqrt2\approx 0.5858$  — roots of the characteristic polynomial $-\lambda^3+6\lambda^2-10\lambda+4$ that we never explicitly computed.

The $2$-by-$2$ block carrying a conjugate pair is *similar* to the normal form $\alpha I+\beta J$ of Lemma 8.2, but it is not usually equal to it: orthogonal similarity preserves the Frobenius norm, and a $2\times 2$ matrix with complex eigenvalues generally has a larger one than the scaled rotation it is similar to.
The block structure allows computation entirely in real arithmetic while still capturing complex behavior — a principle we first encountered when studying rotations in Section 8.1.

Modern implementations accelerate this iteration with shifts, cut its cost with implicit updates, and retire converged eigenvalues by deflation.

> *Example:* The shifted QR algorithm subtracts an estimate $\mu$ of an eigenvalue, iterates, then adds $\mu$ back — dramatically improving convergence when $\mu$ is well-chosen.

Orthogonality is what makes any of this safe: it preserves eigenvalues exactly, and the triangular limit displays them.
What the numerical process forfeits is the Jordan structure — eigenvalues emerge with high accuracy, chains do not emerge at all.
The ideas that illuminated eigenvalue structure theoretically provide the tools for finding them in practice.

## 8.5 Back to Basis

Our development of Jordan form illuminates the solution structure of higher-order linear differential equations.
The abstract machinery of generalized eigenvectors and complex blocks translates directly into concrete solution patterns — polynomial terms multiplying exponentials, trigonometric functions emerging from complex pairs.
This understanding completes our picture of basis solutions begun in Chapter 7, revealing why and how such patterns must arise.

Consider the general linear homogeneous differential equation of order $n$ with degree $n$ characteristic polynomial $p\in\mathcal{P}_n$:

$$
p(D)x = (D^n + a_{n-1}D^{n-1} + \cdots + a_1D + a_0)x = 0
$$

When the roots of $p(\lambda)=0$ are repeated, the companion matrix falls into Jordan blocks, and the basis solutions are read off the first row of the exponential of *each* block, computed in Section 8.3.

**Theorem 8.14 (Basis Solutions for Repeated Roots).** Let $\lambda$ be a root of the characteristic equation $p(\lambda)=0$ with algebraic multiplicity $k$.
Then:

1. For real $\lambda$, the functions


$$
\phi_j(t) = t^je^{\lambda t}, \quad j=0,1,\ldots,k-1
$$

    form a basis for the solution space corresponding to $\lambda$.

2. For complex $\lambda = \alpha \pm i\beta$, the functions


$$
\phi_j(t) = t^je^{\alpha t}\cos(\beta t), \quad \psi_j(t) = t^je^{\alpha t}\sin(\beta t), \quad j=0,1,\ldots,k-1
$$

    form a real basis for the solution space corresponding to the conjugate pair.

**Example 8.15 (Repeated Real Root).** The equation

$$
\frac{d^3x}{dt^3} - 3\frac{d^2x}{dt^2} + 3\frac{dx}{dt} - x = 0
$$

has characteristic polynomial $(\lambda-1)^3=0$. The basis solutions are

$$
\phi_0(t) = e^t, \quad \phi_1(t) = te^t, \quad \phi_2(t) = \frac{1}{2!}t^2 e^t
$$

matching exactly the patterns seen in the Jordan form of its companion matrix.
These emerge from the first row of the matrix exponential computed in our earlier example of a $3\times 3$ Jordan block.
The general solution is their linear combination:

$$
x(t) = c_0\phi_0(t) + c_1\phi_1(t) + c_2\phi_2(t)
$$

**Example 8.16 (Critical Damping).** The equation

$$
\frac{d^2x}{dt^2} + 2\gamma\frac{dx}{dt} + \omega^2x = 0 \tag{8.5}
$$

has roots $\lambda = -\gamma \pm \sqrt{\gamma^2-\omega^2}$.
For $0<\gamma<\omega$ these form a conjugate pair and the solution $e^{-\gamma t}\left(c_1\cos(\sqrt{\omega^2-\gamma^2}\,t) + c_2\sin(\sqrt{\omega^2-\gamma^2}\,t)\right)$ oscillates as it decays.
Set the damping to the precise value $\gamma=\omega$, where it exactly balances the natural frequency, and the characteristic polynomial

> *Example:* In mechanical systems, critical damping represents the fastest return to equilibrium without oscillation — all eigenvalues coincide at the negative point maximizing decay.

$$
\lambda^2 + 2\omega\lambda + \omega^2 = (\lambda+\omega)^2
$$

has repeated root $\lambda=-\omega$. The basis solutions are now

$$
\phi_1(t) = e^{-\omega t}
    \quad\text{and}\quad
    \phi_2(t) = te^{-\omega t}
$$

The transition between underdamped oscillation and pure decay manifests in this borderline case — the polynomial term $t$ replacing trigonometric functions as the roots merge.

**Example 8.17 (Repeated Complex Roots).** Consider the fourth-order equation

$$
\frac{d^4x}{dt^4} + 2\frac{d^2x}{dt^2} + x = 0
$$

whose characteristic polynomial $\lambda^4 + 2\lambda^2 + 1 = (\lambda^2+1)^2$ has root $\lambda=i$ with multiplicity 2.
From the complex solutions $t^je^{it}$, we obtain four real basis solutions:

$$
\phi_1(t) = \cos(t), \quad \phi_2(t) = \sin(t), \quad \phi_3(t) = t\cos(t), \quad \phi_4(t) = t\sin(t)
$$

These emerge directly from the first row of the exponentiated complex Jordan block, which Exercise 3 computes, with the polynomial coefficients modulating pure sinusoidal motion to create more intricate oscillatory patterns.

These examples illustrate the perfect correspondence between Jordan structure and scalar solutions.
The nilpotent part of each Jordan block manifests as powers of $t$, while complex blocks generate the trigonometric functions essential to modeling oscillation.
What appeared first as abstract matrix theory reveals itself as the natural language for describing physical motion.

—

## Pharmacokinetics & The Flip-Flop

A swallowed pill does not reach the blood all at once.
It dissolves in the gut, crosses into the plasma over minutes or hours, and is cleared by the liver and kidneys all the while.
The body is a cascade of compartments, and a drug must move through one to be emptied from the next.
The simplest such cascade is governed by two rates: the rate $k_a$ at which the drug is absorbed from gut to plasma, and the rate $k_e$ at which it is eliminated from the plasma altogether.

Let $g(t)$ measure the drug still in the gut and $p(t)$ the amount circulating in the plasma.
A dose $D$ is swallowed at once, so $g(0)=D$ and $p(0)=0$; thereafter each compartment loses drug at a rate proportional to its content, and whatever leaves the gut arrives in the plasma:

$$
\frac{d}{dt}\begin{pmatrix} g \\ p \end{pmatrix}
    = \begin{bmatrix} -k_a & 0 \\ k_a & -k_e \end{bmatrix}
    \begin{pmatrix} g \\ p \end{pmatrix}
    = A\begin{pmatrix} g \\ p \end{pmatrix}.
$$

The matrix is triangular, so its eigenvalues stand on the diagonal: $-k_a$ and $-k_e$.
Two compartments, two rates of decay — the machinery of Chapter 7 applies without complaint, so long as the two rates differ.

> *FIGURE:* [Plasma concentration $p(t)$ against time: a family of biexponential curves for several ratios $k_a/k_e$, collapsing onto the single curve $D\,k\,t\,e^{-kt}$ as the two rates meet. With $D=100$ mg and common rate $k=1~\mathrm{hr}^{-1}$, the limiting curve peaks at $p=100/e\approx 36.8$ mg one hour in.]

When $k_a \neq k_e$ the matrix is diagonalizable, and the plasma concentration is a difference of two exponentials:

$$
p(t) = \frac{k_a D}{\,k_a - k_e\,}\left(e^{-k_e t} - e^{-k_a t}\right).
$$

The curve climbs from zero as the drug floods in, crests where absorption and elimination momentarily balance, and falls away as the reservoir drains — the familiar arc of any dose taken by mouth, with its peak at $t_{\max} = \ln(k_a/k_e)/(k_a - k_e)$.

Which of the two exponentials is the tail?
Ordinarily a drug is absorbed faster than it is cleared, $k_a > k_e$, so the slow final decline reports the elimination rate $-k_e$ while the quick early rise reports absorption.
Reverse the inequality — let absorption be the slower, rate-limiting step, as it is for a depot injection or a sustained-release tablet — and the two exchange roles: the terminal slope now measures $k_a$, and $k_e$ hides in the rise.
Pharmacologists call this exchange **flip-flop kinetics**, and it is a real hazard of the trade, since the plasma curve alone cannot say which rate is which.
That last claim is algebra, not caution: interchanging $k_a$ and $k_e$ negates both the bracketed time-course $e^{-k_e t}-e^{-k_a t}$ and the prefactor, so the two signs cancel and the swap rescales only the amplitude, by a factor $k_e/k_a$ — and the amplitude is already tangled with the dose and the volume of distribution that any fit must estimate in any case.
The shape of the curve fixes the *pair* $\{k_a,k_e\}$; it does not label its members.

Now press the two rates together.
As $k_a \to k_e$ the prefactor $k_a/(k_a-k_e)$ runs to infinity while the difference $e^{-k_e t}-e^{-k_a t}$ collapses to zero, and the plasma concentration — a measured quantity, which cannot itself diverge — is caught in the indeterminate product.
L'H\^opital's rule in the variable $k_a$ resolves it.
Writing $k$ for the common rate,

$$
p(t) = D\,k\,t\,e^{-kt}.
$$

> *Recall:* The factor $t\,e^{-kt}$ has appeared once already, when the damped oscillator of Section 8.5 was tuned to critical damping.
> There a repeated root was arranged by design; here it arrives when two physical rates happen to agree.

A difference of exponentials has become a single exponential weighted by $t$.
The infinity in the prefactor was never in the pharmacology; it lived in the coordinates.
The two eigenvectors of $A$ — one confined to the plasma, the other carrying a share of the gut — draw together as the rates converge, until the gut-bearing eigenvector folds onto the plasma axis and the two become one.
The basis that diagonalized $A$ collapses to a single line, and the factor of $t$ is the scar it leaves.

The collapse is worth reading in the matrix itself.
At $k_a = k_e = k$,

$$
A = -kI + N,
    \qquad
    N = \begin{bmatrix} 0 & 0 \\ k & 0 \end{bmatrix},
    \qquad
    N^2 = 0,
$$

a single Jordan block: the eigenvalue $-k$ carries algebraic multiplicity two but geometric multiplicity one (Definition 8.4).
The nilpotent part $N$ holds the whole of the story.
Its kernel is the plasma axis $\operatorname{span}\{(0,1)^T\}$ — the lone eigenvector, the single initial state that decays as a pure exponential, drug already in the blood with an empty gut behind it.
Its image is that *same* plasma axis, since $N$ sends the gut direction $(1,0)^T$ to $k\,(0,1)^T$.
Here is the defect made geometric: $\operatorname{im} N = \operatorname{ker} N$.
The direction that absorption fills is exactly the direction that elimination empties.
Drug in the gut is therefore no eigenvector, and cannot be; it is a generalized eigenvector, the head of a chain

$$
\begin{pmatrix} 1 \\ 0 \end{pmatrix}
    \;\xrightarrow{\;N\;}\;
    k\begin{pmatrix} 0 \\ 1 \end{pmatrix}
    \;\xrightarrow{\;N\;}\;
    \mathbf{0},
$$

which is nothing but the drug's passage through the body read as a sequence of subspaces: gut absorbed into plasma, plasma cleared to nothing.
The chain has length two, and that length is precisely why the solution carries its factor of $t$.
A geometric multiplicity of one is not a technicality of the model; it is the statement that the substance has a single road through the body, and must travel all of it.

The pharmacologist meets the same collapse from the other side, in data.
Fitting a sum of two exponentials to plasma measurements is well posed only when the rates are cleanly separated; as $k_a$ approaches $k_e$ the two exponential curves grow proportional, the columns that carry them into the fit turn nearly parallel, and the eigenvector matrix that the fit must invert slides toward singularity.
The parameters lose their identifiability before they ever collide.
The Jordan point is not merely where the formula changes shape; it is where two rates, sought in a curve, become one.

{A drug whose only way in is its only way out leaves the matrix one eigenvector short; that absence is the factor of $t$.}

—

## Quadrotor Flight & Hovering

A fixed-wing aircraft is steadied by the air it moves through — disturb its pitch and the tail surfaces press it back toward trim — but a craft hanging motionless on four rotors moves through nothing.
No slipstream stiffens it; nothing pushes back.
That such a machine hovers at all, and why it cannot do so without a computer, is a diagnosis the Jordan form delivers whole.

Twelve numbers describe the craft near hover: three of position, three of velocity, three of attitude — a small tilt $\theta$ of the thrust axis toward the $x$-direction, a tilt $\phi$ toward $y$, and a heading $\psi$ — and the three rates of those angles.
Freeze the four motors at the setting whose collective thrust exactly cancels the craft's weight, neglect drag, and follow small deviations from a perfect hover.
A tilt leans the thrust vector without shortening it, and a horizontal acceleration appears: $\ddot{x} = g\theta$, and likewise $\ddot{y} = g\phi$, while the vertical equation keeps its cancellation through first order, $\ddot{z} = 0$.
Frozen motors exert no torques, so the tilts and the heading coast at whatever rates they possess: $\ddot{\theta} = \ddot{\phi} = \ddot{\psi} = 0$.

Write the twelve deviations as a state $\mathbf{x}\in\mathbb{R}^{12}$, so that the equations above read $\dot{\mathbf{x}} = A\mathbf{x}$.
They shear apart into four families that never mention one another: the pairs $(z,\dot z)$ and $(\psi,\dot\psi)$, and two quartets, the first being

$$
\frac{d}{dt}\begin{pmatrix} x \\ \dot{x} \\ \theta \\ \dot{\theta} \end{pmatrix}
    =
    \begin{bmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & g & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{bmatrix}
    \begin{pmatrix} x \\ \dot{x} \\ \theta \\ \dot{\theta} \end{pmatrix}
$$

with $(y,\dot y,\phi,\dot\phi)$ its mirror.
Measure tilt not in radians but in the acceleration it commands — coordinates $(x,\,\dot{x},\,g\theta,\,g\dot{\theta})$ — and this matrix becomes the $4\times 4$ Jordan block with eigenvalue zero, superdiagonal ones and all, while the two pairs are already $2\times 2$ blocks of the same species.
No chains need be excavated as in Example 8.11; the physics hands them over pre-assembled, and in these coordinates the full $12\times 12$ matrix is its own Jordan form:

$$
J = \begin{bmatrix}
    J_4 & 0 & 0 & 0 \\
    0 & J_4 & 0 & 0 \\
    0 & 0 & J_2 & 0 \\
    0 & 0 & 0 & J_2
    \end{bmatrix}
    \quad : \quad
    J_k = \text{the } k\times k \text{ Jordan block for } \lambda = 0 .
$$

> *Example:* An airplane in cruise makes the same decomposition with different anatomy: its pitch dynamics splits into two complex pairs — a quick, well-damped pitching bob, and the slow *phugoid*, a minute-long exchange of altitude for airspeed.
> Aircraft can be told apart by their Jordan forms.

Every eigenvalue of hover is zero: the characteristic polynomial is $\lambda^{12}$, and $A$ is nilpotent.
Section 8.3 closed by sorting linear evolution into three ingredients — scaling, rotation, cascade — and hover has renounced the first two.
Nothing grows, nothing decays, nothing circles.
All that remains is influence passed down chains: a tilt rate becomes a tilt, a tilt becomes an acceleration, an acceleration becomes a drift.
The flip-flop of the preceding pages met its Jordan block by coincidence, two rates happening to agree, dissolved by the least perturbation; this one is constitutional, immune to every parameter of the machine.

The kernel of $A$ is four-dimensional, spanned by the two horizontal positions, the altitude, and the heading.
These four eigenvectors are statements of indifference — the air does not care where the craft hovers, nor how high, nor which way it faces — and they exhaust the equilibria: the perfect hovers form not a point but a four-dimensional plane, $\operatorname{ker} A$ exactly, geometric multiplicity four set against algebraic multiplicity twelve.
The filtration of Lemma 8.5 climbs from there through dimensions $4$, $8$, $10$, $12$, and its increments $4,4,2,2$ perform the census of Section 8.3: chains of length at least one, two, three, four number $4,4,2,2$ in turn, forcing two blocks of size four and two of size two — the form $J$ above, recovered from kernel dimensions alone.
Better, each kernel in the tower is a regime of flight.
A state in $\operatorname{ker} A$ hovers forever.
$\operatorname{ker} A^2$ adds the steady motions — coasting level at constant velocity, climbing at a fixed rate, pirouetting at fixed $\dot\psi$ — trajectories linear in $t$.
$\operatorname{ker} A^3$ admits constant tilts, hence constant accelerations: its new trajectories are the parabolas of thrown stones.
And $\operatorname{ker} A^4$ is everything.
The degree of a trajectory's polynomial drift is the depth of its start in the filtration.

> *Terminology:* Control engineers call the system $\dot{\mathbf{w}} = J_k\mathbf{w}$ a **chain of integrators**: each coordinate is the running integral of the one after it.
> Hover is four such chains and nothing else.

Exponentiating block by block, the series of Section 8.3 terminates:

$$
e^{J_4 t} = \begin{bmatrix}
    1 & t & \frac{t^2}{2} & \frac{t^3}{6} \\
    0 & 1 & t & \frac{t^2}{2} \\
    0 & 0 & 1 & t \\
    0 & 0 & 0 & 1
    \end{bmatrix}
$$

and its first row spells out the longitudinal future:

$$
x(t) = x_0 + \dot{x}_0\, t + g\theta_0\,\frac{t^2}{2} + g\dot{\theta}_0\,\frac{t^3}{6} .
$$

This is a Taylor polynomial, and not by resemblance: in the Jordan coordinates the chain's entries are position and its first three derivatives, so the terminating exponential of a nilpotent block is a Taylor series that has run out of derivatives.
No exponential function appears anywhere in $e^{At}$.
Yet the hover fails.
Give the craft a tilt rate of a hundredth of a radian per second — half a degree each second, an error no eye would catch — and the cubic term carries it sixteen meters downrange within ten seconds.
The flip-flop left a factor of $t$ as the scar of a length-two chain; a chain of length four leaves $t^3$, and the drone, unstable with every eigenvalue at zero, does not blow up: it drifts, polynomially, out of the room.
The block sizes even rank the pilot's burdens: altitude and heading, chains of length two, err only linearly, while the horizontal plane owns the cubic.
The hard part of flying is sideways.

Here at last is why the machine carries gyroscopes and accelerometers and closes a feedback loop hundreds of times each second.
The four motors, in combination, command exactly four things — collective thrust and three torques — one entrance per chain, each at its head; the quadrotor is named for its four rotors, though it may as well be named for its four Jordan blocks, in exact correspondence.
Feedback threads measurement back into those entrances, replacing $A$ by a matrix whose eigenvalues sit strictly in the left half-plane: the chains broken, the drift arrested.
Choosing the gains well is the art of control theory and another book's subject; what linear algebra supplies is the diagnosis and the architecture — one small controller per block, pitch, roll, altitude, yaw, rather than one entangled loop in twelve dimensions.
Note, finally, what the pilot's stick commands: not position but tilt, two integrations upstream of where the drone actually is, so that every correction must ride the chain down before it lands.
The air will not push back.
The computer must.

*A quadrotor in hover is four chains of integrators regulated by the Jordan form.*

—

## Exercises: Chapter 8

1. The matrix $A = \begin{bmatrix}5 & -12\\3 & 5\end{bmatrix}$ has eigenvalues $5\pm 6i$.
Build the matrix $P$ of Lemma 8.2 from an eigenvector, minding the order of its columns, and use Lemma 8.3 to write $e^{At}$ in trigonometric form.
The orbits spiral outward, but not along circles: find the constant $c$ for which $e^{At}$ carries the ellipse $x^2+cy^2=1$ to $x^2+cy^2=e^{10t}$.

2. For the system

$$
\frac{d}{dt}\begin{pmatrix}x\\y\\z\\w\end{pmatrix} =
    \begin{bmatrix}
    -1 & 1 & 0 & 0 \\
    0 & -1 & 0 & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{bmatrix}
    \begin{pmatrix}x\\y\\z\\w\end{pmatrix}
$$

compute $e^{At}$ and find every solution that stays bounded as $t\to\infty$.
No eigenvalue has positive real part, yet the bounded solutions form a subspace of dimension three rather than all of $\mathbb{R}^4$.
Say which Jordan block is responsible, and why the block at $\lambda=-1$ is not.

3. The equation $x''''+4x''+4x=0$ has characteristic polynomial $(\lambda^2+2)^2$, so its companion matrix carries a single $4\times 4$ complex Jordan block: $C=\begin{bmatrix}0 & -\sqrt2\\\sqrt2 & 0\end{bmatrix}$ twice down the diagonal and $I$ on the superdiagonal.
Write that block as $\operatorname{diag}(C,C)+N$, check that the two summands commute and that $N^2=\mathbf{0}$, and exponentiate it with Lemma 7.11 and Lemma 8.3.
Read four basis solutions off the first row and match them against Theorem 8.14.

4. Run one step of the QR algorithm (Definition 8.12) by hand on $A_0 = \begin{bmatrix}2 & 1\\1 & 2\end{bmatrix}$.
Confirm that $A_1$ is symmetric again, say what forces it to be, and check that its off-diagonal entry has fallen from $1$ to $3/5$ while its diagonal has moved toward the true eigenvalues $3$ and $1$.

5. Let

$$
A = \begin{bmatrix}
    1 & -4 & 2 & 0 \\
    1 & 1 & 0 & 2 \\
    0 & 0 & 3 & 1 \\
    0 & 0 & 0 & 3
    \end{bmatrix}
$$

Its eigenvalues leave exactly two real Jordan canonical forms possible.
Decide which one holds from $\dim\operatorname{ker}(A-3I)$ alone, without ever constructing $V$.

6. Let $A$ be nilpotent, so that $A^m=\mathbf{0}$ for some $m$.
Show that every eigenvalue of $A$, real or complex, is zero, and conclude from Definition 7.2 that $p_A(\lambda)=(-1)^n\lambda^n$; the sign is not decoration, since $p_A(\lambda)=-\lambda^3$ for the $3\times3$ matrix with ones on the superdiagonal.
Cayley-Hamilton then runs the implication the other way and converts that polynomial into $A^n=\mathbf{0}$: a nilpotent matrix dies by the $n$th power, however large $m$ was.
Exhibit a $5\times5$ nilpotent whose fourth power is nonzero, so that the bound is sharp.

    > See the Chapter 7 exercises for the Cayley-Hamilton Theorem.

7. Grant Theorem 8.8, which this chapter asserts rather than proves, and write $A=VJV^{-1}$ with $\lambda$ a real eigenvalue of algebraic multiplicity $m$.
Prove Lemma 8.5 from it: $(A-\lambda I)^m=V(J-\lambda I)^mV^{-1}$, every block at $\lambda$ has size at most $m$ and is therefore annihilated, and every other block stays invertible.
Then say what goes wrong when $\lambda$ is not real, and why the lemma had to be stated for real eigenvalues only.

8. Prove the criterion asserted in Section 8.2: a real matrix is diagonalizable over $\mathbb{R}$ in the sense of Definition 7.7 exactly when all of its eigenvalues are real and $\dim\operatorname{ker}(A-\lambda I)^2=\dim\operatorname{ker}(A-\lambda I)$ for every one of them.
Use Lemma 7.8 in one direction and Lemma 8.5 in the other.
Then show that neither hypothesis can be dropped, taking a rotation for the first and $\begin{bmatrix}2 & 1\\0 & 2\end{bmatrix}$ for the second.

9. Let $A$ be real, with real eigenvalues $\lambda_j$ of multiplicity $m_j$ and conjugate pairs $\alpha_i\pm i\beta_i$ of multiplicity $k_i$.
Exponentiate the real Jordan form block by block — a nilpotent superdiagonal never reaches the diagonal, and Equation (8.4) gives $\operatorname{tr} e^{Ct}=2e^{\alpha t}\cos(\beta t)$ — and use the invariance of the trace under similarity to prove

$$
\operatorname{tr}(e^{At}) = \sum_j m_je^{\lambda_jt} + \sum_i 2k_ie^{\alpha_it}\cos(\beta_it) .
$$

Deduce that $\operatorname{tr}(e^{At})\to0$ when every $\lambda_j$ and every $\alpha_i$ is negative, and exhibit a matrix with no eigenvalue of positive real part for which it does not.

10. Let $A$ be a real $4\times4$ matrix with eigenvalues $3\pm 4i$ and $-2\pm i$.
Show from the real Jordan form that $e^{-3t}e^{At}$ stays bounded but has no limit as $t\to\infty$: the $-2\pm i$ part decays like $e^{-5t}$ while the $3\pm 4i$ part turns forever at rate $4$.
Show that along the times $t_k=\pi k/2$ it does converge, and that the limit is a projection of rank two.

11. A $6\times6$ matrix has characteristic polynomial $(\lambda+1)^4(\lambda-2)^2$, with $\dim\operatorname{ker}(A+I)=2$, $\dim\operatorname{ker}(A+I)^2=3$ and $\dim\operatorname{ker}(A-2I)=1$.
Ten Jordan canonical forms are consistent with the polynomial alone; say which one survives the three kernel dimensions, drawing each of its blocks as a chain of arrows $\bullet\to\cdots\to\bullet\to\mathbf{0}$.
One of the three kernel dimensions is redundant: find it, and say why no eigenvector need ever be computed.

12. Show that the rotation by $\theta\neq0,\pi$ is its own $Q$, with $R=I$, so that the QR algorithm returns it unchanged at every step and never reaches triangular form.
Explain why no orthogonal similarity could triangularize it in any case, by asking what sits on the diagonal of a real triangular matrix.
Conclude that the $2\times2$ blocks of Section 8.4 are not a failure of the algorithm but the best any real algorithm can do.

13. A real $4\times4$ matrix has characteristic polynomial $(\lambda^2-2\lambda+5)^2$, so the conjugate pair $1\pm2i$ is repeated.
Exhibit the two real Jordan forms Theorem 8.8 permits, and show that $A^2-2A+5I$ vanishes for one of them and not the other.
Neither is diagonalizable over $\mathbb{R}$; say which is diagonalizable over $\mathbb{C}$.

14. An instrument of mass $m=2$ kg hangs on a spring of stiffness $k=8$ N/m, with a dashpot contributing a force $-c\dot{x}$, so that $m\ddot{x}+c\dot{x}+kx=0$.
Find the damping $c$ at which the two roots collide, and write the pair of basis solutions Theorem 8.14 then supplies.
Show that in the overdamped case the slower decay rate is $\gamma-\sqrt{\gamma^2-\omega^2}$ with $\gamma=c/2m$ and $\omega^2=k/m$, and that it *decreases* as $c$ grows.

15. Two identical railcars of mass $m$, free to roll, are joined by a spring of stiffness $k$.
With $\omega^2=k/m$ and state $(x_1,x_2,\dot{x}_1,\dot{x}_2)$ the motion is $\dot{\mathbf{x}}=A\mathbf{x}$ for

$$
A = \begin{bmatrix}
    0 & 0 & 1 & 0\\
    0 & 0 & 0 & 1\\
    -\omega^2 & \omega^2 & 0 & 0\\
    \omega^2 & -\omega^2 & 0 & 0
    \end{bmatrix} .
$$

Show that $\lambda=0$ has algebraic multiplicity two and geometric multiplicity one, so that the real Jordan form carries a $2\times2$ block at zero beside a $2\times2$ block for the pair $\pm i\sqrt2\,\omega$ — both kinds of block in one matrix.
Identify the chain at $\lambda=0$ with the rigid-body motion, and say why the train drifts linearly in $t$ while the spring only oscillates.

16. The hovering craft discussed at the close of this chapter has longitudinal dynamics $\dot{\mathbf{x}}=M\mathbf{x}$ on the coordinates $(x,\dot{x},g\theta,g\dot{\theta})$, in which $M$ is the $4\times4$ Jordan block at zero.
Add a small aerodynamic drag on horizontal velocity, so that the second row now reads $\ddot{x}=-d\dot{x}+g\theta$, and compute the characteristic polynomial and $\dim\operatorname{ker} M^k$.
Conclude that zero now heads a chain of length three rather than four, and that the worst drift falls from $t^3$ to $t^2$.
Drag does not stabilize the hover; it demotes it by one power.

17. (Challenge.) Let $N$ be the $n\times n$ matrix with ones on the superdiagonal, and let $X$ commute with $N$.
Compare $NX$ and $XN$ entry by entry to show that $X$ must be upper triangular and constant along each diagonal, hence a polynomial in $N$: the matrices commuting with a single Jordan block form a space of dimension exactly $n$.
Deduce that if $V$ carries $A$ to a single Jordan block then so does $VX$ for every invertible such $X$, which is why the chain construction of Section 8.3 leaves free parameters — and why they never change the answer.

18. (Challenge.) Let every eigenvalue of $A$ be real, and prove that $A$ and $A^T$ have the same Jordan canonical form.
Apply $\operatorname{rank} M=\operatorname{rank} M^T$ to $M=(A-\lambda I)^k$ to show that the two have identical kernel dimensions at every eigenvalue and every power, and let the census of Section 8.3 do the rest.
This says nothing about their eigenvectors: exhibit a $2\times2$ where those differ.

---


# Chapter 9. Linear Iterative Systems

*"the sea of time & space beat round the rock in mighty waves"*

**Power begets power** in the iteration of linear transformations.
Each application of a matrix to a vector shifts weight toward dominant directions, channeling through preferred pathways until some natural balance emerges.
This fundamental process — the convergence of repeated transformation toward dominant modes — pervades both theory and computation.
Though simpler than the continuous flows and Jordan structures of previous chapters, these iterative systems harbor their own subtleties, where matrix structure fixes asymptotic fate.

The central idea lies in the connection between matrix powers and eigenvalues.
In the cleanest case, iterating a linear transformation leads to one eigenvalue dominating the results, dragging all vectors toward its eigendirection.
This process distills a matrix to its essential axis.
The power method for finding largest eigenvalues emerges naturally from the iteration itself, transforming a theoretical insight into a computational tool.

Yet not all matrices yield so readily to analysis.
Special structures — positivity constraints, probability conservation, symmetry — all complicate and enlighten our study.
The Perron-Frobenius theory reveals how positivity forces uniqueness of dominant directions.
Stochastic matrices preserve total measure while driving systems toward equilibrium states.
Graph matrices encode discrete topology through their spectrum.
Each class brings its own spectral features that shape long-term behavior.

## 9.1 At First Iteration

The Fibonacci sequence provides a first glimpse of the mysteries inherent in linear iteration.
Each number, the sum of its two predecessors, generates the sequence

$$
0,1,1,2,3,5,8,13,21,34,55,89,144,\ldots
$$

More striking than the numbers themselves is a hidden pattern: the ratio of consecutive terms approaches a fixed value $\varphi=(1+\sqrt{5})/2\approx 1.618$.
This convergence of ratios hints at deeper structure within linear recurrence relations.

> Yes, this is the so-called **golden ratio**.
> No, it is not here because it is ubiquitous in art & nature.
> It appears here because it is a dominant eigenvalue.

The Fibonacci rule $x_{n+2} = x_{n+1} + x_n$ represents a second-order recurrence.
Just as we transformed second-order differential equations to first-order systems in Chapter 7, we can recast this scalar sequence as a vector iteration.
Setting

$$
\mathbf{v}(n) = \begin{pmatrix}x_{n}\\x_{n+1}\end{pmatrix}
$$

transforms the recurrence into

$$
\mathbf{v}(n+1) = \begin{bmatrix}0 & 1\\1 & 1\end{bmatrix}\mathbf{v}(n)
$$

This first-order vector system captures the same evolution through matrix multiplication.
Its solution is clear if not clearly computable:

$$
\mathbf{v}(n) = A^n\mathbf{v}(0) = A^n\begin{pmatrix}
        0 \\ 1
    \end{pmatrix}
$$

More generally, a discrete-time linear system evolving has form and solution

$$
\mathbf{x}(n+1) = A\mathbf{x}(n)
    \quad \Rightarrow \quad
    \mathbf{x}(n) = A^n\mathbf{x}(0) \tag{9.1}
$$

where $A$ encodes the rules of evolution.
Just as differential equations $d\mathbf{x}/dt = A\mathbf{x}$ generate continuous flow through infinitesimal change, recurrence relations (9.1) create discrete trajectories through stepped iteration.

> *Historical Note:* This type of economic model is called a **Leontief input-output model**, after W. Leontief who developed it in the 1930s through detailed study of the American economy.
> His work on structural interdependence in production earned him the 1973 Nobel Prize in Economics.
> Though originally developed using data laboriously collected by hand, such models now inform economic planning worldwide through automated data collection and computation.

This discrete framework finds natural application in economic systems, where regular time periods (quarters, years) impose inherent granularity.
Consider an economy divided into $n$ sectors, each producing goods consumed partly by other sectors and partly as final output.
The **input-output matrix** $A=[a_{ij}]$ encodes production requirements: entry $a_{ij}$ represents the amount of sector $i$'s output needed to produce one unit of sector $j$'s output.
The evolution of such a system follows equation (9.1), where $\mathbf{x}(n)$ represents sector outputs in period $n$.

**Example 9.1 (Six-Sector Economy).** Consider an economy with six primary sectors: agriculture, energy, manufacturing, transportation, services, and technology.
The input-output matrix $A$ captures their interdependencies:

$$
A = \begin{bmatrix}
    0.15 & 0.08 & 0.10 & 0.05 & 0.20 & 0.05 \\
    0.25 & 0.30 & 0.35 & 0.40 & 0.20 & 0.30 \\
    0.10 & 0.15 & 0.20 & 0.25 & 0.10 & 0.20 \\
    0.15 & 0.12 & 0.15 & 0.15 & 0.10 & 0.08 \\
    0.20 & 0.25 & 0.15 & 0.15 & 0.25 & 0.30 \\
    0.15 & 0.15 & 0.20 & 0.15 & 0.25 & 0.20
    \end{bmatrix}
$$

Each column represents input requirements for one unit of sector output.
Producing one unit of manufacturing output (column 3) requires 0.10 units of agriculture and 0.35 of energy.
The columns sum to between $1.00$ and $1.15$ — a small surplus in most sectors, none at all in agriculture — and that surplus has a consequence under iteration.

Iterate, and a pattern declares itself.
Regardless of initial conditions, the relative sizes of sectors converge to fixed proportions approximately equal to $(0.22, 0.62, 0.34, 0.25, 0.48, 0.39)^T$, while the overall economy grows by roughly $1.09$ (or $9\%$) each period.

> *Foreshadowing:* The uniform growth rate emerging from Leontief models previews the Perron-Frobenius theory of positive matrices, where special structure ensures uniqueness of a dominant positive eigenvalue.

This tension — between the apparent complexity of sector-wise interaction and the simplicity of asymptotic behavior — runs throughout linear systems.
Complex coupling through multiple variables often reduces to simpler patterns driven by dominant modes.
Our task in this chapter is to understand this reduction, revealing how eigenstructure shapes the long-term character of linear iteration.

## 9.2 Dominance & Convergence

The mysterious convergence of Fibonacci ratios hints at deeper structure within matrix powers.
Just as the ratio sequence $x_{n+1}/x_n$ approaches the golden mean $\varphi$, general matrix iterations often display similar convergence — their behavior dominated by a single eigenvalue that drives long-term evolution.
This reduction of complex iteration to simple scaling reflects a fundamental principle: repeated linear transformation distills a matrix to its essential character.

Convergence is already written in Lemma 7.9, the representation of matrix powers.
For a diagonalizable matrix $A=V\Lambda V^{-1}$, powers take the form

$$
A^n = V\Lambda^n V^{-1}
$$

where $\Lambda^n$ simply raises each eigenvalue to the $n$th power.
When these eigenvalues differ in magnitude, larger ones grow faster than smaller ones, eventually dominating the iteration.
This observation leads to crucial definitions:

**Definition 9.2 (Spectral Radius and Dominance).** The **spectral radius** $\rho_A$ of a matrix $A$ is the maximum magnitude of its eigenvalues:

$$
\rho_A = \max\{|\lambda| : \lambda \text{ is an eigenvalue of }A\}
$$

An eigenvalue $\lambda_*$ is **dominant** if $|\lambda_*|=\rho_A$, no other eigenvalue has this magnitude, and $\lambda_*$ is a simple root of the characteristic polynomial.
Its eigenspace is then a line, and any spanning vector $\mathbf{v}_*$ is called the **dominant eigenvector**.

> Simplicity is not decoration.
> Without it $\operatorname{diag}(2,2,1)$ would have a dominant eigenvalue but no well-defined dominant eigen*direction*, and the lemma below would be false.
> Note also that a dominant eigenvalue of a real matrix must itself be real; the exercises say why.

**Lemma 9.3 (Dominant Convergence).** Let $A$ be diagonalizable with dominant eigenvalue $\lambda_*$ and corresponding eigenvector $\mathbf{v}_*$.
Then for any initial vector $\mathbf{x}_0$ with nonzero component $C$ along $\mathbf{v}_*$,

> *Think:* The notion of eigenvalue dominance holds sway in ODEs and continuous-time dynamics as well; however, it is not the spectral radius that matters for continuous-time dominance — it is the real parts of eigenvalues that count.
> Why?
> The differentiation operator $D$ is the natural logarithm of the shift operator $E$.

$$
\frac{A^n\mathbf{x}_0}{\lambda_*^n} \longrightarrow C\mathbf{v}_*
    \quad\text{as}\quad n\to\infty
$$

*Proof.* Let $A$ be $d\times d$ and index its eigenbasis $\{\mathbf{v}_1,\ldots,\mathbf{v}_d\}$ so that $\lambda_*=\lambda_1$; dominance says $|\lambda_k|<|\lambda_1|$ for every $k>1$.
Writing $\mathbf{x}_0=\sum_k c_k\mathbf{v}_k$ and applying $A^n$ yields

$$
\begin{aligned}
A^n\mathbf{x}_0
    & = \sum_{k=1}^d c_k\lambda_k^n\mathbf{v}_k
    = c_1\lambda_*^n\left(\mathbf{v}_* + \sum_{k=2}^d \frac{c_k}{c_1}\left(\frac{\lambda_k}{\lambda_*}\right)^n\mathbf{v}_k\right)
\end{aligned}
$$

The number of terms in the bracket is fixed at $d-1$, and each ratio $|\lambda_k/\lambda_*|<1$ decays geometrically, so the bracket tends to $\mathbf{v}_*$.
The constant $c_1$ is the component $C$. ∎

This convergence principle underlies the **power method** for computing dominant eigenvalues.
Starting with a random vector $\mathbf{x}_0$, repeated multiplication by $A$ followed by normalization yields convergence to the dominant eigendirection.
The rate of convergence is governed by the ratio of the second largest eigenvalue magnitude to the dominant one.

**Example 9.4 (Fibonacci redux).** For the Fibonacci matrix of the previous section,

$$
A = \begin{bmatrix}0 & 1\\1 & 1\end{bmatrix}
$$

the eigenvalues are $\varphi=(1+\sqrt{5})/2$ and $\psi=(1-\sqrt{5})/2$, with $|\varphi|>1>|\psi|$.
As $n\to\infty$, the powers of the dominant eigenvalue $\varphi^n$ grow exponentially faster than $|\psi|^n$, explaining why consecutive Fibonacci numbers approach ratio $\varphi$.

**Example 9.5 (Economic Convergence).** Returning to Example 9.1, the six-sector economy's input-output matrix $A$ has dominant eigenvalue $\lambda_*=\rho_A\approx 1.09$ with corresponding dominant eigenvector

$$
\mathbf{v}_* \approx (0.22, 0.62, 0.34, 0.25, 0.48, 0.39)^T
$$

normalized to unit length.
This explains both the $9\%$ growth rate and the fixed proportions observed empirically — the economy's structure forces convergence to these ratios regardless of initial conditions.

When $A$ is not diagonalizable, Jordan blocks complicate but do not fundamentally alter this picture.
A real Jordan block splits as a commuting sum $J=\Lambda+N$ with $N$ nilpotent, where $\Lambda$ is $\lambda I$ for a real eigenvalue and the $2\times2$ rotation-scaling $C$ of Theorem 8.8 repeated down the diagonal for a conjugate pair.
The binomial theorem for commuting matrices then gives

$$
J^n = \sum_{k\geq 0}\binom{n}{k}\Lambda^{n-k}N^k
$$

a finite sum, since $N$ is nilpotent.
The binomial coefficients are polynomial in $n$ and cannot overcome the exponential factor $\|\Lambda^{n-k}\|$, so the spectral radius still controls asymptotic behavior.
What the nilpotent part contributes is polynomial growth, never oscillation: oscillation is a statement about the *argument* of an eigenvalue, and enters only through a negative $\lambda$ or a genuine conjugate pair.

## 9.3 Positivity & Perron-Frobenius Theory

Certain natural quantities like mass, energy, and population are bound below by zero; probabilities and measures alike stubbornly refuse to venture into negative territory.
When linear transformations act on such intrinsically positive quantities, their matrices inherit special structure that shapes their spectral properties.

Consider a matrix $A=[a_{ij}]$ whose entries are all positive: $a_{ij}>0$ for all $i,j$.
Such matrices arise naturally in modeling coupled growth processes, where each component positively influences all others.
Such matrices possess uniquely simple spectral properties:

> *Historical Note:* O. Perron first proved these results for positive matrices in 1907. G. Frobenius extended them to the more general class of nonnegative irreducible matrices in 1912, capturing broader applications in economics and probability theory.

**Theorem 9.6 (Perron-Frobenius).** Let $A$ be a square matrix with all entries strictly positive.
Then $A$ has a dominant eigenvalue $\lambda_*=\rho_A>0$, with corresponding dominant eigenvector $\mathbf{v}_*>0$ having all positive components.
Moreover, any nonnegative eigenvector of $A$ must be a multiple of $\mathbf{v}_*$.

The proof of the theorem illuminates how positivity shapes spectral structure.
Consider iteration of $A$ on any positive vector $\mathbf{x}_0$.
The sequence of normalized vectors $\mathbf{y}_n = A^n\mathbf{x}_0/\|A^n\mathbf{x}_0\|$ remains positive, and a key inequality emerges:

$$
\min_i\frac{(A\mathbf{y})_i}{(\mathbf{y})_i}
    \, \leq \, \rho_A \, \leq \, \max_i\frac{(A\mathbf{y})_i}{(\mathbf{y})_i}
$$

holding for any positive vector $\mathbf{y}$.
These bounds, forced by positivity, trap the spectral radius.
A delicate argument shows the bounds converge as $n\to\infty$, yielding both the dominant eigenvalue and its positive eigenvector.
The impossibility of maintaining positivity through oscillation or decay then forces all other eigenvalues to have strictly smaller magnitude.

> There is a more incisive proof using algebraic topology, of which the author is particularly fond.

**Example 9.7 (Research Citation Network).** Consider six major research areas in computer science, with $b_{ij}$ the fraction of all citations *received by* papers in field $j$ that came *from* papers in field $i$:

$$
B = \begin{bmatrix}
    0.60 & 0.25 & 0.15 & 0.10 & 0.05 & 0.05 \\
    0.20 & 0.50 & 0.15 & 0.10 & 0.05 & 0.05 \\
    0.10 & 0.10 & 0.50 & 0.15 & 0.05 & 0.05 \\
    0.05 & 0.05 & 0.10 & 0.50 & 0.10 & 0.05 \\
    0.03 & 0.05 & 0.05 & 0.10 & 0.65 & 0.10 \\
    0.02 & 0.05 & 0.05 & 0.05 & 0.10 & 0.70
    \end{bmatrix}
    \quad : \quad
    \mathbf{v}_* \approx
    \begin{pmatrix}
        0.245 \\ 0.196 \\ 0.153 \\ 0.118 \\ 0.145 \\ 0.143
    \end{pmatrix}
$$

> *Nota bene:* These numbers are artificial, but the principle of using matrices to track citations is legit, and genuinely useful in many other contexts.

The fields are (1) Machine Learning, (2) Artificial Intelligence, (3) Computer Vision, (4) Robotics, (5) Systems & Networks, and (6) Theory, and the Perron-Frobenius eigenvector $\mathbf{v}_*$, normalized to unit sum, ranks their influence.
The ranking is not the ordering of row sums, and not the ordering of diagonal entries: Theory has the largest self-citation rate in the matrix and finishes fifth, while Robotics, the most application-bound field, receives the least reflected influence and finishes last.

The power of these results extends beyond strictly positive matrices.
The vocabulary that carries them, and that will accumulate hypotheses for the rest of the chapter, is worth fixing in one place.

**Definition 9.8 (Positivity Conditions).** Let $A=[a_{ij}]$ be a square matrix.
It is **nonnegative** if $a_{ij}\geq 0$ for all $i,j$, and **positive** if $a_{ij}>0$ for all $i,j$; both conditions are entrywise, imposed on the matrix itself.
A nonnegative $A$ is **irreducible** if no coordinate permutation transforms it into block triangular form, and **primitive** if some power $A^m$ has all entries strictly positive.

> *Terminology:* many authors say **regular** where this book says primitive.
> The condition is the same one; only the name differs.

These properties capture the connectivity of the underlying interaction network: irreducibility means every component eventually influences every other component, either directly or through intermediaries, while primitivity means that influence not only arrives everywhere, but arrives everywhere at the same time.
Primitivity implies irreducibility and is strictly stronger.

**Theorem 9.9 (Frobenius Extension).** Let $A$ be nonnegative and irreducible.
Then $\rho_A>0$ is an eigenvalue of $A$, simple, with a strictly positive eigenvector $\mathbf{v}_*$, and every nonnegative eigenvector of $A$ is a multiple of $\mathbf{v}_*$.
If moreover $A$ is primitive, then $\rho_A$ is *dominant* in the sense of Definition 9.2.

> *Caution:* irreducibility alone does not give dominance, and the difference is the whole content of this theorem.
> An irreducible matrix that cycles through its coordinates can carry several eigenvalues of magnitude $\rho_A$, and Lemma 9.3 is then unavailable; the next example is exactly this case.
> Primitivity is precisely the hypothesis that rules the cycling out, and Section 9.4 identifies the property of the underlying graph that supplies it.

**Example 9.10 (Catalytic Cycle).** Four substrates convert cyclically with rate matrix

$$
```latex
\begin{tikzcd}
    S_1 \arrow[r, "k_1"] & S_2 \arrow[d, "k_2"] \\
    S_4 \arrow[u, "k_4"] & S_3 \arrow[l, "k_3"]
\end{tikzcd}
```

    \quad : \quad
    A = \begin{bmatrix}
    0 & 0 & 0 & k_4 \\
    k_1 & 0 & 0 & 0 \\
    0 & k_2 & 0 & 0 \\
    0 & 0 & k_3 & 0
    \end{bmatrix}
$$

The characteristic polynomial of $A$ is
$\lambda^4-k_1k_2k_3k_4$, so the four
eigenvalues lie equally spaced on the circle in the complex plane of radius $\rho_A = (k_1k_2k_3k_4)^{1/4}$: the real pair $\pm\rho_A$ and the conjugate pair $\pm i\rho_A$.
Irreducibility does its work and no more: there is a strictly positive eigenvector for $\rho_A$, giving the balanced proportions among the substrates, but $A$ is not primitive and $\rho_A$ is not dominant.
The concentrations do not settle into those proportions; they cycle through them with period four.

## 9.4 Stochastic Matrices & Markov Chains

Many real-world processes involve transitions between states where probabilities govern the changes.
Examples include weather patterns shifting between sunny and rainy conditions, animal populations moving between territories, and genetic traits passing between generations.
Such processes, where future states depend only on the present and not on past history, lead naturally to the theory of Markov chains — a framework unifying discrete random processes through linear algebra.

**Definition 9.11 (Markov Chain).** A **Markov chain** is a sequence of random variables $\{X_n\}_{n\geq 0}$ taking values in a set of states $S$, satisfying the **Markov property**:

$$
\mathbb{P}(X_{n+1}=j|X_n=i,X_{n-1}=i_{n-1},\ldots,X_0=i_0)
    =
    \mathbb{P}(X_{n+1}=j|X_n=i)
$$

> *Nota bene:* Conditional probability is not a prerequisite here.
> Read $P$ as a matrix of probabilities and every argument in this section goes through unchanged.

The probability $p_{ij}$ of transitioning from state $j$ to state $i$ in one step defines an entry in the chain's **transition matrix** $P=[p_{ij}]$; the order of the indices is fixed by Definition 9.13, and it is the reverse of the one the conditional above reads most naturally.

The Markov property — that future depends on present but not past — transforms temporal evolution into matrix iteration.
To see this connection, we must first clarify what our vectors represent:

**Definition 9.12 (Probability Distribution).** A vector $\mathbf{x}=(x_1,\ldots,x_n)^T$ is a **probability distribution** if:

1. Nonnegativity: $x_i \geq 0$ for all $i$

2. Total probability: $\sum_{i=1}^n x_i = 1$

The entry $x_i$ represents the probability of being in state $i$.

The transition matrices of Markov chains must preserve these probability constraints, leading to our central object of study:

**Definition 9.13 (Stochastic Matrix).** A square matrix $P=[p_{ij}]$ is **stochastic** if it satisfies:

1. Nonnegativity: $p_{ij} \geq 0$ for all $i,j$

2. Column-stochasticity: $\sum_{i=1}^n p_{ij} = 1$ for all $j$

> *Caveat:* many authors use row-stochastic matrices, where the rows are probability distributions.
> If the term **stochastic** is used, always double-check which type is meant.

The entry $p_{ij}$ represents the probability of transitioning from state $j$ to state $i$ in one step.

The evolution of probabilities in a Markov chain follows our familiar iteration pattern:

$$
\mathbf{x}(k+1) = P\mathbf{x}(k)
$$

where $\mathbf{x}(k)$ represents the probability distribution across states at step $k$.
The stochastic constraints on $P$ ensure that if $\mathbf{x}(k)$ is a probability distribution, then $\mathbf{x}(k+1)$ will be as well.

**Example 9.14 (Weather Patterns).** Consider a simple model of daily weather transitions among three states: Sunny (S), Cloudy (C), and Rainy (R).
Historical data suggests transition probabilities:

$$
P = \begin{bmatrix}
    0.7 & 0.3 & 0.2 \\
    0.2 & 0.4 & 0.3 \\
    0.1 & 0.3 & 0.5
    \end{bmatrix}
$$

Reading down columns: from a sunny day (first column), the weather transitions to sunny with probability 0.7, cloudy with 0.2, and rainy with 0.1; similarly for transitions from cloudy or rainy states.

Given initial distribution $\mathbf{x}(0)=(1,0,0)^T$ representing certainty of sun today, tomorrow's distribution becomes:

$$
\mathbf{x}(1) = P\mathbf{x}(0) = (0.7,0.2,0.1)^T
$$

showing how probability disperses across states. After two days:

$$
\mathbf{x}(2) = P^2\mathbf{x}(0) = (0.57,0.25,0.18)^T
$$

suggesting convergence toward some equilibrium distribution.

The spectral properties of stochastic matrices determine their long-term behavior.
A Markov chain (and its transition matrix $P$) is **irreducible** if it is possible to reach any state from any other state (not necessarily in one step).
It is **aperiodic** if the greatest common divisor of the lengths of all return paths to a given state — the **period** of that state, and for an irreducible chain the same for every state — is 1.
An irreducible and aperiodic Markov chain is called **ergodic**.

Irreducibility has now been said twice, and the two sayings are one condition in two languages.
Draw the directed graph on the states, with an edge $j\to i$ wherever $p_{ij}>0$: a coordinate permutation putting $P$ in block triangular form corresponds exactly to a proper nonempty set of states out of which no edge leads, so that no permutation does so precisely when every state is reachable from every other — when the graph is strongly connected.
The matrix reading and the graph reading of Definition 9.8 never diverge.
What aperiodicity adds is the second Perron-Frobenius hypothesis: *a nonnegative irreducible matrix is primitive precisely when it is aperiodic*, so that ergodic is nothing other than primitive, spelled for chains.
Exercise 15 supplies what follows from primitivity, and exhibits an irreducible matrix that fails to be primitive.

Every column-stochastic matrix has a particularly important eigenvalue:

**Lemma 9.15 (Stochastic Spectral Radius).** For any stochastic matrix $P$:

1. $1$ is an eigenvalue of $P$.

2. The spectral radius $\rho_P = 1$.

3. All other eigenvalues satisfy $|\lambda| \leq 1$.

4. If $P$ is irreducible, the eigenvalue $1$ is simple (algebraic multiplicity one).
    If $P$ is ergodic (irreducible and aperiodic), then $1$ is the unique eigenvalue of $P$ with magnitude $1$.
    If $P$ is irreducible but periodic with period $h>1$, there are $h$ distinct eigenvalues on the unit circle.

*Proof.* First, observe that $\mathbf{1} = (1, 1, \ldots, 1)^T$ is an eigenvector of $P^T$ with eigenvalue 1, since each row of $P^T$ (column of $P$) sums to 1:

$$
P^T\mathbf{1} = \mathbf{1}
$$

Since the eigenvalues of $P$ and $P^T$ are identical, this proves that 1 is an eigenvalue of $P$ as well.

For the spectral radius bound, work with $P^T$, whose spectrum is the same and whose *rows* sum to one.
Let $P^T\mathbf{v}=\lambda\mathbf{v}$ and let $i$ index a largest $|v_i|$.
Then $\lambda v_i = \sum_{j} p_{ji}v_j$, and taking absolute values,

$$
|\lambda||v_i| = \Bigl|\sum_{j=1}^n p_{ji}v_j\Bigr| \leq \sum_{j=1}^n p_{ji}|v_j| \leq |v_i|\sum_{j=1}^n p_{ji} = |v_i|
$$

the last equality being column-stochasticity of $P$.
Since $|v_i| > 0$, we have $|\lambda| \leq 1$, establishing that $\rho_P = 1$.
The refinements in point 4 are Theorem 9.9 restated for stochastic matrices; the exercises prove the ergodic case, which is the one this chapter uses. ∎

A distribution $\mathbf{\pi}$ satisfying $P\mathbf{\pi}=\mathbf{\pi}$ is called **stationary** — it remains unchanged under the transition rules.
For irreducible chains, such a distribution is unique.

> *Recall:* $P\mathbf{\pi}=\mathbf{\pi}$ says precisely that $\mathbf{\pi}\in\operatorname{ker}(P-I)$.
> Every eigenspace is a kernel (Chapter 7); this one, normalized to unit sum, will rank the entire Web before the chapter is out.

For ergodic chains, iteration from any initial distribution converges to this stationary state:

**Theorem 9.16 (Markov Convergence).** Let $P$ be an ergodic stochastic matrix (i.e., irreducible and aperiodic). Then:

1. There exists a unique probability vector $\mathbf{\pi}$ such that $P\mathbf{\pi}=\mathbf{\pi}$.
    This $\mathbf{\pi}$ is called the **stationary distribution**.

    > If $P$ is irreducible but periodic, $P^k\mathbf{x}(0)$ does not converge to a single vector but may exhibit periodic limits or converge in Cesaro mean to $\mathbf{\pi}$.

2. For any initial probability vector $\mathbf{x}(0)$:


$$
\lim_{k\to\infty} P^k\mathbf{x}(0) = \mathbf{\pi}
$$

3. The rate of convergence is governed by the magnitude of the second-largest eigenvalue (i.e., the largest $|\lambda|$ such that $|\lambda|<1$).

The four conditions now in play are nested rather than parallel: entrywise positivity implies primitivity, primitivity implies irreducibility, and for a stochastic matrix primitivity is exactly ergodicity.
Irreducibility is the base and buys a simple $\rho_A$ with a positive eigenvector; primitivity buys dominance on top of it, and with dominance, convergence.
Entrywise positivity is a convenient sufficient condition for primitivity rather than a further strengthening: it is easy to check and buys nothing that primitivity does not already give.

*[Figure omitted]*

**Example 9.17 (Weather Equilibrium).** Returning to our weather model, the matrix $P$ is irreducible (all entries are positive) and aperiodic (e.g., $p_{11}>0$).
Solving $P\mathbf{\pi}=\mathbf{\pi}$ subject to $\sum \pi_i = 1$ yields the stationary distribution exactly:

$$
\mathbf{\pi} = \left(\tfrac{21}{46},\tfrac{13}{46},\tfrac{6}{23}\right)^T \approx (0.457,0.283,0.261)^T
$$

Thus in the long run, regardless of initial conditions, we expect about 45.7% sunny days, 28.3% cloudy, and 26.1% rainy.
The characteristic polynomial factors as $(\lambda-1)(50\lambda^2-30\lambda+3)/50$, so the eigenvalues are $1$ and $(3\pm\sqrt3)/10$, that is $\approx 0.473$ and $\approx 0.127$.
The second-largest magnitude $\approx 0.473$ indicates rapid convergence to this equilibrium.

> *Example:* Hardy-Weinberg equilibrium is the stationary distribution of a rank-one stochastic matrix, and is therefore reached in a single generation.

Special structures within stochastic matrices reveal additional features.
A matrix $P$ is **doubly stochastic** if both its columns and rows sum to one — probability is conserved in both forward and backward time.
Such matrices arise naturally in physical systems where transitions conserve some underlying quantity.
The uniform vector $\pi_i=1/n$ is then always stationary; the exercises settle when it is the only one.

**Example 9.18 (Random Walk on a Graph).** Consider a particle moving randomly on an undirected graph with $n$ vertices, where at each step it moves with equal probability to any adjacent vertex.
The transition probabilities form a stochastic matrix $P=[p_{ij}]$ where

$$
p_{ij} = \begin{cases}
    1/\deg(j) & \text{if vertices $i$ and $j$ are adjacent} \\
    0 & \text{otherwise}
    \end{cases}
$$

Here $\deg(j)$ denotes the degree (number of neighbors) of vertex $j$.
This choice makes $P$ column-stochastic, though not necessarily symmetric.
However, the relationship $\deg(j)p_{ij} = \deg(i)p_{ji}$ holds due to the undirected nature of the graph.

*[Margin figure omitted]*

If the graph is connected and not bipartite — which for this walk implies aperiodicity — the chain is ergodic.
For the six-vertex graph shown, the stationary distribution is $\mathbf{\pi}=(4,3,1,2,3,1)^T/14$, proportional to the degrees: the walk spends more of its time where more edges arrive, a principle underlying many network centrality measures.

## 9.5 Symmetric Matrices & Spectra

The simple structural condition of symmetry ($A^T=A$) constrains the entire spectrum: every eigenvalue real, every pair of eigenspaces perpendicular.

Consider, for example, the matrices

$$
\begin{bmatrix}
    4 & 1 & 2 \\
    1 & 3 & -1 \\
    2 & -1 & 5
    \end{bmatrix}
    \quad\text{or}\quad
    \begin{bmatrix}
    3 & -2 & 0 \\
    -2 & 5 & -1 \\
    0 & -1 & 4
    \end{bmatrix}
$$

Though their entries differ markedly, they share the crucial feature of symmetry about their diagonals.
This visible structure reveals deeper patterns: both matrices share spectral properties that emerge not from the specific numbers but from the symmetric pattern itself.

**Lemma 9.19 (Orthogonal Diagonalization of Symmetric Matrices).** Let $A$ be a real symmetric matrix. Then:

1. All eigenvalues of $A$ are real

2. Eigenvectors corresponding to distinct eigenvalues are orthogonal

3. $A$ has an orthonormal basis of eigenvectors

Thus $A$ can be orthogonally diagonalized: $A=Q\Lambda Q^T$ where $Q$ is orthogonal and $\Lambda$ is diagonal with real entries.

> *Foreshadowing:* This lemma is the shadow of a greater result.
> Its proof, its geometry, and its consequences open Chapter 10, where as the **Spectral Theorem** it will generate the singular value decomposition — the same structure, freed from squareness.

This result — that symmetry forces reality of eigenvalues and orthogonality of eigenvectors — transforms abstract matrices into concrete geometric objects.
Each symmetric matrix acts by stretching or compressing space along perpendicular axes determined by its eigenvectors.
The eigenvalues measure the scale of this deformation, providing a coordinate-independent description of the transformation's action.

The **quadratic form** associated with symmetric $A$ reveals another face of this structure:

$$
q(\mathbf{x}) = \mathbf{x}^TA\mathbf{x}
$$

This scalar function measures a kind of generalized "energy" in direction $\mathbf{x}$.
Symmetric matrices are graded by the sign it takes: $A$ is **positive definite** when $q(\mathbf{x})>0$ for every $\mathbf{x}\neq\mathbf{0}$, and **positive semidefinite** when $q(\mathbf{x})\geq0$ for all $\mathbf{x}$.

> *Caution:* this is the chapter's second sense of *positive*, and it is a condition on the form $q$, not on the entries.
> The positive matrices of Definition 9.8 are positive entrywise, and neither sense implies the other.

Each condition says exactly that every eigenvalue is positive, respectively nonnegative — an inner product's defining axiom from Chapter 5, read off a spectrum — and the exercises supply the reason.

**Example 9.20 (Correlation & Inertia).** Given $n$ measurements of $d$ variables, the correlation matrix $[R]=[R_{ij}]$ records standardized relationships between pairs: symmetric, with ones down the diagonal.
It is, moreover, a Gram matrix in the sense of Chapter 5: writing $\hat{\mathbf{x}}_i$ for the centered, normalized $i$th variable, $R_{ij} = \langle\hat{\mathbf{x}}_i,\hat{\mathbf{x}}_j\rangle$  — the matrix of pairwise cosine similarities.
Its eigenvectors group correlated variables; its small eigenvalues mark redundancy.

> In mechanics, $\mathcal{I}$ is called the *inertia tensor*.
> The intuitive fact that asymmetric massive bodies have three "natural" axes of rotation that are all orthogonal is a consequence of Lemma 9.19.

Weight the same construction by mass and it becomes the inertia matrix $\mathcal{I}$ of a solid body, whose eigenvectors are the principal axes and whose eigenvalues measure extent along them.
A drinking glass has one large eigenvalue along its length and two smaller equal ones across its circular section; a book has three distinct ones.
Chapter 11 builds both matrices in earnest and reads their spectra.

> *Think:* Given only pairwise distances between points, can we reconstruct their relative positions?
> This inverse problem is akin to trying to deduce the shape of a molecule from measurements between its atoms, or inferring a social network's structure from similarities between individuals.

**Example 9.21 (Distance Matrices).** Consider a collection of $n$ abstract points with only their pairwise distances known.
The squared distances form a symmetric matrix $D=[d_{ij}]$ where $d_{ij}$ represents the squared distance between points $i$ and $j$.
Though we cannot visualize these points directly, their geometric structure hides within $D$.

The centering matrix $H=I-\frac{1}{n}[1]$, where $[1]$ denotes the matrix of all ones, builds from $D$ the matrix $B=-\frac{1}{2}HDH$.
While $D$ itself may not be positive definite, $B$ is symmetric, and it is positive semidefinite precisely when the $d_{ij}$ really are squared Euclidean distances of some point set.
When they are, the positive eigenvalues of $B$ count the dimensions the cloud requires, its eigenvectors supply the coordinates, and the decay of its spectrum says how few dimensions would nearly do: position recovered from distance alone, a construction known as **classical multidimensional scaling**.

The extremal properties of quadratic forms associated with symmetric matrices provide another perspective on their structure:

> *Aside:* The Rayleigh quotient is the risk of a portfolio.
> For a covariance matrix $[C]$ and weights $\mathbf{w}$ summing to one, $\mathbf{w}^T[C]\mathbf{w}$ is the variance of the blend, and the lemma bounds it by the extreme eigenvalues.
> Chapter 11 takes up covariance and its risk factors properly.

**Lemma 9.22 (Extreme Values).** For symmetric $A$, the **Rayleigh quotient** $q(\mathbf{x})=\mathbf{x}^TA\mathbf{x}/\mathbf{x}^T\mathbf{x}$, which on the unit sphere $\|\mathbf{x}\|=1$ is just $\mathbf{x}^TA\mathbf{x}$, satisfies:

1. Its maximum is $\lambda_{\max}$, attained at an eigenvector for $\lambda_{\max}$

2. Its minimum is $\lambda_{\min}$, attained at an eigenvector for $\lambda_{\min}$

3. Its range is the whole interval $[\lambda_{\min},\lambda_{\max}]$

## 9.6 Networked Behavior & Consensus

The flow of influence through networks shapes everything from opinion formation to economic behavior to artificial intelligence.
When agents in a network update their states based on their neighbors' values, complex global patterns can emerge from simple local rules.
Understanding such collective behavior requires uniting the spectral theory of Sections 9.3--9.5 with the concrete topology of interaction networks.

**Definition 9.23 (Graph Laplacian).** For an undirected graph with $n$ vertices, the **graph Laplacian** $L=[L_{ij}]$ is an $n\times n$ matrix whose entries are:

$$
L_{ij} = \begin{cases}
        d_i & \text{if }i=j \\
        -1 & \text{if vertices }i\text{ and }j\text{ are connected} \\
        0 & \text{otherwise}
    \end{cases}
$$

where $d_i$ denotes the **degree** of vertex $i$  — the number of edges connected to it.
Equivalently, if $D=\operatorname{diag}(d_1,\ldots,d_n)$ is the **degree matrix** and $A=[a_{ij}]$ is the **adjacency matrix** with $a_{ij}=1$ for connected vertices and $0$ otherwise, then $L=D-A$.

This matrix, though simple to define, carries the network's topology in its spectrum: the count of components, the strength of connection, the natural fault lines.
Its action on a vector measures how quantities diffuse across edges, making it fundamental to understanding collective dynamics.

> *Nota bene:* the sum condition here is on *rows*, not columns.
> A transition matrix pushes a *distribution* forward, so probability is conserved down each column; an averaging matrix replaces a *value* by a weighted mean, so the weights sum to one across each row.
> Definition 9.13 fixes the column convention for this book, so the $W$ of this section is $P^T$.

Consider a network of $n$ agents, each holding a real value $x_i(t)$ that evolves in discrete time through local averaging:

$$
x_i(t+1) = \sum_{j} w_{ij}x_j(t)
    \qquad\text{with}\qquad
    \sum_j w_{ij} = 1
$$

where the weights $w_{ij}$ are nonnegative, supported on agent $i$ and its neighbors, and represent interaction strengths.
Writing $\mathbf{x}(t)$ for the vector of states, this local update rule becomes matrix iteration $\mathbf{x}(t+1) = W\mathbf{x}(t)$, with $W=D^{-1}A$ when neighbors are weighted equally, or $W=I-\epsilon L$ when the step is gradient descent on disagreement.

**Example 9.24 (Five Cohorts).** Five cohorts on social media — not individuals, but interacting groups with aggregate opinions — pass influence among themselves as shown, groups 1 and 4 the best connected:

$$
P = \begin{bmatrix}
    1/4 & 1/2 & 0 & 1/4 & 1/3 \\
    1/4 & 1/2 & 0 & 0 & 0 \\
    0 & 0 & 1/2 & 1/4 & 0 \\
    1/4 & 0 & 0 & 1/4 & 1/3 \\
    1/4 & 0 & 1/2 & 1/4 & 1/3
    \end{bmatrix}
$$

*[Margin figure omitted]*

The matrix is column-stochastic, hence a transition matrix in the sense of Definition 9.13: it does not average opinions, it redistributes them.
Its stationary distribution is $\mathbf{\pi}=\left(\tfrac{16}{57},\tfrac{8}{57},\tfrac{6}{57},\tfrac{12}{57},\tfrac{15}{57}\right)^T$, and from the polarized start $\mathbf{x}(0)=(1,-1,-1,1,-1)^T$, whose entries sum to $-1$, the iteration converges to $-\mathbf{\pi}$: five different numbers, not one.
That is a ranking, not a defect.
Iterate the transpose instead, whose rows sum to one, and the same start converges to the single value $\mathbf{\pi}^T\mathbf{x}(0)=-1/57$, held by every group.
The theorem below carries both readings at once.

When the matrix is ergodic — irreducible and aperiodic, in the sense of Section 9.4 — one phenomenon occurs, and it wears two faces depending on which index the weights are normalized over.
Both follow from the Perron-Frobenius theory of Section 9.3, and they are transposes of one another.

**Theorem 9.25 (Redistribution & Consensus).** Let $P$ be an $n\times n$ ergodic stochastic matrix with stationary distribution $\mathbf{\pi}$, and let $W=P^T$, so that $W$ is the averaging matrix whose rows sum to one.
For any $\mathbf{x}(0)\in\mathbb{R}^n$:

1. $\displaystyle\lim_{t\to\infty} P^t\mathbf{x}(0) = \Bigl(\sum_{i=1}^n x_i(0)\Bigr)\mathbf{\pi}$: the initial total survives and is **redistributed** in the proportions $\mathbf{\pi}$. Nobody agrees with anybody; $\mathbf{\pi}$ is a ranking.

2. $\displaystyle\lim_{t\to\infty} W^t\mathbf{x}(0) = \bigl(\mathbf{\pi}^T\mathbf{x}(0)\bigr)\mathbf{1}$: every agent arrives at the **same** value, the $\mathbf{\pi}$-weighted average of the initial states. This is consensus, and $\mathbf{\pi}$ measures influence over its location.

Both limits are approached geometrically at rate $|\lambda_2|$, the second-largest eigenvalue magnitude, which $P$ and $W$ share.

This theorem connects network structure to collective behavior through spectral properties.
The entries of $\mathbf{\pi}$ measure the relative influence of each node — on where the consensus lands, or on how the total is split — while $|\lambda_2|$ measures how quickly the matter is settled.
Highly connected networks with good mixing properties have a large **spectral gap** $1-|\lambda_2|$, and so rapid convergence, as we saw with stochastic matrices in Section 9.4.

**Example 9.26 (Robotic Flocking).** A swarm of robots aligns its velocities by local averaging, each robot pulled toward whoever is within communication range at time $t$:

$$
\mathbf{v}(t+1) = (I-\epsilon L(t))\mathbf{v}(t)
$$

The Laplacian is now time-varying, and its spectrum at each instant sets both stability and rate.
The tools built for static networks survive a moving topology.

The Laplacian is symmetric, so Section 9.5 applies: real spectrum, orthogonal eigenvectors.
There is more in the Laplacian than symmetry.
Orient the edges of the graph arbitrarily and recall the boundary operator $\partial:C_1(G)\to C_0(G)$ from the discussion of graph topology closing Chapter 3; a direct computation shows that $L=\partial\partial^T$, the choice of orientations cancelling in the product.

This factorization pays immediately: since $\mathbf{x}^TL\mathbf{x}=\|\partial^T\mathbf{x}\|^2$, a vector lies in $\operatorname{ker} L$ precisely when its values agree across every edge — when it is constant on each connected component.
The kernel of the Laplacian is thus the space of **locally constant** vectors, of dimension $\beta_0$, the number of components.
That number was computed in Chapter 3 through the cokernel of $\partial$ and is recomputed here as a kernel, the two answers reconciled by the geometric form of the Fundamental Theorem (Theorem 6.9): $\operatorname{coker}\partial\cong\operatorname{ker}\partial^T$.
The averaging dynamics of Theorem 9.25 converge onto exactly this kernel.
*Agreement is a fundamental subspace.*

**Example 9.27 (Supply Chain Networks).** Returning to the input-output model from Section 9.1, form the weighted graph on the sectors whose edge $\{i,j\}$ carries the symmetrized flow $\tfrac12(a_{ij}+a_{ji})$ — the input-output matrix itself is not symmetric, and Definition 9.23 has nothing to say about it until it is made so.
Discard the diagonal, set $(D_w)_{ii}=\sum_{j\neq i}w_{ij}$, and the **weighted Laplacian** $L=D_w-W$ has the same kernel argument as Definition 9.23.
The eigenvector of its smallest nonzero eigenvalue, the **Fiedler vector**, splits the sectors into two groups.
Industries on opposite sides tend to separate first under stress, identifying natural fault lines; the magnitude of the eigenvalue quantifies how hard the network resists the split.

—

## Spectral Graph Theory & Vibrations

The mathematics of musical instruments emerges through the vibrations of strings and membranes.
A plucked string settles into standing waves whose frequencies fix its pitch; a drum head vibrates in patterns that give it timbre.
Both find their essence in the eigenvalues of the graph Laplacian of Definition 9.23.

Consider a string fixed at its endpoints, discretized into $n$ interior points joined by identical springs.
The displacement $x_i$ of point $i$ feels restoring forces from its neighbors, proportional to the differences:

$$
m\frac{d^2x_i}{dt^2} = \kappa(x_{i+1} - x_i) - \kappa(x_i - x_{i-1}),
$$

or, in matrix form, $m\ddot{\mathbf{x}} = -\kappa L\mathbf{x}$, where $L$ is the **Dirichlet Laplacian** of the path — the Laplacian of Definition 9.23 stiffened at the two fixed ends, so that the first and last displacements each feel a wall as well as a neighbor:

$$
L = \begin{bmatrix}
2 & -1 & 0 & \cdots & 0 \\
-1 & 2 & -1 & \cdots & 0 \\
0 & -1 & 2 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & 2
\end{bmatrix}
$$

> *Note:* Fixing both ends makes this matrix positive *definite* — unlike the free graph Laplacian, it has no zero eigenvalue, so the string cannot drift as a rigid whole.

The eigenvectors of $L$ are the standing-wave modes; the eigenvalues set their frequencies through $\omega_i = \sqrt{\kappa\lambda_i/m}$.
As $n$ grows, these discrete modes converge to the familiar continuum,

$$
v_k(x) = \sin\!\left(\frac{k\pi x}{\ell}\right), \qquad \omega_k = \frac{k\pi}{\ell}\sqrt{\frac{T}{\rho}},
$$

with $\ell$ the string length, $T$ the tension, and $\rho$ the linear density — the exact sine modes of the fixed string, recovered as the continuum limit of the eigenvectors of the tridiagonal $L$.

> *Example:* A circular drum head's modes are the **Bessel functions**, emerging as limits of mesh eigenvectors.

The construction lifts to two dimensions unchanged: for a drum head meshed into triangles, the Laplacian on the mesh vertices again delivers frequencies as eigenvalues and mode shapes as eigenvectors.

The free Laplacian met earlier in this chapter carries a kernel — one locally constant vector for each connected piece.
The fixed ends of the string empty that kernel: with nowhere to drift as a whole, every mode must genuinely vibrate.
The boundary conditions of a physical problem are, in the end, a statement about a subspace.

—

## PageRank: The Flow of Web Authority

The World Wide Web presents perhaps the largest human-constructed network in history — billions of pages connected through hyperlinks that channel attention and information across the digital sphere.
Like the discrete-time systems studied in Section 9.1, this vast network exhibits intrinsic patterns of information flow that can be understood through careful mathematical analysis.
The challenge of organizing this space was met with stochastic matrices and iterative convergence, in the algorithm that became Google's PageRank.

Consider a web surfer following links from page to page, modeling their behavior as the type of Markov chain developed in Section 9.4.
At each step, they either follow a randomly chosen outgoing link (with probability $\alpha$) or jump to a random page anywhere on the web (with probability $1-\alpha$).
This process generates a transition matrix $P = [p_{ij}]$:

$$
p_{ij} = \alpha\frac{a_{ij}}{d_j} + \frac{1-\alpha}{n}
$$

where $a_{ij}=1$ if page $j$ links to page $i$ (and 0 otherwise), $d_j$ is the number of outgoing links from page $j$ (if $d_j=0$, this term is often handled by assuming jumps to all pages equally), and $n$ is the total number of pages.
The term $(1-\alpha)/n$ represents the random teleportation probability.

This construction makes $P$ column-stochastic, and since $0<\alpha<1$, every entry is strictly positive.
Teleportation (typically $\alpha\approx 0.85$) is not a modelling flourish; it is the hypothesis of the theorem, purchased.
It makes $P$ primitive in the sense of Section 9.3 at the very first power, hence ergodic, and Theorem 9.16 then supplies a unique stationary $\mathbf{\pi}=P\mathbf{\pi}$, approached from any start.
This **PageRank vector** measures each page's importance through its long-term visit probability.
Equivalently $\mathbf{\pi}\in\operatorname{ker}(P-I)$: the ranking is the one distribution the Web's own flow leaves unchanged — every eigenspace, once more, a kernel.

**Example 9.28 (Simple Web).** Consider a tiny web of four pages with link structure given by adjacency matrix

$$
A = \begin{bmatrix}
0 & 1 & 0 & 0 \\
1 & 0 & 1 & 0 \\
0 & 1 & 0 & 1 \\
0 & 0 & 1 & 0
\end{bmatrix}
$$

— a chain of pages, each linking to its neighbors.
With damping factor $\alpha = 0.85$, the iteration converges to:

$$
\mathbf{\pi} \approx \begin{pmatrix}
0.18 \\ 0.32 \\ 0.32 \\ 0.18
\end{pmatrix}
$$

This distribution reflects both local link structure and global network position.
Like the network centrality measures from Section 9.6, pages with more incoming paths tend to receive higher scores; the symmetry of the chain reappears, as it must, in the symmetry of $\mathbf{\pi}$.

The rate of convergence, as with all ergodic Markov chains, is determined by the magnitude of the second-largest eigenvalue of $P$, denoted $|\lambda_2(P)|$.
Write $M$ for the pure link-following matrix, with entries $a_{ij}/d_j$, so that $P = \alpha M + \frac{1-\alpha}{n}\mathbf{1}\mathbf{1}^T$.
Since $M$ is column-stochastic, every eigenvector of $M$ for an eigenvalue other than $1$ has entries summing to zero, and the teleportation term annihilates it: $\lambda_1(P)=1$, while $\lambda_k(P) = \alpha\,\lambda_k(M)$ for $k \geq 2$.
Thus $|\lambda_2(P)| = \alpha\,|\lambda_2(M)| \leq \alpha$: teleportation caps the convergence factor at $\alpha$, whatever the graph.

**Example 9.29 (Convergence Behavior).** For our four-page example, tracking successive iterates reveals geometric convergence:

$$
\|\mathbf{x}_k - \mathbf{\pi}\| \approx |\lambda_2(P)|^k\|\mathbf{x}_0 - \mathbf{\pi}\|
$$

where $|\lambda_2(P)| < 1$.
For the four-page chain, $|\lambda_2(M)| = 1$ (the chain, being bipartite, gives $M$ an eigenvalue $-1$), so $|\lambda_2(P)| = \alpha = 0.85$ exactly — the cap is attained.
Start the iteration from the uniform distribution, though, and one observes $0.425$ rather than $0.85$: the eigenvector for $-0.85$ is antisymmetric under the flip $1\leftrightarrow4$, $2\leftrightarrow3$, while the uniform vector and $\mathbf{\pi}$ are both symmetric, so that mode is absent from the error and the next one governs.
The rate $|\lambda_2|$ is worst-case over starting vectors, not a promise about any particular one.

The same construction ranks any network in which importance flows along the edges — citations, social influence, systemic risk — provided teleportation, or some analogue of it, makes the transition matrix ergodic.
The ranking is the stationary voice of the flow.

—

## Opinion Dynamics & The Paradox of Connection

Section 9.6 left a promise: on a connected network, repeated averaging drives every opinion to the same number, and thickening the wiring only hastens the arrival.
This is the model of collective belief proposed by the social psychologist John French in the 1950s and sharpened by the statistician Morris DeGroot two decades later, and it is Theorem 9.25 with $W=I-\epsilon L$: each step descends the gradient of the disagreement $\mathbf{x}^TL\mathbf{x}$, and $\operatorname{ker} L$ is where it lands.
Connect the world, the theorem says, and wait.

The world is now connected as never before, and it has not obliged.
The fault lies with the cast of characters, for every agent in the DeGroot model listens.
The decisive actors of real discourse are those who do not: the propagandist, the provocateur, the sincerely immovable.
Call such an agent a **zealot** — a vertex whose opinion is a datum, not a variable.
Six years before DeGroot, the mathematical psychologist Michael Taylor had already written down the agents who do not listen — a model rediscovered by Friedkin and Johnsen in 1990, and the one these pages are about.

Taylor's move is to enter the zealots as a constant: let the fixed sources push on the network through a vector $\mathbf{b}$, so that $\mathbf{x}(t+1)=W\mathbf{x}(t)+\mathbf{b}$, with equilibrium $\mathbf{x}^*=(I-W)^{-1}\mathbf{b}$.
The move is right; the matrix is wrong.
Here $I-W=\epsilon L$, and $L$ is singular: its kernel, the constant vectors, is precisely the agreement subspace that made consensus inevitable two paragraphs ago.
The geometric form of the Fundamental Theorem (Theorem 6.9) tells exactly what survives: $\epsilon L\mathbf{x}=\mathbf{b}$ is solvable only when $\mathbf{b}\in\operatorname{im} L=(\operatorname{ker} L)^\perp$, that is, when the forcing sums to zero.
A source pumping net opinion into a connected network admits no equilibrium at all — since $\mathbf{1}^TW=\mathbf{1}^T$, the average opinion climbs by $\mathbf{1}^T\mathbf{b}/n$ at every step, forever.
Even mean-zero forcing leaves an entire line of equilibria, $\mathbf{x}_0+\operatorname{ker} L$, among which the initial average — conserved by the dynamics — selects.
One cannot push a system along its own kernel and expect it to stand still.

The remedy is not to abandon the forcing but to repair the matrix.
A zealot is not a force on a network; it is a vertex that does not update.
Partition the vertices into a flexible set $F$ and a stubborn set $S$, ordering the flexible first, so that the Laplacian splits into blocks

$$
L = \begin{bmatrix} L_{FF} & L_{FS} \\ L_{SF} & L_{SS} \end{bmatrix} ,
$$

and let only the flexible average:

$$
\mathbf{x}_F(t+1) \;=\; \mathbf{x}_F(t) - \epsilon\left(L_{FF}\,\mathbf{x}_F(t) + L_{FS}\,\mathbf{x}_S\right),
$$

with $\mathbf{x}_S$ held fixed.
The matrix $L_{FF}$ — the Laplacian with the stubborn rows and columns deleted — is the **grounded Laplacian**, and grounding changes everything: so long as every connected component of the network contains at least one zealot, $L_{FF}$ is positive definite.

> *Terminology:* The term is from circuit theory, where to ground a node is to wire it to the earth, whose potential does not negotiate.
> The zealot is the earth of this network.

> *Fact:* $L_{FF}$ is positive definite as soon as every component holds a zealot.
> The exercises supply the reason, and it is the disagreement energy again.

The kernel that first guaranteed consensus and then blocked the inversion has been emptied — the same stiffening that turned the free Laplacian of Definition 9.23 into the Dirichlet matrix that tuned the fixed string, earlier among these closing pages.
There, walls pinned the endpoints of a string at zero; here, zealots pin their opinions wherever they please.
The iteration now converges (extension by zero, as Exercise 22 runs it, turns $\mathbf{x}_F$ into a vector $\mathbf{x}$ with $\|\mathbf{x}\|=\|\mathbf{x}_F\|$ and $\mathbf{x}^TL\mathbf{x}=\mathbf{x}_F^TL_{FF}\mathbf{x}_F$, so every Rayleigh quotient of $L_{FF}$ is one of $L$, and Lemma 9.22 confines the grounded spectrum to the range of the free one, where the same $\epsilon$ serves) to a unique equilibrium:

$$
\mathbf{x}_F^* \;=\; -L_{FF}^{-1}L_{FS}\,\mathbf{x}_S .
$$

Written as $\mathbf{x}_F(t+1)=W_{FF}\mathbf{x}_F(t)+\mathbf{b}$ with $W_{FF}=I-\epsilon L_{FF}$ and $\mathbf{b}=-\epsilon L_{FS}\mathbf{x}_S$, this has $\rho_{W_{FF}}<1$, and Lemma 9.19 writes the powers of the symmetric $W_{FF}$ as $Q\Lambda^kQ^T$, so $W_{FF}^k\to 0$.
That is the hypothesis of Lemma 1.8: $I-W_{FF}$ is invertible, with the geometric series $I+W_{FF}+W_{FF}^2+\cdots$ for its inverse.
Exercise 18 reaches the same invertibility for an input-output matrix with no series at all, trapping the spectral radius below one by the inequality of Section 9.3 so that $1$ is not an eigenvalue.
Each term of the series counts the walks of one more step (Exercise 6), so an agent's settled opinion is the sum over every path by which a zealot can reach it.

This equilibrium has a shape.
Read row by row, the equation $L_{FF}\mathbf{x}_F^*=-L_{FS}\mathbf{x}_S$ says that every flexible opinion equals the average of its neighbors' opinions: the equilibrium is a discrete harmonic function, with the stubborn set as its boundary.
Averages cannot exceed what they average, so every opinion at equilibrium is trapped between the most extreme positions the zealots stake out — no moderation beyond their compromise, no radicalization past their poles.

> *FIGURE:* [five vertices in a row; filled endpoints labeled $-1$ and $+1$; the equilibrium profile rising in a straight line above them, drawn as a taut string.]

Five groups in a line, with zealots at the two ends holding $-1$ and $+1$, settle at

$$
\mathbf{x}^* = \left(-1, -\tfrac{1}{2},\, 0,\, \tfrac{1}{2},\, 1\right)^T,
$$

the interior solved by the same $3\times 3$ tridiagonal matrix that tuned the string: a linear gradient of conviction, the profile of a taut string pinned at unequal heights.
Consensus returns only if the zealots happen to agree, in which case their common value is the unique harmonic extension.
Otherwise the network does not converge to agreement; it converges to an interpolation of the intransigent.

Where, exactly, does consensus die?
The equilibrium depends linearly on the boundary, and constants pass straight through: shift every stubborn opinion by a common amount and the whole network shifts with it, obstructing nothing.
Only the differences among zealots obstruct, and the obstruction has a formula.
Among all opinion patterns honoring the zealots, the equilibrium attains the least disagreement $\mathbf{x}^TL\mathbf{x}$ the boundary permits, and that minimum is

$$
\mathbf{x}_S^T\,\widehat{L}\,\mathbf{x}_S,
\qquad
\widehat{L} \;=\; L_{SS}-L_{SF}\,L_{FF}^{-1}L_{FS},
$$

a quadratic form in the stubborn opinions alone.

> *Example:* for the five groups in a line, the effective network is a single edge of weight $\tfrac{1}{4}$ joining the two zealots: four unit edges in series conduct one quarter as well as one.
> Electrical engineers know these weights as effective conductances; the flexible interior is, to the boundary, a resistor.

The matrix $\widehat{L}$ is itself a graph Laplacian — of an **effective network** on the zealots alone, its edge weights recording how well the flexible crowd conducts influence between each stubborn pair.
The flexible majority, for all its faithful averaging, is a medium.

Here is the paradox of connection.
Adding edges to this network can never lower the smallest eigenvalue of $L_{FF}$, so with $\epsilon$ retuned it can never slow the last mode to settle — which settles toward the blend the boundary dictates.
No density of wiring restores the emptied kernel while a single zealot remains: the connectivity that promised consensus delivers each zealot's influence, ever more efficiently, to every door.

Two doors lead out of the linear theory, and honesty requires pointing at both.
Antagonistic ties enter the model as negative weights, and with them $L$ forfeits positive semidefiniteness: eigenvalues of the iteration can escape the unit disk, and opinions oscillate or diverge rather than settle.
Bounded confidence lets an agent discount any opinion too distant from its own; the coupling becomes nonlinear, and stably polarized states appear with no zealot anywhere in the graph.

> *BONUS!* In a further refinement, opinions live not at the vertices but over the edges, so that an agent may hold one view and express several, one per audience.
> Lying, in such models, is a change of coefficients.
> The author confesses a professional interest.

The linear theory does not contain these phenomena, and does something more useful instead: it marks the exact assumption each one breaks, so that when averaging fails, the failure has a name.

Agreement remains what this chapter found it to be — a fundamental subspace, the kernel of the Laplacian, one dimension per connected piece — and averaging still descends toward it.
Whether a society arrives is decided not by the density of its wiring, which sets only the speed, but by who refuses to move.
*A zealot is a boundary condition.*

—

## Exercises: Chapter 9

1. Let $G$ have vertices $\{1,2,3,4\}$ and edges $\{(1,2),(2,3),(3,4),(4,1),(2,4)\}$.
Write down its adjacency and degree matrices and compute the Laplacian $L$ of Definition 9.23.
Find its spectrum without a determinant: $L\mathbf{1}=\mathbf{0}$ gives one eigenvalue, the symmetry exchanging vertices $1$ and $3$ gives a second, and $\operatorname{tr} L$ together with $\operatorname{tr} L^2$ pins the remaining pair.
Read the number of components off the multiplicity of $0$, and say which two vertices the eigenvector for the smallest nonzero eigenvalue separates, and what is special about that pair.

2. For $P = \begin{bmatrix}0.5 & 0.3 & 0.2\\0.4 & 0.4 & 0.3\\0.1 & 0.3 & 0.5\end{bmatrix}$ compute $P^2$ and $P^3$ and watch the columns approach one another.
Identify the vector they are approaching and explain, using Theorem 9.16, why column agreement is exactly the statement that the chain forgets where it started.
Compute the second eigenvalue exactly and check that it predicts the rate you observe.

3. Compute the first five powers of $A = \begin{bmatrix}0 & 1 & 0\\1 & 0 & 1\\0 & 1 & 0\end{bmatrix}$ and find the relation among them.
The zero entries fall in a checkerboard pattern at every step; say which pattern, and why the graph's structure forces it.
Now normalize $A$ to the column-stochastic walk matrix $P=AD^{-1}$ of Section 9.4 — the transpose of the averaging matrix of Section 9.6 — and compute its powers.
Does $P^n\mathbf{x}(0)$ converge, and which hypothesis of Theorem 9.16 decides the matter?

4. Run the power method on $A = \begin{bmatrix}4 & 1 & 1\\1 & 4 & 1\\1 & 1 & 4\end{bmatrix}$ from $\mathbf{x}_0=(1,0,0)^T$, clearing common factors at each step and recording the Rayleigh quotient $\mathbf{x}^TA\mathbf{x}/\mathbf{x}^T\mathbf{x}$.
Five steps suffice to see the answer.
The dominant eigenvalue is $6$ and the other is $3$, so Lemma 9.3 predicts the direction's error falls by a factor of $2$ each step; verify that it does once each iterate is normalized to unit sum, and observe that the error in the Rayleigh quotient falls by a factor approaching $4$ instead.

5. Label the cube's eight vertices so that a top square and a bottom square are joined rung by rung, and check that its adjacency matrix is $\begin{bmatrix}B & I\\I & B\end{bmatrix}$ with $B$ the adjacency matrix of the $4$-cycle.
Show that $B\mathbf{u}=\mu\mathbf{u}$ makes $(\mathbf{u},\mathbf{u})^T$ and $(\mathbf{u},-\mathbf{u})^T$ eigenvectors of the cube with eigenvalues $\mu\pm1$, and deduce the whole spectrum from the $4$-cycle's own spectrum $\{2,0,0,-2\}$.
The random walk on the cube has matrix $W=A/3$: is its chain ergodic, and does $W^n\mathbf{x}(0)$ converge?

6. A **walk** of length $k$ from vertex $i$ to vertex $j$ is a list $i=v_0,v_1,\ldots,v_k=j$ with consecutive entries adjacent; vertices and edges may repeat.
Prove by induction that $(A^k)_{ij}$ counts the walks of length $k$ from $j$ to $i$, and say which step of the induction is precisely the definition of matrix multiplication.

7. Prove the first two clauses of Lemma 9.19 without leaving $\mathbb{R}$.
For the first, suppose $A$ is symmetric with a complex eigenvalue $\alpha\pm i\beta$ and split the eigenvector equation into real and imaginary parts as in the proof of Lemma 8.2, giving $A\mathbf{u}=\alpha\mathbf{u}-\beta\mathbf{w}$ and $A\mathbf{w}=\beta\mathbf{u}+\alpha\mathbf{w}$; compare $\mathbf{w}^TA\mathbf{u}$ with $\mathbf{u}^TA\mathbf{w}$ and conclude $\beta=0$.
For the second, compute $\mathbf{v}_1^TA\mathbf{v}_2$ two ways.

8. Let $A$ be symmetric with orthonormal eigenvectors $\mathbf{q}_1,\ldots,\mathbf{q}_n$ and eigenvalues $\lambda_1\geq\cdots\geq\lambda_n$.
Expanding a unit vector in that basis, prove Lemma 9.22: the quadratic form $q(\mathbf{x})=\mathbf{x}^TA\mathbf{x}$ has maximum $\lambda_1$ and minimum $\lambda_n$ on the unit sphere, attained at the corresponding eigenvectors, and takes every value in between.

9. A matrix is doubly stochastic when its rows as well as its columns sum to one.
Prove that the uniform distribution $\tfrac{1}{n}\mathbf{1}$ is then stationary, and identify which of the two sum conditions the proof consumes.
Is it the only stationary distribution?
Give a doubly stochastic matrix with a non-uniform stationary distribution, and state the hypothesis that restores uniqueness.

10. Let $P$ be irreducible with stationary distribution $\mathbf{\pi}$, positive by Theorem 9.9, and let $\tilde{P}$ have entries $\tilde{p}_{ij}=(\pi_i/\pi_j)p_{ji}$.
Prove that $\tilde P$ is stochastic with the same stationary distribution, and that $\tilde{P}=D P^TD^{-1}$ for $D=\operatorname{diag}(\pi_1,\ldots,\pi_n)$, so that $P$ and $\tilde P$ share a spectrum.
Then recognize what you have computed: weight $\mathbb{R}^n$ by $\langle\mathbf{x},\mathbf{y}\rangle_{\mathbf{\pi}}=\sum_i x_iy_i/\pi_i$, which is an inner product because $\mathbf{\pi}$ is positive, and verify $\langle P\mathbf{x},\mathbf{y}\rangle_{\mathbf{\pi}}=\langle\mathbf{x},\tilde P\mathbf{y}\rangle_{\mathbf{\pi}}$, so that the time-reversed chain is the adjoint of $P$ in the sense of Definition 5.10, as in Example 5.15: an adjoint that is not a transpose.
Call the chain **reversible** when $\tilde P=P$; show this says exactly $\pi_jp_{ij}=\pi_ip_{ji}$, and check it for the random walk on a graph of Section 9.4.

11. Let $P$ be doubly stochastic.
Prove that $\|P\mathbf{x}\|\leq\|\mathbf{x}\|$ for every $\mathbf{x}$, using Lemma 5.5 on each coordinate of $P\mathbf{x}$, and deduce the same bound for every power of $P$.
Then show the hypothesis cannot be weakened to column-stochastic: for $P=\tfrac{1}{30}\begin{bmatrix}28&28&1\\1&1&28\\1&1&1\end{bmatrix}$ and $\mathbf{x}=(1,1,-2)^T$, which is orthogonal to $\mathbf{1}$, the norm grows.
Say which step of your proof fails.

12. For a Markov chain, write $m_{ij}$ for the expected number of steps to first reach state $j$ starting from state $i$.
Conditioning on the first step gives $m_{ij}=1+\sum_{k\neq j}p_{ki}m_{kj}$; grant this and do the linear algebra.
Deleting row and column $j$ from $P$ to leave $Q$, show the relation becomes $\mathbf{m}=\mathbf{1}+Q^T\mathbf{m}$ and explain why $I-Q^T$ is invertible.
Solve for all six passage times of the weather matrix of Section 9.4, and for the mean return times $1+\sum_{k\neq j}p_{kj}m_{kj}$; compare the latter with $1/\pi_j$.

13. Show that a dominant eigenvalue of a real matrix, in the sense of Definition 9.2, is necessarily real — so that $\lambda_*^n$ in Lemma 9.3 never leaves the field this book works over.
Then show that $A=\begin{bmatrix}1 & -1\\1 & 1\end{bmatrix}$ has none, and that the power method applied to it produces iterates whose length grows at exactly the rate $\rho_A$ predicts while their direction returns to where it began every eight steps.

14. The matrix $A=\begin{bmatrix}-11 & 9\\9 & -11\end{bmatrix}$ has eigenvalues $-2$ and $-20$, so every solution of $\mathbf{x}'=A\mathbf{x}$ decays.
Show that the Euler step $\mathbf{x}_{k+1}=(I+hA)\mathbf{x}_k$ has spectral radius $\max(|1-2h|,|1-20h|)$ and find the range of $h$ for which it decays, while the exact step $\mathbf{x}_{k+1}=e^{hA}\mathbf{x}_k$ decays for every $h>0$.
Which eigenvalue destroys the Euler scheme, and is it the one that governs the flow?

    > *Nota bene:* continuous time is ruled by $\mathrm{Re}\,\lambda$ and discrete time by $|\lambda|$, and the exponential is what carries one to the other.
    > A discretization is a wager that the two agree.

15. Every power of the cyclic permutation matrix on $n$ states is again a permutation matrix, so it is irreducible and no power of it is strictly positive.
Deduce that all $n$ of its eigenvalues have magnitude $\rho$, so that it has no dominant eigenvalue: Theorem 9.9 cannot be strengthened to Theorem 9.6 by irreducibility alone.
Now let $P$ be stochastic with $P^m$ strictly positive, and let $|\lambda|=1$; show $P^m\mathbf{v}=\lambda^m\mathbf{v}$ directly from $P\mathbf{v}=\lambda\mathbf{v}$, and conclude $\lambda^m=1$.
Show $P^{m+1}$ is strictly positive as well, and divide.

16. Four agents sit at the corners of a square, each replacing its opinion by the average of its two neighbours.
Write down the update matrix, compute its spectrum, and show that the opinions oscillate forever; identify the failed hypothesis of Theorem 9.25.
Show the failure cannot be reweighted away: conjugating any averaging matrix supported on the square's edges by $\operatorname{diag}(1,-1,1,-1)$ negates it, so its spectrum is symmetric about the origin and $-1$ joins the $1$ that every averaging matrix carries.
Now let each agent keep some of its own opinion, $W=I-\epsilon L$, and find the $\epsilon$ that converges fastest.

17. A gambler holding \$2 wins \$1 with probability $1/3$ and loses \$1 otherwise, stopping at \$0 or at \$3.
Write the column-stochastic transition matrix on the states $\{0,1,2,3\}$.
Letting $h_i$ be the probability of reaching \$3 from \$$i$, condition on the first bet to get a linear system for $h_1$ and $h_2$, and solve it.
This chain has two absorbing states: say why Theorem 9.16 does not apply to it.

18. An economy has input-output matrix $A = \begin{bmatrix}0.3 & 0.2 & 0.1\\0.2 & 0.4 & 0.3\\0.1 & 0.2 & 0.4\end{bmatrix}$ and must meet final demand $\mathbf{d}=(20,70,10)^T$, so that total output satisfies $\mathbf{x}=A\mathbf{x}+\mathbf{d}$.
Bound $\rho_A$ without computing a single eigenvalue by putting $\mathbf{y}=\mathbf{1}$ into the trapping inequality of Section 9.3, and conclude that $I-A$ is invertible.
Then find $\mathbf{x}$.
Contrast with Example 9.1, where the same construction has $\rho_A>1$.

19. A toy lights one of three buttons — red, blue, green, in that order — at each press, with transition matrix

$$
P = \begin{bmatrix}
    0.2 & 0.4 & 0.2 \\
    0.5 & 0.3 & 0.1 \\
    0.3 & 0.3 & 0.7
    \end{bmatrix}
$$

Starting from red, find the probability that green is lit after exactly three presses, and the fraction of presses each button is lit over a long session.
The two answers differ; say what would have to be true of $P$ for them to coincide already at the third press.

20. The **eigenvector centrality** of a network is the dominant eigenvector of its adjacency matrix, and Theorem 9.9 is what makes it a ranking rather than a sign-indefinite mess.
Compute it by power iteration for the graph on five vertices with edges $\{1,2\},\{1,3\},\{1,4\},\{2,3\},\{2,5\},\{3,4\}$, normalizing at each step.
Vertices $1$, $2$ and $3$ all have degree $3$ and do not all score alike: explain which of them the ranking demotes, and why counting a vertex's neighbours is not the same as weighting them.

21. (Challenge.) Prove Theorem 9.16 from the two results before it.
Ergodicity makes $P$ primitive, so Exercise 15 and Theorem 9.6 give $\lambda_*=1$ dominant with a positive eigenvector; normalize it to $\mathbf{\pi}$ and apply Lemma 9.3 to each standard basis vector in turn, or the Jordan estimate of Section 9.2 if $P$ is not diagonalizable.
Conclude that $P^k\to\mathbf{\pi}\mathbf{1}^T$, which is the second clause, and that the first follows from simplicity of $\lambda_*=1$.

22. (Challenge.) Partition a connected graph's vertices into a flexible set $F$ and a nonempty stubborn set $S$, and let $L_{FF}$ be the Laplacian with the stubborn rows and columns struck out.
Using the identity $\mathbf{x}^TL\mathbf{x}=\sum_{\{i,j\}\in E}(x_i-x_j)^2$, show that $\mathbf{x}_F^TL_{FF}\mathbf{x}_F$ is the disagreement of the pattern that extends $\mathbf{x}_F$ by zero, and that it vanishes only at $\mathbf{x}_F=\mathbf{0}$.
Conclude that $L_{FF}$ is invertible, so that the equilibrium $\mathbf{x}_F^*=-L_{FF}^{-1}L_{FS}\mathbf{x}_S$ of the closing discussion exists and is unique — the kernel that guaranteed consensus is exactly what grounding removes.

---


---

> **Part marker.** URTHONA — imagination (cokernel)


# Chapter 10. Singular Value Decomposition

*"build we the mundane shell around the rock of albion"*

**Every transformation harbors** hidden regularities beneath its surface complexity.
Like crystal structures buried in seemingly formless rock, these patterns reveal themselves only through careful excavation.
The eigendecomposition developed in previous chapters illuminates the structure of square matrices through their action under iteration.
Yet this tool reaches only part way to the deepest patterns underlying linear transformations.

The limitation of eigentheory to square matrices is no accident — eigenvalues and eigenvectors emerge from iteration, which requires a transformation to map a space to itself.
Yet the geometric essence of a linear transformation — how it stretches and rotates space — extends beyond such endomorphisms.
Every linear transformation, whether square or rectangular, admits a canonical decomposition that reveals its intrinsic geometric character.
This decomposition exposes not just preferred directions, but fundamental relationships between input and output spaces that remain invisible to eigentheory alone.

Our task is to dig beneath the surface structure of linear transformations to discover these deeper patterns.
We begin with the Spectral Theorem: met in shadow in Chapter 9, it here receives its full statement, its proof, and its geometry.
With that instrument in hand we excavate: matrices transform spheres into ellipsoids, revealing natural input and output directions, and from these foundations emerges the singular value decomposition — theoretical insight and practical tool for understanding linear transformations in their full generality.

## 10.1 The Spectral Theorem

Chapter 9 ran on a claim that did heavy work without proof: symmetric matrices diagonalize orthogonally (Lemma 9.19), a fact pressed into service for principal axes, correlation structure, and graph spectra alike.
That claim can stand unproved no longer, for everything this chapter builds rests upon it.

**Theorem 10.1 (Spectral Theorem).** Let $A$ be a real symmetric matrix. Then:

1. All eigenvalues of $A$ are real

2. Eigenvectors corresponding to distinct eigenvalues are orthogonal

3. $A$ has an orthonormal basis of eigenvectors

Thus $A$ can be orthogonally diagonalized: $A=Q\Lambda Q^T$ where $Q$ is orthogonal and $\Lambda$ is diagonal with real entries.

> *Think:* The proof leans three times on the adjoint identity $\langle A\mathbf{x},\mathbf{y}\rangle = \langle\mathbf{x},A^T\mathbf{y}\rangle$ of Chapter 5 — once for orthogonality, once for the invariance of the complement, once for the self-adjointness of the restriction.
> Symmetry means self-adjointness; that is the working hypothesis.

*Proof.* For (1), begin where Definition 7.2 begins: an eigenvalue is a root of the characteristic polynomial.
Lemma 7.4 guarantees, by the Fundamental Theorem of Algebra, that $p_A$ has $n$ roots in $\mathbb{C}$; let $\lambda$ be one of them.
Then $\det(A-\lambda I)=0$, so $A-\lambda I$ is singular as a matrix over $\mathbb{C}$, and there is a nonzero $\mathbf{v}\in\mathbb{C}^n$ with $A\mathbf{v}=\lambda\mathbf{v}$.
Write $\overline{\mathbf{v}}$ for the entrywise complex conjugate of $\mathbf{v}$, the operation met in Chapter 8, and call $\overline{\mathbf{v}}^T$ the **conjugate transpose** of $\mathbf{v}$: transpose, then conjugate every entry.
Consider the scalar $s = \overline{\mathbf{v}}^TA\mathbf{v}$.
Taking the conjugate transpose of this $1\times1$ matrix returns $\bar{s}$ and reverses the product:

$$
\begin{aligned}
\bar{s} &= \overline{\mathbf{v}}^T\overline{A}^{T}\mathbf{v}
      && (\text{$s$ is $1\times1$, so $\bar{s}=\bar{s}^{T}$}) \\
    &= \overline{\mathbf{v}}^TA^{T}\mathbf{v}
      && (\text{$A$ is real: $\overline{A}=A$}) \\
    &= \overline{\mathbf{v}}^TA\mathbf{v}
      && (\text{$A$ is symmetric: $A^{T}=A$}) \\
    &= s ,
\end{aligned}
$$

so $s$ is real.
On the other hand $s = \overline{\mathbf{v}}^T(\lambda\mathbf{v}) = \lambda\,\overline{\mathbf{v}}^T\mathbf{v}$, and

$$
\overline{\mathbf{v}}^T\mathbf{v} = \sum_{k=1}^n \overline{v_k}\,v_k = \sum_{k=1}^n |v_k|^2 > 0
$$

because $\mathbf{v}\neq\mathbf{0}$.
A real number divided by a positive real number is real, so $\lambda = s/(\overline{\mathbf{v}}^T\mathbf{v})$ is real.

For (2), suppose $A\mathbf{u}=\lambda\mathbf{u}$ and $A\mathbf{v}=\mu\mathbf{v}$ with $\lambda\neq\mu$.
Then

$$
\lambda\langle\mathbf{u},\mathbf{v}\rangle
    = \langle A\mathbf{u},\mathbf{v}\rangle
    = \langle\mathbf{u},A\mathbf{v}\rangle
    = \mu\langle\mathbf{u},\mathbf{v}\rangle
$$

the middle equality being symmetry in adjoint form.
Since $\lambda\neq\mu$, the inner product must vanish.

For (3), induct on the size $n$, the case $n=1$ being trivial.
The characteristic polynomial of $A$ has a root, which by (1) is real: an eigenvalue $\lambda_1$, with $(A-\lambda_1I)$ singular over $\mathbb{R}$, so a real unit eigenvector $\mathbf{q}_1$ exists.
Let $W=\mathbf{q}_1^\perp$, which has $\dim W = n-1$ by Lemma 6.2(2).
The adjoint identity of Chapter 5, which for symmetric $A$ reads $\langle A\mathbf{x},\mathbf{y}\rangle=\langle\mathbf{x},A\mathbf{y}\rangle$ for all $\mathbf{x},\mathbf{y}$, does two jobs at once.
Taking $\mathbf{y}=\mathbf{q}_1$ and $\mathbf{x}\in W$ gives

$$
\langle A\mathbf{x},\mathbf{q}_1\rangle = \langle\mathbf{x},A\mathbf{q}_1\rangle = \lambda_1\langle\mathbf{x},\mathbf{q}_1\rangle = 0 ,
$$

so $A\mathbf{x}\in W$: the subspace is invariant and the restriction $A|_W:W\rightarrow W$ is a well-defined linear operator.
Taking instead *both* $\mathbf{x},\mathbf{y}\in W$ gives $\langle A|_W\mathbf{x},\mathbf{y}\rangle=\langle\mathbf{x},A|_W\mathbf{y}\rangle$, so $A|_W$ is self-adjoint on the inner product space $W$.
That is an operator, not yet a matrix, and the induction is on matrix size; the conversion is the fact recorded in Chapter 5, that in an orthonormal basis the matrix of the adjoint is the transpose of the matrix.
Choose an orthonormal basis of $W$  — Gram-Schmidt supplies one — and let $B$ be the matrix of $A|_W$ in it; self-adjointness makes $B$ a real symmetric matrix of size $(n-1)\times(n-1)$.
*This* is what the inductive hypothesis applies to, and it returns an orthonormal basis of $\mathbb{R}^{n-1}$ of eigenvectors of $B$.
Reading those coordinate vectors back through the chosen orthonormal basis — an isometry, so orthonormality survives — yields an orthonormal basis of $W$ made of eigenvectors of $A$.
Adjoining $\mathbf{q}_1$, which is orthogonal to all of them, completes an orthonormal eigenbasis of $\mathbb{R}^n$.
Assembling the basis into $Q=[\mathbf{q}_1\cdots\mathbf{q}_n]$ gives $AQ=Q\Lambda$, whence $A=Q\Lambda Q^T$. ∎

> *Nota bene:* Clauses 1 and 2 can be had without ever leaving $\mathbb{R}$  (see Exercise 7 of Chapter 9), but clause 3 needs an eigenvalue to exist first, and existence of a root is a theorem about $\mathbb{C}$.

The geometry deserves as much attention as the algebra.
A symmetric matrix stretches or compresses space along $n$ perpendicular axes, its eigenvectors, by factors $\lambda_i$ that may be read as the extreme and critical values of the quadratic form $q(\mathbf{x})=\mathbf{x}^TA\mathbf{x}$ on the unit sphere: the transformation carries that sphere to an ellipsoid whose principal semi-axes point along the eigenvectors with lengths $|\lambda_i|$.
One frame of perpendicular directions suffices to describe everything the transformation does.

Now the question that begets this chapter.
An arbitrary matrix $A\in\mathbb{R}^{m\times n}$  — rectangular, asymmetric — has no eigenvectors to offer: its domain and codomain are different spaces, and iteration is not even defined.
Yet the ellipsoid picture refuses to die.
Every matrix, it turns out, carries the unit sphere of its domain to an ellipsoid in its codomain; what must be surrendered is the single frame, for the perpendicular axes of the input sphere and those of the output ellipsoid need no longer coincide.
Two orthonormal frames, one scaling between them: that is the singular value decomposition, and the next sections construct it — from the Spectral Theorem, applied to the symmetric surrogate $A^TA$.
*The SVD is the Spectral Theorem, freed from squareness.*

## 10.2 Spheres, Ellipsoids, & Singular Values

The geometry of a linear transformation $A\in\mathbb{R}^{m\times n}$ is vividly revealed by its action on the unit sphere in its domain, $\mathbb{R}^n$.
The unit sphere, defined by $\|\mathbf{x}\|^2=1$ or $\mathbf{x}^T\mathbf{x} = 1$, is deformed by $A$ into an ellipsoid in the codomain, $\mathbb{R}^m$  — the ellipsoid that closed the last section, now to be computed.

The shape and orientation of this output ellipsoid are determined by the symmetric positive semidefinite matrix $A^TA$.
The squared length of a transformed vector $A\mathbf{x}$ is given by:

$$
\|A\mathbf{x}\|^2 = (A\mathbf{x})^T(A\mathbf{x}) = \mathbf{x}^T(A^TA)\mathbf{x}.
$$

By the Spectral Theorem (Theorem 10.1), $A^TA$ (being an $n \times n$ symmetric matrix) has $n$ real, non-negative eigenvalues $\lambda_1 \geq \lambda_2 \geq \dots \geq \lambda_n \geq 0$.
Let $V=[\mathbf{v}_1 \dots \mathbf{v}_n]$ be an orthogonal matrix whose columns are the corresponding orthonormal eigenvectors of $A^TA$.
These eigenvectors $\mathbf{v}_i$ represent principal directions in the input space $\mathbb{R}^n$.
When $\mathbf{x}$ is one of these eigenvectors, say $\mathbf{x}=\mathbf{v}_i$, then

$$
\|A\mathbf{v}_i\|^2 = \mathbf{v}_i^T(A^TA)\mathbf{v}_i = \mathbf{v}_i^T(\lambda_i \mathbf{v}_i) = \lambda_i \|\mathbf{v}_i\|^2 = \lambda_i.
$$

*[Margin figure omitted]*

Thus, the matrix $A$ stretches the principal input direction $\mathbf{v}_i$ by a factor of $\sqrt{\lambda_i}$.
These stretching factors are fundamental to the transformation $A$.

**Definition 10.2 (Singular Values).** Let $A\in\mathbb{R}^{m\times n}$.
The $n \times n$ matrix $A^TA$ is symmetric and positive semidefinite, so its eigenvalues $\lambda_i$ are real and non-negative.
The **singular values** of $A$, denoted $\sigma_i$, are the square roots of these eigenvalues: $\sigma_i = \sqrt{\lambda_i}$.
They are conventionally arranged in descending order:

> The eigenvalues $\lambda_i$ specifically refer to those of $A^TA$.

$$
\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_n \geq 0.
$$

The number of non-zero singular values is $r = \operatorname{rank}(A^TA)$, and this is $\operatorname{rank}(A)$: Exercise 8 of Chapter 6 shows $\operatorname{ker}(A^TA)=\operatorname{ker} A$, and rank-nullity (Corollary 6.11) applied to two matrices with the same $n$ columns and the same kernel forces the same rank.
The corresponding orthonormal eigenvectors $\mathbf{v}_i$ of $A^TA$ are called the **right singular vectors** of $A$.

The image of the unit sphere under $A$ is an ellipsoid (possibly degenerate if $A$ is rank-deficient) in $\mathbb{R}^m$.
The semi-axes of this ellipsoid are aligned with certain vectors $\mathbf{u}_i \in \mathbb{R}^m$ and have lengths equal to the non-zero singular values $\sigma_i$.
The directions $\mathbf{v}_i$ in $\mathbb{R}^n$ are mapped by $A$ to these semi-axis vectors: $A\mathbf{v}_i = \sigma_i \mathbf{u}_i$.
The vectors $\mathbf{u}_i$ will be the **left singular vectors**.

**Example 10.3 (Two Frames, Not One).** Consider the $2\times 2$ matrix:

$$
A = \begin{bmatrix}
    3 & 0 \\
    4 & 5
    \end{bmatrix}
    \quad
    \Rightarrow
    \quad
    A^TA = \begin{bmatrix}
    25 & 20 \\
    20 & 25
    \end{bmatrix}
$$

The characteristic polynomial of $A^TA$ is $\lambda^2 - 50\lambda + 225 = 0$, whose roots are exactly $\lambda_1 = 45$ and $\lambda_2 = 5$.
The singular values are therefore $\sigma_1 = 3\sqrt{5} \approx 6.708$ and $\sigma_2 = \sqrt{5} \approx 2.236$, with product $\sigma_1\sigma_2 = 15 = |\det A|$: whatever else it does, $A$ multiplies areas by $15$.
The unit eigenvectors of $A^TA$ are $\mathbf{v}_1 = (1,1)^T/\sqrt{2}$ and $\mathbf{v}_2 = (-1,1)^T/\sqrt{2}$, and dividing their images by the corresponding singular values gives a second orthonormal pair,

$$
\mathbf{u}_1 = \frac{1}{\sigma_1}A\mathbf{v}_1 = \frac{1}{\sqrt{10}}\begin{bmatrix}1\\3\end{bmatrix} ,
    \qquad
    \mathbf{u}_2 = \frac{1}{\sigma_2}A\mathbf{v}_2 = \frac{1}{\sqrt{10}}\begin{bmatrix}-3\\1\end{bmatrix} ,
$$

and it is a genuinely different pair: $\mathbf{u}_1$ is not $\mathbf{v}_1$.
Note also what the eigenvalues of $A$ itself have to say.
The matrix is triangular, so they can be read off the diagonal: $3$ and $5$, nowhere near $6.708$ and $2.236$.
Eigenvalues report what survives iteration; singular values report what happens to length, and for an asymmetric matrix these are different questions with different answers.
The unit circle in $\mathbb{R}^2$ is carried to an ellipse in the codomain whose semi-axes have lengths $\sigma_1$ and $\sigma_2$ and point along $\mathbf{u}_1$ and $\mathbf{u}_2$  — the output frame, not the input one.

## 10.3 Constructing the SVD

The geometric insight that a linear transformation $A$ maps orthonormal principal input directions to orthogonal principal output directions, scaled by singular values, leads directly to its most fundamental factorization.
We aim to find orthogonal matrices $U$ and $V$ and a **rectangular diagonal** matrix $\Sigma$ such that $A = U\Sigma V^T$: that is, $\Sigma$ is $m\times n$, not necessarily square, and every entry away from the positions $(i,i)$ is zero.

### Step 1: Finding $V$ and the Singular Values $\sigma_i$.

As established in Section 10.2, the matrix $A^TA$ is an $n \times n$ symmetric positive semidefinite matrix.
By the Spectral Theorem, there exists an $n \times n$ orthogonal matrix $V = [\mathbf{v}_1 \dots \mathbf{v}_n]$ whose columns are orthonormal eigenvectors of $A^TA$, and an $n \times n$ diagonal matrix $\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ of corresponding non-negative eigenvalues, such that $A^TA = V\Lambda V^T$.
The singular values of $A$ are $\sigma_i = \sqrt{\lambda_i}$, ordered $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_n \ge 0$.
Let $r$ be the rank of $A$, which is also the number of non-zero singular values.
The columns $\mathbf{v}_1, \dots, \mathbf{v}_r$ form an orthonormal basis for $(\operatorname{ker} A)^\perp = \operatorname{im}(A^T)$, and $\mathbf{v}_{r+1}, \dots, \mathbf{v}_n$ form an orthonormal basis for $\operatorname{ker}(A^TA)$, which is $\operatorname{ker} A$ by Exercise 8.

### Step 2: Defining the Left Singular Vectors $U$.

For each $i=1, \dots, r$ (where $\sigma_i > 0$), define the vector $\mathbf{u}_i \in \mathbb{R}^m$ by

$$
\mathbf{u}_i = \frac{1}{\sigma_i} A\mathbf{v}_i.
$$

These $r$ vectors are orthonormal. To see this, consider their inner product:

$$
\begin{aligned}
\mathbf{u}_i^T \mathbf{u}_j &= \left(\frac{1}{\sigma_i} A\mathbf{v}_i\right)^T \left(\frac{1}{\sigma_j} A\mathbf{v}_j\right) = \frac{1}{\sigma_i \sigma_j} \mathbf{v}_i^T (A^TA) \mathbf{v}_j \\
    &= \frac{1}{\sigma_i \sigma_j} \mathbf{v}_i^T (\lambda_j \mathbf{v}_j) \quad (\text{since } \mathbf{v}_j \text{ is an eigenvector of } A^TA) \\
    &= \frac{\sigma_j^2}{\sigma_i \sigma_j} (\mathbf{v}_i^T \mathbf{v}_j).
\end{aligned}
$$

Orthonormality of $\{\mathbf{v}_k\}$ finishes it: the last factor vanishes when $i\neq j$, and when $i=j$ the coefficient collapses to $1$.
These $r$ vectors form an orthonormal basis for the image of $A$, $\operatorname{im}(A)$.

### Step 3: Completing the Orthonormal Basis $U$.

If $r < m$, the set $\{\mathbf{u}_1, \dots, \mathbf{u}_r\}$ does not span all of $\mathbb{R}^m$.
We can extend it to a full orthonormal basis for $\mathbb{R}^m$ by choosing an additional $m-r$ orthonormal vectors $\{\mathbf{u}_{r+1}, \dots, \mathbf{u}_m\}$ that form a basis for $(\operatorname{im} A)^\perp = \operatorname{ker}(A^T)$.
Let $U = [\mathbf{u}_1 \dots \mathbf{u}_r \dots \mathbf{u}_m]$ be the $m \times m$ orthogonal matrix whose columns are these left singular vectors.

> *Nota bene:* The columns of $U$ are also the orthonormal eigenvectors of $AA^T$, and the non-zero eigenvalues of $AA^T$ are $\sigma_1^2, \dots, \sigma_r^2$, the same as for $A^TA$.
> One could alternatively start by diagonalizing $AA^T$ to find $U$ and the $\sigma_i^2$.

Finally, let $\Sigma$ be the $m \times n$ matrix with $\Sigma_{ii} = \sigma_i$ for $i=1, \dots, \min(m,n)$ and every other entry zero.
The construction has produced $A\mathbf{v}_i = \sigma_i \mathbf{u}_i$ for $i\leq r$ and $A\mathbf{v}_i = \mathbf{0}$ for $i>r$, those $\mathbf{v}_i$ lying in $\operatorname{ker} A$; column by column, that is $AV=U\Sigma$.
Since $V$ is orthogonal, $A=U\Sigma V^T$.
This construction leads to the central theorem:

**Theorem 10.4 (Singular Value Decomposition).** Every matrix $A\in\mathbb{R}^{m\times n}$ admits a decomposition

$$
A = U\Sigma V^T \tag{10.1}
$$

where:

1. $U\in\mathbb{R}^{m\times m}$ is an orthogonal matrix whose columns are the left singular vectors of $A$.

2. $V\in\mathbb{R}^{n\times n}$ is an orthogonal matrix whose columns are the right singular vectors of $A$.

3. $\Sigma\in\mathbb{R}^{m\times n}$ is a rectangular diagonal matrix, where the diagonal entries $\Sigma_{ii} = \sigma_i$ are the singular values of $A$, ordered $\sigma_1\geq\sigma_2\geq\cdots\geq\sigma_n\geq 0$ as in Definition 10.2 — of which only the first $p=\min\{m,n\}$ have room on the diagonal of $\Sigma$.
    Nothing is lost by the crowding: when $m<n$, the singular values past the $p$th are necessarily zero, since $\operatorname{rank}(A^TA)=\operatorname{rank}(A)\leq m$ leaves at most $m$ of them nonzero and the descending order puts those first.

The singular values $\sigma_i$ are uniquely determined.

That last sentence is easily over-read, so it is worth the two lines it costs.
Let $A=U\Sigma V^T$ be *any* factorization of the admissible kind.
Then $A^TA=V(\Sigma^T\Sigma)V^T$, so $\Sigma^T\Sigma=V^T(A^TA)V$ is diagonal and similar to $A^TA$; its entries are the eigenvalues of $A^TA$, and the descending order fixes which is which.
Thus $\sigma_i^2=\lambda_i$, with no freedom left.
The singular values belong to $A$ alone.
The matrices $U$ and $V$ do not.
Flipping the signs of $\mathbf{u}_i$ and $\mathbf{v}_i$ *together* leaves the term $\sigma_i\mathbf{u}_i\mathbf{v}_i^T$ untouched, so each singular direction carries a free sign, spent in pairs; where a singular value repeats, any rotation within the corresponding block of singular vectors, applied to $U$ and $V$ alike, gives another valid decomposition; and the singular vectors belonging to $\sigma_i=0$ are constrained only to be an orthonormal basis of the kernel, on which $A$ imposes nothing at all.
*The singular values are unique; the frames that carry them are not.*

Both $U$ and $V$ are square here, and stated that way the theorem is easiest to prove.
In use they are almost never square.
Keeping the first $r$ columns of each — or the first $k$, when a truncation is wanted — leaves a rectangular matrix with orthonormal columns, an isometry in the sense of Section 5.5, and the composites part company at once: $V_k^TV_k=I_k$ records that the columns are orthonormal, while $V_kV_k^T$ is the orthogonal projection onto their span.
Chapter 11 computes with exactly that projection, and at $k<r$ it is what the reconstruction leaves behind.

This SVD reveals the fundamental action of $A$: it maps the $i$-th right singular vector $\mathbf{v}_i$ to $\sigma_i$ times the $i$-th left singular vector $\mathbf{u}_i$:

$$
A\mathbf{v}_i = \sigma_i\mathbf{u}_i \quad\text{for } i=1, \dots, \min(m,n).
$$

If $\sigma_i=0$, then $A\mathbf{v}_i = \mathbf{0}$.
The transformation $A$ acts in three moves:

1. Rotating/reflecting the input space so the basis vectors $\mathbf{e}_i$ align with $\mathbf{v}_i$ (action of $V^T$).

2. Scaling these aligned vectors by $\sigma_i$ along the new axes (action of $\Sigma$).

3. Rotating/reflecting the result into the output space so the scaled axes align with $\mathbf{u}_i$ (action of $U$).

## 10.4 Interpreting the SVD

The decomposition $A=U\Sigma V^T$ unveils the intrinsic geometry of the transformation $A$ represents.
Having constructed the components $U$, $\Sigma$, and $V$ in Section 10.3, we now consider their meaning and how they connect to core concepts like rank, the four fundamental subspaces, and the action of $A$ on its domain.

The singular values $\sigma_i$, found on the diagonal of $\Sigma$, are the stretching factors or "gains" of the transformation along specific orthogonal directions.
The largest singular value, $\sigma_1$, is precisely the spectral norm (or 2-norm) of $A$, representing the maximum factor by which $A$ can stretch any unit vector:

$$
\|A\|_2 = \max_{\|\mathbf{x}\|=1} \|A\mathbf{x}\| = \sigma_1.
$$

The ordered sequence $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$ (where $r=\operatorname{rank}(A)$) indicates the relative importance of different modes of the transformation.
A rapid decay in these singular values, as we shall see in Chapter 11, suggests that the matrix $A$ (and the data it might represent) is well-approximated by a matrix of lower rank.

> This is the cornerstone of dimensionality reduction and data compression techniques like Principal Component Analysis.

The columns of $V = [\mathbf{v}_1 \dots \mathbf{v}_n]$ are the **right singular vectors**.
Each $\mathbf{v}_i$ represents a **principal input direction**.
When $A$ represents data (e.g., rows as observations, columns as features), these $\mathbf{v}_i$ correspond to principal directions or inherent patterns within the feature space.
For instance, the term-document matrix of this chapter's application to text records at $a_{ij}$ the weight of word $i$ in document $j$; its columns are the documents, so there the $\mathbf{v}_i$ are themes read across the corpus, while the clusters of words that name those themes appear among the $\mathbf{u}_i$ instead.

> The vectors $\mathbf{v}_i$ are the directions in the domain that get mapped by $A$ to the semi-axes of the ellipsoid formed by transforming the unit sphere.

The columns of $U = [\mathbf{u}_1 \dots \mathbf{u}_m]$ are the **left singular vectors**, forming an orthonormal basis for the output space $\mathbb{R}^m$.
The set $\{\mathbf{u}_1, \dots, \mathbf{u}_r\}$ (corresponding to non-zero $\sigma_i$) forms an orthonormal basis for the image of $A$, $\operatorname{im}(A)$ (the **column space** in classical language).
These $\mathbf{u}_i$ are the **principal output directions**.
In a data context where rows of $A$ are observations, the columns of $U\Sigma$ (specifically $U_r\Sigma_r$, where $U_r$ and $\Sigma_r$ contain the first $r$ components) can be interpreted as the coordinates of the transformed data in the basis of principal output directions.

The SVD refines the Fundamental Theorem of Linear Algebra (Theorem 6.9) by handing over orthonormal bases for all four fundamental subspaces of $A:\mathbb{R}^n\rightarrow\mathbb{R}^m$ at once:

- The image $\operatorname{im}(A) \subset \mathbb{R}^m$ (classically the **column space**) has orthonormal basis $\{\mathbf{u}_1,\ldots,\mathbf{u}_r\}$, the left singular vectors with $\sigma_i>0$; so $\dim(\operatorname{im} A) = r$.

- The kernel $\operatorname{ker}(A) \subset \mathbb{R}^n$ (classically the **null space**) has orthonormal basis $\{\mathbf{v}_{r+1},\ldots,\mathbf{v}_n\}$; so $\dim(\operatorname{ker} A) = n-r$.

- The coimage, realized concretely as $\operatorname{im}(A^T) = (\operatorname{ker} A)^\perp \subset \mathbb{R}^n$ (classically the **row space**), has orthonormal basis $\{\mathbf{v}_1,\ldots,\mathbf{v}_r\}$: since $A^T = V\Sigma^T U^T$, these are left singular vectors for $A^T$. So $\dim(\operatorname{coim} A) = r$.

- The cokernel, realized concretely as $\operatorname{ker}(A^T) = (\operatorname{im} A)^\perp \subset \mathbb{R}^m$ (classically the **left null space**), has orthonormal basis $\{\mathbf{u}_{r+1},\ldots,\mathbf{u}_m\}$; so $\dim(\operatorname{coker} A) = m-r$.

The rank is the number of non-zero singular values, and Rank-Nullity becomes the count $(n-r)+r=n$.
The singular vectors say more than the count: written as $\dim(\operatorname{ker} A)+\dim(\operatorname{im} A^T)=n$, the two summands are not merely complementary in dimension but orthogonal complements in $\mathbb{R}^n$, spanned respectively by $\{\mathbf{v}_{r+1},\ldots,\mathbf{v}_n\}$ and $\{\mathbf{v}_1,\ldots,\mathbf{v}_r\}$.

> *Think:* The SVD decomposes $\mathbb{R}^n = \operatorname{im}(A^T) \boxplus \operatorname{ker}(A)$ and $\mathbb{R}^m = \operatorname{im}(A) \boxplus \operatorname{ker}(A^T)$, with $A$ acting as an isomorphism (scaled by $\sigma_i$) between $\operatorname{im}(A^T)$ and $\operatorname{im}(A)$.

The SVD expresses $A$ as a sum of $r$ rank-one matrices, often called the SVD expansion:

$$
A = U\Sigma V^T = \sum_{i=1}^r \sigma_i \mathbf{u}_i \mathbf{v}_i^T.
$$

Each term $\sigma_i \mathbf{u}_i \mathbf{v}_i^T$ is a rank-one matrix: the **outer product** of a column vector with a row vector, an $m\times n$ matrix every column of which is a multiple of $\mathbf{u}_i$ and every row a multiple of $\mathbf{v}_i^T$.
This expansion shows $A$ as a linear combination of these fundamental rank-one *layers*, ordered by the magnitude of their corresponding singular values $\sigma_i$.
This form is pivotal for low-rank approximation (Chapter 11), where truncating this sum by keeping only the first $k$ terms yields $A_k = \sum_{i=1}^k \sigma_i \mathbf{u}_i \mathbf{v}_i^T$, which Lemma 10.7 will show is the best rank-$k$ approximation in the spectral norm, and which Chapter 11 will show is best in the Frobenius norm as well.

Finally, the SVD provides the most general and stable way to define the pseudoinverse $A^\dagger$ of any matrix $A$, extending the concept from Chapter 6.
If $A = U\Sigma V^T$, its pseudoinverse is given by:

$$
A^\dagger = V \Sigma^\dagger U^T.
$$

Here, $\Sigma^\dagger$ is an $n \times m$ rectangular diagonal matrix.
If $\Sigma_{ii} = \sigma_i > 0$, then $(\Sigma^\dagger)_{ii} = 1/\sigma_i$.
If $\Sigma_{ii} = 0$, then $(\Sigma^\dagger)_{ii} = 0$.
All off-diagonal entries of $\Sigma^\dagger$ are zero.

The pseudoinverse $A^\dagger$ effectively inverts the action of $A$ where possible:

- It maps vectors from $\operatorname{im}(A)$ back to $\operatorname{im}(A^T)$ by undoing the scaling by $\sigma_i$: if $\mathbf{y} = \sigma_i \mathbf{u}_i \in \operatorname{im}(A)$, then $A^\dagger \mathbf{y} = \mathbf{v}_i$.

- It maps vectors from $(\operatorname{im} A)^\perp = \operatorname{ker}(A^T)$ to the zero vector in $\mathbb{R}^n$.

As discussed in Chapter 6, $A^\dagger\mathbf{b}$ yields the minimum-norm least-squares solution to $A\mathbf{x}=\mathbf{b}$.
The SVD construction of $A^\dagger$ makes this general for any $A$.
Furthermore, $AA^\dagger = U_rU_r^T$ (where $U_r = [\mathbf{u}_1 \dots \mathbf{u}_r]$) is the orthogonal projection onto $\operatorname{im}(A)$, and $A^\dagger A = V_rV_r^T$ (where $V_r = [\mathbf{v}_1 \dots \mathbf{v}_r]$) is the orthogonal projection onto $\operatorname{im}(A^T)$.

This formula also settles a debt.
Theorem 6.16 of Chapter 6 listed seven properties of the pseudoinverse and settled the first four; the last three were deferred to here.
They were stated for a transformation $T$ and its adjoint $T^*$, which in orthonormal bases is the transpose, so read $A$ for $T$ and $A^T$ for $T^*$ throughout.
Clause 5 asks that $A^\dagger=A^{-1}$ when $A$ is invertible: then $m=n$, every $\sigma_i>0$, and $\Sigma$ is square and invertible with $\Sigma^\dagger=\Sigma^{-1}$, so $A^\dagger=V\Sigma^{-1}U^T=(U\Sigma V^T)^{-1}=A^{-1}$.
Clause 6 asks that $(A^\dagger)^\dagger=A$.
The recipe $U\Sigma V^T\mapsto V\Sigma^\dagger U^T$ needs only that $U$ and $V$ be orthogonal and $\Sigma$ rectangular diagonal with nonnegative entries — restoring descending order permutes the columns of $U$ and of $V$ together and changes nothing — so it applies to $A^\dagger=V\Sigma^\dagger U^T$ and returns $U(\Sigma^\dagger)^\dagger V^T$.
Transposing a rectangular diagonal matrix twice and reciprocating its nonzero entries twice restores it, so $(\Sigma^\dagger)^\dagger=\Sigma$ and $(A^\dagger)^\dagger=A$.
Clause 7 asks that $(A^T)^\dagger=(A^\dagger)^T$: since $A^T=V\Sigma^TU^T$ is a decomposition of the same kind,

$$
(A^T)^\dagger = U(\Sigma^T)^\dagger V^T = U(\Sigma^\dagger)^T V^T = \left(V\Sigma^\dagger U^T\right)^T = (A^\dagger)^T .
$$

The pseudoinverse also completes an argument begun in Chapter 6.
There, ridge regression replaced $A^\dagger$ with the regularized pseudoinverse $(A^TA+\lambda I)^{-1}A^T$ at a penalty strength $\lambda>0$, and an identity was claimed; the SVD now delivers it.
Substituting $A=U\Sigma V^T$ gives $A^TA+\lambda I = V(\Sigma^T\Sigma+\lambda I)V^T$, whence

$$
(A^TA+\lambda I)^{-1}A^T
    \;=\; V(\Sigma^T\Sigma+\lambda I)^{-1}\Sigma^T U^T
    \;=\; V\,\operatorname{diag}\!\left(\frac{\sigma_i}{\sigma_i^2+\lambda}\right)_{i=1}^{p}U^T
$$

with $p=\min\{m,n\}$ as usual.
Positivity of $\lambda$ is what makes the middle inverse exist: the diagonal entries of $\Sigma^T\Sigma+\lambda I$ are $\sigma_i^2+\lambda$, and these are bounded below by $\lambda$ whatever the rank of $A$.
Set this beside the pseudoinverse itself and beside the pseudoinverse of the truncation $A_k$:

$$
A^\dagger = V\,\operatorname{diag}\!\left(\frac{1}{\sigma_i}\right)U^T
    \qquad\qquad
    A_k^\dagger = V\,\operatorname{diag}\!\left(\frac{1}{\sigma_1},\ldots,\frac{1}{\sigma_k},0,\ldots,0\right)U^T
$$

In both the reciprocal is taken over the nonzero $\sigma_i$ only, exactly as in the construction of $\Sigma^\dagger$ above; a direction that $A$ has already collapsed is not inverted but discarded, and the truncation index is any $k\leq r$.
All three are of the form $V\operatorname{diag}(\varphi(\sigma_i))U^T$ for a choice of **filter** $\varphi$ acting on the singular spectrum.
The pseudoinverse inverts every direction; truncation inverts the strong and kills the weak outright; ridge inverts the strong and damps the weak, rolling off smoothly as $\sigma_i^2$ falls below $\lambda$.
*Regularization is a choice of filter on the singular spectrum.*

## 10.5 Invariance & Natural Structure

The singular values are invariants of the transformation — quantities that remain unchanged when viewed through different orthonormal bases.
If $Q_1$ and $Q_2$ are orthogonal matrices, the transformation $B=Q_1AQ_2^T$ represents the same underlying map as $A$, merely viewed through different coordinates.
Yet its singular values match those of $A$ exactly, measuring intrinsic stretching factors independent of our choice of measurement frame.

Two matrix norms emerge from this geometric perspective:

**Definition 10.5 (Matrix Norms).** For a matrix $A\in\mathbb{R}^{m\times n}$:

1. The **spectral norm** (or **2-norm**) measures maximal stretching:


$$
\|A\|_2 = \max_{\|\mathbf{x}\|=1} \|A\mathbf{x}\| = \sigma_1
$$

2. The **Frobenius norm** measures total energy:


$$
\|A\|_F = \left(\sum_{i,j} a_{ij}^2\right)^{1/2} = \left(\sum_{i=1}^p \sigma_i^2\right)^{1/2}
$$

> *Nota bene:* the second equality in each clause is a claim, not a definition.
> The first is the content of Section 10.4; the second is Exercise 6.

These norms connect deeply to the SVD structure through the fundamental metrics $A^TA$ and $AA^T$ in domain and codomain:

$$
A^TA = V\Sigma^T\Sigma V^T = \sum_{i=1}^p \sigma_i^2\mathbf{v}_i\mathbf{v}_i^T
    \quad\text{and}\quad
    AA^T = U\Sigma\Sigma^T U^T = \sum_{i=1}^p \sigma_i^2\mathbf{u}_i\mathbf{u}_i^T
$$

The equality of nonzero eigenvalues between these matrices now emerges from singular value structure.

Singular values also control the composition of transformations.
While eigenvalues can grow explosively under matrix multiplication, singular values satisfy delicate inequalities:

**Lemma 10.6 (Singular Values under Composition).** Let $A\in\mathbb{R}^{m\times n}$ and $B\in\mathbb{R}^{n\times q}$, with the singular values of each in descending order.
Then for every $k\leq\min\{m,n,q\}$,

$$
\sigma_k(AB) \;\leq\; \sigma_k(A)\,\sigma_1(B)
    \qquad\text{and}\qquad
    \sigma_k(AB) \;\leq\; \sigma_1(A)\,\sigma_k(B) .
$$

Both follow from a variational reading of $\sigma_k$ worth having in its own right: the $k$th singular value is the distance, in the spectral norm, from the matrix to the nearest matrix of rank less than $k$.

**Lemma 10.7 (Singular Values as Distances).** Let $M\in\mathbb{R}^{m\times n}$ and let $1\leq k\leq p=\min\{m,n\}$. Then

$$
\sigma_k(M) \;=\; \min\left\{\, \|M-X\|_2 \;:\; X\in\mathbb{R}^{m\times n},\ \operatorname{rank} X < k \,\right\} .
$$

*Proof.* Write $M=\sum_{i=1}^{p}\sigma_i\mathbf{u}_i\mathbf{v}_i^T$, the SVD expansion carried out to $p$ terms, those past the rank contributing nothing.
Set $X_0=\sum_{i<k}\sigma_i\mathbf{u}_i\mathbf{v}_i^T$, a matrix of rank at most $k-1$.
Then $M-X_0=\sum_{i\geq k}\sigma_i\mathbf{u}_i\mathbf{v}_i^T$ is again an orthogonal matrix times a rectangular diagonal one times an orthogonal matrix, its only nonzero diagonal entries being $\sigma_k\geq\sigma_{k+1}\geq\cdots$; permuting the columns of the two orthogonal factors to bring those entries first displays an SVD, so $\|M-X_0\|_2=\sigma_k$.
The minimum is therefore at most $\sigma_k$, and it is attained.

For the reverse inequality, let $X$ be any matrix with $\operatorname{rank} X<k$ and put $S=\operatorname{span}\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}$, a $k$-dimensional subspace of $\mathbb{R}^n$.
Apply rank-nullity to $X$ restricted to $S$: since $X(S)\subseteq\operatorname{im} X$ has dimension at most $\operatorname{rank} X\leq k-1$,

$$
\dim(S\cap\operatorname{ker} X) \;=\; k-\dim X(S) \;\geq\; k-(k-1) \;=\; 1 ,
$$

so some unit vector $\mathbf{w}\in S$ satisfies $X\mathbf{w}=\mathbf{0}$.
Write $\mathbf{w}=\sum_{i=1}^k c_i\mathbf{v}_i$ with $\sum_i c_i^2=1$.
Then $M\mathbf{w}=\sum_{i=1}^k c_i\sigma_i\mathbf{u}_i$, and the $\mathbf{u}_i$ are orthonormal, so

$$
\|M-X\|_2^2 \;\geq\; \|(M-X)\mathbf{w}\|^2 \;=\; \|M\mathbf{w}\|^2 \;=\; \sum_{i=1}^k c_i^2\sigma_i^2 \;\geq\; \sigma_k^2 ,
$$

the last step because $\sigma_i\geq\sigma_k$ for every $i\leq k$. ∎

*Proof.* The spectral norm is submultiplicative: for any unit $\mathbf{x}$, $\|AC\mathbf{x}\|\leq\|A\|_2\|C\mathbf{x}\|\leq\|A\|_2\|C\|_2$, so $\|AC\|_2\leq\|A\|_2\|C\|_2$.
Let $B_{k-1}$ be the truncation of $B$ to its first $k-1$ terms, so that $\operatorname{rank} B_{k-1}<k$ and, by Lemma 10.7, $\|B-B_{k-1}\|_2=\sigma_k(B)$.
The image of $AB_{k-1}$ lies inside $A(\operatorname{im} B_{k-1})$, so $AB_{k-1}$ also has rank less than $k$, and Lemma 10.7 applied to $AB$ gives

$$
\begin{aligned}
\sigma_k(AB) &\leq \|AB-AB_{k-1}\|_2 = \|A(B-B_{k-1})\|_2 \\
    &\leq \|A\|_2\,\|B-B_{k-1}\|_2 = \sigma_1(A)\,\sigma_k(B) .
\end{aligned}
$$

The first inequality follows by transposition.
From $A^T=V\Sigma^TU^T$ one reads $\sigma_j(A^T)=\sigma_j(A)$ for all $j\leq\min\{m,n\}$, and likewise for $B$; applying what was just proved to $(AB)^T=B^TA^T$ yields

$$
\sigma_k(AB)=\sigma_k(B^TA^T)\leq\sigma_1(B^T)\sigma_k(A^T)=\sigma_1(B)\sigma_k(A) ,
$$

which is the first inequality of the lemma. ∎

This control has no analog for eigenvalues: the spectral radius of Definition 9.2 is not submultiplicative.
Take $N=\begin{bmatrix}0&1\\0&0\end{bmatrix}$ and $M=\begin{bmatrix}0&0\\1&0\end{bmatrix}$: both are nilpotent, so $\rho_N=\rho_M=0$, and yet $NM=\begin{bmatrix}1&0\\0&0\end{bmatrix}$ has $\rho_{NM}=1$.
Two matrices whose spectra consist of nothing but zero compose to a projection; the eigenvalue appears out of nothing.
The singular values of the very same pair are perfectly obedient — $\sigma_1(N)=\sigma_1(M)=\sigma_1(NM)=1$ and $\sigma_2$ vanishes for all three — and Lemma 10.6 holds with equality throughout.

The singular values also provide the most natural measure of matrix rank:

$$
\operatorname{rank}(A) = \#\{\sigma_i > 0\}
$$

This equality illuminates the geometric meaning of rank as counting independent stretching directions.
More subtly, small singular values indicate directions that are *nearly* dependent — which is what makes rank, in Chapter 11, a numerical question rather than an exact one.

The singular values quantify precisely how the matrix distorts space under transformation.
Recall from Chapter 1 the notion of condition number as a measure of numerical sensitivity.
The SVD framework now allows us to define this concept rigorously:

**Definition 10.8 (Condition Number).** Let $A$ be nonsingular, so that every singular value is positive.
Its **condition number** is the ratio

$$
\operatorname{cond}(A) = \frac{\sigma_1}{\sigma_n}
$$

of the largest singular value to the smallest.
For singular matrices, we set $\operatorname{cond}(A)=\infty$.

This definition illuminates why condition number measures sensitivity.
When solving $A\mathbf{x}=\mathbf{b}$, the SVD shows that $A$ stretches some directions by $\sigma_1$ while compressing others by $\sigma_n$.
The ratio $\sigma_1/\sigma_n$ thus bounds how much relative errors can be amplified when computing solutions.
More precisely, a perturbation $\delta\mathbf{b}$ of the right-hand side moves the solution by $\delta\mathbf{x}=A^{-1}\delta\mathbf{b}$, whence

$$
\|\delta\mathbf{x}\| \;\leq\; \frac{\|\delta\mathbf{b}\|}{\sigma_n}
    \qquad\text{and}\qquad
    \frac{\|\delta\mathbf{x}\|}{\|\mathbf{x}\|} \;\leq\; \operatorname{cond}(A)\,\frac{\|\delta\mathbf{b}\|}{\|\mathbf{b}\|} .
$$

The second is the one to carry away.
A condition number is a ratio of singular values and therefore a pure number, carrying no units of $\mathbf{b}$ or of $\mathbf{x}$; it can bound the amplification of a *relative* error and nothing else.
Rescaling $A$ by $10^{-3}$ multiplies every $\|\delta\mathbf{x}\|$ by $10^{3}$ and leaves $\operatorname{cond}(A)$ exactly where it was.

The condition number remains unchanged under orthogonal transformations: if $Q_1$ and $Q_2$ are orthogonal, then $\operatorname{cond}(Q_1AQ_2)=\operatorname{cond}(A)$.
This invariance reflects that conditioning measures intrinsic sensitivity rather than artifacts of particular coordinate choices.
Indeed, $\operatorname{cond}(A)$ can be characterized independently of the SVD as

$$
\operatorname{cond}(A) = \|A\|_2\,\|A^{-1}\|_2 ,
$$

since $\|A\|_2=\sigma_1$ while the singular values of $A^{-1}$ are the reciprocals $1/\sigma_n\geq\cdots\geq1/\sigma_1$, so that $\|A^{-1}\|_2=1/\sigma_n$.
The spectral norm is not interchangeable here with any other orthogonally invariant norm.
The Frobenius norm is orthogonally invariant, yet $\|I_n\|_F\|I_n^{-1}\|_F=n$ where $\operatorname{cond}(I_n)=1$; since $\|A\|_F\geq\|A\|_2$ always, the Frobenius product overshoots $\operatorname{cond}(A)$ for every invertible $A$ of size at least two.

> *Example:* The matrix from Example 1.14 in Chapter 1,
>
>

$$
>
> A = \begin{bmatrix}
> 1 & 0.999 \\
> 0 & 0.001
> \end{bmatrix}
>
>
$$

>
> has singular values $\sigma_1\approx 1.41351$ and $\sigma_2\approx 0.000707$, so $\operatorname{cond}(A)\approx 1998$: about 2000, as claimed there.
> A check that costs nothing: $\sigma_1\sigma_2=|\det A|=0.001$.

## 10.6 Inner Products & the SVD

The singular value decomposition generalizes naturally to linear transformations between arbitrary inner product spaces.
Given $T:V\rightarrow W$ between finite-dimensional inner product spaces, the adjoint $T^*:W\rightarrow V$ defined in Chapter 5 allows us to form $T^*T:V\rightarrow V$ and $TT^*:W\rightarrow W$.
These self-adjoint operators play the role of $A^TA$ and $AA^T$, with their spectral properties determining the SVD structure.

More precisely, let $\{\mathbf{v}_1,\ldots,\mathbf{v}_n\}$ be orthonormal eigenvectors of $T^*T$ with eigenvalues $\{\sigma_1^2,\ldots,\sigma_n^2\}$.
For each nonzero singular value $\sigma_i$, the vector $\mathbf{u}_i=\frac{1}{\sigma_i}T\mathbf{v}_i$ is well-defined, and these vectors form an orthonormal set in $W$.
The transformation then admits decomposition:

> *Definition:* For vectors $\mathbf{u}\in W$ and $\mathbf{v}\in V$, the tensor product $\mathbf{u}\otimes\mathbf{v}$ denotes the rank-one operator sending $\mathbf{x}\mapsto \langle\mathbf{x},\mathbf{v}\rangle\mathbf{u}$.
> This generalizes the matrix outer product $\mathbf{u}\mathbf{v}^T$ to arbitrary inner product spaces, extending associatively to more factors.

$$
T = \sum_{i=1}^r \sigma_i(\mathbf{u}_i\otimes\mathbf{v}_i)
$$

where $r=\operatorname{rank}(T)$.
When expressed in orthonormal bases, this abstract decomposition yields exactly the matrix factorization $A=U\Sigma V^T$ developed earlier.

This coordinate-free perspective reveals the SVD as a fundamental property of linear transformations between finite-dimensional inner product spaces.
Finite dimensionality is not a convenience here.
Compact operators between Hilbert spaces admit a similar decomposition, with countably many singular values decaying to zero — the **Schmidt decomposition** of an integral kernel — but a general bounded operator admits none.
Nor is the inner product a convenience: without it there is no adjoint, no orthogonality, and no seam along which to cut.

**Example 10.9 (Finite-Dimensional Function Spaces).** Consider the space $\mathcal{P}_n$ of polynomials of degree at most $n$, equipped with the $L^2$ inner product on $[0,1]$: $\langle f,g\rangle=\int_0^1 f(t)g(t)\,dt$.
The differentiation operator $D:\mathcal{P}_n\to\mathcal{P}_{n-1}$ is linear, and its adjoint $D^*:\mathcal{P}_{n-1}\to\mathcal{P}_n$ is an ordinary polynomial map: integration by parts absorbs the boundary terms into the polynomial, and no integral survives.
For $n=2$ one computes $D^*(1)=12t-6$ and $D^*(t)=30t^2-24t+2$, and $\langle Df,g\rangle=\langle f,D^*g\rangle$ may be checked directly on the monomials.
Though we work with functions, the finite-dimensionality of these polynomial spaces is what guarantees the SVD exists; it is no more unique here than it was for matrices, and for the same reasons.

Back in coordinates, a matrix assigns a number to each choice of two indices, one for the row and one for the column.
Two indices are not always enough.
A **tensor** of order $k$ assigns a number to each choice of $k$ indices, $\mathcal{T}=[t_{i_1i_2\cdots i_k}]$ with $1\leq i_j\leq n_j$; a stack of colour images varying over time, or the weights of a convolutional layer, organizes itself this way and not into a matrix.
Much survives the extension: fibers and slices in place of rows and columns, outer products, and decompositions bearing the names CP and Tucker.
One thing does not.
A matrix always has a best rank-$k$ approximation; a tensor need not.
The order-three tensor $\mathbf{e}_1\otimes\mathbf{e}_1\otimes\mathbf{e}_2+\mathbf{e}_1\otimes\mathbf{e}_2\otimes\mathbf{e}_1+\mathbf{e}_2\otimes\mathbf{e}_1\otimes\mathbf{e}_1$ has rank $3$, yet sums of two rank-one tensors approach it to within any tolerance one cares to name, and not one of them attains the infimum.

The SVD gives one last gift to the Fundamental Theorem of Chapter 3.
A linear transformation $T:V\rightarrow W$ induces four fundamental spaces, and the two born as quotients now stand revealed as subspaces in disguise:

$$
\operatorname{coker} T = W/\operatorname{im} T \cong (\operatorname{im} T)^\perp
    \qquad\text{and}\qquad
    \operatorname{coim} T = V/\operatorname{ker} T \cong (\operatorname{ker} T)^\perp ,
$$

the isomorphisms being the work of the inner product, which selects from each equivalence class its unique orthogonal representative.
The singular vectors furnish orthonormal bases for all four spaces at once: right singular vectors with $\sigma_i>0$ span $(\operatorname{ker} T)^\perp\cong\operatorname{coim} T$ while the remainder span $\operatorname{ker} T$; left singular vectors with $\sigma_i>0$ span $\operatorname{im} T$ while the remainder span $(\operatorname{im} T)^\perp\cong\operatorname{coker} T$.
Between the chosen bases, $T$ acts by pure scaling, each singular value declaring how loudly its coimage direction speaks in the image.
*The Fundamental Theorem names the spaces; the inner product measures them; the SVD weds the two.*

—

## Latent Semantic Structure in Text

Words are known by the company they keep.
The singular value decomposition makes that maxim quantitative: given a record of which words occur in which documents, it returns the axes along which meaning varies, recovering latent structure from nothing but patterns of co-occurrence.

Consider a collection of documents represented through their word frequencies.
Each document becomes a vector in a high-dimensional space where each dimension corresponds to a possible word.
The complete corpus forms a term-document matrix $A$ where entry $a_{ij}$ represents the (weighted) occurrence of word $i$ in document $j$.
This matrix, though sparse and high-dimensional, contains rich structure that the SVD can expose.

The singular value decomposition $A=U\Sigma V^T$ sorts that structure three ways: left singular vectors (columns of $U$) gather words that tend to occur together, right singular vectors (columns of $V$) identify document themes, and the singular values measure the strength of these semantic associations.
This decomposition often captures genuine semantic relationships despite operating purely on word co-occurrence patterns.
Words with similar meanings tend to appear in similar contexts, creating parallel rows in the term-document matrix.
The SVD detects these parallels and groups related terms in its singular vectors.

**Example 10.10 (Scientific Abstract Analysis).** Consider analyzing a collection of physics abstracts.
Grouping does not begin at the top: a term-document matrix is nonnegative, so $AA^T$ is nonnegative and symmetric, and its dominant eigenvector — which is $\mathbf{u}_1$  — may be taken with every entry of one sign, recording overall frequency rather than any contrast between groups.
From $\mathbf{u}_2$ onward, the left singular vectors often reveal clear semantic groupings:

1. Experimental terms: "measurement", "observation", "data", "experiment"

2. Theoretical terms: "model", "theory", "prediction", "framework"

3. Quantum terms: "state", "superposition", "entanglement", "qubit"

These groupings emerge from co-occurrence patterns, without any explicit semantic knowledge provided to the algorithm.

The singular values tell their own story.
They typically follow a power law decay, with a few large values followed by many smaller ones.
This suggests that most semantic content lies in a low-dimensional subspace: the image of the truncated matrix $A_k$, spanned by the leading left singular vectors.
Indexing and search become geometry in that image — a document is retrieved not for the words it literally contains but for its position in $\operatorname{im} A_k$.

Several practical refinements (such as term frequency-inverse document frequency weighting) as well as more sophisticated modern methods together augment these SVD foundations.
Word embeddings like *Word2Vec* create dense vector representations of words that capture subtle semantic relationships.
Yet these methods still reflect the fundamental insight that meaning emerges from patterns of association — patterns that the SVD is uniquely suited to reveal.

> *Historical Note:* Latent Semantic Analysis (LSA), developed in the late 1980s, used the SVD as its foundational mathematical tool.
> This application of matrix factorization to language transformed both theoretical linguistics and practical information retrieval systems.

Just as the singular value decomposition exposes preferred directions of stretching in any linear map, it exposes the semantic axes hidden in the high-dimensional space of words — and to project onto them is to discard everything else.
What is discarded is much of what separates two near-synonyms; what survives is the meaning they share.
*Meaning is a low-dimensional quotient of the space of words.*

—

## Sensor Networks & The Geometry of Measurement

Sensors are the nerves of the Industrial Body — temperature probes in data centers, accelerometers in smartphones, pressure gauges in industrial plants.
Each device measures external aspects of reality, yet these measurements harbor systematic errors from manufacturing variations, environmental conditions, and malfunctions.
The singular value decomposition separates the signal from the corruption by geometry alone: the true reading and each sensor's private error live in different subspaces, and the decomposition finds the seam.

Consider an array of $n$ sensors measuring the same physical quantity at $m$ different times or conditions.
In an ideal world, these measurements would differ only by known physical variations.
Reality proves messier — each sensor has its own gain, offset, and noise characteristics.
A **measurement matrix** $M\in\mathbb{R}^{m\times n}$ contains these corrupted observations:

$$
M_{ij} = g_j(s_i + \eta_{ij}) + b_j
$$

where the rows of $M$ index the $m$ times and the columns the $n$ sensors: $s_i$ is the true signal at time $i$, $g_j$ and $b_j$ are the **gain** and **bias** of sensor $j$, and $\eta_{ij}$ represents noise.

The SVD of this measurement matrix lays the structure bare.
After centering each sensor's readings (subtracting its mean), we obtain:

$$
M = U\Sigma V^T = \sum_{k=1}^r \sigma_k\mathbf{u}_k\mathbf{v}_k^T
$$

Because the two index sets live in different spaces — the left singular vectors $\mathbf{u}_k\in\mathbb{R}^m$ over times, the right singular vectors $\mathbf{v}_k\in\mathbb{R}^n$ over sensors — the decomposition sorts the temporal signal from the sensor-side corruption.
The leading left singular vector $\mathbf{u}_1$ often captures the true underlying signal as it varies across the $m$ conditions, while $\mathbf{v}_1$ records the accompanying gain pattern across the sensors; the remaining terms are less exciting than one might hope:

- $\sigma_1\mathbf{u}_1\mathbf{v}_1^T$ approximates the physical variation

- were the noise $\eta$ zero, the centered matrix would be *exactly* that one term — gains, biases and all

- so $\sigma_2$ and beyond measure departure from the rank-one ideal: noise first, and then whatever the model has failed to describe

**Example 10.11 (Temperature Sensor Array).** Consider a server room monitored by 100 temperature sensors sampled every minute.
Over an hour of operation (60 samples), we obtain a $60\times 100$ measurement matrix.
The SVD typically reveals:

1. First singular value $\sim 10\times$ larger than second, reflecting true temperature variation

2. A malfunctioning sensor — one whose noise dwarfs its neighbours' — announces itself as a large entry of $\mathbf{v}_2$

3. Third and beyond capture various drift and noise patterns

This decomposition enables both data cleaning and sensor fault detection.

> *Terminology:* This effective rank formula appears in random matrix theory and quantum mechanics as the participation ratio, measuring how many components participate significantly in a system.

The singular values themselves provide diagnostic information.
Define the **effective rank** of the measurement matrix as:

$$
r_{\text{eff}} = \left(\sum_{i=1}^r \sigma_i^2\right)^2 \bigg/ \sum_{i=1}^r \sigma_i^4
$$

This quantity, always between $1$ and $r=\operatorname{rank}(M)$, measures how many independent patterns exist in the data.
A value near 1 says the array sits close to the rank-one ideal; larger values measure how far it strays.
Note what this does *not* detect: gain and bias are precisely what the rank-one structure and the centering absorb, so at zero noise $r_{\text{eff}}$ is exactly $1$ whatever the gains and offsets may be.

More sophisticated analysis uses the full SVD structure to calibrate the sensor array.
If $\mathbf{u}_1$ approximates the true signal direction — the signal as it varies over the $m$ times — we can estimate each sensor's gain by comparing its column against this reference:

$$
\hat{g}_j = \frac{\langle \mathbf{m}_j, \mathbf{u}_1\rangle}{\|\mathbf{u}_1\|^2}
$$

where $\mathbf{m}_j\in\mathbb{R}^m$ is the $j$-th column of $M$ (centered), the readings of sensor $j$ over all $m$ times.
The dot product is well posed because both vectors live in the time space $\mathbb{R}^m$; and since the rank-one ideal gives $\mathbf{m}_j \approx \sigma_1(\mathbf{v}_1)_j\,\mathbf{u}_1$, this projection returns $\sigma_1(\mathbf{v}_1)_j$ — the sensor's gain, read off up to the one common scale.

> More complex calibration models can be addressed through careful analysis of the singular vectors.

This approach to sensor calibration reveals a deeper truth about physical measurement: though raw data often appears complex and corrupted, the underlying signal typically lives in a low-dimensional subspace.
Systematic errors, rather than creating pure noise, generate characteristic geometric patterns that the SVD naturally detects and isolates.
Modern sensor networks extend these principles through sliding window analysis for time-varying calibration and distributed computation across large arrays, yet the core insight remains: measurement errors, seemingly complex, often possess simple structure when viewed in the right coordinates.
*A calibrated array is one whose sensors agree, up to scale, on a single left singular vector.*

—

## Exercises: Chapter 10

1. Compute the singular value decomposition of each of

$$
A = \begin{bmatrix}4 & 1\\7 & 4\end{bmatrix}
    \qquad\text{and}\qquad
    A = \begin{bmatrix}3 & 1\\1 & 2\\2 & -1\end{bmatrix}
$$

by diagonalizing $A^TA$ for $V$ and $\Sigma$, taking $\mathbf{u}_i=A\mathbf{v}_i/\sigma_i$ exactly as Step 2 of Section 10.3 does, and completing $U$ as Step 3 does.
Do not instead obtain $U$ by diagonalizing $AA^T$: that pins each $\mathbf{u}_i$ only up to sign, and a single wrong sign destroys the factorization while leaving every eigenvector computation correct.
For the first matrix check that $\sigma_1\sigma_2=|\det A|$.

2. The **Hilbert matrix** $H_n$ has entries $h_{ij}=1/(i+j-1)$.
Show that $H_n$ is the Gram matrix of the monomials $1,t,\ldots,t^{n-1}$ under the inner product $\langle f,g\rangle=\int_0^1f(t)g(t)\,dt$ of Chapter 5, and conclude from the independence of those monomials that $H_n$ is symmetric and positive definite.
Then compute $\operatorname{cond}(H_n)$ numerically for $n=2,\ldots,6$ and estimate the factor by which it grows with each monomial added.

3. Compute the singular value decomposition of

$$
A = \begin{bmatrix}
    2 & 0 & 2 & 0\\
    1 & 1 & 1 & 1\\
    0 & 2 & 0 & 2
    \end{bmatrix} ,
$$

whose $A^TA$ can be diagonalized by inspection.
Read orthonormal bases for the image, the kernel, the coimage and the cokernel off the singular vectors as Section 10.4 prescribes, check all four dimensions against Corollary 6.11, and confirm that the bases you obtain exhibit the two orthogonal splittings of Theorem 6.9.
Both $\operatorname{ker} A$ and $\operatorname{coker} A$ are nonzero here, so the construction of Section 10.3 does not determine every singular vector: identify the free ones and say how many continuous parameters and how many discrete choices they carry between them.

4. Let $A=\begin{bmatrix}50 & 51\\51 & 50\end{bmatrix}$ and let $\mathbf{b}=(102,100)^T$, which is $(101,101)^T$ displaced by $(1,-1)^T$.
Find the singular values and singular vectors of $A$, and verify that the displacement lies entirely along $\mathbf{u}_2$.
Compute the pseudoinverse solution $A^\dagger\mathbf{b}$, the truncated solution $A_1^\dagger\mathbf{b}$, and the ridge solution $V\operatorname{diag}\!\left(\sigma_i/(\sigma_i^2+\lambda)\right)U^T\mathbf{b}$ at $\lambda=202$, the three filters of Section 10.4.
Compare each against the solution of $A\mathbf{x}=(101,101)^T$, and report by what factor each filter multiplies the displacement $(1,-1)^T$ on its way into the answer.

5. Let $A=\begin{bmatrix}2 & -5\\2 & -2\end{bmatrix}$.
Compute its singular value decomposition, and from it the factors $H=U\Sigma U^T$ and $Q=UV^T$, so that $A=HQ$ with $H$ symmetric positive definite and $Q$ orthogonal.
Confirm that $H^2=AA^T$ and that $HQ=A$, and describe $Q$ geometrically.
Say what $H$ and $Q$ become when $A$ is itself symmetric positive definite.

6. Let $A\in\mathbb{R}^{m\times n}$ and write $p=\min\{m,n\}$.
Show that $\sum_{i,j}a_{ij}^2=\operatorname{tr}(A^TA)$ by reading the diagonal entries of $A^TA$, then combine this with the expansion $A^TA=\sum_{i=1}^{p}\sigma_i^2\mathbf{v}_i\mathbf{v}_i^T$ of Section 10.5 and the linearity of the trace to prove the Frobenius identity $\|A\|_F^2=\sum_{i=1}^{p}\sigma_i^2$ that Definition 10.5 asserts without proof.
Deduce also that $\|A\|_F\geq\|A\|_2$, the inequality by which Section 10.5 rules the Frobenius norm out of the condition number.

7. Let $A\in\mathbb{R}^{n\times n}$ have singular values $\sigma_1\geq\cdots\geq\sigma_n$.
Prove that $|\det A|=\prod_{i=1}^n\sigma_i$ from Theorem 10.4, using clause 5 of Lemma 5.19 to dispose of the two orthogonal factors.
Deduce the bound $|\det A|\leq\|A\|_2^{\,n}$, and show that it is an equality exactly when $A$ is a scalar multiple of an orthogonal matrix.

    > *Recall:* the determinant of a product is the product of the determinants.

8. Call $H$ a **positive square root** of a symmetric matrix $M$ when $H$ is positive semidefinite in the sense of Chapter 9 and satisfies $H^2=M$.
Diagonalize $M$ orthogonally by Theorem 10.1 and take square roots along the diagonal to build one whenever $M$ has no negative eigenvalue.
Prove there is no second: any such $H$ satisfies $HM=H^3=MH$, so $H$ carries each eigenspace of $M$ into itself, and there $H^2=\lambda I$ leaves nothing free but a sign, which positivity spends.
Now let $A$ be nonsingular, let $H$ be the positive square root of $AA^T$, and show that $Q=H^{-1}A$ is the one and only orthogonal matrix with $A=HQ$.

9. Let $A$ be square.
Prove $\sigma_1(A+A^T)\leq2\sigma_1(A)$ and $\sigma_1(A-A^T)\leq2\sigma_1(A)$ from the triangle inequality for vectors together with the identity $\sigma_1(A^T)=\sigma_1(A)$ of Section 10.5, the book offering no triangle inequality for matrices.
Show that equality holds in the first whenever $A$ has a real eigenvalue of modulus $\sigma_1$, and in the second whenever $A$ carries some orthonormal pair $\mathbf{x},\mathbf{y}$ to $\sigma_1\mathbf{y}$ and $-\sigma_1\mathbf{x}$, and exhibit a matrix meeting one condition and failing the other.
Symmetry is sufficient for the first and skewness for the second; produce a matrix that is neither and attains equality in one of them anyway, for which size three will be needed.

10. Let $A$ and $B$ be nonsingular $n\times n$ matrices.
Prove that $\operatorname{cond}(AB)$ is at most $\operatorname{cond}(A)\operatorname{cond}(B)$, using the two facts of Section 10.5: that $\operatorname{cond}$ is the spectral norm of a matrix times that of its inverse, and that the spectral norm is submultiplicative.
Show that equality holds when the right singular vectors of $A$ are the left singular vectors of $B$ in matching order.
Now read $\operatorname{cond}$ of a rectangular matrix as $\sigma_1/\sigma_p$, with $p=\min\{m,n\}$, and break the inequality.
Exhibit a $2\times3$ matrix and a $3\times2$ matrix, each of condition number $1$ in that sense, whose product is singular, and name the step of your proof that squareness was holding up.

11. Let $A$ be symmetric with every eigenvalue positive, and prove that $\sigma_i=\lambda_i$ for every $i$.
Show that the positivity is carrying weight rather than decorating the hypothesis, by exhibiting a symmetric matrix whose singular values are not even the $|\lambda_i|$ taken in the order the eigenvalues arrive in.
Then prove the converse that survives over $\mathbb{R}$: if every eigenvalue of a square real $A$ is real and $\sigma_i=|\lambda_i|$ for every $i$ once both lists are sorted downward, then $A$ is symmetric.
Compare $\operatorname{tr}(A^TA)$, which Exercise 6 equates with $\sum_i\sigma_i^2$, against $\operatorname{tr}(A^2)=\sum_i\lambda_i^2$, and expand $\|A-A^T\|_F^2$.
The reality of the spectrum cannot be dropped: $\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ has $|\lambda_i|=\sigma_i=1$ and is not symmetric, and your proof must say where it stops.

12. Let $A$ be $m\times n$ with $m>n$ and full column rank.
Read $\operatorname{cond}(A)$ as $\sigma_1/\sigma_n$, the extension of Exercise 10, which costs nothing here since Definition 10.2 gives such an $A$ exactly $n$ singular values.
Prove $\operatorname{cond}(A^TA)=\operatorname{cond}(A)^2$, noting that $A^TA$ is square and nonsingular so the unamended definition applies to it.
Chapter 6 solves least squares by forming $A^TA$ (Theorem 6.17), while Section 10.4 reaches the same $\hat{\mathbf{x}}$ as $A^\dagger\mathbf{b}$ without ever forming it.
Double precision carries about sixteen decimal digits and a solve may lose roughly $\log_{10}\operatorname{cond}$ of them: say how many each route can hope to keep at $\operatorname{cond}(A)=10^8$.

13. Call a square real matrix $A$ **normal** when $AA^T=A^TA$, and let $A=HQ$ be the decomposition of Exercise 8 for nonsingular $A$.
Prove that $A$ is normal exactly when its two factors commute, passing from $QH^2Q^T=H^2$ to $QHQ^T=H$ by the uniqueness of the positive square root and by nothing else.
Deduce that a normal $A$ equals $QH$ as well as $HQ$, so that the orthogonal factor may be applied before or after the stretching indifferently.
Then check that a plane rotation is normal but has no real eigenvector.

14. Section 10.4 settles clause 5 of Theorem 6.16 by printing $A^{-1}=V\Sigma^{-1}U^T$ for nonsingular $A$.
Weigh what that formula costs: Chapter 1 puts $LU$ factorization at about $\tfrac{2}{3}n^3$ operations with each further right-hand side $O(n^2)$, while an SVD is also cubic but with a far larger constant.
Decide which you would compute to solve $A\mathbf{x}=\mathbf{b}$, and why a thousand right-hand sides sharing the same $A$ do not change the answer.
Then say what the SVD tells you about $A$ that elimination does not, and why that, and not speed, is the reason to compute one.

15. Section 10.5 remarks that small singular values mark directions that are nearly dependent, and Lemma 10.7 at $k=n$ makes the remark exact: for square $A$, $\sigma_n$ is the spectral-norm distance from $A$ to the nearest singular matrix.
Explain why this makes $\sigma_n/\sigma_1$, and not $\det A$, the honest report of how close a matrix stands to singularity.
Exhibit an $n\times n$ matrix whose determinant is smaller than $10^{-100}$ and whose columns are exactly perpendicular, and a $2\times2$ matrix of determinant $1$ sitting within $10^{-8}$ of a singular matrix.
Say what rescaling $A$ by a scalar does to $\det A$, what it does to $\sigma_n/\sigma_1$, and why that settles the matter.

16. Chapter 3 built $\operatorname{coim} T$ and $\operatorname{coker} T$ as quotients: spaces of equivalence classes, with no preferred representative in any class.
Section 10.6 identifies each with a subspace, $(\operatorname{ker} T)^\perp$ and $(\operatorname{im} T)^\perp$, and credits the inner product with the work.
Name the map that does the identifying, say why the inner product is what makes it well defined, and say what is lost if some other complement of $\operatorname{ker} T$ is chosen instead.
Then explain why changing the inner product on $V$ changes the singular values of $T$ while leaving $\operatorname{ker} T$ and $\operatorname{im} T$ exactly where they were.

17. Three sensors, in the model of the Emanation *Sensor Networks & The Geometry of Measurement*, report $M_{ij}=g_js_i+b_j$  — gain $g_j$, bias $b_j$, signal $s_i$  — at four successive times.
The array returns

$$
M = \begin{bmatrix}
    7 & 5 & 23 \\
    19 & 23 & 59 \\
    23 & 29 & 71 \\
    35 & 47 & 107
    \end{bmatrix} .
$$

Subtract from each column its own mean and exhibit what is left as $\sigma_1\mathbf{u}_1\mathbf{v}_1^T$ for unit vectors $\mathbf{u}_1\in\mathbb{R}^4$ and $\mathbf{v}_1\in\mathbb{R}^3$.
Read the three gains off $\mathbf{v}_1$ up to one common factor, and then show that no data of this form can do better: replacing $(s_i,g_j,b_j)$ by $(s_i/c,\,cg_j,\,b_j)$ for any $c\neq0$ changes no entry of $M$.

18. Two bars pinned to a wall pull along $\mathbf{d}_1=\tfrac{1}{5}(3,4)^T$ and $\mathbf{d}_2=\tfrac{1}{5}(4,3)^T$; a load $\mathbf{f}$ is carried as $t_1\mathbf{d}_1+t_2\mathbf{d}_2=\mathbf{f}$, with $t_j$ the tension in bar $j$.
Compute the singular values of $A=[\mathbf{d}_1\ \mathbf{d}_2]$ and $\operatorname{cond}(A)$, then solve for the tensions under the loads $\mathbf{f}=(1,1)^T$ and $\mathbf{f}=(-1,1)^T$.
The two loads have the same size and the tensions do not: match each load to a left singular vector of $A$, and report the ratio of the two costs.
Then say what becomes of $\sigma_2$, and of the joint, as the two bars are brought toward parallel.

19. The position and velocity errors of a digital control loop, $\mathbf{x}_k=(p_k,v_k)^T$, evolve by $\mathbf{x}_{k+1}=A\mathbf{x}_k$ with $A=\begin{bmatrix}4/5 & 6/5\\0 & 4/5\end{bmatrix}$.
Compute the eigenvalues and the singular values of $A$, and verify by induction that $A^k=(4/5)^k\begin{bmatrix}1 & 3k/2\\0 & 1\end{bmatrix}$, so that every error does eventually die.
Find the unit initial error that grows most in a single sample and the factor by which it grows.
Say which of the two spectra bounds the error at every step and which governs only the limit.

20. (Challenge.) Let $A=U\Sigma V^T$ have rank $r$, fix $k<r$, and let $A_k$ be the truncation of Section 10.4, so that $A-A_k=U\Sigma'V^T$ with $\Sigma'$ the rectangular diagonal matrix carrying $\sigma_{k+1},\sigma_{k+2},\ldots$ and nothing else.
Prove that $\|QAP\|_F=\|A\|_F$ for all orthogonal $Q$ and $P$ of the admissible sizes, by applying clause 3 of Lemma 5.19 to each column in turn and then to each row.
Conclude, as Exercise 6 did for $A$ itself, that $\|A-A_k\|_F^2=\sum_{i>k}\sigma_i^2$, and show that the spectral norm is orthogonally invariant as well, so that $\|A-A_k\|_2=\sigma_{k+1}$.
Say which of the two errors sees every discarded singular value and which sees only the largest.

---


# Chapter 11. Principal Components & Low-Rank Structure

*"and weigh the massy cubes, then fix them in their awful stations"*

**Deep patterns lie hidden** within high-dimensional data.
The challenge is not gathering it — modern science and engineering generate observations in abundance — but extracting structure from measurements spanning hundreds of dimensions.
Within such spaces, important features concentrate along a few key directions, like mineral deposits concentrated by geological processes.

> *Example:* A single human genome contains roughly 20,000 genes whose expression levels vary across conditions; the variation lives in a 20,000-dimensional space.

Principal Component Analysis (PCA) provides the mathematical tools for uncovering these essential patterns.
Through careful study of how measurements vary and correlate, PCA reveals natural coordinates aligned with the data's intrinsic structure.
These coordinates — ordered by their importance in capturing variation — enable both dimension reduction and pattern discovery.

> *Foreshadowing:* The connection between PCA and neural networks (Chapter 13) runs deep: both seek to transform high-dimensional data into more meaningful representations.

The same mathematics reaches further than coordinates.
To retain a few components is to approximate the data matrix by one of lower rank, and the theory of that approximation — what is optimal, what is possible, what survives missing entries or corrupted measurements — belongs to this chapter as well.
A ratings table with most of its entries unobserved, a sensor array with failed channels, a video feed marred by glitches: each conceals a low-rank truth beneath an unreliable surface, and each yields to the tools built here.

The foundations for this analysis emerged from our work with singular values in Chapter 10.
There we saw how any linear transformation admits decomposition into orthogonal stretching along principal axes.
PCA applies this geometric insight to data matrices, where rows represent observations and columns represent measured variables.
The singular vectors of such matrices reveal natural coordinates for understanding variation, while singular values measure the strength of pattern in each direction.

> *Historical Note:* PCA has roots in statistical analysis dating to Pearson (1901), though the SVD is more modern.

Though the data may seem chaotic at first glance, a few directions often carry nearly all of it; our task is both the theory of that simplicity and the tools to reach it.

## 11.1 Covariance & Correlation

The story of variance begins with rotation.
A solid body spinning about its center of mass experiences rotational resistance determined not by total mass, but by how that mass is distributed in space.
The familiar scalar moment of inertia $I = \int r^2\,dm$ measures this resistance about a single axis, but a complete description requires the full **inertia tensor**:

$$
\mathcal{I} = [\mathcal{I}_{ij}]
    \quad : \quad
    \mathcal{I}_{ij} = \int (r^2\delta_{ij} - x_ix_j)\,dm
$$

> *Definition:* the Kronecker delta $\delta_{ij}$ evaluates to $1$ if $i=j$ and $0$ otherwise.

This mechanical perspective — of mass distributed about a center and its resistance to different rotations — provides surprisingly deep insight into the statistical structures we now develop.

> *Think:* Just as a solid's resistance to rotation depends on mass distribution about its axes, a dataset's statistical structure depends on how measurements distribute about their means in different directions.

Consider first a single random variable $Z$.
Its **mean** or **expectation** $\mu=\mathbb{E}(Z)$ acts as a center of mass, while its **variance** $\mathbb{V}(Z)=\mathbb{E}((Z-\mu)^2)$ measures spread about this center — precisely analogous to the scalar moment of inertia of a mass distribution about its centroid.
The **standard deviation** $\sigma=\sqrt{\mathbb{V}}$, like the radius of gyration in mechanics, provides a characteristic length scale of this spread.

> *Nota bene:* Instead of a $1/n$ in front of the variance, one often sees a $1/(n-1)$, especially in the context of statistics.
> This reflects the loss of one degree of freedom in estimating the mean from a sampling.
> For purposes of doing data science and dimension reduction, $1/n$ is the more appropriate scaling and is what we shall use throughout.

In most instances, data is discrete rather than continuous, and we can represent $Z$ as a vector $\mathbb{Z}=(z_1,\ldots,z_n)^T$.
From this, we have basic statistical measures:

$$
\mathbb{E}(Z) = \frac{1}{n}\sum_{i=1}^n z_i \quad\text{and}\quad
    \mathbb{V}(Z) = \frac{1}{n}\sum_{i=1}^n (z_i-\mathbb{E}(Z))^2
$$

In data science and statistics, one typically *centers* the data, transforming $Z$ to $\hat{Z}=Z-\mathbb{E}(Z)$ with mean zero.
This, then, leads to a geometric interpretation of variance as $\mathbb{V}(Z)=\frac{1}{n}\hat{Z}^T\hat{Z}$ with the standard deviation interpreted as dimension-scale length:

$$
\sigma = \sqrt{\mathbb{V}}
    = \frac{1}{\sqrt{n}}\sqrt{\hat{Z}^T\hat{Z}}
    = \frac{1}{\sqrt{n}}\left\|{\hat{Z}}\right\| .
$$

From this one identification the geometry of data unfolds.

What happens with two random variables?
Covariance and correlation are the key measures.
Given random variables $Y$ and $Z$, their **covariance**

$$
\begin{aligned}
\operatorname{cov}(Y,Z) &= \mathbb{E}(\hat{Y}\hat{Z}) = \mathbb{E}((Y-\mathbb{E}(Y))(Z-\mathbb{E}(Z)))  \\
    &= \frac{1}{n} \,\hat{Y}\cdot\hat{Z}
\end{aligned}
$$

measures their tendency to vary together.
Like the off-diagonal terms of the inertia matrix, covariance captures coupling between different directions of variation.
Positive covariance indicates that large values of $Y$ tend to occur with large values of $Z$, while negative covariance suggests opposition — when one variable rises above its mean, the other tends to fall below.

That this is a dot product (scaled by dimension) should act as a balm to anyone who has suffered through a traditional statistics course.
Filled with the geometric imagination that the dot product inspires, one may guess what is to come.

To determine the degree of alignment (or misalignment) between two data vectors, one defines a **correlation** to be a rescaling of the covariance to lie between $-1$ and $+1$ with a correlation of zero connoting the absence of any linear relationship — a strictly weaker condition than independence.
As a formula, correlation becomes a familiar friend:

$$
\operatorname{corr}(Y,Z) = \frac{\operatorname{cov}(Y, Z)}{\sigma(Y)\,\sigma(Z)} = \frac{\hat{Y}\cdot\hat{Z}}{\|\hat{Y}\|\|\hat{Z}\|} = \cos\theta(\hat{Y},\hat{Z}) .
$$

> *Truth:* Correlation is not causation; but it is cosine similarity.

It is the cosine of the angle between the two centered data vectors.

## 11.2 Matrices & Data

A single vector of data corresponds to one point in a point cloud.
How then shall we proceed to work with the entire data set?
The future is already visible: a collection of data points becomes a collection of vectors, assembled into a data matrix.

For an (arbitrarily) ordered collection of $d$ variables $Z_1,\ldots,Z_d$, center them each to $\hat{Z}_i$ and arrange them into a centered **data matrix** $\mathcal{X}\in\mathbb{R}^{n\times d}$ where:

- Each row represents one observation;

- Each column corresponds to one variable;

- Entry $x_{ij}$ is the $j$th measurement from observation $i$.

For instance, consider daily temperature measurements at three weather stations over one year:

$$
\mathcal{X} = \begin{bmatrix}
    72 & 70 & 68 \\
    75 & 74 & 71 \\
    65 & 63 & 62 \\
    \vdots & \vdots & \vdots
\end{bmatrix}
$$

After centering by subtracting column means (analogous to shifting to center of mass coordinates in mechanics), the **covariance matrix** becomes:

$$
[C] = \frac{1}{n}\mathcal{X}^T\mathcal{X}
    = \begin{bmatrix}
    25.3 & 23.1 & 20.4 \\
    23.1 & 24.7 & 19.8 \\
    20.4 & 19.8 & 22.9
    \end{bmatrix} ,
$$

where we assume $\mathcal{X}$ has already been centered.

The diagonal entries show each station's temperature variance — station 1 shows slightly more variability than the others.
The large positive off-diagonal terms indicate strong correlation between stations, as expected for nearby locations experiencing similar weather patterns.
Yet the correlation is not perfect, with station pairs (1,2) showing stronger relationship than pairs involving station 3, suggesting it may be geographically more distant.

This covariance matrix is symmetric positive semidefinite by construction.
Its diagonal entries are the individual variances, while off-diagonal terms measure pairwise relationships.

Just as the inertia matrix's eigenvalues measure resistance to rotation about principal axes, the covariance matrix's eigenstructure reveals fundamental patterns of variation in our data.

> *Caution:* in this section alone, $\sigma_i$ denotes the standard deviation of the $i$th variable.
> Everywhere else in this chapter $\sigma_i$ is the $i$th singular value; the two agree only up to the factor $\sqrt n$ of Section 11.1, and only for a single centered variable.

To better understand these patterns independent of scale, we sometimes normalize through the **correlation matrix** $[R]=[R_{ij}]$ where

$$
R_{ij} = \frac{C_{ij}}{\sigma_i\sigma_j} = \frac{\operatorname{cov}(Z_i,Z_j)}{\sqrt{\mathbb{V}(Z_i)\mathbb{V}(Z_j)}}
$$

This scales every entry into the interval from $-1$ to $1$, measuring purely the strength and the direction of a linear relationship.
For our temperature data, we first extract standard deviations from the diagonal entries of the covariance matrix:

$$
\sigma_1 = \sqrt{25.3} \approx 5.03^\circ, \quad
    \sigma_2 = \sqrt{24.7} \approx 4.97^\circ, \quad
    \sigma_3 = \sqrt{22.9} \approx 4.79^\circ
$$

These measure the typical variation at each station.
The complete correlation matrix then becomes:

$$
[R] = \begin{bmatrix}
    1.000 & 0.924 & 0.848 \\
    0.924 & 1.000 & 0.833 \\
    0.848 & 0.833 & 1.000
    \end{bmatrix}
$$

The covariance and correlation matrices transform abstract statistical relationships into concrete geometric objects.
Their eigenvectors identify principal axes of variation, while their eigenvalues measure the strength of variation along these axes.
Even our simple temperature example suggests how datasets may harbor hidden simplicity: though we measured three variables, the strong correlations hint at fewer degrees of freedom than variables.

## 11.3 Principal Components

The covariance matrix captures how our data varies along different directions in measurement space.
Yet these directions, aligned with our original variables, may obscure simpler underlying patterns.
Just as the projection operators of Chapter 6 revealed optimal approximating subspaces, we now seek coordinates aligned with the inherent structure of our data rather than arbitrary measurement choices.

Consider a centered data matrix $\mathcal{X}\in\mathbb{R}^{n\times d}$, where each row represents one observation of $d$ variables, and each column has zero mean.
The singular value decomposition studied in Chapter 10 provides exactly the transformation we seek:

**Definition 11.1 (Principal Components).** Given a centered data matrix $\mathcal{X}$, its **principal components** are the right singular vectors $\mathbf{v}_1,\ldots,\mathbf{v}_d$ from the SVD $\mathcal{X}=U\Sigma V^T$, ordered by decreasing singular value.
Each component $\mathbf{v}_k$ represents a direction in the original variable space that captures maximal remaining variation after accounting for previous components.

These principal components transform our original variables into new features that capture the data's variation structure:

**Definition 11.2 (PC Scores).** Given a principal component $\mathbf{v}_k$, the corresponding **principal component score** for observation $\mathbf{x}\in\mathbb{R}^d$ is its projection $z_k=\mathbf{x}^T\mathbf{v}_k$ onto that direction.
The scores of all observations along $\mathbf{v}_k$ form the $k$th **score vector** $\mathbf{z}_k=\mathcal{X}\mathbf{v}_k$.

Just as the orthogonal projections of Chapter 6 decomposed vectors into optimal approximating components, these score vectors decompose our data into orthogonal features of decreasing importance.
The singular values price the variation directly: if $\sigma_k$ is the $k$th singular value of $\mathcal{X}$, then $\lambda_k=\sigma_k^2/n$ gives the variance of scores along the $k$th principal component.
These variances decrease as we move through components, reflecting how each successive direction captures maximal remaining variation in the data.

**Example 11.3 (Gene Expression Data).** Consider genetic expression measurements across thousands of genes in different cell types.
Each row of our data matrix represents a cell, while columns record expression levels of different genes:

$$
\mathcal{X} = \begin{bmatrix}
    \leftarrow & \text{cell 1} & \rightarrow \\
    \leftarrow & \text{cell 2} & \rightarrow \\
    & \vdots & \\
    \leftarrow & \text{cell n} & \rightarrow
    \end{bmatrix}
    \begin{array}{l}
    \text{ gene 1} \\
    \text{ gene 2} \\
    \vdots \\
    \text{ gene d}
    \end{array}
$$

Though each cell's state lives in a space of dimension $d\approx 20,000$, biological constraints often restrict variation to a much lower-dimensional manifold.
Principal component analysis reveals these constraints through directions $\mathbf{v}_k$ that often correspond to fundamental regulatory programs or cell state transitions.

> *Foreshadowing:* The dimension reduction achieved through PCA previews how neural networks (Chapter 13) learn to represent high-dimensional data through lower-dimensional features.

Projecting onto the first two principal components produces a two-dimensional visualization:

$$
\begin{bmatrix}
    z_{11} & z_{12} \\
    z_{21} & z_{22} \\
    \vdots & \vdots \\
    z_{n1} & z_{n2}
    \end{bmatrix} = \mathcal{X}[\mathbf{v}_1\;\mathbf{v}_2]
$$

The resulting scatter plot of points $(z_{i1},z_{i2})$ often reveals clusters of similar cell types or gradients of cellular differentiation — patterns invisible in the original high-dimensional space.

> *Recall:* This sequence of directions generalizes the orthogonal bases of Chapter 4, now optimized to capture variation in data rather than arbitrary coordinate choices.

The fraction of total variance captured by the first $k$ components provides a measure of how well they summarize our data:

$$
r_k = \frac{\sum_{i=1}^k \lambda_i}{\sum_{i=1}^d \lambda_i} = \frac{\sum_{i=1}^k \sigma_i^2}{\sum_{i=1}^d \sigma_i^2}
$$

A ratio near $1$ at small $k$ means a low-dimensional representation that captures most of the variation in the data.
In the language of the Fundamental Theorem of Linear Algebra (Theorem 3.25), retaining $k$ components is a choice of coimage.
The truncation

$$
\mathbf{x}\longmapsto(\mathbf{v}_1^T\mathbf{x},\ldots,\mathbf{v}_k^T\mathbf{x})^T
$$

quotients feature space by the discarded directions, and the scores are coordinates on the quotient that survives.

In practice, the choice of scaling decides what patterns PCA discovers.
Two standard approaches emerge:

1. **Covariance PCA**: Use centered data directly, preserving relative scales

2. **Correlation PCA**: Standardize each variable to unit variance first

The first emphasizes directions of large absolute variation; the second focuses on patterns of correlation regardless of scale.
Section 11.5 will explore these choices and their implications in detail.

Principal component analysis thus provides a systematic way to replace arbitrary measurement coordinates with natural axes aligned to variation in our data.
Like the optimal projections of Chapter 6 and the singular vectors of Chapter 10, these directions are not chosen but forced — extremal solutions of an optimization problem.

## 11.4 Optimality Properties

Principal components provide more than just convenient coordinates for data analysis — they are forced by an optimization.
Like the orthogonal projections of Chapter 6, which minimized approximation error in geometric spaces, principal components minimize error in representing high-dimensional data through lower-dimensional summaries.

Consider first the problem of finding a single direction that best captures variation in our data.
Given centered observations $\{\mathbf{x}_1,\ldots,\mathbf{x}_n\}$, we seek a unit vector $\mathbf{v}$ maximizing the variance of projections:

$$
\text{maximize} \quad \frac{1}{n}\sum_{i=1}^n (\mathbf{x}_i^T\mathbf{v})^2
    \quad\text{subject to}\quad \|\mathbf{v}\|=1
$$

The geometry is plain: we seek the direction of greatest spread.
Writing $\mathcal{X}$ for our centered data matrix, this objective becomes:

$$
\frac{1}{n}\mathbf{v}^T\mathcal{X}^T\mathcal{X}\mathbf{v} = \mathbf{v}^T[C]\mathbf{v}
$$

subject to $\mathbf{v}^T\mathbf{v}=1$.

> *Think:* The optimization balances two competing goals: capturing as much variation as possible while maintaining orthogonality between components.

**Theorem 11.4 (Principal Component Optimality).** The first principal component $\mathbf{v}_1$ maximizes $\mathbf{v}^T[C]\mathbf{v}$ subject to $\|\mathbf{v}\|=1$.
Each subsequent component $\mathbf{v}_k$ maximizes this same objective subject to orthogonality with all previous components.

*Proof.* Recall from Chapter 10 that the right singular vectors of $\mathcal{X}$ are precisely the orthonormal eigenvectors of $\mathcal{X}^T\mathcal{X}$, hence of $[C]=\frac1n\mathcal{X}^T\mathcal{X}$, with $[C]\mathbf{v}_k=\lambda_k\mathbf{v}_k$ for $\lambda_k=\sigma_k^2/n$.
The first claim is then Lemma 9.22 of Chapter 9: the maximum of $\mathbf{v}^T[C]\mathbf{v}$ over the unit sphere is the largest eigenvalue of $[C]$, attained at a corresponding unit eigenvector.
For the remaining components, let $W_k=\operatorname{span}\{\mathbf{v}_1,\ldots,\mathbf{v}_{k-1}\}^\perp$.
Since $[C]$ is symmetric and each $\mathbf{v}_i$ is an eigenvector, $[C]$ carries $W_k$ into itself, and its restriction to $W_k$ is again symmetric with eigenvalues $\lambda_k\geq\cdots\geq\lambda_d$ and eigenvectors $\mathbf{v}_k,\ldots,\mathbf{v}_d$.
Applying the same lemma to that restriction gives the maximum $\lambda_k$, attained at $\mathbf{v}_k$. ∎

> *Caution:* When an eigenvalue repeats, the maximizer is not unique — any unit vector of the corresponding eigenspace attains it.
> The theorem asserts that $\mathbf{v}_k$ maximizes, never that it alone does.

Beyond variance maximization, principal components possess several equivalent optimality properties:

1. They minimize mean squared reconstruction error for $k$-dimensional representations

2. They minimize the total shrinkage of squared pairwise distances, in the sense of the classical multidimensional scaling of Chapter 9

3. Among all $k$-dimensional projections of a Gaussian population they maximize the entropy $\tfrac12\log\det(V^T[C] V)$ of the projected variables

> *Nota bene:* the first two are the same statement in different dress, since reconstruction error and distance shrinkage differ by a constant depending only on $\mathcal{X}$.
> The third is a fact about Gaussians, and holds only for them.

> *Example:* In financial portfolio analysis, PCA often reveals risk factors ordered by their contribution to total market variance — a decomposition crucial for risk management.

The reconstruction error perspective proves particularly illuminating.
Given observations $\{\mathbf{x}_i\}$, consider approximating each through:

$$
\hat{\mathbf{x}}_i = \sum_{j=1}^k z_{ij}\mathbf{v}_j
$$

where $z_{ij}$ are scores and $\mathbf{v}_j$ are unit vectors.
The principal components minimize:

$$
\frac{1}{n}\sum_{i=1}^n \|\mathbf{x}_i - \hat{\mathbf{x}}_i\|^2
$$

over all choices of $k$ orthonormal vectors $\{\mathbf{v}_j\}$.
This optimality connects directly to the projection operators of Chapter 6; it is also, and more consequentially, a statement about matrices.
Assemble the approximations $\hat{\mathbf{x}}_i$ as the rows of a matrix $\hat{\mathcal{X}}$, so that summing squared errors over observations builds a Frobenius norm:

$$
\frac{1}{n}\sum_{i=1}^n \left\|\mathbf{x}_i - \hat{\mathbf{x}}_i\right\|^2
    = \frac{1}{n}\left\|\mathcal{X} - \hat{\mathcal{X}}\right\|_F^2 .
$$

Each $\hat{\mathbf{x}}_i$ is a combination of $k$ fixed vectors, so $\hat{\mathcal{X}}$ has rank at most $k$; conversely, any matrix of rank at most $k$ arises this way.
The claim that principal components minimize mean squared reconstruction error is therefore the claim that, among all matrices of rank at most $k$, the truncation of the SVD lies nearest to $\mathcal{X}$.
Statistics has quietly posed a question in pure matrix approximation, and the answer deserves to be stated in full generality.

**Definition 11.5 (Rank-$k$ Approximation).** For a matrix $A\in\mathbb{R}^{m\times n}$ and an integer $k\leq\operatorname{rank}(A)$, a {rank-$k$ approximation} to $A$ is any matrix $B\in\mathbb{R}^{m\times n}$ satisfying $\operatorname{rank}(B)\leq k$, with the error of approximation measured in the spectral or Frobenius norms of Definition 10.5.

The SVD proposes an obvious candidate.
Keeping only the $k$ largest singular values yields the **truncated SVD**

$$
A_k = \sum_{i=1}^k \sigma_i\mathbf{u}_i\mathbf{v}_i^T ,
$$

a matrix of rank exactly $k$.
Note how the discarded remainder $A-A_k=\sum_{i>k}\sigma_i\mathbf{u}_i\mathbf{v}_i^T$ arrives wearing its own singular value decomposition, so that its norms can be read directly off the spectrum — as Exercise 20 of Chapter 10 asks one to verify.
Each truncated singular value contributes exactly its square to the total squared error.
That the obvious candidate is the best possible one is the content of a theorem discovered, in one form or another, every few decades since 1907.

> *Historical Note:* Erhard Schmidt proved this optimality for integral operators in 1907; Eckart & Young rediscovered it for matrices in 1936; Mirsky extended it to every unitarily invariant norm in 1960.
> The theorem has been rediscovered roughly as often as data has outgrown its storage.

**Theorem 11.6 (Eckart-Young-Mirsky).** Let $A\in\mathbb{R}^{m\times n}$ have singular values $\sigma_1\geq\cdots\geq\sigma_r>0$ and let $k<r$.
Then for every matrix $B\in\mathbb{R}^{m\times n}$ of rank at most $k$,

$$
\|A-B\|_2 \geq \sigma_{k+1} = \|A-A_k\|_2
    \quad\text{and}\quad
    \|A-B\|_F^2 \geq \sum_{i=k+1}^{r}\sigma_i^2 = \|A-A_k\|_F^2 .
$$

The truncated SVD is an optimal rank-$k$ approximation in both norms.

Consider how much the quantifier concedes: $B$ ranges over every matrix of rank at most $k$  — every projection, every factorization, every clever encoding a rival method might devise — and none of them beats simple truncation.

*Proof.* Let $B$ have rank at most $k$.
By the Fundamental Theorem (Theorem 3.25), $\dim\operatorname{ker}(B)\geq n-k$, while the subspace $W=\operatorname{span}\{\mathbf{v}_1,\ldots,\mathbf{v}_{k+1}\}$ has dimension $k+1$.
These dimensions sum to more than $n$, so by Exercise 19 of Chapter 2 the two subspaces share a unit vector $\mathbf{x}\in\operatorname{ker}(B)\cap W$.
Writing $\mathbf{x}=\sum_{i=1}^{k+1}c_i\mathbf{v}_i$ with $\sum_i c_i^2=1$, one computes $A\mathbf{x}=\sum_{i=1}^{k+1}\sigma_i c_i\mathbf{u}_i$ and, since $B\mathbf{x}=\mathbf{0}$,

$$
\|A-B\|_2^2 \geq \left\|(A-B)\mathbf{x}\right\|^2 = \left\|A\mathbf{x}\right\|^2
    = \sum_{i=1}^{k+1}\sigma_i^2c_i^2 \geq \sigma_{k+1}^2 .
$$

This proves the spectral claim; it is also, read from the other side, the statement that $\sigma_{k+1}$ measures the distance from $A$ to the set of matrices of rank at most $k$ — which is Lemma 10.7 of Chapter 10.

> *Recall:* Lemma 10.7 was proved in Chapter 10 to settle the behavior of singular values under composition.
> It returns here as the whole of the spectral case, and, iterated, as the whole of the Frobenius one.

The Frobenius claim follows by applying it repeatedly.
Fix $B$ of rank at most $k$, and for each $i\geq 1$ let $C_{i-1}$ be a best rank-$(i-1)$ approximation to $A-B$, so that $\|(A-B)-C_{i-1}\|_2=\sigma_i(A-B)$ by Lemma 10.7.
The sum $B+C_{i-1}$ has rank at most $k+i-1$, whence, invoking that lemma once more,

$$
\sigma_{k+i}(A) \leq \left\|A-(B+C_{i-1})\right\|_2 = \left\|(A-B)-C_{i-1}\right\|_2 = \sigma_i(A-B) .
$$

Squaring and summing over $1\leq i\leq p=\min\{m,n\}$, with the convention that $\sigma_j(A)=0$ for $j>r$, completes the argument:

$$
\|A-B\|_F^2 = \sum_{i=1}^{p}\sigma_i(A-B)^2 \geq \sum_{i=1}^{p}\sigma_{k+i}(A)^2 = \sum_{j>k}\sigma_j(A)^2 = \|A-A_k\|_F^2 .
$$

 ∎

> *BONUS!* The inequality $\sigma_{k+i}(A)\leq\sigma_i(A-B)$ proved en route is a special case of Weyl's 1912 inequalities for singular values of sums — obtained here from the spectral statement alone, iterated.

Mirsky's refinement extends the same optimality to every norm that depends only on singular values, including the nuclear norm $\|A\|_*=\sum_i\sigma_i$, whose surprising utility awaits Section 11.6.
One theorem, stated once, now underwrites the reconstruction claims of this section, the truncation decisions of Section 11.5, and the recovery guarantees to come.

**Example 11.7 (Image Compression).** A grayscale photograph stored as a $1024\times 1024$ matrix $A$ of pixel intensities is, formally, a matrix of rank near $1024$; visually, it is nothing of the sort.
Spatial correlation — skies, walls, and shadows varying smoothly across neighboring pixels — concentrates the singular value spectrum, and a rank-$50$ truncation typically preserves every feature the eye consults.
The storage arithmetic is persuasive: $A_{50}$ requires $50$ singular values together with $50$ left and $50$ right singular vectors, or $50(1024+1024+1)=102{,}450$ numbers in place of the original $1{,}048{,}576$  — better than tenfold compression, with total squared error $\sum_{i>50}\sigma_i^2$ read directly off the discarded spectrum.
The fraction of variance retained is precisely the ratio $r_k$ of Section 11.3, now doing double duty as a measure of image fidelity.

The arithmetic generalizes: a rank-$k$ truncation of an $n\times d$ matrix costs $k(n+d+1)$ numbers in place of $nd$.

The truncation admits one further reading, in the language of Chapter 6.
Reconstruction from $k$ retained components sends each observation $\mathbf{x}$ to $V_kV_k^T\mathbf{x}$, where $V_k=[\mathbf{v}_1\cdots\mathbf{v}_k]$; in matrix form, $\hat{\mathcal{X}}_k=\mathcal{X} V_kV_k^T$.
This operator is no stranger: $V_kV_k^T=\mathcal{X}_k^\dagger\mathcal{X}_k$, the pseudoinverse of the truncation composed with the truncation itself, which Chapter 10 identified as the orthogonal projection onto $\operatorname{row}(\mathcal{X}_k)$.
Section 11.3 called the retention of $k$ components a choice of coimage; that choice has now become an operator.
*Reconstruction is orthogonal projection onto the chosen coimage.*
What PCA discards, it discards orthogonally: the residual $\mathcal{X}-\hat{\mathcal{X}}_k$ lives entirely in the discarded directions, and its Frobenius norm is exactly the reconstruction error that Theorem 11.6 certifies as minimal.
The two norms of Definition 10.5 measure different failures, and Theorem 11.6 certifies the same truncation for both.
The Frobenius error $\|\mathcal{X}-\mathcal{X}_k\|_F=\sqrt{\sum_{i>k}\sigma_i^2}$ aggregates typical reconstruction error across all observations, while the spectral error $\|\mathcal{X}-\mathcal{X}_k\|_2=\sigma_{k+1}$ bounds the worst case — the crucial quantity when reconstructions feed a control system in which errors compound.
One truncation is optimal; which error one is willing to pay decides how deep to cut.

> *Foreshadowing:* Chapter 13 will train a linear autoencoder by gradient descent and find, at the optimum, precisely the projection $V_kV_k^T$  — PCA, relearned.

Optimality, however, is always relative to the data as presented.
The theorem certifies that no rank-$k$ matrix lies closer to $\mathcal{X}$; it does not certify that $\mathcal{X}$, as measured, deserved the devotion.
Variables arrive in incommensurable units and incompatible scales, contaminated by outliers, and a theorem indifferent to units will happily spend its entire rank on whichever column shouts loudest.
The data must first be made worth approximating — units reconciled, outliers arraigned — and only then can one ask how large $k$ must be.

## 11.5 Judgment

Real data rarely arrives in the pristine form assumed by our theoretical development.
Consider monitoring an automated manufacturing process through five sensors:

$$
\mathcal{X} = \begin{bmatrix}
    82.3 & 1205 & 4.2 & 7.1 & 156 \\
    85.1 & 1148 & 4.1 & 7.2 & 158 \\
    79.8 & 1262 & 4.3 & 6.8 & 155 \\
    \vdots & \vdots & \vdots & \vdots & \vdots
\end{bmatrix}
\quad : \quad
\textrm{cols } \Rightarrow
\begin{array}{l}
    \text{ Temperature (°C)} \\
    \text{ Pressure (kPa)} \\
    \text{ Flow (L/s)} \\
    \text{ pH} \\
    \text{ Conductivity ($\mu$S/cm)}
\end{array}
$$

Each row represents one measurement, but the variables differ dramatically in scale.
Direct application of covariance PCA would be dominated entirely by pressure measurements, while potentially important variations in pH or flow rate vanish in the noise.
Yet blindly standardizing each variable might discard meaningful scale information.

**Example 11.8 (Scale Effects).** For the manufacturing data above, the first principal component under different preprocessing choices reveals starkly different patterns:

Covariance PCA yields $\mathbf{v}_1 \approx (0.002, 0.999, 0.001, 0.000, 0.003)^T$, essentially capturing pressure variation alone.
After standardizing to unit variance, correlation PCA gives $\mathbf{v}_1 \approx (0.51, 0.48, -0.42, 0.38, 0.44)^T$, revealing coordinated variation across all measurements.
The choice fundamentally shapes what patterns we can discover.

Beyond scaling, real data suffers contamination from measurement errors, sensor failures, and genuine but extreme events.
We need systematic methods to identify observations requiring special treatment.
The key insight lies in measuring distance not just in terms of raw values, but in a way that accounts for the natural scales and relationships in our data:

**Definition 11.9 (Mahalanobis Distance).** For an observation $\mathbf{x}$ from a collection with mean $\bar{\mathbf{x}}$ and positive definite covariance $[C]$, the **Mahalanobis distance** is:

$$
d_M(\mathbf{x}) = \sqrt{(\mathbf{x}-\bar{\mathbf{x}})^T[C]^{-1}(\mathbf{x}-\bar{\mathbf{x}})}
$$

> *Nota bene:* The matrix $[C]^{-1}$ plays the role of the squared reciprocal standard deviation $1/\sigma^2$ in higher dimensions, accounting for both scale and correlation between variables.

This metric accounts for both scale and correlation structure in measuring how far an observation deviates from typical patterns.
The inverse covariance matrix $[C]^{-1}$ ensures that distances properly reflect the natural variability in each direction.
Recall from Section 11.2 that $[C]$ is guaranteed only to be positive *semi*definite; when singular, the pseudoinverse $[C]^{\dagger}$ of Chapter 6 takes the place of $[C]^{-1}$, measuring distance only along directions in which the data actually varies.

For our engineering applications, this distance provides a natural way to identify observations that deviate markedly from typical patterns.
Experience suggests that observations with Mahalanobis distances more than twice that of typical points warrant careful investigation.

> *Foreshadowing:* This rule of thumb faces an audit in Section 12.3, where the geometry of high dimension locates typical observations at Mahalanobis distance near $\sqrt{d}$  — and sharpens the alarm accordingly.

> *Think:* In one dimension, $d_M$ reduces to distance from the mean measured in standard deviations: $d_M(x) = |x-\mu|/\sigma$.
> This connects to our intuition about "unusual" values in simple measurements.

**Example 11.10 (Outlier Detection).** Returning to our manufacturing data, most observations have Mahalanobis distances between 1.5 and 3 units.
However, one measurement:

$$
\mathbf{x} = (84.2, 1203, 12.8, 7.0, 158)^T
$$

yields $d_M = 4.9$, far exceeding the typical range.
Though each individual measurement appears plausible, their combination suggests a process anomaly requiring investigation.
The flow rate of 12.8 L/s, while not extreme in absolute terms, proves inconsistent with the observed temperature and pressure.

Missing entries present a final challenge: rare ones may simply be dropped, while extensive missingness defeats naive imputation and wants the machinery of Section 11.6.

Scale and contamination settled, one question of judgment remains, and the singular values themselves pose it.
Each singular value measures how strongly its own direction contributes to the structure of the data, precisely as the dominant eigenvalues of Chapter 9 measured contribution to asymptotic behavior; and the ratio $r_k$ of Section 11.3 says how much of the total a given truncation retains.
Neither says where to cut.

**Example 11.11 (Vibration Analysis).** Consider acceleration measurements from twenty-eight accelerometers on a bridge structure, yielding singular values

$$
\sigma_1 = 12.5, \quad \sigma_2 = 9.5, \quad \sigma_3 = 3.6,
$$

with the remaining twenty-five all close to $1.1$.
The sharp drop after $\sigma_2$ suggests two dominant modes of vibration.
Just as dominant eigenvalues governed asymptotic behavior in Chapter 9, these dominant singular values identify directions essential to the bridge's motion.
The first two components capture proportion $r_2\approx0.85$ of total variation — a quantitative measure of their dominance, and one that the long flat tail does more to earn than the third singular value does to threaten.

> *Nota bene:* When analyzing noise-corrupted data, sharp drops in singular values often mark the transition from signal to noise.
> The pattern is lawful: a matrix of pure noise fills a band of singular values with a predictable edge, and Section 12.4 computes it — the noise floor against which a scree plot should be read.

The shape of the spectrum offers what the ratio cannot: sharp drops mark natural truncation points where physical modes separate cleanly; gradual decay without gaps warns that no low-rank approximation is especially favored; clusters of nearly equal singular values indicate coupled features that should be retained or discarded together.

**Example 11.12 (Chemical Process Data).** A chemical reactor monitored through eight sensors yields normalized singular values decreasing more gradually:

$$
\sigma_1 = 2.05, \quad \sigma_2 = 1.76, \quad \sigma_3 = 1.52, \quad \sigma_4 = 1.18,
$$

$$
\sigma_5 = 0.89, \quad \sigma_6 = 0.75, \quad \sigma_7 = 0.62, \quad \sigma_8 = 0.45 .
$$

No sharp dominance emerges, reflecting complex coupling between process variables.
The cumulative proportion $r_4 = 0.85$ suggests retaining four components captures most significant variation while filtering sensor noise — though nothing in the spectrum marks four rather than three or five.

The practical choice of how many components to retain benefits from systematic validation.
By partitioning our data into training and testing sets, we can assess how well different truncation levels generalize to new observations.
Components that dominate in one portion of the data should maintain their dominance in others — a principle that helps distinguish genuine structure from sampling artifacts.

Sample size fundamentally affects our confidence in identified components.
When analyzing $n$ observations of $d$ variables, singular values beyond index $\min\{n,d\}$ must be zero — a fact following directly from the SVD's matrix structure.
More subtly, the ratio $n/d$ affects stability of non-zero singular values: too few observations relative to variables can create spurious apparent structure.
One question remains before these tools scale to practice: how are the dominant singular vectors of an enormous matrix actually found?
The answer was prepared in Chapter 9.
The singular vectors of $\mathcal{X}$ are the eigenvectors of $\mathcal{X}^T\mathcal{X}$, and multiplication by $\mathcal{X}^T\mathcal{X}$ amplifies dominant directions exactly as the iterations of Section 9.2 amplified dominant eigenvectors: dominance emerges through iteration here as it did there.
Industrial-strength refinements — blocked iterations with re-orthogonalization, Krylov subspace methods — accelerate the convergence without changing the principle.
A more audacious acceleration probes $\mathcal{X}$ with a handful of random vectors and lets chance locate the dominant directions — an apparent recklessness that Section 12.6 converts into a guarantee.

> *Caveat:* Physical constraints — non-negative entries, exactly preserved measurements, conservation laws — break the clean optimality of Theorem 11.6; no closed form survives.
> Numerical optimization takes over, with the truncated SVD as its natural starting point.

Preprocessing and truncation are the two decisions no theorem makes.
Different choices serve different ends: covariance PCA preserves absolute scales when they carry meaning, correlation PCA reveals purely relational patterns, robust methods sacrifice efficiency for reliability with corrupted data; and a sharp drop licenses a confident cut where a gradual decay licenses nothing.
*The theorem approximates whatever it is handed; judgment decides what it is handed.*

## 11.6 Completion & Corruption

Organic data arrives damaged in two ways, and the same instinct repairs both.
Entries go missing: recommender systems know a tiny fraction of user preferences, sensor networks suffer failures.
Entries go wrong: sensors fail outright rather than merely adding noise, calibration drift biases entire rows, adversaries contaminate observations deliberately.
In each case the surface is unreliable and the truth beneath it is low rank — a crystal whose fundamental symmetries survive the marring of its face — and in each case the recovery turns on the same manoeuvre, replacing a quantity that counts by a quantity that measures.

Rank alone underdetermines the problem: a matrix with a few entries missing may admit no rank-one completion and a whole family of rank-two ones, and rank itself — a count — is not a quantity optimization can handle.

**Definition 11.13 (Matrix Completion Problem).** Let $M\in\mathbb{R}^{m\times n}$ be an unknown matrix, and let $\Omega\subset\{1,\ldots,m\}\times\{1,\ldots,n\}$ denote a set of observed indices.
Given observations $\{m_{ij}:(i,j)\in\Omega\}$, the **matrix completion problem** seeks to recover $M$ under the assumption it has low rank:

$$
\min_X \operatorname{rank}(X) \quad\text{subject to}\quad x_{ij} = m_{ij}\text{ for all }(i,j)\in\Omega
$$

The fix is to replace the rank by the sum of the singular values.

**Definition 11.14 (Nuclear Norm).** The **nuclear norm** of a matrix $A$, denoted $\|A\|_*$, equals the sum of its singular values:

$$
\|A\|_* = \sum_{i=1}^{\min\{m,n\}} \sigma_i(A)
$$

This norm, previewed in Section 11.4, provides a convex relaxation of matrix rank, since $\operatorname{rank}(A)$ equals the number of nonzero singular values.

**Theorem 11.15 (Matrix Completion).** Let $M\in\mathbb{R}^{m\times n}$ be a rank-$r$ matrix with singular value decomposition $M=U\Sigma V^T$, where $\sigma_r(M)>0$.
Let $\Omega$ contain entries sampled uniformly at random.
Then with probability at least $1-cn^{-3}$ (for some constant $c$), $M$ is the unique solution to:

$$
\min_X \|X\|_* \quad\text{subject to}\quad x_{ij}=m_{ij}\text{ for all }(i,j)\in\Omega
$$

provided:

1. $|\Omega| \geq C\mu r(m+n)\log^2(m+n)$ entries are observed

2. The singular vectors $\{\mathbf{u}_i\}$ and $\{\mathbf{v}_i\}$ satisfy the **incoherence condition**:


$$
\max_{i,j} \left\{\frac{m}{r}\|\Pi_{U}\mathbf{e}_i\|^2, \frac{n}{r}\|\Pi_{V}\mathbf{e}_j\|^2\right\} \leq \mu
$$

    where $\Pi_{U}$ and $\Pi_{V}$ denote projection onto the images $\operatorname{im}(U)$ and $\operatorname{im}(V)$ respectively

Here $C$ is a numerical constant; $\mu$ is the incoherence parameter of condition 2, a property of $M$ itself.

Incoherence is the crucial hypothesis: it asks that information spread evenly through the matrix rather than concentrate in a few entries no sampling can be trusted to catch.

> *BONUS!* At scale the minimization is solved by **proximal gradient**: a gradient step, then a shrinking of the whole spectrum:
> $\mathcal{S}_\tau(Y)=U\operatorname{diag}(\max\{\sigma_i-\tau,0\})V^T.$
> The thresholding step is where the rank is decided.

Missing entries are the gentler damage: one at least knows which entries to distrust.
Corruption announces nothing.
It is gross and structured, not the mild randomness truncation tolerates — yet it typically touches few entries and leaves the rest reliable: sparse deviations from a low-rank truth.

**Definition 11.16 (Robust Principal Component Analysis).** The **robust principal component analysis** problem seeks to decompose an observed matrix $M$ as:

$$
M = L + S + N
$$

where:

- $L$ has low rank (capturing true patterns)

- $S$ is sparse (representing gross errors)

- $N$ contains small random noise

Sparsity, like rank, has a convex surrogate: the $\ell_1$ norm plays for sparse matrices the part the nuclear norm of Definition 11.14 plays for low-rank ones.
Minimizing a weighted sum of the two teases them apart, with guarantees:

> *Terminology:* for a matrix $S=[s_{ij}]$, write $\|S\|_1=\sum_{ij}|s_{ij}|$ and $\|S\|_0=\#\{(i,j) : s_{ij}\neq 0\}$.
> The first is an entrywise norm and measures.
> The second only counts, and a count is blind to scale: no norm at all.

**Theorem 11.17 (Principal Component Pursuit).** Let $M = L_0 + S_0$, where $L_0$ has rank $r$ and the support of $S_0$ is drawn uniformly at random among sets of its cardinality, the corrupted values themselves being arbitrary.
Suppose that the singular vectors of $L_0$ satisfy the incoherence condition of Theorem 11.15 with parameter $\mu$, and that

$$
\operatorname{rank}(L_0) \leq \frac{\rho_r\min\{m,n\}}{\mu\log^2\max\{m,n\}}
    \quad\text{and}\quad
    \|S_0\|_0 \leq \rho_s\,mn .
$$

Then, with high probability, the solution to

$$
\min_{L,S} \|L\|_* + \lambda\|S\|_1 \quad\text{subject to}\quad L + S = M
$$

recovers $L_0$ and $S_0$ exactly, for $\lambda = 1/\sqrt{\max\{m,n\}}$ and $\rho_r,\rho_s$ sufficiently small numerical constants.

**Example 11.18 (Video Surveillance).** A fixed camera records a scene where most variation comes from a few moving objects against a static background.
The data matrix $M$ has rows indexing frames and columns indexing pixels: the background, changing slowly if at all, is the low-rank $L$; the moving objects are the sparse $S$.
Robust PCA separates them, sensor glitches and lighting changes notwithstanding, and the rank of $L$ is rarely more than four.

The same decomposition patrols computer networks.
Let $M$ be a traffic matrix whose entry $M_{ij}$ is the volume flowing from node $i$ to node $j$ over some interval.
Normal traffic is spatially correlated and periodic, hence low rank; an intrusion is a sparse departure from it, and principal component pursuit peels the one from the other.
The geometry of the sparse part $S$ then names the threat:

- a port scan is a sparse *row* — one source probing many destinations;

- a distributed denial-of-service attack is a dense *column* — many sources flooding a single target;

- a propagating worm traces a *diagonal*; sustained data exfiltration, a lone persistent entry.

What robust factorization discards as the sparse residual, a network defender reads as an intrusion.

## 11.7 Beyond Linear PCA

Reality rarely submits to purely linear description.
Though principal components illuminate structure within linear transformations of space, many datasets harbor intrinsic nonlinearity — their essential patterns twist and curve through measurement space like vines growing beyond their linear supports.
A temperature sensor's readings may vary sinusoidally with time; chemical reaction rates couple through nonlinear dynamics; images of handwritten digits trace complex manifolds far from any linear subspace.
When data lies near a curved surface, the principal components — optimal though they are for linear approximation — miss the underlying simplicity entirely.
Like shadows cast by a curved wire that seem tangled and self-intersecting, linear projections can obscure rather than reveal.

The remedy is to keep the linear machinery and change the space it acts on.
Rather than working directly in measurement space, one implicitly maps the data into a higher-dimensional feature space through a kernel function $k(\mathbf{x},\mathbf{y})$ measuring similarity between observations, and performs standard PCA there — now operating on the kernel matrix $K=[k(\mathbf{x}_i,\mathbf{x}_j)]$ rather than on the covariance of raw measurements.
This $K$ is nothing but a Gram matrix — the same object introduced in Chapter 5 — with inner products taken in the implicit feature space rather than in measurement space.
The centering of Section 11.2 must be performed there too, and it can be: subtracting the feature-space mean amounts to replacing $K$ by $HKH$ for the centering matrix $H=I-\frac1n[1]$, an operation on $K$ alone that never touches the feature vectors it centers.

> *Foreshadowing:* the implicit feature mappings of kernel methods preview how neural networks will learn representations transforming data into more meaningful spaces.

This **kernel PCA** reveals nonlinear structure through careful choice of kernel function.
The radial basis kernel

$$
k(\mathbf{x},\mathbf{y}) = \exp\left(-\frac{\|\mathbf{x}-\mathbf{y}\|^2}{2\tau^2}\right)
$$

measures local similarity, allowing the method to follow curved patterns in data.
Though computationally intensive for large datasets, kernel PCA bridges the linear and the nonlinear with no machinery beyond the Gram matrix.

Chapter 13 buys generality of a different kind, replacing the linear map by a trained **autoencoder** — and paying for it with the uniqueness and the closed form that Theorem 11.6 guarantees.

—

## Decoding Neural Population Activity

Modern electrode arrays record hundreds of neurons at once, each a noisy, time-varying signal reflecting both local computation and global brain state.
Individually the cells are erratic; collectively their activity resolves into clear structure when viewed through dimensionality reduction.

Consider a typical motor cortex experiment where researchers record from $n=256$ neurons while a subject performs reaching movements toward different targets.
Each neuron's firing rate varies with time, producing a vector $\mathbf{r}(t)\in\mathbb{R}^n$ of instantaneous population activity sampled at millisecond resolution.
Over a session with 100 reaches lasting 500ms each, we obtain the centered data matrix:

$$
R = \begin{bmatrix}
    \leftarrow & \mathbf{r}(0) - \bar{\mathbf{r}} & \rightarrow \\
    \leftarrow & \mathbf{r}(1) - \bar{\mathbf{r}} & \rightarrow \\
    & \vdots & \\
    \leftarrow & \mathbf{r}(49999) - \bar{\mathbf{r}} & \rightarrow
    \end{bmatrix} \in \mathbb{R}^{50000\times 256}
$$

where $\bar{\mathbf{r}}$ denotes the temporal average firing rate vector and $T=50{,}000$ counts the samples.
The sample covariance matrix $[C] = \frac{1}{T}R^TR \in \mathbb{R}^{256\times 256}$ captures how pairs of neurons co-vary in their firing patterns.

A concrete example shows the structure in this neural data.
During a recent experiment, the first ten singular values of $R$ were:

$$
\sigma_1 = 128.4, \quad \sigma_2 = 84.2, \quad \sigma_3 = 52.1, \quad \sigma_4 = 31.5, \quad \sigma_5 = 18.7
$$

$$
\sigma_6 = 12.3, \quad \sigma_7 = 8.1, \quad \sigma_8 = 5.4, \quad \sigma_9 = 3.8, \quad \sigma_{10} = 2.6
$$

The proportion of variance explained by the first $k$ components:

$$
r_k = \frac{\sum_{i=1}^k \sigma_i^2}{\sum_{i=1}^{256} \sigma_i^2}
$$

reaches $r_5 \approx 0.94$ with just five components, the remaining $251$ directions — all but four of them below $\sigma_{10}=2.6$ — splitting the last six percent among them.
This reduction — from 256 neurons to 5 principal components — suggests neural computation occurs in a much lower-dimensional space than raw cell counts would indicate.

The principal components, the eigenvectors of $[C]$, carry distinct aspects of motor encoding.
Once each cell's own variance is divided out, the leading vector is nearly uniform, $[\mathbf{v}_1]_j \approx 1/\sqrt{n}$: a global activation mode that tracks overall movement vigor.
The second splits the population — positive weights on neurons preferring forward reaches, negative on those preferring backward — so that $\mathbf{v}_2$ reads out direction.
Projecting the activity at each instant onto these axes,

$$
z_i(t) = \mathbf{v}_i^T(\mathbf{r}(t) - \bar{\mathbf{r}}),
$$

yields scores that track behavior tightly: $z_1$ correlates with movement speed, $z_2$ with reach direction, the next pair with grip force.
A five-dimensional shadow of a $256$-neuron recording is enough to follow the hand.

Neural data demand the same care as any other.
Baselines drift with brain state and signals are transiently lost, so the preprocessing of Section 11.5 applies verbatim; the standardization above is that section's correlation option, taken because without it the leading component would report which electrodes sat nearest a loud cell rather than what the population was doing.

This low-dimensional structure is what makes brain-computer interfaces work.
Rather than decode intended movement from individual cells, a modern interface first projects the population onto its leading principal components and decodes from the scores.
The result is robust: lose a neuron or two and the components barely move, because they rest on the coordinated activity of the whole population rather than any single cell — the same few dimensions that describe the data also stabilize its clinical use.

That the brain's motor commands occupy so thin a slice of the space available to $256$ neurons is the real lesson, and linear methods locate that slice exactly, even as the brain's own nonlinearity surely folds richer structure within it.
*A population of neurons computes in the span of a handful of principal components.*

—

## Eigenfaces

**Eigenfaces** shows most plainly how PCA extracts structure from high-dimensional data.
Reshape a grayscale $p\times q$ image into a single vector in $\mathbb{R}^{pq}$: a face at modest $100\times100$ resolution becomes a point in $\mathbb{R}^{10000}$, a space in which direct analysis is hopeless.
Yet faces exhibit strong statistical regularities.

Given $N$ face images $\{\mathbf{x}_1,\ldots,\mathbf{x}_N\}$, each reshaped into a vector, center by subtracting the mean face:

$$
\bar{\mathbf{x}} = \frac{1}{N}\sum_{i=1}^N \mathbf{x}_i
    \quad:\quad
    \tilde{\mathbf{x}}_i = \mathbf{x}_i - \bar{\mathbf{x}}
$$

The centered images form the *columns* of a matrix $X\in\mathbb{R}^{pq\times N}$, which is the transpose of the arrangement of Section 11.2: here one wants a basis for the space of images, not for the space of samples.
Its singular value decomposition $X = U\Sigma V^T$ yields the eigenfaces: the leading columns of $U$, which are principal components in the sense of Definition 11.1 after all, the left singular vectors of $X$ being the right singular vectors of $X^T$.

Reshaped back to image format, the first few eigenfaces carry face shape and gross lighting; later ones, fine detail shading into noise.
Forty or fifty suffice: two orders of magnitude.

Any face is approximated by projection onto the first $k$ eigenfaces:

$$
\mathbf{x} \approx \bar{\mathbf{x}} + \sum_{i=1}^k c_i\mathbf{u}_i
    \quad\text{where}\quad
    c_i = (\mathbf{x}-\bar{\mathbf{x}})^T\mathbf{u}_i
$$

The coefficients $c_i$ form a **face code**.

Modern face recognition has moved to deep learning; yet the intermediate layers of those networks learn representations remarkably like eigenfaces.

Here the singular value decomposition of Chapter 10 becomes a working tool: the leading left singular vectors are a basis, the preprocessing of Section 11.5 decides what that basis sees, and the truncation tests of that same section decide how many of its vectors to keep.
A face, in the end, is a short list of coordinates against the eigenfaces.
*Recognition is a change of basis followed by a nearest neighbor.*

—

## The Netflix Prize

The Netflix Prize of 2006--2009 made reconstruction from fragments precise: a million dollars for predicting human preference at scale.

The mathematical landscape seemed clear: a massive but sparse matrix $R\in\mathbb{R}^{m\times n}$ containing roughly 100 million ratings from $m=480{,}000$ users across $n=17{,}770$ movies.
Each entry $r_{ij}$ represented one user's 1-5 star rating of one movie, with over 98% of entries missing — most users rate only a tiny fraction of available films.
The formal objective was simple: minimize the root mean squared error (RMSE) of predictions:

$$
\text{RMSE} = \sqrt{\frac{1}{|\Omega|}\sum_{(i,j)\in\Omega}(r_{ij} - \hat{r}_{ij})^2}
$$

where $\Omega$ denotes the set of observed ratings and $\hat{r}_{ij}$ represents predicted ratings.

> *Historical Note:* The 10% improvement target was chosen based on Netflix's internal analysis suggesting this threshold would yield meaningful improvement in user experience.
> Few anticipated it would take three years to achieve.

The winning solution turned on the very tools developed in Section 11.6: the singular value decomposition and its offspring.
Yet real-world recommender systems must contend with complexities our pristine theory ignores:

1. Temporal effects: viewing patterns shift over time

2. User bias: some rate generously, others harshly

3. Item bias: some films consistently rate higher than others

4. Implicit feedback: not rating a film conveys information

Low-rank approximation, on its own, proved insufficient.
The winning algorithm addressed these complexities through careful decomposition of the ratings matrix.
For user $u$ rating item $i$ at time $t$, the predicted rating took the form:

$$
\hat{r}_{ui}(t) = \mu + b_u(t) + b_i(t) + \mathbf{q}_i^T\left(\mathbf{p}_u + |\mathcal{N}(u)|^{-\frac{1}{2}}\sum_{j\in\mathcal{N}(u)}\mathbf{y}_j\right)
$$

Here:

- $\mu$ represents global mean rating

- $b_u(t)$ and $b_i(t)$ capture time-varying user and item biases

- Vectors $\mathbf{q}_i,\mathbf{p}_u\in\mathbb{R}^f$ encode $f$ latent features

- The sum over $\mathcal{N}(u)$ incorporates implicit feedback

This decomposition rests on a single wager: that human preference, though complex, largely reduces to the interaction of a few interpretable features.
The parameters were learned by solving the regularized optimization:

$$
\min_{b,\mathbf{p},\mathbf{q},\mathbf{y}} \sum_{(u,i)\in\Omega} \left(r_{ui} - \hat{r}_{ui}\right)^2 +
    \lambda\left(\|b_u\|^2 + \|b_i\|^2 + \|\mathbf{p}_u\|^2 + \|\mathbf{q}_i\|^2 + \sum_{j\in\mathcal{N}(u)}\|\mathbf{y}_j\|^2\right)
$$

which is the nuclear norm regularization of Section 11.6 wearing factored clothes: minimized over all factorizations of a given product, *half* the sum of squared factor norms is the nuclear norm of that product, as Exercise 21 asks one to prove.

Implementation revealed equally important lessons about robust matrix factorization.
Raw ratings proved surprisingly noisy, contaminated by:

- Varying interpretation of star ratings across users

- Temporal drift in rating patterns

- Selection bias in which movies users choose to rate

- Adversarial ratings from competing services

These challenges demanded the robust techniques developed in Section 11.6.
By carefully modeling and removing systematic biases while remaining suspicious of extreme ratings, the winning team achieved an RMSE improvement of 10.06% — just barely crossing the threshold that had seemed impossible when the contest began.
The margin was mathematical: the factor model supplied the structure, and three years of engineering bought the last tenth of a percent.

The legacy of the Netflix Prize extends far beyond movie recommendations.

> Though Netflix never implemented the winning algorithm due to engineering complexity, the competition's insights fundamentally transformed how industry approaches recommender systems.

Its insights now power personalization across the digital economy, from e-commerce to music streaming to social media content ranking.
Each applies the same core principle: that human preference, though seemingly chaotic, often admits low-rank approximation.
*Preference, sampled thinly and mostly missing, still surrendered its factors.*

—

## Exercises: Chapter 11

1. Two centered data vectors of length four are $\hat{Y}=(3,1,-1,-3)^T$ and $\hat{Z}=(1,3,-3,-1)^T$.
Compute $\operatorname{cov}(Y,Z)=\frac{1}{n}\hat{Y}\cdot\hat{Z}$, then compute $\operatorname{corr}(Y,Z)$ as the cosine of the angle between the two vectors, in the sense of Section 5.2 of Chapter 5.
Now take the uncentered pair $Y=(-2,-1,1,2)^T$ and $Z=(4,1,1,4)^T$, center both, and find their correlation.
Since $z_i=y_i^2$ for every $i$, say precisely what a correlation of zero rules out and what it leaves standing.

2. Two sensors monitoring a process report the paired readings

$$
\begin{bmatrix}
    6 & 18 \\ 8 & 16 \\ 12 & 22 \\ 14 & 24
    \end{bmatrix} .
$$

Compute the sample mean and the covariance matrix, with the $1/n$ scaling of Section 11.1.
Diagonalize $[C]$ by hand and identify the first principal component of Definition 11.1.
Report the proportion of total variance it carries, and the correlation of the two sensors.

3. A rank-three matrix $A\in\mathbb{R}^{5\times4}$ has $\sigma_1=12$, $\sigma_2=4$, and $\|A\|_F=13$.
Recover $\sigma_3$ from the Frobenius identity of Exercise 6 of Chapter 10 alone.
Give the smallest error $\|A-B\|_F$ achievable by a matrix $B$ of rank one, by Theorem 11.6, without ever computing $A_1$.
Note that neither answer required a single entry of $A$.

4. Three sensors on a chemical reactor track temperature, pressure, and flow rate, each standardized to a common scale, and return

$$
[C] = \begin{bmatrix}
    13 & 2 & 6 \\ 2 & 8 & 4 \\ 6 & 4 & 12
    \end{bmatrix} .
$$

Find all three eigenvalues and unit eigenvectors by hand; the characteristic polynomial factors over the integers and every eigenvector comes out in thirds.
Report the proportion of total variance carried by the first two principal components, and say what the sign patterns of those two eigenvectors assert about the reactor's three quantities.

5. Let $A=\begin{bmatrix}4&2&1\\2&3&0\\1&0&2\end{bmatrix}$.
Show that $A$ is positive definite with spectrum $\{4+\sqrt{3},\,4-\sqrt{3},\,1\}$, so that Exercise 11 of Chapter 10 identifies its singular values with its eigenvalues.
Deflate the smallest to obtain the best rank-two approximation $A_2$, whose entries are rational, and record $\|A-A_2\|_F$.
Then lower the entry $a_{33}$ from $2$ to $3/8$, check that the result has rank two as well, and measure how much Theorem 11.6 saves over that competitor.

6. As in Example 11.7, block compression approximates each block of

$$
A = \begin{bmatrix}
    200 & 190 & 40 & 50 \\
    180 & 171 & 48 & 60 \\
    60 & 57 & 200 & 150 \\
    80 & 76 & 120 & 90
    \end{bmatrix}
$$

on its own.
Check that each of the four $2\times2$ blocks has rank one, so that the blockwise scheme reproduces $A$ exactly.
The whole of $A$ has rank three with $\sigma_3=5.5367$; record the error $\|A-A_2\|_F$ that its best rank-two approximation commits.
Count what each scheme stores by the arithmetic of that example, and find that the exact fit costs two numbers more.

7. Three quality metrics in semiconductor manufacturing yield the correlation matrix

$$
[R] = \begin{bmatrix}
    1.0 & 0.8 & 0.7 \\
    0.8 & 1.0 & 0.9 \\
    0.7 & 0.9 & 1.0
    \end{bmatrix} .
$$

Write $\mathbf{w}$ for the equiangular unit vector $(1,1,1)^T/\sqrt{3}$.
Evaluate the quadratic form $\mathbf{v}^T[R]\mathbf{v}$ at $\mathbf{v}=\mathbf{w}$ and obtain the exact value $13/5$.
Conclude from Theorem 11.4 and $\operatorname{tr}[R]=3$ that the first principal component carries at least $13/15$ of the total variance, without computing an eigenvalue.
The truth is $0.86759\ldots$, while the characteristic polynomial

$$
250\lambda^3-750\lambda^2+265\lambda-17
$$

is irreducible over the rationals, so the bound is the only figure here that a hand can reach.
Say what a leading component so nearly equiangular reports about the three metrics.

8. Let $[C]=\begin{bmatrix}a & c\\ c & b\end{bmatrix}$ be a covariance matrix with $c\neq0$, and let $[R]$ be the correlation matrix built from it.
Compute the eigenvectors of $[R]$ outright, test them against $[C]$, and prove that covariance PCA and correlation PCA return the same principal components exactly when $a=b$.
Then verify that

$$
[C] = \begin{bmatrix} 8 & 2 & 0\\ 2 & 8 & 0\\ 0 & 0 & 7\end{bmatrix}
$$

has unequal variances, nonzero correlations and simple spectra on both sides, and yet the same ordered components under either scaling — so the divergence displayed in Example 11.8 is a fact about particular data, not a theorem about unequal variances.
Identify what the two-variable argument used that three variables are free to lose.

9. A manufacturing quality inspection system records five measurements per part.
The singular values of the centered data matrix decay as

$$
\sigma_k = 10e^{-0.8k} , \quad k = 1,\ldots,5 .
$$

Prove that the ratio $r_2$ of Section 11.3 is at least $0.95$, noting first that the amplitude $10$ cancels and that the squares form a geometric progression.

10. Section 11.4 asserts that reconstruction from $k$ retained components is an orthogonal projection onto the chosen coimage; supply the proof.
Let the centered data matrix have singular value decomposition $\mathcal{X}=U\Sigma V^T$, write $V_k=[\mathbf{v}_1\cdots\mathbf{v}_k]$, and let $\mathcal{X}_k=\sum_{i\leq k}\sigma_i\mathbf{u}_i\mathbf{v}_i^T$ be the truncation, a rank-$k$ approximation in the sense of Definition 11.5.
Show that $\operatorname{row}(\mathcal{X}_k)=\operatorname{span}\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}$, and conclude from Definition 6.12, Theorem 6.16 and the orthogonal splitting of Theorem 6.9 that $\mathcal{X}_k^\dagger\mathcal{X}_k$ is the orthogonal projection onto that subspace and therefore equals $V_kV_k^T$.
Then prove $\mathcal{X} V_kV_k^T=\mathcal{X}_k$ and that every row of the residual $\mathcal{X}-\mathcal{X}_k$ lies in the span of the discarded right singular vectors, so its Frobenius norm is exactly the error Theorem 11.6 certifies as minimal.

11. The proof of Theorem 11.6 extracts en route an inequality it never states in general: for $X,Y\in\mathbb{R}^{m\times n}$ and indices with $i+j-1\leq\min\{m,n\}$,

$$
\sigma_{i+j-1}(X+Y) \;\leq\; \sigma_i(X)+\sigma_j(Y) .
$$

Establish first the triangle inequality $\|X+Y\|_2\leq\|X\|_2+\|Y\|_2$, which the book nowhere states for matrices, from Definition 10.5 and the triangle inequality for vectors, which Lemma 5.5 yields by expanding $\|\mathbf{u}+\mathbf{v}\|^2$  — the move Exercise 9 made in a special case.
Prove the display by adding a best rank-$(i-1)$ approximation to $X$ to a best rank-$(j-1)$ approximation to $Y$, a matrix of rank less than $i+j-1$, and applying Lemma 10.7 to the sum.
Then take $Y=B$ of rank at most $k$ and $j=k+1$ to recover $\sigma_{k+i}(A)\leq\sigma_i(A-B)$, the step that drives the Frobenius half of Theorem 11.6.

12. Let $A\in\mathbb{R}^{m\times n}$ have singular value decomposition $A=U\Sigma V^T$, fix $k$, and set $W=\operatorname{span}\{\mathbf{u}_1,\ldots,\mathbf{u}_k\}$.
Prove that the truncation $A_k$ is $\Pi_{W}A$, the projection applied to each column of $A$ separately.
Deduce from Lemma 6.7 and the Pythagorean theorem the splitting $\|B\|_F^2=\|\Pi_{W}B\|_F^2+\|B-\Pi_{W}B\|_F^2$ for every $B$ with $m$ rows, hence the contraction $\|\Pi_{W}B\|_F\leq\|B\|_F$, with equality precisely when every column of $B$ lies in $W$.
Conclude that the ratio $r_k$ of Section 11.3 is exactly the fraction $\|A_k\|_F^2/\|A\|_F^2$ of Frobenius energy that truncation retains.

13. Let $A$ have rank $r$ with smallest nonzero singular value $\sigma_r$, and let $E$ be a perturbation with $\|E\|_2<\sigma_r$.
Prove from Lemma 10.7 that $\operatorname{rank}(A+E)\geq r$, and show that the threshold cannot be raised by exhibiting a perturbation of norm exactly $\sigma_r$ that drops the rank.
Assume now the stronger $\|E\|_2<\sigma_r/2$ and prove the gap $\sigma_r(A+E)>\sigma_r/2>\sigma_{r+1}(A+E)$, taking the upper estimate from Lemma 10.7 and the lower from Exercise 11.

14. Consider the completion problem of Definition 11.13 for

$$
M = \begin{bmatrix} 2 & ? & 1\\ ? & 4 & ?\\ 1 & ? & 2\end{bmatrix} .
$$

Count the parameters in a factorization $X=UV^T$ with $U,V\in\mathbb{R}^{3\times2}$, discount those absorbed by the ambiguity $U\mapsto UG$ and $V\mapsto VG^{-T}$, and compare what remains against the five observations and against what Theorem 11.15 asks of a sampling pattern this thin.

15. A time series of strain measurements from a material under cyclic loading yields singular values

$$
\sigma_1 = 12.3, \quad \sigma_2 = 5.1, \quad \sigma_3 = 0.8, \quad \sigma_4 = 0.3, \quad \sigma_5 = 0.2 .
$$

Locate the sharp drop, and compute the proportion of variation retained by the components above it.
Decide whether this spectrum reads like the bridge of Example 11.11 or the reactor of Example 11.12, and say how many modes the material is running.
Say also which of those two examples leaves its truncation rank genuinely in doubt, and what a spectrum without gaps leaves the gap criterion to work with.

16. Fifty centered measurements in $\mathbb{R}^2$ have covariance matrix $\operatorname{diag}(9,1)$, so that the first principal component points along $\mathbf{e}_1$.
Append the single observation $\mathbf{y}=(\rho/\sqrt{2})(1,1)^T$, and show that the covariance of the enlarged sample is a fixed matrix plus $\tfrac{25\rho^2}{2601}(1,1)(1,1)^T$, so that the first component turns toward $\mathbf{y}$ and approaches $45^\circ$.
Compute the Mahalanobis distance of $\mathbf{y}$ from the original fifty by Definition 11.9 and find it equal to $\rho\sqrt{5}/3$.
One grows like $\rho^2$ and the other like $\rho$; conclude why the robust screening of Section 11.5 must precede the eigenvector computation.

17. The eight entries of a $4\times4$ matrix with $i+j$ even are observed and all equal $1$, and the other eight are unknown.
Show that $(1,t,1,t)^T(1,1/t,1,1/t)$ has rank one and matches every observation for each $t\neq0$, so that exactly half the entries determine nothing at all and the error of a reconstruction is unbounded.
Name the hypothesis of Theorem 11.15 that this observation pattern violates, observing that it is not incoherence — the all-ones matrix carries the smallest incoherence parameter a rank-one matrix can have.
Say what uniformly random sampling supplies that a regular pattern does not.

18. Kernel PCA replaces the covariance matrix by the kernel matrix $K=[k(\mathbf{x}_i,\mathbf{x}_j)]$ of Section 11.7.
Take the linear kernel $k(\mathbf{x},\mathbf{y})=\mathbf{x}\cdot\mathbf{y}$ on a centered data matrix $\mathcal{X}\in\mathbb{R}^{n\times d}$, and show that $K$ is the Gram matrix $\mathcal{X}\mathcal{X}^T$ of Chapter 5, already centered in the feature space.
Prove that $\mathbf{w}\mapsto\mathcal{X}\mathbf{w}$ carries every eigenvector of $\mathcal{X}^T\mathcal{X}=n[C]$ with nonzero eigenvalue to an eigenvector of $K$ with the same eigenvalue, so that kernel PCA returns nothing but the components of Definition 11.1.
Say what a kernel must therefore do if it is to see anything $[C]$ cannot.

19. Five thermocouples ring an industrial furnace whose readings, in degrees Celsius, have mean $\bar{\mathbf{x}}=(845,835,840,850,855)^T$ and covariance

$$
[C] = \begin{bmatrix}
    100 & 85 & 82 & 75 & 70 \\
    85 & 120 & 90 & 80 & 75 \\
    82 & 90 & 110 & 85 & 80 \\
    75 & 80 & 85 & 90 & 75 \\
    70 & 75 & 80 & 75 & 95
    \end{bmatrix} .
$$

A single sweep returns $\mathbf{x}=(850,823,841,868,859)^T$, and no sensor lies more than two standard deviations from its own mean.
The smallest eigenvalue of $[C]$ is $\lambda_5\approx13.5$, belonging to the unit eigenvector

$$
\mathbf{v}_5\approx(-0.12,0.02,-0.46,0.84,-0.24)^T
$$

that Definition 11.1 calls a principal component.
Writing $z_k=\mathbf{v}_k^T(\mathbf{x}-\bar{\mathbf{x}})$, the squared Mahalanobis distance of Definition 11.9 is $\sum_k z_k^2/\lambda_k$; compute the term belonging to $\mathbf{v}_5$, and conclude from it alone that $d_M(\mathbf{x})$ exceeds $3$.
Name the direction that raised the alarm, and say why a furnace can be in trouble with every gauge reading plausibly.

20. A network monitor records the volume $M_{ij}$ of traffic sent from internal host $i$ to external destination $j$ over one hour:

$$
M = \begin{bmatrix}
    2 & 1 & 3 & 5 & 4 \\
    11 & 9 & 13 & 10 & 8 \\
    6 & 3 & 9 & 15 & 12 \\
    8 & 4 & 12 & 20 & 16
    \end{bmatrix} .
$$

Ordinary traffic here has rank one, every host dividing its total among the destinations in the same proportions.
Split $M=L+S$ as in Definition 11.16 with $L$ of rank one and $S$ as sparse as it can be made, confirm that $\operatorname{rank} M=2$, and list the support of $S$.
Name the host at fault, and say which of the intrusion patterns catalogued earlier in this chapter its signature indicates.

21. (Challenge.) Let $A\in\mathbb{R}^{m\times n}$ have rank $r$ and thin singular value decomposition $A=W_r\Sigma_rZ_r^T$, and let $U\in\mathbb{R}^{m\times d}$ and $V\in\mathbb{R}^{n\times d}$ run over all factorizations $A=UV^T$ of inner dimension $d\geq r$.
Show that $U=W_r\Sigma_r^{1/2}$ and $V=Z_r\Sigma_r^{1/2}$ is one such factorization, and that for it $\tfrac{1}{2}(\|U\|_F^2+\|V\|_F^2)$ equals the nuclear norm $\|A\|_*$ of Definition 11.14.
Prove that none does better, starting from $\|A\|_*=\operatorname{tr}(W_r^TAZ_r)=\langle W_r^TU,\,Z_r^TV\rangle_F$ in the Frobenius inner product of Example 5.3, applying the Cauchy-Schwarz inequality of Lemma 5.5, and invoking the contraction of Exercise 12 to bound $\|W_r^TU\|_F$ by $\|U\|_F$, and finish with $(\|U\|_F-\|V\|_F)^2\geq0$.
Conclude that the regularizer $\sum_u\|\mathbf{p}_u\|^2+\sum_i\|\mathbf{q}_i\|^2$ of the winning Netflix Prize model, described at the close of this chapter, never falls below twice the nuclear norm of the matrix it factors, and meets it at the balanced factorization.

---


# Chapter 12. Probability & High Dimension

*"do I not stretch the heavens abroad or fold them up like a garment"*

**Randomness has shadowed** this book from its first data set: noise in the measurements of Chapter 6, corruption in the matrices of Chapter 11, sampling error wherever data was finite.
It has been treated, so far, as weather — ambient, adversarial, endured.
This chapter treats it as terrain: a subject with a geometry of its own and, by the end, an instrument with uses of its own.

The geometry comes first, and it is not new; that is the surprise.
The probability glimpsed in multivariable calculus — densities, expectations, variances — has been living all along in the inner product spaces of Chapter 5: expectation is a projection, standard deviation is a length, correlation is a cosine, and the memorized identities of elementary statistics are Pythagoras and his relatives in light disguise.

> The probability assumed here is the multivariable-calculus kind: densities integrated over reasonable domains.
> Nothing measure-theoretic is required.

Where the geometry leads is high dimension, because that is where data now lives — embeddings in $\mathbb{R}^{1024}$, images in $\mathbb{R}^{10^6}$ — and where intuition trained on three dimensions fails in every particular: angles, lengths, volumes, spectra.
Random directions are reliably right-angled; random lengths crowd onto thin shells; the singular values of pure noise assemble into a bulk of computable shape.
Chance, at scale, stops behaving like caprice and starts behaving lawfully.
The same concentration that wrecks low-dimensional intuition will, by the chapter's end, measure a million-point cloud without ever looking at it and factor matrices too large for any exact method to touch.

## 12.1 The Geometry of Expectation

What calculus did not disclose is where densities, expectations, and variances live.
They live in an inner product space.

Begin with finitely many outcomes, numbered $1$ through $N$.
A random variable assigns a number to each outcome, and so is simply a vector $f\in\mathbb{R}^N$; products and sums of random variables are taken outcome-by-outcome.
A probability density on the same outcomes is likewise a vector $\rho=(\rho_1,\ldots,\rho_N)^T$, its entries nonnegative and summing to one; for the inner product below we ask them positive.
Chapter 5 taught that any vector of positive weights induces an inner product; a density is such a vector, and its inner product is the one this chapter inhabits.

**Definition 12.1 (Probability Inner Product).** Let $\rho$ be a probability density on $N$ outcomes, with each $\rho_i>0$ and $\sum_i\rho_i=1$.
The **probability inner product** of random variables $f,g\in\mathbb{R}^N$ is the $\rho$-weighted inner product

$$
\langle f,g\rangle_\rho \,=\, \sum_{i=1}^N \rho_i\,f_i\,g_i .
$$

> For a continuous density on a domain $D\subset\mathbb{R}^n$  — or on a surface sitting inside one — replace sums by integrals: $\langle f,g\rangle_\rho = \int_D fg\,\rho\,dx$, the integral inner product of Chapter 5 carrying a weight.
> Every identity in this section transcribes verbatim.

Note how the axiom that makes $\rho$ a density is, in this light, a statement about the constant random variable $\mathbf{1}=(1,\ldots,1)^T$:

$$
\left\|\mathbf{1}\right\|_\rho^2 = \sum_{i=1}^N \rho_i = 1 .
$$

*Total-probability-one* says that the constant function has unit length.
The familiar expectation follows at once, as an inner product with this newly-unit vector:

$$
\langle f,\mathbf{1}\rangle_\rho = \sum_{i=1}^N \rho_i f_i = \mathbb{E}(f) ,
$$

and, more generally, $\langle f,g\rangle_\rho = \mathbb{E}(fg)$: the inner product of two random variables is the expectation of their product.

As $\mathbf{1}$ has unit length in this geometry, the inner product $\langle f,\mathbf{1}\rangle_\rho$ is performing an operation familiar from Chapter 6: orthogonal projection onto the line of constant random variables, the diagonal of $\mathbb{R}^N$,

$$
\Pi_{\mathbf{1}} f \,=\, \langle f,\mathbf{1}\rangle_\rho\,\mathbf{1} \,=\, \mathbb{E}(f)\,\mathbf{1} ,
$$

the constant random variable whose value is the mean.
Among all constants $c$, the mean is the one minimizing $\|f-c\mathbf{1}\|_\rho$.

> *Think:* This explains a fact so often invoked that its strangeness goes unnoticed: linearity of expectation, $\mathbb{E}(f+g)=\mathbb{E}(f)+\mathbb{E}(g)$, holds with no hypothesis of independence.
> None is needed.
> Inner products and projections alike are linear.

What remains of $f$ after its mean is removed?
The **centered** random variable $\hat{f} = f - \mathbb{E}(f)\mathbf{1}$ is the residual, orthogonal to the constants: $\langle\hat{f},\mathbf{1}\rangle_\rho = \mathbb{E}(f) - \mathbb{E}(f)\|\mathbf{1}\|_\rho^2 = 0$.
Centering, the hat worn throughout Chapter 11, is projection onto the hyperplane $\mathbf{1}^\perp$.
The variance and standard deviation now identify themselves:

$$
\mathbb{V}(f) = \mathbb{E}\left(\hat{f}^2\right) = \left\|\hat{f}\right\|_\rho^2
    \qquad
    \sigma(f) = \left\|\hat{f}\right\|_\rho .
$$

The standard deviation is a length — the distance from $f$ to the constants — which is why it carries the same units as $f$ while the variance carries their square.

> *Compare:* Read $\rho$ as a mass density distributing unit mass at the values of $f$: then $\mathbb{E}(f)$ is the center of mass, $\mathbb{V}(f)$ the moment of inertia about it, and $\sigma$ the radius of gyration.
> The mechanical opening of Chapter 11 was no analogy; it was the same inner product.

The decomposition $f = \mathbb{E}(f)\mathbf{1} + \hat{f}$ splits $f$ into orthogonal pieces, and orthogonal decompositions obey the oldest theorem in this book's prehistory:

$$
\|f\|_\rho^2 = \left\|\mathbb{E}(f)\mathbf{1}\right\|_\rho^2 + \left\|\hat{f}\right\|_\rho^2
    \qquad\text{that is,}\qquad
    \mathbb{E}\left(f^2\right) = \mathbb{E}(f)^2 + \mathbb{V}(f) .
$$

> *Think:* The most memorized identity in statistics is the Pythagorean theorem.
> Generations of students have carried $\mathbb{E}(f^2)=\mathbb{E}(f)^2+\mathbb{V}(f)$ into their examinations without being told it has a hypotenuse.

Two random variables now come with an angle between them.
Their covariance is the inner product of their residuals, and their correlation is its cosine:

$$
\operatorname{cov}(f,g) = \left\langle \hat{f},\hat{g}\right\rangle_\rho
    \qquad
    \operatorname{corr}(f,g) = \frac{\langle \hat{f},\hat{g}\rangle_\rho}{\|\hat{f}\|_\rho\,\|\hat{g}\|_\rho} = \cos\theta .
$$

That correlations lie between $-1$ and $+1$ is the Cauchy-Schwarz inequality (Lemma 5.5).
Expanding $\|\hat{f}+\hat{g}\|_\rho^2$ gives the law of cosines in additive dress,

$$
\mathbb{V}(f+g) = \mathbb{V}(f) + \mathbb{V}(g) + 2\operatorname{cov}(f,g) ,
$$

so that variances add exactly when the residuals are orthogonal: Pythagoras, again.
Uncorrelated random variables are orthogonal.
Independence implies orthogonality of residuals; the converse fails.

> *Recall:* Chapter 11 computed covariance as a dot product scaled by $1/n$ and offered this as balm.
> The scaling is now unmasked: $1/n$ is the uniform density on $n$ observations, and the formulas of Section 11.1 are the special case $\rho_i=1/n$ of this section.
> The inner product space behind *"correlation is cosine similarity"* is at last apparent.

For an event $A$  — a subset of outcomes — the **indicator** $\mathbf{1}_A$ takes the value $1$ on $A$ and $0$ elsewhere, and

$$
\mathbb{P}(A) = \mathbb{E}\left(\mathbf{1}_A\right) = \left\langle \mathbf{1}_A,\mathbf{1}\right\rangle_\rho
    \qquad
    \left\langle \mathbf{1}_A,\mathbf{1}_B\right\rangle_\rho = \mathbb{P}(A\cap B) .
$$

Probabilities of events are inner products of indicators; the overlap of two events is, literally, an inner product.

> *Caveat:* The hypothesis $\rho_i>0$ earns positive-definiteness.
> If some outcome has $\rho_i=0$, the form is only semidefinite, and one identifies random variables that agree except on outcomes of probability zero — a quotient construction in the spirit of Section 3.6.

One inequality converts lengths and distances into statements about how often a random variable strays.

**Lemma 12.2 (Markov & Chebyshev Inequalities).** Let $t>0$.
For a random variable $f\geq 0$,

$$
\mathbb{P}(f\geq t) \,\leq\, \frac{\mathbb{E}(f)}{t} ,
$$

and for arbitrary $f$,

$$
\mathbb{P}\left(\left|f-\mathbb{E}(f)\right|\geq t\right) \,\leq\, \frac{\mathbb{V}(f)}{t^2} .
$$

*Proof.* Let $A$ be the event $f\geq t$.
Outcome-by-outcome, $t\,\mathbf{1}_A \leq f$: on $A$ this is the definition of $A$, and off $A$ it reads $0\leq f$.
Expectation preserves inequalities — the weights $\rho_i$ are positive — and is linear, so $t\,\mathbb{P}(A) = \mathbb{E}(t\,\mathbf{1}_A) \leq \mathbb{E}(f)$.
For the second claim, apply the first to the nonnegative random variable $\hat{f}^2$ with threshold $t^2$: the event $|f-\mathbb{E}(f)|\geq t$ is the event $\hat{f}^2\geq t^2$, whence

$$
\mathbb{P}\left(\hat{f}^2\geq t^2\right) \leq \frac{\mathbb{E}(\hat{f}^2)}{t^2} = \frac{\mathbb{V}(f)}{t^2} .
$$

 ∎

Note how little was used: positivity of the weights and linearity of the inner product.
Distance controls deviation; Section 12.3 will make high dimension pay for this repeatedly.

The random variable has now been geometrized.
The density has not.

## 12.2 The Simplex

Reverse the roles.
The collection of all densities on $N$ outcomes is a geometric object in its own right — one on which the stochastic matrices of Chapter 9 act, and onto which the neural networks of Chapter 13 will need a smooth map.

**Definition 12.3 (Probability Simplex).** The **probability simplex** on $N$ outcomes is the set

$$
\Delta^{N-1} \,=\, \left\{ \rho\in\mathbb{R}^N \,:\, \rho\geq 0 \ \text{ and }\ \langle \rho,\mathbf{1}\rangle = 1 \right\} ,
$$

where $\rho\geq 0$ is meant entrywise and the inner product is the standard one.
The superscript records its dimension.

> *FIGURE:* [$\Delta^0$ a point in $\mathbb{R}^1$; $\Delta^1$ a segment joining $(1,0)^T$ and $(0,1)^T$; $\Delta^2$ a triangle in $\mathbb{R}^3$ with vertices at the standard basis vectors, floating in the plane $\langle\rho,\mathbf{1}\rangle=1$.]

Nonnegativity carves out the orthant, a cone: the natural habitat of masses that cannot go negative.
Unit total mass is an affine hyperplane whose normal is an acquaintance — the same $\mathbf{1}$ that spans the constants in Section 12.1.
The simplex is the bounded slice where cone meets hyperplane, a compact, convex, $(N-1)$-dimensional plate suspended in $\mathbb{R}^N$.

Its vertices are the standard basis vectors $\mathbf{e}_1,\ldots,\mathbf{e}_N$: the densities of **certainty**, each placing all mass on a single outcome.
Writing any density in coordinates,

$$
\rho = \sum_{j=1}^N \rho_j\,\mathbf{e}_j ,
$$

exhibits it as a convex combination of certainties: a **mixture**, with $\rho$ serving as its own list of mixture weights.
The **relative interior** — the interior taken within the hyperplane the simplex spans, since as a plate in $\mathbb{R}^N$ it has none — holds the densities with every outcome possible, which is precisely where Section 12.1's inner product is positive-definite; the boundary holds the densities that have forbidden something.

Which linear maps send densities to densities?
The answer is a class of matrices already encountered in Chapter 9, there wearing dynamical clothing.

**Lemma 12.4 (Stochastic Matrices Preserve the Simplex).** A matrix $P\in\mathbb{R}^{N\times N}$ maps $\Delta^{N-1}$ into $\Delta^{N-1}$ if and only if $P$ is column-stochastic in the sense of Definition 9.13: entrywise nonnegative, with every column summing to one.

*Proof.* If $P$ preserves the simplex, it must in particular send vertices to densities; and $P\mathbf{e}_j$ is the $j$th column of $P$.
Each column is therefore nonnegative with unit sum.
Conversely, suppose the columns are densities.
Nonnegative entries acting on nonnegative entries keep $P\rho\geq 0$, while unit column sums say exactly that $P^T\mathbf{1}=\mathbf{1}$, whence

$$
\langle P\rho,\mathbf{1}\rangle = \langle \rho, P^T\mathbf{1}\rangle = \langle\rho,\mathbf{1}\rangle = 1 ,
$$

by the adjoint identity of Chapter 5. ∎

Conservation of mass is thus an adjoint equation: $P^T\mathbf{1}=\mathbf{1}$, the eigenvector of Lemma 9.15, is the hyperplane's normal held fixed.
The Markov chains of Section 9.4 now stand revealed as dynamics confined to a compact convex plate: every trajectory $\rho, P\rho, P^2\rho,\ldots$ remains in the simplex forever, and the convergence theorem of Chapter 9 (Theorem 9.16) is convergence within $\Delta^{N-1}$ to the fixed point that Perron-Frobenius theory (Theorem 9.6) stations in it.

One more map belongs to this geography.
Machine learning systems routinely produce a vector of raw scores in $\mathbb{R}^N$  — one score per outcome, unconstrained in sign and size — yet what the task demands is a density: a lawful point of the simplex.
The passage from scores to beliefs should be smooth, since Chapter 13 must differentiate through it, and it should preserve the ranking of the scores.

**Definition 12.5 (Softmax).** The **softmax** map $\operatorname{softmax}:\mathbb{R}^N\rightarrow\Delta^{N-1}$ sends a vector of scores $\mathbf{z}$ to the density

$$
\operatorname{softmax}(\mathbf{z}) \,=\, \left.\textrm{exp}(\mathbf{z})\right/{\displaystyle\sum_{i=1}^N e^{z_i}} ,
$$

where the exponential $\textrm{exp}(\mathbf{z})_i = e^{z_i}$ is computed componentwise.

The entries are positive and sum to one by construction, so softmax lands in the relative interior of the simplex: no outcome is ever entirely ruled out.
The map is smooth, and the exponential is strictly increasing, so the ordering of the scores survives.
Note how the diagonal returns: since a common shift multiplies every exponential by the same factor,

$$
\operatorname{softmax}(\mathbf{z} + c\mathbf{1}) = \operatorname{softmax}(\mathbf{z}) ,
$$

softmax is blind to the component of $\mathbf{z}$ along $\mathbf{1}$.
It factors through the quotient $\mathbb{R}^N/\operatorname{span}\{\mathbf{1}\}$, collapsing exactly one dimension — which is just as well, since the target has dimension $N-1$.
On that quotient, softmax loses nothing at all: the entrywise logarithm recovers the scores up to an additive constant, making softmax a smooth bijection from $\mathbb{R}^N/\operatorname{span}\{\mathbf{1}\}$ onto the relative interior of the simplex.
Chapter 3 supplied the name for this quotient: $\operatorname{span}\{\mathbf{1}\}$ is the kernel of the centering map of Section 12.1, and $\mathbb{R}^N/\operatorname{span}\{\mathbf{1}\}$ is its coimage — the space of scores as softmax actually sees them.

What softmax cannot do is reach the boundary.
The hard maximum — send $\mathbf{z}$ to the vertex of its largest coordinate, when that coordinate is unique — is what the name "softmax" softens: a discontinuous jump between vertices becomes a smooth glide through the interior.
Stretching the scores, $\mathbf{z}\mapsto t\mathbf{z}$ with $t$ large, drives $\operatorname{softmax}(t\mathbf{z})$ toward the winning vertex without ever arriving; shrinking them, $t\rightarrow 0^+$, flattens the output toward the uniform density at the simplex's center.
*Certainty lies at infinity.*

> *Foreshadowing:* The scale of the scores thus decides how sharp the belief: too large, and softmax saturates near a vertex where its derivatives vanish; too small, and it commits to nothing.
> How large the inputs to softmax naturally grow will become a matter of consequence in Chapter 13 — and Section 12.3 builds the tool that predicts their size.

The simplex in low dimension is a comfortable object: interval, triangle, tetrahedron.
The temptation is to believe that its higher-dimensional kin — and high-dimensional geometry — are inductively similar.
They are not.

## 12.3 High Dimension & Near-Orthogonality

Choose two directions at random in the plane, and the angle between them promises nothing: every separation from $0$ to $180^\circ$ arrives alike.
Choose two directions at random in $\mathbb{R}^{1000}$, and the outcome is all but scripted: they meet at a nearly-right angle, almost every time.
Nothing in dimension two or three prepares one for this, which is precisely why it must be computed rather than intuited.

A **random unit vector** in $\mathbb{R}^n$ is a point drawn from the unit sphere with uniform density; expectations over that density are surface integrals, per this chapter's continuous transcription.
The inner product below is the standard one — probability enters through the randomness of the vectors, not through a weight.
When two vectors are random and independent, rotating coordinates holds one of them still without disturbing the law of the other, so nothing is lost in fixing one.

**Lemma 12.6 (Random Inner Products).** For $\mathbf{u}\in\mathbb{R}^n$ a fixed unit vector and $\mathbf{v}$ a random unit vector,

$$
\mathbb{E}\langle\mathbf{u},\mathbf{v}\rangle \,=\, 0
    \qquad\text{and}\qquad
    \mathbb{V}\langle\mathbf{u},\mathbf{v}\rangle \,=\, \frac{1}{n} .
$$

*Proof.* Symmetry does nearly all the work.
Negating the $i$th coordinate of $\mathbb{R}^n$ preserves the sphere and its uniform density while negating $v_i$, so $\mathbb{E}(v_i)=0$; the same reflection negates $v_iv_j$ for $j\neq i$, so $\mathbb{E}(v_iv_j)=0$.
Permuting coordinates shows that the numbers $\mathbb{E}(v_i^2)$ are all equal, and since $\sum_i v_i^2=1$ at every outcome — not merely on average — linearity of expectation, which asks no independence of these chained coordinates, forces $\mathbb{E}(v_i^2)=1/n$.
Expanding the inner product,

$$
\mathbb{E}\langle\mathbf{u},\mathbf{v}\rangle = \sum_i u_i\,\mathbb{E}(v_i) = 0
    \qquad
    \mathbb{V}\langle\mathbf{u},\mathbf{v}\rangle = \sum_{i,j} u_i u_j\,\mathbb{E}(v_iv_j) = \sum_i u_i^2\,\mathbb{E}(v_i^2) = \frac{1}{n} .
$$

 ∎

> *Think:* Dimension three is the last innocent dimension.
> There, the cosine of a random angle distributes uniformly over $[-1,1]$ — Archimedes' hat-box theorem — and the variance of that uniform distribution is exactly $1/3$, confirming the lemma.
> The crowding toward zero begins at $n=4$ and never relents.

For unit vectors, $\langle\mathbf{u},\mathbf{v}\rangle=\cos\theta$ (Section 5.2), so the lemma says that the random cosine has mean zero and standard deviation $1/\sqrt{n}$.
Chebyshev's inequality (Lemma 12.2) converts the shrinking standard deviation into a verdict about angles:

$$
\mathbb{P}\left(\left|\cos\theta\right| \geq t\right) \,\leq\, \frac{1}{n\,t^2} .
$$

In $\mathbb{R}^{1000}$, take $t=1/10$: with probability at least $9/10$, two randomly chosen directions satisfy $|\cos\theta|\leq 1/10$, placing $\theta$ within $6^\circ$ of a right angle.
In dimension one thousand, perpendicularity is not one option among a continuum; it is the overwhelming default.

> *Nota bene:* Chebyshev is honest but miserly.
> The true probability of straying beyond $6^\circ$ here is closer to two in a thousand; a sharper instrument arrives momentarily.

Exact orthogonality, meanwhile, remains as scarce as ever: $\mathbb{R}^n$ accommodates $n$ mutually orthogonal directions and not one more.
Relax exactness to near-orthogonality, and the ceiling does not so much rise as vanish.
Certifying this takes a tail sharper than Chebyshev's, asserted rather than built: for a fixed unit vector $\mathbf{u}$ and a random unit vector $\mathbf{v}$ in $\mathbb{R}^n$, as in Lemma 12.6,

$$
\mathbb{P}\left(\left|\langle\mathbf{u},\mathbf{v}\rangle\right| \geq t\right) \,\leq\, 2\,e^{-n t^2/2} ,
$$

and one elementary bound besides.

**Lemma 12.7 (Union Bound).** For any events $A_1,\ldots,A_m$,

$$
\mathbb{P}\left(A_1\cup\cdots\cup A_m\right) \,\leq\, \sum_{k=1}^m \mathbb{P}(A_k) .
$$

*Proof.* Outcome-by-outcome, $\mathbf{1}_{A_1\cup\cdots\cup A_m}\leq\mathbf{1}_{A_1}+\cdots+\mathbf{1}_{A_m}$: the left side equals $1$ only where some term on the right already does.
Expectation preserves inequalities and is linear. ∎

Now draw $m$ unit vectors in $\mathbb{R}^n$ independently at random and fix a tolerance $t$.
Each of the fewer than $m^2/2$ pairs strays beyond tolerance with probability at most $2e^{-nt^2/2}$, so the union bound controls the failure of the entire family at once:

$$
\mathbb{P}\left(\text{some pair has } \left|\cos\theta\right|\geq t\right)
    \,\leq\, \frac{m^2}{2}\cdot 2e^{-nt^2/2}
    \,=\, m^2\,e^{-nt^2/2} ,
$$

which stays below one whenever $m< e^{nt^2/4}$.
A failure probability below one means that some draw succeeds.
There exist, therefore, families of nearly $e^{nt^2/4}$ directions in $\mathbb{R}^n$ with every pair within $t$ of perpendicular: not linearly many but exponentially many, found by no construction cleverer than blind chance — the **probabilistic method**, in its plainest costume.

In $\mathbb{R}^{1024}$ with $t=0.22$, the bound licenses $m\approx 2\times 10^5$: two hundred thousand directions in a space of dimension $1024$, each within $13^\circ$ of a right angle to all the rest.
That is the size of a working vocabulary, and it is no accident that the language models of Chapter 13 store their word embeddings in spaces of just such dimension.
Exact orthogonality would cap the vocabulary at $1024$ words; near-orthogonality shelters a hundred thousand, each one legible against the others through a crosstalk of at most $0.22$.
*In high dimension, almost everything is almost orthogonal.*

> *Terminology:* The machine-learning literature calls this packing **superposition**: a network stores many more features than it has dimensions, paying a small interference tax on each.

Angles are not dimension's only casualty; volume suffers a stranger fate.
Within the unit ball of $\mathbb{R}^n$, the concentric ball of radius $1-\epsilon$ occupies the fraction $(1-\epsilon)^n$ of the volume, since volumes in $\mathbb{R}^n$ scale as the $n$th power of length — and that fraction collapses exponentially.
In $\mathbb{R}^{1000}$, the ball of radius $0.99$ holds less than one part in twenty thousand of the whole: all the rest crowds into a shell of thickness one percent.
The pulp of the high-dimensional orange is in its peel.

> *FIGURE:* [The unit ball with a thin outer shell shaded; annotation that for $n=1000$, $\epsilon=0.01$, the shell holds $99.996\%$ of the volume.]

One might suspect the sphere of engineering this concentration; the Gaussian acquits it.
Let $\mathbf{g}\in\mathbb{R}^n$ have independent standard normal coordinates, with density proportional to $e^{-\|\mathbf{x}\|^2/2}$ — the bell centered at the origin, and maximal there.
Where do its samples actually land?
The squared length $\|\mathbf{g}\|^2=\sum_i g_i^2$ is a sum of $n$ independent random variables, each of mean $1$ and variance $2$, so $\mathbb{E}\left(\|\mathbf{g}\|^2\right)=n$ while independence sums the variances to $2n$, and Chebyshev does the rest: in $\mathbb{R}^{1000}$, at least nineteen samples in twenty have length between $28$ and $35$, hugging $\sqrt{1000}\approx 31.6$.
The peak of the density sits at the origin; the samples are nowhere near it, exiled to a thin shell of radius $\sqrt{n}$.

> *Think:* No paradox survives inspection: mass is density times volume, the shell at radius $r$ carries volume growing like $r^{n-1}$, and the product $r^{n-1}e^{-r^2/2}$ peaks near $r=\sqrt{n}$.
> The origin wins the density contest and loses the volume contest, badly.

> *Caveat:* Distances concentrate too: independent Gaussian samples sit near $\sqrt{2n}$ from one another, so the contrast between nearest and farthest neighbor dwindles as $n$ grows.
> The semantic search of Example 5.16 swims against this current, one reason dimension reduction (Chapter 10, and Section 12.5 to come) precedes it in practice.

The $\sqrt{n}$ shell settles unfinished business from Chapter 11.
The Mahalanobis distance (Definition 11.9) measures deviation in units of the data's own variability, and Section 11.5 counseled investigating any observation farther than twice typical.
Audit it: the standardized vector $\mathbf{y}=[C]^{-1/2}(\mathbf{x}-\bar{\mathbf{x}})$ has mean zero and identity covariance, so $d_M^2=\|\mathbf{y}\|^2$ has expectation $d$ whatever the distribution of the data.

> *Recall:* $[C]^{-1/2}$ inverts the positive square root of Exercise 8 of Chapter 10: diagonalize $[C]$ orthogonally and take square roots along the diagonal.
> Positive definiteness leaves only one such root.

A typical observation sits at Mahalanobis distance $\sqrt{d}$: the shell, again.
For Gaussian data the shell computation applies verbatim, giving $d_M^2$ mean $d$ and variance $2d$, so an honest alarm threshold is $d_M^2 \geq d+3\sqrt{2d}$, growing like $d+O(\sqrt{d})$ and not like a multiple of $d$.
"Twice typical" means $d_M^2\approx 4d$, a full $3\sqrt{d/2}$ standard deviations out — about five when $d=5$, twenty-one when $d=100$ — a threshold that would sleep through most anomalies worth waking for.
The flagged reading of Example 11.10, at $d_M^2=24$ against a mean of $5$, stands six standard deviations out: that alarm was sound.

> *Nota bene:* Statisticians know the distribution of $\|\mathbf{y}\|^2$ for Gaussian $\mathbf{y}$ as **chi-squared** with $d$ degrees of freedom; its tail decays exponentially, so tabulated cutoffs sharpen considerably the guarantee Chebyshev offers at three standard deviations, namely $\mathbb{P}\leq 1/9$.

The same bookkeeping sizes an inner product, and Chapter 13 will need the answer.
For independent standard Gaussian vectors $\mathbf{g},\mathbf{h}\in\mathbb{R}^n$, the score $\langle\mathbf{g},\mathbf{h}\rangle$ has mean zero and variance $\sum_i\mathbb{E}(g_i^2)\,\mathbb{E}(h_i^2)=n$.
Raw inner products of generic $n$-dimensional vectors are not small: they are of size $\sqrt{n}$, growing with the dimension even when nothing is correlated with anything.
Any construction that feeds such scores to an exponential, as softmax does (Definition 12.5), courts saturation unless it first divides by $\sqrt{n}$.

Similarity scores obey the same discipline.
How large must a cosine be in order to mean anything?
Lemma 12.6 answers that the question is incomplete until the dimension is named, since chance alone spreads the cosines of unrelated vectors across a band of width $1/\sqrt{n}$ about zero.
A cosine of $0.2$ is unremarkable in $\mathbb{R}^3$, where random pairs manage it four times in five; in $\mathbb{R}^{1024}$ it stands more than six standard deviations above chance.
The same number is noise in one space and a verdict in the other.

One habitat of randomness remains: the matrix.
High dimension, so lawful about angles and lengths, is no less lawful about spectra.

## 12.4 Random Matrices & the Noise Floor

Let the data matrix $\mathcal{X}\in\mathbb{R}^{n\times d}$ contain no data at all: fill its entries with independent samples of pure noise — mean zero, variance one, Gaussian for definiteness — and, supposing $n\geq d$, compute its singular values as Chapter 11 would.
The population covariance is the identity, no direction of feature space preferred over any other, so a first instinct expects a flat spectrum: every singular value testifying to the same nothing.
The instinct half-survives.

The sound half needs nothing beyond Section 12.1.
The total spectral mass is the Frobenius norm,

$$
\sum_{i=1}^{d}\sigma_i^2 \,=\, \left\|\mathcal{X}\right\|_F^2 \,=\, \sum_{i,j} x_{ij}^2 ,
$$

a sum of $nd$ independent random variables of mean $1$ and variance $2$ — the bookkeeping of the Gaussian shell in Section 12.3 — so Chebyshev confines it near $nd$.

> *Caution:* $\sigma(f)$ has been a standard deviation since Section 12.1; the subscripted $\sigma_i$ are, as ever, singular values.
> The parenthesis marks the difference.

The $d$ singular values share a squared mass of $nd$, whence $\sigma_i^2\approx n$ on average: the typical singular value of pure noise has size $\sqrt{n}$.
In covariance terms the instinct is vindicated on average — the eigenvalues $\sigma_i^2/n$ of $\frac{1}{n}\mathcal{X}^T\mathcal{X}$ average one, exactly as the identity demands.
The spread is another matter, and the noise floor is not at zero: it stands at $\sqrt{n}$, and it rises with every additional observation.

What the mass computation cannot deliver is how the singular values arrange themselves about $\sqrt{n}$ — huddled or straggling.
The shape is asserted.
As $n$ and $d$ grow with the aspect ratio $\gamma=d/n\leq 1$ held fixed, the singular values of pure noise crowd into the interval

$$
\sqrt{n}\left(1-\sqrt{\gamma}\right) \;\leq\; \sigma_i \;\leq\; \sqrt{n}\left(1+\sqrt{\gamma}\right) ,
$$

filling it with a definite limiting density: the **Marchenko-Pastur law**.
The filled interval is called the **bulk** and its endpoints the **edges**, and the crowding is strict in the limit — with probability approaching one, no singular value strays outside by any fixed margin.
Squareness is the worst case: at $\gamma=1$ the lower edge touches zero, so noise alone manufactures near-singularity, as any engineer who has inverted a measured matrix has felt.
The width of the bulk is governed entirely by $\sqrt{\gamma}=\sqrt{d/n}$: more variables per observation, a fatter bulk.
Section 11.5's warning that too few observations relative to variables create spurious apparent structure is this law, drawn to scale.

> *Nota bene:* The law is indifferent to the fine print of the noise: independent entries of mean zero and variance one — Gaussian, uniform, coin flips — produce the same bulk in the limit.
> High dimension forgets the distribution and keeps its first two moments; the Gaussian merely exemplifies.

The numbers rebuke the eye.
Take $n=1000$ observations of $d=100$ variables, a ratio of ten observations per variable that practitioners consider comfortable, so that $\gamma=1/10$.
The bulk runs from $0.68\sqrt{n}$ to $1.32\sqrt{n}$: the largest singular value of pure noise stands nearly double the smallest.
In covariance terms, the eigenvalue estimates range from $0.47$ to $1.73$ about a true value of $1$, and an eye hunting through them for structure will find it — a leading eigenvalue seventy-three percent above truth, a trailing one less than half of it, a graceful decay between — all of it reproducible from one noise draw to the next, none of it signal.
Sampling error has a shape.

Now add signal.
Under the working hypothesis of Chapter 11, where genuine structure of low rank lies wrapped in noise, the noise contributes its bulk regardless, and the fate of each true component is decided at the upper edge.
A component strong enough to push its singular value past $\sqrt{n}(1+\sqrt{\gamma})$ stands clear of the bulk, detected, its singular vector acquiring a definite overlap with the true direction.
A component too weak to clear the edge is swallowed: its singular value joins the crowd, and — the harsher fact — its singular vector forgets the true direction almost entirely.
Below the edge, detection is not merely difficult; in the large-$n$ limit it is impossible.
*Signal is what noise cannot counterfeit.*

> *Nota bene:* The threshold is exact, and crossing it is a phase transition.
> Beneath it, detection does not degrade gracefully; it switches off.
> Above it the overlap is at first faint, and nears true alignment only well clear of the edge.

The scree plots of Section 11.5 can now be read against a standard rather than by instinct.
The bridge of Example 11.11 dropped sharply after two components, and the drop was legible by eye; the reactor of Example 11.12 decayed gradually, and the section could offer only cross-validation and caution.
The noise floor supplies what the eye could not: an absolute reference, indifferent to wishful reading — estimate the noise scale, place the edge at $\sqrt{n}(1+\sqrt{\gamma})$ times it, and grant no belief to any component beneath, where a singular value is not evidence but arithmetic.
An adversary this predictable can be conscripted.

## 12.5 Random Projection

Data in bulk is geometry in bulk.
A library of images, a corpus of documents, a vocabulary of embeddings: $m$ points in $\mathbb{R}^n$, with $m$ running to the millions while $n$ runs to the thousands, and downstream of them algorithms — nearest-neighbor search, clustering, retrieval — that consume nothing of the points beyond their mutual distances and angles.
Every such distance costs $n$ operations to read and every point costs $n$ numbers to keep, so the engineering question is how far the dimension can be lowered before the geometry deforms beyond tolerance.
Fill the projection with noise.

**Definition 12.8 (Random Projection).** A **random projection** from $\mathbb{R}^n$ to $\mathbb{R}^k$ is the linear map $\mathbf{x}\mapsto\Phi\mathbf{x}$ given by a matrix $\Phi\in\mathbb{R}^{k\times n}$ with independent mean-zero Gaussian entries of variance $1/k$.

The variance $1/k$ is calibration, not decoration, and the way to see it is row-by-row.
The rows of $\sqrt{k}\,\Phi$ are independent standard Gaussian vectors $\mathbf{g}_1,\ldots,\mathbf{g}_k$ in $\mathbb{R}^n$  — the species whose lengths and scores Section 12.3 sized — so that

$$
\left\|\Phi\mathbf{x}\right\|^2 \,=\, \frac{1}{k}\sum_{i=1}^k \left\langle \mathbf{g}_i,\mathbf{x}\right\rangle^2 .
$$

Each score $\langle\mathbf{g}_i,\mathbf{x}\rangle$ is one blind reading of $\mathbf{x}$ along a random direction, and the squared length of the image is the average of $k$ squared readings.
What that average estimates, and how well, the chapter is now equipped to answer in a few lines.

**Lemma 12.9 (Random Projections Measure Length).** For a fixed vector $\mathbf{x}\in\mathbb{R}^n$ and a random projection $\Phi$ to $\mathbb{R}^k$,

$$
\mathbb{E}\left(\left\|\Phi\mathbf{x}\right\|^2\right) = \left\|\mathbf{x}\right\|^2
    \qquad\text{and}\qquad
    \mathbb{V}\left(\left\|\Phi\mathbf{x}\right\|^2\right) = \frac{2}{k}\left\|\mathbf{x}\right\|^4 .
$$

*Proof.* The Gaussian density is a function of length alone, hence blind to rotation — the same symmetry that held one vector still in Lemma 12.6 — so a rotation carrying $\mathbf{x}/\|\mathbf{x}\|$ onto the first coordinate axis shows that each score $\langle\mathbf{g}_i,\mathbf{x}\rangle$ has the law of $\|\mathbf{x}\|\,g$ for a single standard normal $g$.
Its square then has mean $\|\mathbf{x}\|^2$ and variance $2\|\mathbf{x}\|^4$, since $g^2$ has mean $1$ and variance $2$: the bookkeeping of the Gaussian shell.
Averaging the $k$ independent readings preserves the mean by linearity, while independence adds the variances against the $k^2$ of the average:

$$
\mathbb{V}\left(\left\|\Phi\mathbf{x}\right\|^2\right) \,=\, \frac{k\cdot 2\|\mathbf{x}\|^4}{k^2} \,=\, \frac{2}{k}\left\|\mathbf{x}\right\|^4 .
$$

 ∎

The lemma says more than it computes: a random projection is a measuring instrument.
The variance of the average falls like $1/k$, so the instrument sharpens as rows accumulate.
Chebyshev's inequality (Lemma 12.2) converts variance into guarantee:

$$
\mathbb{P}\left( \left|\, \|\Phi\mathbf{x}\|^2 - \|\mathbf{x}\|^2 \,\right| \,\geq\, \epsilon\,\|\mathbf{x}\|^2 \right)
    \,\leq\, \frac{2}{k\,\epsilon^2} .
$$

Observe what the bound omits: $n$.
Fidelity is governed by $k$ alone, the number of readings taken.

One length is a modest prize; linearity multiplies it.
For any two points of a cloud, $\Phi\mathbf{x}_i-\Phi\mathbf{x}_j = \Phi(\mathbf{x}_i-\mathbf{x}_j)$, so every pairwise distance of the projected cloud is the measured length of a difference vector, and a cloud of $m$ points has fewer than $m^2/2$ differences to guard.
Guarding them all at once is the office of the union bound (Lemma 12.7), and here Chebyshev falters: with each pair straying at rate $2/(k\epsilon^2)$, the combined failure stays below one only for $k$ beyond $m^2/\epsilon^2$, which for a million points at tolerance one quarter means sixteen trillion dimensions.
That is no longer a projection; it is an ascent.

> *Think:* The proof is Chebyshev's own idea promoted: apply Markov's inequality not to $\hat{f}^2$ but to $e^{\lambda f}$, then choose $\lambda$ shrewdly.

The remedy is already on record.
For the unit vector $\mathbf{u}=\mathbf{x}/\|\mathbf{x}\|$, the sum $k\,\|\Phi\mathbf{u}\|^2 = \sum_i \langle\mathbf{g}_i,\mathbf{u}\rangle^2$ collects $k$ independent squared standard normals: precisely the chi-squared distribution with $k$ degrees of freedom met in the margin of Section 12.3, whose tail was there recorded as exponential.
Stated precisely, for $0<\epsilon<1$,

$$
\mathbb{P}\left( \left|\, \|\Phi\mathbf{x}\|^2 - \|\mathbf{x}\|^2 \,\right| \,\geq\, \epsilon\,\|\mathbf{x}\|^2 \right)
    \,\leq\, 2\,e^{-k\epsilon^2/12} .
$$

Exponential decay in $k$ is the hinge of everything that follows: it converts a head-count of $m^2/2$ pairs into a requirement that grows only like $\ln m$.

**Theorem 12.10 (Johnson-Lindenstrauss).** Let $\mathbf{x}_1,\ldots,\mathbf{x}_m$ be any collection of points in $\mathbb{R}^n$, let $0<\epsilon<1$, and let $\Phi$ be a random projection to $\mathbb{R}^k$ with

$$
k \,\geq\, \frac{36\,\ln m}{\epsilon^2} .
$$

Then, with probability at least $1-1/m$, every pair of points satisfies

$$
(1-\epsilon)\left\|\mathbf{x}_i-\mathbf{x}_j\right\|^2
    \;\leq\; \left\|\Phi\mathbf{x}_i-\Phi\mathbf{x}_j\right\|^2
    \;\leq\; (1+\epsilon)\left\|\mathbf{x}_i-\mathbf{x}_j\right\|^2 .
$$

*Proof.* By linearity, $\Phi\mathbf{x}_i-\Phi\mathbf{x}_j=\Phi(\mathbf{x}_i-\mathbf{x}_j)$, so each pair fails its inequality only if the measured length of its difference vector strays beyond tolerance, an event of probability at most $2e^{-k\epsilon^2/12}$.
The union bound totals the fewer than $m^2/2$ failures:

$$
\mathbb{P}\left(\text{some pair strays}\right)
    \;\leq\; \frac{m^2}{2}\cdot 2\,e^{-k\epsilon^2/12}
    \;\leq\; m^2\,e^{-3\ln m}
    \;=\; \frac{1}{m} .
$$

 ∎

Run the numbers against the earlier appetite.
A million points at tolerance one quarter: the theorem asks $k\geq 36\ln(10^6)/(1/4)^2\approx 8000$, eight thousand dimensions carrying the complete pairwise geometry of a million points, whatever dimension they came from — the theorem never asks.
A billion points in place of a million multiplies the requirement by $3/2$, since only the logarithm grows.
Chebyshev wanted trillions; the exponential tail asks thousands.
Nor do distances travel alone: the polarization identity $4\langle\mathbf{x},\mathbf{y}\rangle = \|\mathbf{x}+\mathbf{y}\|^2-\|\mathbf{x}-\mathbf{y}\|^2$ writes every inner product as a difference of squared lengths, so enlarging the union to include the sums $\mathbf{x}_i+\mathbf{x}_j$, which merely doubles the count, carries inner products, angles, and cosine similarities along with distortion of the same order.
This is the reduction toward which Section 12.3's caveat pointed: the semantic search of Example 5.16 may project its library once, then run every subsequent comparison in $\mathbb{R}^k$, within tolerance of every original cosine.

> *Nota bene:* The Gaussian is a convenience, not a necessity: entries drawn as fair coin flips $\pm 1/\sqrt{k}$ obey the same theorem with adjusted constants — **database-friendly** projections, all additions and subtractions.
> High dimension keeps the first two moments and forgets the rest, exactly as with the noise bulk.

What ought to astonish is less the size of $k$ than the ignorance of $\Phi$.
The matrix is drawn without a glance at the data, and could be drawn before the data exists at all.
One draw serves whatever cloud arrives, with the theorem's full guarantee.
Set this against the reigning practice of Chapter 11, which looks before it projects.
When the cloud hugs a low-dimensional subspace, PCA finds that subspace and compresses to the effective rank, far below any $\ln m$, its axes interpretable as principal directions, and Theorem 11.6 certifies that no rank-$k$ map reconstructs the data more faithfully.
Random projection reconstructs nothing — from $\mathbb{R}^k$ there is no way back — and its coordinates mean nothing one at a time; what it guarantees is every pairwise distance of every cloud, structured or structureless, for the cost of one matrix multiplication.
Adaptive optimality or oblivious universality: the SVD when one can afford to look, chance when one cannot.

Randomness has changed station.
It entered as the adversary — counterfeiter of structure, swallower of weak signal — and it stands now as an instrument: blind, cheap, and honest about every distance in its care.
Nor is the instrument confined to clouds of points.
A matrix is a cloud of columns.
*Almost every shadow is faithful.*

## 12.6 The Randomized SVD

The last conscription aims highest: at the singular value decomposition itself.
For the data matrices of Chapter 11 the need is chronic, since a matrix $A\in\mathbb{R}^{n\times d}$ with millions of rows and tens of thousands of columns puts the constructions of Chapter 10 out of reach — the full decomposition costs on the order of $nd\cdot\min(n,d)$ operations — while everything actually wanted from it is a truncation: the top $k$ singular triples, with $k$ in the dozens (Theorem 11.6).

Send one blind probe through $A$: for $\mathbf{\omega}\in\mathbb{R}^d$ with independent standard normal entries, the singular value decomposition $A=\sum_i \sigma_i\mathbf{u}_i\mathbf{v}_i^T$ expands the image as

$$
A\mathbf{\omega} \,=\, \sum_i \sigma_i\,\langle\mathbf{v}_i,\mathbf{\omega}\rangle\,\mathbf{u}_i
    \,=\, \sum_i \sigma_i\,g_i\,\mathbf{u}_i ,
$$

where the coefficients $g_i=\langle\mathbf{v}_i,\mathbf{\omega}\rangle$ are independent standard normals: the $\mathbf{v}_i$ are orthonormal, and the Gaussian is blind to rotation, exactly as in the proof of Lemma 12.9.
This display is the entire idea.
The probe returns a random mixture of the left singular vectors in which each direction speaks at its native volume $\sigma_i$.

Now stack $k+p$ probes as the columns of a matrix $\Omega\in\mathbb{R}^{d\times(k+p)}$ — a random projection in spirit, though the calibration of Definition 12.8 is unnecessary where only a range will be kept — and form the **sketch**

$$
Y \,=\, A\,\Omega \,\in\, \mathbb{R}^{n\times(k+p)} .
$$

Its columns are $k+p$ independent mixtures of the $\mathbf{u}_i$, every one of them favoring the directions of large $\sigma_i$, and their common span captures the dominant left singular subspace with room to spare: the $p$ surplus probes guard against the occasional whispered coefficient, and failure probabilities collapse at the rate $p^{-p}$.

The rest is Chapter 10 in miniature.
Orthonormalize the sketch (Gram-Schmidt, Chapter 5) into $Q\in\mathbb{R}^{n\times(k+p)}$; compress $A$ into the sketched frame as $B=Q^TA$, a matrix of only $k+p$ rows; take the exact singular value decomposition $B=\tilde{U}\Sigma V^T$, now affordable; and reassemble:

$$
A \,\approx\, QQ^TA \,=\, QB \,=\, \left(Q\tilde{U}\right)\Sigma\,V^T .
$$

The left-hand approximation is an orthogonal projection — each column of $A$ cast onto the sketched subspace, in the manner of Chapter 6 — and the right-hand side is a genuine singular value decomposition.
The whole computation touches $A$ twice, once to sketch and once to compress, for a total of about $nd(k+p)$ operations: cheaper than the full decomposition by a factor of $\min(n,d)/(k+p)$, often a hundredfold and more.
Chance finds the range; algebra does the rest.

> *BONUS!* Blind probes estimate more than ranges.
> For $\mathbf{\omega}$ with independent mean-zero, variance-one entries and any square matrix $M$, expanding $\mathbb{E}\left(\mathbf{\omega}^TM\mathbf{\omega}\right)=\sum_{i,j}m_{ij}\,\mathbb{E}(\omega_i\omega_j)=\sum_i m_{ii}$ shows $\mathbf{\omega}^TM\mathbf{\omega}$ to be an unbiased estimate of $\operatorname{tr} M$ — invaluable when $M$ is too large to form and exists only as a subroutine.

How much does the sketch forfeit?
The benchmark is absolute — no rank-$k$ approximation, however carefully built, improves on $\sigma_{k+1}$ (Theorem 11.6) — and the sketch comes within a computable factor of it.

**Theorem 12.11 (Randomized Range Finder).** Let $A\in\mathbb{R}^{n\times d}$, let $k\geq 2$ be a target rank, and let $p\geq 2$ be an oversampling parameter with $k+p\leq\min(n,d)$.
For $\Omega\in\mathbb{R}^{d\times(k+p)}$ standard Gaussian and $Q$ an orthonormal basis for the range of $A\Omega$,

$$
\mathbb{E}\left\|A - QQ^TA\right\|_2
    \,\leq\, \left(1 + \frac{4\sqrt{k+p}}{p-1}\cdot\sqrt{\min(n,d)}\right)\sigma_{k+1} .
$$

> *Caveat:* The factor $\sqrt{\min(n,d)}$ is the analysis's caution rather than the algorithm's habit: observed errors ordinarily sit within a small multiple of $\sigma_{k+1}$, and the guarantee in expectation upgrades to overwhelming probability.

Two remarks translate the theorem into practice.
First, the guarantee is relative to $\sigma_{k+1}$, and Section 12.4 appraised $\sigma_{k+1}$ exactly: under the low-rank-plus-noise hypothesis of Chapter 11, everything below the top $k$ sits at the noise floor, so the sketch loses only what the noise floor had already condemned.
Second, when the spectrum decays too gradually for comfort, as in the reactor of Example 11.12 rather than the bridge of Example 11.11, the remedy is iteration.
Sketch not $A$ but $(AA^T)^qA$, whose singular vectors are identical and whose singular values are $\sigma_i^{2q+1}$: the dominance of Section 9.2, put to work wholesale, at the cost of $2q$ further passes over $A$.
The bracket of the theorem, dimensional factor and all, then enters only through its $(2q+1)$st root — a factor of one thousand at $q=0$ falls below four at $q=2$ — so that even slow spectra yield to a handful of passes.

The chapter's instruments were all drawn from one urn: independent entries, mean zero, variance calibrated.
So, before training, are the neural networks of Chapter 13.
An untrained network's weight matrices are initialized as pure noise, their variance set to the reciprocal of the layer's width so that a passing signal keeps its scale in expectation — Lemma 12.9 exactly when the layer is square, and adjusted by a fan-in convention when the widths disagree; rediscovered by engineers as the condition for a trainable start.
Everything this chapter established therefore describes a newborn network exactly: its spectra pool in the Marchenko-Pastur bulk, and its features are not yet distinguishable from the counterfeits of Section 12.4.
*Every network is born at the noise floor.*

—

## The Market Mode

Take the daily returns of the several hundred stocks in a broad index, standardize each to zero mean and unit variance, and stack them as the columns of a matrix $\mathcal{X}\in\mathbb{R}^{T\times N}$: $N$ stocks watched over $T$ trading days.
The empirical correlation matrix

$$
[R] = \frac{1}{T}\mathcal{X}^T\mathcal{X} \in \mathbb{R}^{N\times N}
$$

records how every pair of stocks moves together, its $(i,j)$ entry the cosine of the angle between two centered return vectors: the correlation of Section 12.1, computed $N^2$ times over.
The matrix is symmetric, so the Spectral Theorem (Theorem 10.1) furnishes an orthonormal basis of eigenvectors and real eigenvalues, and the portfolio theory of Chapter 11 would read the leading ones as the market's true factors.
Which of them to believe is the question, and Section 12.4 has already answered it in the negative.
Were the returns pure noise — $N$ independent walks, no stock more kin to another than chance allows — the eigenvalues of $[R]$ would not scatter at random; they would crowd into the Marchenko-Pastur bulk $[(1-\sqrt{\gamma})^2,\,(1+\sqrt{\gamma})^2]$ with aspect ratio $\gamma=N/T$.
For some four hundred stocks over five years of days, $\gamma\approx 0.31$ and the upper edge sits near $2.4$.

Laid against that band, the empirical spectrum tells a stark story.
One eigenvalue stands near $85$ — thirty-five times the edge, a fifth of the total variance by itself — and its eigenvector is entirely positive and very nearly uniform, $[\mathbf{v}_1]_j\approx 1/\sqrt{N}$: every stock loaded the same way, rising and falling as one.
This is the **market mode**, the tide under all the boats.
Below it a handful more, half a dozen or so, clear the upper edge, and their eigenvectors split the market into recognizable sectors: technology against energy, industry against retail.
Beneath those, ninety-four of every hundred eigenvalues lie inside the bulk, where the theory of Section 12.4 forbids us to distinguish them from the spectrum of noise.

> That most of a market's correlation spectrum is indistinguishable from noise is the finding of Laloux, Cizeau, Bouchaud, and Potters, who named it *noise dressing*: some ninety-four percent of the eigenvalues of a real correlation matrix fall inside the bulk, the market mode and a few sectors alone standing clear.

The believable content of such a matrix is therefore not the matrix but a subspace: the span of the few eigenvectors that clear the noise floor, a handful of dimensions carrying the market and its sectors.
Everything orthogonal to that span is dressing — reproducible in shape from any draw of noise, and genuine in none of it.

This is worse than academic, for the classical minimum-variance portfolio weights the stocks by $[R]^{-1}\mathbf{1}$, and inversion is where noise does its worst.
$[R]^{-1}$ scales each eigendirection by the reciprocal of its eigenvalue, so it pours almost all of its weight onto the smallest eigenvalues — the very floor of the bulk, the least trustworthy directions there are.
The matrix is consulted most confidently exactly where it knows least.
A smallest eigenvalue near $0.14$ against a largest near $85$ makes the condition number of Chapter 1 some six hundred, and the optimizer, handed $[R]^{-1}$, trusts the noise above all else.

The repair is to trust the subspace and flatten the rest.
Keep the eigenvalues above the edge with their eigenvectors untouched; replace every eigenvalue inside the bulk by their common average, which holds the trace, and so the total variance, fixed; reassemble.
The cleaned matrix carries the same signal subspace above a level, honest noise floor; its condition number falls from six hundred toward one hundred, and the portfolios it recommends, tried on the returns of the years that follow, run measurably steadier than those the raw matrix proposes.
Nothing was estimated better and no new data gathered: a symmetric matrix was resolved into eigenspaces, and each was judged against a threshold that noise itself supplied.
What cleared the threshold was kept; what did not was returned to the floor.
*One direction carries the tide; nearly all the rest is dressing.*

—

## The Blessing of Dimensionality

> *Terminology:* The **curse of dimensionality** is Bellman's coinage, minted for the exponential cost of gridding a high-dimensional state space; the countervailing **blessing** is Donoho's.
> Both name the same geography, surveyed in opposite moods.

Every incoming message submits to the same examination.
A spam filter reads mail as a vector in $\mathbb{R}^n$ — word frequencies, header oddities, the hour of sending, standardized to zero mean and unit variance in the manner of Section 11.5 — with $n$ running easily to the thousands, and the two populations sit as the standard idealization places them: Gaussian clouds of identity covariance, centered at $+\mathbf{\mu}$ for spam and $-\mathbf{\mu}$ for legitimate mail.

Distances first, since Section 12.3 lodged the complaint.
Set $\|\mathbf{\mu}\|=1$ and $n=5000$.
Two messages of the same class sit at distance $\sqrt{2n}=100$ from one another, give or take one; a spam and a ham sit farther apart by two hundredths.
The separation between the classes is a whisper fifty times fainter than the fluctuations carrying it, so the identity of a message's nearest neighbor is an accident of noise, and the classifier that consults it — assign each message the class of its closest labeled specimen — misclassifies forty-eight messages in every hundred.
One may as well flip the coin directly.

Now let the filter consult centroids instead of neighbors: assign the message to whichever of $\pm\mathbf{\mu}$ sits closer.
Expanding the two squared distances leaves

$$
\left\|\mathbf{x}-\mathbf{\mu}\right\|^2 - \left\|\mathbf{x}+\mathbf{\mu}\right\|^2
    \,=\, -4\,\langle\mathbf{x},\mathbf{\mu}\rangle ,
$$

and the term $\|\mathbf{x}\|^2$ — every coordinate of noise, all of the concentration — cancels in the comparison, leaving the sign of a single score.
For a spam message $\mathbf{x}=\mathbf{\mu}+\mathbf{g}$, that score $\langle\mathbf{x},\mathbf{\mu}\rangle = \|\mathbf{\mu}\|^2 + \langle\mathbf{g},\mathbf{\mu}\rangle$ has mean $\|\mathbf{\mu}\|^2$ and standard deviation $\|\mathbf{\mu}\|$, and $n$ appears nowhere.
The verdict fails only when a single standard normal overshoots $\|\mathbf{\mu}\|$: probability $0.159$ at $\|\mathbf{\mu}\|=1$, in $\mathbb{R}^2$ and in $\mathbb{R}^{5000}$ alike.
The ambient dimension has vanished from the guarantee, as it vanished in Section 12.5, and for the same reason: one reading, taken along one direction, of a cloud living anywhere.

The subspaces of Chapter 3 say why.
The score $\langle\,\cdot\,,\mathbf{\mu}\rangle$ is a linear functional whose kernel is the hyperplane $\mathbf{\mu}^\perp$, and the splitting

$$
\mathbb{R}^n \,=\, \operatorname{span}\{\mathbf{\mu}\} \boxplus \mathbf{\mu}^\perp
$$

apportions the space with brutal asymmetry: one dimension of signal against $n-1$ dimensions of nuisance.
Squared distance, a sum over all $n$ coordinates, drags the noise of the entire nuisance subspace into every comparison — the curse in mechanism rather than in slogan.
The score annihilates $\mathbf{\mu}^\perp$ outright and hears one coordinate of noise, no more.
High dimension never hurt the problem; it hurt an algorithm that insisted on listening to all of it.

> *Historical Note:* The discriminating direction is Fisher's **linear discriminant** (1936, the iris data), and the centroid rule is **linear discriminant analysis** in its simplest costume.
> Classes of general covariance $[C]$ rotate the axis to $[C]^{-1}(\mathbf{\mu}_+ - \mathbf{\mu}_-)$, a whitening in the spirit of Definition 11.9.

> *Caveat:* The axis must be learned.
> From $m=500$ labeled messages per class at $n=5000$ the centroid difference is mostly error — $\|\hat{\mathbf{\mu}}-\mathbf{\mu}\|\approx 2.2$ against $\|\mathbf{\mu}\|=1$ — yet the error rate climbs only to $0.35$: by Lemma 12.6 the noise lands nearly orthogonal to $\mathbf{\mu}$, diluting the score without redirecting it.

A flat error rate is deliverance, not yet blessing; the blessing arrives when the features are many and each is nearly worthless.
Suppose every coordinate of $\mathbf{\mu}$ is a mere one-twentieth, so that a filter consulting one word alone errs forty-eight times in the hundred — the coin again.
The shifts accumulate in quadrature along the discriminating axis, $\|\mathbf{\mu}\|=\sqrt{n}/20$, and the error now falls with every word admitted: three in ten on a vocabulary of one hundred, six in a thousand on a vocabulary of twenty-five hundred, each new word a witness too timid to testify alone.
No single word can convict; the vocabulary convicts.

The two faces are one law.
Concentration plays no favorites: it presses each measurement onto its expectation, the distance no less than the score, and the fates diverge only in what the expectations remember.
Expected distances barely distinguish friend from foe, so concentration perfects a blur; expected scores are signed by the class, so concentration perfects a verdict.
*The curse and the blessing are one concentration, read by two instruments.*

—

## Exercises: Chapter 12

1. Three outcomes are equally likely.
Take $f=(-1,0,1)^T$ and $g=f^2$, the square taken outcome-by-outcome.
Compute the residuals $\hat{f}$ and $\hat{g}$, then the cosine of the angle between them in the inner product of Definition 12.1.
Compare $\mathbb{P}(f=1)\,\mathbb{P}(g=0)$ against $\mathbb{P}(f=1\text{ and }g=0)$.
Say what feature of $g$ makes the refusal of independence as complete as it could be.

2. On five equally likely outcomes take $f=(-2,-1,0,1,2)^T$.
Run Gram-Schmidt (Section 5.3) on $\mathbf{1}$, $f$, $f^2$ in the inner product of Definition 12.1, and report the resulting orthonormal basis.
Explain why orthogonality to $\mathbf{1}$ leaves the two later basis vectors mean-zero, and therefore uncorrelated with each other.
Compare the third against the Legendre polynomial $P_2$ of Section 5.3, and say what single construction produces both.

3. Take the score vector $\mathbf{z}=(2,1,1,0)^T$ and compute $\operatorname{softmax}(\mathbf{z})$, per Definition 12.5, exactly; the denominator factors.
Exhibit, in the language of Section 3.6, the set of all score vectors that $\operatorname{softmax}$ carries to this same density.
Then compute $\lim_{t\rightarrow\infty}\operatorname{softmax}(t\mathbf{z})$, and say why the tie between the middle scores leaves the limit a vertex all the same.

4. A cloud of $m=50{,}000$ points is to be projected as in Definition 12.8, every pairwise squared distance held within distortion $\epsilon=1/10$.
How many dimensions does Theorem 12.10 demand?
How many at $\epsilon=1/20$?
Determine every ambient dimension $n$ at which the second guarantee compresses nothing.

5. The matrix $A$ below has rank two; the test matrix $\Omega$ is fixed, not random:

$$
A = \begin{bmatrix} 1&1&2\\ 1&-1&0\\ 1&1&2\\ 1&-1&0 \end{bmatrix},
    \qquad
    \Omega = \begin{bmatrix} 1&1\\ 1&-1\\ 0&0 \end{bmatrix} .
$$

Execute the sketch of Section 12.6: form $Y=A\Omega$, orthonormalize its columns into $Q$, compress to $B=Q^TA$, and assemble $QB$.
Report, alongside $\sigma_3$, the error $\|A-QQ^TA\|_2$ that Theorem 12.11 controls for random probes.
Account for the exactness by identifying the subspace the two columns of $Y$ span.

6. Let $\Pi=\Pi_{\mathbf{1}}$ be the orthogonal projection onto $\operatorname{span}\{\mathbf{1}\}$ in the inner product of Definition 12.1, so that centering is $\hat{f}=(I-\Pi)f$.
Show from Lemma 6.7 that

$$
\mathbb{V}(f) \,=\, \left\langle f,\,(I-\Pi)f\right\rangle_\rho
    \qquad\text{for every } f\in\mathbb{R}^N :
$$

the variance is a quadratic form, represented by the self-adjoint operator $I-\Pi$.
Conclude that $\mathbb{V}(f)\geq 0$ always, and that $\mathbb{V}(f)=0$ exactly on $\operatorname{ker}(I-\Pi)=\operatorname{span}\{\mathbf{1}\}$: the random variables of zero variance are the constants, and no others.

7. Let $f_1,\ldots,f_d$ be random variables on $N$ outcomes with density $\rho$, and let $[C]\in\mathbb{R}^{d\times d}$ collect their covariances, $C_{ij}=\operatorname{cov}(f_i,f_j)$.
Exhibit $[C]=\hat{\mathcal{X}}^T\operatorname{diag}(\rho)\,\hat{\mathcal{X}}$ for $\hat{\mathcal{X}}\in\mathbb{R}^{N\times d}$ the matrix whose columns are the centered residuals $\hat{f}_1,\ldots,\hat{f}_d$ — the Gram matrix of Chapter 5, its inner products taken per Definition 12.1 — and conclude that $[C]$ is symmetric positive semidefinite with $\operatorname{rank}[C]=\dim\operatorname{span}\{\hat{f}_1,\ldots,\hat{f}_d\}$.
Then set $\rho_i=1/n$ on $N=n$ outcomes, one per observation, and verify that $[C]$ becomes exactly the sample covariance $\frac{1}{n}\mathcal{X}^T\mathcal{X}$ of Section 11.2, whose $\mathcal{X}$ arrives already centered.

8. Let $\rho$ lie in the relative interior of the simplex (Definition 12.3).
Expand the quadratic form to show that

$$
f^T\left(\operatorname{diag}(\rho)-\rho\rho^T\right)f \,=\, \mathbb{V}(f)
    \qquad\text{for every } f\in\mathbb{R}^N :
$$

this matrix represents the variance of Section 12.1 in the *standard* inner product.
Conclude that it is symmetric positive semidefinite, with kernel exactly $\operatorname{span}\{\mathbf{1}\}$ by Exercise 6, and identify its $(i,j)$ entry as $\operatorname{cov}(\mathbf{1}_{\{i\}},\mathbf{1}_{\{j\}})$.

    > *Foreshadowing:* Exercise 9 of Chapter 13 computes this same matrix as the derivative of softmax: the softmax derivative is a covariance matrix.

9. Let the nonempty events $A_1,\ldots,A_k$ partition the outcomes $\{1,\ldots,N\}$.
Show that the indicators $\mathbf{1}_{A_1},\ldots,\mathbf{1}_{A_k}$ are pairwise orthogonal in the inner product of Definition 12.1, with $\|\mathbf{1}_{A_j}\|_\rho^2=\mathbb{P}(A_j)$, and that their span $W$ holds exactly the random variables constant on each block, so $\dim W=k$.
Then show that the orthogonal projection $\Pi_{W}$ replaces $f$, on each block $A_j$, by the constant

$$
\left.\sum_{i\in A_j}\rho_i\,f_i\,\right/\;\mathbb{P}(A_j) ,
$$

its $\rho$-weighted average there.
Statisticians call $\Pi_{W}f$ the conditional expectation of $f$ given the partition; at $k=1$ it is $\mathbb{E}(f)\,\mathbf{1}$.
Finally, observe that $\Pi_{W}$ is self-adjoint for $\langle\cdot,\cdot\rangle_\rho$, then write down its matrix and find the condition on $\rho$ under which that matrix fails to be symmetric: self-adjointness in the sense of Definition 5.10 is not symmetry of the array, as Example 5.15 of Chapter 5 already showed.

10. Show that $P\in\mathbb{R}^{N\times N}$ maps the orthant $\{\rho\geq 0\}$ into itself if and only if $P$ is entrywise nonnegative, and maps the hyperplane $\{\langle\rho,\mathbf{1}\rangle=1\}$ into itself if and only if $P^T\mathbf{1}=\mathbf{1}$.
Exhibit $2\times 2$ matrices satisfying each condition without the other.
Conclude via Lemma 12.4 that a matrix preserving the bounded plate $\Delta^{N-1}$ must preserve both unbounded constraint sets entire: neither invariance can be traded for the other.

11. Unit vectors $\mathbf{u}_1,\ldots,\mathbf{u}_m$ in $\mathbb{R}^n$ satisfy $|\langle\mathbf{u}_i,\mathbf{u}_j\rangle|\leq t$ for all $i\neq j$, with $t<1/(m-1)$.
Prove the family linearly independent — its Gram matrix nonsingular, per Exercise 11 of Chapter 5.
Conclude that more than $n$ unit vectors in $\mathbb{R}^n$ always carry a pair with $|\langle\mathbf{u}_i,\mathbf{u}_j\rangle|\geq 1/(m-1)$.
Show that constant exact by exhibiting $n+1$ unit vectors in an $n$-dimensional space with every pairwise inner product $-1/n$; the vertices of $\Delta^{n}$ (Definition 12.3) supply them.

12. Let $C$ be a symmetric positive definite $d\times d$ matrix — a covariance estimated from data, say — and fix a threshold $\tau>0$ beneath which at least one eigenvalue of $C$ falls.
Form $\tilde{C}$ by replacing every eigenvalue below $\tau$ with the average of those replaced, leaving all eigenvectors untouched.
Prove that $\tilde{C}$ is symmetric positive definite, that $\operatorname{tr}\tilde{C}=\operatorname{tr} C$, and that $\operatorname{cond}(\tilde{C})\leq\operatorname{cond}(C)$ in the sense of Definition 10.8.

13. Let $\Phi:\mathbb{R}^n\rightarrow\mathbb{R}^k$ be linear with $k<n$.
Show from Corollary 3.26 that $\dim\operatorname{ker}\Phi\geq n-k$, and exhibit two distinct points of $\mathbb{R}^n$ whose positive distance $\Phi$ collapses to zero.
Conclude that no linear map into $\mathbb{R}^k$, random or otherwise, satisfies the lower bound of Theorem 12.10 for every pair of points in $\mathbb{R}^n$: the theorem's restriction to a finite cloud is not caution but necessity.

14. Let $A\in\mathbb{R}^{n\times d}$ and let $\Omega\in\mathbb{R}^{d\times(k+p)}$ be any matrix of probes, as in Section 12.6.
Prove that $\operatorname{im}(A\Omega)\subseteq\operatorname{im} A$, whatever the draw.
Show that equality holds if and only if $\operatorname{rank}(A\Omega)=\operatorname{rank} A$, so that equality demands $\operatorname{rank} A\leq k+p$.
Exhibit nonzero $A$ and $\Omega$ with $\operatorname{rank} A\leq k+p$ for which the containment is strict, and name the subspace of Chapter 3 that swallowed the columns of $\Omega$.

15. Definition 12.1 demands every $\rho_i>0$; let the demand fail, with $\rho_i=0$ exactly for the outcomes $i$ in a nonempty set $Z$.
Exhibit two random variables $f\neq g$ with $\|f-g\|_\rho=0$.
Show that the degenerate directions $U=\{f\in\mathbb{R}^N : \|f\|_\rho=0\}$ form precisely the subspace $\operatorname{span}\{\mathbf{e}_i : i\in Z\}$, and conclude that $\langle\,\cdot\,,\cdot\,\rangle_\rho$ is an honest inner product on the quotient space $\mathbb{R}^N\!/U$ of Section 3.6, of dimension $N-|Z|$.

16. Section 12.3 licenses families of nearly $e^{nt^2/4}$ directions in $\mathbb{R}^n$ with every pair within $t$ of perpendicular.
Evaluate the license at $t=0$, reconcile it with the $n$ mutually orthogonal directions $\mathbb{R}^n$ actually holds, and decide whether the bound there is false or merely empty.
Then say what the probabilistic method demands of its failure probability, and why zero tolerance puts that demand out of reach.

17. One team reports a cosine of $0.35$ between two feature vectors in $\mathbb{R}^{64}$; another reports $0.35$ in $\mathbb{R}^{4096}$.
Express each report in multiples of the standard deviation that chance alone supplies (Lemma 12.6), and say which is the stronger evidence of genuine kinship.
Then find what each team must report to equal the other's surprise, and explain why one of the two numbers no pair of vectors can attain.

18. A cloud of $m$ points in $\mathbb{R}^n$ spans a subspace of dimension $r\ll n$.
Stack an orthonormal basis of the span into $Q\in\mathbb{R}^{n\times r}$ and show that $\mathbf{x}\mapsto Q^T\mathbf{x}$ preserves every pairwise distance exactly — the adaptive target, $k=r$ at $\epsilon=0$.
Find the point count beyond which the demand of Theorem 12.10 exceeds $r$; evaluate at $r=100$, $\epsilon=0.1$, recalling how many points a rank-$100$ cloud contains.

19. A shared channel serves $m$ users at once: user $i$ transmits $a_i\mathbf{c}_i$ for a unit code $\mathbf{c}_i\in\mathbb{R}^{1024}$, the channel delivers $\mathbf{s}=\sum_j a_j\mathbf{c}_j$, and the receiver reads $\hat{a}_i=\langle\mathbf{s},\mathbf{c}_i\rangle$.
Show that $\hat{a}_i-a_i=\sum_{j\neq i}a_j\langle\mathbf{c}_j,\mathbf{c}_i\rangle$, of size at most $t\sum_{j\neq i}|a_j|$ when every pairwise $|\langle\mathbf{c}_i,\mathbf{c}_j\rangle|\leq t$.
Count the codes Section 12.3's packing guarantee licenses at $t=0.1$ and at $t=0.2$, and say at which tolerance the orthogonal ceiling of $1024$ breaks.

20. A spectrometer records $n=600$ sweeps over $d=60$ frequency channels, stacked as a data matrix $\mathcal{X}\in\mathbb{R}^{600\times 60}$; calibration fixes the instrument noise at independent entries of mean zero and standard deviation $\sigma=0.5$.
The sixty singular values of $\mathcal{X}$ begin $146,\ 98,\ 61,\ 17.2,\ 15.9,\ 15.5,\ 15.3,\ldots$ and decline steadily to $8.6$.
Place the noise-floor edge of Section 12.4 for this instrument, and report the rank of the genuine spectral structure.
Say where an eye reading the plunge after $61$ goes wrong.

21. An archive will hold $m=10^7$ records, each a raw sensor trace in $\mathbb{R}^{10^5}$, and must afterwards answer nearest-neighbor queries.
Records arrive once, one at a time, and can be neither stored at full length nor revisited, so each must be reduced on arrival.
Explain why projection onto principal axes is unavailable here.
Then size the oblivious route: report the $k$ that Theorem 12.10 prescribes at $\epsilon=0.25$, and at $\epsilon=0.1$.

22. A network's graph Laplacian $L$ (Definition 9.23) exists only as a subroutine returning $L\mathbf{v}$.
For $\mathbf{g}$ with independent $\pm 1$ entries, the blind probes $\langle\mathbf{g},L\mathbf{g}\rangle$ and $\|L\mathbf{g}\|^2$ estimate $\operatorname{tr} L$ and $\operatorname{tr}(L^2)$ without bias (Section 12.6).
Show that $\operatorname{tr} L$ counts each edge twice and $\operatorname{tr}(L^2)-\operatorname{tr} L$ sums the squared degrees.
Show that $\mathbb{V}\langle\mathbf{g},L\mathbf{g}\rangle=2\sum_{i\neq j}L_{ij}^2$ — four times the edge count — and conclude from Lemma 12.2 that one probe of a million-edge network reads the edge count within one percent, ninety-nine times in a hundred.

23. (Challenge.) Section 12.3 packed exponentially many directions into $\mathbb{R}^n$; this is the converse: a floor beneath the crosstalk of any $m>n$ unit vectors, however chosen.
Assemble $\mathbf{u}_1,\ldots,\mathbf{u}_m$ as the columns of $X$, with Gram matrix $G=X^TX$, and prove

$$
\max_{i\neq j}\,\bigl|\langle\mathbf{u}_i,\mathbf{u}_j\rangle\bigr| \;\geq\; \sqrt{\frac{m-n}{n(m-1)}}
$$

by aiming the Cauchy-Schwarz inequality (Lemma 5.5) at the spectrum Theorem 10.1 grants $G$.
Verify that the family of Exercise 11 attains equality.
Then price chance against the floor: compute it for the $2\times10^5$ directions Section 12.3 packed into $\mathbb{R}^{1024}$ at crosstalk $0.22$, and name the standard deviation toward which the floor climbs as $m$ grows without bound.

    > *Hint:* $\operatorname{rank} G=\operatorname{rank} X\leq n$ (Exercise 8 of Chapter 6 with Corollary 6.11), while $\operatorname{tr} G=m$ and $\operatorname{tr}(G^2)=\sum_{i,j}\langle\mathbf{u}_i,\mathbf{u}_j\rangle^2$ (Lemma 7.5).

---


---

> **Part marker.** ALBION — synthesis


# Chapter 13. Neural Networks & AI

*"multitudes without number work incessant: the hewn stone is plac'd in beds of mortar mingled with the ashes of Vala"*

**Linear algebra is insufficient for machine intelligence.**
Linear maps cannot separate what is not linearly separable, and the tasks now asked of machines — pixels to categories, sentences to meanings, sensor streams to actions — are nonlinear through and through.
Twelve chapters of linear structure would seem to end at this boundary.
They do not end; they compose.
Interleave the linear maps of this text with one small fixed nonlinearity, applied coordinate by coordinate, and the resulting stack — a neural network — escapes the limitations of its parts while keeping their mathematics: nearly all of its computation, and nearly all of its parameters, live in the matrix.

This chapter dissects the construction with tools already in hand.
Why these assemblies of matrices, trained by descent on text and images, should come to translate and summarize and converse is a question that mathematics has not answered.
This chapter holds to what can be said exactly — and by the end that is a great deal.

## 13.1 Beyond Linear Transformations

No matrix multiplication captures the XOR function; no sequence of linear operations represents a complex logical decision.
The lesson is composition: linearity composed is still linear, but linearity interleaved with mild nonlinearity decides essentially anything.

> *Historical Note:* Minsky and Papert's 1969 book *Perceptrons* noted that single-layer networks cannot learn XOR.
> The solution required training hidden layers — an advance that would wait until the 1980s.

The mathematical foundation for this composition comes through nonlinear operations that transform their inputs componentwise:

**Definition 13.1 (Activation Function).** An **activation function** $\varsigma:\mathbb{R}\to\mathbb{R}$ is a nonlinear function applied elementwise to vectors.
Common choices include:

1. ReLU (Rectified Linear Unit): $\varsigma(x) = \max\{0,x\}$

2. Sigmoid: $\varsigma(x) = 1/(1+e^{-x})$

3. Hyperbolic tangent: $\varsigma(x) = \tanh(x)$

When applied to a vector $\mathbf{x}$, we write $\varsigma(\mathbf{x})=(\varsigma(x_1),\ldots,\varsigma(x_n))^T$.

The ReLU function implements a basic form of sparsity — setting negative values to zero while preserving positive ones.
Its derivative does not exist at zero — the graph has a corner there, and implementations simply decree a value — but the kink is not what makes ReLU train well.
That virtue lies on the positive half-line, where the derivative is exactly $1$: an active ReLU contributes a factor of one to the chain-rule product, however deep the stack, where a saturating activation contributes something small at every layer it appears in.
The sigmoid and hyperbolic tangent functions provide smooth transitions between asymptotic limits, and pay for those limits at both ends, where the derivative dies.

Consider now how linear and nonlinear operations combine.
Given input vector $\mathbf{x}\in\mathbb{R}^n$, **weight matrix** $W\in\mathbb{R}^{m\times n}$, and **bias vector** $\mathbf{b}\in\mathbb{R}^m$, a single neural network layer computes:

$$
\mathbf{h} = \varsigma(W\mathbf{x} + \mathbf{b}) \tag{13.1}
$$

This composition of matrix multiplication, vector addition, and elementwise nonlinearity forms the fundamental building block of neural computation.
Though each operation is simple, their combination is not:

**Lemma 13.2 (Universal Approximation).**

> The hypothesis on $\varsigma$ is not decorative: a polynomial activation of degree $k$ yields only polynomials of degree at most $k$, no matter the width.

A neural network with a single hidden layer of sufficient width, using a continuous non-polynomial activation $\varsigma$, can approximate any continuous function on a compact domain to arbitrary precision.
More precisely, given any continuous function $f:[0,1]^n\to\mathbb{R}$ and error $\epsilon>0$, there exist weights $W_1,W_2$ and biases $\mathbf{b}_1,\mathbf{b}_2$ such that:

$$
\left|f(\mathbf{x}) - \left(W_2\varsigma(W_1\mathbf{x} + \mathbf{b}_1) + \mathbf{b}_2\right)\right| < \epsilon
$$

for all $\mathbf{x}\in[0,1]^n$.

The guarantee offers no practical guidance: modern networks achieve their power through depth, not width.

> *Foreshadowing:* CNNs are anatomized at this chapter's end.

The power of the construction lies not in its parts — the linear map and the activation are each transparent — but in their composition; and composition, of all things, is what this text knows how to take apart.

## 13.2 Network Architecture & Matrix Factorization

Layered composition suggests its own architecture.
Like the singular value decomposition of Chapter 10, neural networks factorize complex transformations into simpler components — not through analytically derived singular vectors, but through learned weight matrices separated by nonlinearity.

*[Margin figure omitted]*

Consider a neural network with $\Lambda$ layers.

> *Notation:* $\Lambda$ counts layers — not the eigenvalue matrix of Chapter 7.

> *Think:* Two things are given up, to two different culprits.
> Convexity goes to *depth*: with the activations deleted, fitting $W_\Lambda\cdots W_1$ is matrix factorization, the canonical non-convex problem.
> The closed form goes to the *activation*: with $\varsigma$ in the way, no pseudoinverse writes the answer down.

Each layer performs the transformation described by equation (13.1), but now we chain these operations together:

$$
\begin{array}{rcl}
\mathbf{h}_1 &=& \varsigma(W_1\mathbf{x} + \mathbf{b}_1) \\
\mathbf{h}_2 &=& \varsigma(W_2\mathbf{h}_1 + \mathbf{b}_2) \\
&\vdots& \\
\hat{\mathbf{y}} &=& W_\Lambda\mathbf{h}_{\Lambda-1} + \mathbf{b}_\Lambda
\end{array} \tag{13.2}
$$

where $\mathbf{x}$ denotes input, the $\mathbf{h}_\ell$ are **hidden layers**, and $\hat{\mathbf{y}}$ provides output.
Without the nonlinear functions $\varsigma$, this would reduce to the single affine map $\mathbf{x}\mapsto W_\Lambda\cdots W_1\mathbf{x}+\mathbf{c}$, whose linear part is the mere product $W_\Lambda\cdots W_1$ and whose offset $\mathbf{c}=\sum_{\ell=1}^{\Lambda}W_\Lambda\cdots W_{\ell+1}\mathbf{b}_\ell$ accumulates the biases — precisely the form we studied in the context of matrix factorization.
The activation functions transform this affine composition into something far more expressive, yet the underlying structure of matrix multiplication remains essential.

**Definition 13.3 (Feedforward Neural Network).** A **feedforward neural network** is a function $f:\mathbb{R}^n\to\mathbb{R}^m$ parameterized by weight matrices $\{W_\ell\}$ and bias vectors $\{\mathbf{b}_\ell\}$ that transforms its input through successive application of equation (13.2).
The **width** of layer $\ell$ equals the number of rows in $W_\ell$, while the **depth** equals the total number of layers $\Lambda$.

Depth and width both buy expressive power, and not equally.
The advantage of depth is not merely empirical: there are functions a deep network expresses with a handful of units per layer that no shallow network matches without exponentially many — a separation that Section 13.6 will exhibit outright, by folding.

Depth also endangers the product on which it rests.
The emanation closing Chapter 5 weighed exactly this object at initialization: weight matrices of independent random entries, scaled to preserve length on average, nonetheless stretch some directions and crush others, and composition compounds the disparity until the product has acquired — in arithmetic if not in algebra — a kernel that no factor of it possesses.
Orthogonal initialization was the remedy there, every length preserved exactly at every depth because $O(n)$ is closed under multiplication.
Training leaves the orthogonal group at its first step, so the architecture must keep doing by other means what the initialization did by geometry.

Modern architectures enhance this basic structure through innovations that echo ideas from matrix conditioning.
**Skip connections** allow information to bypass layers directly:

> *Historical Note:* The introduction of residual networks (ResNets) in 2015 enabled training of networks with over 100 layers.
> The insight came from asking *"what if layers learned differences rather than absolute transformations?"*

$$
\mathbf{h}_\ell = \varsigma(W_\ell\mathbf{h}_{\ell-1} + \mathbf{b}_\ell) + \mathbf{h}_{\ell-1}
$$

The addition demands that the two vectors inhabit the same space, so a skip connection requires the layer it bypasses to preserve width — $W_\ell$ square.
Like the regularization techniques of Chapter 11, these residual paths improve numerical stability by providing direct routes for gradient flow.
They transform the learning task from approximating the desired function to learning its refinements — often a better-conditioned optimization problem.
Similarly, **normalization layers** standardize their inputs; **layer normalization**, the instance the transformers of Section 13.5 use, takes its statistics along the layer itself:

$$
\hat{h}_i = \frac{h_i - \mathbb{E}(h)}{\sqrt{\mathbb{V}(h) + \epsilon}}
$$

where $h_i$ is the $i$th component of $\mathbf{h}_\ell$, and $\mathbb{E}(h)$ and $\mathbb{V}(h)$ are the mean and variance of those components under the uniform density of Section 11.1.
This operation stabilizes the scale of intermediate representations, standardizing activations as Section 11.5 standardized data; it leaves every $W$ untouched, but it equilibrates the scale of what the next layer must fit.

These architectural choices serve trainability as much as expressive power: the structure exists so that optimization can succeed.

## 13.3 Chains & Backpropagation

The challenge of neural network training lies not in understanding what to optimize — clearly we seek parameters that minimize prediction error — but in computing how small changes in parameters affect network output.
With potentially billions of parameters spread across many layers, direct calculation of derivatives seems hopelessly complex.
Yet the chain rule of multivariable calculus provides exactly the tool we need, transforming an apparently intractable computation into a single product of matrices.

Consider first the mathematical structure of what we wish to compute.
Given a network with parameters $\Psi$ (encoding all weights and biases), we seek to minimize some loss function $\mathcal{L}(\Psi)$ measuring prediction error on our training data.
The challenge lies in computing $[\partial \mathcal{L}/\partial\Psi]$, the derivatives of loss with respect to parameters.
Though $\mathcal{L}$ is ultimately scalar-valued, it emerges from complex composition of many operations.

The loss is chosen to match the task: this chapter uses squared error $\mathcal{L}=\frac{1}{2}\|\mathbf{y}-\hat{\mathbf{y}}\|^2$ for regression and the logistic loss for classification, writing $\mathbf{y}$ for true values and $\hat{\mathbf{y}}$ for the network's predictions.

Each layer transforms the one below it by (13.2).
The derivative with respect to the bias is immediate: perturbing $\mathbf{b}_\ell$ shifts the pre-activation identically, so $[\partial(W_\ell\mathbf{h}_{\ell-1}+\mathbf{b}_\ell)/\partial\mathbf{b}_\ell]=I$.
The derivative with respect to the weight matrix is a subtler object — the input being perturbed is itself a matrix — and we postpone it until the chain structure is in place.

To see the algorithm whole, write the loss as a composition.
Let $f_\ell$ denote the map effected by layer $\ell$, so that $f_\ell(\mathbf{h})=\varsigma(W_\ell\mathbf{h}+\mathbf{b}_\ell)$ for $\ell<\Lambda$ while the read-out $f_\Lambda(\mathbf{h})=W_\Lambda\mathbf{h}+\mathbf{b}_\Lambda$ carries no activation, as the last line of (13.2) records; and let $g$ denote the scalar function comparing network output to target; then $\mathcal{L} = g\circ f_\Lambda\circ\cdots\circ f_1$ as a function of the input.

> *Nota bene:* Throughout this section, $[Df]$ is the derivative of $f$ as a linear transformation; so for a scalar field the derivative is a row and the gradient is its transpose.

In that convention the chain rule is pure matrix multiplication, in the order of the composition:

$$
[D\mathcal{L}] \;=\; [Dg]\,[Df_\Lambda]\,[Df_{\Lambda-1}]\cdots[Df_1] \tag{13.3}
$$

with each factor evaluated where the forward pass visits, and with

$$
[Df_\ell] = \operatorname{diag}(\varsigma'(\mathbf{z}_\ell))\,W_\ell
    \quad(\ell<\Lambda) ,
    \qquad
    [Df_\Lambda] = W_\Lambda ,
$$

the last factor carrying no diagonal because the read-out carries no activation.
The derivative of the network is the product of the derivatives of its layers.

> *Compare:* The product (13.3) is the object whose conditioning the emanation closing Chapter 5 weighed at initialization.
> Vanishing and exploding gradients are that same arithmetic, read backward: a factor of $10^{-14}$ accumulated across ten layers is a derivative that has arrived at zero.
> An orthogonal start is the choice that makes both sweeps arrive at full strength.

The entire content of backpropagation is a question about the product (13.3): in what order should it be multiplied out?
Associativity guarantees that the answer does not change; the cost does.
Associate from the left, and the computation begins with $[Dg]$  — a single row, since the loss is a scalar field — and a row times a matrix costs $O(n^2)$ operations, with the intermediate result remaining a row through all $\Lambda$ factors, for a total of $O(\Lambda n^2)$.
Associate from the right, and the computation begins with a full matrix times a full matrix at $O(n^3)$ per step, for a total of $O(\Lambda n^3)$.
The left order is **reverse mode** differentiation — reverse because the product is consumed from the loss end backward toward the input — while the right order is **forward mode**.
Same product, same chain rule, and a thousandfold difference in cost when the width is a thousand.
*Backpropagation is the associativity of matrix multiplication, exploited.*

> Automatic differentiation is the art of choosing the order of association.

The row that sweeps leftward through the product deserves a name.

**Definition 13.4 (Error Signal).** The **error signal** $[\delta_\ell]$ at layer $\ell$ is the derivative of loss with respect to that layer's pre-activation output:

$$
\left[\delta_\ell\right] = \left[\frac{\partial \mathcal{L}}{\partial \mathbf{z}_\ell}\right] \in \mathbb{R}^{1 \times n_\ell}
$$

where $\mathbf{z}_\ell = W_\ell\mathbf{h}_{\ell-1} + \mathbf{b}_\ell \in \mathbb{R}^{n_\ell}$ denotes the layer's pre-activation values.

The name is inherited, and it misleads: what $[\delta_\ell]$ measures is a **sensitivity**, the rate at which the loss would move per unit change in the pre-activation $\mathbf{z}_\ell$, evaluated where the forward pass has just been.
At a hidden layer nothing whatever is being subtracted from anything, there being no target for $\mathbf{z}_\ell$ to miss.
{ An error is a difference; $\delta$ is a derivative.}

> *Compare:* Much of the literature writes $\delta_\ell$ as a column and sprinkles transposes through the recursion to compensate.
> The row is the honest shape, a derivative being a linear functional on perturbations of $\mathbf{z}_\ell$ rather than a vector living alongside them — which is exactly why $\delta$ is an adjoint object.

**Lemma 13.5 (Backpropagation Rule).** Let $\mathcal{L}$ be a scalar loss function of network output.
The recursion is initialized at the read-out by

$$
\left[\delta_\Lambda\right] = \left[Dg\right] ,
$$

the derivative of the loss with respect to the network output; and for any layer $\ell<\Lambda$:

$$
\left[\delta_\ell\right] = \left[\delta_{\ell+1}\right]W_{\ell+1}\operatorname{diag}(\varsigma'(\mathbf{z}_\ell))
$$

where $\varsigma'$ denotes the derivative of the activation function.

*Proof.* By the chain rule:

$$
\left[\frac{\partial \mathcal{L}}{\partial \mathbf{z}_\ell}\right] =
    \left[\frac{\partial \mathcal{L}}{\partial \mathbf{z}_{\ell+1}}\right]
    \left[\frac{\partial \mathbf{z}_{\ell+1}}{\partial \mathbf{h}_\ell}\right]
    \left[\frac{\partial \mathbf{h}_\ell}{\partial \mathbf{z}_\ell}\right]
$$

The result follows from computing each factor: $[\partial \mathbf{z}_{\ell+1}/\partial \mathbf{h}_\ell] = W_{\ell+1}$ and $[\partial \mathbf{h}_\ell/\partial \mathbf{z}_\ell] = \operatorname{diag}(\varsigma'(\mathbf{z}_\ell))$, noting carefully the dimensions of each matrix product.
This is left-association of the product (13.3), one factor at a time. ∎

> *Historical Note:* Transposing the whole of (13.3) gives $\nabla\mathcal{L}=[Df_1]^T\cdots[Df_\Lambda]^T[Dg]^T$  — a column swept through adjoints (Definition 5.10), with $(AB)^T=B^TA^T$ the transposed shadow of the same associativity.
> Optimal control theorists of the 1960s knew this backward sweep as the **adjoint method** and its backward variable as the costate; the treatment in Bryson & Ho's *Applied Optimal Control* (1969) contains what a modern reader will recognize as backpropagation, long before the name.
> Werbos's 1974 thesis gave it that name, and was ignored until the 1980s.

The initialization does not stay abstract.
The read-out carries no activation, so the network output is the last pre-activation, $\hat{\mathbf{y}}=\mathbf{z}_\Lambda$; and for the squared loss $\mathcal{L}=\frac{1}{2}\|\mathbf{y}-\hat{\mathbf{y}}\|^2$ a perturbation gives $g(\hat{\mathbf{y}}+\mathbf{v})-g(\hat{\mathbf{y}})=\langle\hat{\mathbf{y}}-\mathbf{y},\mathbf{v}\rangle+O(\|\mathbf{v}\|^2)$, whence

$$
\left[\delta_\Lambda\right] \;=\; \left[Dg\right] \;=\; (\hat{\mathbf{y}}-\mathbf{y})^T \;\in\; \mathbb{R}^{1\times n_\Lambda}
$$

Prediction minus truth, transposed into a row: at the read-out, and for this loss alone, the error signal is the least squares residual of Chapter 6 with its sign reversed.
That coincidence is where the name came from, and it is why the name misleads everywhere else — one layer back, Lemma 13.5 has multiplied by $W_\Lambda$ and by a diagonal of activation slopes, and what arrives is the difference of nothing at all.

The two sweeps are one map and its adjoint.
Forward, layer $\ell$ applies $W_\ell$ to a perturbation of its input; backward, that same layer multiplies a functional of its output on the right by $W_\ell$, which is $W_\ell$ acting through its adjoint in the sense of Definition 5.10, with no transpose written anywhere because the row already carries it.
A quantity propagated by adjoints lives on the dual side of the layer, among the functionals rather than among the vectors, and control theory has the honest word for such a variable: $\delta$ is a **costate**.

What of the parameters?
The loss depends on the weight matrix $W_\ell$, so its derivative with respect to $W_\ell$ is a linear functional on the space $\mathbb{R}^{n_\ell\times n_{\ell-1}}$ of weight perturbations — not a formula to be memorized but a linear transformation to be found, exactly as the convention of the Incipit demands.
Perturb, and read off the leading term: a perturbation $W_\ell\rightsquigarrow W_\ell+E$ enters the pre-activation as $\mathbf{z}_\ell\rightsquigarrow\mathbf{z}_\ell+E\mathbf{h}_{\ell-1}$, whence

$$
\mathcal{L}(W_\ell+E)-\mathcal{L}(W_\ell) \;=\; [\delta_\ell]\,E\,\mathbf{h}_{\ell-1} + O(\|E\|^2)
$$

The derivative is the scalar-valued linear map $E\mapsto[\delta_\ell]E\mathbf{h}_{\ell-1}$ on matrix space, and the Frobenius inner product of Example 5.3 represents it by a single matrix:

$$
[\delta_\ell]\,E\,\mathbf{h}_{\ell-1} = \left\langle\, [\delta_\ell]^T\mathbf{h}_{\ell-1}^T \,,\, E \,\right\rangle_F
    \qquad\text{so}\qquad
    G_\ell = [\delta_\ell]^T\mathbf{h}_{\ell-1}^T \in \mathbb{R}^{n_\ell\times n_{\ell-1}}
$$

This **gradient matrix** $G_\ell$ is what the optimizer consumes, and likewise $\nabla_{\mathbf{b}_\ell}\mathcal{L} = [\delta_\ell]^T$.
The interface between conventions is thus stated once and honored throughout: rows propagate (the derivative, Lemma 13.5); a matrix is delivered (the gradient, its Frobenius representative).

Look again at $G_\ell$: it is manifestly an outer product — *rank one*.
The gradient of the loss with respect to a weight matrix of a million entries is a rank-one matrix, assembled from one row of sensitivities and one column of activations.
For a mini-batch of $b$ samples the gradients add, so the update applied at each step of training has rank at most $b$: stochastic gradient descent nudges each weight matrix along a thin, low-rank direction, and a trained network is a long accumulation of rank-one corrections to its initial matrices — the same shape of object as the expansion $A=\sum_i\sigma_i\mathbf{u}_i\mathbf{v}_i^T$ of Chapter 10, though not the same decomposition.

> The practice of fine-tuning large models by learning only a low-rank correction to each weight matrix is called **LoRA** (low-rank adaptation).
> The rank-one anatomy of the gradient is one reason such a constraint surrenders far less than one would guess; it is not the whole account, and no theorem here supplies the rest.

In practice the algorithm is two sweeps through the network: a forward pass that computes and stores the activations $\mathbf{h}_\ell$ and pre-activations $\mathbf{z}_\ell$, then a backward pass that carries the error signals $[\delta_\ell]$ from the loss toward the input, assembling each gradient matrix from values already in hand.

**Theorem 13.6 (Backpropagation Complexity).** For a network with $\Lambda$ layers each of width at most $n$, backpropagation computes all parameter derivatives in time $O(\Lambda n^2)$ using storage $O(\Lambda n)$ beyond the parameters themselves, the gradient matrices being consumed as computed or held as their rank-one factors.

*Proof.* Both sweeps are the counts already made for the product (13.3): $O(n^2)$ per layer forward, $O(n^2)$ per layer backward under left-association, and $O(n^2)$ entries in each rank-one $G_\ell$. ∎

Linear in depth, quadratic in width: the entire gradient — one number for every parameter in the network — costs a fixed multiple of a single forward pass.
The derivative of the network is no more expensive than the network.

## 13.4 Stochastic Gradient Descent

The mathematics of scale prompts probabilistic thinking.
Backpropagation delivers the exact gradient at the cost of one forward pass — for a single training example.
The loss that matters is an average over a dataset of millions, so its exact gradient is a sum of millions of terms, recomputed at every step of descent — far too much arithmetic per step to permit many steps.
Chapter 12 taught the way out: an average too long to compute is an expectation, and an expectation can be estimated by a sample.

**Definition 13.7 (Stochastic Gradient Descent).** Let $\{\Psi_t\}_{t\geq 0}$ denote a sequence of parameter vectors updated iteratively according to:

$$
\Psi_{t+1} = \Psi_t - \eta_t\left[\frac{\widehat{\partial \mathcal{L}}}{\partial \Psi}\right]^T
$$

where $\eta_t > 0$ is the learning rate and $[\widehat{\partial \mathcal{L}}/\partial \Psi]$ denotes a stochastic estimate of the loss gradient.

The true gradient averages over the whole dataset of $n$ examples:

$$
\left[\frac{\partial \mathcal{L}}{\partial \Psi}\right] = \frac{1}{n}\sum_{i=1}^n \left[\frac{\partial \mathcal{L}_i}{\partial \Psi}\right]
$$

A mini-batch $\mathcal{B}$ of size $b \ll n$, sampled uniformly at random, estimates it:

$$
\left[\frac{\widehat{\partial \mathcal{L}}}{\partial \Psi}\right] = \frac{1}{b}\sum_{i\in\mathcal{B}} \left[\frac{\partial \mathcal{L}_i}{\partial \Psi}\right]
$$

Why descend at all?
Chapter 6 would seem to offer something better: linearize the network in its parameters, assemble the matrix $A=[DF]$ of the derivative of predictions $F$ with respect to weights, and leap toward the residual $\mathbf{r}$ in a single stroke $A^{\dagger}\mathbf{r}$ — least squares applied to learning, known to numerical analysts as the **Gauss-Newton** step.
That matrix is nothing but the bracket of Section 13.3 written out in full, one row for each prediction and one column for each parameter, while $\mathbf{r}$ is a genuine difference of numbers, the vector the read-out hands to the backward sweep, up to sign, and the only stage of the algorithm at which any $\delta$ resembles it.
The formula is correct and the advice is unusable: $A$ has a column for every parameter in the network, and forming, storing, or factoring such a matrix is precisely the labor that backpropagation exists to avoid.
The backward sweep of Section 13.3 delivers products against $A$ one row at a time and never $A$ itself; descent is the concession that at this scale, products are all one can afford.
*The pseudoinverse names the ideal step; the gradient names the affordable one.*

> *Terminology:* The machine learning literature calls $A$ the "Jacobian".
> Both *Jacobian matrix* and *Jacobian determinant* are standard usage; the bare word goes to the determinant in analysis and to the matrix in machine learning.
> This text writes the derivative in brackets and leaves the ambiguity to others.

**Lemma 13.8 (Mini-batch Properties).** Let $\nu^2$ denote the variance of individual gradient estimates.
The mini-batch gradient estimator satisfies:

1. Unbiasedness:
    $\displaystyle \mathbb{E}\left[\frac{\widehat{\partial \mathcal{L}}}{\partial \Psi}\right] = \left[\frac{\partial \mathcal{L}}{\partial \Psi}\right]$

2. Variance bound:
    $\displaystyle \mathbb{V}\left[\frac{\widehat{\partial \mathcal{L}}}{\partial \Psi}\right] =\mathbb{E}\left\|\left[ \frac{\widehat{\partial \mathcal{L}}}{\partial \Psi}\right] - \left[\frac{\partial \mathcal{L}}{\partial \Psi} \right]\right\|_F^2 \leq \frac{\nu^2}{b}$

where $\|\cdot\|_F$ denotes the Frobenius norm.

*Proof.* Each index is drawn uniformly, so linearity of expectation gives (1).
For (2), the estimator is a mean of $b$ draws of variance $\nu^2$, hence of variance $\nu^2/b$; drawing without replacement only shrinks it further, by the factor $(n-b)/(n-1)$, which is why the lemma is stated as an inequality. ∎

**Example 13.9 (Binary Classification).** A network classifying points of $\mathbb{R}^2$ under the logistic loss carries parameters $\mathbf{w}\in\mathbb{R}^2$ and $c\in\mathbb{R}$ and computes

$$
p(x) = \frac{1}{1+e^{-(\mathbf{w}^T\mathbf{x} + c)}}
$$

For data $\{(\mathbf{x}_i,y_i)\}_{i=1}^n$ with $y_i\in\{0,1\}$ the loss is

$$
\mathcal{L}(\mathbf{w},c) = -\frac{1}{n}\sum_{i=1}^n \left[y_i\log p(\mathbf{x}_i) + (1-y_i)\log(1-p(\mathbf{x}_i))\right]
$$

and a mini-batch of size $b=2$, drawn on the points $i,j$, updates

$$
\begin{array}{rcl}
    \mathbf{w}_{t+1} &=& \mathbf{w}_t - \frac{1}{2}\eta_t\sum_{k\in\{i,j\}} (p(\mathbf{x}_k)-y_k)\mathbf{x}_k \\
    c_{t+1} &=& c_t - \frac{1}{2}\eta_t\sum_{k\in\{i,j\}} (p(\mathbf{x}_k)-y_k)
    \end{array}
$$

**Momentum** methods pool recent gradients into the update:

$$
\begin{array}{rcl}
    \mathbf{m}_t &=& \beta\mathbf{m}_{t-1} + (1-\beta)\left[\frac{\widehat{\partial \mathcal{L}}}{\partial \Psi}\right]^T \\
    \Psi_{t+1} &=& \Psi_t - \eta_t\mathbf{m}_t
    \end{array}
$$

with $\beta\in[0,1)$ and $\mathbf{m}_0=\mathbf{0}$.
Averaging the derivatives damps the variance of the estimate and accelerates descent along the elongated valleys characteristic of ill-conditioned systems.

Two conditions calibrate how fast descent can converge.

**Definition 13.10 (Smoothness and Strong Convexity).** A differentiable function $f:\mathbb{R}^n\to\mathbb{R}$ is:

1. {$L$-smooth} if its gradient is Lipschitz continuous with parameter $L>0$:


$$
\|\nabla f(\mathbf{x}) - \nabla f(\mathbf{y})\| \leq L\|\mathbf{x}-\mathbf{y}\|
        \quad\text{for all }\mathbf{x},\mathbf{y}\in\mathbb{R}^n
$$

    > *Caveat:* These hypotheses are imports: the analysis of descent draws on an optimization course this text does not contain.

2. {$\mu$-strongly convex} if for some $\mu>0$:


$$
f(\mathbf{y}) \geq f(\mathbf{x}) + \nabla f(\mathbf{x})^T(\mathbf{y}-\mathbf{x}) + \frac{\mu}{2}\|\mathbf{y}-\mathbf{x}\|^2
        \quad\text{for all }\mathbf{x},\mathbf{y}\in\mathbb{R}^n
$$

In effect, $L$-smoothness provides an upper bound on how quickly the gradient can change, while $\mu$-strong convexity ensures a minimum amount of curvature in all directions.

> *Nota bene:* These conditions relate directly to matrix conditioning: for quadratic functions $f(\mathbf{x})=\frac{1}{2}\mathbf{x}^TA\mathbf{x}$, the ratio $L/\mu$ equals the condition number of $A$.

**Theorem 13.11 (SGD Convergence).** Let $\mathcal{L}$ be $\mu$-strongly convex and $L$-smooth, and set $\gamma = 2L/\mu$.
For the learning rate schedule $\eta_t = \frac{2}{\mu(t+\gamma)}$ and mini-batch size $b$, stochastic gradient descent converges in expectation:

$$
\mathbb{E}[\|\Psi_t - \Psi^*\|^2] \;\leq\; \frac{1}{t+\gamma}\max\left\{\gamma\|\Psi_0 - \Psi^*\|^2,\; \frac{4\nu^2}{b\mu^2}\right\} \;=\; O\left(\frac{1}{t}\right)
$$

where $\Psi^*$ denotes the optimal parameters and $\nu^2$ bounds the variance of individual gradients.

The offset is not cosmetic.
It fixes the opening rate at $\eta_0 = 2/(\mu\gamma) = 1/L$, the step at which the smoothness bound still guarantees descent at every point, and half of the $2/L$ at which a gradient method on an $L$-smooth function ceases to be stable at all; deleted, the schedule begins at $\eta_t>2/L$ and holds there for the first $L/\mu$ steps, and the iteration diverges along the stiffest direction long before the decay has gone far enough to contract.
For the non-convex losses of deep learning no such theorem exists; what provably shrinks is the expected gradient norm, and practice asks no more.

The noise in the estimate, moreover, is not merely tolerable.
Stochastic steps shake the iterate out of narrow basins that would trap exact descent, and their fluctuations act as an implicit regularizer, biasing training toward flat minima whose predictions survive perturbation.
Randomness entered the algorithm for reasons of arithmetic; it stays for reasons of quality.

## 13.5 Attention & Transformers

Every inner product in this text has been chosen.
The dot product came by default; the weighted inner products of Chapter 5 let a modeler emphasize the coordinates that domain knowledge singled out; the Frobenius pairing of Example 5.3 extended the choice to matrices.
In every case a person, understanding the problem, selected the geometry.
The attention mechanism at the heart of the transformer architecture removes the person: relevance between vectors is measured by a bilinear form that the network itself learns, adjusted by gradient descent along with every other parameter.
Like the divine smith forging his own compasses, attention does not measure with a given instrument — it learns one.

The mechanism's vocabulary descends from information retrieval.
A patron approaches a library with a **query**; every book displays a **key** — title, subjects, catalog terms; matching query against keys decides which books' contents, their **values**, are consulted and combined.
Attention casts each token in all three roles at once: from the embedding $\mathbf{x}_i\in\mathbb{R}^d$ of the $i$th token, three learned matrices extract a query $\mathbf{q}_i=W_Q\mathbf{x}_i$, a key $\mathbf{k}_i=W_K\mathbf{x}_i$, and a value $\mathbf{v}_i=W_V\mathbf{x}_i$  — what the token seeks, what it offers, and what it delivers.
Token $i$ scores its whole context by matching query against keys, $\langle\mathbf{q}_i,\mathbf{k}_j\rangle$; softmax converts the scaled scores into a density over the $n$ tokens; and the output for token $i$ is the corresponding mixture of values.

> *Historical Note:* Attention entered neural machine translation through Bahdanau, Cho & Bengio (2015); the transformer of Vaswani *et al.*, "Attention Is All You Need" (2017), removed recurrence entirely and let attention carry the whole computation.

**Definition 13.12 (Attention Mechanism).** Given token embeddings assembled as the columns of $X\in\mathbb{R}^{d\times n}$, with learned **projection matrices** $W_Q$, $W_K\in\mathbb{R}^{d_k\times d}$ and $W_V\in\mathbb{R}^{d_v\times d}$, form $Q=W_QX$, $K=W_KX$, and $V=W_VX$.
The **attention mechanism** returns

$$
Y \,=\, V\,\operatorname{softmax}\!\left(\frac{K^TQ}{\sqrt{d_k}}\right) \;\in\;\mathbb{R}^{d_v\times n} , \tag{13.4}
$$

with softmax (Definition 12.5) applied to each column.
The **attention matrix** $S=\operatorname{softmax}(K^TQ/\sqrt{d_k})\in\mathbb{R}^{n\times n}$ records the result: the entry $s_{ji}$ weighs how much token $i$ heeds token $j$, and the $i$th column of $S$ is the attention density of token $i$.

> *Nota bene:* A ledger of shapes: $Q,K\in\mathbb{R}^{d_k\times n}$; the score matrix $K^TQ$ and its normalization $S$ in $\mathbb{R}^{n\times n}$; $V,Y\in\mathbb{R}^{d_v\times n}$.
> $W_Q$, $W_K$ and $W_V$ are called projection matrices by habit rather than by Definition 6.4: they carry embedding space to separate query, key and value spaces, and nothing asks them to be square, let alone idempotent and self-adjoint.
> When queries come from one sequence and keys and values from another — translation, say — the mechanism is **cross-attention**; the algebra is unchanged.

> *A note on convention.*
> The machine-learning literature stacks its $n$ tokens as the *rows* of a matrix and lets maps act on the right, so that attention appears there as $\operatorname{softmax}(QK^T\!/\sqrt{d_k}\,)\,V$, with softmax taken along rows.
> Every formula of that dialect is the transpose of one of ours.
> The crossing requires a single dictionary entry: *transpose everything*.

The columns of $S$ are densities, so $S$ is column-stochastic in the very sense of Definition 9.13: a stochastic matrix, preserving the simplex (Lemma 12.4) — except that this one is not designed but computed, manufactured afresh from the tokens at every input.
The Markov chains of Chapter 9 mixed by a fixed law; attention mixes by a law the tokens themselves write.

As commonly presented, the formula is a recipe: project, score, normalize, blend.
Watch instead what the scores compute.
Writing $M=W_K^TW_Q\in\mathbb{R}^{d\times d}$ and $\langle\mathbf{u},\mathbf{v}\rangle_M:=\mathbf{u}^TM\mathbf{v}$, the score matrix is

$$
K^TQ \,=\, (W_KX)^T(W_QX) \,=\, X^TMX ,
    \qquad
    \left(K^TQ\right)_{ji} \,=\, \langle\mathbf{k}_j,\mathbf{q}_i\rangle \,=\, \langle\mathbf{x}_j,\mathbf{x}_i\rangle_M . \tag{13.5}
$$

The queries and keys are scaffolding.
What the mechanism has learned is a single bilinear form $M$ on embedding space, and the score matrix collects its pairwise evaluations.
The shape is an old acquaintance: Chapter 5 assembled vectors as the columns of $X$ and formed the Gram matrix $G=X^TX$  — the same construction with the dot product sitting silently in the middle as $M=I$.
The correlation matrix of Chapters 9 and 11 and the kernel matrix of Chapter 11 wore the next two disguises; here is the final one, the silent identity replaced by a learned form.
Between identity and arbitrary lies the middle ground of Example 5.2: a diagonal $M$, its positive weights chosen by a modeler from knowledge of the problem.
Attention fills in the diagonal and surrenders the choosing — a full matrix of weights, learned from data.

The notation flatters: $\langle\cdot,\cdot\rangle_M$ is not an inner product.
Definition 5.1 demanded symmetry and positive definiteness, and the product $M=W_K^TW_Q$ is generically neither — indeed, with $d_k<d$ the form is rank-deficient, so definiteness was never available.
Ask what the failure of symmetry expresses.
Symmetry would force every pair of tokens to heed one another equally: whatever attention "burning" grants "tyger," "tyger" must return in equal measure.
Language refuses.
In "Tyger Tyger, burning bright," the participle leans on the noun it modifies far harder than the noun leans back; a pronoun attends to its antecedent, rarely the reverse; grammar is a web of directed dependencies.
The asymmetry of $M$ is not a defect tolerated for convenience but the capacity to express who modifies whom, which no symmetric form can say.
Definiteness fails just as usefully: nothing forbids $\mathbf{x}^TM\mathbf{x}<0$, and a token may find itself a poor context for itself.

The form is also economical.
Since $M=W_K^TW_Q$ factors through $\mathbb{R}^{d_k}$, its rank is at most $d_k$  — and in practice $d_k\ll d$.
The number $d_k$, presented in most accounts as an arbitrary width to be tuned, is the rank of the learned metric: the dimension of the space of comparisons the mechanism can express.
Chapter 10 met low rank as economy of a map and Chapter 11 as structure hidden in data; here it appears a third way, as economy of measurement, the form scoring relevance along $d_k$ learned directions and blind to all others.

> *Example:* The original transformer took $d=512$ with $h=8$ heads and $d_k=d_v=64$: eight metrics of rank at most $64$ apiece, in a $512$-dimensional embedding space, in place of one full-rank form.

One low-rank form is a narrow instrument; the transformer's remedy is a chorus of them.
The map of Definition 13.12 is called a **head**, and $h$ heads with independent projections $W_Q^{(i)},W_K^{(i)},W_V^{(i)}$ run in parallel, their outputs $Y_i$ stacked and mixed by a final learned matrix $W_O\in\mathbb{R}^{d\times hd_v}$:

$$
\textrm{MultiHead}(X)
    \,=\, W_O\begin{bmatrix} Y_1 \\ \vdots \\ Y_h \end{bmatrix}
    \,=\, \sum_{i=1}^h W_O^{(i)}\,Y_i ,
$$

where the blocks $W_O^{(i)}\in\mathbb{R}^{d\times d_v}$ partition $W_O$ by columns.
The sum should look familiar.
The singular value decomposition wrote a map as $A=\sum_i\sigma_i\mathbf{u}_i\mathbf{v}_i^T$, full complexity assembled from rank-one terms; multi-head attention performs the analogous expansion one level up, assembling its measurement from a family of bilinear forms $M^{(1)},\ldots,M^{(h)}$, each of rank at most $d_k$.
Where the SVD expands the map, multi-head expands the metric.
Probes of trained language models find heads that specialize — one tracking syntactic dependency, another coreference, others patterns that resist naming — though the architecture asks for none of this and the names belong to the investigators rather than to the model.
What the mathematics supplies is the room for such a decomposition: relevance itself factored, and available to be discovered rather than derived.

One factor of formula (13.4) remains unexplained: the $\sqrt{d_k}$.
Section 12.3 supplies the missing size.
For vectors whose coordinates are independent with mean zero and unit variance — a fair portrait of embeddings at initialization, and, thanks to the normalizations of the architecture, not far wrong afterward — the inner product of two such vectors in $\mathbb{R}^{d_k}$ has mean zero and standard deviation $\sqrt{d_k}$: raw scores grow with the dimension even when nothing is related to anything.
Softmax is an exponential normalizer, and Section 12.2 recorded its failure mode: scores of large scale drive each column of $S$ toward a vertex of the simplex, where the derivatives of softmax vanish.
A saturated attention matrix contributes a factor of nearly zero to the chain-rule product (equation 13.3), and the backward sweep of Section 13.3 returns nothing: the mechanism stops learning.
Dividing the scores by their own standard deviation restores them to unit scale at every width.
The $\sqrt{d_k}$ is a concentration-of-measure correction.

The values now claim their turn.
$Y=VS$ with $S$ column-stochastic, so each output

$$
\mathbf{y}_i \,=\, V\mathbf{s}_i \,=\, \sum_{j=1}^n s_{ji}\,\mathbf{v}_j
$$

is a convex combination of the value vectors, the $i$th column of $S$ serving as its mixture density — a point of the simplex $\Delta^{n-1}$, weighting tokens.
The geometric consequences deserve collection.

**Theorem 13.13 (Attention Properties).** Let $Y=VS$ be the output of the attention mechanism (13.4).
Then:

1. $S$ is column-stochastic: each column is a density, entrywise positive with unit sum;

2. each column of $Y$ lies in the **convex hull** of the columns of $V$  — the set of all combinations of them with nonnegative coefficients summing to one — hence in the image $\operatorname{col}(V)$;

3. attention is **permutation equivariant**: for any $n\times n$ permutation matrix $P$, replacing $X$ by $XP$ replaces $Y$ by $YP$;

4. given $Q$, $K$, and $V$, the computation costs $O(n^2\max\{d_k,d_v\})$ operations and $O(n^2)$ memory.

*Proof.* (1) is Definition 12.5, applied column by column.
For (2), the combination $\sum_j s_{ji}\mathbf{v}_j$ with nonnegative weights of unit sum lies in the convex hull of the $\mathbf{v}_j$, and the hull lies in their span.
For (3), replacing $X$ by $XP$ turns the projections into $QP$, $KP$, $VP$; the scores become $(KP)^T(QP)=P^T(K^TQ)P$, permuting rows and columns alike, so column-wise softmax yields $P^TSP$, and $(VP)(P^TSP)=VSP=YP$.
For (4), the score matrix is $n^2$ inner products in $\mathbb{R}^{d_k}$, the blend $VS$ another $n^2d_v$ multiplications, and storing $S$ requires $O(n^2)$ numbers. ∎

Item (2) is a fundamental-subspace statement about a transformer, and it bounds what attention can do.
The mechanism decides the mixture; it cannot manufacture new directions.
Whatever meaning is absent from the image of the value matrix is absent from the output — whatever the scores, however trained the metric — and nothing smaller than $\operatorname{col}(V)$ will do: as the mixture densities range over the simplex the outputs sweep out a bounded convex set, and that set spans $\operatorname{col}(V)$ exactly, so no proper subspace holds everything the mechanism can produce.
*Attention cannot leave the span of its own values.*
In the full architecture the residual connection adds back to $X$ the mixed output $\textrm{MultiHead}(X)=\sum_{i=1}^hW_O^{(i)}Y_i$, the one object of the block already living in $X$'s own $\mathbb{R}^{d\times n}$, and the confinement travels with it: item (2) holds each column of $Y_i$ in the image of that head's values $V_i=W_V^{(i)}X$, so each column of what the block adds lies in $\operatorname{col}(W_O^{(1)}V_1)+\cdots+\operatorname{col}(W_O^{(h)}V_h)$.
What a block adds is confined; what it passes through is not.

Item (3) names a blindness.
Attention treats its tokens as a set: shuffle the words of the line and the outputs shuffle along, none the wiser.
Word order — the difference between "dog bites man" and "man bites dog" — must therefore be injected, and the transformer does so by adding to each embedding a **positional encoding**, trigonometric or learned, before any attention acts.
Order arrives as data, not as structure.

The full transformer interleaves attention with apparatus met earlier in other dress: feed-forward layers of the kind anatomized in Section 13.2; layer normalization, holding the scales steady between blocks; residual connections easing the backward sweep.
The price of attention is its quadratic appetite — the $n\times n$ matrix of item (4) — and much architectural ingenuity, from sparse attention patterns to clever factorizations, goes toward blunting it.
The fundamental operation survives every such economy: matrix multiplication, scoring all pairs at once.

Read formula (13.4) once more, slowly, as a sentence in the language of this text.
A bilinear form stands where Chapter 5 chose weighted inner products, its weights now learned; the form is low-rank, the economy of Chapters 10 and 11; its scores are standardized against the concentration of measure computed in Chapter 12; softmax carries them column by column onto the simplex, as Section 12.2 built it to do; and what emerges is a stochastic mixture confined to the image of the values, in the oldest vocabulary of Chapter 3.
The most famous formula in modern AI is one line long and five chapters deep.

## 13.6 Representation Learning

Look once more at the architecture of equation (13.2) and note what its final line lacks: an activation.
The last act of every network in this chapter is purely linear — one matrix applied to the top hidden layer — so whatever the network has computed must, in the end, be readable from that hidden vector by a single linear map.
All the nonlinearity, every fold and crease, is spent earlier, in the manufacture of the vector itself.
That vector, not the output, is the object of study.

**Definition 13.14 (Representation).** The **representation** of an input $\mathbf{x}$ at depth $\ell$ is the hidden vector $\mathbf{h}_\ell\in\mathbb{R}^{n_\ell}$ produced by the first $\ell$ layers: the value at $\mathbf{x}$ of the composite map $\phi_\ell = f_\ell\circ f_{\ell-1}\circ\cdots\circ f_1$.

One imagines the network rewriting its input, layer by layer, into successive systems of coordinates, the representation being the description current at depth $\ell$.
The wager of deep learning is that some such rewriting renders the task easy — and "easy" here has an exact meaning, supplied by the observation above: a representation is good when what must follow it can be linear.

The wager is older than any network.
Chapter 6 chose its features in advance — $x$ replaced by $(1,x,x^2,\ldots)$, a polynomial fit become a hyperplane fit — and Section 11.7 reached, through a fixed kernel, a feature space it never constructed.
A neural network takes the remaining step: its feature map $\phi_{\Lambda-1}$ is neither designed nor fixed but learned, revised at every step of descent, jointly with the linear read-out that will consume it.
Freeze a trained network's layers and retrain only the last, and all of Chapter 6 returns: the problem is linear least squares in the features $\phi_{\Lambda-1}(\mathbf{x})$, convex, solvable in closed form.
To ask whether a representation has captured some quantity — the tense of a sentence, the pose of a face — one fits a linear map from the frozen features to the quantity and measures the error, a diagnostic known as a **linear probe**: what a probe recovers cheaply, the representation may fairly be said to know.

What kind of function is a network, that its inner coordinates can be probed so plainly?
For the most common activation, the answer is sharp.

**Theorem 13.15 (Piecewise Linearity).** Let $f:\mathbb{R}^{n_0}\to\mathbb{R}^{n_\Lambda}$ be a feedforward network (Definition 13.3) with ReLU activations.
Then $f$ is continuous and piecewise-affine: its domain decomposes into finitely many polyhedral regions, on each of which

$$
f(\mathbf{x}) \,=\, A_R\,\mathbf{x} + \mathbf{c}_R ,
    \qquad
    A_R \,=\, W_\Lambda\, D_{\Lambda-1} W_{\Lambda-1}\cdots D_1 W_1 ,
$$

where each $D_\ell$ is diagonal, with a $1$ for every unit of layer $\ell$ active on the region $R$ and a $0$ for every unit inactive there.

*Proof.* Record, for each unit of each layer, whether its pre-activation is nonnegative — an **activation pattern**.
On the inputs realizing a fixed pattern, every ReLU acts as multiplication by $1$ or by $0$, so layer $\ell$ acts as the affine map $\mathbf{h}\mapsto D_\ell(W_\ell\mathbf{h}+\mathbf{b}_\ell)$, and the composite is affine with linear part as displayed.
The inputs realizing a pattern are cut out by one affine inequality per unit, hence form a polyhedron; the patterns are finite in number; and $f$ is continuous as a composite of continuous maps. ∎

*Between the folds, the network is a matrix.*
And the matrix arrives with everything Chapter 3 attaches to matrices: on each region, $A_R$ has a kernel — the input variation to which the network is locally blind — and an image, its local repertoire of outputs.
Neither is fixed once for all.
Crossing into a neighboring region toggles entries of the $D_\ell$, and with them $A_R$, kernels and images included, so that a trained network carries not one fundamental decomposition but an atlas of them, one page per region; which page governs a given input is exactly what the nonlinearity decides.

Depth now shows its advantage in a form one can count.
Two ReLU units compute the **tent map** — $t(x)=2x$ on $[0,\tfrac{1}{2}]$ and $2-2x$ on $[\tfrac{1}{2},1]$ — which folds the unit interval once upon itself; a network of $\Lambda$ such layers computes the $\Lambda$-fold composite, whose graph is an accordion of $2^\Lambda$ linear pieces.
A single hidden layer of $w$ ReLU units, by contrast, computes a function of one variable with at most $w+1$ pieces — one new kink per unit — so matching the accordion at depth one requires width exponential in $\Lambda$.
Depth multiplies folds; width merely adds them.
This, made geometric, is the separation between deep and shallow claimed in Section 13.2.

What all the folding is for, the data itself suggests.
Natural data rarely fills the space that holds it — an observation the field has elevated to a working principle under the name of the **manifold hypothesis**.

> *Think:* every image you have ever seen lies near a thin, curved sliver of pixel space.
> Almost all of $\mathbb{R}^n$, for $n$ the pixel count, is static that no camera will ever return.

Chapter 11 met the linear shadow of this idea: PCA finds the flat subspace nearest the data — optimal among projections, and helpless when the thin set curves.
A deep network labors under no such restriction.
Region by region, fold by fold, it can press a curved data set toward flatness, and training drives it to do exactly that, since only structure that arrives linearly separable — classes split by hyperplanes, regression targets lying on planes — survives the final, purely linear line of (13.2).

**Example 13.16 (Word Embeddings).** The representation of words shows learned geometry at its most legible.
A learned map $W\in\mathbb{R}^{d\times v}$ sends the one-hot encoding $\mathbf{x}_w\in\mathbb{R}^v$ of a word to a dense vector

$$
\mathbf{e}_w = W\mathbf{x}_w ,
$$

so the embeddings are the columns of $W$, and the geometry carries the semantics: words of similar use come to lie near one another, and difference vectors align across related pairs, so that analogies become near-equalities of vectors, as Example 5.16 of Chapter 5 exhibited with *king*, *man*, *woman*, and *queen*.
The similarity structure of the whole vocabulary is the Gram matrix $W^TW$: all $v^2$ pairwise inner products, yet of rank at most $d\ll v$ — low-rank structure in the sense of Chapter 11, and the reason a lexicon of tens of thousands fits in a space of hundreds.

No person chooses what the coordinates of a learned representation mean, and no person needs to: the geometry is answerable to the task and to nothing else.
What remains is to read that geometry with the instruments this text has spent twelve chapters grinding.

## 13.7 Deep Linear Algebra

A neural network is no linear map, yet it is assembled from nothing else: on each region of input space it is one affine map, whose matrix this text knows how to interrogate.
To ask what a network has learned is to ask where its kernels and images have come to lie, and no architecture answers more legibly than the autoencoder, whose entire purpose is a chosen forgetting.

**Example 13.17 (Learned Decompositions).** Consider an autoencoder compressing data through a narrow hidden layer: an encoder $E:\mathbb{R}^n\to\mathbb{R}^k$ and decoder $D:\mathbb{R}^k\to\mathbb{R}^n$ with $k\ll n$, trained so that $D(E(\mathbf{x}))\approx\mathbf{x}$ across the data.
One might hope to read meaning from the fundamental spaces of $E$ alone, but a trained encoder is (generically) surjective — its image is all of $\mathbb{R}^k$ and its cokernel is trivial — so the encoder by itself has little to confess.
The right object of study is the round trip $D\circ E:\mathbb{R}^n\to\mathbb{R}^n$ (taking $E$ and $D$ linear here, or linearized about a data point), whose fundamental spaces carry the meaning:

- The kernel $\operatorname{ker}(D\circ E)$ is the variation the autoencoder discards

- The image $\operatorname{im}(D\circ E)$ is its learned model of where the data lives

- The cokernel $\operatorname{coker}(D\circ E)\cong(\operatorname{im}(D\circ E))^\perp$ is where the reconstruction residual $\mathbf{x}-D(E(\mathbf{x}))$ points, at the optimum orthogonally to the image — the geometric reconstruction loss

- The coimage $\operatorname{coim}(D\circ E)\cong(\operatorname{ker}(D\circ E))^\perp$ is the effective feature space, inputs modulo discarded variation

For a linear autoencoder on centered data under squared reconstruction error, at the optimum, $D\circ E$ is the orthogonal projection $\sum_{j=1}^k\mathbf{v}_j\mathbf{v}_j^T$ onto the span of the top $k$ principal components, recovering the PCA reconstruction of Section 11.4.
*A linear autoencoder learns PCA; a nonlinear one keeps the four subspaces only one data point at a time.*

—

## Convolutional Networks & The Virtue of Constraint

An image reaches a neural network as a matrix of pixel intensities, flattened into a vector, and the flattening exacts a price: a modest photograph of $256\times256$ pixels becomes a point of $\mathbb{R}^{65536}$, and a single fully connected layer on such a vector carries $65536^2$  — over four billion — weights.
The obstacle is not size alone.
A dense weight matrix grants every pixel an opinion about every other, though nothing binds the upper-left corner of a photograph to the lower right; whatever vision is, it begins locally, in the relations between a pixel and its neighbors.
The remedy is not a larger machine but a smaller matrix, smaller in a structured way.

> *Nota bene:* on a finite row the commutation below fails precisely in the rows that see the border, and practice patches the failure by padding.
> The one place a convolution knows where it is, is the edge of the image.

Convolution is that structure.
In one dimension, for a filter $\mathbf{w}=(w_{-1},w_0,w_1)$, the convolutional layer applies

$$
C \;=\; \begin{bmatrix}
    w_0 & w_{1} & & & \\
    w_{-1} & w_0 & w_{1} & & \\
     & w_{-1} & w_0 & w_{1} & \\
     & & \ddots & \ddots & \ddots \\
     & & & w_{-1} & w_0
    \end{bmatrix} ,
$$

each output a weighted reading of an entry and its immediate neighbors.
Two constraints are visible at a glance.
The matrix is **banded**, its action hugging the diagonal, so that each output attends only to a neighborhood: locality, legislated.
Its diagonals are constant — one weight per diagonal, the same three numbers repeated down the rows — a single detector applied everywhere, known to engineers as **weight sharing**.
An image tells the same story with a doubly indexed filter: a $3\times3$ filter holds nine numbers where the dense layer held four billion.
The constraint does not approximate the dense layer; it declines it.

> *Think:* convolutions on the ring are exactly the polynomials in the shift $S$, and the eigenvalues of $S$ are the $n$ roots of unity: one eigenbasis — the discrete Fourier modes — serves them all at once.
> Convolution in space is multiplication in frequency, and the fast Fourier transform makes the change of basis cheap.

What the missing parameters purchase is a symmetry.
Let $S$ denote the shift, the matrix sliding every entry one place along the row (wrapped at the ends into a ring, to keep the boundary honest).
A direct check gives

$$
CS \;=\; SC :
$$

the filter commutes with translation.
Slide the image and the features slide with it, so that the detector finds an edge wherever it occurs, having never been taught positions at all.
Theorem 13.13 proved the mirror statement for attention: there the mechanism was blind to order, and order had to be injected as data, through positional encodings.
Convolution sits at the opposite pole, its geometry built into the matrix itself, where no data can dislodge it.
The transformer must be told where its tokens stand; the convolution cannot forget.

The simplest filters already do honest work.
The difference filter $\mathbf{w}=(-1,1)$ responds only where adjacent pixels disagree — a one-dimensional edge detector — and its kernel, on the ring, is exactly the constants: rank $n-1$, one dimension discarded, uniform images invisible by construction.
This is the subspace promised long ago, when the closing pages of Chapter 2 observed that the signals a filter silences form a subspace, and Chapter 3 supplied its name.
In a convolutional network that blindness is chosen: an edge detector that registered ambient brightness would be a worse edge detector.

Depth does the rest.
Stacked layers, each convolution followed by a nonlinearity, widen the neighborhood surveyed by any given output, so that filters of filters assemble edges into textures and textures into parts; trained on any large corpus of natural images, the first layer rediscovers much the same oriented edges and spots of contrast, as though the statistics of the visual world had a preferred basis.
The lesson outlives vision: wherever data carries a known symmetry, the matrix can be required to respect it in advance, and whatever the network no longer spends rediscovering geometry, it spends learning content.
*A convolutional layer is a matrix under vows: poverty in its parameters, obedience to translation.*

—

## Large Language Models & The Geometry of the Next Word

Ask a question of a machine, in plain language, and a machine now answers — fluently, at length, in prose that remembers what was said three paragraphs ago.
The engineering that makes this possible is intricate past summarizing; the mathematics is not.
A large language model is assembled, part for part, from the objects of this text, and the reader who has arrived at this page owns every one of them.
It remains to walk through the machine once, prompt to answer, and name what passes.

The prompt is broken into **tokens**: words and pieces of words, drawn from a vocabulary of some tens of thousands.
A token is a choice among $v$ symbols — a one-hot vector in $\mathbb{R}^v$ — and the embedding matrix of Example 13.16, here written $W_E\in\mathbb{R}^{d\times v}$, sends it to its own column: a learned vector of $d$ coordinates, with $d$ in the thousands and no coordinate whose meaning any person chose.
A prompt of $n$ tokens thereby becomes a matrix $X\in\mathbb{R}^{d\times n}$, one column per token — precisely the matrix on which Section 13.5 operated.

What follows is a long alternation of blocks this chapter has already anatomized, arranged around a device with a name worth knowing: the **residual stream**.
Each attention block and each feed-forward layer reads the current stream, computes a correction, and adds it back, $X\rightsquigarrow X+\textrm{block}(X)$, with layer normalization standardizing columns between blocks as Section 11.5 standardized data.
After several dozen such layers, the stream above any token is its embedding plus the sum of every contribution any block has elected to make — a running total in $\mathbb{R}^d$, the machine's working memory.
The confinement of Theorem 13.13 governs each contribution as it is made: what a head returns is a mixture of the values it read off the prompt, so what a block adds to the stream is assembled from what the context actually contains, never a direction manufactured from nothing.

At the far end stands the decision.
Let $\mathbf{h}\in\mathbb{R}^d$ be the stream above the final token — everything the machine has computed about the conversation so far.
One last matrix, the **unembedding** $W_U\in\mathbb{R}^{v\times d}$, converts state into scores, $\mathbf{z}=W_U\mathbf{h}$, one real number for every word in the vocabulary; and here, at the end of everything, the Fundamental Theorem takes the stage a final time.
The matrix $W_U$ has rank at most $d$, so its image is a subspace of dimension at most $d$ inside $\mathbb{R}^v$: among all conceivable scorings of the vocabulary, the model can produce only those lying in one thin slice, and the remaining $v-d$ dimensions — a cokernel's worth of score-space standing perpendicular to that slice — stay out of reach of every prompt, every context, every training of the layers below.
What the machine can say is a subspace.

> Engineers know the confinement of $\mathbf{z}$ to a subspace of dimension $d\ll v$ as the *softmax bottleneck*; the standard escapes widen $d$ or mix several softmaxes.
> That the bound is felt at all measures how much smaller the stream is than the vocabulary.

The reachable scores then pass through softmax (Definition 12.5), which is blind along the diagonal: a constant added to every score changes nothing, for softmax factors through the quotient $\mathbb{R}^v/\operatorname{span}\{\mathbf{1}\}$ that Section 12.2 called the space of scores as softmax actually sees them.
The machine's last map forgets along a kernel this book has already named.

What emerges is a point of the simplex $\Delta^{v-1}$: not a word but a density over all words, positive on every one.
The machine does not assert; it weights.

> *Example:* the "temperature" dial on a deployed model is the scaling $\mathbf{z}\rightsquigarrow\mathbf{z}/T$ applied upstream of softmax: $T\rightarrow0$ drives the density toward the winning vertex, large $T$ flattens it toward uniform.
> The knob the public turns is the stretching of Section 12.2.

An answer is obtained by sampling this density, and however confidently the scores may stretch, the finding of Section 12.2 stands — certainty lies at infinity, the vertices approached and never attained.
Every fluent sentence such a model utters is drawn from an interior point of the simplex, which is why fluency is not evidence, and why a machine with no mechanism for asserting can be wrong in perfect grammar.

The sampled token is appended to the prompt, and the whole machine runs again on $n+1$ columns.
Generation is that loop and nothing more: a trajectory through the simplex, one density per step, each conditioned by attention on the entire history — a Markov chain, if one insists, whose transition law the context rewrites at every step.
The output re-enters the domain, and the oldest arrow in this book, domain to codomain, curls into a circle.

None of the matrices in this walk was designed; all were learned.
At initialization each is noise, its spectrum pooled in the bulk that Chapter 12 computed — every network is born at the noise floor — and training is the long climb out: derivatives assembled by the backward associativity of Section 13.3, applied as the rank-one corrections of stochastic descent, hundreds of billions of parameters revised until signal stands clear of the bulk.
Why the same arithmetic, composed deeply enough and trained long enough, should begin to translate and summarize and argue is a question this text cannot answer; no text yet can.
What can be said exactly is the anatomy.

Stand back, then, from the machine that answers questions, and read that anatomy in the oldest vocabulary of Chapter 3.
Its attention is confined to images.
Its final map forgets along a kernel and sees only a coimage.
Its voice lives inside the thin image of one last matrix, beneath a vast and silent cokernel it will never enter.
The four spaces this text spent thirteen chapters naming are all present, all load-bearing, and all at work at once in the engine of the age.
*The four spaces labor in one body now, and the body speaks.*

—

## Exercises: Chapter 13

1. A network of depth $\Lambda=2$ has ReLU activation, one hidden layer, and the parameters

$$
W_1=\begin{bmatrix}1&1\\1&-2\end{bmatrix},\quad
    \mathbf{b}_1=\begin{bmatrix}1\\-1\end{bmatrix},\quad
    W_2=\begin{bmatrix}1&2\end{bmatrix},\quad
    b_2=-1 ,
$$

the read-out carrying no activation as in (13.2).
On the input $\mathbf{x}=(2,1)^T$ with target $t=6$ and loss $\mathcal{L}=\tfrac12(y-t)^2$, run the forward sweep and record $\mathbf{z}_1$, $\mathbf{h}_1$ and $y$.
Then run the backward sweep of Lemma 13.5 and record $[\delta_2]$, $[\delta_1]$ and both gradient matrices $G_\ell=[\delta_\ell]^T\mathbf{h}_{\ell-1}^T$, with $\mathbf{h}_0=\mathbf{x}$.
Account for the vanishing row of $G_1$.

2. Take the chain (13.3) for a network of depth $\Lambda=6$ with every layer of width $n=200$, so that $[Dg]$ is $1\times n$ and each $[Df_\ell]$ is $n\times n$.
Count the scalar multiplications spent multiplying the chain out from the left, then from the right, and report the ratio.
Then give that ratio for general $\Lambda$ and $n$.

3. Run one mini-batch step of the classifier of Example 13.9 from $\mathbf{w}_0=(1,-1)^T$ and $c_0=0$ at learning rate $\eta=4$, on the batch $\mathbf{x}_1=(2,2)^T$, $y_1=1$ and $\mathbf{x}_2=(1,1)^T$, $y_2=0$, and report $\mathbf{w}_1$ and $c_1$.
Evaluate the batch loss before and after the step, and account for what you find.

4. An attention head in embedding dimension $d=3$ with $d_k=2$ carries

$$
W_Q=\begin{bmatrix}1&0&1\\0&1&-1\end{bmatrix},
    \qquad
    W_K=\begin{bmatrix}1&1&0\\0&1&1\end{bmatrix} .
$$

Form the learned bilinear form $M=W_K^TW_Q$ of (13.5) and report its rank.
Then score the token embeddings $\mathbf{x}_1=(1,1,0)^T$ and $\mathbf{x}_2=(0,1,1)^T$ against one another in both orders, and say which of the two heeds the other the harder.

5. The tent map of Section 13.6 is computed by one hidden layer of two ReLU units: find $a$ and $b$ making $t(x)=a\,\varsigma(x)+b\,\varsigma(x-\tfrac12)$ agree with $t$ on $[0,1]$.
At $k=10$, compare the $2^k$ pieces a stack of $k$ such layers folds against the width a single hidden layer needs to produce as many.

6. A residual block computes $\mathbf{h}_{\text{out}}=\mathbf{h}_{\text{in}}+F(\mathbf{h}_{\text{in}})$, so its derivative is $I+[DF]$ at every point.
Assume $\|[DF]\|_2\leq\epsilon<1$ and prove that every singular value of $I+[DF]$ lies between $1-\epsilon$ and $1+\epsilon$, so that the block is nonsingular with $\operatorname{cond}(I+[DF])\leq(1+\epsilon)/(1-\epsilon)$ in the sense of Definition 10.8.
Then say what the estimate asserts once $\epsilon$ reaches $1$.

7. Layer normalization returns $\hat{h}_i=s\left(h_i-\mathbb{E}(h)\right)/\sqrt{\mathbb{V}(h)+\epsilon}+c$, where $\mathbb{E}(h)$ and $\mathbb{V}(h)$ are the mean and variance of the $n$ components of $\mathbf{h}$, both with the $1/n$ scaling that Section 11.1 used on data, and $s,c$ are learned scalars.
Show that the output has mean exactly $c$, and variance $s^2\mathbb{V}(h)/(\mathbb{V}(h)+\epsilon)$ rather than the $s^2$ one might expect.
Say what the $\epsilon$ buys and what it costs.

8. The gradient matrix $G_\ell=[\delta_\ell]^T\mathbf{h}_{\ell-1}^T$ of Section 13.3 is rank one; ask what its row space is.
Show that every row of $G_\ell$ is a multiple of $\mathbf{h}_{\ell-1}^T$, and conclude that after $T$ steps of descent the total change $W_\ell^{(T)}-W_\ell^{(0)}$ has rank at most the dimension of the span of the activations $\mathbf{h}_{\ell-1}$ met in training.
Say what follows for a layer whose inputs all lie in a $k$-dimensional subspace.

9. Let $\mathbf{p}=\operatorname{softmax}(\mathbf{z})$ as in Definition 12.5, and write $\delta_{ij}$ for the Kronecker delta, equal to $1$ when $i=j$ and to $0$ otherwise.
Differentiate the quotient to obtain $\partial p_i/\partial z_j = p_i(\delta_{ij}-p_j)$, that is $[D\operatorname{softmax}]=\operatorname{diag}(\mathbf{p})-\mathbf{p}\mathbf{p}^T$.
Prove that this matrix has kernel exactly $\operatorname{span}\{\mathbf{1}\}$ and rank $n-1$ — every $p_i$ being positive by construction — and name the property of Definition 12.5 that the kernel expresses infinitesimally.

10. The batch size in Theorem 13.11 enters only through the second entry of the maximum.
Show that while that entry is the larger the bound depends on $b$ and $t$ only through $b(t+\gamma)$, and that once the first entry takes over it contains no $b$ at all.
Find the batch size at which the changeover occurs, and say what it leaves larger batches to be good for.

11. Theorem 13.15 gives a ReLU network of depth $\Lambda=2$ the region matrices $A_R=W_2D_1W_1$, one page of its atlas per activation pattern.
Let $R$ and $R'$ be regions whose patterns differ in the single hidden unit $j$, and show that $A_R-A_{R'}$ is, up to sign, the outer product of the $j$th column of $W_2$ with the $j$th row of $W_1$, hence of rank at most one.
Show also that the two affine maps agree wherever the $j$th pre-activation vanishes, which is the wall the two regions share.

12. The embedding matrix $W\in\mathbb{R}^{d\times v}$ of Example 13.16 carries $v$ words in $d\ll v$ coordinates.
Show that $\dim\operatorname{ker} W\geq v-d$, so that some nontrivial combination of the vocabulary has zero net embedding, and that no more than $d$ of the $v$ embeddings can be nonzero and pairwise orthogonal.
Say what either crowding owes to the meanings of the words.

13. Equation (13.2) gives the read-out no activation; consider a scalar-output network that has one, $y=\varsigma(W_\Lambda\mathbf{h}_{\Lambda-1}+b_\Lambda)$ with $\varsigma$ the ReLU, trained under squared error.
Name the targets it cannot fit however long it trains.
Then suppose its read-out pre-activation is negative at every training input, and show from Lemma 13.5 that every parameter gradient in the network is exactly zero.

14. Theorem 13.13 makes the attention matrix $S$ of Definition 13.12 entrywise positive and column-stochastic.
Conclude from Theorem 9.6 and Lemma 9.15 that $1$ is the dominant eigenvalue of $S$, belonging to a positive density $\mathbf{\pi}$ with $S\mathbf{\pi}=\mathbf{\pi}$ and to no other.
Then say what $\mathbf{\pi}$ is the stationary distribution of, given that $S$ is manufactured afresh from every input and that no transformer ever forms $S^2$.

15. Show that at $h=1$ the multi-head output $W_OY_1$ of Section 13.5 is again a head in the sense of Definition 13.12, with value matrix $W_OW_V$ and $d_v$ replaced by $d$: the output projection is absorbed.
For the original transformer's $h=8$ heads of rank $d_k=64$ in embedding dimension $d=512$, say what rank the forms $M^{(1)},\ldots,M^{(h)}$ jointly reach, against the rank one head commands.
Then name the two features of the expansion $A=\sum_i\sigma_i\mathbf{u}_i\mathbf{v}_i^T$ of Theorem 10.4 that the head expansion does not supply.

16. Six strain gauges ring a drive shaft, and a processing stage reports for each gauge its reading minus the next gauge's — the matrix $D=I-S$ for the cyclic shift $S$.
Two such stages run in series with no nonlinearity between them: write out the resulting $6\times6$ matrix and read off the three-tap filter it applies.
Show that the second stage discards nothing the first had not.

17. A vibration monitor reads two sensor deviations $\mathbf{x}\in\mathbb{R}^2$ and reports the scalar $y=\mathbf{w}_2^T\varsigma(W_1\mathbf{x}+\mathbf{b}_1)$ with ReLU activation,

$$
W_1=\begin{bmatrix}1&2\\3&-1\end{bmatrix},\quad
    \mathbf{b}_1=\begin{bmatrix}1\\-1\end{bmatrix},\quad
    \mathbf{w}_2=\begin{bmatrix}1\\1\end{bmatrix} .
$$

At the nominal operating point $\mathbf{x}=\mathbf{0}$, find the region matrix $A_R$ of Theorem 13.15 and the fault direction spanning its kernel.
Then drive the fault along that direction and find how large it must grow before the monitor's reading moves at all.

18. A router splits traffic over four outgoing links, producing the split $\mathbf{p}=\operatorname{softmax}(W_U\mathbf{h})$ from a two-dimensional internal state $\mathbf{h}$, with

$$
W_U^T=\begin{bmatrix}1&0&-1&0\\0&1&0&-1\end{bmatrix} .
$$

Every reachable split has $\log\mathbf{p}$ in $\operatorname{im} W_U+\operatorname{span}\{\mathbf{1}\}$; find the one direction of $\mathbb{R}^4$ perpendicular to that subspace, and write the condition it imposes as a relation among the four probabilities.
Then decide which of $(\tfrac49,\tfrac29,\tfrac19,\tfrac29)$ and $(0.4,0.3,0.2,0.1)$ the router can produce, and give the state producing it.

19. A bearing-fault network is frozen and its last hidden layer, of width two, is read at four test rigs, returning the representations $(1,0)$, $(0,1)$, $(1,1)$ and $(2,1)$.
The four rigs run at shaft speeds $12,13,15,17$ and carry radial loads $1,1,1,5$.
Fit an affine probe $\mathbf{a}^T\mathbf{h}+c$ to the speeds and find that it reproduces all four exactly.
Then show that no affine probe reproduces the four loads.

20. (Challenge.) A network with more parameters than training points is often said to fit them exactly; one network of Definition 13.3 refutes the claim.
Take the ReLU network $1\to4\to1$, whose $P=13$ parameters exceed the $n=12$ points $x_i=i$, $y_i=(-1)^i$, and show that a continuous piecewise-affine function through those twelve points needs at least ten kinks while Section 13.6 allows a hidden layer of $m$ units at most $m$ of them.
Conclude that no width below ten fits this data at all, whatever the training.
Then show that the least value of $\tfrac{1}{12}\sum_{i=1}^{12}(f(x_i)-y_i)^2$ that width four attains is $40/63$, spending its four kinks to meet four consecutive points at one end exactly and leaving the other eight, still alternating, to a single line.

---


# Explicit

**Linear Algebra** is the study of linear transformations between vector spaces — how they compose, and how they factor.
This text has as its organizing principle the Fundamental Theorem of Linear Algebra, naming four fundamental spaces which scaffold a transformation.
Two of the four arrive not as subspaces but as *quotients* — a construction this text takes up earlier, and leans on harder, than is customary.

Two inputs sent to the same output are, to the transformation, as one input; the space of genuinely different inputs is therefore a quotient of the domain rather than a subspace of it, and that quotient is the *coimage*.
It arrives early and abstractly, the least conspicuous of the four until one notices how often the object of real interest is such a quotient.
Perceived color is not a spectrum but an equivalence class of spectra, a point of a three-dimensional coimage of an infinite-dimensional space of light.
Retaining $k$ principal components is a choice of which quotient of feature space to keep.
A vector of scores is read by a softmax only up to an additive constant, so that the space such a function truly sees is the quotient by the constants.
Supplied with an inner product the quotient acquires a body, $(\operatorname{ker} T)^\perp$, one orthogonal optimal representative drawn from each class.

What is attained is the *image*, and of the four the applications ask after it most insistently.
It is the set of achievable right-hand sides in Chapter 1 and the column space in Chapter 2; it is the destination of the orthogonal projection with which Chapter 6 answers an unsolvable system, returning the nearest solvable one; it is what a smoothing filter keeps, and what a random sketch goes looking for and finds.
An attention block, thirteen chapters along, may contribute to its running stream only vectors drawn from the image of its value map, so that the reachable set of the largest machines now in service is a statement about a column space.

What vanishes is the *kernel*, and it is the busiest of the four.
To solve a linear differential equation is to compute the kernel of a polynomial differential operator.
To find an eigenvalue is to find one of the exceptional numbers $\lambda$ at which $A-\lambda I$ acquires a nontrivial kernel — its eigenspace. The Jordan form is a census of how those (iterated) kernels grow.
A stationary distribution is a kernel vector of $P-I$, and a ranking of the entire Web is that vector normalized.
The agreement of a network is the kernel of its Laplacian, and a boundary condition is the emptying of it.
The freedom of a redundant arm is the kernel of its derivative; the blindness of a difference filter to constants is the kernel of a convolution.
No other space in these pages does so much by being reduced to nothing.

What is most easily missed is the *cokernel*, the most hidden and obscure of the four fundamentals.
Its dimension counts what the codomain holds that the transformation cannot supply: two conservation laws for two components, in the network of the opening pages; the subspace in which a least-squares residual is obliged to live, perpendicular to everything the model can produce; and, at the very end, that vast part of a language model's score space — one coordinate for every word it knows — lying outside the image of one final matrix of far smaller rank: a limit, written in rank, on what a machine of that kind can say.

Two strands run the length of this text.
The first names.
It gives kernel and image, coimage and cokernel, quotients before complements and structure before measurement, and it culminates in the theorem: the domain and codomain each split in two, and the halves that survive are the same space wearing different clothes.
The second measures.
It gives inner products, angles, and lengths, and in Chapter 12 it annexes probability outright, where an expectation is a projection, a variance a squared distance, and a correlation the cosine of an angle.
The strands meet in Chapter 10, where the singular vectors furnish orthonormal bases for all four spaces at once and the transformation, read in those bases, is a list of scalings and nothing besides.
*The Fundamental Theorem names the spaces; the inner product measures them; the SVD weds the two.*

Linear Algebra is not the residence but the vestibule of greater mathematical structures: infinite-dimensional spaces, where the singular values of a compact operator trail off in a tail no matrix possesses; chains of transformations strung so that each image lies inside the next kernel, whose quotients measure the shape they were built from; the nonlinear country where a map is a matrix only in patches, and where reading the patches is the last chapter's whole art.
The Reader who ascends the stair will find these rooms already furnished with familiar artwork.

---


# Appendix: Brief Answers to Exercises

> Final answers for computational problems; a one- or two-sentence claim-and-reason for proofs and conceptual problems. Answer *N* in a given chapter corresponds to Exercise *N* at the end of that chapter.

## Chapter 1

1. First system: $\det = -36$, unique solution $(1,2,-1)$.
Second system: $R_3 = R_1+R_2$, so elimination produces a row of zeros; the coefficient matrix has rank $2$.
The system is consistent because the right-hand side obeys the same relation ($9 = 4+5$), and the solutions form the family $(2+t,\ 1-t,\ t)$.
A zero row demands that the corresponding combination of the right-hand side vanish.

2. $\det A = 3$, $\ A^{-1} = \begin{bmatrix}-1 & 8/3 & -2\\ 0 & 1/3 & 0\\ 0 & 2/3 & -1\end{bmatrix}$;
$\ \det B = 1$, $\ B^{-1} = \begin{bmatrix}4&3&0&0\\-1&-1&0&0\\0&0&2&-3\\0&0&1&-2\end{bmatrix}$.
$A$ is block upper triangular and $B$ is block diagonal, so each determinant is the product of the $2\times2$ block determinants and each inverse is assembled from block inverses.
(The lower-right block of $B$ is its own inverse.)

3. $\textrm{rref}(A) = \begin{bmatrix}1&0&2&0&3\\0&1&-1&0&1\\0&0&0&1&2\\0&0&0&0&0\end{bmatrix}$.
Pivot columns $1, 2, 4$; free columns $3, 5$; $\operatorname{rank}(A)=3$.
The zero row comes from $R_4 = R_1 + R_2$.

4. $L = \begin{bmatrix}1&0&0\\2&1&0\\-1&2&1\end{bmatrix}$, $\ U = \begin{bmatrix}2&3&1\\0&1&-3\\0&0&13\end{bmatrix}$, $\ \det A = 26$.
No row exchanges are needed.

5. Exact solution $\mathbf{x} = (10000/9999,\ 9998/9999)$, near $(1,1)$.
Without pivoting the multiplier is $10^4$ and three-digit arithmetic returns $(0,1)$ — the first component is $100\%$ wrong.
After the exchange the multiplier is $10^{-4}$ and three-digit arithmetic returns $(1.00,\ 1.00)$.
Nothing was wrong with the problem; a small pivot forced a large multiplier, and the subtraction that followed erased the data.
Partial pivoting bounds every multiplier by $1$.

6. $G$ is singular: $\operatorname{rank}(G)=2$ and $G\mathbf{1}=\mathbf{0}$.
The system is solvable because $\mathbf{i}=(1,0,-1)^T$ has components summing to zero — current in must equal current out.
The solutions are $\mathbf{v} = (4/11,\ 1/11,\ 0)^T + t\,(1,1,1)^T$: only voltage differences are determined, so the whole family is one network at every possible offset.

7. $\mathbf{c} = (1/3,\ 1/3,\ 1/3)^T$.
$K$ is symmetric under every permutation of the three species, so no species can be distinguished from another at steady state and the answer must be uniform.
Since mass is conserved, only the total matters — $\mathbf{c}_0$ never enters.

8. If $B\mathbf{x}=\mathbf{0}$ then $\mathbf{x} = (AB)\mathbf{x} = A(B\mathbf{x}) = \mathbf{0}$, so $B$ is nonsingular by Definition 1.7.
Then $A = A(BB^{-1}) = (AB)B^{-1} = B^{-1}$.
Squareness and finite dimension are both essential: the claim is false for rectangular matrices.

9. The powers of $P$ cannot all be distinct, so $P^i=P^j$ for some $i<j$, and $P^{j-i}=I$.
The order is the least common multiple of the cycle lengths of the underlying permutation, so $k=n!$ always works but is rarely least.
A $3\times3$ transposition has order $2$; the $5\times5$ matrix of the permutation $(1\,2)(3\,4\,5)$ has order $\textrm{lcm}(2,3)=6 > 5$.

10. $N\mathbf{e}_j = \mathbf{e}_{j-1}$, so $N^p\mathbf{e}_j = \mathbf{e}_{j-p}$, which vanishes exactly when $j \leq p$.
Hence $N^p$ carries ones on the $p$-th superdiagonal, which is nonempty precisely when $p \leq k-1$.

11. $\operatorname{cond}(A) = \max(1,|1-\alpha|)/\min(1,|1-\alpha|)$.
Well-conditioned: $\alpha \in (-9,\,0.9)\cup(1.1,\,11)$.
Ill-conditioned: $\alpha \in (-\infty,-99)\cup(0.99,1)\cup(1,1.01)\cup(101,\infty)$.
At $\alpha=1$ the matrix is singular and $\operatorname{cond}$ is undefined — not a large number but no number at all, which is why the point is excluded rather than included.

12. $\operatorname{cond}(A)=1$, for every $\theta$.
A rotation carries the unit circle to the unit circle, stretching nothing, so maximum and minimum stretching agree.
Rotations are the perfectly conditioned matrices.

13. Eliminate the first block row from the second: $\mathbf{u}_2$ solves $S\mathbf{u}_2 = \mathbf{f}_2 - K_{21}K_{11}^{-1}\mathbf{f}_1$, then back-substitute.
$\det K = \det K_{11}\det S$ follows from the block factorization of $K$ into unit-triangular factors, and forces $\det S \neq 0$.
The reorganization pays when $K_{11}$ is sparse or structured, when $K_{22}$ is small, or when many right-hand sides share the same $K_{11}$.
Both $K_{11}$ and $S$ must be well-conditioned: nonsingularity of $K_{11}$ is no more sufficient here than a nonzero pivot is in the scalar case.

14. Without pivoting the first multiplier is $1/\epsilon$ and the $(2,2)$ entry becomes $(\epsilon-1)/\epsilon$, giving $\rho(A) = (1-\epsilon)/\epsilon$.
Exchanging rows $1$ and $2$ gives $\rho(PA)=1/(1-\epsilon)\approx 1$.
Since $\det A = -1$ and $\operatorname{cond}(A)\approx 4$ for every $\epsilon$, the matrix was never ill-conditioned; the instability was created by the choice of pivot and destroyed by a better one.

15. The $k$-th pivot is $\Delta_k/\Delta_{k-1}$; total positivity makes every $\Delta_k$ positive, so no pivot vanishes and no exchange is required.
It does *not* follow that the answer is accurate.
Elimination on a totally positive matrix has growth factor $1$ and introduces no new error, but the Hilbert matrix is totally positive and its condition number is enormous: the error already present in the data is amplified regardless.
Backward stability concerns the algorithm; conditioning concerns the problem.

16. Force balance on mass $i$: the two springs flanking it pull with $k_i(x_i-x_{i-1})$ and $k_{i+1}(x_i-x_{i+1})$, where $x_0=x_{n+1}=0$ at the walls.
Equilibrium is $k_i(x_i-x_{i-1}) + k_{i+1}(x_i-x_{i+1}) = f_i$, which collects into $a_{ii}=k_i+k_{i+1}$ and $a_{i,i\pm1}=-k_{i+1}$.
For $n=2$, $\det A = k_1k_2+k_1k_3+k_2k_3$.
$A$ is the Hessian of the potential energy $\frac12 k_1x_1^2 + \frac12 k_2(x_2-x_1)^2 + \frac12 k_3x_2^2$, so symmetry is equality of mixed partial derivatives: the spring forces are conservative.
Tridiagonality means each elimination step touches a bounded number of entries, so the cost is linear in $n$.

17. Summing the rows gives $\mathbf{1}^TA = \mathbf{0}^T$, so $\operatorname{rank}(A)\leq n-1$; conversely, if $\mathbf{y}^TA=\mathbf{0}^T$ then $y_u=y_v$ across every edge, so $\mathbf{y}$ is constant on each component.
Hence $\operatorname{rank}(A)=n-c$ for $c$ components, and solvability of $A\mathbf{x}=\mathbf{b}$ costs one constraint per component: the flow into each component must balance the flow out.
The matrix of Example 1.2 is the incidence matrix of a triangle together with a disjoint edge — $n=5$, $c=2$, $\operatorname{rank} = 3$ — and its two constraints are exactly $b_1+b_2+b_3=0$ and $b_4+b_5=0$.

18. Elimination yields the two conditions $b_3 = b_1+b_2$ and $b_4 = 2b_1+b_2$.
For $\mathbf{b}=(1,1,2,3)^T$ the solutions are $(1,1,0)^T + t\,(-1,-2,1)^T$.
Sensors $3$ and $4$ report nothing that sensors $1$ and $2$ have not already reported; and the combination $(-1,-2,1)$ of the underlying quantities is invisible to all four sensors at once.

19. If $A\mathbf{x}=\mathbf{0}$ with $\mathbf{x}\neq\mathbf{0}$, choose $i$ maximizing $|x_i|$; then $|a_{ii}||x_i| = |\sum_{j\neq i}a_{ij}x_j| \leq \sum_{j\neq i}|a_{ij}||x_i| < |a_{ii}||x_i|$, a contradiction.
Strict diagonal dominance is inherited by each successive Schur complement, so every pivot is nonzero and no exchange is forced.
Pivoting is not thereby pointless — but for such matrices the growth factor is bounded by $2$, so little is lost by skipping it, and the savings are real.

20. Rewrite as $(I-\alpha L)\mathbf{x} = (1-\alpha)\mathbf{1}/n$.
Each column of $I-\alpha L$ has diagonal $1-\alpha L_{jj}$ against off-diagonal mass $\alpha(1-L_{jj})$, a margin of $1-\alpha = 0.15 > 0$; so $(I-\alpha L)^T$ is strictly diagonally dominant and therefore nonsingular, hence so is $I-\alpha L$.
Multiplying on the left by $\mathbf{1}^T$ gives $(1-\alpha)\sum_i x_i = 1-\alpha$, so the scores sum to $1$ automatically.
Uniqueness means the ranking is a property of the web itself, not of where the computation started or when it stopped.
At $\alpha=1$ the margin vanishes, and a web with disconnected pieces no longer has a determined ranking.

## Chapter 2

1. Under ordinary operations, commutativity and associativity of addition survive, as do all four scalar axioms wherever both sides are defined; the zero vector and additive inverses fail.
Of the two operations, scalar multiplication is the one that does not return an element of $\mathbb{R}_{>0}$, since $(-1)\cdot 2 = -2$, whereas addition is closed.
Under $x\oplus y=xy$ and $c\odot x=x^c$, all eight axioms hold, the two distributivities being the exponent laws $(xy)^c=x^cy^c$ and $x^{c+d}=x^cx^d$; the zero vector is $1$ and the inverse of $x$ is $1/x$.
Since $y=2^{\log_2 y}$, $\{2\}$ is a minimal spanning set and $\dim=1$: the space is a disguised copy of $\mathbb{R}$, and the exponential is the disguise.

2. The single failure is distributivity over scalar addition: $(1+1)\cdot(1,1)^T=(2,1)^T$ while $1\cdot(1,1)^T+1\cdot(1,1)^T=(2,2)^T$.
Now $0\mathbf{v}=(0+0)\mathbf{v}=0\mathbf{v}+0\mathbf{v}$ by distributivity over *scalar* addition, and $c\mathbf{0}=c(\mathbf{0}+\mathbf{0})=c\mathbf{0}+c\mathbf{0}$ by distributivity over *vector* addition; adding the additive inverse of the left side cancels each to $\mathbf{0}$.
In this $\mathbb{R}^2$ the second survives, since $c\cdot(0,0)^T=(0,0)^T$, while the first fails, since $0\cdot(1,1)^T=(0,1)^T$  — exactly the one whose proof consumed the broken axiom.

3. $\mathbf{v}_1+\mathbf{v}_2-\mathbf{v}_3=\mathbf{0}$, so any two of the three are a minimal spanning set and the span has dimension $2$.
The equation is $y=2x$.
It holds for $(4,8,1)^T=2\mathbf{v}_1+\mathbf{v}_2$ and fails for $(1,1,0)^T$, since $1\neq 2$.

4. $A_3=2A_1+A_2$.
The two conditions become a $2\times2$ system in $c_1,c_2$ of determinant $2\neq0$, hence uniquely solvable: $c_1=-1$, $c_2=2$, giving $\begin{bmatrix}3&1\\2&-1\end{bmatrix}$.

5. The matrix with these three columns has rank $3$, so $S$ is independent, and $\mathbf{w}=\mathbf{v}_1+2\mathbf{v}_2+3\mathbf{v}_3$ with coefficients unique for that reason.
Adjoining $\mathbf{u}$ as a fourth column raises the rank to $4$, so no combination of $S$ reaches it and $S$ does not span.
No three vectors can span $\mathbb{R}^4$: $\{\mathbf{e}_1,\ldots,\mathbf{e}_4\}$ is independent of size $4$, so Corollary 2.22 would force $4\leq3$.

6. $p = 2q_1-q_2 = q_1-2q_2+q_3$.
Two expressions for one polynomial means the set is dependent — indeed $q_3=q_1+q_2$  — so the span has dimension $2$.
It is $\{a+bx+(a-b)x^2\}$, which omits the constant polynomial $1$ (and $x$, and $x^2$).

7. $\operatorname{rank} A = 2$; $\operatorname{row}(A)$ has minimal spanning set $\{(1,2,0),(0,0,1)\}$ and $\operatorname{col}(A)$ has $\{(1,2,-1)^T,(1,-1,3)^T\}$.
The equation is $5b_1-4b_2-3b_3=0$: it holds for $(2,1,2)^T$, since $10-4-6=0$, and $\mathbf{x}=(1,0,1)^T$ solves that system, while $(1,0,0)^T$ gives $5\neq0$ and is unsolvable.
The relation is $2\mathbf{a}_1-\mathbf{a}_2=\mathbf{0}$ on the columns: the second column is twice the first, and so redundant.
Both spaces are planes in $\mathbb{R}^3$, but not the same plane: $\operatorname{row}(A)$ is $y=2x$ while $\operatorname{col}(A)$ is $5b_1-4b_2-3b_3=0$, and $(1,-1,3)^T$ lies in the second and not in the first.

8. The singular matrices contain $\mathbf{0}$ and are closed under scaling, since $\det(kA)=k^2\det A$, but not under addition: $\begin{bmatrix}1&0\\0&0\end{bmatrix}+\begin{bmatrix}0&0\\0&1\end{bmatrix}=I$.
The integer-coefficient polynomials contain $\mathbf{0}$ and are closed under addition but not scaling, since $\tfrac12(x^2+1)$ escapes; the empty set satisfies conditions 2 and 3 vacuously and fails condition 1.
Only $\{A: A(1,1)^T=\mathbf{0}\}$ is a subspace.
The first two items are the witnesses: one is closed under scaling and not addition, the other under addition and not scaling, so neither closure condition implies the other.
The empty set constrains the marginnote: condition 1 follows from condition 3 only for a *nonempty* $W$, where some $\mathbf{v}\in W$ gives $0\mathbf{v}=\mathbf{0}\in W$.

9. Each defining condition, $A^T=A$ and $A^T=-A$, is linear and homogeneous in $A$, so both sets pass the subspace test.
$V$ is spanned by the three $E_{ii}$ and the three $E_{ij}+E_{ji}$ with $i<j$, and $W$ by the three $E_{ij}-E_{ji}$ with $i<j$; each is independent because in a vanishing combination every coefficient appears alone as a matrix entry.
If $A^T=A$ and $A^T=-A$ then $A=\mathbf{0}$, and $M=\tfrac12(M+M^T)+\tfrac12(M-M^T)$ gives the sum; here

$$
M = \begin{bmatrix}2&1&1\\1&-1&2\\1&2&3\end{bmatrix} + \begin{bmatrix}0&2&-1\\-2&0&2\\1&-2&0\end{bmatrix} .
$$

10. $A\mathbf{x}$ is the combination of the columns of $A$ with weights $x_i$, so the achievable $\mathbf{b}$ are exactly $\operatorname{col}(A)$, with minimal spanning set $(-1,1,0,0,0)^T$, $(0,-1,1,0,0)^T$, $(0,0,0,-1,1)^T$ and $\dim\operatorname{col}(A)=\operatorname{rank}(A)=3$.
For the given $\mathbf{b}$, both constraints hold, $\mathbf{x}_p=(1,1,0,2)^T$ works, and the null space is $\operatorname{span}\left((1,1,-1,0)^T\right)$, so the solution set is the line $\mathbf{x}_p+t\,(1,1,-1,0)^T$  — not a subspace, since it omits $\mathbf{0}$ and the sum of two of its elements solves $A\mathbf{x}=2\mathbf{b}$.
That set is the null space of $A^T$, and elimination gives $\operatorname{span}\left((1,1,1,0,0)^T,(0,0,0,1,1)^T\right)$.
If $\mathbf{y}^TA=\mathbf{0}^T$ and $A\mathbf{x}=\mathbf{b}$ then $\mathbf{y}^T\mathbf{b}=\mathbf{y}^TA\mathbf{x}=0$, so the first vector yields $b_1+b_2+b_3=0$ and the second $b_4+b_5=0$.

11. $W$ is the null space of the $1\times5$ matrix of ones, whose rank is $1$, leaving $5-1=4$ free variables, so $\dim W=4$.
Since $c\mathbf{1}\in W$ forces $5c=0$ and $\mathbf{x}=\bar{x}\mathbf{1}+(\mathbf{x}-\bar{x}\mathbf{1})$, the sum is direct; for $\mathbf{x}=(4,7,1,5,3)^T$, $\bar{x}=4$ and $\mathbf{x}=(4,4,4,4,4)^T+(0,3,-3,1,-1)^T$.
Shifting by $c$ raises the mean by $c$, so $(\mathbf{x}+c\mathbf{1})-\overline{(x+c)}\mathbf{1}=\mathbf{x}-\bar{x}\mathbf{1}$: the $L$-summand carries the entire choice of origin and the $W$-summand everything independent of it.
This is the $n-1$ in the denominator of the sample variance, and Chapter 11 returns to centered data under the name PCA.

12. Taking every coefficient zero gives $\mathbf{0}$, and sums and scalar multiples of combinations are combinations, so $S$ is a subspace; taking one coefficient equal to $1$ and the rest $0$ puts each $\mathbf{v}_i$ in $S$.
If $W<V$ contains every $\mathbf{v}_i$, closure under scaling puts each $c_i\mathbf{v}_i$ in $W$ and closure under addition puts the sum there, so $S\subseteq W$.
Hence $S$ is contained in every subspace containing the $\mathbf{v}_i$, and so equals their intersection.

13. If $c\mathbf{v}+\sum\beta_i\mathbf{b}_i=\mathbf{0}$ with $c\neq0$, then $\mathbf{v}=-\tfrac1c\sum\beta_i\mathbf{b}_i\in\operatorname{span}(B)$; so independence forces $\mathbf{v}\notin\operatorname{span}(B)$.
Conversely, if $\mathbf{v}\notin\operatorname{span}(B)$ then $c$ must vanish, and independence of $B$ kills the rest.
Since $\operatorname{span}(B)\subseteq U$, the hypothesis $\mathbf{v}\notin U$ is stronger than needed, and the converse fails: take $B=\{\mathbf{e}_1\}$, $U=\operatorname{span}(\mathbf{e}_1,\mathbf{e}_2)$, $\mathbf{v}=\mathbf{e}_2\in U$, with $\{\mathbf{e}_1,\mathbf{e}_2\}$ independent.

14. True. Some $c_3\neq0$, for otherwise $c_1\mathbf{v}_1+c_2\mathbf{v}_2=\mathbf{0}$ nontrivially; then $\mathbf{v}_3=-(c_1\mathbf{v}_1+c_2\mathbf{v}_2)/c_3$.
Dropping the independence of $\mathbf{v}_1,\mathbf{v}_2$ breaks it: $\mathbf{v}_1=\mathbf{e}_1$, $\mathbf{v}_2=2\mathbf{e}_1$, $\mathbf{v}_3=\mathbf{e}_2$.

15. $U=\operatorname{span}(1,x^2)$ and $W=\operatorname{span}(x)$, both cut out by conditions linear in $p$; and $p=(a_0+a_2x^2)+(a_1x)$, while a polynomial both even and odd has all coefficients zero.
The two decompositions agree termwise.
The averaging formula needs no degree bound — only that $p(x)\mapsto p(-x)$ makes sense — and directness needs none either, since a $p$ that is both even and odd satisfies $p=-p$ and hence $p=0$.
So the same splitting holds for $\mathcal{P}_n$ at every $n$, and for the space of all polynomials besides.

16. $\begin{bmatrix}a&b\\c&d\end{bmatrix}=\begin{bmatrix}a&b\\0&d\end{bmatrix}+\begin{bmatrix}0&0\\c&0\end{bmatrix}$, and a matrix both upper triangular and strictly lower triangular has every entry zero.
The same sum works with the second summand read in $W$, but $U\cap W$ is the set of diagonal matrices, of dimension $2$.
Any line missing $U$ serves as a second complement: $W'=\operatorname{span}\left(E_{21}+E_{11}\right)$ gives $V=U\oplus W'$ as well, since a nonzero multiple of $E_{21}+E_{11}$ has a nonzero $(2,1)$ entry and so escapes $U$.
So the decomposition of a vector is unique, but the complement is not.
Here $\dim U=\dim W=3$, $\dim W_0=1$, $\dim V=4$: the direct sum gives $3+1=4$, while $3+3=6$ overshoots by exactly $\dim(U\cap W)$.
Filling up $V$ is a statement about the sum and directness is a statement about the intersection; the two are independent.

17. Two decompositions give $\mathbf{u}_1-\mathbf{u}_2=\mathbf{w}_2-\mathbf{w}_1\in U\cap W=\{\mathbf{0}\}$, so the first condition implies the second; $\mathbf{0}=\mathbf{0}+\mathbf{0}$ is one such expression, hence under the second condition the only one; and for $\mathbf{x}\in U\cap W$, $\mathbf{0}=\mathbf{x}+(-\mathbf{x})$, so the third condition returns the first.
Closure under scaling is what puts $-\mathbf{x}$ in $W$, and closure under addition is what forms the differences; for arbitrary subsets neither step is available.

18. Three distinct lines through the origin meet pairwise only at $\mathbf{0}$, and $U_1+U_2$ is already $\mathbb{R}^2$.
The decomposition is far from unique: $(1-t)(1,0)^T+(1-t)(0,1)^T+t(1,1)^T=(1,1)^T$ for every $t\in\mathbb{R}$.
Applying Exercise 17 first to $U_1,U_2$ and then to $U_1+U_2$ and $U_3$ gives uniqueness; the example fails the second condition, since $(U_1+U_2)\cap U_3=\mathbb{R}^2\cap U_3=U_3\neq\{\mathbf{0}\}$.

19. While $\operatorname{span}(B)\neq U$, pick $\mathbf{v}\in U\setminus\operatorname{span}(B)$ and adjoin it; the enlarged set stays independent, Corollary 2.22 bounds every independent set in $U$ by the size of any spanning set for $U$, so the process halts, and it halts at an independent spanning set — a minimal spanning set by Lemma 2.20.
Write $B=\{\mathbf{z}_1,\ldots,\mathbf{z}_d\}$, $B_U=B\cup\{\mathbf{u}_1,\ldots,\mathbf{u}_{p-d}\}$, $B_W=B\cup\{\mathbf{w}_1,\ldots,\mathbf{w}_{q-d}\}$, with $p=\dim U$, $q=\dim W$, $d=\dim(U\cap W)$; spanning is immediate.
For independence, suppose $\sum\alpha_k\mathbf{z}_k+\sum\beta_i\mathbf{u}_i+\sum\gamma_j\mathbf{w}_j=\mathbf{0}$; then $\sum\gamma_j\mathbf{w}_j$ lies in $U$ and in $W$, hence in $\operatorname{span}(B)$, and independence of $B_W$ forces every $\gamma_j=0$, after which independence of $B_U$ kills the rest.
So $\dim(U+W)=d+(p-d)+(q-d)=p+q-d$, which reads $6+3=9$ and $3+1=4$ in the two earlier exercises.
If $\dim U+\dim W>3$ with $U\cap W=\{\mathbf{0}\}$, then $U+W$ would be a subspace of $\mathbb{R}^3$ of dimension greater than $3$, contradicting Corollary 2.22 applied to the spanning set $\{\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3\}$.

## Chapter 3

1. $T$: $\operatorname{ker} T=\{\mathbf{0}\}$, $\operatorname{im} T=\mathbb{R}^2$, bijective; $\operatorname{rank} 2$, $\operatorname{null} 0$, $\dim\operatorname{coker} T=0$.
$S$: $\operatorname{ker} S=\operatorname{span}\big((1,-2)^T\big)$, $\operatorname{im} S=\operatorname{span}\big((1,2)^T\big)$, neither injective nor surjective; $\operatorname{rank} 1$, $\operatorname{null} 1$, $\dim\operatorname{coker} S=1$.
In both cases $2 = \operatorname{null} + \operatorname{rank}$ and $2 = \operatorname{rank} + \dim\operatorname{coker}$.

2. Linearity is the distributive law for the dot product.
For $\mathbf{v}\neq\mathbf{0}$: $\operatorname{im} T_{\mathbf{v}}=\mathbb{R}$, and $\operatorname{ker} T_{\mathbf{v}}$ is the solution set of the single equation $\mathbf{v}\cdot\mathbf{x}=0$, of dimension $n-1$ by Corollary 3.26.
For $\mathbf{v}=\mathbf{0}$: $\operatorname{im} T_{\mathbf{0}}=\{0\}$ and $\operatorname{ker} T_{\mathbf{0}}=\mathbb{R}^n$; the rank drops and the kernel jumps.
If $T_{\mathbf{v}}=T_{\mathbf{w}}$ then testing on $\mathbf{x}=\mathbf{e}_i$ gives $v_i=w_i$ for each $i$.

3. $S(px+q) = \tfrac12 px^2 + qx + (c_1p+c_2q)$ for arbitrary constants $c_1,c_2$: a two-parameter family, not a single antiderivative.
No $S$ has $S\circ D=\mathrm{id}$, since $D(1)=0$ while $\mathrm{id}(1)=1$.

4. Evaluation is linear in $p$, and surjective since $T\big(\tfrac{1+x}{2}\big)=(1,0)^T$ and $T\big(\tfrac{1-x}{2}\big)=(0,1)^T$.
$\operatorname{ker} T$ is the set of polynomials in $\mathcal{P}_4$ divisible by $x^2-1$, spanned by $x^2-1$, $x^3-x$, $x^4-1$, of dimension $3$.
So $\operatorname{im} T=\mathbb{R}^2$, $\operatorname{coim} T=\mathcal{P}_4/\operatorname{ker} T\cong\mathbb{R}^2$, $\operatorname{coker} T=\{\mathbf{0}\}$, and $5=3+2$.

5. $\operatorname{rank} T_A=3$ and $\dim\operatorname{coker} T_A = 5-3 = 2$.
Since $\operatorname{im} T_A$ is cut out by $b_4=b_1+b_3$ and $b_5=b_2+b_3$, no combination $\alpha\mathbf{e}_4+\beta\mathbf{e}_5$ lies in $\operatorname{im} T_A$ unless $\alpha=\beta=0$, so $[\mathbf{e}_4],[\mathbf{e}_5]$ are independent; and the expression below shows they span, so they are a minimal spanning set.
Explicitly $[\mathbf{b}] = (b_4-b_1-b_3)[\mathbf{e}_4] + (b_5-b_2-b_3)[\mathbf{e}_5]$.
Thus $[\mathbf{b}]=[\mathbf{0}]$ exactly when $\mathbf{b}\in\operatorname{im} T_A$, which is exactly when $A\mathbf{x}=\mathbf{b}$ is solvable: the class of $\mathbf{b}$ in the cokernel *is* the obstruction, and its two coordinates are the two conditions.

6. The class of $(2,-1)^T$ is the line $y=x-3$.
$\varphi$ is linear with $\varphi(\mathbf{a})=0$, and $\operatorname{null}\varphi=1$ by Corollary 3.26, so $\operatorname{ker}\varphi=\operatorname{span}(\mathbf{a})$.
Then $[\,(x,y)^T\,]\mapsto x-y$ is well-defined, linear, injective and onto $\mathbb{R}$.

7. Both are linear because transposition is.
$T\circ T=\mathrm{id}$ exhibits a two-sided inverse for $T$, so $T$ is invertible and hence an isomorphism by Lemma 3.7(3); no kernel computation is needed.
$\operatorname{ker} S$ is the symmetric matrices, of dimension $3$; $\operatorname{im} S$ is the skew-symmetric matrices, of dimension $1$; and both halves balance, $4=3+1$ over the domain and $4=1+3$ over the codomain.

8. The restriction has kernel $U\cap\operatorname{ker} T$ and image $T(U)$, so Corollary 3.26 gives $\dim T(U)=\dim U-\dim(U\cap\operatorname{ker} T)$.
For the criterion, note that $\sum_i c_iT(\mathbf{v}_i)=\mathbf{0}$ says exactly that $\sum_i c_i\mathbf{v}_i$ lies in $U\cap\operatorname{ker} T$; if that intersection is trivial then independence of the $\mathbf{v}_i$ forces every $c_i=0$, and if it is not, a nonzero element of it supplies coefficients that are not all zero.
When $\operatorname{ker} T=\{\mathbf{0}\}$ the intersection is trivial for every $U$, which is the forward half of Lemma 3.7(1).
Take $T(x,y)=x+y$ with $\mathbf{v}_1=\mathbf{e}_1$, $\mathbf{v}_2=\mathbf{e}_2$: both images equal $1$, and the list $1,1$ is dependent.

9. If $T$ is invertible it is injective, so $\operatorname{ker} T=\{\mathbf{0}\}$.
Conversely $\operatorname{null} T=0$ gives $\operatorname{rank} T=\dim V$ by Corollary 3.26, and a subspace of $V$ of full dimension is $V$ — adjoining an outside vector would, by Exercise 13, produce an independent set too large for Corollary 2.22 — so $T$ is onto and hence invertible.
On the space of all polynomials, $p\mapsto xp$ is injective but misses every nonzero constant, and $D$ is surjective but kills them; in infinite dimensions neither implication survives.

10. If $S\mathbf{v}=\mathbf{0}$ and $T\mathbf{v}=\mathbf{0}$ then $(S+T)\mathbf{v}=\mathbf{0}$; and if $S\mathbf{v}=\mathbf{0}$ and $(S+T)\mathbf{v}=\mathbf{0}$ then $T\mathbf{v}=(S+T)\mathbf{v}-S\mathbf{v}=\mathbf{0}$.
The three pairwise intersections therefore coincide, and each is contained in $\operatorname{ker}(S+T)$.
With $S=\mathrm{id}$ and $T=-\mathrm{id}$ on $\mathbb{R}^2$, both kernels are $\{\mathbf{0}\}$ while $\operatorname{ker}(S+T)=\mathbb{R}^2$.

11. Set $\overline{T}([\mathbf{v}])=T(\mathbf{v})$.
This is well-defined because $\mathbf{v}_1-\mathbf{v}_2\in\operatorname{ker} T$ forces $T(\mathbf{v}_1)=T(\mathbf{v}_2)$; it is linear because $T$ is; it is injective because $\overline{T}([\mathbf{v}])=\mathbf{0}$ puts $\mathbf{v}$ in $\operatorname{ker} T$; and it is onto $\operatorname{im} T$ by construction.
Finite-dimensionality is never used.

12. Linearity is exactly the two defining equations of Definition 3.18 read from right to left, and surjectivity holds because every class is $[\mathbf{v}]$ for some $\mathbf{v}$.
Then $\Pi_{}(\mathbf{v})=[\mathbf{0}]$ means $\mathbf{v}-\mathbf{0}\in U$, so $\operatorname{ker}\Pi_{}=U$.
Since $U$ was an arbitrary subspace, $\Pi_{}$ exhibits every subspace as the kernel of a linear transformation.

13. Set $\overline{T}([\mathbf{v}])=T(\mathbf{v})$; this is well-defined because $\mathbf{v}_1-\mathbf{v}_2\in U<\operatorname{ker} T$, and linear because $T$ is.
Uniqueness holds because $\Pi_{}$ is surjective, so the value of $\overline{T}$ on every class is forced.
With $V=W=\mathbb{R}^2$, $U=\operatorname{span}(\mathbf{e}_1)$ and $T(x,y)=(x,0)^T$, one has $[\mathbf{0}]=[\mathbf{e}_1]$ but $T(\mathbf{0})\neq T(\mathbf{e}_1)$, so no function on $V/U$ can agree with $T$.

14. $\operatorname{ker} N=\operatorname{im} N=\operatorname{span}\big((1,0)^T\big)$, so the intersection is not $\{\mathbf{0}\}$ and the sum is only one-dimensional.
There is no contradiction: the first statement of Theorem 3.25 pairs $\operatorname{ker} N$ with $\operatorname{coim} N=\mathbb{R}^2/\operatorname{ker} N$, not with $\operatorname{im} N$, and it asserts an isomorphism rather than an equality of subspaces.
Indeed $\dim\operatorname{ker} N+\dim\operatorname{coim} N=1+1=2$.

15. $\varphi(S\mathbf{v})=T\mathbf{v}$ is well-defined because $S\mathbf{v}_1=S\mathbf{v}_2$ puts $\mathbf{v}_1-\mathbf{v}_2$ in $\operatorname{ker} S=\operatorname{ker} T$; it is linear, injective (its kernel comes from $\operatorname{ker} T=\operatorname{ker} S$) and onto $\operatorname{im} T$.
For the converse, $S(x,y)=(x,0)^T$ and $T(x,y)=(y,0)^T$ have the same image, the $x$-axis, but $\operatorname{ker} S=\operatorname{span}(\mathbf{e}_2)$ and $\operatorname{ker} T=\operatorname{span}(\mathbf{e}_1)$.
The kernel remembers more than the image does.

16. $\mathbb{Z}$ contains $0$ and is closed under addition and negation, so $\sim$ is an equivalence relation and $(x+y)-(x'+y')=(x-x')+(y-y')\in\mathbb{Z}$ makes class addition well-defined.
Yet $0\sim1$, and $\tfrac12\cdot1-\tfrac12\cdot0=\tfrac12\notin\mathbb{Z}$, so $[\tfrac12\cdot0]\neq[\tfrac12\cdot1]$.
What failed is closure under scalar multiplication, needed at the step $x-x'\in U\Rightarrow c(x-x')\in U$; integer scalars still work, which locates the failure exactly.
Each operation consumes exactly its own closure property, and neither borrows the other's.

17. $M$ is linear by linearity of the integral, and surjective since $M(c/L)=c$; the function $f(x)=x-L/2$ is a nonzero element of $\operatorname{ker} M$.
$X$ is undefined on all of $\operatorname{ker} M$, including at the zero function, so it is not a function on $C([0,L])$; and $\{f:M(f)\neq0\}$ is not a subspace, so there is no honest smaller domain either.
Where it is defined, $X(cf)=X(f)$ for $c\neq0$: it is homogeneous of degree zero, which is the opposite of what linearity requires.

18. $\operatorname{rank} S=2$, so $\operatorname{ker} S=\operatorname{span}\big((1,-1,-2)^T\big)$: the third reaction is not independent, being half the difference of the first two, which is Hess's law in this instance.
$\dim\operatorname{coker} S=5-2=3$, so there are three independent obstructions.
Writing $\mathbf{\Delta}$ for the composition change, they are $\Delta_1+\Delta_3=0$, $\ \Delta_1+2\Delta_2+2\Delta_3+\Delta_5=0$, and $\Delta_4+\Delta_5=0$: one conservation law for each of carbon, oxygen, and hydrogen.
Each independent conservation law is one coordinate on the cokernel, so its dimension is the number of elements.

19. Every element of $\operatorname{im}(S+T)$ is $S\mathbf{v}+T\mathbf{v}$, hence lies in $\operatorname{im} S+\operatorname{im} T$; a spanning set for $\operatorname{im} S$ together with one for $\operatorname{im} T$ spans the sum, so Lemma 2.20 and Corollary 2.22 give $\operatorname{rank}(S+T)\leq\operatorname{rank} S+\operatorname{rank} T$.
For the example, $\operatorname{im} S$ and $\operatorname{im} T$ are the two axes of $\mathbb{R}^2$ and meet only at $\mathbf{0}$, yet $(S+T)(t)=(t,t)^T$ has rank $1<2$.
Equality means both inequalities in that argument are tight: $\operatorname{im}(S+T)=\operatorname{im} S+\operatorname{im} T$ closes the first, and Exercise 19 turns $\dim(\operatorname{im} S+\operatorname{im} T)=\operatorname{rank} S+\operatorname{rank} T$ into $\operatorname{im} S\cap\operatorname{im} T=\{\mathbf{0}\}$, closing the second.

20. $W/U$ contains $[\mathbf{0}]$ and is closed under the operations of $V/U$, hence is a subspace.
The map is well-defined since $\mathbf{v}_1-\mathbf{v}_2\in U<W$ gives $[\mathbf{v}_1]_W=[\mathbf{v}_2]_W$; it is linear and surjective, and $[\mathbf{v}]_U$ lies in its kernel exactly when $\mathbf{v}\in W$, so the kernel is $W/U$.
Exercise 11 then gives $(V/U)/(W/U)\cong V/W$, and the dimensions read $(\dim V-\dim U)-(\dim W-\dim U)=\dim V-\dim W$.

## Chapter 4

1. $P=\begin{bmatrix}1&1\\2&-1\end{bmatrix}$.
Its $j$th column is the standard coordinate vector of $\mathbf{v}_j$, which is what Definition 4.9 asks for when the second basis is the standard one.
$[\mathbf{w}]_\mathcal{B}=(2,3)^T$, obtained from $P^{-1}\mathbf{w}$: $P$ converts $\mathcal{B}$-coordinates to standard ones, so its inverse is what goes the other way.

2. $[\mathbf{v}]_\mathcal{B}=(2,-1,0)^T$ and $[p]_{\mathcal{B}'}=(0,-1,1)^T$.
A zero in the $j$th slot says the vector lies in the span of the *other* basis vectors: $\mathbf{v}$ needs nothing of $(1,0,1)^T$, and $p=x^2-2x+1$ needs nothing of $1+x^2$.

3. Independence and spanning both follow from the triangular pattern of degrees.
$1=1$, $\ x=(1+x)-1$, $\ x^2=(1+x+x^2)-(1+x)$.
The change of basis matrix to $\{1,x,x^2\}$ is $\begin{bmatrix}1&1&1\\0&1&1\\0&0&1\end{bmatrix}$, and the three expressions are the columns of its inverse $\begin{bmatrix}1&-1&0\\0&1&-1\\0&0&1\end{bmatrix}$.

4. $[T]=\begin{bmatrix}0&1&0\\0&0&2\\0&0&0\end{bmatrix}$, so $\operatorname{rank} T=2$ and $\operatorname{null} T=1$ — the kernel being the constants.
The basis $\{1,x,x^2/2\}$ gives the requested matrix.
No basis makes $[T]$ diagonal: a diagonal matrix would require $p'=\lambda p$ for each basis vector, and since differentiation lowers degree this forces $\lambda=0$ throughout, hence $T=0$.

5. In both bases the matrix is $\frac{\sqrt2}{2}\begin{bmatrix}1&-1\\1&1\end{bmatrix}$.
The change of basis matrix $\begin{bmatrix}1&-1\\1&1\end{bmatrix}$ is itself $\sqrt2$ times a rotation by $\pi/4$, and rotations commute, so the conjugation returns $T$ unchanged.
In $\{(1,0)^T,(1,1)^T\}$ the matrix is $\frac{\sqrt2}{2}\begin{bmatrix}0&-2\\1&2\end{bmatrix}$, which is not.

6. $\operatorname{tr} A=\operatorname{tr} B=5$ settles nothing; $\det A=-2$ against $\det B=-6$ settles it, and $A\not\sim B$.
For the second pair, $P=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$ gives $P^{-1}A'P=\begin{bmatrix}4&0\\0&2\end{bmatrix}$.
It is not unique: solving $A'P=PB'$ gives the whole family $\begin{bmatrix}s&t\\s&-t\end{bmatrix}$ with $s,t\neq0$.

7. Extend a basis of $\operatorname{ker} T$ to a basis of $V$ by Theorem 4.3 and let $U$ be the span of the vectors added; then $V=\operatorname{ker} T\oplus U$.
So $T$ restricted to $U$ has kernel $U\cap\operatorname{ker} T=\{\mathbf{0}\}$ and image $T(U)=\operatorname{im} T$, making it an isomorphism onto $\operatorname{im} T$, whence $\dim U=\operatorname{rank} T=r$.
The same theorem extends $T(\mathbf{u}_1),\ldots,T(\mathbf{u}_r)$ to a basis of $W$.
With those orderings, $T(\mathbf{u}_j)$ is the $j$th basis vector of $W$ for $j\leq r$ and $T$ kills the remaining domain vectors, so the columns of $[T]$ are $\mathbf{e}_1,\ldots,\mathbf{e}_r$ followed by zeros.

8. Any $\mathbf{v}$ is uniquely $\sum c_i\mathbf{v}_i$, so $T\mathbf{v}=\sum c_iT(\mathbf{v}_i)$ is forced; conversely, prescribing arbitrary $\mathbf{w}_i\in W$ and defining $T$ by that formula gives a well-defined linear map.
Taking $W=\mathbb{R}^n$ and $\mathbf{w}_i=\mathbf{e}_i$ makes $\mathbf{v}\mapsto[\mathbf{v}]_\mathcal{B}$ an isomorphism $V\to\mathbb{R}^n$.
Two spaces of dimension $n$ are then each isomorphic to $\mathbb{R}^n$, and composing one isomorphism with the inverse of the other relates them.

9. If $P\mathbf{c}=\mathbf{0}$ then the vector with $\mathcal{B}'$-coordinates $\mathbf{c}$ has $\mathcal{B}$-coordinates $\mathbf{0}$, hence is $\mathbf{0}$, hence $\mathbf{c}=\mathbf{0}$ by uniqueness of coordinates; so $P$ is invertible.
Since $[\mathbf{v}]_\mathcal{B}=P[\mathbf{v}]_{\mathcal{B}'}$ for all $\mathbf{v}$, we get $[\mathbf{v}]_{\mathcal{B}'}=P^{-1}[\mathbf{v}]_\mathcal{B}$, which is the definition of the matrix in the other direction.
Writing $Q$ for the matrix from $\mathcal{B}''$ to $\mathcal{B}'$, the matrix from $\mathcal{B}''$ to $\mathcal{B}$ is $PQ$: coordinates are converted right to left.

10. Reflexivity uses $P=I$; symmetry, $B=P^{-1}AP$ gives $A=PBP^{-1}=(P^{-1})^{-1}B(P^{-1})$; transitivity, conjugating by $P$ then $Q$ is conjugating by $PQ$.
Then $B^k=(P^{-1}AP)^k=P^{-1}A^kP$, the inner factors cancelling; and $B$ is invertible exactly when $A$ is, since $\det B=\det A$.
Every step above inverts $P$  — symmetry inverts it explicitly, transitivity needs $(PQ)^{-1}$, and even $B=P^{-1}AP$ is not defined without it.

11. $\det(P^{-1}AP)=\det(P)^{-1}\det A\det P=\det A$, and $\operatorname{tr}(P^{-1}AP)=\operatorname{tr}(APP^{-1})=\operatorname{tr} A$ by the commutation identity of Section 4.5.
The converse fails: the $3\times3$ zero matrix and the matrix with a single $1$ in the upper right both have determinant $0$ and trace $0$, yet $P^{-1}0P=0$ for every $P$, so the zero matrix is similar to nothing but itself.

12. The $j$th column of $[T]_\mathcal{B}^\mathcal{B}$ holds the $\mathcal{B}$-coordinates of $T(\mathbf{v}_j)$, and that column is a multiple of $\mathbf{e}_j$ exactly when $T(\mathbf{v}_j)$ is a multiple of $\mathbf{v}_j$.
Requiring this for every $j$ is requiring the matrix to be diagonal, and the $j$th diagonal entry is precisely the scalar.

13. If $D'$ is $D$ with its entries permuted, then $D'=\Pi^{-1}D\Pi$ for the corresponding permutation matrix $\Pi$, and similarity is transitive.
Sharing a diagonal is not enough: $I$ and $\begin{bmatrix}1&1\\0&1\end{bmatrix}$ have the same diagonal entries, but $I$ is similar only to itself.

14. A similarity class describes a linear transformation, not a matrix: it is what survives every choice of basis, so the class is the transformation and each matrix in it merely one view.
Asking what a matrix looks like asks about the basis, not the map — which is why the fourth power returning to the identity, a property of the class, is visible in one representative and hidden in the other.

15. The four spaces are defined by what $T$ does, so they cannot depend on a basis; a matrix is what $T$ does *after* both bases are fixed.
Rank, determinant, trace and invertibility are properties of the transformation; the individual entries, the shape of the pattern of zeros, and whether the matrix is triangular or diagonal are artifacts of the basis.
The similarity class is exactly the boundary between the two lists.

16. Writing $A=[T]_\mathcal{B}^\mathcal{B}$, the new matrix is $P^{-1}AP$, so it equals $A$ precisely when $AP=PA$ — when $P$ commutes with $A$.
A matrix representation is therefore not a description of $T$ but a description of the pair $(T,\mathcal{B})$, and the change of basis matrices that leave it alone are exactly those the transformation cannot distinguish.

17. Rewriting a vector's $\mathcal{B}'$-coordinates in terms of $\mathcal{B}$ *is* substituting the expressions for the $\mathbf{b}'_j$, so the same coefficients must serve both purposes: the two directions are one act read at its two ends, not two facts that happen to agree.
Defining $P$ by rows instead would transpose it, and the coefficients that build $\mathcal{B}'$ would no longer be the coefficients that move coordinates.

18. In the basis $\{(1,1)^T,(1,-1)^T\}$ the matrix is $\begin{bmatrix}1&0\\0&3\end{bmatrix}$.
The two masses moving together never stretch the middle spring, so that mode feels stiffness $1$; moving oppositely stretches it by twice the displacement, giving $1+2=3$.
$\det K=3=1\cdot 3$ and $\operatorname{tr} K=4=1+3$ are unchanged: the product of the modal stiffnesses and their sum are properties of the system, not of the coordinates.

19. The columns of $P$ are the standard coordinates of the two sensor directions, $(1,0)^T$ and $(\cos\theta,\sin\theta)^T$, which is what Definition 4.9 requires.
$\det P=\sin\theta$, so $P$ is invertible exactly when the sensors are not parallel.
As $\theta\to0$ the two columns nearly coincide: $P$'s least stretching is $\sin\theta$ against a greatest near $\sqrt2$, so $\operatorname{cond}(P)\to\infty$ in the sense of Chapter 1.
Widely different readings then produce nearly the same $\mathbf{a}$, and an error small relative to the readings becomes an error large relative to $\mathbf{a}$.

20. $[\mathbf{x}]_\mathcal{B}=(3,2,1,1)^T$.
Discarding the last two coordinates leaves $3(1,1,1,1)^T+2(1,1,-1,-1)^T=(5,5,1,1)^T$, with error $(1,-1,1,-1)^T$.
It is sensible when the leading coordinates are typically the large ones, as here, so that what is discarded is small; and when all four are kept nothing is lost in any basis, since coordinates determine the vector.

21. Taking traces, $\operatorname{tr}(AB-BA)=\operatorname{tr}(AB)-\operatorname{tr}(BA)=0$, while $\operatorname{tr} I=n\neq0$.
The argument uses that the matrices are square and finite, which is exactly what the polynomial case lacks: on the space of all polynomials, $D(xp)-xD(p)=p$ gives $DM-MD=\mathrm{id}$, and no trace is available to contradict it.

22. Let $\mathbf{v}\neq\mathbf{0}$ and extend $\{\mathbf{v}\}$ to a basis by Theorem 4.3; since $[T]$ is diagonal in it, $T\mathbf{v}=\lambda_{\mathbf{v}}\mathbf{v}$, and this holds for every nonzero $\mathbf{v}$.
If $\mathbf{u},\mathbf{v}$ are independent then $\lambda_{\mathbf{u}+\mathbf{v}}(\mathbf{u}+\mathbf{v})=\lambda_{\mathbf{u}}\mathbf{u}+\lambda_{\mathbf{v}}\mathbf{v}$ forces $\lambda_{\mathbf{u}}=\lambda_{\mathbf{v}}$, and dependent vectors share their scalar outright.
So one $\lambda$ serves for all, and $T=\lambda\,\mathrm{id}$.

## Chapter 5

1. $p=(1+x)^2$, so $\|p\|^2=\int_0^1(1+x)^4dx = 31/5$ and $\|p\| = \sqrt{31/5} = \sqrt{155}/5 \approx 2.490$.

2. $\langle A,B\rangle_F = \operatorname{tr} B = 2$, $\|A\|_F=\sqrt2$, $\|B\|_F=2$, so $\cos\theta = 1/\sqrt2$ and $\theta=\pi/4$.

3. $\langle \mathbf{u},\mathbf{v}\rangle = 9 = \|\mathbf{u}\|^2$, so the projection coefficient is exactly $1$ and $\mathbf{v}-\mathbf{u}=(2,1,-2)^T$, of norm $3$.
Thus $\mathbf{q}_1 = \frac13(1,2,2)^T$ and $\mathbf{q}_2 = \frac13(2,1,-2)^T$.
The two orthogonality conditions have solution $\mathbf{w}=(2,-2,1)^T$ up to scale, again of norm $3$; the sign wanted is the opposite one, $\mathbf{q}_3=\frac13(-2,2,-1)^T$, giving

$$
Q = \frac13\begin{bmatrix}1 & 2 & -2\\ 2 & 1 & 2\\ 2 & -2 & -1\end{bmatrix},
    \qquad Q^TQ=I, \qquad \det Q = 1 .
$$

The opposite sign gives $\det Q=-1$.

4. All three cross terms integrate to zero over a full period, while $\|1\|=\sqrt{2\pi}$ and $\|\cos x\|=\|\sin x\|=\sqrt\pi$, so the set is orthogonal and not orthonormal; scaling by $1/\sqrt{2\pi}$, $1/\sqrt\pi$, $1/\sqrt\pi$ makes it orthonormal.
On $[-\pi,\pi]$ the function $\cos(mx)$ is even and $\sin(nx)$ odd, so the product is odd and integrates to zero over an interval symmetric about the origin — no trigonometric identity is needed.
At $n=0$ the function $\sin(nx)$ is identically zero: it is orthogonal to everything vacuously, has norm $0$, and can belong to no orthogonal set.

5. $r_{11}=\sqrt2$, $\mathbf{q}_1=\frac{1}{\sqrt2}(1,1,0)^T$, $r_{12}=1/\sqrt2$, and $\mathbf{q}_2=\frac{1}{\sqrt6}(1,-1,2)^T$ with $r_{22}=\sqrt6/2$:

$$
Q = \begin{bmatrix}1/\sqrt2 & 1/\sqrt6\\ 1/\sqrt2 & -1/\sqrt6\\ 0 & 2/\sqrt6\end{bmatrix},
    \qquad R = \begin{bmatrix}\sqrt2 & 1/\sqrt2\\ 0 & \sqrt6/2\end{bmatrix} .
$$

Then $QQ^T = \frac13\begin{bmatrix}2&1&1\\1&2&-1\\1&-1&2\end{bmatrix}$, of rank $2$.
Definition 5.22 asks only that the columns of $Q$ be orthonormal, and they are; $QQ^T$ is the projection onto the plane those two columns span, and a plane in $\mathbb{R}^3$ is not $\mathbb{R}^3$.

6. $B_1=\begin{bmatrix}1&0\\0&0\end{bmatrix}$, $B_2=\begin{bmatrix}0&0\\0&1\end{bmatrix}$, $B_3=\frac{1}{\sqrt2}\begin{bmatrix}0&1\\1&0\end{bmatrix}$; only the third needs rescaling, since $\|B_3\|^2$ would otherwise be $2$.
For the given $A$, $c=(3,-2,\sqrt2)$ and $9+4+2=15=\|A\|^2$.

7. Symmetry and linearity are inherited from multiplication of reals.
For $f=a+bx$, $\langle f,f\rangle = a^2+(a+b)^2$, which vanishes only at $a=b=0$; and $\langle f,x\rangle = f(1)$, so the orthogonal polynomials are the multiples of $1-x$.
On $\mathcal{P}_2$ there are still only two evaluation points against $\dim\mathcal{P}_2=3$, so the form must be degenerate: $w=x-x^2$ is nonzero with $\langle w,w\rangle = 0$.

8. Equality makes the discriminant of $q(t)=\|\mathbf{v}\|^2t^2+2\langle \mathbf{u},\mathbf{v}\rangle t+\|\mathbf{u}\|^2$ vanish, so $q$ has the repeated root $t_0 = -\langle \mathbf{u},\mathbf{v}\rangle/\|\mathbf{v}\|^2$; then $\|\mathbf{u}+t_0\mathbf{v}\|^2=0$, and positive definiteness gives $\mathbf{u}=-t_0\mathbf{v}$.
When $\mathbf{v}=\mathbf{0}$, $q$ is the constant $\|\mathbf{u}\|^2$ and has no root at all, so the argument says nothing — yet equality does hold, both sides being zero.
The right conclusion there is $\mathbf{v}=0\,\mathbf{u}$, which is the multiple running the other way: $\mathbf{u}=(1,2)^T$ with $\mathbf{v}=\mathbf{0}$ satisfies equality and no $c$ makes $\mathbf{u}=c\mathbf{v}$.

9. $Q^TQ=I$ says the first column has unit length, and in $\mathbb{R}^2$ the unit vectors perpendicular to $(\cos\theta,\sin\theta)^T$ are exactly $\pm(-\sin\theta,\cos\theta)^T$, giving the two forms; their determinants are $+1$ and $-1$.
For the second, the double-angle formulas give $Q\mathbf{m}=\mathbf{m}$ where $\mathbf{m}=(\cos\frac{\theta}{2},\sin\frac{\theta}{2})^T$, so the fixed line is the one through $\mathbf{m}$ — at half the angle appearing in the matrix.

10. $\frac{\langle \mathbf{u},\mathbf{v}\rangle}{\|\mathbf{v}\|^2}\mathbf{v} = \frac{\mathbf{v}^T\mathbf{u}}{\mathbf{v}^T\mathbf{v}}\mathbf{v} = \frac{\mathbf{v}\mathbf{v}^T}{\mathbf{v}^T\mathbf{v}}\mathbf{u}$, since $\mathbf{v}^T\mathbf{u}$ is a scalar and may be moved.
The matrix is symmetric because $(\mathbf{v}\mathbf{v}^T)^T=\mathbf{v}\mathbf{v}^T$, and squaring it returns it because $\mathbf{v}^T\mathbf{v}$ cancels once in the product.
Without coordinates, $\langle \Pi_{\mathbf{v}}\mathbf{u},\mathbf{w}\rangle = \frac{\langle \mathbf{u},\mathbf{v}\rangle\langle \mathbf{v},\mathbf{w}\rangle}{\|\mathbf{v}\|^2} = \langle \mathbf{u},\Pi_{\mathbf{v}}\mathbf{w}\rangle$, which is symmetric in $\mathbf{u}$ and $\mathbf{w}$.

11. Symmetry is the first axiom applied entrywise.
If $\sum_j c_j\mathbf{v}_j=\mathbf{0}$ with $\mathbf{c}\neq\mathbf{0}$ then $(G\mathbf{c})_i = \langle \mathbf{v}_i,\sum_j c_j\mathbf{v}_j\rangle = 0$, so $G$ is singular; that direction needs symmetry and linearity but not positive definiteness.
Conversely $G\mathbf{c}=\mathbf{0}$ gives $0=\mathbf{c}^TG\mathbf{c} = \|\sum_i c_i\mathbf{v}_i\|^2$, and positive definiteness — the only place it is used — forces the combination to vanish.
Dropping it breaks the claim: the pairing $\langle \mathbf{u},\mathbf{v}\rangle = u_1v_1$ on $\mathbb{R}^2$ is symmetric and linear in each argument but not positive definite, and the independent pair $\mathbf{e}_1,\mathbf{e}_2$ has $G=\begin{bmatrix}1&0\\0&0\end{bmatrix}$, singular.

12. Any nonzero constant has zero derivative, so $\langle 1,1\rangle=0$ with $1\neq0$: positive definiteness fails, and the constants are the whole of the degeneracy.
On $W$ the constraint $f(0)=0$ removes them, since $\langle f,f\rangle=0$ forces $f$ constant and then zero.
Writing $f=ax+bx^2+cx^3$, the two conditions read $a+b+c=0$ and $a+\frac43b+\frac32c=0$, whose solution is $a=\frac{c}{2}$, $b=-\frac{3c}{2}$; taking $c=2$ gives $f(x)=2x^3-3x^2+x = x(x-1)(2x-1)$, unique up to scaling because the constraint matrix has rank $2$ on a space of dimension $3$.

13. For $T=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ and $\mathbf{v}=(x,y)^T$, $\langle T\mathbf{v},\mathbf{v}\rangle = -xy+yx = 0$ identically, while $T\neq0$.
Expanding, $\langle T(\mathbf{u}+\mathbf{v}),\mathbf{u}+\mathbf{v}\rangle - \langle T\mathbf{u},\mathbf{u}\rangle - \langle T\mathbf{v},\mathbf{v}\rangle = \langle (T+T^*)\mathbf{u},\mathbf{v}\rangle$, so the hypothesis holds for all vectors exactly when $\langle (T+T^*)\mathbf{u},\mathbf{v}\rangle=0$ for all $\mathbf{u},\mathbf{v}$, that is when $T^*=-T$.
If such a $T$ is also self-adjoint then $T=T^*=-T$, so $2T=0$ and $T=0$ — the rotation of the first sentence is as far from self-adjoint as a map can be.

14. Expanding both squares, the cross terms $\pm2\langle \mathbf{u},\mathbf{v}\rangle$ cancel; only symmetry and linearity are used, never positive definiteness — the identity holds for any pairing satisfying the first two axioms.
Under $\|\cdot\|_1$ the left side is $2^2+2^2=8$ against a right side of $2(1+1)=4$; under $\|\cdot\|_\infty$ it is $1+1=2$ against the same $4$.
A norm arising from an inner product must satisfy the identity, so neither does.

15. Expanding $\|\mathbf{u}+\mathbf{v}\|^2 = \|\mathbf{u}\|^2+2\langle \mathbf{u},\mathbf{v}\rangle+\|\mathbf{v}\|^2$ shows the identity holds if and only if $\langle \mathbf{u},\mathbf{v}\rangle=0$, which is both directions at once.
The pair $\mathbf{e}_1$ and $\mathbf{v}=\mathbf{0}$ satisfies $\langle \mathbf{e}_1,\mathbf{v}\rangle=0$ and the norm identity, but is dependent — so Lemma 5.7 would be false without its nonzero hypothesis, which earns its place in the independence claim alone.
It is also why Section 5.3 admits only nonzero vectors into an orthogonal set.

16. Under $\int_0^1(fg+f'g')$: $\langle f,g\rangle = \frac16-1 = -\frac56$ and $\|f\|^2=\|g\|^2=\frac43$, so $\cos\theta = -5/8$ and $\theta\approx128.7^\circ$.
The derivative term compares slopes, and $f'=1$ against $g'=-1$ are exactly opposed; the second inner product weighs that opposition equally with the agreement of the values, and it wins.

17. $\mathbf{q}_1=\frac{1}{\sqrt2}(1,1)^T$ and $\mathbf{q}_2=\frac{1}{\sqrt2}(-1,1)^T$, with $R = \begin{bmatrix}2\sqrt2 & 2\sqrt2\\ 0 & \sqrt2\end{bmatrix}$.
Then $Q^T\mathbf{b} = (6\sqrt2,\,2\sqrt2)^T$, and back-substitution gives $x_2=2$ then $x_1=1$, so $\mathbf{x}=(1,2)^T$.
Because $Q$ is orthogonal, $Q^{-1}=Q^T$, and a transpose is free; every new load costs one matrix-vector product and one triangular solve, with the factorization paid for once.

18.

$$
G = \begin{bmatrix}1 & 1/2 & 0\\ 1/2 & 1 & 1/2\\ 0 & 1/2 & 1\end{bmatrix} .
$$

Documents $1$ and $3$ share no vocabulary and are orthogonal; the pairs $1,2$ and $2,3$ are equally aligned, both at $60^\circ$.
The entries are cosine similarities only because the columns are unit vectors: in general $g_{ij}=\|\mathbf{x}_i\|\|\mathbf{x}_j\|\cos\theta_{ij}$, so unnormalized columns would report length as though it were similarity, and a long document would look like everything.

19. The inner product is $\langle \mathbf{u},\mathbf{v}\rangle = u_1v_1 + \frac14u_2v_2 + \frac{1}{25}u_3v_3$.
Euclidean lengths are $5$ and $1$, but $\|(0,0,5)^T\|^2 = 25/25 = 1$ and $\|(1,0,0)^T\|^2 = 1$: in units of each instrument's own noise the two residuals are the same size.
The unit vectors along the axes are $(1,0,0)^T$, $(0,2,0)^T$ and $(0,0,5)^T$.
The weighted norm should decide, since a five-unit miss on the noisiest instrument is no more surprising than a one-unit miss on the cleanest.

20. Setting $\mathbf{c}=\bar{\mathbf{x}}$ and expanding, $\sum_i\|\mathbf{x}_i-\bar{\mathbf{x}}\|^2 = \sum_i\|\mathbf{x}_i\|^2 - 2\langle \sum_i\mathbf{x}_i,\bar{\mathbf{x}}\rangle + M\|\bar{\mathbf{x}}\|^2$, and $\sum_i\mathbf{x}_i = M\bar{\mathbf{x}}$ collapses the last two terms to $-M\|\bar{\mathbf{x}}\|^2$.
For the four sites $\bar{\mathbf{x}}=(1,1)^T$, so the minimum cost is $16-4\cdot 2 = 8$.
On the line, the mean of $0,1,10$ is $11/3$, where the unsquared total is $38/3$; at $c=1$ it is only $10$.
Squaring rewards the outlier's pull, and without it the balance point is the middle site rather than the average of all three.

21. Writing $\alpha = \langle \mathbf{x},\mathbf{a}\rangle/\|\mathbf{a}\|^2$ and similarly $\beta$ for $\mathbf{y}$, the expansion of $\langle T\mathbf{x},T\mathbf{y}\rangle$ contributes $-2\alpha\beta\|\mathbf{a}\|^2-2\alpha\beta\|\mathbf{a}\|^2+4\alpha\beta\|\mathbf{a}\|^2 = 0$ beyond $\langle \mathbf{x},\mathbf{y}\rangle$.
Since $\Pi_{\mathbf{a}}\mathbf{a}=\mathbf{a}$ we get $T\mathbf{a}=-\mathbf{a}$, and $\Pi_{\mathbf{a}}\mathbf{x}=\mathbf{0}$ for $\mathbf{x}\perp\mathbf{a}$ leaves such $\mathbf{x}$ fixed; the matrix statement is the projection matrix $\mathbf{a}\mathbf{a}^T/\mathbf{a}^T\mathbf{a}$ scaled by $-2$ and added to $I$.
For the last part, take $\mathbf{a}=(-\sin\frac{\theta}{2},\cos\frac{\theta}{2})^T$ in the second normal form of Exercise 9: the double-angle formulas turn $I-2\mathbf{a}\mathbf{a}^T$ into exactly $\begin{bmatrix}\cos\theta & \sin\theta\\ \sin\theta & -\cos\theta\end{bmatrix}$.

22. If $Q_1R_1=Q_2R_2$ then $Q_2^TQ_1 = R_2R_1^{-1}$, and the left side is orthogonal while the right side is upper triangular with positive diagonal, since inverses and products of such matrices are again such.
So it suffices that an orthogonal upper triangular $U$ with positive diagonal is $I$: its first column is a unit vector of the form $(u_{11},0,\ldots,0)^T$ with $u_{11}>0$, hence $\mathbf{e}_1$; its second column is a unit vector orthogonal to $\mathbf{e}_1$ with only its first two entries possibly nonzero, hence $\mathbf{e}_2$; and so on down the columns.
Then $Q_1=Q_2$ and $R_1=R_2$.

## Chapter 6

1. $U^\perp = \operatorname{span}\{(1,-1,1)^T\}$, and $\Pi_{U}\mathbf{v} = \mathbf{v}-\frac{4}{3}(1,-1,1)^T = (\frac{2}{3},\frac{7}{3},\frac{5}{3})^T$, with residual $\frac{4}{3}(1,-1,1)^T$.

2. $\langle 1,x-\frac{1}{2}\rangle = \int_0^1(x-\frac{1}{2})dx = 0$.
Gram-Schmidt subtracts $\frac{1}{3}\cdot 1 + 1\cdot(x-\frac{1}{2}) = x-\frac{1}{6}$ from $x^2$, leaving $x^2-x+\frac{1}{6}$; the orthogonal basis is $\{1,\ x-\frac{1}{2},\ x^2-x+\frac{1}{6}\}$.
What was subtracted lies in $\operatorname{span}\{1,x-\frac{1}{2}\}$ and what remains is orthogonal to both, which are precisely the two clauses of Definition 6.4; uniqueness of the projection then forces the identification.

3. $\operatorname{ker} A = \operatorname{span}\{(1,1,1)^T\}$ and $\operatorname{row}(A) = \operatorname{span}\{(2,-1,-1)^T,(-1,2,-1)^T\}$, the plane $x_1+x_2+x_3=0$; every listed inner product is $0$.
Since $A^T=A$, the row and column spaces coincide, so $\operatorname{ker} A\perp\operatorname{im} A$ here as well.

4. $A^TA = \begin{bmatrix}5&3\\3&3\end{bmatrix}$ and $A^T\mathbf{b} = (7,6)^T$, giving $m=\frac{1}{2}$, $b=\frac{3}{2}$ and $y=\frac{1}{2}x+\frac{3}{2}$.
The residual is $(-\frac{1}{2},1,-\frac{1}{2})^T$, orthogonal to $(0,1,2)^T$ and to $(1,1,1)^T$; and $14 = \frac{25}{2}+\frac{3}{2}$.

5. $AA^T = \begin{bmatrix}3&0\\0&2\end{bmatrix}$, so $A^{\dagger} = \frac{1}{6}\begin{bmatrix}2&3\\2&-3\\2&0\end{bmatrix}$ and $A^{\dagger}\mathbf{b} = (\frac{3}{2},\frac{1}{2},1)^T$, which does satisfy $A\mathbf{x}=(3,1)^T$.
The vector $\mathbf{k}=(-1,-1,2)^T$ spans $\operatorname{ker} A$ and $\langle A^{\dagger}\mathbf{b},\mathbf{k}\rangle = 0$, so every solution is $A^{\dagger}\mathbf{b}+t\mathbf{k}$.
An arm spends that $t$ on obstacles and joint limits, buying clearance at the price of joint speed.

6. $A^TA = \begin{bmatrix}3&3\\3&5\end{bmatrix}$ and $A^{\dagger} = \frac{1}{6}\begin{bmatrix}5&2&-1\\-3&0&3\end{bmatrix}$; all four conditions hold, and since $A^{\dagger}A=I_2$ three of them are immediate; the only one with content is the symmetry of $AA^{\dagger}$.
Then

$$
AA^{\dagger} = \frac{1}{6}\begin{bmatrix}5&2&-1\\2&2&2\\-1&2&5\end{bmatrix}
$$

satisfies both clauses of Definition 6.4 for $W=\operatorname{col}(A)$: its columns lie in $\operatorname{col}(A)$, and $A^T(I-AA^{\dagger}) = A^T-A^T=0$.
It annihilates $(1,-2,1)^T$, which spans $\operatorname{ker}(A^T) = \operatorname{col}(A)^\perp$.

7. Idempotence gives $V = \operatorname{im} P \oplus \operatorname{ker} P$, since $\mathbf{v} = P\mathbf{v} + (\mathbf{v}-P\mathbf{v})$ and $P(\mathbf{v}-P\mathbf{v})=\mathbf{0}$.
Self-adjointness makes the splitting orthogonal: for $\mathbf{u}\in\operatorname{im} P$, say $\mathbf{u}=P\mathbf{z}$, one has $\langle \mathbf{u},\mathbf{v}-P\mathbf{v}\rangle = \langle P\mathbf{z},\mathbf{v}\rangle-\langle P\mathbf{z},P\mathbf{v}\rangle = \langle\mathbf{z},P\mathbf{v}\rangle-\langle\mathbf{z},P^2\mathbf{v}\rangle = 0$.
So $P$ satisfies both clauses of Definition 6.4 for $W=\operatorname{im} P$, and the norm inequality is the Pythagorean identity applied to that splitting, with equality exactly when the second component vanishes.

8. $\langle A^TA\mathbf{x},\mathbf{x}\rangle = \langle A\mathbf{x},A\mathbf{x}\rangle = \|A\mathbf{x}\|^2$, so $A^TA\mathbf{x}=\mathbf{0}$ forces $A\mathbf{x}=\mathbf{0}$; the reverse inclusion is immediate, whence $\operatorname{ker}(A^TA)=\operatorname{ker} A$ and $A^TA$ is invertible exactly when that kernel is trivial.
For $P = A(A^TA)^{-1}A^T$: every $P\mathbf{v}$ is $A$ applied to something, so lies in $\operatorname{col}(A)$; and $A^T(I-P) = A^T - A^TA(A^TA)^{-1}A^T = 0$, so $\mathbf{v}-P\mathbf{v}$ is orthogonal to every column of $A$.

9. $T\mathbf{v}=\mathbf{0}$ if and only if $\langle T\mathbf{v},\mathbf{w}\rangle=0$ for all $\mathbf{w}\in W$, which by definition of the adjoint says $\langle\mathbf{v},T^*\mathbf{w}\rangle=0$ for all $\mathbf{w}$, i.e. $\mathbf{v}\perp\operatorname{im} T^*$.
The splitting is then Lemma 6.2(4).
For the normal equations, $T^*T\mathbf{x}=T^*\mathbf{b}$ says $T\mathbf{x}-\mathbf{b}\in\operatorname{ker} T^* = (\operatorname{im} T)^\perp$, and the unique vector of $\operatorname{im} T$ differing from $\mathbf{b}$ by an element of $(\operatorname{im} T)^\perp$ is $\Pi_{\operatorname{im} T}\mathbf{b}$.
Since $\Pi_{\operatorname{im} T}\mathbf{b}$ always lies in $\operatorname{im} T$ the system is always solvable, and it returns $T\mathbf{x}=\mathbf{b}$ exactly when $\Pi_{\operatorname{im} T}\mathbf{b}=\mathbf{b}$.

10. If $\mathbf{v}\perp U$ then $\|\mathbf{v}+\mathbf{u}\|^2 = \|\mathbf{v}\|^2+\|\mathbf{u}\|^2$, which exceeds $\|\mathbf{v}\|^2$ unless $\mathbf{u}=\mathbf{0}$; this gives minimality and uniqueness at once.
Conversely, if $\langle\mathbf{v},\mathbf{u}\rangle\neq 0$ for some $\mathbf{u}\in U$, then $\|\mathbf{v}+t\mathbf{u}\|^2 = \|\mathbf{v}\|^2+2t\langle\mathbf{v},\mathbf{u}\rangle+t^2\|\mathbf{u}\|^2$ dips below $\|\mathbf{v}\|^2$ at $t = -\langle\mathbf{v},\mathbf{u}\rangle/\|\mathbf{u}\|^2$, so $\mathbf{v}$ is not minimal.

11. $\operatorname{im} A\subseteq\operatorname{im} A'$, so the minimum of $\|\mathbf{b}-\mathbf{y}\|$ over the larger set is no larger; by Lemma 6.5 both minima are attained at the respective projections.
Writing $\mathbf{r} = \mathbf{b}-\Pi_{\operatorname{im} A}\mathbf{b}$, equality holds iff $\Pi_{\operatorname{im} A'}\mathbf{b} = \Pi_{\operatorname{im} A}\mathbf{b}$, iff $\mathbf{r}\perp\operatorname{im} A'$, and since $\mathbf{r}$ is already orthogonal to $\operatorname{im} A$ this reduces to $\langle\mathbf{c},\mathbf{r}\rangle=0$.
A column of pure noise shrinks the residual whenever it happens not to be orthogonal to $\mathbf{r}$, which for noise is almost certain; the residual falls for reasons having nothing to do with the model being better.

12. If $PQ=QP$ then $(PQ)^2 = P(QP)Q = P(PQ)Q = P^2Q^2 = PQ$ and $(PQ)^* = Q^*P^* = QP = PQ$, so Exercise 7 makes $PQ$ an orthogonal projection.
Conversely, if $PQ$ is an orthogonal projection it is self-adjoint, so $PQ = (PQ)^* = Q^*P^* = QP$ — the reverse implication uses self-adjointness alone and never touches idempotence.
When they commute, $PQ = \Pi_{U\cap W}$: its image lies in $U$ since $PQ=P(\cdot)$ and in $W$ since $PQ=QP$, while it fixes $U\cap W$ pointwise.

13. By Example 6.3, $\mathbb{R}^{n\times n} = \operatorname{sym}_n\boxplus\operatorname{skew}_n$ and $A$ splits as $\frac{1}{2}(A+A^T)+\frac{1}{2}(A-A^T)$ with the first term in $\operatorname{sym}_n$ and the second in $\operatorname{skew}_n$.
That is exactly the pair of clauses in Definition 6.4, so $\frac{1}{2}(A+A^T) = \Pi_{\operatorname{sym}_n}A$, and Lemma 6.5 makes it the nearest symmetric matrix, at distance the Frobenius norm of the skew part.
For the example, the nearest symmetric matrix is $\begin{bmatrix}1&2\\2&3\end{bmatrix}$ and the distance is $\|\begin{bmatrix}0&3\\-3&0\end{bmatrix}\|_F = 3\sqrt{2}$.

14. The function $h(x) = x(1-x)g(x)$ is continuous with $h(0)=h(1)=0$, so $h\in U$ and $0 = \langle g,h\rangle = \int_0^1 g(x)^2x(1-x)\,dx$.
The integrand is continuous and nonnegative, so it vanishes identically; as $x(1-x)>0$ on $(0,1)$ this gives $g=0$ there, and continuity finishes it.
So $U^\perp = \{\mathbf{0}\}$ and $(U^\perp)^\perp = V$, which is not $U$ since $1-x\notin U$.

15. Take $\mathbf{w}=\mathbf{v}_1\times\mathbf{v}_2 = (-3,2,1)^T$; rescaling $\mathbf{w}$ rescales the third coordinate and its quotient alike, so the comparison does not depend on the choice.
The true coordinates are $(\frac{11}{7},\frac{9}{14},\frac{1}{14})$; the three quotients are $(2,\frac{7}{6},\frac{1}{14})$.
Only the third agrees, because $\mathbf{w}$ alone is orthogonal to the rest of the basis; $\mathbf{v}_1$ and $\mathbf{v}_2$ have $\langle\mathbf{v}_1,\mathbf{v}_2\rangle = 2$, and each contaminates the other's quotient.
The recipe of Section 6.2 requires an orthogonal basis (orthonormal, if the denominators are to be dropped), and applied here it reconstructs $(\frac{62}{21},\frac{94}{21},\frac{19}{21})^T$ rather than $\mathbf{v}$.

16. $AB = \begin{bmatrix}1&1\\0&0\end{bmatrix}$, so $(AB)^{\dagger} = \frac{1}{2}\begin{bmatrix}1&0\\1&0\end{bmatrix}$, while $B^{\dagger} = \frac{1}{4}\begin{bmatrix}1&1\\1&1\end{bmatrix}$ and $A^{\dagger}=A$ give $B^{\dagger}A^{\dagger} = \frac{1}{4}\begin{bmatrix}1&0\\1&0\end{bmatrix}$, half the correct answer.
The wrong candidate satisfies both adjoint conditions and fails both consistency conditions of Definition 6.12.
The reason is that $\operatorname{im} B = \operatorname{span}\{(1,1)^T\}$ is not contained in $(\operatorname{ker} A)^\perp = \operatorname{span}\{\mathbf{e}_1\}$: $B^{\dagger}$ undoes $B$ only on $\operatorname{im} B$, and $A$ then discards part of what it returns, so the two undoings are performed on mismatched subspaces.

17. Weights inversely proportional to the variances are $\mathbf{w} = (1,1,4,1,1,4)$ up to scale, and $(A^TWA)\mathbf{c} = A^TW\mathbf{b}$ gives $a = \frac{19}{22}$ and $b = -\frac{557}{33}$, so $E \approx 0.8636\,T - 16.879$.
The residual is $(\frac{5}{33},-\frac{10}{33},\frac{7}{66},-\frac{29}{66},\frac{19}{66},-\frac{1}{33})^T$ and $A^TW\mathbf{r}=\mathbf{0}$.

18. Since $\Pi_{N}$ fixes $N$ pointwise, with $\mathbf{\epsilon}=\mathbf{0}$ we have $\mathbf{y}=\mathbf{s}+\mathbf{p}$ for some $\mathbf{p}\in N$, so $\Pi_{N}\mathbf{y} = \Pi_{N}\mathbf{s}+\mathbf{p} = \mathbf{p}$ when $\mathbf{s}\perp N$, and subtracting returns $\mathbf{s}$.
For the counterexample, $s(t) = \cos(\pi t/2)$ sampled at $t=0,\ldots,7$ is the vector $(1,0,-1,0,1,0,-1,0)^T$, which is the first spanning vector of $N$; the subtraction returns $\mathbf{0}$.
By contrast $s\equiv 1$ is orthogonal to both spanning vectors and passes through untouched.

19. Since $\mathbf{x}_\lambda$ beats $\mathbf{0}$, $\|A\mathbf{x}_\lambda-\mathbf{b}\|^2+\lambda\|\mathbf{x}_\lambda\|^2\leq\|\mathbf{b}\|^2$, giving $\|\mathbf{x}_\lambda\|\leq\|\mathbf{b}\|/\sqrt{\lambda}$.
Pairing $(A^TA+\lambda I)\mathbf{x}_\lambda = A^T\mathbf{b}$ with $\mathbf{z}\in\operatorname{ker} A$ kills the first and third terms, since $\langle A^TA\mathbf{x}_\lambda,\mathbf{z}\rangle = \langle A\mathbf{x}_\lambda,A\mathbf{z}\rangle = 0$ and $\langle A^T\mathbf{b},\mathbf{z}\rangle = \langle\mathbf{b},A\mathbf{z}\rangle = 0$, leaving $\lambda\langle\mathbf{x}_\lambda,\mathbf{z}\rangle=0$.
Subtracting $A^TA\mathbf{x}^+ = A^T\mathbf{b}$ gives $(A^TA+\lambda I)\mathbf{d} = -\lambda\mathbf{x}^+$, and pairing with $\mathbf{d}$ gives the stated identity; hence $\|\mathbf{d}\|\leq\|\mathbf{x}^+\|$ and $\|A\mathbf{d}\|^2\leq\lambda\|\mathbf{x}^+\|^2\to 0$.
Both $\mathbf{d}$ and $\mathbf{x}^+$ lie in $(\operatorname{ker} A)^\perp$, where Theorem 6.9(1) makes $A$ invertible onto $\operatorname{im} A$; that inverse is one fixed linear map $C$, and writing $C$ in orthonormal bases and applying Cauchy-Schwarz to each of its rows gives $\|\mathbf{d}\| = \|CA\mathbf{d}\|\leq c\,\|A\mathbf{d}\|$ for a constant $c$ depending only on $A$.
Hence $\mathbf{x}_\lambda\to\mathbf{x}^+$.

## Chapter 7

1. $\lambda = 2,-3$ with $\mathbf{v}=(2,1)^T,(1,-2)^T$; $e^{At}=\frac{1}{5}\begin{bmatrix} 4e^{2t}+e^{-3t} & 2e^{2t}-2e^{-3t}\\ 2e^{2t}-2e^{-3t} & e^{2t}+4e^{-3t}\end{bmatrix}$, and $\mathbf{x}(t)=e^{2t}(2,1)^T+e^{-3t}(1,-2)^T$.

2. $\lambda = 1,2,3$ with eigenvectors $(0,0,1)^T$, $(2,1,-7)^T$, $(1,0,-2)^T$; take these as the columns of $V$ and $\Lambda=\operatorname{diag}(1,2,3)$.
$\operatorname{tr} B = 6 = 1+2+3$ and $\det B = 6 = 1\cdot 2\cdot 3$.

3. Eigenvalues $0,-1,1,2$; four distinct real values, so $A$ is necessarily diagonalizable.
Solutions stay bounded exactly for $\mathbf{x}(0)$ in the $2$-dimensional subspace $\operatorname{ker} A\oplus\operatorname{ker}(A+I)$, on which they converge to a point of $\operatorname{ker} A$ — a line of equilibria, since $\det A=0$.

4. Roots $1,-1,-2$; basis $\{e^{t},e^{-t},e^{-2t}\}$ and $x=c_1e^{t}+c_2e^{-t}+c_3e^{-2t}$.
Bounded exactly when the growing coefficient $c_1=\tfrac13 x(0)+\tfrac12\dot{x}(0)+\tfrac16\ddot{x}(0)$ vanishes, i.e. when $2x(0)+3\dot{x}(0)+\ddot{x}(0)=0$.

5. $p_A(\lambda)=\lambda^2-7\lambda+10=(\lambda-2)(\lambda-5)$ and $A^2=\begin{bmatrix}11&7\\14&18\end{bmatrix}$, so $A^2-7A+10I$ is the zero matrix.
Hence $(A-2I)(A-5I)$ vanishes: the columns of $A-5I$ are multiples of $(1,-1)^T$, the $\lambda=2$ eigenvector, and the columns of $A-2I$ are multiples of $(1,2)^T$, the $\lambda=5$ eigenvector.

6. $A^k=\begin{bmatrix}1&k\\0&1\end{bmatrix}$, so the series sums exactly to $e^{At}=\begin{bmatrix}e^t&te^t\\0&e^t\end{bmatrix}$ with no diagonalization used.
Yet $\operatorname{ker}(A-I)=\operatorname{span}\{(1,0)^T\}$ is one-dimensional, so there is no second eigenvector with which to fill out $V$: the hypothesis of $n$ distinct eigenvalues fails, $1$ being the only eigenvalue, the eigenvectors do not span $\mathbb{R}^2$, and $A$ is not diagonalizable.

7. $A-\lambda I$ is triangular with diagonal $a_{ii}-\lambda$, so $p_A(\lambda)=\prod_i(a_{ii}-\lambda)$ and the roots, with multiplicity, are the diagonal entries; the displayed matrix has eigenvalue set $\{2,3\}$ but diagonal $2,2,3$.
Distinct diagonal entries give $n$ distinct real eigenvalues, hence an eigenbasis by Theorem 7.6, hence diagonalizability over $\mathbb{R}$.

8. $e^{At}=Ve^{\Lambda t}V^{-1}$ and each $e^{\lambda_it}\to0$, so $e^{At}\to0$ and $\mathbf{x}(t)=e^{At}\mathbf{x}_0\to\mathbf{0}$ for every initial condition.
For $R$ the eigenvalues $\pm2i$ are not real; $R^2=-4I$, so the series of Definition 7.10 splits into the cosine and sine series in $2t$, giving $e^{Rt}=(\cos 2t)I+\tfrac12(\sin 2t)R=\begin{bmatrix}\cos 2t&-\sin 2t\\ \sin 2t&\cos 2t\end{bmatrix}$, rotation by angle $2t$, for which no limit exists.

9. Matching $t^2$ coefficients of the two series leaves $\tfrac12(BA-AB)=0$, so the identity for all $t$ forces $AB=BA$; with Lemma 7.11, commuting is necessary and sufficient.
For $A=\operatorname{diag}(1,-1)$ and $B=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ the sum $A+B$ is symmetric, hence $e^{(A+B)t}$ is symmetric, while $e^{At}e^{Bt}$ transposes to $e^{Bt}e^{At}$ and is not.

10. Expanding entrywise, $A^2-\operatorname{tr}(A)A=(bc-ad)I=-\det(A)I$, so the expression vanishes identically in $a,b,c,d$.
Since $p_A(\lambda)=\lambda^2-\operatorname{tr}(A)\lambda+\det(A)$ for $2\times2$ matrices, the identity reads $p_A(A)=0$ — Cayley-Hamilton in this case.

11. From $Q-I=Q(I-Q^T)$ and $\det M^T=\det M$ one gets $\det(Q-I)=(-1)^n\det(Q)\det(Q-I)$, so $\det(Q-I)=0$ — and $1$ is an eigenvalue — whenever $(-1)^n\det Q\neq1$; this covers every rotation of $\mathbb{R}^3$ and every orthogonal $2\times2$ of determinant $-1$.
It is not a parity dichotomy: $J=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ is a rotation of $\mathbb{R}^2$ with eigenvalues $\pm i$ and no eigenvalue $1$.

12. From the series, $A\mathbf{v}=\lambda\mathbf{v}$ gives $A^k\mathbf{v}=\lambda^k\mathbf{v}$ and hence $e^A\mathbf{v}=e^\lambda\mathbf{v}$, with no diagonalizability used.
With $n$ distinct real $\lambda_i$ the $e^{\lambda_i}$ are distinct ($\exp$ is injective on $\mathbb{R}$) and Lemma 7.4 allows no more than $n$, so they are all the eigenvalues; then $\det e^A=e^{\operatorname{tr} A}$, never zero, in agreement with the invertibility already recorded in (7.9).

13. $P_1+P_2=I$ and $\lambda_1P_1+\lambda_2P_2=A$ are algebra valid for any two distinct scalars; $P_1P_2=0$ needs $(A-\lambda_1I)(A-\lambda_2I)=0$, hence the true eigenvalues, and then $P_i=P_i(P_1+P_2)=P_i^2$.
Multiplying $\lambda_1P_1+\lambda_2P_2=A$ by $P_i$ gives $AP_i=\lambda_iP_i$, so every nonzero column of $P_i$ is an eigenvector for $\lambda_i$.

14. $\det V = x_2-x_1$ for $n=2$ and $(x_2-x_1)(x_3-x_1)(x_3-x_2)$ for $n=3$, suggesting $\det V=\prod_{i<j}(x_j-x_i)$.
A product of differences vanishes exactly when two nodes coincide, which is precisely the nondegeneracy the proof of Theorem 7.15 requires.

15. $\operatorname{tr} A=0$ forces $\lambda_2=-\lambda_1$, so $\lambda=\pm\sqrt{-\det A}$ and distinct real eigenvalues require $\det A<0$; the portrait is a saddle.
$\det e^{At}=e^{(\operatorname{tr} A)t}=1$, so the flow carries every region to one of equal area: stretching by $e^{\lambda t}$ in one eigendirection is exactly paid for by compression by $e^{-\lambda t}$ in the other.

16. $\operatorname{tr} A=7$ and $\det A=8$ (the roots are $1,2,4$), and $A^3=7A^2-14A+8I$.
Distinct real eigenvalues make Cayley-Hamilton unnecessary: $A^3-7A^2+14A-8I=V(\Lambda^3-7\Lambda^2+14\Lambda-8I)V^{-1}$ by Lemma 7.9, and the diagonal factor vanishes because each $\lambda_i$ is a root of the cubic.

17. $(A-\lambda I)^T=A^T-\lambda I$ and $\det M^T=\det M$ give $\det(A^T-\lambda I)=\det(A-\lambda I)$, so $A$ and $A^T$ share eigenvalues; zero column sums put $(1,1,1)^T$ in $\operatorname{ker} A^T$, so $0$ is an eigenvalue of $A$.
$\operatorname{ker} A^T=\operatorname{span}(1,1,1)^T$ is the conservation law (total solute is constant) and $\operatorname{ker} A=\operatorname{span}(2,1,2)^T$ is the line of equilibria; the eigenvalues are $0,-1,-5$ and $\mathbf{x}(t)\to(4,2,4)^T$.
The eigenvectors are $(2,1,2)^T$, $(1,0,-1)^T$, $(1,-2,1)^T$ for $0,-1,-5$, and only the second has vanishing middle entry, so Theorem 7.15 gives $y(t)=c_1e^{0t}-2c_3e^{-5t}$.
Independence of distinct exponentials forces $c_1=c_3=0$, leaving $c_2$ free: the initial profiles the probe never sees are exactly $\operatorname{ker}(A+I)=\operatorname{span}(1,0,-1)^T$, the whole $\lambda=-1$ eigenspace and nothing else.

18. Eigenvalues $2,3$ with eigenvectors $(1,1)^T,(2,1)^T$; $A-DI$ has eigenvalues $2-D,3-D$, so every deviation decays exactly when $D>3$ (no smallest such $D$).
Since $(A-DI)-\lambda I=A-(\lambda+D)I$, the eigenvectors never move; at $D=3$ the equilibria fill the line $\operatorname{ker}(A-3I)=\operatorname{span}(2,1)^T$.

19. For $\mathbf{w}=\sum_ic_i\mathbf{v}_i\in W$ the vectors $A^k\mathbf{w}$, $k<n$, lie in $W$ and satisfy $[\,\mathbf{w}\ \cdots\ A^{n-1}\mathbf{w}\,]=[\,c_1\mathbf{v}_1\ \cdots\ c_n\mathbf{v}_n\,]V$ with $V$ Vandermonde in the distinct $\lambda_i$; inverting $V$ puts each $c_i\mathbf{v}_i$ in $W$.
Hence $W$ is the span of $\{\mathbf{v}_i:\mathbf{v}_i\in W\}$ and there are exactly $2^n$ invariant subspaces, whereas $A=I$ makes every subspace invariant.

20. The commuting product $\prod_{j\neq i}(A-\lambda_jI)$ annihilates $\mathbf{u}_j$ for $j\neq i$ and multiplies $\mathbf{u}_i$ by $\prod_{j\neq i}(\lambda_i-\lambda_j)\neq0$, so $\mathbf{u}_1+\cdots+\mathbf{u}_m=\mathbf{0}$ forces every $\mathbf{u}_i=\mathbf{0}$: the eigenspaces form a direct sum and their dimensions sum to at most $n$.
For $A=\begin{bmatrix}0&1\\0&0\end{bmatrix}$ the only eigenvalue is $0$ and $\dim\operatorname{ker} A=1<2$, so the inequality can be strict.

## Chapter 8

1. An eigenvector for $5+6i$ is $\mathbf{v}=(2i,1)^T$, so $\mathbf{u}=(0,1)^T$ and $\mathbf{w}=(2,0)^T$; taking $P=[\mathbf{u}\;\;{-\mathbf{w}}]=\begin{bmatrix}0&-2\\1&0\end{bmatrix}$ gives $P^{-1}AP=5I+6J$ and

$$
e^{At}=e^{5t}\begin{bmatrix}\cos6t & -2\sin6t\\ \tfrac{1}{2}\sin6t & \cos6t\end{bmatrix} .
$$

The invariant family is $x^2+4y^2$, so $c=4$.

2. $e^{At}=\operatorname{diag}\!\left(e^{-t}\begin{bmatrix}1&t\\0&1\end{bmatrix},\ \begin{bmatrix}1&t\\0&1\end{bmatrix}\right)$, with solution $\big((c_1+c_2t)e^{-t},\,c_2e^{-t},\,c_3+c_4t,\,c_4\big)$, bounded exactly when $c_4=0$: the subspace $w(0)=0$, of dimension three.
The block at $\lambda=0$ is responsible, since $t$ grows unopposed there, while $te^{-t}\to0$; a chain lengthens the polynomial factor but only matters for boundedness when the real part is zero.

3. $\operatorname{diag}(C,C)$ and $N$ commute because $C$ commutes with $I$, and $N^2=\mathbf{0}$, so $e^{Jt}=\begin{bmatrix}e^{Ct} & te^{Ct}\\ \mathbf{0} & e^{Ct}\end{bmatrix}$ with $e^{Ct}=\cos(\sqrt2\,t)I+\sin(\sqrt2\,t)J$.
Its first row is $\cos(\sqrt2\,t)$, $-\sin(\sqrt2\,t)$, $t\cos(\sqrt2\,t)$, $-t\sin(\sqrt2\,t)$ — Theorem 8.14(2) with $\alpha=0$, $\beta=\sqrt2$, $k=2$, up to sign.

4. $Q_0=\tfrac{1}{\sqrt5}\begin{bmatrix}2&-1\\1&2\end{bmatrix}$ and $R_0=\tfrac{1}{\sqrt5}\begin{bmatrix}5&4\\0&3\end{bmatrix}$, so $A_1=R_0Q_0=\begin{bmatrix}14/5 & 3/5\\ 3/5 & 6/5\end{bmatrix}$.
Symmetry survives because $A_1=Q_0^TA_0Q_0$ and the transpose of that is itself; $2.8$ and $1.2$ have moved toward $3$ and $1$.

5. $p_A(\lambda)=(\lambda-3)^2(\lambda^2-2\lambda+5)$, and $A-3I$ has rank $3$, so $\dim\operatorname{ker}(A-3I)=1$: one block at $\lambda=3$, necessarily of size two.
Hence

$$
J=\operatorname{diag}\!\left(\begin{bmatrix}1&-2\\2&1\end{bmatrix},\ \begin{bmatrix}3&1\\0&3\end{bmatrix}\right) .
$$

6. If $A\mathbf{v}=\lambda\mathbf{v}$ with $\mathbf{v}\neq\mathbf{0}$ then $\mathbf{0}=A^m\mathbf{v}=\lambda^m\mathbf{v}$, so $\lambda=0$; all $n$ roots of $p_A$ vanish and Lemma 7.4 fixes the leading coefficient, giving $p_A(\lambda)=(-1)^n\lambda^n$.
Cayley-Hamilton then reads $(-1)^nA^n=\mathbf{0}$, and the $5\times5$ matrix with ones on the superdiagonal has $N^4\neq\mathbf{0}$, $N^5=\mathbf{0}$.

7. The blocks at $\lambda$ total $m$ in size, so each has size at most $m$ and $(J_i-\lambda I)^m=\mathbf{0}$; a real block at $\mu\neq\lambda$ is triangular with $\mu-\lambda$ down its diagonal, and a complex block has $\det(C-\lambda I)=(\alpha-\lambda)^2+\beta^2>0$, so both remain invertible.
The kernel is therefore exactly the $\lambda$-blocks, of total dimension $m$.
For non-real $\lambda$ the matrix $A-\lambda I$ is not real at all, and the only real solution of $(A-\lambda I)\mathbf{x}=\mathbf{0}$ is $\mathbf{x}=\mathbf{0}$.

8. If $A=V\Lambda V^{-1}$ with both real then every eigenvalue is real, and $(A-\lambda I)^2=V(\Lambda-\lambda I)^2V^{-1}$ has the same kernel dimension as $A-\lambda I$ because a diagonal entry vanishes exactly when its square does.
Conversely, a filtration that stops at the first step makes $\dim\operatorname{ker}(A-\lambda I)$ the algebraic multiplicity by Lemma 8.5, and these sum to $n$ when all eigenvalues are real, supplying the eigenbasis of Lemma 7.8.
A rotation satisfies the kernel condition vacuously and fails realness; $\begin{bmatrix}2&1\\0&2\end{bmatrix}$ is real and fails the kernel condition.

9. Similarity leaves the trace alone, $e^{Jt}$ is block diagonal, and within a block the nilpotent part is strictly above the diagonal and contributes nothing; a real block of size $m$ therefore gives $me^{\lambda t}$ and a complex block of size $2k$ gives $2ke^{\alpha t}\cos(\beta t)$, which is the stated formula.
Every term is dominated by $e^{\lambda_jt}$ or $e^{\alpha_it}$, so all-negative exponents force the limit $0$; the rotation generator $\begin{bmatrix}0&-\beta\\\beta&0\end{bmatrix}$ has eigenvalues of real part zero and $\operatorname{tr}(e^{At})=2\cos(\beta t)$, which oscillates forever.

10. The eigenvalues are distinct, so $J=\operatorname{diag}\!\left(\begin{bmatrix}3&-4\\4&3\end{bmatrix},\begin{bmatrix}-2&-1\\1&-2\end{bmatrix}\right)$ and $e^{-3t}e^{Jt}$ is the rotation by $4t$ beside $e^{-5t}$ times the rotation by $t$.
The second block dies and the first never settles, so the quotient is bounded and has no limit; at $t_k=\pi k/2$ the rotation is the identity and the limit is $V\operatorname{diag}(1,1,0,0)V^{-1}$, the projection onto the $3\pm4i$ plane along the $-2\pm i$ plane, of rank two.

11. $J=\operatorname{diag}\big(J_3(-1),\,J_1(-1),\,J_2(2)\big)$: as chains, one of length $3$ beside one of length $1$ at $\lambda=-1$, and one of length $2$ at $\lambda=2$.
The datum $\dim\operatorname{ker}(A+I)=2$ is redundant: $\dim\operatorname{ker}(A+I)^2=3$ already forces the partition $3+1$ at $\lambda=-1$, while $\dim\operatorname{ker}(A-2I)=1$ is needed to choose $2$ over $1+1$.
Every one of these is a rank computation.

12. A rotation is orthogonal, so $Q=A$ and $R=I$ is the factorization with nonnegative diagonal, and $RQ=A$ returns the matrix unchanged forever.
A real triangular matrix carries its eigenvalues on its diagonal and so has real eigenvalues; a rotation by $\theta\neq0,\pi$ has none, so no real similarity whatever can triangularize it, and the $2\times2$ blocks are not the algorithm's failure but its best possible output.

13. With $C=\begin{bmatrix}1&-2\\2&1\end{bmatrix}$ the two forms are $\operatorname{diag}(C,C)$ and $\begin{bmatrix}C&I\\ \mathbf{0}&C\end{bmatrix}$.
The first satisfies $A^2-2A+5I=\mathbf{0}$; the second gives $\begin{bmatrix}\mathbf{0}&2(C-I)\\ \mathbf{0}&\mathbf{0}\end{bmatrix}\neq\mathbf{0}$, and it is the first that is diagonalizable over $\mathbb{C}$.

14. $\omega=2$ rad/s, and the roots $-\gamma\pm\sqrt{\gamma^2-\omega^2}$ collide at $c=2\sqrt{km}=8$ N$\cdot$s/m, giving $e^{-2t}$ and $te^{-2t}$.
The slower of the two, $-\gamma+\sqrt{\gamma^2-\omega^2}$, has derivative $1-\gamma/\sqrt{\gamma^2-\omega^2}<0$ for $\gamma>\omega$, so it falls from $\omega$ toward zero as the dashpot is stiffened.

15. $p_A(\lambda)=\lambda^2(\lambda^2+2\omega^2)$, with $\operatorname{ker} A=\operatorname{span}(1,1,0,0)^T$ one-dimensional and $\dim\operatorname{ker} A^2=2$, so $\lambda=0$ carries a single block of size two.
Its chain is $(0,0,1,1)^T\mapsto(1,1,0,0)^T\mapsto\mathbf{0}$: equal velocities, which the spring cannot feel, so the pair translates with $\mathbf{x}(t)=\mathbf{x}(0)+\mathbf{v}(0)t$, while the relative coordinate obeys $\ddot{r}=-2\omega^2r$ and merely oscillates.

16. In these coordinates $M$ has second row $(0,-d,1,0)$, so $p_M(\lambda)=\lambda^3(\lambda+d)$ and $\dim\operatorname{ker} M^k=1,2,3,3$: the form is $J_3(0)\oplus[-d]$ against the undamped counts $1,2,3,4$ and $J_4(0)$.
One integrator has become a decaying mode, so a tilt rate now drives $t^2$ rather than $t^3$ — and the eigenvalue zero, with it the drift, is still there.

17. Matching entries in $NX=XN$ gives $X_{i+1,j}=X_{i,j-1}$, while the empty last row of $NX$ and the empty first column of $XN$ kill everything below the diagonal; what remains is constant along each diagonal, so $X=c_0I+c_1N+\cdots+c_{n-1}N^{n-1}$ and the space has dimension $n$.
If $V^{-1}AV=\lambda I+N$ then $X$ commutes with $\lambda I+N$ as well, so $(VX)^{-1}A(VX)=\lambda I+N$ too: the free parameters move the basis and not the form.

18. Since $\big((A-\lambda I)^k\big)^T=(A^T-\lambda I)^k$ and transposition preserves rank, the two matrices have equal kernel dimensions at every eigenvalue and every power, and the census of Section 8.3 reads the same block sizes off both.
Their eigenvectors need not agree: $A=\begin{bmatrix}1&1\\0&1\end{bmatrix}$ has $\operatorname{ker}(A-I)=\operatorname{span}(1,0)^T$ while $A^T$ has $\operatorname{span}(0,1)^T$.

## Chapter 9

1. $A=\begin{bmatrix}0&1&0&1\\1&0&1&1\\0&1&0&1\\1&1&1&0\end{bmatrix}$ and $D=\operatorname{diag}(2,3,2,3)$, so $L=\begin{bmatrix}2&-1&0&-1\\-1&3&-1&-1\\0&-1&2&-1\\-1&-1&-1&3\end{bmatrix}$ with spectrum $\{0,2,4,4\}$.
$L\mathbf{1}=\mathbf{0}$ gives $0$; the swap of vertices $1$ and $3$ gives $(-1,0,1,0)^T$ with eigenvalue $2$; then $\operatorname{tr} L=10$ and $\operatorname{tr} L^2=\sum d_i^2+2|E|=36$ force the last pair to sum to $8$ and have squares summing to $32$, hence both equal $4$.
The multiplicity of $0$ is one, so the graph is connected, and the Fiedler vector separates $1$ from $3$ — the only pair of vertices not joined by an edge, and so the cheapest place to cut.

2. $P^2=\begin{bmatrix}0.39&0.33&0.29\\0.39&0.37&0.35\\0.22&0.30&0.36\end{bmatrix}$ and $P^3=\begin{bmatrix}0.356&0.336&0.322\\0.378&0.370&0.364\\0.266&0.294&0.314\end{bmatrix}$, with the columns converging to $\mathbf{\pi}=(21,23,18)^T/62$.
Column $j$ of $P^k$ is $P^k\mathbf{e}_j$, the distribution after $k$ steps from state $j$; the columns agreeing is exactly the statement that the answer no longer depends on $j$.
$P$ is strictly positive, hence ergodic, so clause 2 of Theorem 9.16 gives $P^k\to\mathbf{\pi}\mathbf{1}^T$ — the columns agreeing *is* that limit, entry by entry.
The eigenvalues are $1$ and $(2\pm\sqrt2)/10$, so $|\lambda_2|=(2+\sqrt2)/10\approx0.341$ predicts a spread of $0.341^3\approx0.040$ at the third step, against an observed largest gap of $0.048$.

3. $A^2=\begin{bmatrix}1&0&1\\0&2&0\\1&0&1\end{bmatrix}$, $A^3=2A$, $A^4=2A^2$, $A^5=4A$; in general $A^{2k+1}=2^kA$ and $A^{2k}=2^{k-1}A^2$, the relation $A^3=2A$ being the minimal polynomial $\lambda(\lambda^2-2)$ at work.
The path is bipartite with classes $\{1,3\}$ and $\{2\}$, so a walk of length $k$ joins $i$ to $j$ only when $k$ has the parity of the distance between them (Exercise 6); the odd powers are zero on the diagonal blocks and the even powers off them.
Then $P=AD^{-1}=\begin{bmatrix}0&1/2&0\\1&0&1\\0&1/2&0\end{bmatrix}$ has spectrum $\{1,0,-1\}$: the chain is irreducible but has period $2$, aperiodicity fails, and for every $\mathbf{x}(0)$ other than the fixed $(1/4,1/2,1/4)^T$ the iterates alternate forever between two distributions, averaging to that vector but converging to nothing.

4. Clearing common factors, the iterates are $(1,0,0)$, $(4,1,1)$, $(2,1,1)$, $(10,7,7)$, $(6,5,5)$, $(34,31,31)$, heading for $(1,1,1)$, with Rayleigh quotients

$$
4,\quad 5,\quad \tfrac{17}{3},\quad \tfrac{65}{11},\quad \tfrac{257}{43},\quad \tfrac{1025}{171}\ \longrightarrow\ 6
$$

Since $A^n\mathbf{x}_0/6^n=\tfrac13\mathbf{1}+2^{-n}\cdot\tfrac13(2,-1,-1)^T$, an iterate normalized to unit sum exceeds $\tfrac13\mathbf{1}$ in its first coordinate by $\tfrac23,\tfrac13,\tfrac16,\tfrac1{12},\tfrac1{24},\tfrac1{48}$: halved exactly at every step.
The quotient's errors are $6-R_n=6/(4^n+2)$, whose successive ratios climb to $\tfrac14$ without reaching it — squared, not linear.
The reason is Exercise 8: the Rayleigh quotient attains its maximum at the dominant eigenvector, so it is stationary there and a direction error of size $\epsilon$ costs it only $\epsilon^2$.

5. The block form is read off the labelling: within each square a vertex is adjacent to two others, giving $B$ twice down the diagonal, and each rung contributes a single $1$, giving $I$ off it.
If $B\mathbf{u}=\mu\mathbf{u}$ then

$$
\begin{bmatrix}B&I\\I&B\end{bmatrix}\begin{pmatrix}\mathbf{u}\\\pm\mathbf{u}\end{pmatrix}
    =\begin{pmatrix}\mu\mathbf{u}\pm\mathbf{u}\\\mathbf{u}\pm\mu\mathbf{u}\end{pmatrix}
    =(\mu\pm1)\begin{pmatrix}\mathbf{u}\\\pm\mathbf{u}\end{pmatrix}
$$

The four-cycle has spectrum $\{2,0,0,-2\}$, so the cube has $\pm3$ once each and $\pm1$ three times each.
The eight vectors so produced are independent: a vanishing combination forces $\sum(a_i\pm b_i)\mathbf{u}_i=\mathbf{0}$ in each block, hence $a_i=b_i=0$.
So nothing is missed.
Then $W=A/3$ has spectrum $\pm1$ together with $\pm\tfrac13$ three times each.
The eigenvalue $-1$ says the cube is bipartite and the walk has period $2$, so the chain is *not* ergodic and $W^n\mathbf{x}(0)$ does not converge: it oscillates between the two parity classes, averaging to the uniform distribution.

6. Induction on $k$. The case $k=1$ is the definition of the adjacency matrix.
A walk of length $k+1$ from $j$ to $i$ is an edge $j\to m$ followed by a walk of length $k$ from $m$ to $i$, and the second vertex $m$ partitions these walks, so the count is $\sum_m (A^k)_{im}a_{mj}=(A^{k+1})_{ij}$.
That sum is the definition of matrix multiplication: composing one-step transitions *is* multiplying matrices.

7. Suppose $A=A^T$ has the pair $\alpha\pm i\beta$, giving $A\mathbf{u}=\alpha\mathbf{u}-\beta\mathbf{w}$ and $A\mathbf{w}=\beta\mathbf{u}+\alpha\mathbf{w}$ with $\mathbf{u},\mathbf{w}$ not both zero.
Then $\mathbf{w}^TA\mathbf{u}=\alpha\,\mathbf{w}^T\mathbf{u}-\beta\|\mathbf{w}\|^2$ and $\mathbf{u}^TA\mathbf{w}=\beta\|\mathbf{u}\|^2+\alpha\,\mathbf{u}^T\mathbf{w}$; symmetry makes these equal, the $\alpha$ terms cancel, and $\beta\left(\|\mathbf{u}\|^2+\|\mathbf{w}\|^2\right)=0$ forces $\beta=0$.
For the second clause, $\mathbf{v}_1^TA\mathbf{v}_2$ equals $\lambda_2\,\mathbf{v}_1^T\mathbf{v}_2$ read one way and $\lambda_1\,\mathbf{v}_1^T\mathbf{v}_2$ read the other, so $(\lambda_1-\lambda_2)\mathbf{v}_1^T\mathbf{v}_2=0$.

8. Write $\mathbf{x}=\sum_ic_i\mathbf{q}_i$ with $\sum_ic_i^2=1$.
Then $q(\mathbf{x})=\sum_i\lambda_ic_i^2$, a weighted average of the eigenvalues with weights summing to one, so $\lambda_n\leq q(\mathbf{x})\leq\lambda_1$, with equality at the top exactly when all the weight sits on the $\lambda_1$ eigenspace.
Taking $\mathbf{x}=(\cos\theta)\mathbf{q}_1+(\sin\theta)\mathbf{q}_n$ gives $q=\lambda_1\cos^2\theta+\lambda_n\sin^2\theta$, which sweeps the whole interval as $\theta$ runs from $0$ to $\pi/2$.

9. $\left(P\tfrac1n\mathbf{1}\right)_i=\tfrac1n\sum_jp_{ij}$, which is $\tfrac1n$ times the $i$th *row* sum: the row condition is what the proof consumes, while the column condition is what makes $P$ a transition matrix at all.
It need not be unique: $P=I$ is doubly stochastic and fixes everything, and the block sum of two $2\times2$ swaps fixes $(t,t,\tfrac12-t,\tfrac12-t)^T$ for every $t$.
Irreducibility restores uniqueness, since it makes the eigenvalue $1$ simple by Lemma 9.15.

10. $\sum_i\tilde p_{ij}=\tfrac1{\pi_j}\sum_i\pi_ip_{ji}=\tfrac{(P\mathbf{\pi})_j}{\pi_j}=1$, and $(\tilde P\mathbf{\pi})_i=\sum_j\tfrac{\pi_i}{\pi_j}p_{ji}\pi_j=\pi_i\sum_jp_{ji}=\pi_i$; the first uses stationarity of $\mathbf{\pi}$ and the second column-stochasticity of $P$, and nothing else.
Reading $\left(DP^TD^{-1}\right)_{ij}=\pi_i p_{ji}\pi_j^{-1}$ identifies $\tilde P$ as similar to $P^T$, and a matrix and its transpose share a characteristic polynomial, so $\tilde P$ and $P$ have the same spectrum.
Finally $\tilde P=P$ says $\pi_jp_{ij}=\pi_ip_{ji}$, and for the random walk on a graph both sides equal $1/2|E|$, since $p_{ij}=1/\deg(j)$ on an edge and $\pi_i=\deg(i)/2|E|$.

11. Apply Lemma 5.5 to the vectors with entries $\sqrt{p_{ij}}$ and $\sqrt{p_{ij}}\,x_j$: $\left(\sum_jp_{ij}x_j\right)^2\leq\left(\sum_jp_{ij}\right)\left(\sum_jp_{ij}x_j^2\right)=\sum_jp_{ij}x_j^2$ by the row sums, and summing over $i$ and using the column sums gives $\|P\mathbf{x}\|^2\leq\|\mathbf{x}\|^2$.
Powers of a doubly stochastic matrix are doubly stochastic, so the bound iterates.
For the counterexample $P\mathbf{x}=(9/5,-9/5,0)^T$ and the ratio is $3\sqrt3/5\approx1.039$.
What fails is not Cauchy-Schwarz itself, which still gives $3.24\leq 1.9\times2$, but the substitution of $1$ for $\sum_jp_{1j}$ immediately after it: the first row of that $P$ sums to $57/30$.

12. Deleting index $j$ turns $m_{ij}=1+\sum_{k\neq j}p_{ki}m_{kj}$ into $\mathbf{m}=\mathbf{1}+Q^T\mathbf{m}$, since $\sum_kp_{ki}m_{kj}$ reads the $i$th *column* of $Q$ against $\mathbf{m}$.
The $i$th column of $Q$ sums to $1-p_{ji}$, and irreducibility puts a path from every state to $j$, so mass leaks out of $Q$ and the maximal-coordinate argument that proved Lemma 9.15 gives $\rho_Q<1$; hence $I-Q^T$ is invertible and $\mathbf{m}=(I-Q^T)^{-1}\mathbf{1}$.
For the weather matrix every $p_{ji}$ is already positive, so every such column sum is strictly below one outright, and $m_{21}=\tfrac{80}{21}$, $m_{31}=\tfrac{30}{7}$, $m_{12}=\tfrac{60}{13}$, $m_{32}=\tfrac{50}{13}$, $m_{13}=\tfrac{20}{3}$, $m_{23}=5$.
The return times come out as $\tfrac{46}{21},\tfrac{46}{13},\tfrac{23}{6}$, which are exactly $1/\pi_j$: a state is revisited, on average, once every $1/\pi_j$ steps.

13. If $\lambda_*$ were not real then $\overline{\lambda_*}$ would be a different eigenvalue of the same magnitude, which dominance forbids.
For $A=\begin{bmatrix}1&-1\\1&1\end{bmatrix}$ the eigenvalues are $1\pm i$, both of magnitude $\sqrt2=\rho_A$, so there is no dominant eigenvalue and Lemma 9.3 is unavailable.
Indeed $A$ is $\sqrt2$ times a rotation by $\pi/4$, so $\|A^n\mathbf{x}\|=\rho_A^n\|\mathbf{x}\|$ exactly, while $A^8=16I$ returns every direction to where it started.

14. $I+hA$ has eigenvalues $1-2h$ and $1-20h$, so its spectral radius is $\max(|1-2h|,|1-20h|)$, which is less than one exactly for $0<h<1/10$; at $h=1/10$ the fast mode sits at $-1$ and oscillates without decaying.
The exact step $e^{hA}$ has eigenvalues $e^{-2h}$ and $e^{-20h}$, in $(0,1)$ for every $h>0$, so it never fails.
The eigenvalue $-20$ is what destroys the Euler scheme, and it is *not* the one that governs the flow: long-run behavior is set by $-2$, the slowest mode, while the step size is dictated by the fastest.

15. Every power of the cyclic permutation is again a permutation matrix, so no power is strictly positive; it is irreducible, since the cycle reaches every state from every other.
Its characteristic polynomial is $\lambda^n-1$ up to sign, so its eigenvalues are the $n$th roots of unity, all of magnitude $1=\rho$, and there is no dominant eigenvalue — irreducibility alone cannot deliver one.
For the second part, $P^{k+1}\mathbf{v}=P(\lambda^k\mathbf{v})=\lambda^{k+1}\mathbf{v}$ by induction; $P^m$ is stochastic and strictly positive, so Theorem 9.6 makes $1$ its dominant eigenvalue, and $\lambda^m$, having magnitude $1$, can only be that one.
Every column of $P$ carries a positive entry, so $(P^mP)_{ij}>0$ as well and $\lambda^{m+1}=1$; dividing, $\lambda=1$.

16. $W=A/2$ has spectrum $\{1,0,0,-1\}$ and satisfies $W^3=W$ exactly, so from $\mathbf{x}(0)=(1,0,0,0)^T$ the states alternate between $(0,\tfrac12,0,\tfrac12)^T$ and $(\tfrac12,0,\tfrac12,0)^T$ forever: aperiodicity is the hypothesis that fails.
Every edge of the square joins an odd-numbered vertex to an even-numbered one, so $S=\operatorname{diag}(1,-1,1,-1)$ gives $SWS^{-1}=-W$ for any weighting supported on the edges; the spectrum is therefore symmetric about the origin, and since an averaging matrix fixes $\mathbf{1}$ and so always carries the eigenvalue $1$, it always carries $-1$ too.
With $W=I-\epsilon L$ the spectrum is $\{1,1-2\epsilon,1-2\epsilon,1-4\epsilon\}$, so $|\lambda_2|=\max(|1-2\epsilon|,|1-4\epsilon|)$ is smallest at $\epsilon=1/3$, where it equals $1/3$. (At $\epsilon=1/2$ one recovers $A/2$ and its failure.)

17. The transition matrix has columns $\mathbf{e}_0$, $(\tfrac23,0,\tfrac13,0)^T$, $(0,\tfrac23,0,\tfrac13)^T$, $\mathbf{e}_3$.
First-step conditioning gives $h_1=\tfrac13h_2$ and $h_2=\tfrac13+\tfrac23h_1$, so $h_1=\tfrac17$ and $h_2=\tfrac37$: the gambler reaches \$3 from \$2 with probability $3/7$.
Two absorbing states make the chain reducible, so the eigenvalue $1$ has multiplicity two, there is a whole segment of stationary distributions, and Theorem 9.16 does not apply.

18. With $\mathbf{y}=\mathbf{1}$ the trapping inequality reads $\min_i(A\mathbf{1})_i\leq\rho_A\leq\max_i(A\mathbf{1})_i$, and the row sums are $0.6,\,0.9,\,0.7$, so $0.6\leq\rho_A\leq0.9<1$ and $1$ is not an eigenvalue of $A$.
Hence $I-A$ is invertible, with $(I-A)^{-1}=\tfrac1{17}\begin{bmatrix}30&14&12\\15&41&23\\10&16&38\end{bmatrix}$, and $\mathbf{x}=(I-A)^{-1}\mathbf{d}=(100,200,100)^T$.
In Example 9.1 the same inequality applied to $A^T$, which has the same spectrum, reads $1.00\leq\rho_A\leq1.15$ off the column sums — no bound below one is available, and in truth $\rho_A\approx1.09$: there the equation has no nonnegative solution for nonnegative demand, and the economy grows rather than settling.

19. $P^3\mathbf{e}_1=\left(\tfrac{32}{125},\tfrac{69}{250},\tfrac{117}{250}\right)^T$, so green is lit after exactly three presses with probability $117/250=0.468$, while the long-run fractions are $\mathbf{\pi}=(\tfrac14,\tfrac14,\tfrac12)^T$.
They would already agree at the third press if the third row of $P^3$ were constant, and the cleanest way to arrange that is for the third row of $P$ itself to be constant — for the chance of landing on green not to depend on which button is lit now.

20. The Rayleigh quotient settles within half a dozen steps on $\rho\approx2.6412$; the eigenvector is slower, since $|\lambda_2|/\rho\approx0.67$, and takes about a dozen steps — alternating about the limit, $\lambda_2$ being negative — to reach, at unit sum,

$$
(0.2515,\ 0.2223,\ 0.2515,\ 0.1905,\ 0.0842)^T
$$

Vertices $1$, $2$ and $3$ share degree $3$, and the ranking demotes vertex $2$: one of its three edges is spent on the pendant vertex $5$, which has almost no score to lend, while $1$ and $3$ spend theirs on each other and on vertex $4$.
Degree counts a vertex's neighbours; centrality weights each neighbour by what that neighbour is itself worth, and the fixed point of that weighting is what Theorem 9.9 guarantees exists and is positive, the graph being connected and non-bipartite.

21. Ergodicity makes $P$ primitive, so $P^m$ is strictly positive for some $m$ and Theorem 9.6 gives it a dominant, simple $\rho=1$ with a strictly positive eigenvector; by Exercise 15 the only eigenvalue of $P$ of magnitude one is $1$ itself, and it is simple, so $1$ is dominant for $P$.
Normalize its eigenvector to unit sum to get $\mathbf{\pi}$, which is the unique stationary distribution — clause 1.
Simplicity transfers: were $1$ a repeated root for $P$ it would be one for $P^m$, which Theorem 9.6 forbids.
Lemma 9.3 applied to $\mathbf{e}_j$ gives $P^k\mathbf{e}_j\to c_j\mathbf{\pi}$, and the Jordan estimate of Section 9.2 gives the same limit when $P$ is not diagonalizable; since $\mathbf{1}^TP^k\mathbf{e}_j=1$ for every $k$ and $\mathbf{1}^T\mathbf{\pi}=1$, the constant is $c_j=1$, so every column of $P^k$ tends to $\mathbf{\pi}$ and $P^k\to\mathbf{\pi}\mathbf{1}^T$ — clause 2, and clause 3 is the ratio $|\lambda_k/\lambda_*|^n$ that drives that lemma's proof.

22. Extend $\mathbf{x}_F$ by zero to a vector $\mathbf{x}$ on all $n$ vertices. In the block form of $L$ the cross terms are multiplied by the zero block, so $\mathbf{x}^TL\mathbf{x}=\mathbf{x}_F^TL_{FF}\mathbf{x}_F$; and by the edge identity this equals $\sum_{\{i,j\}\in E}(x_i-x_j)^2$, which is the disagreement of the extended pattern.
A sum of squares vanishes only when every term does, so $\mathbf{x}$ must be constant on each connected component; the graph is connected and $\mathbf{x}$ is zero on the nonempty stubborn set, so that constant is zero and $\mathbf{x}_F=\mathbf{0}$.
Hence $L_{FF}$ is positive definite, in particular invertible, and $L_{FF}\mathbf{x}_F=-L_{FS}\mathbf{x}_S$ has exactly one solution.
Grounding has emptied the kernel of locally constant vectors, which is precisely the kernel that made consensus inevitable and the unforced equilibrium non-unique.

## Chapter 10

1. For the first, $A^TA=\begin{bmatrix}65&32\\32&17\end{bmatrix}$ has eigenvalues $81$ and $1$, so

$$
U=\frac{1}{\sqrt5}\begin{bmatrix}1&-2\\2&1\end{bmatrix},\quad
    \Sigma=\operatorname{diag}(9,1),\quad
    V=\frac{1}{\sqrt5}\begin{bmatrix}2&-1\\1&2\end{bmatrix}
$$

Then $\sigma_1\sigma_2=9=|\det A|$.
For the second, $A^TA=\begin{bmatrix}14&3\\3&6\end{bmatrix}$ has eigenvalues $15$ and $5$, so $\sigma_1=\sqrt{15}$ and $\sigma_2=\sqrt5$, with

$$
V=\frac{1}{\sqrt{10}}\begin{bmatrix}3&-1\\1&3\end{bmatrix},\quad
    \mathbf{u}_1=\frac{(2,1,1)^T}{\sqrt6},\quad
    \mathbf{u}_2=\frac{(0,1,-1)^T}{\sqrt2}
$$

Step 3 completes $U$ from $(\operatorname{im} A)^\perp=\operatorname{ker}(A^T)$, a line, contributing $\mathbf{u}_3=(-1,1,1)^T/\sqrt3$ up to sign, and $\Sigma$ carries $\sqrt{15},\sqrt5$ on the diagonal of a $3\times2$ frame.

2. $\langle t^{i-1},t^{j-1}\rangle=\int_0^1t^{i+j-2}\,dt=1/(i+j-1)=h_{ij}$, so $H_n$ is the Gram matrix of the monomials; a Gram matrix is symmetric, and $\mathbf{c}^TH_n\mathbf{c}=\|\sum_kc_kt^{k-1}\|^2$, which vanishes only for $\mathbf{c}=\mathbf{0}$ because the monomials are independent.
The condition numbers for $n=2,\ldots,6$ are $1.93\times10^1$, $5.24\times10^2$, $1.55\times10^4$, $4.77\times10^5$ and $1.50\times10^7$, so each added monomial multiplies the conditioning by $27.2$, $29.6$, $30.7$, $31.4$ in turn: call it a factor of $30$.
The ratios are still climbing at $n=6$, toward the asymptotic $(1+\sqrt2)^4\approx34$ that they have not reached in this range.

3. $A^TA$ has the two rows $(5,1,5,1)$ and $(1,5,1,5)$ each written twice, and is diagonalized by $\mathbf{v}_1=\tfrac12(1,1,1,1)^T$, $\mathbf{v}_2=\tfrac12(1,-1,1,-1)^T$, $\mathbf{v}_3=(1,0,-1,0)^T/\sqrt2$, $\mathbf{v}_4=(0,1,0,-1)^T/\sqrt2$ with eigenvalues $12,8,0,0$.
So $\sigma_1=2\sqrt3$, $\sigma_2=2\sqrt2$, and

$$
\mathbf{u}_1=\frac{(1,1,1)^T}{\sqrt3},\quad
    \mathbf{u}_2=\frac{(1,0,-1)^T}{\sqrt2},\quad
    \mathbf{u}_3=\frac{(1,-2,1)^T}{\sqrt6}
$$

Thus $\operatorname{im} A=\operatorname{span}\{\mathbf{u}_1,\mathbf{u}_2\}$, $\operatorname{coker} A=\operatorname{span}\{\mathbf{u}_3\}$, $\operatorname{coim} A=\operatorname{span}\{\mathbf{v}_1,\mathbf{v}_2\}$ and $\operatorname{ker} A=\operatorname{span}\{\mathbf{v}_3,\mathbf{v}_4\}$, with $2+2=4$ and $2+1=3$ as Corollary 6.11 requires, and the two splittings $\mathbb{R}^4=\operatorname{coim} A\boxplus\operatorname{ker} A$ and $\mathbb{R}^3=\operatorname{im} A\boxplus\operatorname{coker} A$ exhibited outright.
The freedom is exactly one continuous parameter and four binary choices: $\mathbf{v}_3,\mathbf{v}_4$ may be replaced by any orthonormal basis of the two-dimensional kernel, and the group of such changes is $O(2)$, of dimension $1$ and with two components — an angle and a reflection; $\mathbf{u}_3$ spans a line and carries a sign; and since $\sigma_1\neq\sigma_2$ the pairs $(\mathbf{v}_1,\mathbf{u}_1)$ and $(\mathbf{v}_2,\mathbf{u}_2)$ are determined up to one sign apiece, spent on the two members together.

4. $A$ is symmetric with eigenvalues $101$ and $-1$, so $\sigma_1=101$ and $\sigma_2=1$, with $\mathbf{v}_1=\mathbf{u}_1=(1,1)^T/\sqrt2$ and $\mathbf{u}_2=-\mathbf{v}_2=(1,-1)^T/\sqrt2$; the displacement is $(1,-1)^T=\sqrt2\,\mathbf{u}_2$, with no $\mathbf{u}_1$ component whatever.
Against $A^{-1}(101,101)^T=(1,1)^T$, the three filters return

$$
A^\dagger\mathbf{b}=\begin{bmatrix}0\\2\end{bmatrix},\qquad
    A_1^\dagger\mathbf{b}=\begin{bmatrix}1\\1\end{bmatrix},\qquad
    \frac{1}{20909}\begin{bmatrix}20400\\20606\end{bmatrix}
$$

the last because $\lambda=202$ makes $\sigma_i/(\sigma_i^2+\lambda)$ exactly $101/10403=1/103$ and $1/203$.
Since $1/\sigma_2=1$, the factor by which each filter multiplies the displacement is just its value at $\sigma_2$: the pseudoinverse multiplies it by $1$ and admits $(1,-1)^T$ undamped, so the answer moves by $(-1,1)^T$; truncation multiplies it by $0$; ridge multiplies it by $1/203$, moving the answer by $(-1,1)^T/203$.
A one-percent change in $\mathbf{b}$ becoming a hundred-percent change in $\mathbf{x}$ is $\operatorname{cond}(A)=101$ doing its work; ridge pays for suppressing it by shrinking the surviving component to $101/103$ of its true size.

5. $A^TA=\begin{bmatrix}8&-14\\-14&29\end{bmatrix}$ has eigenvalues $36$ and $1$, so $\sigma_1=6$, $\sigma_2=1$, and $\sigma_1\sigma_2=6=|\det A|$; the frames are $\mathbf{v}_1=(-1,2)^T/\sqrt5$, $\mathbf{v}_2=(2,1)^T/\sqrt5$, $\mathbf{u}_1=(-2,-1)^T/\sqrt5$, $\mathbf{u}_2=(-1,2)^T/\sqrt5$.
Then

$$
H=U\Sigma U^T=\begin{bmatrix}5&2\\2&2\end{bmatrix},
    \qquad
    Q=UV^T=\begin{bmatrix}0&-1\\1&0\end{bmatrix}
$$

with $H^2=AA^T=\begin{bmatrix}29&14\\14&8\end{bmatrix}$ and $HQ=A$; $H$ has eigenvalues $6$ and $1$, hence is positive definite, and $Q$ is the counterclockwise quarter-turn.
If $A$ is itself symmetric positive definite then $U=V$ and $\Sigma=\Lambda$, so $H=A$ and $Q=I$: there is nothing left to turn.

6. The $i$th diagonal entry of $A^TA$ is the squared length of the $i$th column of $A$, so the trace collects every $a_{ij}^2$ exactly once.
Taking traces in $A^TA=\sum_i\sigma_i^2\mathbf{v}_i\mathbf{v}_i^T$ and using $\operatorname{tr}(\mathbf{v}_i\mathbf{v}_i^T)=\|\mathbf{v}_i\|^2=1$ gives $\|A\|_F^2=\sum_{i=1}^p\sigma_i^2$.
Finally $\|A\|_F^2=\sum_i\sigma_i^2\geq\sigma_1^2=\|A\|_2^2$, with equality only when the rank is at most one, so the Frobenius norm overstates the gain of every matrix of higher rank.

7. $\det A=\det U\det\Sigma\det V^T$, and clause 5 of Lemma 5.19 makes the two outer determinants $\pm1$, so $|\det A|=\det\Sigma=\prod_i\sigma_i$.
Each $\sigma_i\leq\sigma_1=\|A\|_2$, whence $|\det A|\leq\|A\|_2^{\,n}$.
Equality forces $\sigma_1=\cdots=\sigma_n$, so $\Sigma=\sigma_1I$ and $A=\sigma_1UV^T$ is $\sigma_1$ times an orthogonal matrix; conversely any such matrix has all its singular values equal and meets the bound.

8. If $M=Q\Lambda Q^T$ has no negative eigenvalue, then $H=Q\Lambda^{1/2}Q^T$ is symmetric and its quadratic form is $\sum_i\sqrt{\lambda_i}\,(\mathbf{q}_i^T\mathbf{x})^2\geq0$, so $H$ is positive semidefinite, and $H^2=M$.
For uniqueness: $HM=H^3=MH$, so $H$ preserves each eigenspace of $M$, and on the $\lambda$-eigenspace the restriction is symmetric with square $\lambda I$, hence diagonalizable with eigenvalues $\pm\sqrt\lambda$ — and semidefiniteness leaves only $\sqrt\lambda$.
Every eigenspace is thereby forced, so $H$ is.
For the polar factor, $A$ nonsingular makes $AA^T$ positive definite and $H$ invertible, and $Q=H^{-1}A$ satisfies $Q^TQ=A^T(H^2)^{-1}A=A^T(AA^T)^{-1}A=I$; if also $A=HQ'$ then $Q'=H^{-1}A=Q$.

9. For any unit $\mathbf{x}$, $\|(A\pm A^T)\mathbf{x}\|\leq\|A\mathbf{x}\|+\|A^T\mathbf{x}\|\leq\sigma_1(A)+\sigma_1(A^T)=2\sigma_1(A)$, which is both bounds.
If $A\mathbf{x}=\lambda\mathbf{x}$ with $\mathbf{x}$ a unit vector and $|\lambda|=\sigma_1$, then $\|A\mathbf{x}\|=\sigma_1$ is maximal, so $A^TA\mathbf{x}=\sigma_1^2\mathbf{x}$ and therefore $A^T\mathbf{x}=(\sigma_1^2/\lambda)\mathbf{x}=\lambda\mathbf{x}$; then $(A+A^T)\mathbf{x}=2\lambda\mathbf{x}$ and the first bound is met.
If $A\mathbf{x}=\sigma_1\mathbf{y}$ and $A\mathbf{y}=-\sigma_1\mathbf{x}$ on an orthonormal pair, the same reading gives $A^T\mathbf{x}=-\sigma_1\mathbf{y}$, so $(A-A^T)\mathbf{x}=2\sigma_1\mathbf{y}$ and the second is met.
The identity meets the first and fails the second, since $\sigma_1(I-I^T)=0$; the quarter-turn $\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ meets the second and fails the first.
Symmetry is not necessary:

$$
A=\begin{bmatrix}1&0&0\\0&0&1/2\\0&0&0\end{bmatrix}
$$

is neither symmetric nor skew, has singular values $1,\tfrac12,0$ and the real eigenvalue $1$ at $\mathbf{e}_1$, and $A+A^T$ has singular values $2,\tfrac12,\tfrac12$ — equality in the first bound.

10. Submultiplicativity, used once on each factor, gives

$$
\operatorname{cond}(AB)=\|AB\|_2\,\|B^{-1}A^{-1}\|_2
    \leq \|A\|_2\|B\|_2\|B^{-1}\|_2\|A^{-1}\|_2
$$

and the right side is $\operatorname{cond}(A)\operatorname{cond}(B)$.
If the right singular vectors of $A$ are the left singular vectors of $B$ in matching order, the middle factors cancel: $AB=U_A(\Sigma_A\Sigma_B)V_B^T$, and the entrywise product of two descending nonnegative lists is descending, so $\sigma_i(AB)=\sigma_i(A)\sigma_i(B)$ and the ratio is exactly $\operatorname{cond}(A)\operatorname{cond}(B)$.
For the break, take

$$
A=\begin{bmatrix}1&0&0\\0&1&0\end{bmatrix},
    \qquad
    B=\begin{bmatrix}0&0\\1&0\\0&1\end{bmatrix}
$$

Both have singular values $1,1$ and so $\sigma_1/\sigma_p=1$, yet $AB=\begin{bmatrix}0&0\\1&0\end{bmatrix}$ is singular and $\operatorname{cond}(AB)=\infty$.
The step squareness was holding up is the first one: $\operatorname{cond}(M)=\|M\|_2\|M^{-1}\|_2$ needs an inverse to exist, and the factorization $(AB)^{-1}=B^{-1}A^{-1}$ needs all three of them.

11. Write $A=Q\Lambda Q^T$. Then $A^TA=Q\Lambda^2Q^T$, so $\sigma_i=|\lambda_i|$, which is $\lambda_i$ by positivity, and the two descending orders therefore agree.
Positivity is doing real work: $\operatorname{diag}(1,-2)$ has eigenvalues $1,-2$ in the order they arrive, while its singular values are $2,1$ — even the moduli come out reversed.
For the converse, $\|A-A^T\|_F^2=2\operatorname{tr}(A^TA)-2\operatorname{tr}(A^2)=2\sum_i\sigma_i^2-2\sum_i\lambda_i^2=0$, so $A=A^T$.
On the rotation the proof stops at the middle step: $\operatorname{tr}(A^2)=\sum_i\lambda_i^2$ is a statement about squares and not moduli, and $\lambda_i^2=(\pm i)^2=-1$ is not $|\lambda_i|^2=1$, so $\operatorname{tr}(A^2)=-2$ while $\sum_i\sigma_i^2=2$ and $\|A-A^T\|_F^2=8$, as it should be.

12. $A^TA=V(\Sigma^T\Sigma)V^T$ is symmetric with eigenvalues $\sigma_i^2$, which are therefore also its singular values, so $\operatorname{cond}(A^TA)=\sigma_1^2/\sigma_n^2=\operatorname{cond}(A)^2$.
At $\operatorname{cond}(A)=10^8$ the normal equations are solved at condition $10^{16}$ and can hope to keep none of the sixteen digits, while the SVD route works at $10^8$ throughout and can hope for about eight.
The estimate is a rule of thumb and it errs on the harsh side: on a $200\times50$ system at that condition number the normal equations in fact keep about one digit, and the pseudoinverse about nine.

13. $AA^T=H^2$ while $A^TA=Q^TH^2Q$, so $A$ is normal exactly when $QH^2Q^T=H^2$.
Given that, $QHQ^T$ is symmetric, carries the eigenvalues of $H$ and so no negative one, and squares to $H^2$; uniqueness of the positive square root (Exercise 8) forces $QHQ^T=H$, that is $QH=HQ$.
Conversely commuting factors give $QH^2Q^T=H^2$ at once, and then $A=HQ=QH$: the turn may be taken before the stretch or after, indifferently.
A rotation through $\theta$ satisfies $R^TR=RR^T=I$, so it is normal, with $H=I$ and $Q=R$ trivially commuting; yet for $\theta$ not a multiple of $\pi$ its eigenvalues $e^{\pm i\theta}$ are not real and it fixes no line in $\mathbb{R}^2$.

14. Compute $LU$ in both cases.
A thousand right-hand sides do not change the answer, because they are reused equally cheaply on either side: $\mathbf{x}=V\Sigma^{-1}U^T\mathbf{b}$ is two matrix-vector products and $n$ divisions, $O(n^2)$, exactly the order of a pair of triangular solves.
The only cost that separates them is the factorization, and there $\tfrac23n^3$ beats a cubic with a much larger constant, by a margin the reuse never repays.
What the SVD tells you is the singular spectrum: the rank, the condition number, the spectral distance to the nearest matrix of lower rank (Lemma 10.7), and which directions are being inverted at what cost — hence the option of not inverting them all, which is the filtering of Section 10.4.
Elimination returns a solution and no diagnosis; that, and not speed, is what one pays the extra constant for.

15. $\sigma_n$ is the distance from $A$ to the nearest singular matrix and $\sigma_1$ is the size of $A$, so $\sigma_n/\sigma_1$ reports that distance relative to the matrix itself — the only reading a dimensionless report can bear.
The matrix $10^{-51}I_2$ has determinant $10^{-102}$ and exactly perpendicular columns, with $\operatorname{cond}=1$; the matrix $\operatorname{diag}(10^8,10^{-8})$ has determinant $1$ and sits $\sigma_2=10^{-8}$ away from singular.
Rescaling $A$ by $c$ multiplies $\det A$ by $c^n$, so a change of units alone drives the determinant to $0$ or to $\infty$ while $\sigma_n/\sigma_1$ does not move at all.
A quantity that a change of units can drive to zero was never measuring how close the matrix stands to singularity.

16. The map is $\mathbf{x}+\operatorname{ker} T\mapsto\mathbf{x}^\perp$, the unique representative of the class lying in $(\operatorname{ker} T)^\perp$, and it is well defined precisely because the inner product splits $V=(\operatorname{ker} T)^\perp\boxplus\operatorname{ker} T$, so each class meets that complement once and once only; the same recipe with $\operatorname{im} T$ in place of $\operatorname{ker} T$ handles $\operatorname{coker} T$.
Any other complement of $\operatorname{ker} T$ would serve equally well as a set of representatives and give an isomorphism just as good, but it would be a choice rather than a consequence, and what is lost with it is orthogonality — and with orthogonality the right angle that makes projection onto $(\operatorname{ker} T)^\perp$ the nearest-point map, the singular vectors perpendicular, and the splitting canonical rather than arbitrary.
Changing the inner product changes the adjoint, hence $T^*T$, hence its eigenvalues; but $\operatorname{ker} T$ and $\operatorname{im} T$ are defined by the words $T\mathbf{x}=\mathbf{0}$ and $\{T\mathbf{x}\}$, in which no inner product occurs.
Numerically, let $T:\mathbb{R}^3\rightarrow\mathbb{R}^2$ carry $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ to $(1,0)^T$, $(1,1)^T$, $(0,1)^T$, with $\mathbb{R}^2$ standard throughout and $\mathbb{R}^3$ carrying in turn the standard inner product and $\mathbf{x}^TG\mathbf{y}$ for $G=\operatorname{diag}(1,4,1)$:

$$
\sigma_1,\sigma_2 \;=\; \sqrt3,\ 1
    \qquad\text{against}\qquad
    \sigma_1,\sigma_2 \;=\; \tfrac{1}{2}\sqrt6,\ 1
$$

while $\operatorname{ker} T=\operatorname{span}\{(1,-1,1)^T\}$ and $\operatorname{im} T=\mathbb{R}^2$ under both.

17. The column means are $21$, $26$, $65$, and what is left is exactly rank one:

$$
\begin{bmatrix}-14&-21&-42\\-2&-3&-6\\2&3&6\\14&21&42\end{bmatrix}
    = 70\,\mathbf{u}_1\mathbf{v}_1^T ,
$$

with $\mathbf{u}_1=(-7,-1,1,7)^T/10$ and $\mathbf{v}_1=(2,3,6)^T/7$, so $\sigma_1=70$ and every later singular value is zero.
The gains are therefore proportional to $(2,3,6)$; for instance $\mathbf{g}=(2,3,6)$ with $\mathbf{s}=(1,7,9,15)$ and $\mathbf{b}=(5,2,17)$ reproduces $M$ entry for entry.
Nothing better is available, since $(cg_j)(s_i/c)+b_j=g_js_i+b_j$ leaves every reading unchanged: the data determine the ratios of the gains and nothing more.

18. $A^TA=\begin{bmatrix}1&24/25\\24/25&1\end{bmatrix}$ has eigenvalues $49/25$ and $1/25$, so $\sigma_1=7/5$, $\sigma_2=1/5$ and $\operatorname{cond}(A)=7$, with $\mathbf{u}_1=(1,1)^T/\sqrt2$ and $\mathbf{u}_2=(-1,1)^T/\sqrt2$.
The tensions are $(5/7,5/7)^T$ under $\mathbf{f}=(1,1)^T$ and $(5,-5)^T$ under $\mathbf{f}=(-1,1)^T$, of sizes $5\sqrt2/7\approx1.01$ and $5\sqrt2\approx7.07$.
The cheap load is $(1,1)^T=\sqrt2\,\mathbf{u}_1$, along the bisector the two bars share; the costly one is $(-1,1)^T=\sqrt2\,\mathbf{u}_2$, across it, and the ratio of the two costs is exactly $\operatorname{cond}(A)=7$.
As the bars turn toward parallel, $\sigma_2\rightarrow0$ and $\operatorname{cond}(A)\rightarrow\infty$: the joint loses all purchase across the common direction, and in the limit no tension whatever carries a load transverse to it.

19. Both eigenvalues are $4/5$, while $A^TA=\tfrac1{25}\begin{bmatrix}16&24\\24&52\end{bmatrix}$ has eigenvalues $64/25$ and $4/25$, so $\sigma_1=8/5$ and $\sigma_2=2/5$, with $\sigma_1\sigma_2=16/25=|\det A|$.
Since $A=\tfrac45\begin{bmatrix}1&3/2\\0&1\end{bmatrix}$ and $\begin{bmatrix}1&c\\0&1\end{bmatrix}^k=\begin{bmatrix}1&kc\\0&1\end{bmatrix}$, the closed form follows.
The unit error that grows most is $\mathbf{v}_1=(1,2)^T/\sqrt5$, amplified by $\sigma_1=8/5$ in one sample.
The singular values bound the error at every step, $\|\mathbf{x}_{k+1}\|\leq\sigma_1\|\mathbf{x}_k\|$, and $\sigma_1>1$ is exactly why a settled loop can still bulge before it settles; the eigenvalues govern only the limit, where $\rho_A=4/5<1$ finally tells.

20. Each column of $QA$ is $Q$ applied to a column of $A$, and clause 3 of Lemma 5.19 leaves its length alone; summing the squared column lengths gives $\|QA\|_F=\|A\|_F$.
Each row of $AP$ is a row of $A$ times $P$, that is $P^T$ applied to the transposed row, whose length is likewise unchanged; summing squared row lengths gives $\|AP\|_F=\|A\|_F$, and the two together give $\|QAP\|_F=\|A\|_F$.
Hence $\|A-A_k\|_F^2=\|U\Sigma'V^T\|_F^2=\|\Sigma'\|_F^2=\sum_{i>k}\sigma_i^2$.
For the spectral norm, $\|QAP\mathbf{x}\|=\|AP\mathbf{x}\|$ by the same clause, and $P$ carries the unit sphere onto itself, so the maximum is unmoved; the largest entry of $\Sigma'$ is $\sigma_{k+1}$, and $\|A-A_k\|_2=\|\Sigma'\|_2=\sigma_{k+1}$.
The Frobenius error sees every discarded singular value; the spectral error sees only the largest of them.

## Chapter 11

1. $\hat{Y}\cdot\hat{Z}=12$, so $\operatorname{cov}(Y,Z)=3$; both vectors have squared length $20$, so the variances are $5$ apiece and

$$
\operatorname{corr}(Y,Z)=\frac{12}{20}=\frac{3}{5}=\cos\theta ,
$$

an angle of $53.13^\circ$.
The second pair centers to $\hat{Y}=(-2,-1,1,2)^T$ and $\hat{Z}=\tfrac12(3,-3,-3,3)^T$, whose dot product is $0$, so the correlation vanishes; yet $z_i=y_i^2$ determines $Z$ from $Y$ outright.
Zero correlation rules out a linear relation and rules out nothing else.

2. Mean $(10,20)$; centered rows $(-4,-2)$, $(-2,-4)$, $(2,2)$, $(4,4)$; and

$$
[C]=\begin{bmatrix}10&9\\9&10\end{bmatrix}
$$

with eigenvalues $19$ and $1$, eigenvectors $(1,1)^T/\sqrt2$ and $(1,-1)^T/\sqrt2$.
The first component carries $r_1=19/20=0.95$, points along the diagonal, and pairs with a sensor correlation of $0.9$.

3. $\sigma_3^2=169-144-16=9$, so $\sigma_3=3$.
The rank-one minimum is $\sqrt{\sigma_2^2+\sigma_3^2}=\sqrt{16+9}=5$.

4. $\chi(\lambda)=(\lambda-20)(\lambda-8)(\lambda-5)$, with unit eigenvectors

$$
\tfrac13(2,1,2)^T,\quad \tfrac13(-2,2,1)^T,\quad \tfrac13(-1,-2,2)^T
$$

in that order, and $r_2=28/33\approx0.848$.
The first has no sign change, so all three quantities rise and fall together — a loading mode; the second sets temperature against pressure and flow, trading one for the other two.

5. $\chi_A(\lambda)=(\lambda-1)(\lambda^2-8\lambda+13)$, and all three roots are positive.
The eigenvector for $\lambda=1$ is $(-1,1,1)^T$, so deflation gives

$$
A_2=A-\tfrac13(-1,1,1)^T(-1,1,1)=\tfrac13\begin{bmatrix}11&7&4\\7&8&-1\\4&-1&5\end{bmatrix}
$$

of rank two, with $\|A-A_2\|_F=\sigma_3=1$.
Replacing $a_{33}$ by $t$ makes $\det A=8t-3$, so $t=3/8$ also has rank two, at Frobenius distance $13/8$: Theorem 11.6 saves $5/8$.

6. Every block has determinant zero — $200\cdot171=190\cdot180$ and so on — hence rank one, and the blockwise scheme errs by nothing.
The whole matrix truncated to rank two errs by $\sigma_3=5.5367$.
Storage is $2(4+4+1)=18$ numbers against $4\cdot1\cdot(2+2+1)=20$, so the exact fit costs two more.

7. Every entry of $[R]$ is summed once by the equiangular direction, so
$\mathbf{v}^T[R]\mathbf{v}=\tfrac13\left(3+2(0.8+0.7+0.9)\right)=\tfrac{7.8}{3}=\tfrac{13}{5}$.
Theorem 11.4 makes $\lambda_1$ the maximum of that form over unit vectors, so $\lambda_1\geq13/5$, and dividing by $\operatorname{tr}[R]=3$ gives $r_1\geq13/15=0.8667$.
The true value is $0.8676$, the bound falling short by under a thousandth, which is as close as $\mathbf{w}$ can come to the leading component without being it: a single common drift — lot, chamber, tool age — moves all three metrics together.

8. Writing $[R]$ with off-diagonal $c/\sqrt{ab}\neq0$ makes its eigenvectors $(1,1)^T$ and $(-1,1)^T$ for every admissible $a,b,c$, while $[C](1,1)^T$ has components differing by $a-b$; so $(1,1)^T$ is an eigenvector of $[C]$ if and only if $a=b$.
For the $3\times3$ matrix the variances are $8,8,7$ and the correlation of the first two variables is $1/4$, yet $[C]$ has spectrum $10,7,6$ and $[R]$ spectrum $\tfrac54,1,\tfrac34$, both simple, with the same ordered components

$$
\tfrac{1}{\sqrt2}(1,1,0)^T,\qquad (0,0,1)^T,\qquad \tfrac{1}{\sqrt2}(-1,1,0)^T .
$$

With two variables the single covariance necessarily links variables of different variance; with three, the odd variance can be quarantined in a variable uncorrelated with the rest, and the two eigenbases never separate.

9. Put $q=e^{-1.6}$, so $\sigma_k^2=100q^k$ and the amplitude cancels from

$$
r_2 = \frac{q+q^2}{q+q^2+q^3+q^4+q^5} = \frac{1-q^2}{1-q^5} .
$$

Since $0<q<1$ the denominator is less than $1$, so $r_2>1-q^2=1-e^{-3.2}$, and $e^{3.2}>e^3>20$ gives $r_2>0.95$; the exact value is $0.9596$.

10. The rows of $\mathcal{X}_k=\sum_{i\leq k}\sigma_i\mathbf{u}_i\mathbf{v}_i^T$ are combinations of $\mathbf{v}_1,\ldots,\mathbf{v}_k$, and independence of $\mathbf{u}_1,\ldots,\mathbf{u}_k$ with $\sigma_i>0$ makes the span exactly $\operatorname{span}\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}$; clause 4 of Theorem 6.16 makes $\mathcal{X}_k^\dagger\mathcal{X}_k$ the orthogonal projection onto $(\operatorname{ker}\mathcal{X}_k)^\perp=\operatorname{row}(\mathcal{X}_k)$, and orthonormal columns render that projection as $V_kV_k^T$.
Applying it to $\mathcal{X}=\sum_i\sigma_i\mathbf{u}_i\mathbf{v}_i^T$ kills every term with $i>k$ by orthonormality of the $\mathbf{v}_i$, leaving $\mathcal{X} V_kV_k^T=\mathcal{X}_k$, so the residual is $\sum_{i>k}\sigma_i\mathbf{u}_i\mathbf{v}_i^T$, whose rows lie in the discarded span.
Its squared Frobenius norm is $\sum_{i>k}\sigma_i^2$, which is exactly the minimum of Theorem 11.6: reconstruction keeps the coimage and discards its orthogonal complement, losing nothing that could have been kept at rank $k$.

11. For any unit $\mathbf{x}$, $\|(X+Y)\mathbf{x}\|\leq\|X\mathbf{x}\|+\|Y\mathbf{x}\|\leq\|X\|_2+\|Y\|_2$, and maximizing over $\mathbf{x}$ gives the triangle inequality for $\|\cdot\|_2$.
Choose $C$ of rank less than $i$ with $\|X-C\|_2=\sigma_i(X)$ and $D$ of rank less than $j$ with $\|Y-D\|_2=\sigma_j(Y)$, both by Lemma 10.7; then $C+D$ has rank less than $i+j-1$, so the same lemma gives

$$
\sigma_{i+j-1}(X+Y)\leq\|(X-C)+(Y-D)\|_2\leq\sigma_i(X)+\sigma_j(Y) .
$$

With $X=A-B$, $Y=B$ of rank at most $k$, and $j=k+1$, the second term is $\sigma_{k+1}(B)=0$ and the display reads $\sigma_{k+i}(A)\leq\sigma_i(A-B)$.

12. Since $\Pi_{W}\mathbf{u}_i$ is $\mathbf{u}_i$ for $i\leq k$ and $\mathbf{0}$ otherwise, applying $\Pi_{W}$ to $A=\sum_i\sigma_i\mathbf{u}_i\mathbf{v}_i^T$ column by column deletes exactly the terms past $k$, so $\Pi_{W}A=A_k$.
Lemma 6.7 makes $\mathrm{id}-\Pi_{W}$ the projection onto $W^\perp$, so each column splits orthogonally and Pythagoras summed over columns gives $\|B\|_F^2=\|\Pi_{W}B\|_F^2+\|B-\Pi_{W}B\|_F^2\geq\|\Pi_{W}B\|_F^2$, with equality if and only if $B=\Pi_{W}B$, that is, every column of $B$ lies in $W$.
Taking $B=A$ and reading both sides through $\|A\|_F^2=\sum_i\sigma_i^2$ identifies $\|A_k\|_F^2/\|A\|_F^2$ with $r_k$: the variance ratio and the retained fraction of Frobenius energy are one quantity.

13. Were $\operatorname{rank}(A+E)<r$, then $A+E$ would be admissible in Lemma 10.7 at index $r$ and $\|E\|_2=\|A-(A+E)\|_2\geq\sigma_r$ would contradict the hypothesis; the threshold is sharp, since $E=-\sigma_r\mathbf{u}_r\mathbf{v}_r^T$ has norm exactly $\sigma_r$ and makes $A+E=A_{r-1}$, of rank $r-1$.
For the gap, $\operatorname{rank} A=r$ makes $A$ admissible in Lemma 10.7 at index $r+1$, whence $\sigma_{r+1}(A+E)\leq\|E\|_2<\sigma_r/2$, while Exercise 11 with $X=A+E$, $Y=-E$, $i=r$, $j=1$ gives $\sigma_r\leq\sigma_r(A+E)+\|E\|_2$ and so $\sigma_r(A+E)>\sigma_r/2$.

14. A rank-two $3\times3$ carries $6+6-4=8$ parameters against $5$ observations, leaving $3$ free, and Theorem 11.15 asks for entries on the order of $r(m+n)\log^2(m+n)$ sampled at random, which five is not.

15. Retain two.
The ratios $\sigma_k/\sigma_{k+1}$ are $2.41$, $6.375$, $2.67$, $1.50$, so the sharp drop is after $\sigma_2$; and $r_1=0.8496$ against $r_2=0.9957$ puts the variance criterion in the same place.
This is Example 11.11 again, sharper: two active modes and a noise floor beneath them.
Example 11.12 is the doubtful one, since a spectrum decaying without gaps gives the gap criterion nothing to read, and the retained fraction must then be chosen by hand.

16. The enlarged sample has mean $\mathbf{y}/51$ and covariance

$$
\operatorname{diag}\!\left(\tfrac{150}{17},\tfrac{50}{51}\right)+\tfrac{25\rho^2}{2601}(1,1)(1,1)^T .
$$

The Rayleigh quotient at $(1,1)^T/\sqrt2$ grows like $\rho^2$ while on the orthogonal direction it stays bounded, so the first component tends to $(1,1)^T/\sqrt2$.
Meanwhile $d_M(\mathbf{y})^2=\tfrac{\rho^2}{2}(\tfrac19+1)=\tfrac59\rho^2$, so $d_M=\rho\sqrt5/3$.
Influence is quadratic and detection linear: by the time the flag goes up the component has already been captured, which is why screening comes first.

17. The product has rank one, and its entries with $i+j$ even are all $1$, so it matches every observation for every $t\neq0$ while the eight unobserved entries take the values $t$ and $1/t$  — unbounded in both directions.
The hypothesis that fails is that $\Omega$ be sampled uniformly at random; incoherence is a property of $M$, and the all-ones matrix attains $\mu=1$, the smallest value possible.
Random sampling couples every row to enough columns to fix the relative scaling that a checkerboard leaves free.

18. $K_{ij}=\mathbf{x}_i\cdot\mathbf{x}_j$ are exactly the entries of $\mathcal{X}\mathcal{X}^T$, and the linear kernel's feature map is the identity, so centering in the feature space is the centering $\mathcal{X}$ already carries.
If $\mathcal{X}^T\mathcal{X}\mathbf{w}=\lambda\mathbf{w}$ with $\lambda\neq0$ then $\mathbf{w}\notin\operatorname{ker}\mathcal{X}$ and $\mathcal{X}\mathcal{X}^T(\mathcal{X}\mathbf{w})=\lambda\,\mathcal{X}\mathbf{w}$, so the nonzero spectra of $K$ and $n[C]$ agree and the scores are the same.
A kernel sees what $[C]$ cannot only when its feature map is nonlinear.

19. The deviation is $\mathbf{x}-\bar{\mathbf{x}}=(5,-12,1,18,4)^T$, and the premise holds sensor by sensor: the largest of the five ratios $|x_i-\bar{x}_i|/\sqrt{C_{ii}}$ is $18/\sqrt{90}=1.90$.
The score along the last component is $z_5\approx12.9$, so its term is

$$
\frac{z_5^2}{\lambda_5}\approx12.25 ,
$$

and since every term of $\sum_kz_k^2/\lambda_k$ is nonnegative, $d_M^2\geq12.25$ and $d_M\geq3.5>3$.
The alarm comes from $\mathbf{v}_5$, which is dominated by sensor 4: that sensor rose while the four it is tightly correlated with did not follow, and the furnace varies least of all in exactly that direction.
Eighteen degrees is unremarkable on one gauge and decisive along $\mathbf{v}_5$: a reading is anomalous for its direction rather than its size.

20. Rows 1, 3 and 4 are $1$, $3$ and $4$ times $(2,1,3,5,4)$, and row 2 would be twice it were its first three entries $4,2,6$; so $L$ is the matrix whose four rows are $1$, $2$, $3$ and $4$ times $(2,1,3,5,4)$, and $S$ carries $7$ at $(2,1)$, $(2,2)$ and $(2,3)$ and nothing elsewhere.
Row 2 leaves the line the other three rows span, so $\operatorname{rank} M=2$ while $\operatorname{rank} L=1$; no rank-one matrix differs from $M$ in fewer than three entries, and no other three-entry support admits one, so this splitting is the sparsest and the only sparsest.
Host 2 sent an identical small probe to three destinations while its ordinary traffic continued underneath: the sparse part is a single row, and a single row is one source reaching many destinations — a port scan.

21. With $U_0=W_r\Sigma_r^{1/2}$ and $V_0=Z_r\Sigma_r^{1/2}$ one has $U_0V_0^T=W_r\Sigma_rZ_r^T=A$ and $\|U_0\|_F^2=\|V_0\|_F^2=\operatorname{tr}\Sigma_r=\|A\|_*$, so the objective equals $\|A\|_*$ there.
For any factorization $A=UV^T$,

$$
\|A\|_* = \langle W_r^TU,\,Z_r^TV\rangle_F
    \leq \|W_r^TU\|_F\|Z_r^TV\|_F
    \leq \|U\|_F\|V\|_F ,
$$

the second step by the contraction of Exercise 12 applied to $W_r^TU$, the coordinate array of $\Pi_{W}U$ in the basis $\mathbf{w}_1,\ldots,\mathbf{w}_r$; and $\|U\|_F\|V\|_F\leq\tfrac{1}{2}(\|U\|_F^2+\|V\|_F^2)$ since $(\|U\|_F-\|V\|_F)^2\geq0$.
Hence the minimum is $\|A\|_*$, attained at the balanced factorization.
Collecting the latent vectors as the rows of $P$ and $Q$ makes the Netflix penalty $\|P\|_F^2+\|Q\|_F^2$, never less than $2\|PQ^T\|_*$ and equal to it once the factors are balanced, so that the search over factors is a search over nuclear norms.

## Chapter 12

1. $\mathbb{E}(f)=0$ and $\mathbb{E}(g)=\tfrac23$, so $\hat{f}=f$ and $\hat{g}=(\tfrac13,-\tfrac23,\tfrac13)^T$, whence $\langle\hat{f},\hat{g}\rangle_\rho=\tfrac13\left(-\tfrac13+0+\tfrac13\right)=0$: the cosine is $0$, a perfect right angle.
Meanwhile $\mathbb{P}(f=1)\,\mathbb{P}(g=0)=\tfrac19$ against $\mathbb{P}(f=1\text{ and }g=0)=0$, since $g=0$ forces the middle outcome, where $f=0$.
The feature is that $g=f^2$ is a function of $f$ — knowing $f$ determines $g$ outright, dependence at its most total — and orthogonality of residuals registers none of it.

2. Since $\|\mathbf{1}\|_\rho=1$, $\mathbb{E}(f)=\mathbb{E}(f^3)=0$, $\mathbb{E}(f^2)=2$, and $\|f^2-2\cdot\mathbf{1}\|_\rho^2=\tfrac{14}{5}$, the basis is $\mathbf{1}$, $f/\sqrt{2}$, and $\sqrt{5/14}\,\bigl(f^2-2\cdot\mathbf{1}\bigr)$.
Orthogonality to $\mathbf{1}$ reads $\langle v,\mathbf{1}\rangle_\rho=\mathbb{E}(v)=0$, so the later vectors are their own residuals, and their orthogonality is zero covariance.
$P_2\propto x^2-\tfrac13$ subtracts from $x^2$ its mean under the uniform density on $[-1,1]$, exactly as $f^2-2\cdot\mathbf{1}$ does under uniform $\rho$: Gram-Schmidt on the monomials against a density — a weighted inner product, as in Example 5.2 — manufactures orthogonal polynomials and uncorrelated random variables in one stroke.

3. The denominator is $e^2+2e+1=(1+e)^2$, so $\operatorname{softmax}(\mathbf{z})=\left(e^2,e,e,1\right)^T\!/(1+e)^2\approx(0.534,0.197,0.197,0.072)^T$.
The preimage is the coset $\mathbf{z}+\operatorname{span}\{\mathbf{1}\}=\left\{(2+c,\,1+c,\,1+c,\,c)^T\right\}$, a single point of the quotient $\mathbb{R}^4/\operatorname{span}\{\mathbf{1}\}$.
Dividing through by $e^{2t}$ sends $\operatorname{softmax}(t\mathbf{z})\rightarrow(1,0,0,0)^T=\mathbf{e}_1$: the hard maximum demands a unique winner, not unique runners-up, and the tied middle scores split a share that vanishes anyway.

4. At $\epsilon=1/10$, $k\geq 36\ln(50{,}000)\cdot 100\approx 38{,}951.2$: take $k=38{,}952$.
At $\epsilon=1/20$ the demand quadruples to $k\geq 155{,}804.8$: take $k=155{,}805$.
The guarantee compresses nothing whenever $n\leq 155{,}805$; below that the "projection" ascends.
The ambient dimension made its first and only appearance in that comparison — neither count could consult a quantity the bound does not contain.

5. $Y$ has orthogonal columns $(2,0,2,0)^T$ and $(0,2,0,2)^T$ of length $2\sqrt2$, so $Q$ has columns $(1,0,1,0)^T/\sqrt2$ and $(0,1,0,1)^T/\sqrt2$; then $B=\begin{bmatrix}\sqrt2&\sqrt2&2\sqrt2\\ \sqrt2&-\sqrt2&0\end{bmatrix}$ and $QB=A$ exactly.
The error is $0=\sigma_3$: a rank-two matrix has only two nonzero singular values ($\sigma_1=2\sqrt3$, $\sigma_2=2$).
The two columns of $Y$ span $\operatorname{im} A$ — the sketch kept the rank at two — so $QQ^T$ projects onto $\operatorname{im} A$ itself and fixes every column of $A$.

6. Complementarity makes $I-\Pi=\Pi_{\mathbf{1}^\perp}$, so $\mathbb{V}(f)=\|(I-\Pi)f\|_\rho^2=\langle f,(I-\Pi)^2f\rangle_\rho=\langle f,(I-\Pi)f\rangle_\rho$, self-adjointness moving one factor across and idempotence collapsing the square.
A squared norm is nonnegative, and $\mathbb{V}(f)=0$ forces $(I-\Pi)f=\mathbf{0}$ by positive-definiteness ($\rho_i>0$), that is $f=\Pi f\in\operatorname{span}\{\mathbf{1}\}$; every constant centers to zero.
The zero-variance random variables are exactly $\operatorname{ker}(I-\Pi)=\operatorname{span}\{\mathbf{1}\}$ — the kernel of the centering map.

7. Entry $(i,j)$ of $\hat{\mathcal{X}}^T\operatorname{diag}(\rho)\hat{\mathcal{X}}$ is $\sum_k\rho_k\hat{f}_i(k)\hat{f}_j(k)=\langle\hat{f}_i,\hat{f}_j\rangle_\rho=\operatorname{cov}(f_i,f_j)$.
Then $\mathbf{c}^T[C]\mathbf{c}=\|\sum_ic_i\hat{f}_i\|_\rho^2\geq0$, with equality exactly on the linear relations among the residuals ($\rho_i>0$), so rank-nullity gives $\operatorname{rank}[C]=\dim\operatorname{span}\{\hat{f}_i\}$.
At $\rho_i=1/n$ the $\rho$-mean is the column mean, $\operatorname{diag}(\rho)=\frac1nI$, and the Gram matrix is $\frac1n\hat{\mathcal{X}}^T\hat{\mathcal{X}}$: the sample covariance of Chapter 11, its $1/n$ the uniform density all along.

8. $f^T\operatorname{diag}(\rho)f=\mathbb{E}(f^2)$ and $f^T\rho\rho^Tf=(\rho^Tf)^2=\mathbb{E}(f)^2$; subtracting gives $\mathbb{V}(f)$ by the Pythagorean identity.
Positive semidefiniteness is free — a variance is a squared length — and for symmetric PSD $M$, $f^TMf=0$ forces $Mf=\mathbf{0}$ (diagonalize via Theorem 10.1), so the kernel is the zero set of $\mathbb{V}$: $\operatorname{span}\{\mathbf{1}\}$ by Exercise 6, and only because $\rho$ avoids the boundary.
Entry $(i,j)$ is $\rho_i\delta_{ij}-\rho_i\rho_j=\mathbb{E}(\mathbf{1}_{\{i\}}\mathbf{1}_{\{j\}})-\mathbb{E}(\mathbf{1}_{\{i\}})\mathbb{E}(\mathbf{1}_{\{j\}})=\operatorname{cov}(\mathbf{1}_{\{i\}},\mathbf{1}_{\{j\}})$.
Shift-blindness of softmax and shift-blindness of variance are one and the same kernel.

9. $\langle\mathbf{1}_{A_i},\mathbf{1}_{A_j}\rangle_\rho=\mathbb{P}(A_i\cap A_j)$: zero off the diagonal, $\mathbb{P}(A_j)>0$ on it.
A combination $\sum_jc_j\mathbf{1}_{A_j}$ is precisely a random variable worth $c_j$ on $A_j$, and the disjoint supports make the $k$ indicators linearly independent, so $\dim W=k$.
Expanding in the orthogonal basis, $\Pi_{W}f=\sum_j\langle f,\mathbf{1}_{A_j}\rangle_\rho\,\mathbf{1}_{A_j}/\mathbb{P}(A_j)$, whose value on $A_j$ is $\sum_{i\in A_j}\rho_if_i/\mathbb{P}(A_j)$; at $k=1$ this is $\mathbb{E}(f)\mathbf{1}$, Section 12.1's projection recovered.
The matrix has $(\Pi_{W})_{ai}=\rho_i/\mathbb{P}(A_j)$ whenever $a$ and $i$ share a block $A_j$, and zero otherwise; it is symmetric exactly when $\rho$ is constant on each block.
What is symmetric is always $\operatorname{diag}(\rho)\Pi_{W}$, and that is precisely the statement $\Pi_{W}^*=\operatorname{diag}(\rho)^{-1}\Pi_{W}^T\operatorname{diag}(\rho)=\Pi_{W}$ of Example 5.15: self-adjoint without being a symmetric matrix.

10. Vertices work twice over: $\mathbf{e}_j$ lies in both sets and $P\mathbf{e}_j$ is the $j$th column, so each invariance reads its condition off the columns — nonnegativity for the orthant, unit sums for the hyperplane — while the converses are the entrywise product and the adjoint identity $\langle P\rho,\mathbf{1}\rangle=\langle\rho,P^T\mathbf{1}\rangle$.
The matrices $\begin{bmatrix}2&-1\\-1&2\end{bmatrix}$ and $\begin{bmatrix}1&1\\1&1\end{bmatrix}$ preserve one set apiece; with Lemma 12.4, preserving the simplex equals column-stochasticity equals both invariances at once, so the compact slice remembers each unbounded constraint in full.

11. If $\sum_i c_i\mathbf{u}_i=\mathbf{0}$ with some coefficient nonzero, take $j$ with $|c_j|$ largest: the inner product with $\mathbf{u}_j$ gives $c_j=-\sum_{i\neq j}c_i\langle\mathbf{u}_i,\mathbf{u}_j\rangle$, whence $|c_j|\leq(m-1)\,t\,|c_j|<|c_j|$.
So every $c_i=0$: the family is independent and its Gram matrix nonsingular.
Independent vectors number at most $n$, so for $m>n$ the hypothesis must fail and some pair has $|\langle\mathbf{u}_i,\mathbf{u}_j\rangle|\geq1/(m-1)$.
The vectors $\mathbf{u}_i=\sqrt{(n+1)/n}\,\bigl(\mathbf{e}_i-\tfrac{1}{n+1}\mathbf{1}\bigr)$ are unit, orthogonal to $\mathbf{1}$, carry $\langle\mathbf{u}_i,\mathbf{u}_j\rangle=-1/n$, and sum to $\mathbf{0}$: dependence at crosstalk exactly $1/(m-1)$.

12. In an orthonormal eigenbasis (Theorem 10.1) the surgery replaces the clipped eigenvalues by their average $\mu$, positive and sum-preserving, so $\tilde{C}$ is symmetric positive definite with the trace of $C$.
Every clipped eigenvalue lies below $\tau$ and every survivor at or above it, so $\mu<\tau$ never overtakes a survivor: the bottom of the spectrum rises from $\lambda_d$ to $\mu$, the top never rises, and $\operatorname{cond}(\tilde{C})\leq\lambda_1/\lambda_d=\operatorname{cond}(C)$, with equality exactly when the clipped eigenvalues were already equal; if nothing survives, $\tilde{C}=\mu I$ has condition one.

13. Corollary 3.26 gives $\dim\operatorname{ker}\Phi = n-\dim\operatorname{coim}\Phi\geq n-k\geq 1$, so some $\mathbf{v}\neq\mathbf{0}$ has $\Phi\mathbf{v}=\mathbf{0}$: the points $\mathbf{x}$ and $\mathbf{x}+\mathbf{v}$ sit at distance $\|\mathbf{v}\|>0$ upstairs and $0$ downstairs, violating the lower bound of Theorem 12.10 for every $\epsilon<1$.
Dimension itself forbids a guarantee over all of $\mathbb{R}^n$; only a finite cloud, whose finitely many differences a generic draw keeps out of the kernel, can be protected.

14. Each column of $A\Omega$ is $A$ applied to a column of $\Omega$, hence lies in $\operatorname{im} A$; a subspace inside another equals it exactly when the dimensions — the two ranks — agree, and $\operatorname{rank}(A\Omega)\leq k+p$ makes $\operatorname{rank} A\leq k+p$ necessary.
For $A=\operatorname{diag}(1,0)$ and $\Omega=\mathbf{e}_2$ the sketch is the zero matrix: the probe fell into $\operatorname{ker} A$, the one subspace a sketch cannot survive, which is what a generic draw avoids.

15. For any $i\in Z$ the pair $f=\mathbf{0}$, $g=\mathbf{e}_i$ differs as vectors yet $\|f-g\|_\rho^2=\rho_i=0$.
Since $\|f\|_\rho^2$ is a sum of nonnegative terms, degeneracy forces $f_i=0$ wherever $\rho_i>0$ and constrains nothing on $Z$: $U=\operatorname{span}\{\mathbf{e}_i:i\in Z\}$.
Every term of $\langle u,g\rangle_\rho$ with $u\in U$ carries a factor $\rho_i=0$, so the form does not feel which coset representative is chosen; and $\|[f]\|_\rho=0$ now forces $[f]=[\mathbf{0}]$ — an honest inner product on $\mathbb{R}^N\!/U$, of dimension $N-|Z|$, one dimension surrendered per forbidden outcome.

16. At $t=0$ the license reads $m<e^0=1$: it certifies no family at all — and asserts nothing false, since a bound may sit far beneath the truth ($n$ orthogonal directions, and not one more) without contradicting it.
Empty, not wrong.
The probabilistic method needs the failure probability strictly below one before some draw succeeds; at $t=0$ the tail bound for a single pair already reads $2e^0=2$, certifying nothing, and no union-bound bookkeeping descends below certainty.
Chance needs tolerance to have room; the license first overtakes the trivial $n$ only at $t=2\sqrt{\ln n/n}$ — about $0.16$ in $\mathbb{R}^{1024}$.

17. Chance spreads cosines with standard deviation $1/\sqrt{n}$ (Lemma 12.6): $0.35$ stands $0.35\cdot8=2.8$ deviations above chance in $\mathbb{R}^{64}$ and $0.35\cdot64=22.4$ in $\mathbb{R}^{4096}$ — the high-dimensional report is far the stronger.
To match $2.8$ deviations the $\mathbb{R}^{4096}$ team need report only $2.8/64=0.04375$; to match $22.4$ the $\mathbb{R}^{64}$ team must report $22.4/8=2.8$, and Cauchy-Schwarz (Lemma 5.5) caps every cosine at $1$.
No report from $\mathbb{R}^{64}$ — identical vectors included, at a mere $8$ deviations — can carry that much evidence: a similarity score is measured in units of $1/\sqrt{n}$, not of $1$.

18. Differences of points in the span remain in the span, where $\|Q^T\mathbf{v}\|^2=\mathbf{v}^TQQ^T\mathbf{v}=\|\mathbf{v}\|^2$: every distance survives exactly — with $\sigma_{r+1}=0$, nothing of the cloud lies outside the span, and the adaptive target is $k=r$ at zero error.
The oblivious demand $36\ln m/\epsilon^2$ exceeds $r$ once $m>e^{r\epsilon^2/36}$; at $r=100$, $\epsilon=0.1$ that is $e^{1/36}\approx1.03$, while a rank-$100$ cloud already contains at least $100$ points — the adaptive map wins at every legal $m$.
Dimension-free is not free; what $\ln m/\epsilon^2$ buys is the right never to look.

19. $\hat{a}_i=\langle\textstyle\sum_j a_j\mathbf{c}_j,\mathbf{c}_i\rangle=a_i\|\mathbf{c}_i\|^2+\sum_{j\neq i}a_j\langle\mathbf{c}_j,\mathbf{c}_i\rangle$, and the triangle inequality bounds the crosstalk by $t\sum_{j\neq i}|a_j|$.
The guarantee licenses $m<e^{1024\,t^2/4}$: at $t=0.1$ that is $m<e^{2.56}\approx 12.9$ — twelve codes, eighty-five times short of the orthogonal ceiling — while at $t=0.2$ it is $e^{10.24}\approx 2.8\times 10^4$, and the ceiling breaks.
The exponent must overcome the dimension before near-orthogonality pays.

20. With $\gamma=60/600$, the edge sits at $\sigma\sqrt{n}(1+\sqrt{\gamma})=0.5\sqrt{600}\,(1+\sqrt{0.1})\approx 16.1$.
Four singular values clear it — $146$, $98$, $61$, and $17.2$ — so the genuine structure has rank $4$.
The eye cuts at the plunge after $61$ and condemns $17.2$ to the bulk; the bulk of this instrument ends at $16.1$, and $17.2$ clears it.

21. The principal axes are a function of the whole cloud, computable only after the last record has passed — by which time the unreduced records are gone; the reducing map must be fixed before the first arrival, and only an oblivious map can be.
Theorem 12.10 with $\ln(10^7)\approx 16.12$ gives $k=9285$ at $\epsilon=0.25$, an eleven-fold reduction holding every pairwise squared distance within $25\%$ with probability $1-10^{-7}$; at $\epsilon=0.1$ it gives $k=58026$, more than half the ambient dimension.

22. $\operatorname{tr} L=\sum_i d_i=2\,\#E$ and, by symmetry, $\operatorname{tr}(L^2)=\sum_{i,j}L_{ij}^2=\sum_i d_i^2+2\,\#E$, whence the difference.
Since $g_i^2=1$, $\langle\mathbf{g},L\mathbf{g}\rangle=\operatorname{tr} L+\sum_{i\neq j}L_{ij}g_ig_j$, and $\mathbb{E}(g_ig_jg_kg_l)$ vanishes unless $\{i,j\}=\{k,l\}$, giving $\mathbb{V}=2\sum_{i\neq j}L_{ij}^2=4\,\#E$.
Chebyshev at threshold $0.01\cdot 2\,\#E$: failure probability at most $10^4/\#E=1/100$ when $\#E=10^6$.

23. $G$ is symmetric with unit diagonal, and $\operatorname{rank} G=\operatorname{rank} X\leq n$ leaves at most $n$ nonzero eigenvalues $\lambda_1,\ldots,\lambda_r$; Cauchy-Schwarz against the all-ones vector of $\mathbb{R}^r$ gives $m^2=(\operatorname{tr} G)^2\leq r\sum\lambda_i^2\leq n\,\operatorname{tr}(G^2)$, and symmetry reads the diagonal of $G^2$ as $\operatorname{tr}(G^2)=m+\sum_{i\neq j}\langle\mathbf{u}_i,\mathbf{u}_j\rangle^2$.
The $m(m-1)$ off-diagonal squares thus total at least $m(m-n)/n$, and the largest is at least their average, $(m-n)/(n(m-1))$.
The centered simplex family has $m=n+1$ and crosstalk $1/n$ against a floor of $\sqrt{1/n^2}$: equality, both inequalities tight.
At $n=1024$, $m=2\times10^5$ the floor is $0.0312$ against the $0.22$ the packing paid; as $m\to\infty$ it climbs to $1/\sqrt{n}$, the standard deviation of a random cosine (Lemma 12.6) — no family, however large, sinks its crosstalk below the one-standard-deviation scale of chance.

## Chapter 13

1. $\mathbf{z}_1=(4,-1)^T$, so $\mathbf{h}_1=(4,0)^T$ and $y=3$.
The read-out is unactivated, so $[\delta_2]=y-t=-3$, and
$[\delta_1]=-3\begin{bmatrix}1&2\end{bmatrix}\operatorname{diag}(1,0)=\begin{bmatrix}-3&0\end{bmatrix}$, whence
$G_2=\begin{bmatrix}-12&0\end{bmatrix}$ and $G_1=\begin{bmatrix}-6&-3\\0&0\end{bmatrix}$.
The second unit is off, so $\varsigma'(z_{1,2})=0$ zeroes the second entry of $[\delta_1]$ and with it the whole second row of $G_1$: a silent unit learns nothing from this input.

2. Left association costs $\Lambda n^2=6\cdot200^2=240{,}000$ multiplications; right association costs $(\Lambda-1)n^3+n^2=40{,}040{,}000$, a ratio of $1001/6\approx166.8$.
In general the ratio is $\bigl((\Lambda-1)n+1\bigr)/\Lambda$, linear in $n$ and asymptotically independent of depth.
The saving is one factor of the width, and nothing else.

3. Both points sit on the decision boundary, $p=\tfrac12$ apiece, so the batch gradient is $\tfrac12\bigl[(-\tfrac12)(2,2)^T+(\tfrac12)(1,1)^T\bigr]=(-\tfrac14,-\tfrac14)^T$ in $\mathbf{w}$ and $0$ in $c$: the two residuals cancel and the bias does not move.
Hence $\mathbf{w}_1=(2,0)^T$ and $c_1=0$.
The batch loss rises from $\log2\approx0.6931$ to $1.0725$.
The direction was a descent direction and the gradient was exact; $\eta=4$ simply overshoots the valley.

4. $M=W_K^TW_Q=\begin{bmatrix}1&0&1\\1&1&0\\0&1&-1\end{bmatrix}$, of rank $2=d_k$ — its determinant vanishes, as a form factoring through $\mathbb{R}^{d_k}$ must.
Then $\mathbf{x}_1^TM\mathbf{x}_2=2$ while $\mathbf{x}_2^TM\mathbf{x}_1=3$, so by (13.5) token $1$ heeds token $2$ with raw score $3$ and token $2$ heeds token $1$ with only $2$.
No symmetric form could record the difference, and it is the difference that carries who modifies whom.

5. $t(x)=2\varsigma(x)-4\varsigma(x-\tfrac12)$: below $\tfrac12$ the second unit is silent and the value is $2x$; above it the second unit subtracts $4(x-\tfrac12)$ and the value is $2-2x$.
At $k=10$ the deep stack spends $20$ units for $1024$ pieces, while one hidden layer needs $w+1\geq1024$, that is $1023$ units — fifty-one times as many, for the identical graph.
Depth multiplies what width can only add.

6. For any unit $\mathbf{x}$ the triangle inequality gives $1-\epsilon\leq\|\mathbf{x}\|-\|[DF]\mathbf{x}\|\leq\|(I+[DF])\mathbf{x}\|\leq1+\epsilon$, and the upper half is $\sigma_1=\|I+[DF]\|_2\leq1+\epsilon$ by Definition 10.5.
The lower half makes $I+[DF]$ injective, hence nonsingular, and applied to $(I+[DF])^{-1}\mathbf{y}$ it reads $\|(I+[DF])^{-1}\mathbf{y}\|\leq\|\mathbf{y}\|/(1-\epsilon)$, so $1/\sigma_n=\|(I+[DF])^{-1}\|_2\leq1/(1-\epsilon)$ and $\sigma_n\geq1-\epsilon$.
Hence $\operatorname{cond}(I+[DF])\leq(1+\epsilon)/(1-\epsilon)$.
At $\epsilon=1$ the lower bound is zero and the estimate asserts nothing whatever — not that the block is badly conditioned, only that this argument has run out; the skip connection is no longer buying anything the inequality can see.

7. The deviations $h_i-\mathbb{E}(h)$ sum to zero, so the mean of $\hat{\mathbf{h}}$ is $c$ exactly, for every $s$ and every $\epsilon$.
Each deviation is then scaled by the constant $s/\sqrt{\mathbb{V}(h)+\epsilon}$, so the variance is multiplied by its square: $s^2\mathbb{V}(h)/(\mathbb{V}(h)+\epsilon)$, which equals $s^2$ only when $\epsilon=0$.
The $\epsilon$ buys a denominator that cannot vanish — a layer whose activations happen to agree has $\mathbb{V}(h)=0$ — and it costs exactness, docking the variance by the factor $\mathbb{V}(h)/(\mathbb{V}(h)+\epsilon)$, most severely on precisely the least varying layers it was inserted to protect.

8. Row $i$ of $G_\ell$ is $([\delta_\ell])_i\,\mathbf{h}_{\ell-1}^T$, so $\operatorname{row}(G_\ell)\subseteq\operatorname{span}\{\mathbf{h}_{\ell-1}\}$ — the rank-one statement, read on the row side.
Summing $T$ updates, the total change $W_\ell^{(T)}-W_\ell^{(0)}=-\sum_t\eta_t[\delta_\ell^{(t)}]^T(\mathbf{h}_{\ell-1}^{(t)})^T$ has row space inside the span of the activations, and rank is the dimension of the row space.
So a layer whose inputs never leave a $k$-dimensional subspace can only ever be altered by a correction of rank at most $k$, however many steps are taken and whatever the losses: training moves a weight matrix only along the directions its data actually present to it, and the coimage of the change is chosen by the data before descent has any say.

9. Differentiating the quotient $p_i=e^{z_i}/\sum_k e^{z_k}$ gives $\partial p_i/\partial z_j=\bigl(\delta_{ij}e^{z_i}\sum_ke^{z_k}-e^{z_i}e^{z_j}\bigr)/\bigl(\sum_ke^{z_k}\bigr)^2=p_i(\delta_{ij}-p_j)$, which assembled is $\operatorname{diag}(\mathbf{p})-\mathbf{p}\mathbf{p}^T$.
Factor it as $\operatorname{diag}(\mathbf{p})(I-\mathbf{1}\mathbf{p}^T)$: with every $p_i>0$ the first factor is invertible, and $(I-\mathbf{1}\mathbf{p}^T)\mathbf{x}=\mathbf{x}-(\mathbf{p}^T\mathbf{x})\mathbf{1}$ vanishes exactly when $\mathbf{x}$ is a multiple of $\mathbf{1}$, since $\mathbf{p}^T\mathbf{1}=1$.
So the kernel is $\operatorname{span}\{\mathbf{1}\}$ and the rank is $n-1$.
That kernel is the invariance $\operatorname{softmax}(\mathbf{z}+c\mathbf{1})=\operatorname{softmax}(\mathbf{z})$ of Definition 12.5 differentiated: raising every score together moves no probability at all.

10. Both entries of the maximum are constants, so which is active depends on $b$ alone: the noise entry $4\nu^2/(b\mu^2)$ exceeds $\gamma d_0^2$, with $d_0=\|\Psi_0-\Psi^*\|$, exactly when $b<b^\ast=2\nu^2/(L\mu d_0^2)$.
Below the threshold the bound is $4\nu^2/\bigl(b\mu^2(t+\gamma)\bigr)$ and sees $b$ and $t$ only through $b(t+\gamma)$, which is the count of gradients evaluated plus $b\gamma$: at a fixed budget the batch size is nearly free, and exactly free in the limit $t\gg\gamma$.
Above it the bound is $\gamma d_0^2/(t+\gamma)$, in which $b$ does not appear, so a larger batch buys proportionally fewer steps and nothing at all in exchange.
Enlarging the batch is worth doing up to $b^\ast$, where it costs the bound nothing, and past $b^\ast$ it is worth doing only for what the mathematics cannot see — the width of a matrix multiplication a machine performs for free.

11. The two patterns differ only at $j$, so $D_1-D_1'=\pm\mathbf{e}_j\mathbf{e}_j^T$ and

$$
A_R-A_{R'} \,=\, W_2(D_1-D_1')W_1 \,=\, \pm(W_2\mathbf{e}_j)(\mathbf{e}_j^TW_1) ,
$$

the outer product of the $j$th column of $W_2$ with the $j$th row of $W_1$: rank one, or zero if either factor is.
The two affine maps differ by $W_2(D_1-D_1')(W_1\mathbf{x}+\mathbf{b}_1)=\pm(W_2\mathbf{e}_j)\,z_{1,j}(\mathbf{x})$, which vanishes exactly on $\{z_{1,j}=0\}$ — the wall between the regions.
So consecutive pages of the atlas differ by one rank-one correction and agree wherever they meet: this is the continuity of Theorem 13.15, computed rather than asserted.

12. The columns of $W$ lie in $\mathbb{R}^d$, so $\operatorname{rank} W\leq d$ and $\dim\operatorname{ker} W=v-\operatorname{rank} W\geq v-d>0$; any nonzero $\mathbf{c}$ in that kernel is a weighting of the whole vocabulary whose embeddings cancel, $\sum_wc_w\mathbf{e}_w=\mathbf{0}$.
Pairwise orthogonal nonzero vectors are linearly independent, and $\mathbb{R}^d$ admits at most $d$ independent vectors, so at most $d$ of the $v$ embeddings can be mutually perpendicular.
Neither crowding owes anything to meaning: both follow from $d<v$ alone, before a single word has been read.
A lexicon in a small space must overlap itself, whatever it is a lexicon of.

13. A ReLU read-out returns nothing negative, so every target with a negative value is unreachable and leaves $\tfrac12t^2$ in the loss forever.
If the read-out pre-activation is negative at every training input, then $\varsigma'(z_\Lambda)=0$ there and $[\delta_\Lambda]=0$; Lemma 13.5 carries that zero down every layer, so every $G_\ell$ and every bias gradient vanishes and descent never moves again.
The network is dead and cannot revive itself, the output being scalar.
The last line of (13.2) is left linear so that neither failure is possible: the read-out must be free to reach the whole of $\mathbb{R}^m$ and to pass a derivative back on every input.

14. $S$ is entrywise positive, so Theorem 9.6 supplies a dominant eigenvalue with a strictly positive eigenvector, and no other nonnegative eigenvector but its multiples; $S$ is column-stochastic, so Lemma 9.15 fixes that eigenvalue at $1$.
Normalizing to unit sum gives the unique positive density $\mathbf{\pi}$ with $S\mathbf{\pi}=\mathbf{\pi}$.
Of nothing.
A stationary distribution is the fixed point of a law iterated in time, and $S$ is computed afresh from every prompt and applied exactly once, so $S^2,S^3,\ldots$ describe no process any transformer runs: the eigenvector is real, the chain is imaginary.

15. $Y_1=(W_VX)S$ with $S$ assembled from $W_Q$ and $W_K$ alone, so $W_OY_1=\bigl((W_OW_V)X\bigr)S$ — Definition 13.12 verbatim, with value matrix $W_OW_V\in\mathbb{R}^{d\times d}$.
One head behind an output projection is one head.
Each $M^{(i)}=W_K^{(i)T}W_Q^{(i)}$ has rank at most $d_k=64$, and eight of them span at most $hd_k=512=d$, which is attained: the chorus recovers full rank on the embedding space exactly, where a single head reaches an eighth of it and no more.
What the analogy with $A=\sum_i\sigma_i\mathbf{u}_i\mathbf{v}_i^T$ lacks is ordering and optimality — the heads carry no $\sigma_1\geq\sigma_2\geq\cdots$, so there is no first head and no last, and truncating to any $k$ of them is not best among rank-$k$ competitors in the way Theorem 11.6 certifies for the SVD.

16. With $(S\mathbf{x})_i=x_{i+1}$, the pair in series is $D^2=I-2S+S^2$, whose first row is $(1,-2,1,0,0,0)$ and whose every later row is that one shifted: the three-tap filter $(1,-2,1)$, a second difference.
Its kernel is again exactly the constants — if $D^2\mathbf{x}=\mathbf{0}$ then $D\mathbf{x}$ is constant, and the entries of $D\mathbf{x}$ telescope around the ring to zero, so $D\mathbf{x}=\mathbf{0}$ — hence $\operatorname{rank} D^2=\operatorname{rank} D=5$ and the second stage removes no further dimension.
The array is blind to uniform strain and to nothing else: a thermal expansion of the whole shaft is invisible by construction, at any depth of linear processing.
Only a nonlinearity between the stages could change that.

17. At $\mathbf{x}=\mathbf{0}$ the pre-activations are $\mathbf{z}_1=(1,-1)^T$: unit one on, unit two off, so $D=\operatorname{diag}(1,0)$ and $A_R=\mathbf{w}_2^TDW_1=\begin{bmatrix}1&2\end{bmatrix}$, whose kernel is spanned by $\mathbf{f}=(2,-1)^T$.
Along $\mathbf{x}=t\mathbf{f}$ the first pre-activation is pinned at $1$ while the second is $7t-1$, so unit two switches on at $t=1/7$: the reading holds at $y=1$ for every $t\leq1/7$ and equals $7t$ beyond.
The monitor is therefore blind to this fault up to magnitude $\|\mathbf{x}\|=\sqrt5/7\approx0.319$, and blind to $-\mathbf{f}$ at every magnitude whatsoever.
A local kernel is a local statement; the fold is what ends it, and on the other side the network reads a different page of its atlas.

18. The subspace $\operatorname{im} W_U+\operatorname{span}\{\mathbf{1}\}$ is spanned by the two columns of $W_U$ together with $\mathbf{1}$, so it has dimension three, and its perpendicular is the line through

$$
\mathbf{u} = (1,-1,1,-1)^T .
$$

Reachability therefore reads

$$
\log p_1-\log p_2+\log p_3-\log p_4=0,
    \qquad\text{that is}\qquad
    p_1p_3=p_2p_4 .
$$

The first split passes, since $\tfrac49\cdot\tfrac19$ and $\tfrac29\cdot\tfrac29$ agree, and is produced by $\mathbf{h}=(\log2,0)^T$.
The second fails: $0.4\cdot0.2=0.08$ against $0.3\cdot0.1=0.03$, and no state of the router produces it.
Two state coordinates cannot steer four links: the reachable splits are a two-parameter family inside a three-dimensional simplex, and the split demanded lies off it.

19. The speeds fit exactly with $\mathbf{a}=(2,3)^T$ and $c=10$: the four values $12,13,15,17$ are $2h_1+3h_2+10$ at the four representations.
The loads do not.
The first three readings force $a_1+c=a_2+c=a_1+a_2+c=1$, hence $a_1=a_2=0$ and $c=1$, which predicts $1$ at the fourth rig against the observed $5$.

20. The network has $4+4+4+1=13$ parameters against $12$ points, and cannot fit them all.
The eleven consecutive slopes alternate in sign, so any piecewise-affine interpolant changes direction at ten interior points, while a hidden layer of $m$ units contributes at most $m$ kinks: $m\geq10$ is necessary, and $m=4$ is not merely untrained but incapable.
Four kinks give five affine pieces, and a best use of them is to isolate four consecutive points at one end, one to a piece, leaving the other eight — still alternating — to a single line.
Against those eight the targets have mean zero and the least-squares line has slope $\pm2/21$, so the residual sum of squares is $8-16/42=160/21$ and $\tfrac{1}{12}\sum_i(f(x_i)-y_i)^2=160/(21\cdot12)=40/63\approx0.635$.
Dropping continuity would permit five blocks of sizes $2,2,2,2,4$ — the first four fitted exactly, all the error carried by the last — and report only $4/15$; but those four blocks have the common slope $2$ and distinct intercepts, so they never meet, and Theorem 13.15 makes every ReLU network continuous.

---


# About the Author

*[Figure omitted]*



*& these again surrounded by

Four Wonders of the Almighty Incomprehensible

Pervading all amidst & round about

Fourfold each in the other reflected

They are named Life's in Eternity

Four Starry Universes going forward

From Eternity to Eternity
*

**ABOUT THE AUTHOR**

Robert Ghrist (Ph.D., Cornell, Applied Mathematics, 1995)

is the Andrea Mitchell PIK Professor of Mathematics and

Electrical & Systems Engineering at the University of Pennsylvania.

He is a recognized leader in the field of Applied Algebraic Topology,

working in networks, robotics, signal processing, data analysis,

optimization, and more. He is an award-winning researcher,

teacher, and expositor of Mathematics and its applications,

currently serving as the Associate Dean of Undergraduate Education

in the School of Engineering & Applied Sciences
at Penn.

He is the author of several books, such as:

*Elementary Applied Topology* and the *Calculus Blue Guide*;

as well as the creator of YouTube video series, including

*Calculus BLUE,
Calculus GREEN, &
Applied Dynamical Systems*.

In his spare time
he publishes mathematical art

and animation
under the moniker *colimit*.