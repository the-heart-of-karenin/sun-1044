> 辅助研究笔记。个别段落保留早期进度描述；本文的用途及后续主稿见 [阅读顺序](../docs/reading-guide.md)。

# 级数问题：已证解析约化

2026-10-15。此文件给出生成函数和微分方程的证明，不声称已完成 $90/\pi$ 的特殊值计算。

令
$$
A_n(t)=\sum_{k=0}^n\frac{(n+2k)!}{(n-k)!k!^3}t^{n-k},
\quad G_t(u)=\sum_{n\ge0}A_n(t)u^n,
\quad F_t(z)=\sum_{n\ge0}\binom{2n}n A_n(t)z^n.
$$
本题为 $t=-324$、$z_0=1/2160$，目标是
$$
(357\theta+103)F_{-324}(z_0)=90/\pi,
\qquad \theta=z\frac{d}{dz}.
$$

## 1. 内层生成函数及收敛性

令 $H(v)={}_2F_1(1/3,2/3;1;v)$。逐项展开得
$$
G_t(u)=\frac{1}{1-tu}H\!\left(\frac{27u}{(1-tu)^3}\right).
$$
详细的重排证明和原级数绝对收敛证明见 [research-notes.md](../archive/research-notes.md) 第 1、2 节。

## 2. 已证定理：一个四阶微分方程

定义以下关于 $h$ 的多项式：
$$
\begin{aligned}
R_0(h)&=-h^3(h-1),\\
R_1(h)&=2h\big((11t+54)h^3+(-t+81)h^2+(7t+39)h+t+6\big),\\
R_2(h)&=-12t(2h+1)\big((7t+45)h^3+7th^2+(6t-5)h+2t\big),\\
R_3(h)&=8t^3(2h+1)(2h+3)(17h^2+24h+12),\\
R_4(h)&=-80t^4(h+1)(2h+1)(2h+3)(2h+5).
\end{aligned}
$$
则
$$
\boxed{\mathcal L_4 F_t=0,\qquad \mathcal L_4=\sum_{j=0}^4z^jR_j(\theta).}
$$
这里规定 $z^jR_j(\theta)$ 先对函数施加 $R_j(\theta)$，再乘 $z^j$。所有算子乘积均为复合，不能将 $z$ 与 $\theta$ 当作可交换量。

### 证明

Gauss 方程为
$$
v(1-v)H''+(1-2v)H'-\frac29 H=0.
$$
将 $v=27u/(1-tu)^3$、$G_t=(1-tu)^{-1}H(v)$ 代入。记 $\vartheta=u\,d/du$，得到
$$
\mathcal P G_t=0,\qquad \mathcal P=\sum_{j=0}^4u^jP_j(\vartheta),
$$
其中
$$
\begin{aligned}
P_0(h)&=-h^2,\\
P_1(h)&=(t+27)h^2+(5t+27)h+t+6,\\
P_2(h)&=3t\big((t+18)h^2-2th-t-2\big),\\
P_3(h)&=-t^3h(5h+3),\\
P_4(h)&=2t^4(h+1)^2.
\end{aligned}
$$
因此 $A_n(t)$ 满足
$$
\sum_{j=0}^{\min(4,n)}P_j(n-j)A_{n-j}(t)=0.
$$
置 $b_n=\binom{2n}n A_n(t)$。利用
$$
\frac{\binom{2n}n}{\binom{2(n-j)}{n-j}}
=4^j\frac{(n-j+1/2)_j}{(n-j+1)_j},
$$
将上述递推乘以 $n(n-1)(n-2)\binom{2n}n$，得到
$$
\mathcal L_5F_t=0,\qquad
\mathcal L_5=\sum_{j=0}^4z^jQ_j(\theta),
$$
其中
$$
Q_j(h)=4^jP_j(h)\frac{(h+1/2)_j(h+j)(h+j-1)(h+j-2)}{(h+1)_j}.
$$
这些表达式约去因子后都是多项式。在 $n=0,1,2$ 处也可直接检查相应的系数关系成立。

直接展开可验证以下**算子恒等式**：
$$
\boxed{(1-10tz)\mathcal L_5
=\big((1+8tz)\theta-2(1+2tz)\big)\mathcal L_4.}
$$
因此 $g=\mathcal L_4F_t$ 满足
$$
(1+8tz)zg'-2(1+2tz)g=0,
$$
故在原点邻域
$$
g=C\,z^2(1+8tz)^{-3/2}.
$$
由
$$
b_0=1,\quad b_1=2(t+6),\quad b_2=6(t^2+24t+90)
$$
可算出
$$
[z^2]g=-8b_2+36(t+10)b_1-24t^2b_0=0.
$$
所以 $C=0$，定理得证。上述 Gauss 方程代入和算子恒等式的独立代数核验保存在 [ode-certificate.py](../scripts/ode-certificate.py)。该核验运行约 0.3 秒。

### 原题参数下的方程

在 $t=-324$ 处，将算子整体乘以 $-1$，得到
$$
\begin{aligned}
0={}&\big[\theta^3(\theta-1)
+6z\theta(1170\theta^3-135\theta^2+743\theta+106)\\
&+3888z^2(2\theta+1)(2223\theta^3+2268\theta^2+1949\theta+648)\\
&+272097792z^3(2\theta+1)(2\theta+3)(17\theta^2+24\theta+12)\\
&+881596846080z^4(\theta+1)(2\theta+1)(2\theta+3)(2\theta+5)\big]F_{-324}(z).
\end{aligned}
$$
其 $\theta^4$ 系数为
$$
(1+864z)(1+3240z)(1+2916z+2519424z^2).
$$
这给出了可复核的微分方程；尚未证明它是最小阶方程，也尚未完成其函数分解和特殊值计算。

## 3. 已证的常数项表示

$\operatorname{CT}_{x,y}$ 表示取 $x^0y^0$ 的系数。先按 $z$ 展开，再在每个系数中按 $x,y$ 展开，有
$$
A_n(t)=\operatorname{CT}_{x,y}\frac{(t+1/(xy))^n}{(1-x-y)^{n+1}}.
$$
因此
$$
\boxed{F_t(z)=\operatorname{CT}_{x,y}
\frac{1}{\sqrt{(1-x-y)(1-x-y-4tz-4z/(xy))}}.}
$$
平方根取在 $z=0$ 给出 $1-x-y$ 的支。

等价地，根号内乘以 $(xy)^2$，会出现六次多项式
$$
P_{t,z}(x,y)=xy(1-x-y)\big(xy(1-x-y-4tz)-4z\big).
$$
该式给出几何研究的明确入口，但仅有此常数项表示还不足以证明任何复乘分解。

## 4. 尚缺少的关键一步

需要把上述四阶方程的特定解与可求值的椭圆周期或其他周期建立严格关系，并在 $z_0$ 处处理一阶导数组合。四阶方程、绝对收敛性和高精度数值吻合，均不能单独推出 $(357\theta+103)F_{-324}(z_0)=90/\pi$。
