> 辅助研究笔记。个别段落保留早期进度描述；本文的用途及后续主稿见 [阅读顺序](../docs/reading-guide.md)。

# 惰性素数的全部高次幂：几何证明草稿

2026-10-16续研。本文处理p>7且(-105/p)=-1的全部p次幂，不是仅检验n=(p^r-1)/2。p=17也已由[divisibility-seven-seventeen.md](divisibility-seven-seventeen.md)独立处理。以下自审尚无外部同行审阅。

记号及全n等价约化见[divisibility-brauer-reduction.md](divisibility-brauer-reduction.md)：

g=(1+x+y)^3/(xy)-324(1+x+y)，
beta_n(v)=CT(vg-540)^n，
ell_v(u)=sum beta_n(v)u^(2n+1)/(2n+1)，
J=(103+357v*d/dv)ell_v|_(v=1)。

目标是J属于Z_p[[u]]。

## 1. 一个明确的判别式60子格

这一步不需要假定完整Neron--Severi格的判别式。

先把双平面改写为已有椭圆模型，补全此前只写出双有理关系的连接。置

X=x/(1+x+y)，Y=y/(1+x+y)，Z=1-X-Y，

则

(vg-540)(XYZ)^2
 =-540 XYZ*[XY(c-X-Y)-b]，
c=1+3v/5，b=v/540。

因此除去常数二次扭曲-540，中央v=1正是[geometric-exploration.md](../archive/geometric-exploration.md)的曲面。
其椭圆模型为

Y^2=X^3+(3-2c)X^2+(3-c)(q-e)X+(q-e)^2，
c=8/5，e=3/5，q=(s+1)^2/(540s)，d=1/135。

奇异纤维为2 IV*+3 I2+2 I1，平凡格判别式绝对值72。
两个截面为

P=(0,q-e)，
X_Q=(5q-3)(135q-16)/80，
Y_Q=(3 sqrt(15)/64)(q-e)(135q-64)*sqrt(q(q-d))。

两个截面均与零截面不相交：有限处坐标没有极点；在s=0、无穷，令t=1/q并用最小坐标(t^2 X,t^3 Y)，两者仍有限。

P在两个IV*纤维各遇非恒等分量，贡献4/3；在q=e上方的两个I2各贡献1/2；在q=0的I2遇恒等分量。
Q在IV*处的最小X坐标为135/16非零，遇恒等分量；在三个I2均遇非恒等分量。
于是Shioda高度公式给

<P,P>=4-2*(4/3)-2*(1/2)=1/3，
<Q,Q>=4-3*(1/2)=5/2。

底变换对合s -> 1/s保持P、把Q变为-Q，所以<P,Q>=0。
平凡格与这两个截面生成一个整格L，秩19，且

|disc L|=72*(1/3)*(5/2)=60。

这里计算的是实际生成子格的行列式。无需证明截面生成整个Mordell--Weil群，也无需证明L在NS中饱和。
高度与行列式公式出处：T. Shioda, On the Mordell-Weil lattices (1990)，第8节。
https://doi.org/10.14992/00009994

## 2. 好约化及Artin不变量

在p>7、p不等于17时，双平面分支为三个坐标轴与光滑三次曲线

C=(x+y+z)^3-324xy(x+y+z)-540xyz。

分支的固定接触给2 A5+6 A1；这些有理双点在v=1的一阶邻域内等奇异，可以逐次吹起消解。所需坐标常数仅在2、3、5处有分母，分支点分裂可作有限不分歧扩张。

为了核对没有漏掉其他坏素数，有以下恒等式：

C_x-C_y=108(x-y)(3x+3y+8z)，
C(x,-8/3-x,1)=-125/27，
disc_x C(x,x,1)=2^6*3^9*7*17^2，
disc_x C(x,1,0)=2^12*3^12*5。

故p>7、p不等于17时无额外三次曲线奇点或轴上接触碰撞。p=23虽会合并此椭圆纤维中的I1与I2，却不破坏双平面的这个同时消解；不能把椭圆纤维碰撞误判为曲面坏约化。

因此L在光滑K3约化上专化且保持判别式60，模p仍给非退化的秩19子格。

令h=(p-1)/2。双平面Hasse系数为beta_h，并且

