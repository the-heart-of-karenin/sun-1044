> 辅助研究笔记。个别段落保留早期进度描述；本文的用途及后续主稿见 [阅读顺序](../docs/reading-guide.md)。

# 第一题的新约化：完整生成函数是两个二阶方程的特定解之积

2026-10-15，第二轮研究。以下给出已由算子恒等式验证的分解；它尚不是 $90/\pi$ 的特殊值证明，也不预先断言两个因子就是普通椭圆积分。

后续进展：第一题已通过另一条参数曲线接到 30 级模函数，完整证明草稿见 [proof-series.md](../proofs/proof-series.md)。本文件保留此前的固定参数二阶乘积分解。

## 1. 分解公式

改用 $x=108z$，令
$$
\Phi(x)=F_{-324}(x/108),\qquad x_0=1/20.
$$
定义
$$
\begin{aligned}
C(x)&=(1+12x)^3-x=(1+8x)(1+27x+216x^2),\\
B(x)&=1-24x,\qquad A(x)=1+30x,\\
N(x)&=3359232x^4-46656x^3-52200x^2-1419x+53,
\end{aligned}
$$
以及
$$
\begin{aligned}
a(x)&=\frac1x+\frac{C'(x)}{2C(x)}+\frac{12}{B(x)},\\
b(x)&=\frac{N(x)}{18xB(x)^2C(x)},\\
d(x)&=\frac{4\sqrt{30}}{3}\frac{A(x)}{xB(x)^2\sqrt{C(x)}}.
\end{aligned}
$$
在原点取 $\sqrt{C(0)}=1$。分别令 $f_+$、$f_-$ 为以下方程在原点的唯一解析解，归一化为 $f_\pm(0)=1$：
$$
\boxed{f_\pm''+a(x)f_\pm'+\big(b(x)\pm d(x)\big)f_\pm=0.}
$$
它们的一阶导数由方程确定：
$$
f_\pm'(0)=-\frac{53}{18}\mp\frac{4\sqrt{30}}3.
$$
则在原点邻域有严格恒等式
$$
\boxed{\Phi(x)=f_+(x)f_-(x).}
$$

## 2. 证明方式

若 $u,v$ 分别满足上述正号和负号方程，令
$$
Y=uv,\quad V=u'v+uv',\quad W=u'v',\quad R=u'v-uv'.
$$
直接微分可得
$$
\begin{pmatrix}Y\\V\\W\\R\end{pmatrix}'
=\begin{pmatrix}
0&1&0&0\\
-2b&-a&2&0\\
0&-b&-2a&d\\
-2d&0&0&-a
\end{pmatrix}
\begin{pmatrix}Y\\V\\W\\R\end{pmatrix}.
$$
消去后三个量即得四阶方程。它只涉及 $a,b,d^2,d'/d$，后两者为有理函数，因此可用纯有理代数核验。

具体地，令
$$
\beta=b-\frac12a'-\frac14a^2,\qquad H=-d'/d.
$$
把两个二阶方程去掉一阶导数后，其乘积的算子为
$$
\mathcal M=D^4+HD^3+4\beta D^2+(4H\beta+6\beta')D
+2H\beta'+4d^2+2\beta'',\quad D=d/dx.
$$
由于原乘积 $Y=e^{-\int a}\widetilde Y$，对 $\mathcal M$ 作非交换代入 $D\mapsto D+a$，恰好得到第一轮已经证明的四阶方程（改为变量 $x$，并使最高阶系数为一）。

此处是各阶系数相等的恒等式，不是有限 Taylor 系数拟合；计算附件为 [product-certificate.py](../scripts/product-certificate.py)。首次完整直接展开约用 12.3 秒；后续宜使用归一化后的较短核验式，不重复该展开。

还需匹配具体的解。由正则奇点级数递推，$f_\pm(0)=1$ 唯一确定原点解析解，而且
$$
(f_+f_-)(0)=1,\qquad (f_+f_-)'(0)=-53/9.
$$
这与 $\Phi(0)=1$、$\Phi'(0)=2(-324+6)/108=-53/9$ 相同。原四阶方程在 $x=0$ 的指标多项式为 $h^3(h-1)$，对每个 $n\ge2$ 相应递推的最高系数非零；故两个初始系数已经唯一确定解析解。分解公式因此成立。

## 3. 分支与原题特殊点

两个二阶方程在 $x=1/24$ 有奇点，而完整生成函数在此处解析。这个点位于原点到 $x_0=1/20$ 的实线段上。因此不能将各因子分别用原点 Taylor 级数直接代入 $x_0$，也不能随意独立选择分支。

分解恒等式可沿共同路径解析延拓；可先在上半平面绕过 $1/24$，然后取 $x\to1/20$ 的极限。乘积及其导数由 $\Phi$ 的解析延拓唯一确定。

在 $x=1/24$ 附近，取由原点延拓来的 $\sqrt C$，两因子的局部指数分别为
$$
f_+:\ \{1/4,5/4\},\qquad
f_-:\ \{-1/4,7/4\}.
$$
这些局部指数也说明，分别观察因子时会出现原级数中不存在的分支行为。

原题特殊点有
$$
B(x_0)=-1/5,\qquad A(x_0)=5/2,\qquad
C(x_0)=2023/500,\qquad \sqrt{C(x_0)}=17\sqrt{35}/50.
$$

## 4. 现在的目标

第一题已化为证明
$$
\boxed{\left[357x\big(f_+'f_-+f_+f_-'\big)+103f_+f_-\right]_{x=1/20}=\frac{90}{\pi}.}
$$
尚缺少把这些二阶解与可求值的周期联系起来，以及证明此处的特殊值／导数关系。

方法参考：M. van Hoeij, *Decomposing a 4th order linear differential equation as a symmetric product*, Banach Center Publications 58 (2002), 89–96：
<https://www.impan.pl/en/publishing-house/banach-center-publications/all/58/0/85805/decomposing-a-4th-order-linear-differential-equation-as-a-symmetric-product>。
这里只借助其分解思路；本文件的具体方程及初值已按本题单独验证。不对该具体分解的文献新颖性作判断。
