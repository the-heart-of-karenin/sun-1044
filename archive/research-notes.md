> 历史记录。文中的进度判断和待办反映写作时的状态；当前状态见 [项目说明](../README.md)。

# 孙智伟猜想 10.44(i)、(iv)：研究记录

研究开始：2026-10-15。本文区分已证推导、文献陈述与待证步骤。局部数值检验不作为证明。按用户要求，避免长时间或后台计算。

## 0. 目标与状态

令
$$
A_n=\sum_{k=0}^n\binom nk\binom{n+2k}{2k}\binom{2k}k(-324)^{n-k},
\qquad F(z)=\sum_{n\ge0}\binom{2n}n A_nz^n.
$$

首先研究
$$
(357zF'(z)+103F(z))\big|_{z=1/2160}=90/\pi.
$$
然后研究同一系数的模素数平方截断和。**2026-10-16最新续研：第一题、完整九分支超同余、加权超同余，以及最后的全部正整数整除断言，现均已形成完整证明草稿。新整除主稿见[divisibility-proof.md](../proofs/divisibility-proof.md)，自审见[divisibility-audit.md](../review/divisibility-audit.md)。均尚未接受外部同行审阅。旧笔记中的未闭合状态按[remaining-work.md](remaining-work.md)更新。**

已保存的可继续使用的结果：

- [divisibility-proof.md](../proofs/divisibility-proof.md)、[divisibility-audit.md](../review/divisibility-audit.md)：本次续研的新完整整除证明与自审，包含普通、惰性及特殊素数的所有幂。
- [divisibility-tate-class.md](../lemmas/divisibility-tate-class.md)、[divisibility-ordinary-lemma.md](../lemmas/divisibility-ordinary-lemma.md)：加权导数组合的除子类识别，以及高度1整同构/相对晶体比较。
- [divisibility-inert-powers.md](../lemmas/divisibility-inert-powers.md)：判别式60子格、Artin不变量1及全阶一阶变形论证。
- [nine-branches-proof.md](../proofs/nine-branches-proof.md)：完整九分支证明研究稿。有限二次同余、Hecke乘积、有理函数刚性、CM特殊化及惰性分支。
- [nine-branches-audit.md](../review/nine-branches-audit.md)：针对特征p积分常数、极点界、定理假设、CM特殊化的逐点自审。
- [global-isotropy.md](../lemmas/global-isotropy.md)、[finite-isotropy.md](../lemmas/finite-isotropy.md)：全曲线模p²二次恒等式及截断边界证明。
- [generic-product-certificate.py](../scripts/generic-product-certificate.py)、[curve-isotropy-certificate.py](../scripts/curve-isotropy-certificate.py)：全参数的精确四阶算子及曲线二次型证书，分别约0.3秒。
- [transverse-congruence.md](../lemmas/transverse-congruence.md)：加权问题横向误差项的完整模p²求值，使用已证Franel同余确定一个边界常数。
- [weighted-wronskian-proof.md](../proofs/weighted-wronskian-proof.md)、[weighted-wronskian-audit.md](../review/weighted-wronskian-audit.md)：用7次对应的Wronskian完成全部普通、惰性加权分支，p=7另核验。
- [weighted-ordinary-proof.md](weighted-ordinary-proof.md)：此前只处理普通素数的证明，保留供比对。
- [divisibility-reduction.md](../lemmas/divisibility-reduction.md)：完整整除断言等价于(2n+1)|R_n；已证全部3进部分与所有素数的一阶整除。
- [divisibility-brauer-reduction.md](../lemmas/divisibility-brauer-reduction.md)：新等价条件(2n+1)|(151beta_n+192780beta_(n-1))，固定双平面形式Brauer对数与准对数引理。
- [divisibility-five-adic.md](../lemmas/divisibility-five-adic.md)、[divisibility-seven-seventeen.md](../lemmas/divisibility-seven-seventeen.md)：新的全部5进、7进、17进部分证明草稿。
- [remaining-work.md](remaining-work.md)：本轮完成状态与下一步明确断点。

- [proof-series.md](../proofs/proof-series.md)：目前的主要结果。证明原级数约化到 30 级模函数，独立构造七次模方程并证明复乘特殊值，最终得到 $90/\pi$。外部输入明确限于标准的 30 级模参数化，并列出出处。
- [nl-certificate.py](../scripts/nl-certificate.py)、[bivariate-period.py](../scripts/bivariate-period.py)：两条偏微分方程、参数曲线上一阶导数关系与二阶平方约化的精确代数证书；运算约 0.2–0.4 秒。
- [modular7-certificate.py](../scripts/modular7-certificate.py)、[modular7-polynomial.txt](../data/modular7-polynomial.txt)、[cm-certificate.py](../scripts/cm-certificate.py)：七次模方程、先验 128 次极点界所需的精确展开、复乘选根及导数计算；各次运算均不到一秒。
- [section-locus.md](../lemmas/section-locus.md)：通向上述约化的显式截面及参数曲线；保留为第二题的几何线索。
- [analytic-reduction.md](../lemmas/analytic-reduction.md)：已证生成函数、绝对收敛性、四阶微分方程及精确算子证书、常数项表示。
- [product-decomposition.md](../lemmas/product-decomposition.md)：第二轮新结果，已证 $F_{-324}(x/108)=f_+(x)f_-(x)$，给出两个二阶方程、初值和延拓约定；特殊值仍待证明。
- [quadratic-forms.md](../lemmas/quadratic-forms.md)：用二次型约化证明八行表示的存在性与分类完整性；用一个行列式界直接证明表示选择无关。另附属理论背景。
- [finite-sum-reduction.md](../lemmas/finite-sum-reduction.md)：已证模 $p$ 单一多项式系数表示，以及模 $p^2$ 前后半段的必要修正。
- [geometric-exploration.md](geometric-exploration.md)：常数项曲面的可逆有理换元与显式椭圆纤维模型；单独标记尚未完成的判别式 24 方向。
- [ode-certificate.py](../scripts/ode-certificate.py)：精确代数核验（约 0.3 秒），无后台任务。
- [short-ode-check.py](../scripts/short-ode-check.py)：曾用于发现四阶方程的有界模线性代数计算（约 0.02 秒）；发现性检验已由精确证书取代，不需要反复运行。
- [verify-short.py](../scripts/verify-short.py)：九个小素数例子和三个模 $p$ 多项式系数核验；无大规模素数扫描。

## 1. 已证引理：内层和的生成函数

暂令
$$
A_n(t)=\sum_{k=0}^n\binom nk\binom{n+2k}{2k}\binom{2k}k t^{n-k}.
$$
直接约去阶乘，得到
$$
\binom nk\binom{n+2k}{2k}\binom{2k}k
=\frac{(n+2k)!}{(n-k)!k!^3}.
$$
置 $m=n-k$。在形式幂级数意义下（每个系数只含有限项），
$$
\begin{aligned}
G_t(u)&:=\sum_{n\ge0}A_n(t)u^n\\
&=\sum_{k,m\ge0}\frac{(m+3k)!}{m!k!^3}t^m u^{m+k}\\
&=\sum_{k\ge0}\frac{(3k)!}{k!^3}\frac{u^k}{(1-tu)^{3k+1}}\\
&=\frac1{1-tu}\,{}_2F_1\!\left(\frac13,\frac23;1;\frac{27u}{(1-tu)^3}\right).
\end{aligned}
$$
这里 ${}_2F_1(a,b;1;v)=\sum_{k\ge0}(a)_k(b)_kv^k/(k!)^2$，$(a)_k$ 为上升阶乘，并用了
$(3k)!/(k!^3)=27^k(1/3)_k(2/3)_k/(k!)^2$。

因此原序列满足
$$
\boxed{G_{-324}(u)=\frac1{1+324u}\,{}_2F_1\!\left(\frac13,\frac23;1;\frac{27u}{(1+324u)^3}\right).}
$$

注意：这是 $A_n$ 的生成函数，尚不是含中央二项式系数的 $F$。直接把此式当作 $F$ 会遗漏关键的一步。

## 2. 已证引理：原级数绝对收敛

令 $B_n=A_n(324)\ge0$。由逐项三角不等式，$|A_n|\le B_n$，且 $\binom{2n}n\le4^n$。在 $u_0=1/540$ 处，
$$
324u_0=3/5,\qquad \frac{27u_0}{(1-324u_0)^3}=\frac{25}{32}<1.
$$
上述 $G_{324}$ 公式在 $u_0$ 的某个邻域解析，且系数非负。因此
$$
\sum_{n\ge0}(357n+103)\binom{2n}n |A_n|2160^{-n}
\le 357u_0G_{324}'(u_0)+103G_{324}(u_0)<\infty.
$$
这也允许在 $z=1/2160$ 的邻域逐项微分以及在绝对收敛范围内交换双重求和。

## 3. 文献入口与核查边界

- 孙智伟，MathOverflow 原帖，公式 (3)：<https://mathoverflow.net/questions/369569/two-curious-series-for-1-pi>。2026-10-15 读取的页面仍称其为猜想，未见完整回答；不能据此断言全部后续文献均未解决。
- 孙智伟，*Open Conjectures on Congruences*，2011 v59：<https://arxiv.org/abs/0911.5665>。
- 孙智伟，*List of conjectural series for powers of pi and other constants*，arXiv:1102.5649：<https://arxiv.org/abs/1102.5649>。需核对公式与后续引用。
- Almkvist–Aycock，附录 Meurman，*Proof of some conjectured formulas for 1/pi by Z.-W. Sun*，arXiv:1112.3259：<https://arxiv.org/abs/1112.3259>。已检索其 HTML 中 2160、357，未直接找到本题公式；不能将该论文标题当成本题已获证明的证据。

## 4. 待推进

1. 对第一题的完整证明草稿作人工复核，尤其是所有外部模函数输入、解析路径和模方程的极点界；不作发表优先权判断。
2. 对超同余寻找可在模 $p^2$ 保持的有限变换；不能直接截断现已得到的无穷解析变换。

### 第二题继续研究后的新增结果

- [toric-period.md](../lemmas/toric-period.md)：已证A_n(t)及完整系数的Laurent多项式常数项模型；Newton多面体为反射多面体。另记录为何现有Beukers定理与Dwork晶体结果不能直接当成本题模p²证明。
- [hasse-invariant.md](../lemmas/hasse-invariant.md)：已证Hasse不变量平方表达式，推出对所有p>7，S_p模p消失当且仅当(-105/p)=-1。惰性p!=17时，双变量截断和的一阶偏导数也都模p消失；p=17的退化已明确列出。
- [cm-eight-branches.md](../lemmas/cm-eight-branches.md)：已证30级权2周期的Atkin–Lehner字符，给出八行二次型的统一复乘单位因子，并精确核对其模p²展开就是原表右侧。**截断和与此因子的模p²比较仍待证明，因此八分支不能标为已证。**
- [frobenius-probe.py](../scripts/frobenius-probe.py)：只用于有限发现的短时形式级数探测。候选B_p(r(q))*H(q^p)=H(q) (modp²)在选定小素数及有界展开中成立；尚无对任意素数和全部系数的证明。

上面这一批是2026-10-15的历史状态。2026-10-16已由 [nine-branches-proof.md](../proofs/nine-branches-proof.md) 填补模p²比较并覆盖全部九分支；转入另两个断言。新增运算均为短时前台计算，没有启动后台任务或大规模搜索。

## 5. 直接相关的后续文献（重要）

van Hoeij–Tsai–Ye, *The Modularity of Z.-W. Sun's Conjectural Formulas for 1/pi*, arXiv:2410.19289v2 (2024-11-02)：
<https://arxiv.org/html/2410.19289#S4>。

第 4 节的 Conjecture 4.1 定义的 $U(t;x,b)$ 正是本题系列；其 (4.3) 为
$$
U(1/2160;-324,103/357)=30/(119\pi),
$$
乘以 357 即本题。作者在该节说明尚未得到 $U(t;x)$ 的分解公式。因此该文前面证明其他系列的主定理不能直接当成本题的证明。这只是截至该文版本的状态信息，并非对截至 2026-10-15 所有论文的穷尽核查。

相关方法资料：van Hoeij–van Straten–Zudilin, *A hyperelliptic saga on a generating function of the squares of Legendre polynomials*, arXiv:2306.04921，<https://arxiv.org/html/2306.04921>。其对象与本题不同，不应把该文的超椭圆积分分解自动套用于本题。

## 6. 当前断点与计算记录

此前断点已被第一题及九分支的新证明推进：见 [proof-series.md](../proofs/proof-series.md) 与 [nine-branches-proof.md](../proofs/nine-branches-proof.md)。

最优先的下一项工作现为 [remaining-work.md](remaining-work.md) 中的惰性加权导数与整除的高次幂问题。30级变换的模p²有限版本已在九分支证明中建立；判别式24的泛型格计算仍未完成，本轮两道主要证明均不依赖它。

短时精确数值核验选择的九个素数为 $109,53,47,19,41,13,43,11,17$，依原表八行和最后消失分支排列。它们的 $S_p$ 最小非负剩余分别为
$$
11679,\ 2705,\ 46,\ 32,\ 1679,\ 153,\ 26,\ 113,\ 0.
$$
这些有限例子仅用作转录核对。精确算子证书的运算约 0.3 秒，小素数与新多项式约化核验约 0.02 秒；没有启动持续运行的后台计算。
