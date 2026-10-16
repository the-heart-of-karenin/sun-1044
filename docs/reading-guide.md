# 阅读顺序与前置知识

先读 [题面](problem-statement.md)，再按下表顺序阅读。主稿以外的文件是引理笔记或计算附件，不必一次全部读完。

| 次序 | 主稿 | 主要依赖 |
| --- | --- | --- |
| 1 | [级数](../proofs/proof-series.md) | 生成函数与偏微分方程；30 级模参数化；七次模方程与复乘特殊值 |
| 2 | [九分支](../proofs/nine-branches-proof.md) | 有限截断二次同余；Hasse 不变量；Hecke 乘积；二次型分类 |
| 3 | [加权](../proofs/weighted-wronskian-proof.md) | 九分支中的全曲线比较；横向导数项；七次对应的 Wronskian |
| 4 | [整除性](../proofs/divisibility-proof.md) | 整数坐标变换；形式 Brauer 对数；普通与超特殊 K3 的局部论证 |

## 1. 级数的辅助文件

- [解析约化](../lemmas/analytic-reduction.md)：内层生成函数、绝对收敛性、四阶微分方程及常数项表示。
- [两个二阶解的乘积分解](../lemmas/product-decomposition.md)：此前获得的另一种约化，不代替主稿中的特殊值计算。
- [参数曲线与截面](../lemmas/section-locus.md)：通向主稿参数曲线的几何线索。
- 代数计算：[nl-certificate.py](../scripts/nl-certificate.py)、[bivariate-period.py](../scripts/bivariate-period.py)。
- 模方程与复乘计算：[modular7-certificate.py](../scripts/modular7-certificate.py)、[cm-certificate.py](../scripts/cm-certificate.py)、[多项式数据](../data/modular7-polynomial.txt)。

## 2. 九分支的辅助文件

- [常数项模型](../lemmas/toric-period.md)、[有限和约化](../lemmas/finite-sum-reduction.md)。
- [Hasse 不变量](../lemmas/hasse-invariant.md)。
- [有限截断二次恒等式](../lemmas/finite-isotropy.md)、[全曲线二次同余](../lemmas/global-isotropy.md)。后者处理了早期点上消元出现的例外。
- [二次型的存在性与选择无关性](../lemmas/quadratic-forms.md)、[八个复乘因子](../lemmas/cm-eight-branches.md)。后一文件末尾的“尚缺比较”记录的是早期状态；比较论证位于九分支主稿。
- 代数计算：[generic-product-certificate.py](../scripts/generic-product-certificate.py)、[curve-isotropy-certificate.py](../scripts/curve-isotropy-certificate.py)。

## 3. 加权问题的辅助文件

- [横向项的模 $p^2$ 求值](../lemmas/transverse-congruence.md)。
- [Wronskian 计算附件](../scripts/weighted-wronskian-certificate.py)。
- [此前的普通分支笔记](../archive/weighted-ordinary-proof.md) 只用于比较早期路径，阅读主稿无需先读它。

## 4. 整除性的辅助文件

1. [奇数分母约化](../lemmas/divisibility-reduction.md)：把有限和整除性转成 $(2n+1)\mid R_n$，并处理 $3$ 进部分。
2. [形式 Brauer 对数约化](../lemmas/divisibility-brauer-reduction.md)：将整除性转成准对数 $J$ 的整性。该笔记还保留一条未完成的早期 CM 对应路线，主稿不依赖那条路线。
3. [加权导数组合的除子类识别](../lemmas/divisibility-tate-class.md)。
4. [普通素数处的整性引理](../lemmas/divisibility-ordinary-lemma.md)。
5. [惰性素数的全部幂次](../lemmas/divisibility-inert-powers.md)：截面格、Artin 不变量与一阶变形。
6. [全部 $5$ 进部分](../lemmas/divisibility-five-adic.md)、[全部 $7$ 进与 $17$ 进部分](../lemmas/divisibility-seven-seventeen.md)。

对应代数附件以 `divisibility-` 开头，见 [程序目录](../scripts/README.md)。

## 所需背景

读懂级数主稿，需要熟悉形式幂级数、超几何函数、线性微分方程、模形式与模函数、$q$ 展开和复乘。研究生阶段的复分析与数论背景可以作为起点；模形式的具体定理可随文补充。

九分支与加权主稿进一步使用 $p$ 进整性、模曲线、Hasse 不变量、Hecke 算子、椭圆曲线的普通与超奇异约化，以及二元二次型。

整除性证明所需背景最深：代数曲面、椭圆纤维化、Picard 格与截面高度、K3 的 Hodge 理论和格极化模空间，以及形式群、形式 Brauer 群、晶体上同调、Dieudonné 理论与变形理论。逐步独立审阅这一部分，通常需要算术代数几何博士阶段并进一步接触过 K3 曲面与 $p$ 进上同调的训练。

若只希望理解证明结构，可以先把文中列出的标准几何定理作为已知结果接受。代数计算附件能帮助核对公式，不能代替这些定理及其适用条件。
