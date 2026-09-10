# Weeks 1–11 gap pool — 0327–0347 (needs-review)

## ESE2030-0327
*week 1 · POOL pool #35 · needs-review · Core*  
skills: `W01.S09` Recognize when permutation or block structure decouples a system  

In each pattern below, $\ast$ marks an entry that may be nonzero and $0$ an entry that is zero. For which coefficient matrix can $A\mathbf{x} = \mathbf{b}$ be solved as two independent $2\times 2$ systems, possibly after reordering the unknowns and the equations?

- **(A)** $\begin{bmatrix} \ast & 0 & \ast & 0 \\ 0 & \ast & 0 & \ast \\ \ast & 0 & \ast & 0 \\ 0 & \ast & 0 & \ast \end{bmatrix}$
- **(B)** $\begin{bmatrix} \ast & \ast & 0 & 0 \\ 0 & \ast & \ast & 0 \\ 0 & 0 & \ast & \ast \\ \ast & 0 & 0 & \ast \end{bmatrix}$
- **(C)** $\begin{bmatrix} \ast & \ast & \ast & \ast \\ 0 & \ast & \ast & \ast \\ 0 & 0 & \ast & \ast \\ 0 & 0 & 0 & \ast \end{bmatrix}$
- **(D)** $\begin{bmatrix} \ast & \ast & 0 & 0 \\ \ast & \ast & 0 & 0 \\ 0 & 0 & \ast & \ast \\ \ast & 0 & \ast & \ast \end{bmatrix}$
- **(E)** $\begin{bmatrix} \ast & \ast & \ast & \ast \\ \ast & \ast & \ast & \ast \\ 0 & 0 & \ast & \ast \\ 0 & 0 & \ast & \ast \end{bmatrix}$

<details><summary>Answer</summary>

**Correct: (A)** *(unverified)*

Equations 1 and 3 involve only $x_1$ and $x_3$; equations 2 and 4 involve only $x_2$ and $x_4$. Reordering the unknowns as $(x_1, x_3, x_2, x_4)$ and the equations likewise makes the matrix block diagonal with two $2\times 2$ blocks, and the system decomposes into two independent subsystems. Block structure need not be visible in the given ordering; permutations of rows and columns reveal it.

Why the distractors tempt:
- (B) Distractor: a cycle of couplings ($x_1$ to $x_2$ to $x_3$ to $x_4$ back to $x_1$); no reordering separates the unknowns into two groups that never meet.
- (C) Distractor: upper triangular. Back substitution solves it one unknown at a time, but each equation depends on the ones below it; nothing is independent.
- (D) Trick: nearly block diagonal, but the single entry coupling $x_1$ into the last equation ties the two halves together. One nonzero is enough to destroy decoupling.
- (E) Trick: block upper triangular. The lower block can be solved on its own, but the upper block then needs its answer; the two systems are sequential, not independent.

</details>

---

## ESE2030-0328
*week 1 · POOL pool #36 · needs-review · Core*  
skills: `W01.S09` Recognize when permutation or block structure decouples a system  

Elimination on a dense $n\times n$ system costs about $c\,n^3$ operations for a constant $c$. The unknowns and equations of a particular system can be reordered so that its matrix is block diagonal with two $\tfrac{n}{2}\times\tfrac{n}{2}$ blocks. By roughly what factor does the elimination cost fall?

- **(A)** 2
- **(B)** 8
- **(C)** 4
- **(D)** $n/2$
- **(E)** It does not fall; reordering costs as much as it saves

<details><summary>Answer</summary>

**Correct: (C)** *(unverified)*  — partial credit: B

Each block is a system of half the size, costing $c(n/2)^3 = c\,n^3/8$; there are two of them, for $c\,n^3/4$ in all. The cubic scaling is what makes decoupling pay: halving the size divides the work by eight, and doing it twice still leaves a factor of four. A permutation costs nothing to apply.

Why the distractors tempt:
- (A) Distractor: treats the cost as linear in the size, so two half-size problems cost the same as one full one.
- (B) Partial credit: has the cubic scaling ($1/8$ per block) but forgets that there are two blocks to solve. Insight 1 of 2: cost scales as the cube of the size. Missing: two subsystems, so $2/8 = 1/4$. Prefix: yes. Guessable: no. Defensible: yes.
- (D) Distractor: a size, not a factor; confuses the block dimension with the saving.
- (E) Distractor: a permutation of rows and columns is bookkeeping, not arithmetic; it costs nothing on the scale of $n^3$.

</details>

---

## ESE2030-0329
*week 1 · POOL pool #37 · needs-review · Core*  
skills: `W01.S10` Say what conditioning warns about and what it does not — and that a small determinant is not the diagnostic  

A student claims that a matrix with a very small determinant must be ill-conditioned, so that solving $A\mathbf{x} = \mathbf{b}$ with it is numerically unreliable. Which matrix is a counterexample to the claim?

- **(A)** $\begin{bmatrix} 1 & 1 \\ 1 & 1.001 \end{bmatrix}$
- **(B)** $\begin{bmatrix} 0.001 & 0 \\ 0 & 0.001 \end{bmatrix}$
- **(C)** $\begin{bmatrix} 1 & 0 \\ 0 & 0.001 \end{bmatrix}$
- **(D)** $\begin{bmatrix} 1000 & 0 \\ 0 & 0.001 \end{bmatrix}$
- **(E)** $\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$

