---
name: 2030-mc-quizzam
description: >
  Generate conceptual multiple-choice "Quizzam" problems for ESE 2030
  (Linear Algebra for Engineers), keyed to LAEF 2nd edition. Trigger when
  the user asks for MC, multiple-choice, bubble-sheet, Quizzam, quiz, or
  final-exam problems for ESE 2030; when the user asks to add problems to
  an existing Quizzam .tex file, revise distractors, add or repair a
  figure, generate permuted versions, or produce a solutions guide.
  Covers all 13 weeks: solving systems and abstract structure (1-3),
  geometry and orthogonal decomposition (4-6), eigenvalues and dynamics
  (7-9), SVD and PCA (10-11), probability and high dimension (12), neural
  networks and AI (13). Course philosophy emphasizes conceptual
  understanding over computation, with the Fundamental Theorem of Linear
  Algebra as a recurring spine and a consistent ker/im/coim/coker
  vocabulary.
---

# ESE 2030 Quizzam Multiple-Choice Skill

Quizzams are 60-minute bubble-sheet exams of roughly 22 problems, five
choices (A)-(E), one best answer, partial credit on a minority of
problems, and five permuted versions distributed in a checkerboard
seating pattern.

The format is collaborative: propose a topic-and-form distribution, get
approval, then draft. The instructor revises surgically; adapt without
redrafting whole batches.

**This file teaches procedures, not problems.** It deliberately contains
almost no worked mathematical examples. Earlier versions were dense with
them, and two failures followed: the assistant reused them instead of
generating fresh material, and some drifted out of scope entirely
(a previous edition promoted `det(e^A) = e^{tr A}` to a named pattern —
an identity that appears nowhere in the course text). Concreteness comes
from the source files at generation time, never from this file.

---

## 0. Sources

### The weekly topic files (`WEEK_N_*.txt`) — primary source

Each file has a fixed anatomy. Every section has a distinct job. Mine
**all** of them; the single largest cause of repetitive output is
drafting from CORE CONCEPTS alone.

| Section | Present in | What it supplies |
|---|---|---|
| Header line: `LAEF 2E -- Chapter N (Sections N.x-N.y)` | 13/13 | Provenance for source citations |
| `NOTE ON SCOPE` | 9/13 | What changed in the 2nd edition. **Read first.** Overrides any assumption from general linear-algebra knowledge |
| `CORE CONCEPTS` | 13/13 | Numbered by section, with Def/Lemma/Thm/Ex numbers. Definitions → Recall hooks; theorems → MUST-BE-TRUE and HYPOTHESIS-REMOVAL hooks; "this only works because…" caveats → the best Deeper hooks |
| `ESSENTIAL SKILLS (core; expected without hesitation)` | 13/13 | What the student must be able to *do*. Each admits an IDENTIFY-THE-OBJECT or TOOL-SELECTION stem. Richest source of behavior-level questions |
| `TYPICAL MCQ TRAPS` | 13/13 | **The primary distractor source.** ~7-11 per week, 98 total, curated and in-scope |
| `PERIPHERAL -- CONTEXT ONLY (de-emphasized)` | 13/13 | Authoritative scope exclusions for that week. Do not build problems on these |
| `CONNECTIONS` / `CONNECTIONS FORWARD` | 13/13 | Synthesis hooks, explicitly labelled Back:/Forward: |

Two sections deserve special handling:

