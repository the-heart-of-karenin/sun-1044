> 辅助研究笔记。个别段落保留早期进度描述；本文的用途及后续主稿见 [阅读顺序](../docs/reading-guide.md)。

# 加权导数组合在中央K3上是除子类：Hodge论证草稿

2026-10-16。本文件补普通素数准对数引理所需的特定几何输入。使用标准的K3周期域、极化变分的半单性、Lefschetz(1,1)定理。下列有理结构核对不可省略；一个90/pi数值本身并不等于一个除子类证明。

## 1. 二形式的归一化与两参数族

原双平面族

w^2=xyz*[v((x+y+z)^3-324xy(x+y+z))-540xyz]

的H^2(O)切基是Cech类w/(xyz)。其Serre对偶二形式omega_v为常数倍dx wedge dy/w，常数不依赖v。

作[divisibility-inert-powers.md](divisibility-inert-powers.md)第1节的射影换元后，该族与

W^2=xy(1-x-y)*[xy(c-x-y)-b_0]

只差常数扭曲-540，c=1+3v/5，b_0=v/540。

更一般地置c=1-4a、b_0=4b。由

1-4b*(1+x+y)^3/(xy)-4a*(1+x+y)

的平方根周期及同一射影换元，二形式的一个周期是[proof-series.md](../proofs/proof-series.md)的F(a,b)，只差与a,b无关的常数。不存在依赖v的sqrt(v)正规化因子。

因此所需的几何类为

eta=103 omega+357(a nabla_a+b nabla_b)omega

在(a,b)=(-3/20,1/2160)的值。

## 2. 为何系列的PDE也是所需几何周期的PDE

这一步说明从一个常数项周期得到的PDE足以用于完整的秩4几何实现。

两参数椭圆K3模型的泛型纤维构型为2 IV*+3 I2+2 I1，并有截面P=(0,q-c+1)。平凡格加P给秩18子格，P高度1/3，行列式绝对值24。

这确实是二维K3模族。把两个IV*纤维规范到s=0、无穷，并把q=0的I2规范到s=-1（其他标记只有有限种选择）后，剩余I2与I1的位置分别恢复

(c-1)/b_0， c^3/b_0。

这两个有理函数对(c,b_0)的Jacobian为c^2(2c-3)/b_0^3，泛型非零。一个固定K3上的椭圆纤维类与截面类是离散的；固定这些类后，纤维方程的模不再有连续选择。因此遗忘纤维标记的K3模映射仍泛型有限。

秩18格极化K3的周期域维数2，故本族支配相应模曲面的开集。对秩18子格取原始闭包只引入有限种选择，不改变此维数论证。由K3算术周期域描述，泛型正交补T_0秩4。

具体使用Dolgachev, Mirror symmetry for lattice polarized K3 surfaces，第3节，尤其Theorem3.1、Proposition3.3及其后的算术商描述：固定格嵌入的模空间是周期域对正交整群的有限指数子群取商。本族的模映射泛型有限；在适当开集和有限水平覆盖上可使它有限etale，故单值像仍为有限指数。Borel稠密性给其Zariski闭包的连通分量为SO(T_0)，四维标准表示不可约。
https://arxiv.org/pdf/alg-geom/9502005

原环面周期来自一个整Betti循环，T_0投影非零。其解析延拓的循环轨道因不可约而张成T_0。[proof-series.md](../proofs/proof-series.md)的两条PDE为有理系数算子，已逐项证明消去原周期，所以也消去所有这些解析延拓。它们因此可用于整个T_0的Gauss--Manin实现。

永久的18个除子类与omega及其a,b导数都正交。故以下由PDE推出的向量恒等式不仅是一个解析支上的函数等式。

## 3. Noether--Lefschetz曲线上的分解

沿

a(r)=r(r+2)/(4(r^2-1))，
b(r)=-r^4/[16(r-1)^3(r+1)]，

[section-locus.md](section-locus.md)的Q截面使Picard数至少19。相应T_0分解为一个除子线和秩3的正交补T_3。

[proof-series.md](../proofs/proof-series.md)已证第三阶算子的解空间由

H(r)，tau(r)H(r)，tau(r)^2 H(r)