<details><summary>Answer</summary>

**Correct: (B)** *(unverified)*

Conditioning measures how unequally a matrix stretches different directions: the ratio of the largest stretch to the smallest. The matrix $0.001\,I$ has determinant $10^{-6}$ but stretches every direction by the same factor, so a relative error in $\mathbf{b}$ becomes the same relative error in $\mathbf{x}$; it is as well-conditioned as the identity. The determinant is a product of stretches and says nothing about their ratio. (Chapter 10 makes this precise with singular values; here it is the qualitative warning of Section 1.8.)

Why the distractors tempt:
- (A) Distractor: this one has a small determinant and IS ill-conditioned (nearly parallel rows), so it supports the claim rather than refuting it.
- (C) Distractor: small determinant and ill-conditioned (stretches one direction $1000$ times more than the other); consistent with the claim.
- (D) Trick: determinant exactly $1$ yet badly conditioned. It refutes the converse claim (that a determinant near $1$ means well-conditioned), not the claim that was made.
- (E) Distractor: well-conditioned, but its determinant is $-2$, not small, so it does not test the claim at all.

</details>

---

## ESE2030-0330
*week 1 · POOL pool #38 · needs-review · Core*  
skills: `W01.S10` Say what conditioning warns about and what it does not — and that a small determinant is not the diagnostic  

The matrix $A$ of a system $A\mathbf{x} = \mathbf{b}$ is nonsingular but ill-conditioned. What does the ill-conditioning warn you about?

- **(A)** $\det A$ is close to zero
- **(B)** The system may have no solution
- **(C)** The solution is not unique
- **(D)** A small change in $\mathbf{b}$ can move the solution $\mathbf{x}$ a long way
- **(E)** Elimination will meet a zero pivot and must exchange rows to proceed

<details><summary>Answer</summary>

**Correct: (D)** *(unverified)*

Ill-conditioning is about sensitivity, not existence or uniqueness. A nonsingular matrix has exactly one solution for every $\mathbf{b}$; conditioning asks how far that solution moves when $\mathbf{b}$ is perturbed by measurement error, roundoff, or truncation. A matrix that stretches some direction a thousand times more than another can amplify a small error in $\mathbf{b}$ by that same factor in $\mathbf{x}$, so the computed answer deserves skepticism even though it exists and is unique.

Why the distractors tempt:
- (A) Trick: the listed trap in reverse. A small determinant is neither necessary nor sufficient for ill-conditioning; the diagnostic is the ratio of stretches, not their product.
- (B) Distractor: existence is settled by nonsingularity. Ill-conditioning never removes a solution; it makes the one that exists unreliable to compute.
- (C) Distractor: uniqueness is likewise settled by nonsingularity.
- (E) Distractor: a zero pivot is an exact event handled by pivoting; ill-conditioning is a matter of degree and persists under any pivoting strategy.

</details>

---

## ESE2030-0331
*week 2 · POOL pool #39 · needs-review · Core*  
skills: `W02.S09` Recognize an infinite-dimensional space and say why it is one  

Which of the following vector spaces is infinite-dimensional?

- **(A)** $\mathcal{P}_{100}$, the polynomials of degree at most $100$
- **(B)** The solutions of $y'' + y = 0$ on $\mathbb{R}$
- **(C)** $\mathbb{R}^{10\times 10}$, the $10\times 10$ real matrices
- **(D)** The symmetric $4\times 4$ real matrices
- **(E)** $\mathcal{P}$, the polynomials of every degree

<details><summary>Answer</summary>

**Correct: (E)** *(unverified)*

A space is infinite-dimensional when it has no finite spanning set. In $\mathcal{P}$ the monomials $1, x, x^2, \ldots, x^n$ are independent for every $n$; were some $k$ polynomials to span $\mathcal{P}$, the Exchange Bound would cap every independent set at $k$ members, and the monomials do not respect the cap. The other four spaces have finite bases: $101$, $2$, $100$, and $10$ elements respectively. A large dimension is still a dimension.

Why the distractors tempt:
- (A) Distractor: $\dim \mathcal{P}_{100} = 101$; large, but the monomials $1, \ldots, x^{100}$ are a finite spanning set.
- (B) Trick: a space of functions, but a two-dimensional one, spanned by $\cos t$ and $\sin t$. Being made of functions does not make a space infinite-dimensional.
- (C) Distractor: dimension $100$, one for each entry.
- (D) Distractor: dimension $10$, one for each entry on or above the diagonal.

</details>

---

## ESE2030-0332
*week 3 · POOL pool #40 · needs-review · Core*  
skills: `W03.S07` Distinguish the quotient V/U from a complement of U, and know how a direct-sum decomposition V = U ⊕ U′ makes U′ a model for V/U  

Let $V = \mathbb{R}^3$ and let $U$ be the $z$-axis. Which statement about the quotient $V/U$ is forced?

- **(A)** The $xy$-plane is the unique complement of $U$
- **(B)** $V/U$ is the $xy$-plane
- **(C)** $\dim V/U = 2$
- **(D)** $V/U = U^\perp$
- **(E)** $V/U$ is a subspace of $V$

<details><summary>Answer</summary>

**Correct: (C)** *(unverified)*

