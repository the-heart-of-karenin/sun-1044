# 一个 $90/\pi$ 级数的证明草稿

本稿将原级数约化到 30 级模函数，并计算所需的复乘特殊值。初稿日期为 2026-10-15；审阅状态与 AI 参与情况见 [项目说明](../README.md)。相关超同余由另外的主稿讨论。

## 1. 双变量函数及收敛

定义
$$
\mathcal F(a,b)=\sum_{m,k\ge0}
\frac{(2m+2k)!(m+3k)!}{(m+k)!^2m!k!^3}\,a^m b^k.
$$
于是题中的生成函数为
$$
F(z)=\mathcal F(-324z,z).
$$
记 $\vartheta_a=a\partial_a$、$\vartheta_b=b\partial_b$。待证数为
$$
\left[357(a\mathcal F_a+b\mathcal F_b)+103\mathcal F\right]_
{a=-3/20,\ b=1/2160}.
\tag{1}
$$

[analytic-reduction.md](../lemmas/analytic-reduction.md) 中的非负系数比较证明原级数绝对收敛，并且在 $(|a|,|b|)=(3/20,1/2160)$ 附近仍有收敛余量。因此本文件中的重排、有限次求导和以下实参数路径上的延拓均合法。

## 2. 两条已证偏微分方程

逐项比较系数得到
$$
\left\{\vartheta_a(\vartheta_a+\vartheta_b)
-2a(2\vartheta_a+2\vartheta_b+1)
(\vartheta_a+3\vartheta_b+1)\right\}\mathcal F=0,
\tag{2}
$$
以及
$$
\begin{aligned}
0={}&\big\{2a(2a+1)+6(2a^2+a+6b)\vartheta_a
+2a(4a+5)\vartheta_b\\
&\quad +(8a^2+2a+36b-1)\vartheta_a^2
+(8a^2+20a+108b-1)\vartheta_a\vartheta_b\big\}\mathcal F.
\end{aligned}
\tag{3}
$$
这里含参数的系数均放在微分算子左侧。

证明可直接使用系数
$c_{m,k}=(2m+2k)!(m+3k)!/((m+k)!^2m!k!^3)$
的相邻项比。例如
$$
\frac{c_{m-1,k}}{c_{m,k}}
=\frac{m(m+k)}{2(2m+2k-1)(m+3k)}.
$$
第二条只涉及向前移动 $(1,0),(2,0),(0,1)$ 的项，代入相邻比后是零有理函数。边界 $m=0$ 的各项均为零；$k=0$ 退化为中央二项式系数的递推；余下边界 $m=1,k>0$ 可直接代入。通用有理恒等式保存在 [bivariate-period.py](../scripts/bivariate-period.py)。

## 3. 一条参数曲线与一阶导数关系

置
$$
a(r)=-\frac{r(r+2)}{4(1-r^2)},\qquad
b(r)=-\frac{r^4}{16(r-1)^3(r+1)},\qquad
H(r)=\mathcal F(a(r),b(r)).
\tag{4}
$$
当 $0\le r\le1/4$ 时，$|a(r)|,b(r)$ 分别递增至 $3/20,1/2160$，故这条路径处于同一绝对收敛区域。

定义
$$
\begin{aligned}
R_0&=-16(r-2)(r-1)^3(r+1),\\
R_1&=-4(r-1)^2(r+2)(3r^2-2r-2),\\
R_2&=r^3(3r^2-8r+2).
\end{aligned}
$$
则沿 (4) 有
$$
\boxed{R_0\mathcal F+R_1\mathcal F_a+R_2\mathcal F_b=0.}
\tag{5}
$$

