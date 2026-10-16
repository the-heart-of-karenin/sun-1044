# 九分支超同余的证明草稿

本稿将有限二次同余与有理函数刚性结合，讨论 [题面](../docs/problem-statement.md) 中无权和的全部九个分支。初稿日期为 2026-10-16；审阅状态与 AI 参与情况见 [项目说明](../README.md)。有限探测只用于此前发现。

## 0. 记号与已建立的输入

使用 [proof-series.md](proof-series.md) 的 a(r),b(r),H(r)、alpha(r),beta(r)。令

P_p(r)=sum_(m+k<p) c_(m,k) a(r)^m b(r)^k，P_p(1/4)=S_p，

I(Y)=YY''-(Y')²/2+alpha YY'+2beta Y²，导数均对r。

已证输入：

1. H(q)=(B-A)(A+B)²/(AB)，其中 A=eta1 eta2 eta15 eta30、B=eta3 eta5 eta6 eta10。r=-2/(T+2)，T=A/B+B/A-2，是Gamma0(30)^+的有理坐标；r=-2q+O(q²)。H=1+2q+O(q²)。
2. H=f²，f''+alpha f'+beta f=0，且 (Dr/H)²=r²(r+2)(3r-2)(3r+1)/(4(r-1))，D=q d/dq。特别地 alpha=(log(Dr/H))'。
3. 模p的 Laurent 常数项/Lucas 恒等式给出 P_p(q)=H(q)/H(q^p) (modp)。
4. [global-isotropy.md](../lemmas/global-isotropy.md) 已证明，对每个p>7，I(P_p)=0 (modp²)，作为p整有理函数同余成立。该步包含有限截断的边界证明和两个符号计算附件，不用下面的模形式比较。
5. [cm-eight-branches.md](../lemmas/cm-eight-branches.md) 已证明Atkin-Lehner字符、八种表示给出的单位u及 chi(W_e)u²/e 与八行右侧的相等模p²。[quadratic-forms.md](../lemmas/quadratic-forms.md) 已处理表示存在性与选择的无关性。

下面新证明关键的全曲线比较，再在CM点特殊化。

## 1. 权2周期的除子与模p的P_p

H的内部零点只有R=A/B=1、-1，它们分别对应r=-1、1。它们在上半平面局部参数tau-tau0中的零点阶数分别为1、2；r在两点的分歧阶数均为2。因此在r曲线上H的有理除子阶数分别为1/2、1。

可直接从eta表达式与DX=X sqrt(G)Z核对阶数：若R-1零点阶数k，则T=(R-1)²/R给出X极点阶数2k，DX恒等式给出H零点阶数2k-1，与eta式的k相等，故k=1；若R+1零点阶数k，同理比较得H的2k=3k-1，仍得k=1。

其余可能分歧点r=-2,2/3,-1/3由(Dr/H)²的三个简单零点给出，分歧阶数均为2；r=0是唯一尖点，r=无穷不是分歧点。p>7时这些点互异，所有有关分歧均为与p互素的2。

记 P0=P_p modp。Hasse不变量Ha与q展开原理给出

P0*H^(p-1)=Ha² (modp)，

作为Gamma0(30)上的模形式恒等式，等价于第0节的模p比较。可先从模p仍非零项的阶乘赋值得到P0的极点上界p-1、h，确认乘积P0*H^(p-1)全纯，再与q展开为1的E_(p-1)²比较。Hasse不变量在超奇异点处只有简单零点，在尖点非零。这里使用Igusa定理，可见Katz--Mazur, Arithmetic Moduli of Elliptic Curves, Theorem12.4.3。

因此：

- r=1处，P0的极点阶数是p-1或p-2；
- r=-1处，P0的极点阶数是h或h-1，其中h=(p-1)/2；
- 其余各点P0的零点阶数至多2；
- P0(0)=1。

这些是确切的阶数范围，而不只是上界。它们将排除额外的特征p积分常数。

## 2. Hecke乘积提供一个有理Frobenius商

令Theta=H，定义

T_p(U)=(1-H(p tau)U/H(tau))*product_(k=0)^(p-1)(p²-H((tau+k)/p)U/H(tau))。

写T_p(U)=sum_m T_m(r)U^m，A_p=T_(p+1)。Gamma0(30)上的字符平凡，而在完整Atkin-Lehner群上为[cm-eight-branches.md](../lemmas/cm-eight-branches.md)的正负字符。因此Hecke对应置换此乘积的因子，T_m均为Q(r)中的有理函数。这是Beukers, arXiv2403.03301, Lemma3.7及Section5使用的同一乘积。

这里不套用该文需要“唯一零点”等条件的最终定理。只使用/重新证明此乘积的基本性质，允许H有上述两个零点。

T_m的极点只能在H的两个零点，阶数满足

pole_(r=1)(T_m)<=m，pole_(r=-1)(T_m)<=floor(m/2)。

乘积的q展开是整数展开；以(r-1)^m(r+1)^floor(m/2)清分母，再用r(q)=-2q+...形式反演，可知清分母后的有理数多项式在p>7处整。

基本同余为

T_p(U)=T_p(r) U^p+A_p(r) U^(p+1) (modp³)，A_p=1 (modp)。     (M)

注意式中T_p(r)是U^p的系数，不是整个多项式。

简证(M)：展开有p个因子的乘积，U^m系数至少含p^(2(p-m))。m<=p-2因此含p^4；m=p-1时额外的对称和e_(p-1)被p整除，因它是去掉一个因子的p个循环平移之和。令v=q^(1/p)、zeta为p次单位根，循环平移之和只保留v^(pj)的系数，每项被p乘；这些保留系数因Galois不变性而为整数。另一外部因子的贡献也至少含p³。最高系数

A_p=H(q^p)*product_k H(zeta^k q^(1/p))/H(q)^(p+1)

模p为1（先在整数环Z_p[zeta]中约化zeta=1，再用其与Z_p的交理想为p）。这证明(M)，并且所有同余是p整有理函数的同余。

定义明确的有理函数

C_p(r)=-T_p(r)*(2-A_p(r))。

因为A_p=1(modp)，(2-A_p)是A_p的模p²逆元。把形式零点U=H(q)/H(q^p)代入(M)，得到

C_p(r(q))=H(q)/H(q^p) (modp²)。                         (F)

其极点界为

pole_1(C_p)<=2p+1，pole_(-1)(C_p)<=p，且其余各点（包括无穷和尖点）无极点。

## 3. C_p也满足二次同余

令K(q)=H(q^p)，g=f K^(-1/2)，则H/K=g²。由alpha=(log(Dr/H))'，

(d²/dr²+alpha*d/dr+beta)(f v(q))= f/(Dr)² * D²v(q)。

取v=K^(-1/2)。其q展开只含q^(pj)，所以D²v含因子p²。f与1/(Dr)²的q Laurent展开均p整。又对任意g有恒等式

I(g²)=2g³(g''+alpha g'+beta g)。

因此I(H/K)=0 (modp²)。由(F)与q展开原理/有理函数清分母，得到

I(C_p)=0 (modp²)。

## 4. 有理函数刚性：C_p必为原来的有限截断

由模p比较，C_p=P_p=P0 (modp)。令

D0=(C_p-P_p)/p (modp)，w=D0/P0，均属于F_p(r)。

把两个二次同余相减并线性化，得到

w''+(P0'/P0+alpha)w'=0。                              (R)

这里P0(0)=1、alpha=1/r+O(1)。若w'非零，取它在r=0的首项c*r^n，则(R)的首项迫使n=-1(modp)。然而一个形式Laurent级数的导数不可能具有这样的首项：r^(jp)的导数为0，所有非零导数项的指数都不等于-1模p。矛盾。因此w'=0，从而w属于F_p(r^p)。

现在控制w的极点。由第2节C_p的界，以及P_p定义中各项的阶乘赋值，

pole_1(P_p)<=3h，pole_(-1)(P_p)<=p-1。

第一个界的说明：模p²仍可能非零的项满足floor(2n/p)+floor((m+3k)/p)<=1。若n=m+k<=h，则m+3k<=3h；若n>h，则必须m+3k<p。第二个界直接由n<p得到。

结合第1节P0的确切极点阶数，w在1处的极点阶数至多p+3<2p；在-1处至多h+2<p；在P0的其余零点处至多2<p；在无穷处同样至多2。w属于F_p(r^p)，其非零极点阶数必须是p的倍数。因此唯一允许的极点在r=1，阶数至多p。必有

w=c0+c1/(r-1)^p。

最后只需两个很短的初始系数。C_p/H=1/H(q^p)=1-2q^p+O(q^(2p)) (modp²)。而a(q)=q+O(q²)、b(q)=q^4+O(q^5)，故原完整双变量级数被三角截断丢掉的第一项，在q^p处只有(m,k)=(p,0)，其系数为binom(2p,p)=2(modp²)。因此

P_p/H=1-2q^p+O(q^(p+1)) (modp²)。

所以w的常数项与q^p项都为0。由r=-2q+...，上述c0+c1/(r-1)^p的常数项是c0-c1，q^p项是2c1，迫使c0=c1=0。

严格得到对所有p>7的有理函数/形式幂级数同余

P_p(r(q)) H(q^p)=H(q) (modp²)。                       (KEY)

更适合CM特殊化的说法是 P_p(r)=C_p(r) (modp²)，两边在r=1/4均p整。本步从未将复数q值直接代入p进形式同余。

## 5. 八个分裂分支

取alpha_CM=(15+sqrt(-105))/30，r(alpha_CM)=1/4。对任一分裂p>7，使用[cm-eight-branches.md](../lemmas/cm-eight-branches.md)表中的e,u,c,d，满足

u=c alpha_CM+d为p进单位，u*bar(u)=ep，30|c，e|d。

令c'=-c，d'=d+c(alpha_CM+bar(alpha_CM))，则bar(u)=c'alpha_CM+d'。与Beukers的Theorem1.16证明同样的初等整数矩阵构造给出W_e中的矩阵gamma=(a,b;c',d')及整数k，使

gamma alpha_CM=(alpha_CM+k)/p。

该矩阵构造只要求30|alpha_CM|²=11、(30/e)(alpha_CM+bar(alpha_CM))=30/e为整数，并使用gcd(c'/e,d')=1；后者若有公因子只能为p，继而会推出p²|ep，矛盾。

由权2斜杠变换H|gamma=chi(W_e)H，

v=p² H(alpha_CM)/H((alpha_CM+k)/p)=chi(W_e)u²/e。

它是T_p(U)在r=1/4处的一个p进单位根。由于r0±1均为单位，第2节的所有系数同余可在该点特殊化，而且A_p(r0)=1(modp)为单位。(M)代入v后给出

v=-T_p(r0)/A_p(r0)=C_p(r0) (modp²)。

结合第4节，

S_p=chi(W_e)u²/e (modp²)。

[cm-eight-branches.md](../lemmas/cm-eight-branches.md) 第3节已逐行证明这个表达式就是题目所列的八个4x²/2x²/...公式。表示存在性及任意表示给出相同答案见[quadratic-forms.md](../lemmas/quadratic-forms.md)。

## 6. 惰性分支

若(-105/p)=-1，Deuring判别与第1节的Hasse平方恒等式给出：r0=1/4处P_p恰有二重零点模p。该点不等于上述5个分歧值，也不是尖点，p>7时始终如此。因此

P_p(r0)=P_p'(r0)=0 (modp)，P_p''(r0)为单位。

由第0节的全曲线二次同余，后三项均被p²整除，剩下P_p(r0)P_p''(r0)=0(modp²)，故

S_p=P_p(r0)=0 (modp²)。

本步包括p=17、331，无须逐素数补丁；先前的点上消元例外已由[global-isotropy.md](../lemmas/global-isotropy.md)消除。

## 标准文献输入与边界

- 第一题已用的30级模参数化：Campbell--Cooper--Ye, arXiv2602.09352v1，https://arxiv.org/html/2602.09352v1 。
- Hecke乘积的不变性及CM整数矩阵构造：Beukers, arXiv2403.03301v3, Lemma3.7与Theorem1.16的证明，https://arxiv.org/html/2403.03301v3 。本稿没有直接应用该文最终定理的零点假设；两零点情形的比较由第4节另证。
- Hasse不变量的简单零点：Katz--Mazur, Theorem12.4.3（Igusa），https://math.bu.edu/people/jsweinst/AWS/Files/KatzMazurArithmeticModuli.pdf 。
- Deuring的CM普通/超奇异约化判别。

本文处理无权九分支。加权同余见 [加权主稿](weighted-wronskian-proof.md)，整除性见 [整除主稿](divisibility-proof.md)。