**`TYPICAL MCQ TRAPS` is the distractor inventory.** Do not invent
distractors from general knowledge while these sit unread. They are
written in informal shorthand ("projecting onto the row space when the
column space is meant"), so a trap must be **translated into §2 notation**
before it reaches a student. Every problem should be able to point at
the trap entry its main distractor implements.

**`PERIPHERAL` replaces any hardcoded exclusion list.** It is maintained
alongside the course; a list in this file would rot. Some weeks also
carry per-topic de-emphasis inside `NOTE ON SCOPE`.

### `LAEFcorpus.md` — notational and definitional authority

The text itself. When the week file's plain-text shorthand and the
corpus disagree on notation, the corpus wins (the week files are ASCII,
so they write `A^+`, `U^perp`, `rho(A)` where the text writes
`A^\dagger`, `U^\perp`, `\rho(A)`). Search it for a term's actual
treatment before building a problem on it.

### Prior Quizzam `.tex` files — optional

Useful for tone. **Not** required reading before drafting; see §12.

### Scope rule

**A true theorem is not automatically in scope.** If a hook's central
identity or named object does not appear in a week file or the corpus,
it is out — however standard it is in linear algebra generally. When
unsure, search before drafting. This rule exists because plausible-
sounding fabrications are the hardest error to catch by eye.

If the week files for the target weeks are unavailable, say so before
drafting rather than working from generic knowledge.

---

## 1. Philosophy

1. **Conceptual over computational.** Students have computational tools
   in practice. A problem that reduces to "did they row-reduce
   correctly" is a wasted slot. Test why an object exists, what it
   represents, which tool applies, and what changes when an assumption
   changes.

2. **Don't give it away.** The stem must not contain definitions,
   formulas, or theorem names the student should be supplying. If the
   point is whether they recognize that diagonalization applies, do not
   name it — describe the situation. If the point is a dimension count,
   do not cite rank-nullity; let them invoke it.

3. **Bare answer choices.** Each option is a mathematical expression or
   a short declarative phrase. No "because…" clauses, no embedded
   justification. Verbose options invite elimination by reading rather
   than thinking. (Exception: FUNDAMENTAL-DESCRIPTION problems, where
   declarative options are intrinsic. Keep them tight even there.)

4. **Distractors implement named errors.** Every wrong answer
   corresponds to a specific error a real student makes, preferably one
   drawn from that week's `TYPICAL MCQ TRAPS`. If the error cannot be
   named in the comment block, replace the option.

5. **Vary the cognitive task, not just the topic.** Two problems on
   different topics can be the same problem — "which of these is a
   correctly-formed factorization?" is one question whether the object
   is QR, SVD, or the spectral decomposition. Variety is enforced on the
   FORM axis (§3), not the topic axis.

6. **Partial credit is a measurement tool, not a design goal.** It
   applies only to problems that genuinely decompose (§5). Over-awarding
   it compresses the score distribution and erodes the advantage of full
   understanding, which the score transformation then has to fight.

7. **The FTLA spine.** Kernel, image, coimage, cokernel; the
   four-subspace decomposition; `coim T ≅ im T`. It links Wk 3 (abstract
   maps), Wk 6 (the geometric form: `coim = (ker T)^⊥`,
   `coker = (im T)^⊥`, and the pseudoinverse built by inverting the
   isomorphism), Wk 10 (the SVD's four subspaces), and Wk 11 (PCA's
   centered geometry). At least one problem per Quizzam should touch it.

---

## 2. Notation (LAEF 2E)

Verify against `LAEFcorpus.md`; the table is a fast reference, not the
authority.

| Object | This course | Note |
|---|---|---|
| Four fundamental subspaces | `\ker A`, `\operatorname{im} A`, `(\ker A)^\perp`, `(\operatorname{im} A)^\perp` | — |
| Equivalent characterizations | `(\ker A)^\perp = \operatorname{im}(A^T)`, `(\operatorname{im} A)^\perp = \ker(A^T)` | State explicitly when used |
| Coimage / cokernel, algebraic | `\operatorname{coim} T = V/\ker T`, `\operatorname{coker} T = W/\operatorname{im} T` | Quotient construction (Wk 3) |
| Coimage / cokernel, geometric | `\operatorname{coim} T = (\ker T)^\perp`, `\operatorname{coker} T = (\operatorname{im} T)^\perp` | Thm 6.9. **Both forms are course vocabulary**; the Wk 3 → Wk 6 passage from one to the other is itself a strong hook |
| FTLA punchline | `\operatorname{coim} T \cong \operatorname{im} T`; `T` restricts to an isomorphism `(\ker T)^\perp \to \operatorname{im} T` | — |
| Subspace relation | `U < V` means "is a subspace of" | Not a numerical inequality. A genuine source of student confusion |
| Vectors | `\mathbf{v}` (bold); components `v_i`; zero vector `\mathbf{0}` | — |
| Quotient class | equivalence-class framing, `[\mathbf{v}]` | Not "coset" |
| Polynomial spaces | `\mathcal{P}_n`, degree at most `n`, `\dim = n+1` | — |
| Inner product / norm | `\langle \mathbf{u},\mathbf{v}\rangle`; `\norm{\mathbf{v}}` via the `\norm` macro | — |
| Orthogonal projection | `\Pi_U` (macro `\proj{U}`) | Projection *matrix* `P` acceptable when the matrix is the object |
| Direct sums | `\oplus`; orthogonal direct sum `\boxplus` | `\boxplus` is 2E house notation |
| Pseudoinverse | `A^\dagger` | 2E promotes it to §6.4, **before** least squares; least squares is a consequence of it, not its setting. The four Moore-Penrose conditions are course vocabulary (Def 6.12) |
| Pseudoinverse special cases | `A^\dagger = A^{-1}` (invertible); `(A^TA)^{-1}A^T` (independent columns); `A^T(AA^T)^{-1}` (independent rows) | The unguarded middle formula is a listed Wk 6 trap |
| Diagonalization | `A = V\Lambda V^{-1}` | `V^{-1}\Lambda V` is a listed Wk 7 trap |
| Spectral theorem | `A = Q\Lambda Q^T`, `Q` orthogonal | — |
| Matrix exponential | `e^{At}`; defined by power series (Def 7.10); `e^Ae^B = e^{A+B}` only when `AB = BA` (Lemma 7.11) | Entrywise exponentiation is a listed trap |
| Markov | **Column-stochastic**: `\mathbf{x}_{k+1} = A\mathbf{x}_k`, columns sum to 1, `A^T\mathbf{1} = \mathbf{1}`, `\rho(A) = 1` | Mixing conventions mid-problem is a listed Wk 9 trap |
| SVD | `A = U\Sigma V^T`, `\sigma_1 \geq \sigma_2 \geq \cdots \geq 0` | `\sigma_i = \sqrt{\lambda_i(A^TA)}` — be explicit about the root |
| Data matrix | `\mathcal{X}` (macro `\Data`) | Not plain `X` |
| Covariance / correlation matrix | `[C]` (macro `\COV`), `[R]` (macro `\CORR`) | — |
| Covariance scaling | **`[C] = \frac{1}{n}\mathcal{X}^T\mathcal{X}`** for centered `\mathcal{X}` | The `1/n` data-science convention throughout, **not** `1/(n-1)` |
| Wk 13 parameters | `\Psi` all parameters; `\mathcal{L}` loss; `\varsigma` activation; `\hat{\mathbf{y}}` network output; `\delta` error signal / costate | `\mathbf{y}` is reserved for true values |
| Wk 13 layer count | `\Lambda` = **number of layers** | **Collision:** `\Lambda` is the eigenvalue matrix in Wks 7-11. Never let both meanings appear in one problem; in Wk 13 synthesis problems, rename or avoid |
| Derivative in Wk 13 | "derivative" | Not "Jacobian" |
| Assessment name | "Quizzam" | Not "quiz" or "exam" |

### The row/column-space arc — a week-dependent rule

Earlier versions of this file banned "row space," "column space," and
"null space" outright. **That is wrong for the 2E.** The text uses
`\operatorname{row} A` and `\operatorname{col} A` as standing notation,
and the vocabulary follows a deliberate arc:

- **Weeks 1-2:** null space, column space, and row space are the
  *native* vocabulary. Problems should use them.
- **Week 3 onward:** kernel and image are primary. The Wk 3 CONNECTIONS
  entry ("null space and column space from Weeks 1-2 are now kernel and
  image") marks the handover, and the renaming is itself a good
  TRANSLATE hook.
- **Week 6 onward:** the row/column distinction survives as a *targeted
  trap* — "projecting onto the row space when the column space is meant"
  is a listed Wk 6 trap and a legitimate distractor.

So: match the vocabulary to the week, and use the older terms
deliberately rather than accidentally.

---

## 3. Question FORMS

Every problem carries a `% FORM =` tag from this closed list. Forms are
*cognitive tasks*. Topic spread does not produce variety; form spread
does.

| Code | Form | The task |
|---|---|---|
| DIM | DIM-COUNT | Propagate a dimension, rank, or nullity through a structural relation |
| CLS | CLASSIFY | Does this object have property P (diagonalizable, orthogonal, positive semidefinite, stochastic, a member of the subspace) |
| MBT | MUST-BE-TRUE | Which conclusion is *forced* by the hypotheses, versus merely sometimes true |
| CEX | COUNTEREXAMPLE | Which object witnesses the failure of a plausible false claim |
| HYP | HYPOTHESIS-REMOVAL | Drop a hypothesis from a theorem — does the conclusion survive, and which part fails first |
| FUN | FUNDAMENTAL-DESCRIPTION | The defining property versus its true-but-derivative consequences |
| WFM | WELL-FORMED | Which is a correctly-formed instance of a decomposition: shape, ordering, orthogonality, sign, factor position |
| IDO | IDENTIFY-THE-OBJECT | The result of a computation is given; what *is* it (eigenvalue vs singular value; which basis the coordinates are in; variance in which units) |
| TSL | TOOL-SELECTION | Which decomposition or method serves this stated goal, and why this one rather than the near-miss |
| INV | INVARIANCE | What survives a change of setup: similarity, orthogonal change of basis, centering, rescaling the data, row operations |
| PRT | PERTURB-THE-SETUP | One hypothesis or parameter moves; what happens to the answer (append a column; let `\lambda \to 0^+`; make an eigenvalue complex; double the data) |
| FRD | FIGURE-READ | Extract a stated relation or quantity from a supplied figure (§6) |
| FSL | FIGURE-SELECT | The five choices are pictures (§6) |
| TRN | TRANSLATE | Restate algebraic as geometric, or abstract as matrix, or Wk 1-2 vocabulary as Wk 3 vocabulary |
| BND | BOUNDARY-CASE | The degenerate end: the zero map, rank one, a repeated eigenvalue, `\sigma_k = 0`, `n = 1`, `\lambda \to \infty` |

### Quotas (22-problem Quizzam)

- **No form more than 3 times.**
- **At least 8 distinct forms** represented.
- **At least 2 forms** that did not appear on the previous Quizzam.
  (This is the only cross-Quizzam constraint in this file, and it
  concerns *form*, not content — see §12.)
- CEX, HYP, PRT, and BND resist guessing-by-elimination better than the
  others. Include at least two of the four.
- FUN is a course signature but is easy to overuse. Cap at 2.

Scale proportionally for the ~43-problem final: no form more than 5, at
least 11 distinct forms.

### Stem construction

- **Concrete and small.** Fix small dimensions and values so the answer
  space is finite and the student cannot hide in generality.
- **Hand over what isn't being tested.** If a fact is needed but is not
  the point, give it, in a `Given:` clause. The handed fact must never
  be the answer, and must not be the formula under test.
- **No essential computation.** Ask "which of these is X," not
  "compute X." If setting up the question takes three lines of work,
  move the work into `Given:` or rewrite.
- **1-3 sentences.** Longer only when the setup genuinely requires it
  (a two-approach synthesis problem may need a short paragraph each).
- **State the convention** when a convention-sensitive object appears
  (column-stochastic, descending singular values, `1/n` covariance).
  Stating a convention is not a giveaway; relying on an unstated one is
  a bug.

---

## 4. Distractor construction

Four options, each implementing a named error. Build them as procedures,
not by recall of past problems.

**Start from the traps.** Open the week's `TYPICAL MCQ TRAPS`, pick the
entry closest to the hook, and construct the option that a student
committing that error would produce. This is the default route and
should account for most distractors.

### Archetypes, as generative procedures

**D1. Twin pair.** Two options sharing surface structure, differing in
one feature, so elimination-by-scan fails. *Construct:* take the correct
answer and swap exactly one structural element — factor order, which of
two objects gets the operation, which side an inverse or transpose sits
on, which of two subspaces is named. Verify both readings are things a
student might write down. Aim for at least one twin pair per problem
outside pure Recall.

**D2. Correct structure, wrong detail.** *Construct:* take the correct
answer and corrupt exactly one atomic feature — one sign, one exponent,
one index, one ordering, one transpose position. Verify the corruption
matches a trap entry; an unmatched corruption is an arbitrary
perturbation, not a distractor. This is the most common legitimate
partial-credit candidate, but see §5 — being a D2 does not by itself
earn credit.

**D3. Surface match.** Right vocabulary, wrong question. *Construct:*
find a true statement about the same object that answers a *different*
question about it, then offer it. Catches keyword pattern-matching.
**Never earns partial credit** (§5): the error is conceptual, not
incremental.

**D4. Naive prior.** What an untrained student guesses — usually a
scalar rule misapplied to matrices, or an "obvious" symmetry.
*Construct:* ask what the answer would be if the objects commuted, were
scalars, or behaved additively. **Never earns partial credit.**

**D5. Shape implies property.** Inferring a property from a structural
feature that does not entail it. *Construct:* find a feature of the
setup that is *necessary* for the conclusion and offer it as if
*sufficient*, or find two objects of equal dimension and assert a
natural isomorphism.

**D6. Convention collision.** Correct under a different convention than
the one in play. *Construct:* apply the other common convention from
the §2 table. Strongest when the stem has stated the convention, since
the option then also tests careful reading.

**D7. Combine options** — `Both (X) and (Y)` or `None of the above`.
Two legitimate uses:

- *`None` as the genuine answer,* when the four visible options span a
  coherent error landscape and the true statement is absent. Rewards
  confidence.
- *`Both (X) and (Y)` as the genuine answer,* when two visible options
  are equivalent characterizations of the same object via the FTLA, the
  spectral theorem, or another natural isomorphism, and recognizing the
  equivalence *is* the question.

Use sparingly and never as filler. Per Quizzam: `None` correct at most
twice, `Both` correct at most three times. If `None` appears and is
wrong, every visible option must be independently plausible.

### Checklist per problem

- [ ] No option is wrong for an arbitrary reason.
- [ ] The correct answer is genuinely best, with a clean reason it
      dominates the near-misses.
- [ ] At least one distractor traces to a `TYPICAL MCQ TRAPS` entry.
- [ ] At least one twin pair, unless pure Recall.
- [ ] The correct answer is not the longest option.
- [ ] Two of the four wrong options relate to each other (twin pair, or
      two corruptions of the same feature). Four options wrong for four
      unrelated reasons is a weak problem.
- [ ] No escape-hatch option ("cannot be determined") unless it is the
      answer or a live trap. Repeated across problems, these become
      Schelling points for the confused.
- [ ] Vocabulary matches the week (§2's row/column arc).
- [ ] Nothing from that week's `PERIPHERAL` list.

---

## 5. Partial credit

Partial credit is worth 50% of a question. It is appropriate on roughly
a third of problems, never more. Default to **none** and justify each
award affirmatively.

### Three labels

Every wrong option gets exactly one:

```
% \textbf{Partial credit:} — earns 50%. Must pass the gate and all three tests.
% \textbf{Trick answer:}   — implements a named misconception. No credit.
% \textbf{Distractor:}     — plausible error. No credit, not a trap.
```

Most wrong options are `Distractor:`. Earlier versions offered only the
first two, so ordinary wrong answers were inflated into partial credit
because "trick" did not fit them.

### The two-insight gate

**Partial credit is available only on problems that decompose into two
or more separable insights, and only for an option demonstrating one of
them.**

A single-insight problem gets no partial credit, ever. Partial credit is
half the question's value; on a single-insight problem there is no half
to award. Before assigning credit, state the decomposition: "insight 1
is X, insight 2 is Y." If that sentence cannot be written, there is no
partial credit on this problem.

### The three tests — all must pass

1. **Prefix.** The option is reachable by executing a correct *prefix*
   of the intended reasoning and stopping, or by erring only at the
   final step. If reaching it requires a *different, wrong conception*
   rather than an *incomplete correct one*, it is a Trick answer.

2. **No free lunch.** The option is not reachable by surface
   pattern-matching, by guessing, or by a naive prior. If a student who
   knows nothing can land there, the award pays for ignorance. This is
   why D3 and D4 never earn credit.

3. **Defensible.** The half-credit could be justified aloud to a student
   who answered fully correctly and objects. "It felt close" fails.

### Comment format

```
% \textbf{Partial credit:} B -- insight 1 of 2. Has: [the insight demonstrated].
%   Missing: [the insight absent]. Prefix: yes. Guessable: no. Defensible: yes.
```

The three verdicts are written out so the award cannot be made silently.

### Budget

- At most **one** partial-credit option per problem.
- Partial credit on at most **⅓** of problems; report the count (§10).
- For a `Both (X) and (Y)` correct answer, (X) and (Y) individually are
  the natural partial-credit options — but this is the *one* case where
  two are allowed, and only because they are symmetric halves of one
  award. Standard phrasing: "(X) or (Y) individually — recognizes one
  characterization but misses that they describe the same object."

---

## 6. Figures

Budget 2-4 figure problems per Quizzam, at least one FSL. Figures are
generated as TikZ inside the `.tex`; never reference an external image.

### Two rules that decide whether a figure earns its place

**Load-bearing.** If the figure's content can be restated in one
sentence of the stem, it is decoration — delete it, or promote it into
the answer choices as an FSL. Students learn quickly to ignore
decorative figures.

**No measurement.** The figure must not be solvable by reading
coordinates off gridlines; that turns a conceptual exam into a ruler
exercise. Encode only qualitative features: order, sign, orthogonality,
rank, direction, relative magnitude, containment. **Draw no numeric
tick labels** unless the numbers are the point.

### The two forms

**FRD (FIGURE-READ).** The figure carries the data; the stem asks a
conceptual question about it. Good subjects: which drawn vector lies in
which fundamental subspace; whether a drawn decomposition is orthogonal;
which of two singular values is larger; what the drawn orbit implies
about the dominant eigenvalue's magnitude.

**FSL (FIGURE-SELECT).** The five choices are pictures; the stem states
algebraic hypotheses and asks which picture is consistent. This is the
strongest conceptual figure format, because it cannot be solved by
computation or by reading text.

### Permutation safety

Five shuffled versions are generated per Quizzam, so:

- **Never write "the figure on the left," "the upper panel," or "the
  first diagram."** Refer only to labelled objects (`W`, `\mathbf{v}_1`,
  `\Pi_U\mathbf{b}`). Choice order shuffles; spatial references break.
- **Never reference a choice letter in the stem.**
- **For FSL, each choice's `tikzpicture` must be self-contained inside
  its own choice.** Never draw all five panels in one picture labelled
  (i)-(v); the permutation script shuffles choices atomically and cannot
  reorder panels inside a shared picture.
- Use the horizontal `\choicefig` row for FSL (§7), not `enumerate` —
  `enumerate` stacks pictures vertically and consumes a third of a page.

### Solutions guide

Figure problems need a one-line verbal description of the figure in the
comment block. The guide is organized by topic, so the reader must be
able to identify which problem an entry refers to without the picture.

Greyscale only. These are photocopied; nothing may be encoded in colour
alone. Use line weight, dash pattern, and labels to distinguish.

Appendix A holds the primitive library.

---

## 7. LaTeX

### Preamble

```latex
\documentclass[12pt]{amsart}
\pagestyle{plain}

\usepackage{amsmath,amssymb}
\usepackage[shortlabels]{enumitem}
\setlist[enumerate]{itemsep=6pt, topsep=6pt, parsep=0pt}

\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,calc,patterns,decorations.pathreplacing}
\usepackage{needspace}
\usepackage[left=0.75in,right=1in,bottom=0.9in]{geometry}
\usepackage[T1]{fontenc}
\usepackage[parfill]{parskip}
\renewcommand{\baselinestretch}{1}

\newcommand{\norm}[1]{\left\|#1\right\|}

% SECTION DIVIDERS
\newcommand{\divider}{
  \vspace{-1em}
  \noindent
  \raisebox{-0.15ex}{\textbullet}%
  \hspace{0.5em}%
  \rule[0.5ex]{0.95\textwidth}{1.0pt}%
  \hspace{0.5em}%
  \raisebox{-0.15ex}{\textbullet}%
  \vspace{0em}
}

% FIGURE STYLES -- greyscale-safe, print-legible
\tikzset{
  fig/.style={line width=0.7pt, >={Stealth[length=2.2mm]}},
  vec/.style={->, line width=0.9pt},
  sub/.style={line width=1.1pt},
  resid/.style={->, densely dashed, line width=0.7pt},
  ghost/.style={line width=0.5pt, gray},
  lbl/.style={font=\footnotesize, inner sep=1.5pt},
}

% FIGURE ANSWER CHOICES -- one self-contained picture per choice
\newcommand{\choicefig}[2]{%
  \begin{minipage}[t]{0.18\textwidth}\centering
  (#1)\\[2pt]
  \begin{tikzpicture}[fig, scale=0.55]#2\end{tikzpicture}
  \end{minipage}}

\title{ESE 2030 QUIZZAM N : Fall YYYY}
\author{prof-g}
```

Note: `\usepackage{enumerate}` has been dropped. It conflicts with
`enumitem`, which supersedes it and supplies the `[(A)]` syntax via
`shortlabels`.

### Instructions block (verbatim)

```latex
\begin{document}
\maketitle

\begin{center}
    {\bf INSTRUCTIONS}
\end{center}

\begin{itemize}
\item No books, notes, or calculators. Use a writing utensil and logic.
\item Please follow question instructions and fill in the bubble-sheet.
\item Select one answer per problem.
\item Each problem has one best answer.
\item In some problems, a wrong choice may be worth partial credit.
\item Be careful to fill in the correct problem number.
\item These questions are written carefully: if you detect an error, read closely and do your best.
\item If anything is unclear, use your best judgment.
\item Cheating in any form will be dealt with severely.
\end{itemize}

\bigskip
\divider
```

### Page breaks

**Do not emit `\newpage` anywhere.** Not after the instructions, not
between problem groups. The document flows continuously and pagination
is left to LaTeX.

Consequence: a tall problem can split across a page boundary, separating
a stem from its choices. Do not silently prevent this. Instead, tag any
problem judged tall — figure problems, wide-matrix choices, subset
problems with three long items — with

```latex
% TALL -- add \needspace{5\baselineskip} above if this splits badly
```

and leave the decision to the instructor. `\needspace{}` and `\filbreak`
both break only when necessary; neither goes in by default.

### Problem skeleton

```latex
{\bf PROBLEM N:}
% WEEK   = ...
% FORM   = ...
% TOPICS = ...
% SOURCE = ...

[Stem: 1-3 sentences. No giveaways.]

\begin{enumerate}[(A)]
\item [bare answer]
\item [bare answer]
\item [bare answer]
\item [bare answer]
\item [bare answer]
\end{enumerate}

% \textbf{Correct Answer:} X
% \textbf{Explanation:} ...
% \textbf{Partial credit:} ... (or omit)
% \textbf{Trick answer:} ...
% \textbf{Distractor:} ...

\divider
```

### Layout

- Exactly five choices, (A)-(E), exactly one correct (possibly a `Both`
  or `None` option).
- `\divider` between every pair of problems.
- Solution commentary in LaTeX comments only.
- Output raw `.tex` in a fenced code block. **Never render LaTeX.** Do
  not compile unless asked.
- When matrix choices are too wide for the `enumerate` layout, use the
  centered horizontal form:
  `(A) [matrix] \quad : \quad (B) [matrix] \quad : \quad (C) [matrix]`
  with a `\bigskip` after.
- For FSL problems, use `\choicefig` in a `\hfill`-separated row.

### Solutions guide

Organized by **week and topic**, not problem number, so it stays
version-agnostic across the five permuted versions. Correct answers are
highlighted **in blue within the choice list itself** (`\textcolor{blue}`),
never identified by letter — a student with Version C looks up the topic,
sees the correct choice's content in blue, and finds that content
wherever it sits in their version. Requires `\usepackage{xcolor}`.

Each entry: full problem text, choice list with the blue-highlighted
answer, conceptual explanation, then the labelled distractor analysis.

---

## 8. Tagging

Immediately after each `{\bf PROBLEM N:}` line:

```
% WEEK   = [number, comma-separated list, or "X, Y SYNTHESIS"]
% FORM   = [one code from §3]
% TOPICS = [precise comma-separated phrases, not vague headers]
% SOURCE = [week file section and item, e.g. "WEEK_6 CORE 4 / TRAPS 1"]
```

`SOURCE` is mandatory and does real work: it grounds each problem in
maintained course material rather than in this file, and makes
out-of-scope fabrication hard to write down — a citation to a line that
does not exist is visible on inspection.

`DIFFICULTY` is optional, useful when curating a pool:

- **Core** (~60%): standard application of a week's central concept.
- **Deeper** (~20%): a subtle structural fact, necessary versus
  sufficient, or what a result does *not* say.
- **Recall** (~10%): memory of a definition or theorem statement.
  Useful but limited; do not mistake these for conceptual.
- **Synthesis** (~10%): cross-week. Tag all weeks involved.

Synthesis hooks come from the `CONNECTIONS` sections, which label them
Back: and Forward: explicitly. Mine those rather than inventing links.

---

## 9. Workflow

### Phase 0 — Mine the week files

For each week in scope, in this order:

1. **`NOTE ON SCOPE`** first, if present. It says what the 2E changed.
   Everything downstream depends on it.
2. **`TYPICAL MCQ TRAPS`** second. This is the distractor inventory;
   reading it before drafting is what keeps distractors real and
   in-scope. Translate each into §2 notation as you go.
3. **`PERIPHERAL`** third — the exclusion list for this week.
4. **`CORE CONCEPTS`**, **`ESSENTIAL SKILLS`**, **`CONNECTIONS`** for
   hooks.

Then produce a **hook list**: one sentence per hook, each with a
`SOURCE` citation and a candidate `FORM`.

**Overproduce at least 3×.** For a week supplying ~11 problems, list
30+ hooks. The week files support this easily — they average about 45
addressable items each (roughly 30 core-concept bullets, 9 essential
skills, 8 traps). Without overproduction there is no selection pressure
and every hook ships, which is the mechanical cause of repetitive
Quizzams. Draw from all sections: a hook list more than half sourced
from `CORE CONCEPTS` means `ESSENTIAL SKILLS` and `CONNECTIONS` were
under-mined.

### Phase 1 — Distribution table

Propose for approval, before writing any LaTeX:

| Slot | Week(s) | Topic | FORM | Difficulty | SOURCE | Twin pair? | PC? | Notes |

Include a **rejected-hooks** list beneath it, so the selection is
visible. Wait for approval. The instructor revises surgically at this
stage; strategic consensus on coverage precedes drafting.

Starting targets for a 2-week Quizzam (~22 problems): ~10-12 on the more
recent week, ~8-10 on the prior week, 2-4 synthesis, 2-4 figure
problems, and the §3 form quotas satisfied.

### Phase 2 — Draft

Per problem: pick the hook and its FORM; write the stem; write the
correct answer as a bare expression; build four distractors from §4,
starting from the traps; check the §5 gate before assigning any partial
credit; verify arithmetic; check vocabulary against §2 for that week;
write the comment block; run §4's checklist.

Verify arithmetic before writing LaTeX. Eigenvalue computations,
determinant and trace consistency, FTLA dimension counts, and SVD sign
and ordering conventions are the error-prone spots. Use a scratch
computation rather than eyeballing.

### Phase 3 — Self-review and ledger

Fill in the ledger (§10) and check it against the quotas. Then confirm:
form quotas met; letter distribution balanced; partial-credit rate at or
under a third; at least one FTLA problem; figure budget met; nothing
from any `PERIPHERAL` list; no `\newpage`; every problem's `SOURCE`
resolves to a real line.

### Phase 4 — Output

Raw LaTeX in a fenced code block, ledger comment at the top. Never
render. Do not compile unless asked.

### Phase 5 — Permuted versions

Defer to `generate_quiz_versions.py`. This skill does not permute by
hand. Both problem order and choice order shuffle, so confirm §6's
permutation-safety rules hold before handing off.

---

## 10. Pre-output ledger

Emit this as a comment block at the top of the `.tex` file. It replaces
several prose prohibitions from earlier versions of this file: a
countable, visible tally is checkable at a glance, whereas a repeated
"do not fixate" is not.

```latex
% ===== QUIZZAM LEDGER =====
% FORMS:        DIM:2 CLS:3 MBT:2 HYP:2 WFM:3 IDO:2 INV:2 PRT:2 FSL:1 FRD:1 BND:2
%               -> 11 distinct, max 3. OK
% NEW FORMS vs previous Quizzam: BND, PRT  (need >=2). OK
% GUESS-RESISTANT (CEX/HYP/PRT/BND): 6  (need >=2). OK
% LETTERS:      A:4 B:5 C:4 D:4 E:5  (spread <=2). OK
% PARTIAL CREDIT: 6/22 = 27%  (target <=33%, <=1 per problem). OK
% FIGURES:      1 FRD, 1 FSL  (target 2-4). OK
% FTLA:         problems 3, 11, 19. OK
% HOOKS:        34 proposed, 22 used, 12 rejected  (>=3x). OK
% SOURCES:      all 22 cite a week-file line. OK
% PERIPHERAL:   none drawn on. OK
% ==========================
```

---

## 11. Acceptance criteria

A problem is ready when:

1. The hook is articulable in one sentence and carries a resolvable
   `SOURCE`.
2. The stem is 1-3 sentences with no method giveaway.
3. Options are bare (FUNDAMENTAL-DESCRIPTION excepted).
4. A twin pair or a correct-structure-wrong-detail distractor is
   engineered in, unless pure Recall.
5. At least one distractor traces to a `TYPICAL MCQ TRAPS` entry.
6. Every wrong option carries exactly one of the three §5 labels.
7. Any partial credit passes the two-insight gate and all three tests,
   with the verdicts written out.
8. `WEEK`, `FORM`, `TOPICS`, `SOURCE` are all present.
9. Arithmetic is verified.
10. Vocabulary matches the week per §2's row/column arc, and nothing is
    drawn from that week's `PERIPHERAL` list.
11. No hook is the headline of two problems in this Quizzam.
12. Form and letter tallies are updated in the ledger.
13. No `\newpage`; tall problems tagged.

Otherwise mark `% DRAFT -- needs [X]` and present for revision.

---

## 12. Repetition policy

The Quizzam corpus is large and growing. Cross-corpus novelty is no
longer achievable and is no longer a goal.

**Prohibited: wholesale reuse.** A stem with the same option set, or a
trivial rewording of one, lifted from a prior Quizzam. Also verbatim
reuse within a semester where students have the earlier Quizzam back.

**Explicitly acceptable: convergent problems.** Same topic, same form,
a similar hook, arrived at independently. Near-repeats are unavoidable
at this corpus size, and re-testing prior material — especially on the
final — is intentional and appropriate.

Consequences for the workflow:

- **No pre-draft search of prior Quizzams is required.** It costs a lot
  and now buys little. An optional single pass at curation time, to
  catch verbatim duplication only, if the instructor asks for it.
- Collision-checking is **within-batch only**: do not test the same hook
  twice in the same Quizzam. That is cheap and is the constraint that
  actually affects an assessment's quality.

The constraint is variety *within* an assessment, not novelty *across*
the corpus. Relaxing the cross-corpus check is safe because variety now
comes from the 98-entry trap inventory and the §3 form quotas rather
than from novelty policing.

---

## 13. Iteration

- Revise surgically. Identify exact problem numbers and parts; do not
  redraft batches unsolicited. Deliver corrections as targeted
  find/replace blocks.
- Re-read a revised problem against §11 before presenting.
- Most common pushback causes, in order — self-diagnose these first:
  method given away in the stem; distractors invented rather than drawn
  from the traps; missing twin pair; **partial credit awarded without
  passing the gate and the three tests**; vocabulary mismatched to the
  week; content drawn from a `PERIPHERAL` list or absent from the text
  entirely; the same hook headlining two problems in one batch;
  decorative rather than load-bearing figure.
- If reaching for the same hook twice in a batch, the cause is an
  under-mined source, not a styling problem. Return to Phase 0 and mine
  `ESSENTIAL SKILLS` and `CONNECTIONS` for that week.
- Pool growth is open-ended. Resist declaring coverage complete; propose
  a fresh candidate alongside any revision.
- Corrections arrive direct and precise. Adapt immediately, without
  defensiveness or excessive apology.

---

## Appendix A. Figure primitive library

Compose from these rather than inventing geometry. All are greyscale,
tick-free, and compile with the §7 preamble. Adapt coordinates and
labels; keep the style keys.

**A1. Projection and residual.** Weeks 5-6. Subject: best approximation,
orthogonality of the residual, which vector lies in `U^\perp`.

```latex
\begin{tikzpicture}[fig, scale=0.9]
  \draw[ghost,->] (-0.4,0) -- (4.2,0);
  \draw[ghost,->] (0,-0.4) -- (0,3.0);
  \draw[sub] (-0.3,-0.15) -- (4.0,2.0) node[lbl, right] {$U$};
  \draw[vec] (0,0) -- (1.6,2.4) node[lbl, above left] {$\mathbf{b}$};
  \draw[vec] (0,0) -- (2.6,1.3) node[lbl, below right] {$\Pi_U\mathbf{b}$};
  \draw[resid] (2.6,1.3) -- (1.6,2.4) node[lbl, midway, above right] {$\mathbf{r}$};
  \draw (2.6,1.3) ++(153:0.28) -- ++(-0.2,-0.1) -- ++(0.1,-0.24);
\end{tikzpicture}
```

**A2. Unit circle to ellipse.** Week 10. Subject: singular values as
axis lengths, right versus left singular vectors, which `\sigma` is
larger, rank from a degenerate ellipse.

```latex
\begin{tikzpicture}[fig, scale=0.75]
  \draw[ghost] (0,0) circle (1.2);
  \draw[vec] (0,0) -- (30:1.2) node[lbl,above right] {$\mathbf{v}_1$};
  \draw[vec] (0,0) -- (120:1.2) node[lbl,above left] {$\mathbf{v}_2$};
  \draw[->, line width=0.8pt] (2.0,0) -- (3.6,0) node[lbl, midway, above] {$A$};
  \begin{scope}[xshift=6.4cm, rotate=20]
    \draw[ghost] (0,0) ellipse (2.1 and 0.8);
    \draw[vec] (0,0) -- (2.1,0) node[lbl,right] {$\sigma_1\mathbf{u}_1$};
    \draw[vec] (0,0) -- (0,0.8) node[lbl,above] {$\sigma_2\mathbf{u}_2$};
  \end{scope}
\end{tikzpicture}
```

**A3. FTLA four-subspace diagram.** Weeks 3, 6, 10. Subject: which
subspace lives in which space, where the isomorphism acts, what the
pseudoinverse does on the cokernel.

```latex
\begin{tikzpicture}[fig, scale=0.9]
  \draw (0,0) rectangle (2.4,3.0);
  \draw (4.6,0) rectangle (7.0,3.0);
  \node[lbl, below] at (1.2,-0.1) {$V$};
  \node[lbl, below] at (5.8,-0.1) {$W$};
  \draw[dashed] (0,1.1) -- (2.4,1.1);
  \draw[dashed] (4.6,1.9) -- (7.0,1.9);
  \node[lbl] at (1.2,0.5) {$\ker T$};
  \node[lbl] at (1.2,2.0) {$(\ker T)^{\perp}$};
  \node[lbl] at (5.8,2.5) {$(\operatorname{im}T)^{\perp}$};
  \node[lbl] at (5.8,0.9) {$\operatorname{im}T$};
  \draw[->, line width=0.8pt] (2.5,2.0) -- (4.5,0.9);
  \draw[->, line width=0.8pt] (2.5,0.5) -- (4.5,0.25);
\end{tikzpicture}
```

**A4. Centered scatter with principal axes.** Week 11. Subject: which
direction is the first principal component, effect of centering,
covariance versus correlation PCA, what a near-circular cloud implies.

```latex
\begin{tikzpicture}[fig, scale=0.85]
  \draw[ghost,->] (-2.3,0) -- (2.3,0);
  \draw[ghost,->] (0,-1.7) -- (0,1.7);
  \foreach \p in {(-1.8,-0.9),(-1.3,-0.8),(-1.0,-0.3),(-0.6,-0.5),(-0.2,0.1),
                  (0.1,-0.2),(0.4,0.4),(0.9,0.3),(1.3,0.8),(1.7,0.9),(0.6,0.1),(-0.9,-0.6)}
    \fill \p circle (1.6pt);
  \draw[sub] (-2.1,-1.05) -- (2.1,1.05) node[lbl, right] {$\mathbf{w}_1$};
  \draw[sub, densely dashed] (-0.6,1.2) -- (0.6,-1.2) node[lbl, below] {$\mathbf{w}_2$};
\end{tikzpicture}
```

**A5. Iterated orbit.** Weeks 7, 9. Subject: convergence toward a
dominant eigendirection, what the drawn behaviour implies about
`|\lambda|` or `\rho(A)`, alternation under a negative eigenvalue.

```latex
\begin{tikzpicture}[fig, scale=0.9]
  \draw[ghost,->] (-0.3,0) -- (4.0,0);
  \draw[ghost,->] (0,-0.3) -- (0,2.6);
  \draw[sub, densely dotted] (0,0) -- (3.6,1.8);
  \foreach \pt/\lb in {(0.5,2.2)/{$\mathbf{x}_0$}, (1.3,1.6)/{$\mathbf{x}_1$},
                       (2.0,1.25)/{$\mathbf{x}_2$}, (2.6,1.35)/{$\mathbf{x}_3$}}
    \node[lbl, circle, fill=black, inner sep=1.4pt,
          label={[lbl]above right:\lb}] at \pt {};
\end{tikzpicture}
```

**A6. Markov transition digraph.** Week 9. Subject: reading a
column-stochastic matrix off a graph, which column sums to one,
reachability and the stationary distribution's support.

```latex
\begin{tikzpicture}[fig, every node/.style={draw, circle, minimum size=7mm, font=\footnotesize}]
  \node (1) at (0,0) {$1$};
  \node (2) at (2.4,0) {$2$};
  \node (3) at (1.2,-1.7) {$3$};
  \draw[->] (1) to[bend left=18] node[draw=none, lbl, above] {$0.6$} (2);
  \draw[->] (2) to[bend left=18] node[draw=none, lbl, right] {$0.5$} (3);
  \draw[->] (3) to[bend left=18] node[draw=none, lbl, left]  {$1.0$} (1);
  \draw[->] (2) to[bend left=18] node[draw=none, lbl, below] {$0.5$} (1);
\end{tikzpicture}
```

**A7. FSL choice row.** Any week. Each choice is a self-contained
picture, so the permutation script can shuffle atomically.

```latex
Which picture is consistent with the stated hypotheses?

\vspace{4pt}
\noindent
\choicefig{A}{\draw[ghost] (0,0) circle (1); \draw[sub] (-1.2,0)--(1.2,0);
              \draw[vec] (0,0)--(0.8,0.6);}\hfill
\choicefig{B}{\draw[ghost] (0,0) ellipse (1.3 and 0.5); \draw[sub] (-1.4,0)--(1.4,0);
              \draw[vec] (0,0)--(1.3,0);}\hfill
\choicefig{C}{\draw[ghost] (0,0) ellipse (0.5 and 1.3); \draw[sub] (0,-1.4)--(0,1.4);
              \draw[vec] (0,0)--(0,1.3);}\hfill
\choicefig{D}{\draw[ghost] (0,0) circle (1); \draw[sub] (-1.2,-1.2)--(1.2,1.2);
              \draw[vec] (0,0)--(0.7,0.7);}\hfill
\begin{minipage}[t]{0.18\textwidth}\centering
  (E)\\[2pt] \vspace{0.6cm} None of the above
\end{minipage}

\vspace{10pt}
```

The trailing `\vspace` matters: the tallest choice sets the row height,
and without it the following `\divider` can collide with a wrapped (E).

**A8. Additional primitives**, built on the same style keys when needed:
a basis lattice with a marked point and its coordinates (Week 4);
quadratic-form level curves with a constraint line (Weeks 6, 11); a
layered network graph with `\Psi` labelled on the edges (Week 13); a
probability simplex with a stochastic matrix's action drawn on it
(Weeks 9, 12).

---

## Appendix B. Special choice formats

### Subset format

Present three Roman-numeralled statements, then ask which have a given
property; subsets fill (A)-(E). Three items is the sweet spot; never
more than four.

```latex
Consider the following statements about ...:

I. [statement]

II. [statement]

III. [statement]

Which statements are true?

\begin{enumerate}[(A)]
\item I only
\item III only
\item I and II only
\item II and III only
\item All three
\end{enumerate}
```

Each item must be quick to check individually; the difficulty lies in
the classification, not in any one check. Every wrong subset must
correspond to a specific error.

**Balance the item frequencies.** Each of I, II, III should appear in
roughly the same number of the five offered subsets. If III appears in
four options and I in one, a student infers the answer without checking
anything — this is a live leak, not a theoretical one.

Avoid "how many of the following are true?" — it discards the
information about *which*, and with it any diagnostic value.

### `Both (X) and (Y)`

Use when two visible options are equivalent characterizations of the
same object via the FTLA, the spectral theorem, or another natural
isomorphism, and recognizing the equivalence is the question. Mark (X)
and (Y) individually as the paired partial credit (§5).

### `None of the above`

Correct only when all four visible options are independently plausible
and the true statement is genuinely absent. Wrong only when every
visible option is plausible enough that `None` is a real trap rather
than filler. Never a fifth-option afterthought.

---

## Appendix C. Anti-patterns

- A stem naming the theorem the student was supposed to recognize.
- A formula in the stem with the question "which formula is this."
- "because…" clauses inside answer choices.
- A distractor no reasonable student would pick — a five-choice problem
  functioning as a four-choice problem.
- Four wrong options wrong for four unrelated reasons.
- The same escape hatch in every problem.
- Absolute-language tells ("always," "only," "any") that let a student
  eliminate without understanding.
- Obvious twin pairs, where one member is visibly malformed.
- More than three stem sentences without a genuine need.
- A figure whose content fits in one stem sentence.
- A figure solvable by measuring.
- Spatial references to choices ("the left figure") under permutation.
- Content absent from the text, however true.
- Content drawn from a `PERIPHERAL` list.
- "A student says [X] — why is that incorrect?" Use direct framings.
- Asking for a generalized eigenvector or a vector's place in a Jordan
  chain. Jordan form is in scope as a *structural* object — block sizes
  from multiplicities, what it buys for powers and exponentials, its
  numerical caveat — but not as something to compute.
- `\newpage`, anywhere.