$\dim V/U = \dim V - \dim U = 3 - 1 = 2$, and that is the only statement here that depends on nothing but $V$ and $U$. The quotient is the space of cosets $\mathbf{v} + U$, the lines parallel to the $z$-axis; it is not a subspace of $V$. Any plane through the origin that does not contain the $z$-axis is a complement of $U$, and each such plane is isomorphic to $V/U$; but the plane is a choice, and the quotient is not.

Why the distractors tempt:
- (A) Trick: the listed trap. The $xy$-plane is one complement among infinitely many; the plane $z = x$ is another. A complement is a choice.
- (B) Trick: the $xy$-plane is a model for $V/U$ (a complement), not $V/U$ itself. The elements of $V/U$ are cosets, vertical lines, not vectors.
- (D) Distractor: $U^\perp$ needs an inner product, which the quotient construction never uses; and even with one, $U^\perp$ is a complement (a subspace of $V$), not the quotient.
- (E) Distractor: the quotient is built from $V$ but does not live inside it; its elements are equivalence classes of vectors.

</details>

---

## ESE2030-0333
*week 3 · POOL pool #41 · needs-review · Core*  
skills: `W03.S07` Distinguish the quotient V/U from a complement of U, and know how a direct-sum decomposition V = U ⊕ U′ makes U′ a model for V/U  

Let $U = \operatorname{span}\{(1, 1, 0)\}$ in $\mathbb{R}^3$. Which of the following planes through the origin is NOT a complement of $U$?

- **(A)** The plane $x = 0$
- **(B)** The plane $y = 0$
- **(C)** The plane $x + y + z = 0$
- **(D)** The plane $x = y$
- **(E)** The plane $z = x$

<details><summary>Answer</summary>

**Correct: (D)** *(unverified)*

A subspace $W$ is a complement of $U$ when $U \cap W = \{\mathbf{0}\}$ and $U + W = \mathbb{R}^3$; for a plane, the dimension count $1 + 2 = 3$ makes trivial intersection the whole condition. The vector $(1,1,0)$ satisfies $x = y$, so that plane contains $U$ and the intersection is all of $U$. The other four planes miss $(1,1,0)$ and are all complements, none canonical: a direct-sum decomposition $\mathbb{R}^3 = U \oplus W$ makes each of them a model for $\mathbb{R}^3/U$.

Why the distractors tempt:
- (A) Distractor: $(1,1,0)$ has $x = 1 \neq 0$, so the plane misses $U$; it is a complement.
- (B) Distractor: $(1,1,0)$ has $y = 1 \neq 0$; a complement.
- (C) Trick: a student who thinks a complement must be perpendicular to $U$ may reject this plane because its normal $(1,1,1)$ is not parallel to $(1,1,0)$. But $1 + 1 + 0 = 2 \neq 0$, the plane misses $U$, and no inner product is needed for complements at all.
- (E) Distractor: $(1,1,0)$ has $z = 0 \neq 1 = x$; a complement.

</details>

---

## ESE2030-0334
*week 3 · POOL pool #42 · needs-review · Core*  
skills: `W03.S10` Recognize that rank(A) = rank(Aᵀ) is a theorem (the FTLA), not a definition  

A matrix $A \in \mathbb{R}^{7\times 4}$ has rank $3$. What is $\dim \ker(A^T)$?

- **(A)** 4
- **(B)** 1
- **(C)** 3
- **(D)** 7
- **(E)** It cannot be determined from the rank of $A$ alone

<details><summary>Answer</summary>

**Correct: (A)** *(unverified)*

$A^T$ is $4\times 7$, a map out of $\mathbb{R}^7$, so Rank--Nullity for $A^T$ reads $\operatorname{rank}(A^T) + \dim\ker(A^T) = 7$. The step that needs a theorem is $\operatorname{rank}(A^T) = \operatorname{rank}(A) = 3$: the Fundamental Theorem identifies the coimage of $A$ with its image, and the coimage has the dimension of the row space, which is the image of $A^T$. Hence $\dim\ker(A^T) = 7 - 3 = 4$. This is the cokernel of $A$, and its dimension is the number of independent constraints a right-hand side must satisfy to be reachable.

Why the distractors tempt:
- (B) Distractor: $4 - 3 = 1$ is the nullity of $A$, computed with the domain of $A$; the question asks about $A^T$, whose domain is $\mathbb{R}^7$.
- (C) Distractor: the rank itself, which is the dimension of the image of $A^T$, not of its kernel.
- (D) Distractor: the number of rows; forgets to subtract the rank.
- (E) Trick: the listed trap taken the other way. That $\operatorname{rank}(A^T) = \operatorname{rank}(A)$ is not obvious, but it is a theorem, and once it is in hand the count is determined.

</details>

---

## ESE2030-0335
*week 4 · POOL pool #43 · needs-review · Core*  
skills: `W04.S07` Extend an independent set to a basis and trim a spanning set to one; use dimension counting as a proof technique  

The set $\{1 + x,\; x^2\}$ is linearly independent in $\mathcal{P}_3$. Which pair of polynomials extends it to a basis of $\mathcal{P}_3$?

- **(A)** $\{1,\; x\}$
- **(B)** $\{x,\; x^3\}$
- **(C)** $\{1 + x + x^2,\; x^3\}$
- **(D)** $\{2 + 2x,\; x^3\}$
- **(E)** $\{x^2,\; x^3\}$

