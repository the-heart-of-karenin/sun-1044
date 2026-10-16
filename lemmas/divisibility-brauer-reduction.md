> 辅助研究笔记。个别段落保留早期进度描述；本文的用途及后续主稿见 [阅读顺序](../docs/reading-guide.md)。

# 整除断言的新约化：一个固定双平面的形式Brauer对数

2026-10-16。第1、2节是完整的约化；第3节给出后续可能使用的形式群引理，不把尚未构造的几何对应当成已有证明。

后续更新：[divisibility-proof.md](../proofs/divisibility-proof.md)现通过另一条路径完成全体素数的整性证明草稿，详见[divisibility-audit.md](../review/divisibility-audit.md)。第3节所提7次整形式群对应仍未构造，新证明使用Hodge除子类、普通相对晶体比较及超特殊一阶变形；下面的“尚未完全证明”保留为本文件初稿时的历史状态。

## 1. 消掉R_n中的卷积

令g=(1+x+y)^3/(xy)-324(1+x+y)，以及

beta_n(v)=CT_(x,y)(v g-540)^n，beta_n=beta_n(1)。

则beta_n(v)=sum_(j<=n) binom(n,j)(-540)^(n-j) v^j A_j。
定义奇形式级数

ell_v(u)=sum_(n>=0) beta_n(v) u^(2n+1)/(2n+1)，
J(u)=[(357v*d/dv+103)ell_v(u)]_(v=1)。

置phi(t)=t/sqrt(1-540t²)。它和其复合逆t=u/sqrt(1+540u²)都属于t Z[[t]]，首项系数1。
由逐项微分及常数项计算有恒等式

d/dt ell_v(phi(t))
 =CT (1-540t²)^(-3/2)/(1-(v g-540)t²/(1-540t²))
 =(1-540t²)^(-1/2) G(vt²)。

因此

J(phi(t))=sum_(n>=0) R_n t^(2n+1)/(2n+1)。              (A)

由两个坐标变换的整数系数，原整除断言等价于J(u)属于Z[[u]]。
写J=sum D_n u^(2n+1)/(2n+1)，则

D_n=(357n+103)beta_n+192780n beta_(n-1)，beta_(-1)=0。

令N=2n+1，有

2D_n=N*(357beta_n+192780beta_(n-1))
      -(151beta_n+192780beta_(n-1))。

所以原断言又等价于

(2n+1) divides 151beta_n+192780beta_(n-1) 对每个n>=0。   (B)

这不是把模p的一阶同余迭代成素数幂同余，而是对每个n的整数等价变换。

## 2. 双平面与形式群

令s=x+y+z，

P_v=xyz*[v(s³-324xy s)-540xyz]。

它是整系数六次齐次多项式，而且

beta_n(v)=[x^(2n)y^(2n)z^(2n)] P_v^n。

双平面X_v: w²=P_v（w权3）的形式Brauer群有上述ell_v作为一个坐标下的对数。
这里不应额外乘binom(2n,n)；那是把双平面改写成另一加权超曲面坐标时可能得到的另一坐标公式。

可直接按Cech上同调说明所需的整形式群：取P²三个标准仿射开集的逆像，三重交集上的乘法2余循环1-u*w/(xyz)给出坐标。
pi_*O_X=O_(P²)直和O_(P²)(-3)，所以H¹(O_X)=H³(O_X)=0，H²(O_X)为底环上的秩1自由模。
按u次数逐步消去Cech余边界，只需对Laurent单项式分组，不需要除以整数；这给出整系数的一维形式群法则。
在特征0取-log(1-a)：偶次项属于O_(P²)的H²，故为余边界；第2n+1项投到w/(xyz)方向的系数恰为beta_n(v)/(2n+1)。
这也说明该公式在奇特征下的平坦双平面族上可用，不要求预先选取整个族的同时消解。
中央纤维若只有有理双点，消解满足R^i pi_*O=0 (i>0)，对幂零理想逐层应用1+I的过滤，知其形式Brauer群与消解的一致。

标准出处：J.Stienstra, Formal group laws arising from algebraic varieties, Amer.J.Math.109 (1987), 907-925, Theorem2；原文书目和扫描件入口见
https://webspace.science.uu.nl/~stien101/publications
https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/stienstra1-ocr.pdf
上段给出本题所需的Cech计算，以免只靠未经核对的对数正规化。

## 3. 以后可使用的反对称准对数引理（已证，但尚未对本题全体p应用）

设p为奇素数，F是一维Z_p形式群。q(u)∈Q_p[[u]]满足q(0)=0、q'整，且

q(F(x,y))-q(x)-q(y)∈Z_p[[x,y]]。

若存在a∈Z_p^×使

q([a]_F(u))+a q(u)∈Z_p[[u]]，                           (C)

则q本身为整系数。

证明：若首个非整系数为c_N，则线性项因q'整而无问题。准对数条件迫使p整除所有中间二项式系数binom(N,j)，所以N=p^r；这些二项式系数的最大公因子恰为p，又迫使v_p(c_N)=-1。
(C)的第N项模整系数为(a^N+a)c_N，但a^(p^r)+a=2a(modp)为单位，矛盾。

本题J是该形式群的准对数：对ell_v(F_v(x,y))=ell_v(x)+ell_v(y)求v导数，并用ell_v'整，立即得到准对数条件。
因此，如果能在p整形式群上构造使J满足(C)的CM对应，就可以一次控制所有p次幂，而无需扫描n或素数。
**这个对应及其p整性尚未构造。** 复数周期的7次模方程及加权超同余的Wronskian论证，不会自动给出(C)。不能在这里宣布完整整除命题成立。

另一有用的已证引理：若R是p进完备且p无挠，形式群F/R的 $[p](u)$ 全部系数含p，则其正规化对数ell∈R[[u]]。
按次数归纳：$\ell([p](u))=p\ell(u)$，第N项给p(1-p^(N-1))ell_N等于p倍的R元素；因1-p^(N-1)为单位，得ell_N整。

## 4. 当前状态

原命题仍未完全证明。(A)、(B)提供与原断言等价的全n问题；形式群解释提供可针对素数幂使用的结构。
[divisibility-five-adic.md](divisibility-five-adic.md)进一步用本模型证明全部5进部分。
