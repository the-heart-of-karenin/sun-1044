> 辅助研究笔记。个别段落保留早期进度描述；本文的用途及后续主稿见 [阅读顺序](../docs/reading-guide.md)。

# 普通形式Brauer群：由Tate类消去准对数的全部分母

2026-10-16。以下给出抽象比较引理及证明。本题的Hodge/Tate类识别单独写在[divisibility-tate-class.md](divisibility-tate-class.md)；不要只用一次模p加权同余代替该识别。

## 引理的设置

设p>2，O=W(k)，k为代数闭域。X_delta/O[delta]/delta^2为光滑K3族，中央约化普通。F_delta为其形式Brauer群，取一个整坐标u，正规化对数ell_delta(u)，ell_delta'(0)=1。

该坐标的切基e_O(delta)属于H^2(O_X)。取二形式omega_delta为它的Serre对偶基：<e_O,omega>=1。记

q(u)=d_delta ell_delta(u)|_0，
eta=A omega_0+B nabla_(d/delta) omega|_0， A,B属于O。

若eta在中央p进de Rham实现中与晶体单位根线正交，则

A ell_0+B q属于O[[u]]。

特别地，若eta是代数除子的一阶Chern类的有理线性组合，这一正交条件自动成立。

## 1. 高度1形式群的直接计算

由高度1形式群的Lubin--Tate变形刚性，选择中央约化到乘法形式群的同构后，可在O[delta]/delta^2上取整同构

h_delta:F_delta -> Ghat_m， h_delta(u)=a(delta)u+...， a(delta)为单位。

正规化对数满足恒等式

ell_delta(u)=a(delta)^(-1)*log(1+h_delta(u))。

求导得

q(u)=lambda ell_0(u)+I(u)，
lambda=-a'(0)/a(0)，
I(u)=a(0)^(-1)*h'_delta(u)|_0/(1+h_0(u))属于O[[u]]。

因此只需证明A+B lambda=0；一旦这个标量严格为零，所有次数的分母同时消失。

## 2. 标量lambda的Gauss--Manin解释

使用形式Brauer群的协变Dieudonne晶体到K3晶体的自然映射。普通时前者秩1，中央纤维斜率0。这个映射是晶体映射，因而水平；在平凡PD增厚上向H^2(O_X)的投影等于形式群切映射。

可引用的输入是Nygaard--Ogus, Theorem3.20；便于核对的当前文本为K. Inoue, Construction of quasi-canonical liftings of K3 surfaces of finite height in odd characteristic, arXiv2108.11227, Theorem3.1及其前两段：

D(Brhat) -> D(Psi) -> H^2_crys

是自然晶体映射，且Theorem3.1的Hodge过滤交换图在取商后给

D(Psi)_R/F^1 -> H^2_dR/F^1=H^2(O_X)

的同构。Brhat是Psi的连通分量，故其Lie与Psi的Lie相同。这正是所需的切映射兼容性。
https://arxiv.org/pdf/2108.11227

对R=(O/p^m)[delta]/delta^2应用该定理并对m取逆极限，得到这里使用的O上一阶族比较。无须把仅在完美域上的斜率同构自行推广到混合特征的非约化底。

另一核对为Langer--Zink, Grothendieck--Messing deformation theory for varieties of K3 type (2019)，第5节式(85)：D(Brhat)到H^2_crys再到H^2(W O)的复合是秩1模同构；H^2(W O)正是Brhat的Cartier曲线模。结合到H^2(O)的投影，这固定了上述Lie兼容性，而非任意选择一个可能随delta变化的标量同构。
https://msp.org/tunis/2019/1-4/tunis-v1-n4-p01-s.pdf

令e(delta)为对应于h_delta下乘法形式群标准基的水平单位根基。由于h_delta在切空间上乘以a(delta)，e(delta)在H^2(O_X)中的像为

a(delta)^(-1)e_O(delta)。

于是f(delta)=<e(delta),omega_delta>=a(delta)^(-1)，从而

lambda=f'(0)/f(0)。

e是水平的，所以

<e(0),eta>=A f(0)+B f'(0)=f(0)*(A+B lambda)。

f(0)是单位，假设的正交条件恰好给A+B lambda=0。代入第1节的直接计算即得结论。

这里需要的是整个形式群的整同构及其切映射；不是把有限截断和当作无限p进周期值。上述晶体映射提供Gauss--Manin兼容性，不能仅凭一个模p的斜率维数计算替代。

原始背景：Artin--Mazur, Formal groups arising from algebraic varieties, Ann. Sci. ENS 10 (1977), 87--131，形式Brauer群与de Rham--Witt/Cartier实现。
https://www.numdam.org/article/ASENS_1977_4_10_1_87_0.pdf
普通族与其形式Brauer群的现代整理可参Taelman, Ordinary K3 surfaces over a finite field，第1节；本引理不用该文附加的潜在半稳定约化猜想或其分类定理。
https://arxiv.org/pdf/1711.09225

归一化的一个检验：若只有坐标变化h_delta(u)=(1+c delta)u，则q=c(u ell'_0-ell_0)，lambda=-c；几何二形式的对偶基相应乘(1+c delta)^(-1)，其连接系数也是-c。两边的符号一致。

## 3. 为什么代数除子类满足正交条件

好约化下，代数除子的晶体Chern类在有限剩余域扩张后满足F^d c=p^d c，因此斜率为1。单位根线斜率为0，而H^2的杯积配对具有权2。Frobenius兼容性迫使两者正交。

即使原除子只在数域扩张上定义，也可先在有限扩张后延拓，再作de Rham/晶体比较；有理系数的正交为零，不需要假定除子本身或其系数在p处为整。由于第1节的I本来就是整级数，不会因此丢失整性精度。

## 本题代入

v=1+delta，A=103，B=357。
[divisibility-brauer-reduction.md](divisibility-brauer-reduction.md)的Cech切基为w/(xyz)，其Serre对偶二形式为常数倍dx wedge dy/w；常数与v无关。

因此，只要证明

eta=103 omega+357 nabla_(v*d/dv)omega|_(v=1)

是除子类的线性组合，便在每个普通好素数处得到J属于Z_p[[u]]，包括所有高次幂。系数原在Q_p中，扩张到W(k)后得到的整性可直接下降。