<details><summary>Answer</summary>

**Correct: (B)** *(unverified)*

$\dim \mathcal{P}_3 = 4$, so exactly two more polynomials are needed, and they must keep the set independent. $\{1 + x, x^2, x, x^3\}$ is independent: from $x$ and $1 + x$ one recovers $1$, so the four span $\{1, x, x^2, x^3\}$ and hence all of $\mathcal{P}_3$. Basis Extension guarantees some pair works; it does not say every pair does, and the four rejected pairs each introduce a dependence on what is already present.

Why the distractors tempt:
- (A) Trick: adds two polynomials, but $1 + x$, $1$, and $x$ are dependent ($1 + x = 1 + x$), so the set of four has rank $3$ and spans only a hyperplane of $\mathcal{P}_3$.
- (C) Distractor: $1 + x + x^2 = (1 + x) + x^2$ is already in the span of the given set.
- (D) Distractor: $2 + 2x = 2(1 + x)$ is a multiple of a vector already present.
- (E) Distractor: $x^2$ is already in the set; adding it again adds nothing, and the four-element list is dependent.

</details>

---

## ESE2030-0336
*week 4 · POOL pool #44 · needs-review · Core*  
skills: `W04.S07` Extend an independent set to a basis and trim a spanning set to one; use dimension counting as a proof technique  

Five vectors $\mathbf{v}_1, \ldots, \mathbf{v}_5$ span $\mathbb{R}^3$. Which statement is forced?

- **(A)** Any three of them form a basis
- **(B)** Exactly two of them are redundant, and which two is determined by the set
- **(C)** All five are dependent, so none of them can belong to a basis
- **(D)** Five vectors cannot span $\mathbb{R}^3$; three is the most a spanning set can have
- **(E)** Some three of them form a basis

<details><summary>Answer</summary>

**Correct: (E)** *(unverified)*

A spanning set can always be trimmed to a basis: discard any vector that is a combination of the others and the span is unchanged; repeat until the survivors are independent. Since $\dim \mathbb{R}^3 = 3$ the survivors number exactly three. Which three survive depends on the order of discarding, so the trimmed basis is not unique, and the three chosen must actually be independent, so not every triple qualifies.

Why the distractors tempt:
- (A) Trick: the listed trap. Three vectors in a three-dimensional space are a basis only if independent; if $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ all lie in one plane they span only that plane.
- (B) Distractor: two must go, but which two is a choice. If $\mathbf{v}_1 = \mathbf{v}_2$, either may be discarded.
- (C) Trick: dependence of the whole list does not taint its members; a dependent spanning list always contains an independent spanning sublist.
- (D) Distractor: spanning sets can be as large as one likes; it is independent sets that are capped at the dimension (the Exchange Bound).

</details>

---

## ESE2030-0337
*week 4 · POOL pool #45 · needs-review · Deeper*  
skills: `W04.S08` Recognize which questions require a basis and which do not (dimension and quotient do not; coordinates and matrices do)  

Let $T : V \to V$ be a linear operator on a finite-dimensional space and $\mathbf{v} \in V$. Consider the following quantities:

I. $\dim \ker T$

II. The coordinate vector $[\mathbf{v}]_B$

III. The trace of the matrix representing $T$

Which of them require a choice of basis before they can be computed?

- **(A)** I only
- **(B)** II only
- **(C)** III only
- **(D)** II and III only
- **(E)** I and III only

<details><summary>Answer</summary>

**Correct: (B)** *(unverified)*

Coordinates exist only relative to a basis: the same vector has different coordinate vectors in different bases, so II requires the choice. The kernel of $T$ is defined by the map alone, with no basis in sight, so its dimension is coordinate-free. The trace is subtler: one computes it from a matrix, which needs a basis, but similar matrices have equal traces, so the number obtained does not depend on which basis was used. It is a property of the operator that happens to be computed through coordinates.

Why the distractors tempt:
- (A) Distractor: the kernel is $\{\mathbf{v} : T\mathbf{v} = \mathbf{0}\}$, a set defined by $T$ alone; no basis enters.
- (C) Distractor: the trace is basis-independent (a similarity invariant), and coordinates are the one thing here that is not.
- (D) Trick: the trace is computed via a matrix, but every basis gives the same answer, so nothing is being chosen. A quantity that needs a basis to compute but not to define is coordinate-free.
- (E) Distractor: both of these are properties of $T$ itself; neither depends on a basis.

</details>

---

## ESE2030-0338
*week 5 · POOL pool #46 · needs-review · Core*  
skills: `W05.S09` Recognize the Gram matrix AᵀA: symmetric, positive semidefinite, ker(AᵀA) = ker A, and invertible exactly when the columns of A are independent  

A matrix $A \in \mathbb{R}^{5\times 3}$ has linearly independent columns. Which statement about $A^TA$ and $AA^T$ is forced?

- **(A)** Both $A^TA$ and $AA^T$ are invertible
- **(B)** $A^TA$ is $3\times 3$ and singular; $AA^T$ is $5\times 5$ and invertible
- **(C)** $A^TA = I$
- **(D)** $A^TA$ is $3\times 3$ and invertible; $AA^T$ is $5\times 5$ and singular
- **(E)** $A^TA$ is invertible only if $A$ is square

