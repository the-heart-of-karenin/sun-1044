> 辅助研究笔记。个别段落保留早期进度描述；本文的用途及后续主稿见 [阅读顺序](../docs/reading-guide.md)。

# 显式截面与通往 30 级周期的参数曲线

2026-10-15。以下是代数恒等式，不预先使用尚未完成的 Picard 格识别。

在 [geometric-exploration.md](../archive/geometric-exploration.md) 的椭圆纤维模型中，写
$$
Y^2=X^3+(3-2c)X^2+(3-c)(q-c+1)X+(q-c+1)^2,
\quad q=b_0(s+1)^2/s.
$$
置 $d=4b_0$。取参数
$$
c=\frac{1+2r}{1-r^2},\qquad
d=-\frac{r^4}{(r-1)^3(r+1)}.
$$
令 $e=c-1$，则
$$
X=(q-e)\left(\frac{r^2q}{d}-1\right),\qquad
Y=\frac{(q-e)(r^3q-d)}{d^{3/2}}\sqrt{q(q-d)}
$$
满足纤维方程。由于
$\sqrt{q(q-d)}=b_0(s^2-1)/s$，这是在加入常数 $\sqrt d$ 后的有理截面。

证明只需代入：除去 $q(q-e)^2$ 后，余式由以下两个系数组成：
$$
-\frac{r^3}{d^3}\big((c-1)r^3-d(r^3-3r+2)\big),\qquad
\frac{cr^4-d(2r^3-3r^2+1)}{d^2}.
$$
上述 $c,d$ 使它们同时为零。

在 $r=1/4$，$c=8/5$、$d=1/135$、$b_0=1/540$，并可写为
$$
X=\frac{(5q-3)(135q-16)}{80},\qquad
Y=\frac{3\sqrt{15}(5q-3)(135q-64)}{320}
\frac{s^2-1}{540s}.
$$
这一特殊点正对应原题。

对解析生成函数，参数对应关系是
$$
a=(1-c)/4=-\frac{r(r+2)}{4(1-r^2)},\qquad
b=d/16=-\frac{r^4}{16(r-1)^3(r+1)}.
$$
沿这条曲线的周期及其导数关系已由偏微分方程独立证明，见 [proof-series.md](../proofs/proof-series.md)。因此第一题的证明不需要先证明截面的高度、原始性、Picard 数或格判别式。上述几何问题仍可作为研究第二题的线索。
