# 命题陈述

记 $\mathbb N=\{0,1,2,\ldots\}$，并令

$$
A_n=\sum_{k=0}^{n}\binom nk\binom{n+2k}{2k}\binom{2k}{k}(-324)^{n-k},
\qquad b_n=\binom{2n}{n}A_n.
$$

以下列出本仓库研究的四项命题，不以本页替代证明。来源及版本范围见 [悬赏与版本说明](bounty-scope.md)。有理数同余中的分母均通过模数下的逆元解释。

## 1. 无穷级数

按照通常的级数求和意义，

$$
\sum_{n=0}^{\infty}\frac{357n+103}{2160^n}b_n=\frac{90}{\pi}.
$$

这是 [MathOverflow 原帖](https://mathoverflow.net/questions/369569/two-curious-series-for-1-pi) 的公式 (3)。主稿见 [级数证明](../proofs/proof-series.md)。

## 2. 无权九分支超同余

对素数 $p>7$，令

$$
S_p=\sum_{n=0}^{p-1}\frac{b_n}{2160^n},\qquad
\varepsilon_p=\left(\left(\frac{-1}{p}\right),\left(\frac p3\right),\left(\frac p5\right),\left(\frac p7\right)\right).
$$

括号中的符号为勒让德符号。若 $\varepsilon_p$ 属于下表，则该行的二次型表示存在；对任何满足表示的整数 $x,y$，有相应同余。

| $\varepsilon_p$ | 二次型表示 | $S_p\pmod{p^2}$ |
| --- | --- | --- |
| $(1,1,1,1)$ | $p=x^2+105y^2$ | $4x^2-2p$ |
| $(1,-1,-1,1)$ | $2p=x^2+105y^2$ | $2x^2-2p$ |
| $(-1,-1,-1,-1)$ | $p=3x^2+35y^2$ | $2p-12x^2$ |
| $(-1,1,1,-1)$ | $2p=3x^2+35y^2$ | $2p-6x^2$ |
| $(1,-1,1,-1)$ | $p=5x^2+21y^2$ | $20x^2-2p$ |
| $(1,1,-1,-1)$ | $2p=5x^2+21y^2$ | $10x^2-2p$ |
| $(-1,1,-1,1)$ | $p=7x^2+15y^2$ | $28x^2-2p$ |
| $(-1,-1,1,1)$ | $2p=7x^2+15y^2$ | $14x^2-2p$ |

若 $\left(\frac{-105}{p}\right)=-1$，则

$$
S_p\equiv0\pmod{p^2}.
$$

由二次互反律，

$$
\left(\frac{-105}{p}\right)
=\left(\frac{-1}{p}\right)\left(\frac p3\right)\left(\frac p5\right)\left(\frac p7\right).
$$

表中八行覆盖乘积为 $1$ 的组合，最后一个分支覆盖乘积为 $-1$ 的组合。主稿见 [九分支证明](../proofs/nine-branches-proof.md)。

## 3. 加权超同余

对每个素数 $p>5$，

$$
W_p:=\sum_{n=0}^{p-1}(357n+103)\frac{b_n}{2160^n}
\equiv54p\left(\frac{-1}{p}\right)+49p\left(\frac{15}{p}\right)\pmod{p^2}.
$$

这也可写作

$$
W_p\equiv p\left(\frac{-1}{p}\right)
\left[54+49\left(\frac p3\right)\left(\frac p5\right)\right]\pmod{p^2}.
$$

主稿见 [加权证明](../proofs/weighted-wronskian-proof.md)。

## 4. 整数整除性

对每个整数 $n\ge1$，

$$
n\binom{2n-1}{n-1}\;\bigg|\;
T_n:=\sum_{k=0}^{n-1}(357k+103)2160^{n-1-k}b_k.
$$

主稿见 [整除证明](../proofs/divisibility-proof.md)。

## 版本关系

第 2—4 项合起来对应已核对的 2019 年猜想 39 及其 105 美元历史悬赏范围；第 1 项对应另一笔 90 美元历史悬赏。仓库没有取得 2021 年著作中相应页的全文，因而不将两版各小项的编号强行一一对应。
