# Week 11: Principal Components

*7 problems*

## Topics Covered
- A^T A vs covariance
- Choosing number of components
- Correlation as cosine similarity
- Covariance vs Correlation PCA
- Dimension of vector spaces
- Effect of orthogonal transformations
- Interpreting principal components
- PCA variance structure
- SVD geometry
- angle interpretation
- creative application
- invariance properties
- orthogonality
- physical meaning
- preprocessing and scaling
- singular value decay patterns

---

## Problem Q5-P09

**Week 11** | **Principal Components**
**Concepts:** Covariance vs Correlation PCA, preprocessing and scaling

An engineer monitors a chemical reactor with three sensors measuring temperature ($T$, in °C), pressure ($P$, in kPa), and flow rate ($F$, in mL/min). A week of measurements yields:

$$\text{Temperature: } T \in [180, 220] \text{ °C}$$
$$\text{Pressure: } P \in [2000, 2500] \text{ kPa}$$
$$\text{Flow rate: } F \in [5, 15] \text{ mL/min}$$

The engineer performs covariance PCA on the centered data and finds that the first principal component is approximately:
$$\mathbf{v}_1 \approx (0.002, 0.998, 0.005)^T$$

Which statement best explains this result?

**Choices:**
- (A) Pressure dominates the first principal component because it has the largest absolute variance, masking potentially important patterns in temperature and flow.
- (B) The principal component correctly identifies pressure as the most important variable since it has the widest measurement range.
- (C) This result suggests the three variables are uncorrelated, with pressure varying independently of temperature and flow.
- (D) The small coefficients for temperature and flow indicate these variables contribute negligible information and can be discarded.
- (E) Covariance PCA automatically accounts for different measurement scales, so this result reveals genuine physical dominance of pressure variation.

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P10

**Week 11** | **Principal Components**
**Concepts:** Interpreting principal components, physical meaning

Four vibration sensors measure vertical displacement (in mm) on a suspension bridge at locations: North anchor, North midspan, South midspan, South anchor. After centering the data, (covariance) PCA reveals the following eigenvectors/eigenvalues of $X^TX$:

$$\mathbf{v}_1 = \frac{1}{2}\begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix}, \quad \mathbf{v}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 0 \\ 0 \\ -1 \end{pmatrix}, \quad \mathbf{v}_3 = \frac{1}{\sqrt{2}}\begin{pmatrix} 0 \\ 1 \\ -1 \\ 0 \end{pmatrix}$$

with eigenvalues $\lambda_1 = 36$, $\lambda_2 = 9$, $\lambda_3 = 4$, $\lambda_4 = 1$ (in mm²).

Which interpretation is most consistent with these results?

**Choices:**
- (A) $\mathbf{v}_1$ represents uniform vertical motion of the entire bridge (all sensors move together), capturing 72\
- (B) $\mathbf{v}_2$ represents torsional twisting where the North side moves opposite to the South side, while midspan points remain stationary.
- (C) $\mathbf{v}_3$ represents antisymmetric bending where the two midspan points move in opposite directions while anchors remain fixed.
- (D) All of the above (A, B, and C) are correct interpretations of the principal components.
- (E) None of the above.

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P12

**Week 11** | **Principal Components**
**Concepts:** Dimension of vector spaces

A data scientist analyzes measurements from six sensors monitoring a thermodynamic process. The sensors measure various properties of the system: pressure, temperature, volume, entropy, enthalpy, and work.
The figures below plot (vertically) cumulative explained variance for covariance PCA (left) and correlation PCA (right), versus (horizontally) number of singular values (from 0 to 6). Based on these plots, which interpretation is most appropriate?

\begin{center}
\begin{figure}[h]
\includegraphics[width=7in]{2030 Q5 SCREE COV-COR.jpg}

\end{figure}
\end{center}

![Figure](../images/2030 Q5 SCREE COV-COR.jpg)

**Choices:**
- (A) Covariance PCA reveals that the process is essentially one-dimensional: a single latent variable explains 94\
- (B) Correlation PCA suggests the process has intrinsic dimension approximately 3, with scale differences among sensors masking this structure in the covariance analysis.
- (C) Both analyses agree on low intrinsic dimensionality; correlation PCA is always preferable as it preserves the natural units of measurement.
- (D) The correlation PCA result is misleading because standardizing variables inflates the apparent contribution of low-variance sensors like volume.
- (E) A rank-2 approximation captures over 75\

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P13

**Week 11** | **Principal Components**
**Concepts:** Choosing number of components, singular value decay patterns

Two centered data matrices are analyzed via covariance PCA:

\textbf{Dataset A:} $X_A \in \mathbb{R}^{200 \times 10}$ has all nonzero singular values:
$$\sigma_1 = 24, \quad \sigma_2 = 22, \quad \sigma_3 = 20, \quad \sigma_4 = 18, \quad \sigma_5 = 16, \ldots$$