<details><summary>Answer</summary>

**Correct: (D)** *(unverified)*

$A^TA$ is the Gram matrix of the columns of $A$: $3\times 3$, symmetric, and with $\ker(A^TA) = \ker A = \{\mathbf{0}\}$ because the columns are independent, hence invertible. $AA^T$ is $5\times 5$ but has rank at most $\operatorname{rank} A = 3 < 5$, so it is singular. Independence of the columns is exactly the condition for the Gram matrix to be invertible, and it says nothing about the larger product.

Why the distractors tempt:
- (A) Distractor: $AA^T$ has rank at most $3$ in a $5\times 5$ frame; it cannot be invertible.
- (B) Distractor: the two conclusions swapped. The small Gram matrix is the invertible one when the columns are independent.
- (C) Trick: $A^TA = I$ says the columns are orthonormal, far more than independent. Independence gives invertibility, not the identity.
- (E) Distractor: $A^TA$ is square whatever the shape of $A$; its invertibility is decided by the columns of $A$, not by $A$ being square.

</details>

---

## ESE2030-0339
*week 5 · POOL pool #47 · needs-review · Core*  
skills: `W05.S09` Recognize the Gram matrix AᵀA: symmetric, positive semidefinite, ker(AᵀA) = ker A, and invertible exactly when the columns of A are independent  

For $A \in \mathbb{R}^{m\times n}$ and $\mathbf{x} \in \mathbb{R}^n$, the number $\mathbf{x}^T(A^TA)\mathbf{x}$ equals which of the following?

- **(A)** $\|\mathbf{x}\|^2$
- **(B)** $\langle A\mathbf{x}, \mathbf{x}\rangle$
- **(C)** $\|A^T\mathbf{x}\|^2$
- **(D)** $\|A\|_F^2\,\|\mathbf{x}\|^2$
- **(E)** $\|A\mathbf{x}\|^2$

<details><summary>Answer</summary>

**Correct: (E)** *(unverified)*

Regroup: $\mathbf{x}^TA^TA\mathbf{x} = (A\mathbf{x})^T(A\mathbf{x}) = \|A\mathbf{x}\|^2$. This one line is the whole theory of the Gram matrix: the quadratic form is a squared length, so it is never negative ($A^TA$ is positive semidefinite), and it vanishes exactly when $A\mathbf{x} = \mathbf{0}$, so $\ker(A^TA) = \ker A$ and $A^TA$ is positive definite precisely when the columns of $A$ are independent.

Why the distractors tempt:
- (A) Distractor: true only when $A$ has orthonormal columns ($A^TA = I$); in general $A$ changes lengths.
- (B) Distractor: $A\mathbf{x}$ lives in $\mathbb{R}^m$ and $\mathbf{x}$ in $\mathbb{R}^n$, so the pairing is not even defined unless $m = n$, and then it is $\mathbf{x}^TA\mathbf{x}$, a different quadratic form.
- (C) Distractor: $A^T\mathbf{x}$ is undefined for $\mathbf{x} \in \mathbb{R}^n$ unless $m = n$; the transpose belongs on the outside of the product, not on the vector.
- (D) Distractor: an upper bound (Cauchy--Schwarz in the Frobenius pairing), not an equality.

</details>

---

## ESE2030-0340
*week 6 · POOL pool #48 · needs-review · Core*  
skills: `W06.S10` Know what ridge regularization does (shrinks the solution, not the residual; unique for every λ > 0; tends to A⁺b as λ → 0)  

Ridge regression minimizes $\|A\mathbf{x} - \mathbf{b}\|^2 + \lambda\|\mathbf{x}\|^2$ with solution $\mathbf{x}_\lambda$. The parameter $\lambda > 0$ is increased. What happens to the size of the solution $\|\mathbf{x}_\lambda\|$ and to the residual $\|A\mathbf{x}_\lambda - \mathbf{b}\|$?

- **(A)** $\|\mathbf{x}_\lambda\|$ decreases; the residual does not decrease
- **(B)** Both $\|\mathbf{x}_\lambda\|$ and the residual decrease
- **(C)** $\|\mathbf{x}_\lambda\|$ increases; the residual decreases
- **(D)** $\|\mathbf{x}_\lambda\|$ decreases; the residual is unchanged
- **(E)** Both $\|\mathbf{x}_\lambda\|$ and the residual increase

<details><summary>Answer</summary>

**Correct: (A)** *(unverified)*  — partial credit: D

The penalty $\lambda\|\mathbf{x}\|^2$ charges for the size of the solution, and a larger $\lambda$ charges more, so the minimizer shrinks. The unpenalized least squares solution already makes the residual as small as it can be; any other $\mathbf{x}$, the shrunken one included, has a residual at least as large. Regularization trades fit for a smaller, better-behaved solution: it shrinks $\mathbf{x}$, not the residual. (Chapter 10 will show it as damping of the small singular values.)

Why the distractors tempt:
- (B) Trick: the listed trap. Ridge cannot lower the residual below the least squares minimum; it moves away from that minimum on purpose.
- (C) Distractor: backwards on both counts; the penalty pushes $\mathbf{x}$ toward zero, not away.
- (D) Partial credit: sees that the penalty shrinks the solution. Insight 1 of 2: $\|\mathbf{x}_\lambda\|$ decreases with $\lambda$. Missing: leaving the least squares minimizer costs fit, so the residual grows. Prefix: yes. Guessable: no. Defensible: yes.
- (E) Distractor: the residual does grow, but the solution shrinks; the penalty is on $\|\mathbf{x}\|$.

