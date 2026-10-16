> 辅助研究笔记。个别段落保留早期进度描述；本文的用途及后续主稿见 [阅读顺序](../docs/reading-guide.md)。

# 加权问题中的横向项：模p²的完整求值

2026-10-16。记P_p(r)、E_p(r)同[global-isotropy.md](global-isotropy.md)，h=(p-1)/2，epsilon=(-1/p)。下面证明对所有p>7的有理函数同余

E_p(r)=16p*epsilon*r^(p-1)*(2-r)^p /
       [(r-1)^(3(p-3)/2)*(r+1)^((p-3)/2)] (modp²)。        (E)

## 1. 一阶方程与极点

两个偏微分方程对截断仍模p²成立，因此[nl-certificate.py](../scripts/nl-certificate.py)的一阶关系适用于有限截断：

E_p'=lambda E_p (modp²)，lambda=-1/r+9/[2(r-1)]+3/[2(r+1)]。

而E_p=0(modp)。写e=E_p/p(modp)。令

s(r)=(r-1)^(h+5)*(r+1)^(h+2)/r。

则s'/s=lambda(modp)，从而e/s属于F_p(r^p)。

从显式定义可将E_p写成

-16(r-1)³(r+1)/r * sum_(m+k<p) c_(m,k)a^m b^k
  *[r(r-2)+(3r²-2r-2)m+(3r²-8r+2)k]。

由此及模p²的阶乘赋值区域，E_p在1的极点阶数至多3h-3，在-1至多p-2，在无穷至多5。原点处完整E恒为0，而首次丢失项的偏导来自(m,k)=(p,0)，所以

e(r)=-32 r^(p-1)+O(r^p)。

于是e/s在0与无穷均至少有p阶零点，在1处极点至多2p，在-1处极点小于2p。它又是r^p的有理函数，因此存在常数A,B属于F_p，使

e(r)=r^(p-1)*(A r^p+B)/
 [(r-1)^(3(p-3)/2)*(r+1)^((p-3)/2)]。

原点首项给出B=32epsilon。

## 2. 用已证Franel同余确定另一个常数

在r趋于无穷时a趋于1/4、b趋于-1/16，且

[r^5]E_p=-16*sum_(n<p)(3n+1)binom(2n,n)A_n(-4)/(-16)^n。

这里A_n(-4)=f_n=sum_k binom(n,k)^3 是已知的Franel恒等式。Guo的已证定理为

sum_(n<p)(3n+1)binom(2n,n)f_n/(-16)^n=p epsilon (modp³)。

见Victor J.W.Guo, Proof of a supercongruence conjectured by Z.-H.Sun, arXiv1404.6978v1, Theorem1.4；A_n(-4)=f_n在同文(2.1)。
https://arxiv.org/html/1404.6978

因此A=-16epsilon，代回便得(E)。该引用只需其modp²精度。

## 3. 本题点上的值与加权拆分

在r0=1/4，D=(r0-1)³(r0+1)=-135/256，Euler判别准则给出

E_p(r0)=-(945/64)*p*(15/p) (modp²)。

而原加权和W_p满足线性关系（不忽略有限截断的E项）

W_p=54P_p(r0)+(315/16)P_p'(r0)-(448/135)E_p(r0)。

于是

W_p=54P_p(r0)+(315/16)P_p'(r0)+49p*(15/p) (modp²)。

所以剩余加权命题完全等价于

54P_p(r0)+(315/16)P_p'(r0)=54p*(-1/p) (modp²)。       (T)

横向项已求值；不能将E_p模p为0误用为模p²为0。
