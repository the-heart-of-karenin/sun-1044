> 辅助研究笔记。个别段落保留早期进度描述；本文的用途及后续主稿见 [阅读顺序](../docs/reading-guide.md)。

# 截断和：已证的模 p 约化与模 p² 修正项

2026-10-15。这里的公式均可直接证明，但不包含原猜想的九分支求值。

记
$$
T_p(t,z)=\sum_{n=0}^{p-1}\binom{2n}n A_n(t)z^n,
\qquad h=(p-1)/2,
$$
其中 $t,z$ 是分母不被奇素数 $p$ 整除的有理数。本题 $S_p=T_p(-324,1/2160)$。

## 1. 一个单一多项式系数给出模 p 的值

令
$$
P_{t,z}(x,y)=xy(1-x-y)\big(xy(1-x-y-4tz)-4z\big).
$$
则
$$
\boxed{T_p(t,z)\equiv[x^{p-1}y^{p-1}]P_{t,z}(x,y)^h\pmod p.}
$$

### 证明

对 $0\le n\le h$，有
$\binom{2n}n\equiv(-4)^n\binom hn\pmod p$；对 $h<n<p$，有 $p\mid\binom{2n}n$。

令
$$
D=(1-x-y)(1-x-y-4tz-4z/(xy))=P_{t,z}/(xy)^2.
$$
展开 $D^h$ 得
$$
D^h=\sum_{n=0}^h\binom hn(-4z)^n(t+1/(xy))^n(1-x-y)^{p-1-n}.
$$
在模 $p$ 的形式幂级数环中，
$$
(1-x-y)^{p-1-n}
\equiv\frac{1-x^p-y^p}{(1-x-y)^{n+1}}.
$$
因 $n<p$，$(t+1/(xy))^n$ 的负指数在每个变量中都不小于 $-n>-p$。故分子中的 $-x^p$、$-y^p$ 两项不贡献常数项。于是
$$
\operatorname{CT}D^h
\equiv\sum_{n=0}^h\binom hn(-4z)^n
\operatorname{CT}\frac{(t+1/(xy))^n}{(1-x-y)^{n+1}}
=\sum_{n=0}^h\binom hn(-4z)^n A_n(t).
$$
又 $\operatorname{CT}D^h=[x^{2h}y^{2h}]P_{t,z}^h$，即得结论。

### 本题的整系数形式

定义固定的整系数六次多项式
$$
\mathcal P(x,y)=xy(1-x-y)\big(xy(864-540x-540y)-1\big).
$$
它等于 $540P_{-324,1/2160}$。Euler 判别准则给出 $540^h\equiv(15/p)\pmod p$，所以对所有素数 $p>7$，
$$
\boxed{S_p\equiv\left(\frac{15}{p}\right)
[x^{p-1}y^{p-1}]\mathcal P(x,y)^{(p-1)/2}\pmod p.}
$$
这为原双重和提供了一个统一的模 $p$ 系数提取问题。尚未由它推出九分支的模 $p$ 值，更没有因此得到模 $p^2$ 的值。

## 2. 模 p² 时不能丢掉后半段

令
$$
O_n=\sum_{j=0}^{n-1}\frac1{2j+1},\qquad O_0=0.
$$
对 $0\le n\le h$，有
$$
\binom{2n}n
\equiv(-4)^n\binom hn(1+pO_n)\pmod{p^2}.
$$
这是因为恒等式
$$
(-4)^n\binom hn=\binom{2n}n\prod_{j=0}^{n-1}\left(1-\frac p{2j+1}\right)
$$
可在模 $p^2$ 展开并求逆。

对 $h<n<p$，则有
$$
\binom{2n}n\equiv\frac{2p}{n\binom{2(p-n)}{p-n}}\pmod{p^2}.
$$
证明：置 $m=p-n\le h$，用 Wilson 定理和阶乘反射，得到
$$
\frac1p\binom{2n}n
\equiv-\frac{(m-1)!^2}{(2m-1)!}
=-\frac2{m\binom{2m}m}
\equiv\frac2{n\binom{2(p-n)}{p-n}}\pmod p.
$$

因此保留全部精度的公式为
$$
\boxed{\begin{aligned}
T_p(t,z)\equiv{}&\sum_{n=0}^{h}(-4z)^n\binom hn A_n(t)(1+pO_n)\\
&+2p\sum_{n=h+1}^{p-1}\frac{A_n(t)z^n}{n\binom{2(p-n)}{p-n}}
\pmod{p^2}.
\end{aligned}}
$$
其中后半段只需知道 $A_n(t)\pmod p$，但一般不能将它删去。

例如本题参数下的短时核验给出：

| p | 前半段 $0\le n\le h$ | 后半段 $h<n<p$ | 完整和（模 $p^2$） |
|---|---:|---:|---:|
| 11 | 69 | 44 | 113 |
| 17 | 238 | 51 | 0 |
| 19 | 336 | 57 | 32 |

特别地，$p=17$ 的零值来自两段相消；仅凭中央二项式系数在后半段被 $p$ 整除，不能证明模 $p^2$ 的消失。

## 3. 双重和中可直接删去的区域

对整数 $t$ 且 $p\nmid t$，原双重和的第 $(n,k)$ 项含有阶乘比
$$
\frac{(2n)!(n+2k)!}{n!^2(n-k)!k!^3}t^{n-k}z^n.
$$
当 $0\le k\le n<p$ 时，它的 $p$-进赋值为
$$
\left\lfloor\frac{2n}{p}\right\rfloor+
\left\lfloor\frac{n+2k}{p}\right\rfloor
$$
（若 $z$ 被 $p$ 整除，另计其非负赋值即可；本题 $z$ 为单位）。所以模 $p^2$ 只需保留下述三种区域：

1. $n\le h,\ n+2k<p$：赋值零；
2. $n\le h,\ p\le n+2k<2p$：赋值一；
3. $n>h,\ n+2k<p$：赋值一。

其余项都被 $p^2$ 整除。此结论只用于控制有限变换的精度，不是猜想的求值。