</details>

---

## ESE2030-0341
*week 6 · POOL pool #49 · needs-review · Deeper*  
skills: `W06.S10` Know what ridge regularization does (shrinks the solution, not the residual; unique for every λ > 0; tends to A⁺b as λ → 0)  

The columns of $A$ are linearly dependent, so the least squares problem $\min \|A\mathbf{x} - \mathbf{b}\|^2$ has infinitely many solutions. For $\lambda > 0$ the ridge problem $\min \|A\mathbf{x} - \mathbf{b}\|^2 + \lambda\|\mathbf{x}\|^2$ has a unique solution $\mathbf{x}_\lambda$. As $\lambda \to 0^+$, what does $\mathbf{x}_\lambda$ tend to?

- **(A)** $(A^TA)^{-1}A^T\mathbf{b}$
- **(B)** It diverges, since $A^TA$ is singular
- **(C)** $A^+\mathbf{b}$, the least squares solution of minimum norm
- **(D)** A least squares solution, but not a determined one
- **(E)** $\mathbf{0}$

<details><summary>Answer</summary>

**Correct: (C)** *(unverified)*  — partial credit: D

For every $\lambda > 0$ the modified normal equations $(A^TA + \lambda I)\mathbf{x} = A^T\mathbf{b}$ have a unique solution, rank-deficient $A$ or not. As the penalty is switched off the solution approaches the least squares set, and among the infinitely many least squares solutions the penalty on $\|\mathbf{x}\|$ has been selecting for smallness all along: the limit is the one of minimum norm, $A^+\mathbf{b}$. Ridge regularization is a continuous path that lands on the pseudoinverse solution.

Why the distractors tempt:
- (A) Trick: the formula for independent columns. Here $A^TA$ is singular and the inverse does not exist; this is the listed Week 6 trap.
- (B) Distractor: the singular limit of the matrix does not make the solutions blow up; the penalty keeps $\|\mathbf{x}_\lambda\|$ bounded by the norm of any least squares solution.
- (D) Partial credit: has that the limit solves the least squares problem. Insight 1 of 2: the limit is a least squares solution. Missing: the penalty singles out the minimum-norm one, so the limit is determined. Prefix: yes. Guessable: no. Defensible: yes.
- (E) Distractor: the $\lambda \to \infty$ limit, where the penalty dominates and everything is shrunk to nothing.

</details>

---

## ESE2030-0342
*week 8 · POOL pool #50 · needs-review · Core*  
skills: `W08.S04` Know what a generalized eigenvector is ((A − λI)w = v) and what it buys — the t e^{λt} terms — without constructing chains by hand  

$\lambda$ is an eigenvalue of $A$ with eigenvector $\mathbf{v}$, and $\mathbf{w}$ is a vector with $(A - \lambda I)\mathbf{w} = \mathbf{v}$. Which of the following is a solution of $\dot{\mathbf{x}} = A\mathbf{x}$ that the vector $\mathbf{w}$ makes available?

- **(A)** $e^{\lambda t}(\mathbf{v} + t\,\mathbf{w})$
- **(B)** $t\,e^{\lambda t}\,\mathbf{w}$
- **(C)** $e^{\lambda t}\,\mathbf{w}$
- **(D)** $t\,e^{\lambda t}\,\mathbf{v}$
- **(E)** $e^{\lambda t}(\mathbf{w} + t\,\mathbf{v})$

<details><summary>Answer</summary>

**Correct: (E)** *(unverified)*  — partial credit: A

Differentiate $\mathbf{x} = e^{\lambda t}(\mathbf{w} + t\mathbf{v})$: $\dot{\mathbf{x}} = e^{\lambda t}(\lambda\mathbf{w} + \lambda t\mathbf{v} + \mathbf{v})$. Apply $A$: $A\mathbf{x} = e^{\lambda t}(A\mathbf{w} + tA\mathbf{v}) = e^{\lambda t}(\lambda\mathbf{w} + \mathbf{v} + \lambda t\mathbf{v})$, using $A\mathbf{w} = \lambda\mathbf{w} + \mathbf{v}$. The two agree. The generalized eigenvector buys the $t e^{\lambda t}$ term that a defective eigenvalue needs and an eigenvector alone cannot supply; the $t$ multiplies the eigenvector, and the generalized eigenvector rides along without it.

Why the distractors tempt:
- (A) Partial credit: the right two ingredients with the roles swapped. Insight 1 of 2: the solution combines $\mathbf{v}$ and $\mathbf{w}$ with a factor $t e^{\lambda t}$. Missing: differentiating shows the $t$ must sit on the eigenvector; $e^{\lambda t}(\mathbf{v} + t\mathbf{w})$ fails since $A\mathbf{w} \neq \lambda\mathbf{w}$. Prefix: yes. Guessable: no. Defensible: yes.
- (B) Distractor: $\frac{d}{dt}(te^{\lambda t}\mathbf{w}) = e^{\lambda t}\mathbf{w} + \lambda t e^{\lambda t}\mathbf{w}$, while $A(te^{\lambda t}\mathbf{w}) = te^{\lambda t}(\lambda\mathbf{w} + \mathbf{v})$; the terms without $t$ do not match.
- (C) Trick: treats $\mathbf{w}$ as an eigenvector. $A\mathbf{w} = \lambda\mathbf{w} + \mathbf{v} \neq \lambda\mathbf{w}$, so $e^{\lambda t}\mathbf{w}$ is not a solution.
- (D) Distractor: the listed trap in a new coat: the $te^{\lambda t}$ term never appears alone; differentiating it produces an $e^{\lambda t}\mathbf{v}$ that must be absorbed by the $\mathbf{w}$ term.

