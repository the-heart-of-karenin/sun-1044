> 辅助研究笔记。个别段落保留早期进度描述；本文的用途及后续主稿见 [阅读顺序](../docs/reading-guide.md)。

# 有限截断的二次恒等式：模 p² 的证明

2026-10-16。本记录用于九分支研究，给出有限截断的代数论证。没有用有限个素数的吻合替代证明。

令 b_n(t)=binom(2n,n) A_n(t)，P_p(t,z)=sum_(n<p) b_n(t) z^n。所有 p 均为素数，p>7。

## 1. 截断仍满足四阶方程模 p²

使用 [analytic-reduction.md](analytic-reduction.md) 的 L4=sum_(j=0)^4 z^j R_j(theta)。则

L4 P_p(t,z)=0 (mod p²)，在 Z_(p)[t,z] 中成立。

证明：只有 z^p 至 z^(p+3) 的系数可能不为零。

z^p 的系数用完整递推写成 -R0(p)b_p，含 p³。

z^(p+1) 的系数用完整递推写成

-R0(p+1)b_(p+1)-R1(p)b_p
=p[b_(p+1)-2(t+6)b_p] (mod p²)。

[toric-period.md](toric-period.md) 的 Laurent 多项式 Lambda_t 的各坐标指数位于 [-1,2]、[-1,2]、[-1,1]，所以 p>3 时

b_p(t)=b_1(t^p)，b_(p+1)(t)=b_1(t)b_1(t^p) (mod p)，b_1(t)=2(t+6)。

这也可直接由 Freshman dream 和常数项提取得到：Lambda 的指数若被 p 整除，只能是0。因此该系数为0。若 t 已特殊化为整数，才可把 t^p 换成 t；作为多项式恒等式不作此替换。

z^(p+2) 的系数只有 R3(p-1)b_(p-1)+R4(p-2)b_(p-2)。由阶乘公式

A_(p-1)=t^(p-1)，A_(p-2)=t^(p-2) (mod p)，

b_(p-1)=-p A_(p-1)，b_(p-2)=-(p/6) A_(p-2) (mod p²)，

故该系数为 40p t³[A_(p-1)-t A_(p-2)]=0 (mod p²)。

最后，z^(p+3) 系数为 R4(p-1)b_(p-1)，两个因子各含 p。

## 2. 双变量截断的两个偏微分方程也成立模 p²

记 C_p(a,b)=sum_(m+k<p) c_(m,k) a^m b^k，c 与 [proof-series.md](../proofs/proof-series.md) 相同。该文件 (2)、(3) 的两个算子均消去 C_p 模 p²。

第一算子的边界只有 m+k=p，完整系数关系给出误差 -mp c_(m,k)。当 0<k<p 时 c_(m,k) 被 p 整除；k=0 时 m=p，额外再有一个 p；m=0 时误差为0。

第二算子的 m+k=p 边界同理。其 m+k=p+1 边界只来自向前移动 (2,0) 的项。写 j=m-2，j+k=p-1，该项的算子系数模 p 为

4+12j+8k+8j(j+k)=4k (mod p)。

若 k>=1，c_(j,k) 的两个分子阶乘各提供一个 p；若 k=0，该算子系数本身被 p 整除，而中央二项式系数另外含 p。因此误差均被 p² 整除。

对这些多项式同余求导，再进行有理线性消元是合法的；特殊化时须检查消元分母。

## 3. 固定 t=-324 的二次不变量

改用 x=108z，Y_p(x)=P_p(-324,x/108)。沿用 [product-decomposition.md](product-decomposition.md) 的 a(x), b(x), d²(x), C(x), B(x), A(x)：

C=(1+12x)^3-x，B=1-24x，A=1+30x，

a=1/x+C'/(2C)+12/B，

b=(3359232x^4-46656x³-52200x²-1419x+53)/(18xB²C)，

d²=(160/3) A²/(x²B^4 C)。

为任意函数 Y 定义