以下给出能用纯有理代数逐项检查的证明，避免将有限个系数吻合当成证明。令
$$
J=8a^2+2a+36b-1,\quad K=8a^2+20a+108b-1,
\quad V=(\mathcal F,\mathcal F_a,\mathcal F_b,\mathcal F_{ab})^{\!t}.
$$
由 (2)、(3)，$\mathcal F_{aa}=uV$、$\mathcal F_{bb}=vV$，其中行向量
$$
\begin{aligned}
u&=\frac{1}{aJ}\big(-2(2a+1),\,-20a^2-8a-72b+1,\,-2b(4a+5),\,-bK\big),\\
v&=\frac{a(1-4a)u+(-2,1-10a,-22b,b(1-16a))}{12b^2}.
\end{aligned}
\tag{6}
$$
把 (4) 代入，直接展开给出
$$
\frac{d}{dr}(R_0\mathcal F+R_1\mathcal F_a+R_2\mathcal F_b)
=\frac{5r^2+3r+1}{r(r-1)(r+1)}
(R_0\mathcal F+R_1\mathcal F_a+R_2\mathcal F_b).
\tag{7}
$$
验证时只需使用 (6)，不涉及第三阶偏导数。(7) 右侧系数在零点的留数为 $-1$；非零局部解必有一阶极点，而左侧括号内的函数在原点解析。故它恒为零，证明 (5)。

## 4. 与已知 30 级周期的变换