\textbf{Dataset B:} $X_B \in \mathbb{R}^{200 \times 10}$ has all nonzero singular values:
$$\sigma_1 = 50, \quad \sigma_2 = 25, \quad \sigma_3 = 8, \quad \sigma_4 = 3, \quad \sigma_5 = 1, \ldots$$

Which statement best characterizes the difference between these datasets?

**Choices:**
- (A) Dataset A has clearer low-dimensional structure.
- (B) Dataset B has clearer low-dimensional structure.
- (C) Dataset A is better for dimensionality reduction based on better total variance.
- (D) Both datasets have similar intrinsic dimensionality since all singular values are positive.
- (E) Dataset B should have been handled via correlation PCA.

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P16

**Week 11** | **Principal Components**
**Concepts:** Effect of orthogonal transformations, invariance properties, creative application

Consider two analysts working with the same centered data matrix $X \in \mathbb{R}^{100 \times 6}$ that has singular values $\sigma_1 = 20, \sigma_2 = 15, \sigma_3 = 8, \sigma_4 = 5, \sigma_5 = 2, \sigma_6 = 1$.

\textbf{Analyst A} performs PCA directly on $X$.

\textbf{Analyst B} first applies an orthogonal transformation $Q \in \mathbb{R}^{6 \times 6}$ to get $Y = XQ$, then performs PCA on $Y$.

How do their results compare?

**Choices:**
- (A) Analyst B's principal components are related to Analyst A's by the transformation: $\mathbf{w}_k = Q^T\mathbf{v}_k$, where $\mathbf{v}_k$ are A's principal components.
- (B) Both analysts obtain identical singular values: $\{20, 15, 8, 5, 2, 1\}$, but their principal component directions differ.
- (C) Analyst A's results are superior because applying $Q$ distorts the covariance structure of the data.
- (D) The analyses are equivalent only if $Q$ is a rotation (determinant +1), but not if $Q$ includes reflections (determinant -1).
- (E) Both analyses capture the same total variance and the same variance proportions, but the ordering of principal components may differ.

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P17

**Week 11** | **Principal Components**
**Concepts:** Correlation as cosine similarity, orthogonality, angle interpretation

Four feature vectors $(X_1, X_2, X_3, X_4)$ are extracted from centered sensor data. The covariance and correlation matrices are:

$$[\Sigma] = \begin{bmatrix}
4 & 3 & -4.2 & 6.4 \\
3 & 25 & -6 & -12 \\
-4.2 & -6 & 9 & 1.2 \\
6.4 & -12 & 1.2 & 16
\end{bmatrix}
\quad : \quad
[R] = \begin{bmatrix}
1.0 & 0.3 & -0.7 & 0.8 \\
0.3 & 1.0 & -0.4 & -0.6 \\
-0.7 & -0.4 & 1.0 & 0.1 \\
0.8 & -0.6 & 0.1 & 1.0
\end{bmatrix}$$

Which pairs of feature vectors have directions within $30^\circ$ of being orthogonal?

**Choices:**
- (A) $(X_1, X_3)$ and $(X_2, X_4)$
- (B) $(X_1, X_2)$ and $(X_3, X_4)$
- (C) $(X_2, X_3)$ only
- (D) $(X_1, X_3)$, $(X_2, X_3)$, and $(X_2, X_4)$
- (E) $(X_1, X_2)$, $(X_2, X_3)$, and $(X_3, X_4)$

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---

## Problem Q5-P18

**Week 11** | **Principal Components**
**Concepts:** SVD geometry, PCA variance structure, A^T A vs covariance

A centered data matrix $X \in \mathbb{R}^{100 \times 3}$ represents 100 observations of three variables. The matrix $X^TX$ has eigenvalues:
$$\lambda_1 = 1600, \quad \lambda_2 = 400, \quad \lambda_3 = 100$$

Consider the linear transformation $T: \mathbb{R}^3 \to \mathbb{R}^{100}$ defined by $T(\mathbf{v}) = X\mathbf{v}$. This transformation maps the unit sphere in $\mathbb{R}^3$ to an ellipsoid in $\mathbb{R}^{100}$.

Which statement correctly relates the SVD geometry to the PCA variance structure?

**Choices:**
- (A) The ellipsoid has semi-axis lengths 1600, 400, and 100, which equal the variances along the three principal component directions.
- (B) The ellipsoid has semi-axis lengths 40, 20, and 10, which equal the variances along the three principal component directions.
- (C) The ellipsoid semi-axes have lengths in ratio 4:2:1, while the principal component variances have ratio 16:4:1.
- (D) The ellipsoid semi-axes have lengths in ratio 4:2:1, and the principal component variances have the same ratio 4:2:1.
- (E) The ellipsoid lies in a 3-dimensional subspace of $\mathbb{R}^{100}$, but the semi-axis lengths and PC variances are unrelated quantities.

<details>
<summary>Show Answer</summary>

**Correct: (None)**

</details>

---
