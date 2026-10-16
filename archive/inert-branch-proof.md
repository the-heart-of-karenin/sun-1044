> 历史记录。文中的进度判断和待办反映写作时的状态；当前状态见 [项目说明](../README.md)。

# 九分支中的惰性分支：模 p² 的证明

2026-10-16。结论：对每个素数 p>7，若 (-105/p)=-1，则原题 S_p=0 (mod p²)。八个分裂分支尚不包括在此结论中。

后续加强：[global-isotropy.md](../lemmas/global-isotropy.md) 已将第2节的有限二次同余提升为全r的有理函数同余，包含全部p>7。因此本文件第3节的17、331有限计算已非证明必需。完整九分支证明稿现见 [nine-branches-proof.md](../proofs/nine-branches-proof.md)。

## 1. 二重零点实际恰为二重

[hasse-invariant.md](../lemmas/hasse-invariant.md) 已证明，在 r0=1/4 的复乘点附近，

H_p(r) H(r)^(p-1)=Ha(r)² (mod p)，

Ha 为椭圆曲线的 Hasse 不变量，H 为在本点非零的权2周期。

当 (-105/p)=-1，Deuring 判别表明该点超奇异。Hasse 不变量在模曲线的超奇异点处具有简单零点；这里在 p>7 处为好约化，30级的自然标记不会引入 p 阶分歧。

还需检查 r 在本点确为局部参数。由 [proof-series.md](../proofs/proof-series.md) 的 DX=X sqrt(G) Z 以及 r=-2X/(1+2X)、H=(1+4X)Z，

(Dr)/H=-2X sqrt(G)/[(1+2X)²(1+4X)]。

本点 X=-1/10，G=189/500，所有可能为零或为极点的因子仅涉及 2,3,5,7。因此 p>7 时此比值为单位。于是 Ha 对 r 的一阶零点仍为一阶，H_p 恰为二重零点，即

H_p(r0)=H_p'(r0)=0 (mod p)，H_p''(r0) !=0 (mod p)。

这里没有从“至少二重”跳到“恰好二重”；额外使用了 Hasse 除子的单性与局部参数检查。

## 2. 用有限二次恒等式增加一阶精度

当 p 不等于17、331，[finite-isotropy.md](../lemmas/finite-isotropy.md) 第4节给出

H_p H_p''-(H_p')²/2+alpha H_p H_p'+2beta H_p²=0 (mod p²)

在 r0 成立。alpha,beta 在 r0 的分母对 p>7 均为单位。

后三项因 H_p、H_p' 各被 p 整除而为0模p²，故 H_p(r0) H_p''(r0)=0 (mod p²)。由于 H_p''(r0) 为单位，得到

S_p=H_p(r0)=0 (mod p²)。

## 3. p=17、331 的例外是有限计算，不影响一般论证

上面的四维有理消元在 p=17、331 处退化，须另查。两者均满足 (-105/p)=-1。直接在 Z/289Z、Z/109561Z 中计算题目的有限和分别为0，独立处理这两个素数。

[inert-exception-certificate.py](../scripts/inert-exception-certificate.py) 直接使用原定义中的三个二项式系数、整数幂与2160的模逆元；没有调用微分方程或所要证明的同余。两例合计不到1秒。这是两个明确整数同余的有限验证，并非对一般素数的抽样。

因此惰性分支对所有 p>7 成立。

## 证明输入的范围

代数部分是原系数递推、有限截断边界的 p² 整除、二次不变量及点上的精确有理矩阵恒等式。标准几何输入仅为 Hasse 不变量的简单超奇异零点、模形式的 q 展开原理、Deuring 的 CM 约化判别。没有将一般的普通单位根定理套用于惰性素数。