令
$$
G(X)=(1+5X)(1+4X)(1+X)(1-4X),\qquad
Q(X)=-4X(1-4X-58X^2-75X^3).
$$
定义 $y(X)$ 为以下方程的原点解析解，$y(0)=1$：
$$
y''+\left(\frac1X+\frac{G'}{2G}\right)y'
-\frac{Q}{4X^2G}y=0,\qquad Z(X)=y(X)^2.
\tag{8}
$$
所需的函数恒等式是
$$
\boxed{H(r)=\frac{1-r}{1+r}\,
Z\!\left(-\frac{r}{2(1+r)}\right).}
\tag{9}
$$

为证明 (9)，定义
$$
\begin{aligned}
\alpha(r)&=\frac{2(9r^4-19r^2+5r+2)}
{r(r-1)(r+2)(3r-2)(3r+1)},\\
\beta(r)&=\frac{29r^4+71r^3+12r^2-8r-8}
{4r(r-1)^2(r+1)^2(r+2)(3r-2)(3r+1)}.
\end{aligned}
$$
由 (2)、(3)、(5) 消元可得
$$
H'''+3\alpha H''+(\alpha'+4\beta+2\alpha^2)H'
+(2\beta'+4\alpha\beta)H=0.
\tag{10}
$$
其原点指标为 $h^3$，故 $H(0)=1$ 唯一确定原点解析解。

这里的消元也有一个较短的完整计算附件：由 (6) 对 $b,a$ 分别求导，解两条线性方程，得到 $\mathcal F_{aab}$、$\mathcal F_{abb}$。沿 (4) 对 $V$ 构造四维一阶系统，再把 (10) 的左侧化为行向量乘 $V$；所得行向量恰为 $(R_0,R_1,R_2,0)$ 的有理函数倍数。因此由 (5) 为零。各操作与恒等式均见 [nl-certificate.py](../scripts/nl-certificate.py)，不依赖有限 Taylor 系数检验，运算约 0.3 秒。

另一方面，对 (8) 作换元
$X=-r/(2(1+r))$，再乘上 $\sqrt{(1-r)/(1+r)}$，其二阶方程恰为
$f''+\alpha f'+\beta f=0$。故 (9) 右侧也满足 (10)，且常数项为一，证明 (9)。在 $[0,1/4]$ 上无其他奇点，两边延拓一致。

## 5. 使用的标准模函数资料

仅需要下列已知的 30 级模参数化。记 $q=e^{2\pi i\tau}$、$D=q\,d/dq$、$\eta_d=\eta(d\tau)$，置
$$
R(\tau)=\frac{\eta_1\eta_2\eta_{15}\eta_{30}}
{\eta_3\eta_5\eta_6\eta_{10}},\qquad
T(\tau)=R+R^{-1}-2,\quad X(\tau)=T(\tau)^{-1}.
\tag{11}
$$
则 $T$ 是 $\Gamma=\Gamma_0(30)^+$ 的 Hauptmodul，在唯一尖点有一个一阶极点，且
$$
T=q^{-1}-1+4q+2q^2+6q^3+\cdots,
\qquad DX=X\sqrt{G(X)}\,Z(X).
\tag{12}
$$
这里 $Z$ 正是 (8) 的归一化解析函数；平方根取原点值一。

这些标准资料可见 Campbell–Cooper–Ye，*Quadratic irrational analogues of Ramanujan's series for 1/pi*，arXiv:2602.09352v1，定理 2.1–2.2、式 (3.2)–(3.3) 取 $c=-2$：
<https://arxiv.org/html/2602.09352v1>。
该文表 39 也直接列出下一节所需的 $N=7$ 数据；为使本证明不依赖表格中特殊值的省略计算，下面另给模方程证明。

## 6. 独立核验所需复乘特殊值

令
$$
\tau_0=\frac{15+i\sqrt{105}}{30},\qquad
y_0=\operatorname{Im}\tau_0=\frac{\sqrt{105}}{30}.
$$
下面证明
$$
\boxed{X(\tau_0)=-\frac1{10},\qquad
\left[(X\partial_X+4/21)Z(X)\right]_{X=-1/10}
=\frac{50}{21\pi}.}
\tag{13}
$$

### 6.1 模方程及其证明界

令 $P(T,U)$ 为 [modular7-polynomial.txt](../data/modular7-polynomial.txt) 中的对称整数多项式。它的每个变量次数至多 8，并有
$$
P(T(\tau),T(7\tau))=0.
\tag{14}
$$
这是严格的模函数恒等式，证明如下。令 $\Gamma'$ 为 $\Gamma_0(210)$ 加入所有 $W_e$（$e\mid30$）的扩张。其在 $\Gamma$ 中的指数为 8；$\operatorname{diag}(7,1)\Gamma'\operatorname{diag}(7,1)^{-1}$ 同样包含于 $\Gamma$，指数也是 8。这可直接从 Atkin–Lehner 矩阵
$\bigl(\begin{smallmatrix}ea&b\\210c&ed\end{smallmatrix}\bigr)$
经共轭变为
$\bigl(\begin{smallmatrix}ea&7b\\30c&ed\end{smallmatrix}\bigr)$
看出。

故 $T(\tau),T(7\tau)$ 在 $X(\Gamma')$ 上的极点除子次数各为 8。$P$ 的极点总次数至多 $8\cdot8+8\cdot8=128$。从 (11) 的整数乘积直接展开，(14) 左侧在无穷尖点的系数从 $q^{-64}$ 至 $q^{129}$ 全部为零；故其零点阶数至少 130，大于极点总次数，只能恒为零。生成与核验见 [modular7-certificate.py](../scripts/modular7-certificate.py)，约 0.6 秒。这里有限展开成为证明，是因为已经给出先验极点界。

所需的对角分解为
$$
\begin{aligned}
P(T,T)={}&-T^2(T-20)(T-2)(T+4)^2(T+6)^2(T+10)\\
&\times(T^2+4T-4)(T^3+2T^2-4T+20).
\end{aligned}
\tag{15}
$$

### 6.2 选定正确的根

矩阵
$$
A=\begin{pmatrix}15&-11\\30&-15\end{pmatrix}
=\begin{pmatrix}15&-8\\30&-15\end{pmatrix}
\begin{pmatrix}1&3\\0&7\end{pmatrix}
\tag{16}
$$
固定 $\tau_0$，左侧行列式为 105，右侧第一因子是 $\Gamma$ 中的 $W_{15}$。由 (14)、对称性及 $T(\tau+3)=T(\tau)$，
$P(T(\tau),T(A\tau))=0$。特别地 $P(T(\tau_0),T(\tau_0))=0$。

这里可用很粗的严格估计选根，无需把数值识别当作证明。写
$q_0=-\rho=-e^{-\pi\sqrt{105}/15}$，则
$29/250<\rho<59/500$。从 eta 乘积取出第一个因子 $1+\rho$，对剩余乘积使用 $|\log(1-w)|\le |w|/(1-|w|)$，其对数绝对值小于 $1/25$。因此
$$
\frac3{25}<|R(\tau_0)|<\frac7{50},\qquad
-11<T(\tau_0)<-9.
$$
(15) 在此区间只有根 $-10$，故 $X(\tau_0)=-1/10$。这些区间可仅用有理数和指数函数的 16 项 Taylor 上下界验证，见 [cm-certificate.py](../scripts/cm-certificate.py)。

### 6.3 导数特殊值

在 $(T,U)=(-10,-10)$，微分给出
$$
P_U=429649920000,\quad
P_{TT}=-723889152000,\quad
P_{TU}=-807091200000.
$$
由对称性，局部分支 $U=U(T)$ 满足
$$
U'=-1,\qquad U''=-\frac{2(P_{TT}-P_{TU})}{P_U}
=-\frac{122}{315}.
$$
改为 $x=1/T,y=1/U$，得到
$$
\frac{dy}{dx}=-1,\qquad
\frac{d^2y}{dx^2}=-100U''-40=-\frac{80}{63}.
\tag{17}
$$

另一方面 $y(\tau)=X(A\tau)$，而 (16) 在固定点的导数为
$(A\tau)'=-1$、$(A\tau)''=-2i/y_0$。对
$y(\tau)=y(x(\tau))$ 微分两次，并在固定点代入 (17)，得到
$$
D\log(DX)=\frac{1}{2\pi y_0}
+\frac12\frac{d^2y}{dx^2}\,DX.
$$
结合 (12)，
$$
\left[X\partial_X+
1+\frac{XG'}{2G}-\frac X2\frac{d^2y}{dx^2}\right]Z
=\frac{1}{2\pi y_0\sqrt{G}}.
\tag{18}
$$
在 $X=-1/10$，方括号中的常数为 $4/21$，且
$G=189/500$、$\sqrt G=3\sqrt{105}/50$。右侧即 $50/(21\pi)$，证明 (13)。在此点所用局部坐标无分歧：它不是 $G$ 的零点；亦可由标准 eta 表达式 $Z^2=\eta_1\eta_2\eta_3\eta_5\eta_6\eta_{10}\eta_{15}\eta_{30}/X^3$ 看出 $Z\ne0$。

## 7. 回到原级数

在 $r=1/4$，有
$$
a=-3/20,\ b=1/2160,\qquad
\mathcal F_b=5040\mathcal F-3996\mathcal F_a,
$$
以及由 (4)、(5) 得
$$
H'=\frac{224}{5}H-\frac{544}{15}\mathcal F_a.
$$
故 (1) 化为
$$
54H+\frac{315}{16}H'.
$$
再由 (9)，$X=-1/10$、$H=\tfrac35 Z$、
$H'=-\tfrac{32}{25}Z-\tfrac{24}{125}Z'$，从而
$$
54H+\frac{315}{16}H'
=\frac{189}{5}\left(XZ'+\frac4{21}Z\right)_{X=-1/10}
=\frac{189}{5}\cdot\frac{50}{21\pi}
=\boxed{\frac{90}{\pi}}.
$$
原级数已经证明绝对收敛，故这里得到的是题目要求的通常级数和。证毕。

## 8. 复核边界

- 这是使用标准 30 级 Hauptmodul 参数化的证明；第 5 节明确列出外部数学输入与出处。
- 第 2–4 节的代数消元、第 6 节的模方程及复乘导数都具有有理数计算附件，有限数据并未被无条件当作恒等式证明。
- 不对该变换或证明的发表优先权作判断。模 $p^2$ 的有限论证见 [九分支主稿](nine-branches-proof.md)。