</details>

---

## ESE2030-0343
*week 8 · POOL pool #51 · needs-review · Core*  
skills: `W08.S08` Distinguish the QR ALGORITHM (eigenvalues, Week 8) from the QR DECOMPOSITION (factorization, Week 5), and know that Jordan form is a theorem, not what software computes  

You need all the eigenvalues of a $200\times 200$ nonsymmetric matrix $A$, numerically. Which procedure does the job?

- **(A)** Factor $A = QR$ once and read the eigenvalues off the diagonal of $R$
- **(B)** Compute the Jordan canonical form of $A$ and read its diagonal
- **(C)** Expand $\det(A - \lambda I)$ and find the roots of the resulting polynomial of degree $200$
- **(D)** Iterate $A_k = Q_kR_k$, $A_{k+1} = R_kQ_k$, and read the diagonal of the limit
- **(E)** Apply Gram--Schmidt to the columns of $A$ and read the lengths of the resulting vectors

<details><summary>Answer</summary>

**Correct: (D)** *(unverified)*

This is the QR algorithm. Each step replaces $A_k$ by $R_kQ_k = Q_k^TA_kQ_k$, a similar matrix with the same spectrum, and the iterates converge to a triangular matrix (block triangular, with $2\times 2$ blocks, for complex conjugate pairs) whose diagonal carries the eigenvalues. It is what software actually runs. The QR decomposition of Week 5 is one ingredient of one step; by itself it computes nothing about eigenvalues.

Why the distractors tempt:
- (A) Trick: the listed confusion of the QR decomposition (Week 5) with the QR algorithm (Week 8). The diagonal of $R$ records lengths in Gram--Schmidt, not eigenvalues; one factorization is one step of the algorithm, and the step has not been taken.
- (B) Trick: the listed trap. Jordan form is a theorem about similarity, numerically unstable to compute and not what any software produces.
- (C) Distractor: correct in principle, hopeless in practice. Root-finding on a degree-$200$ polynomial is catastrophically ill-conditioned, and the determinant is never expanded in numerical work.
- (E) Distractor: Gram--Schmidt produces the $Q$ and $R$ of a single factorization; the lengths are the diagonal of $R$, and again these are not eigenvalues.

</details>

---

## ESE2030-0344
*week 9 · POOL pool #52 · needs-review · Core*  
skills: `W09.S08` Know what the Rayleigh quotient measures and that its extremes are λ_max and λ_min at the eigenvectors  

A symmetric $3\times 3$ matrix $A$ has eigenvalues $1$, $4$, and $9$. As $\mathbf{x}$ ranges over all nonzero vectors in $\mathbb{R}^3$, what is the set of values taken by $\dfrac{\mathbf{x}^TA\mathbf{x}}{\mathbf{x}^T\mathbf{x}}$?

- **(A)** $\{1, 4, 9\}$
- **(B)** $[1, 9]$
- **(C)** $[0, 9]$
- **(D)** $[4, 9]$
- **(E)** $(-\infty, \infty)$

<details><summary>Answer</summary>

**Correct: (B)** *(unverified)*

This is the Rayleigh quotient. For symmetric $A$ its maximum is $\lambda_{\max} = 9$, attained at the corresponding eigenvector, and its minimum is $\lambda_{\min} = 1$; between them every value is attained, since the quotient is continuous on the connected unit sphere. In the eigenbasis the quotient is a weighted average $(c_1^2 + 4c_2^2 + 9c_3^2)/(c_1^2 + c_2^2 + c_3^2)$ of the eigenvalues, and a weighted average sweeps out exactly the interval between the extremes.

Why the distractors tempt:
- (A) Trick: the eigenvalues are the values at the eigenvectors, but every other direction gives a mixture. The quotient is not confined to the spectrum; it fills the gaps.
- (C) Distractor: the lower end is $\lambda_{\min} = 1$, not $0$; since every eigenvalue is positive, $\mathbf{x}^TA\mathbf{x} > 0$ for all $\mathbf{x} \neq \mathbf{0}$.
- (D) Distractor: drops the smallest eigenvalue; the eigenvector for $\lambda = 1$ gives the quotient the value $1$.
- (E) Distractor: the denominator normalizes away the length of $\mathbf{x}$, and the numerator is then bounded by the extreme eigenvalues. Unboundedness would need a nonsymmetric matrix and a different story.

</details>

---

## ESE2030-0345
*week 9 · POOL pool #53 · needs-review · Synthesis*  
skills: `W09.S08` Know what the Rayleigh quotient measures and that its extremes are λ_max and λ_min at the eigenvectors  