beta_h=(-540)^h S_p (modp)。

这里用binom(h,j)=(-1)^j binom(2j,j)/4^j(modp)，以及j>h时binom(2j,j)=0(modp)。由已证惰性分支S_p=0(modp)，知约化不普通。Picard数至少19及Artin--Mazur的rho<=22-2h不等式，排除其余有限高度，所以形式Brauer群高度无穷。

超奇异K3的Tate格是p初等格，模p非退化部分秩22-2sigma，sigma为Artin不变量。判别式为p单位的L在其中给非退化秩19子格，所以

19 <= 22-2sigma，

从而sigma=1。也可以在Ogus的超奇异K3晶体T_H中作同一计算，不必以Tate猜想为前提。

## 3. 超特殊K3的一阶形式Brauer变形引理

**引理。** p为奇数，X/k为Artin不变量1的超奇异K3曲面。其任意光滑一阶变形X_epsilon/k[epsilon]/(epsilon^2)的形式Brauer群，都满足[p]=0。

注意：本引理涉及所有系数；只知道第一个Hasse不变量的一阶导数为零，不足以代替它。

证明可用van der Geer--Katsura的高阶Hasse构造逐阶给出。令B_m Omega^1为高阶恰当微分形式层。对sigma=1，所有m>=1都有

Im[H^1(B_m Omega^1) -> H^1(Omega^1)]=0。

这由该文Corollary11.12给出；本曲面是椭圆K3，超奇异时rho=22，满足该节的假设。

假设相对Witt上同调H^2(W_j O)上的F已经对j<m为零。依该文第8、13节，下一障碍由一个标量g_m给出：

g_m=<Phi_m(alpha),omega>，

其中omega为二形式基，alpha提升H^2(O)的对偶基，Phi_m(alpha)为水平de Rham类；在中央纤维，其F^1/F^2分量来自H^1(B_m Omega^1)。前述像为零，故中央Phi_m(alpha)为omega的倍数。

由水平性及<omega,omega>=0，

dg_m|_0=<Phi_m(alpha)|_0,nabla omega|_0>=0。

而中央g_m=0，所以在一阶底上g_m恒为零。m=1时同一论证从共轭线=Hodge二形式线开始。归纳对每个m成立，得到F在所有有限长度Witt上同调上都为零。

相对Cartier模实现H^2(W O)为形式Brauer群的曲线模；p=FV，故其p级数为零。这是对整个形式群的结论，而非仅有限个高度的结论。

使用的相对构造在该文第8节的Cech双复形及第13节的水平性证明中给出，均可在一阶底上进行；这里没有把仅对域值点成立的高度判别无条件用于非约化底。
https://arxiv.org/pdf/math/9910061

另一核对入口是Ogus, Singularities of the height strata in the moduli of K3 surfaces，Corollary13及Theorem19。前者给超特殊点的所有高度分层具有完整切空间，后者给非约化的S_infinity=S_11；本证明采用上面的全m归纳，避免只凭约化点集作推断。
https://math.berkeley.edu/~ogus/preprints/k3strat.pdf

## 4. 回到整系数

在R=W(k)[epsilon]/epsilon^2上取v=1+epsilon。第2节的同时消解给光滑一阶K3族；由第3节，其形式Brauer群的[p]全部系数属于pR。

[divisibility-brauer-reduction.md](divisibility-brauer-reduction.md)的整对数引理于是给

ell_(1+epsilon)(u)属于R[[u]]。

分别取epsilon的0次、1次项，ell_1与(dell_v/dv)|_1都p整，所以J也p整。系数原在Q_p中，向W(k)的扩张不改变其p进赋值。

这证明对每个惰性p>7及每个n，

p^r | R_n，只要p^r | 2n+1。

p=17由先前的独立论证补入，不要求在那里的一阶平滑化有同时消解。

## 5. 核验及边界

[divisibility-inert-certificate.py](../scripts/divisibility-inert-certificate.py)核验第1、2节的代数恒等式，并只抽查p=23、37的r=1、2个别系数；总运算约0.13秒。抽查不代替第3节的全阶论证。

此稿完成惰性素数的全部幂。完整整除命题尚需普通素数p>7处的p进比较，不能从本引理推到普通点。