生成，其中H=f^2，tau是30级上半平面参数。
事实上Dr=G H，且G'/G=alpha，所以tau*f与f满足同一二阶方程；Wronskian是1/(2 pi i G)。其单值群含有限指数的Gamma_0(30)，对称平方表示不可约，故这些周期真的张成秩3部分。于是曲线上泛型Picard数恰为19。

记

Eomega=R_0 omega+R_1 nabla_a omega+R_2 nabla_b omega，

R_0=-16(r-2)(r-1)^3(r+1)，
R_1=-4(r-1)^2(r+2)(3r^2-2r-2)，
R_2=r^3(3r^2-8r+2)。

已证PDE计算给向量关系

nabla_r(Eomega)=lambda(r) Eomega，
lambda=-1/r+9/[2(r-1)]+3/[2(r+1)]。

所以Eomega生成单值至多为正负号的平坦线（或为零）。T_3不可约且秩3，故其在T_3的投影为零。Eomega属于上述除子线。

在r_0=1/4，直接线性代数给向量恒等式

eta=54 omega+(315/16)nabla_r omega-(448/135)Eomega。

最后一项已是除子类。沿这条曲线永久的19个除子类平坦且始终与omega正交，故nabla_r omega也在T_3中。下面只需处理前两项。

## 4. 秩3部分的有理结构

不能仅因写出了H、tau H、tau^2 H，就未经说明把这三个函数当成有理Betti基。

在这组解基中，Gamma_0(30)的单值矩阵为有理矩阵的对称平方；至多再乘有理的正负号角色。几何T_3自身也有有理Betti结构。两者复化后同构，而且表示绝对不可约。求交织映射是一组有理线性方程；既然复数上有可逆解，有理数上也有非零解，后者因不可约而可逆。由Schur引理，任意两个交织映射只差一个公共复数标量。

所以这组周期的投影有理结构就是标准Sym^2(Q^2)，至多有一个对三个坐标相同的标量。特别地，某个周期向量张成有理线，是可以在这三个坐标中检验的。

标准极化二次式为z_1^2-z_0 z_2，差一个非零标量；Hodge(2,0)线为

(1,tau,tau^2)，

Hodge(0,2)线为其共轭。Hodge(1,1)线因此为

(1,(tau+bar(tau))/2,tau*bar(tau))。

在tau_0=(15+i sqrt(105))/30，后一个向量是

(1,1/2,11/30)，

为有理向量。Lefschetz(1,1)定理给中央曲面一个新的有理除子类。因此中央Picard数为20，且该秩3部分的Hodge(1,1)线就是这个除子线。

## 5. 待证组合恰好在该除子线上

置k=315/16、G_0=sqrt(105)/32。G_0的正号由r从0到1/4的原周期支确定。[proof-series.md](../proofs/proof-series.md)的CM计算给

54H(r_0)+k H'(r_0)=90/pi。

由于d tau/dr=1/(2 pi i G H)，54omega+k nabla_r omega的三个周期坐标，乘以pi并除去前述共同常数后，依次是

90，
90 tau_0+k/(2 i G_0)，
90 tau_0^2+2tau_0*k/(2 i G_0)。

它们等于

(90,45,33)=90*(1,1/2,11/30)。

因此这个组合就在第4节的除子线上。第3节的Eomega项也是除子类，所以eta属于NS(X_C) tensor C。

eta由代数de Rham类及有理系数Gauss--Manin导数构成，定义在Qbar上。除子Chern类同样在Qbar上定义；在有限维Qbar向量空间中作线性代数，可将上述系数取在Qbar中。故对任一p进嵌入，eta仍是代数除子Chern类的线性组合，可用于[divisibility-ordinary-lemma.md](divisibility-ordinary-lemma.md)。

此处不要求构造7次对应在整个形式Brauer群上的整模型；也没有把复数周期公式直接视为p进级数求和公式。

## 核验

[divisibility-tate-certificate.py](../scripts/divisibility-tate-certificate.py)核验第2节Jacobian、第3节的三项向量系数及第5节的(90,45,33)，约0.15秒。
深层输入是K3格极化模空间的周期域与单值性、极化变分的半单性、Lefschetz(1,1)及普通晶体/形式Brauer比较；这些不能用有限Taylor展开来替代。
