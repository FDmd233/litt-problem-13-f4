# A Realization of F4 for Litt Problem No. 13

This repository contains a construction of a complex abelian fourfold and an integral surface whose full convolution Tannaka pair is $(F_4,V_{26})$.

The construction applies to every smooth cubic threefold with a marked Eckardt point. It quotients the Albanese variety of its Fano surface by the elliptic curve of lines through that point. The quotient surface has characteristic cycle $\Lambda_X+2\Lambda_0$, conormal Gauss degree $24$, and generic twisted Hodge multiplicities $(6,14,6)$. The ambient fourfolds form a seven-dimensional polarized family of type $(1,2,2,2)$.

Authoritative source revised October 21, 2026. The corrected PDF and SHA-256 checksums were rebuilt from that source in GitHub Actions.

## Manuscript

- [PDF](output/pdf/Litt_Problem_13_F4.pdf)
- [Complete LaTeX source](Litt_Problem_13_F4.tex)

## Computational verification

The [exact Albert Hessian audit](verification/verify_albert_hessian.py) verifies, independently of the manuscript's quoted ranks, that the norm-cubic Hessians at the diagonal Albert rank-one and rank-two representatives have ranks 10 and 18 (kernel dimensions 17 and 9). It uses the fact that the octonionic trilinear term has zero Hessian at diagonal points, so a nondegenerate 8-dimensional quadratic model suffices. The [GitHub Actions check](.github/workflows/verify-albert-hessian.yml) reproduces these exact ranks.

This validates one key algebraic lemma, **not** the Fano geometry, the full Tannakian reduction, or the external classification of irreducible subgroups of F4.

## Build

~~~bash
make
~~~

This writes the PDF to `output/pdf/Litt_Problem_13_F4.pdf` and the PDF and TeX checksums to `SHA256SUMS.txt`.

## Publication record

- [Current corrected release: v2.1.0](https://github.com/FDmd233/litt-problem-13-f4/releases/tag/v2.1.0) — snapshot PDF, complete LaTeX source, and portable SHA-256 checksums.
- [Previous release: v2.0.0](https://github.com/FDmd233/litt-problem-13-f4/releases/tag/v2.0.0).
- [First release: v1.0.0-preprint](https://github.com/FDmd233/litt-problem-13-f4/releases/tag/v1.0.0-preprint).

The `main`-branch PDF is continuously updated; release tags remain fixed snapshots for version tracking.

## Authorship and assistance

The manuscript is signed OpenAI. OpenAI GPT-5.6 Sol was used during parts of the earlier drafting and checking process. OpenAI ChatGPT/Codex was used for the present revision, examination of the arguments and references, and LaTeX checks. This statement records assistance and does not imply journal review or acceptance.


## Proof correction and verification scope

The revised proof states and proves a restricted tensor pushforward lemma
for the semismall quotient construction. The previously overbroad functor
claim is no longer used. The committed PDF is rebuilt from the corrected
TeX source by [the build workflow](.github/workflows/build-audited-pdf.yml),
which checks compilation, references, manuscript hygiene, and checksums.

These checks support reproducibility. They are not a substitute for
independent mathematical peer review of the full proof.
