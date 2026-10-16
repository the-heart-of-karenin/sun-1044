> 辅助研究笔记。个别段落保留早期进度描述；本文的用途及后续主稿见 [阅读顺序](../docs/reading-guide.md)。

# 全曲线的有限二次同余（消除17、331的点上例外）

2026-10-16。以下加强 [finite-isotropy.md](finite-isotropy.md) 的第4节，给出所有 p>7 的有理函数同余；因此不再需要对17、331单独计算来证明惰性分支。

## 1. 任意 t 的四阶方程具有同一种二次不变量

令 z 为自变量，置

C=(1-4tz)^3-108z，B=1+8tz，A=1-10tz，

a=1/z+C_z/(2C)-4t/B，

N=768t^5z^4+32t^4z³-108t³z²-192t²z²+9t²z+78tz+t+6，

b=-N/(zB²C)，d²=6t(t+4)A²/(z²B^4 C)。

沿用 [finite-isotropy.md](finite-isotropy.md) 的 W,V,Q,J 定义（把 x 换成 z），则

J'(Y)=(z²C/B)(V/d²)L_monic(Y)。

[generic-product-certificate.py](../scripts/generic-product-certificate.py) 已在 Q(t,z) 中逐项核验原四阶算子与此结构的恒等式；d² 的常数因子恰为6t(t+4)。

[finite-isotropy.md](finite-isotropy.md) 第3节的全部论证现在可在 p-adic Gauss 赋值的系数域 Q(t) 中原样进行：分母 t,t+4 在此赋值下为单位；剩余系数域为 F_p(t)。J 的有限极点分母仍为 B³C²A²，有限极点阶数小于p；无穷远次数界仍为2p+3。初始斜率为2(t+6)=-2[z^-1]b，故 J(0)=0。x^p 项的 N² 因子、x^(2p) 项两个中央二项式系数的 p 因子同样成立。

因此对于 Y=P_p(t,z)，作为 Q(t,z) 中 p 整有理函数的同余，

Q(P_p)=0 (mod p²)。

这里“p 整有理函数”指分母的 p-adic Gauss 赋值为0，不是说可以在分母为0的点直接代入。

## 2. 全参数曲线上的二次型恒等式

现在代入 z=b(r)、t=a(r)/b(r)，并使用 [finite-isotropy.md](finite-isotropy.md) 第2节的模p²偏微分方程消元。令 H_p(r)=C_p(a(r),b(r))，E_p=R0 C_p+R1 C_(p,a)+R2 C_(p,b)。

[curve-isotropy-certificate.py](../scripts/curve-isotropy-certificate.py) 证明下式是 Q(r) 中四元变量的二次型恒等式：

Q_fixed=lambda(r) I(H_p)+kappa(r) E_p²，

lambda=64(r-1)^6(r+1)^4(r+2)(3r-2)(3r²+4r-1)/[5r^6(3r²+4r+2)²]，

kappa=-3(r+1)(3r²+4r-1)/[20r^6(r-1)²(3r+1)(3r²+4r+2)²]。

这里 Q_fixed 的导数是对 z 求导；所以在 r0=1/4 比用 x=108z 的点上二次式多出108²的整体因子。

前节 Q_fixed=0 (modp²)，而 E_p=0 (modp) 是 [toric-period.md](toric-period.md) 的 Lucas 同余微分后与原解析曲线关系结合的直接结论。因此

I(H_p)=H_p H_p''-(H_p')²/2+alpha H_p H_p'+2beta H_p²=0 (modp²)

对所有p>7，作为有理函数同余成立。

每个用于消元的分母以及 lambda，在 F_p(r) 中均非零。即使它们在某个特定r值消失，也不影响有理函数同余的建立。最后将 I(H_p) 写回其原始表达式：其分母只可能涉及 r,r±1,r+2,3r-2,3r+1 以及p进单位常数。它在r=1/4的分母对所有p>7均为单位。因此此处可安全特殊化，包括p=17、331。

## 3. 对惰性分支的简化

[inert-branch-proof.md](../archive/inert-branch-proof.md) 第1节的 H_p=H_p'=0 (modp)、H_p''为单位，结合本文件的全曲线同余，直接给出所有惰性p>7的S_p=0 (modp²)。第3节的17、331有限核验可以保留作交叉检查，但已不是证明必需输入。