W=(Y''+aY'+2bY)/2，

V=(b'+2ab)Y+(2b+a'/2+a²)Y'+(3a/2)Y''+Y'''/2，

Q(Y)=YW-(Y')²/4+V²/(4d²)，

J(Y)=4x² C Q(Y)/B。

完整生成函数 Phi 满足 Q(Phi)=0，见 [product-decomposition.md](product-decomposition.md) 的两个二阶因子之积。直接微分也给出

J(Y)'=(x² C/B)(V/d²) L_monic(Y)，

其中 L_monic 是同一四阶算子的首一形式。因此第1节推出 J(Y_p)'=0 (mod p²)。

下面证明这一导数同余确实使 J(Y_p)=0 (mod p²)，需要排除特征 p 的积分常数，不能只用“导数为零”。

(a) J 的各个 jet 二次系数没有 x=0 的极点，其有限极点分母可取

D=B³ C² A²。

在 p>7 的剩余特征中，D 的任一根的重数小于 p。事实上 B 不与 A,C 相碰；A 与 C 只可能在 p=11,17 相碰，合并后重数至多4。D 的首项系数是 p 进单位。

一个有限极点阶数小于 p 的有理函数，若导数模 p 为零，其极点部分只能为零。对 J 先模 p 应用，再对剩余的 p 倍有理函数应用一次，得到 J(Y_p) 模 p² 是多项式。

(b) 在无穷远有 a=O(x^-1)、b=O(x^-2)、1/d²=O(x^7)、x²C/B=O(x^4)。所以 J(Y_p) 的多项式部分次数至多 2(p-1)+5=2p+3。结合 J'=0 模 p²，只有次数0、p、2p 的项可能存在。

(c) Y_p(0)=1，Y_p'(0)=-53/9，故 J(Y_p)(0)=0。完整 Phi 与 Y_p 首次在 x^p 项有差异。将一个 epsilon*x^N 加到具有相同初值的 Phi 中，J 的首次变化在 x^N，其系数是

epsilon * [2N²+gamma*N³/d20]，

其中 d20=160/3，gamma=[x^-1]V(Phi) 在 Z_(p) 中。此式直接由 a=1/x+O(1)、d²=d20/x²+O(x^-1) 和 Y_p'(0)=-2[x^-1]b 得到。因此 N=p 时该变化被 p² 整除，排除 x^p 项。

(d) J(Y_p) 在无穷远的 x^(2p) 项，只可能来自 Y_p 的两项 x^i、x^j 满足 i+j+5>=2p。因 i,j<=p-1，必有 i,j>=p-4>(p-1)/2。两个相应系数都因中央二项式系数而被 p 整除。各固定有理 jet 系数在无穷远的 Laurent 展开均 p 整，故这个 x^(2p) 系数也被 p² 整除。

综上，严格得到

J(Y_p)=0 (mod p²)，亦即 Q(Y_p)=0 (mod p²)

作为有理函数同余。后一式特殊化时仍须检查其固定分母。

## 4. 特殊点处与一参数对称平方二次式的关系

取 r0=1/4，x0=1/20，a0=-3/20，b0=1/2160。令 H_p(r)=C_p(a(r),b(r))，并令

I(H_p)=H_p H_p''-(H_p')²/2+alpha H_p H_p'+2beta H_p²，

E_p=R0 C_p+R1 C_(p,a)+R2 C_(p,b)，

其中 alpha,beta,R0,R1,R2 沿用 [proof-series.md](../proofs/proof-series.md)。

使用第2节的两条偏微分方程及其导数，将全部三阶导数化为 (C_p,C_(p,a),C_(p,b),C_(p,ab)) 后，以下是四元变量上的二次型恒等式：

Q_fixed = -(1875/18496) I(H_p) -(16384/13272903) E_p²。

计算附件 [isotropy-certificate.py](../scripts/isotropy-certificate.py) 逐个比较两个对称4×4矩阵，运算全为有理数，约0.6秒。18496=2^6*17²，13272903=3^8*7*17²。中间消元还出现表观分母331：全部 u,v 及三阶行向量分母的最小公倍数为 2^5*3^3*7*17²*331。这里不能遗漏331。

由 [hasse-invariant.md](hasse-invariant.md) 中已经证明的模 p 曲线关系，E_p=0 (mod p)。因此，当 p>7 且 p 不等于17、331时，前节二次不变量给出

I(H_p)(1/4)=0 (mod p²)。

这已经是一条模 p² 的有限恒等式，不需要任何复乘值的猜测。

## 5. 对惰性分支的应用

另见 [inert-branch-proof.md](../archive/inert-branch-proof.md)。本文件本身不宣称解决八个普通分支。