Let $[C]$ be the covariance matrix of a centered data set and let $\mathbf{w}$ be a unit vector. What does $\mathbf{w}^T[C]\mathbf{w}$ measure, and over all unit vectors where is it largest?

- **(A)** The correlation between $\mathbf{w}$ and the data; largest value $1$
- **(B)** The mean of the data projected onto $\mathbf{w}$; largest along the direction of the mean
- **(C)** The variance of the data projected onto $\mathbf{w}$; largest at the first principal component, with value $\lambda_{\max}$
- **(D)** The variance of the data projected onto $\mathbf{w}$; largest at the last principal component, with value $\lambda_{\min}$
- **(E)** The total variance of the data; the same for every unit $\mathbf{w}$

<details><summary>Answer</summary>

**Correct: (C)** *(unverified)*

Projecting each centered data point onto $\mathbf{w}$ gives the scalars $\mathbf{x}_i^T\mathbf{w}$, whose variance is $\frac{1}{n}\sum_i(\mathbf{x}_i^T\mathbf{w})^2 = \mathbf{w}^T[C]\mathbf{w}$. That is the Rayleigh quotient of the symmetric matrix $[C]$ on the unit sphere, so its maximum is $\lambda_{\max}$, attained at the top eigenvector, which is by definition the first principal component. PCA is the Rayleigh quotient at work: the direction of greatest variance is the direction the quotient singles out.

Why the distractors tempt:
- (A) Distractor: correlation is a cosine between two centered variables; $\mathbf{w}$ is a direction, not a variable, and the quadratic form has the units of variance.
- (B) Trick: the data are centered, so the projected mean is zero along every direction; and the mean would be linear in $\mathbf{w}$, not quadratic.
- (D) Distractor: the minimum of the Rayleigh quotient is at $\lambda_{\min}$; the question asks for the maximum.
- (E) Distractor: the total variance is the trace of $[C]$, the sum over an orthonormal basis of directions; a single direction captures only its share.

</details>

---

## ESE2030-0346
*week 11 · POOL pool #54 · needs-review · Core*  
skills: `W11.S10` Know what the nuclear norm is and why it stands in for rank; recognize the low-rank- plus-sparse decomposition and what "sparse" means there  

Let $A$ have singular values $\sigma_1 \geq \sigma_2 \geq \cdots$ and eigenvalues $\lambda_i$ (if square). The nuclear norm $\|A\|_*$ equals which of the following?

- **(A)** $\displaystyle\sum_i \sigma_i$
- **(B)** $\sigma_1$
- **(C)** $\displaystyle\sqrt{\sum_i \sigma_i^2}$
- **(D)** The number of nonzero $\sigma_i$
- **(E)** $\displaystyle\sum_i \lambda_i$

<details><summary>Answer</summary>

**Correct: (A)** *(unverified)*

The nuclear norm is the sum of the singular values. It stands in for rank because rank is the number of nonzero singular values, a count that jumps and cannot be minimized by any smooth or convex method, whereas the sum is a norm, convex, and minimizing it favors matrices with many singular values exactly zero. Eckart--Young--Mirsky's optimality extends to it, and matrix completion and robust PCA are built on it.

Why the distractors tempt:
- (B) Distractor: the spectral (operator) norm, the largest singular value alone.
- (C) Distractor: the Frobenius norm, the root of the sum of squares.
- (D) Trick: that is the rank itself, the quantity the nuclear norm replaces because it is a count and not a norm.
- (E) Distractor: the trace. It agrees with the nuclear norm only for symmetric positive semidefinite matrices, where singular values and eigenvalues coincide.

</details>

---

## ESE2030-0347
*week 11 · POOL pool #55 · needs-review · Core*  
skills: `W11.S10` Know what the nuclear norm is and why it stands in for rank; recognize the low-rank- plus-sparse decomposition and what "sparse" means there  

Robust principal component analysis writes an observed matrix as $M = L + S$ with $L$ of low rank and $S$ ``sparse.'' Which description of $S$ is what sparse means here?

- **(A)** Every entry of $S$ is small compared with the entries of $L$
- **(B)** $S$ has low rank, but lower than $L$
- **(C)** $S$ is the noise: small random entries in every position
- **(D)** $S$ has few nonzero entries, which may be arbitrarily large
- **(E)** $S$ has small nuclear norm

<details><summary>Answer</summary>

**Correct: (D)** *(unverified)*

Sparse means few nonzero entries, with no restriction on their size: gross, structured corruption that touches a small fraction of the matrix and leaves the rest reliable. That is why the sparse part is measured by the entrywise $\ell_1$ norm, which plays for sparsity the role the nuclear norm plays for low rank. Small noise everywhere is a different kind of damage, the kind truncated SVD tolerates on its own; it is the $N$ in $M = L + S + N$, not the $S$.

Why the distractors tempt:
- (A) Trick: the listed trap. Sparsity is about how many entries are nonzero, not how big they are; a single corrupted pixel of enormous value is sparse.
- (B) Distractor: low rank is the property of $L$; if $S$ were also low rank the two could not be told apart.
- (C) Trick: dense small noise is $N$, handled by truncation; the sparse term exists precisely for the errors truncation cannot absorb.
- (E) Distractor: the nuclear norm is the surrogate for rank, applied to $L$; the surrogate for sparsity is the entrywise $\ell_1$ norm.

</details>

---
