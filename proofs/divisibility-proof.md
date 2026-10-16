# 整数整除性的证明草稿

本稿组装对所有正整数的整除性论证；具体引理分别保存在所链接的辅助笔记中。初稿日期为 2026-10-16；审阅状态与 AI 参与情况见 [项目说明](../README.md)。

## 命题

令

$$
A_k=\sum_{j=0}^{k}\binom kj\binom{k+2j}{2j}\binom{2j}{j}(-324)^{k-j},
\qquad
T_n=\sum_{k=0}^{n-1}(357k+103)2160^{n-1-k}\binom{2k}{k}A_k.
$$

则对每个整数 $n\ge1$，

$$
n\binom{2n-1}{n-1}\mid T_n.
$$

## 1. 形式级数约化

令

$$
G(z)=\sum_{k\ge0}A_kz^k,\qquad B(z)=(1-540z)^{-1/2},
$$

并定义

$$
R(z)=B(z)\bigl(357zG'(z)+103G(z)\bigr)=\sum_{k\ge0}R_kz^k.
$$

[奇数分母约化](../lemmas/divisibility-reduction.md) 由原有限和的递推得到：命题等价于对所有 $k\ge0$ 有 $(2k+1)\mid R_k$。

再令

$$
g=\frac{(1+x+y)^3}{xy}-324(1+x+y),\qquad
\beta_k(v)=\operatorname{CT}_{x,y}(vg-540)^k,
$$

$$
\ell_v(u)=\sum_{k\ge0}\frac{\beta_k(v)}{2k+1}u^{2k+1},\qquad
J(u)=\left[103\ell_v(u)+357v\partial_v\ell_v(u)\right]_{v=1}.
$$

[形式 Brauer 对数约化](../lemmas/divisibility-brauer-reduction.md) 给出

$$
J\left(\frac{t}{\sqrt{1-540t^2}}\right)
=\sum_{k\ge0}\frac{R_k}{2k+1}t^{2k+1}.
$$

该坐标变换及其逆都有整数系数，首项系数为 $1$。因此只需证明 $J\in\mathbb Z[[u]]$。

上述 $\ell_v$ 是双平面

$$
X_v:\quad w^2=xyz\left[v\left((x+y+z)^3-324xy(x+y+z)\right)-540xyz\right]
$$

的形式 Brauer 对数。固定 Čech 切基 $w/(xyz)$，其 Serre 对偶二形式 $\omega_v$ 的常数归一化与 $v$ 无关。

## 2. 普通素数

设 $p>7$ 且 $\left(\frac{-105}{p}\right)=1$。[九分支主稿](nine-branches-proof.md) 的模 $p$ 结果给出 $\beta_{(p-1)/2}(1)\ne0$，所以 $X_1$ 的约化普通。分支三次曲线在这些素数处光滑；只有 $7,17$ 可能出现额外节点，而 $17$ 属于惰性分支。固定的 $A_5$ 与 $A_1$ 点有同时消解，因此可在 $v=1$ 的一阶邻域用光滑 K3 族计算形式 Brauer 群。

[除子类识别](../lemmas/divisibility-tate-class.md) 给出

$$
\eta=103\omega+357\left.\nabla_{v\partial_v}\omega\right|_{v=1}
$$

是中央 K3 曲面上代数除子 Chern 类的 $\overline{\mathbb Q}$ 线性组合。该笔记分别处理两参数格极化 K3 族、完整秩四周期的偏微分方程、30 级秩三部分的 Betti 有理结构，以及复乘点的加权周期向量。最后的向量为 $(90,45,33)/\pi$，位于有理 Hodge $(1,1)$ 线上。

应用 [普通整性引理](../lemmas/divisibility-ordinary-lemma.md)。高度一形式群的整同构 $h_v:F_v\to\widehat{\mathbb G}_m$ 给出

$$
\left.\partial_v\ell_v\right|_{v=1}=\lambda\ell_1+I(u),
\qquad I(u)\in W(\overline{\mathbb F}_p)[[u]].
$$

Nygaard–Ogus 相对晶体比较将 $\lambda$ 识别为水平单位根周期的对数导数，所用版本及 Hodge 交换图见 Inoue Theorem 3.1。由于 $\eta$ 是除子类，斜率为 $1$，它与斜率 $0$ 的单位根线正交。因此

$$
103+357\lambda=0.
$$

于是 $J=357I$ 在上述扩张后为整系数；原系数又属于 $\mathbb Q_p$，故 $J\in\mathbb Z_p[[u]]$。这一结论控制所有次数。

## 3. 惰性素数

设 $p>7$ 且 $\left(\frac{-105}{p}\right)=-1$，暂除去 $p=17$。[惰性素数引理](../lemmas/divisibility-inert-powers.md) 采用如下论证。

平凡格与两个显式截面给出判别式为 $60$ 的秩十九子格。Hasse 不变量为零，结合 Picard 数与高度的不等式，得到超奇异约化；上述非退化子格进一步迫使 Artin 不变量为 $1$。

对超特殊 K3 曲面，所有高阶恰当形式的 $H^1(B_m)$ 在 $H^1(\Omega^1)$ 中的像均为零。逐阶应用水平的高阶 Hasse 构造，得到任意光滑一阶变形的形式 Brauer 群满足 $[p]=0$。对 $v=1+\epsilon$ 应用这一结论，再使用整对数引理，得到

$$
\ell_{1+\epsilon}(u)\in
\bigl(W(\overline{\mathbb F}_p)[\epsilon]/(\epsilon^2)\bigr)[[u]].
$$

其常数项与 $\epsilon$ 项分别为 $\ell_1$ 与 $\left.\partial_v\ell_v\right|_{v=1}$，均为 $p$ 整，故 $J$ 为 $p$ 整。这里使用整个 $p$ 级数，而不是将一阶模 $p$ 同余直接迭代。$p=17$ 不在这一同时消解论证内，下一节单独处理。

## 4. 特殊素数

- **$p=2$：** $J$ 的显式系数只有奇数分母，因而自动 $2$ 整。
- **$p=3$：** [奇数分母约化](../lemmas/divisibility-reduction.md) 给出 $v_3(R_k)\ge s_3(k)$。若 $3^r\mid2k+1$，则 $k$ 的末 $r$ 位三进制数字均为 $1$，所以 $s_3(k)\ge r$。
- **$p=5$：** [五进引理](../lemmas/divisibility-five-adic.md) 使用中央约化的 $2D_6+A_3+3A_1$ 构型，得到 Picard 数至少为十九，结合 Hasse 为零得到形式群高度无穷。模 $5$ 时，$v=1+\epsilon$ 的变形仅为平方单位扭曲，整个一阶族满足 $[p]=0$，所以对数及参数导数同时 $5$ 整。
- **$p=7,17$：** [七进与十七进引理](../lemmas/divisibility-seven-seventeen.md) 处理中央约化的有理双点消解，并得到高度无穷，因此 $\ell_1$ 为整系数。参数导数是准对数；具有整对数的形式群上，任意准对数乘以 $p$ 都整。再由 $p\mid357$ 得到 $J$ 整。

特殊素数的论证直接在原整形式群上使用模 $p$ 为零的 $p$ 级数，没有将有限扩张的极大理想代替理想 $(p)$。

## 5. 还原整除性

$J$ 的每个系数是有理数，且在每个素数处都整，因而 $J\in\mathbb Z[[u]]$。通过第 1 节的整数坐标变换和有限和递推，得到对所有 $n\ge1$，

$$
\frac{T_n}{n\binom{2n-1}{n-1}}\in\mathbb Z.
$$

证毕。

## 依赖与审阅入口

普通部分依赖 [除子类识别](../lemmas/divisibility-tate-class.md) 和 [相对晶体比较引理](../lemmas/divisibility-ordinary-lemma.md)；惰性部分依赖 [超特殊变形引理](../lemmas/divisibility-inert-powers.md)。这些步骤使用 K3 周期域、格极化模空间、Lefschetz $(1,1)$ 定理、Shioda 高度公式、形式 Brauer 群的 Cartier 实现及高阶 Hasse 构造。

此前的内部自审见 [整除性自审记录](../review/divisibility-audit.md)，标准文献见 [参考文献](../docs/references.md)。
