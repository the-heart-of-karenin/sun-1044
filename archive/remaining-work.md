> 历史记录。文中的进度判断和待办反映写作时的状态；当前状态见 [项目说明](../README.md)。

# 2026-10-16 最新续研状态：四项均已有完整证明草稿

本页开头为最新状态；后半保留此前的研究状态，旧的“尚缺”描述已由本次主稿替代。所有稿件目前只有本工作区内自审，尚无独立同行审阅。

## 当前主稿

1. 90/pi级数：[proof-series.md](../proofs/proof-series.md)，[proof-audit.md](../review/proof-audit.md)。
2. 无权九分支模p^2：[nine-branches-proof.md](../proofs/nine-branches-proof.md)，[nine-branches-audit.md](../review/nine-branches-audit.md)。
3. 加权超同余，全部p>5：[weighted-wronskian-proof.md](../proofs/weighted-wronskian-proof.md)，[weighted-wronskian-audit.md](../review/weighted-wronskian-audit.md)。
4. 所有正整数n的整除断言：[divisibility-proof.md](../proofs/divisibility-proof.md)，[divisibility-audit.md](../review/divisibility-audit.md)。本次续研新完成。

## 整除命题新证明的结构

精确整坐标变换先把原断言等价为固定双平面形式Brauer准对数J的整性。

- 普通素数：[divisibility-tate-class.md](../lemmas/divisibility-tate-class.md)识别加权导数组合为除子类；[divisibility-ordinary-lemma.md](../lemmas/divisibility-ordinary-lemma.md)用高度1整同构及Nygaard--Ogus相对晶体/Lie比较，精确消掉对数部分，一次控制所有幂。
- 惰性素数：[divisibility-inert-powers.md](../lemmas/divisibility-inert-powers.md)用两个截面的高度给判别式60的秩19子格，强迫Artin不变量1，再用所有高阶Hasse的水平性控制一阶形式群的整个p级数。
- 2、3、5、7、17沿用先前的独立局部论证；17未被无条件放进一阶同时消解步骤。

此前计划构造的7次CM对应在整个整形式Brauer群上的模型仍未构造；本轮证明通过Hodge除子类及相对晶体比较绕过了这一步。

## 审阅入口

[divisibility-audit.md](../review/divisibility-audit.md)列出本轮核对点。独立审阅尤其应检查：两参数K3模族的泛型有限性及单值性、秩3周期的Betti有理结构、对偶二形式归一化、Inoue Theorem3.1交换图的使用，以及超特殊一阶变形的全m归纳。

新精确证书[divisibility-inert-certificate.py](../scripts/divisibility-inert-certificate.py)、[divisibility-tate-certificate.py](../scripts/divisibility-tate-certificate.py)各约0.1--0.2秒；另仅取普通p=11的三个幂作符号旁证，约0.03秒。没有大规模搜索、后台进程或定时工作。

2019年已核验猜想39的三项及独立90/pi级数，现均有完整证明草稿。版本和悬赏范围仍见[bounty-scope.md](../docs/bounty-scope.md)；不认定发表优先权、奖金当前有效性或悬赏方接受情况。

---

# 此前一轮研究状态与当时断点（历史记录）

## 已完成

1. 原90/pi恒等式：[proof-series.md](../proofs/proof-series.md)（此前完成并审计）。
2. 无权九分支模p²：[nine-branches-proof.md](../proofs/nine-branches-proof.md)。包含八个分裂表示及全部惰性p>7，没有17、331例外。[nine-branches-audit.md](../review/nine-branches-audit.md)为自审记录。尚未接受外部同行审阅。
3. 加权问题的横向项E_p：[transverse-congruence.md](../lemmas/transverse-congruence.md)给出全r、全p>7的显式模p²公式。
4. 加权同余的全部素数p>5：[weighted-wronskian-proof.md](../proofs/weighted-wronskian-proof.md)给出新的完整证明草稿，[weighted-wronskian-audit.md](../review/weighted-wronskian-audit.md)为自审。使用7次对应的Wronskian处理惰性素数，无需普通单位根；p=7按原定义另已核验。尚无外部同行审阅。
5. 整除命题的等价奇数分母约化，以及全部3进部分、所有素数的一阶整除：[divisibility-reduction.md](../lemmas/divisibility-reduction.md)。
6. 新固定双平面/形式Brauer对数约化：[divisibility-brauer-reduction.md](../lemmas/divisibility-brauer-reduction.md)；由此得到全部5进、7进和17进部分，见[divisibility-five-adic.md](../lemmas/divisibility-five-adic.md)及[divisibility-seven-seventeen.md](../lemmas/divisibility-seven-seventeen.md)。新几何及形式群证明仍未经外部审阅。

## 加权问题的新进展

此前缺少的惰性导数同余为

P_p'(1/4)=(96/35)p*(-1/p) (modp²)。

[weighted-wronskian-proof.md](../proofs/weighted-wronskian-proof.md)现通过以下步骤给出证明：先由全曲线二次同余构造在超奇异点正则的平方根提升，再与7次模对应作Wronskian，最后在对角CM点求值。普通/惰性两类的平方根符号相反，由模p恒等式求导确定。

曾查阅的路线：CM椭圆形式群的第一、第二类周期乘积与Frobenius行列式。Babei--Roy--Swisher--Tobin--Tu, arXiv2408.08844v3（2025-03-12），Theorem1.3及Appendix7.1，处理超几何椭圆曲线的普通/超奇异两类，并引Chisholm--Deines--Long--Nebe--Swisher的CM形式群论证。
https://arxiv.org/html/2408.08844

本题不是该文四个三角群的直接超几何参数，所以没有直接套用其最终定理。新Wronskian论证使用本题已独立建立的有限截断比较。

## 整除问题尚缺

对素数q不属于{2,3,5,7,17}及r>=2，证明q^r|R_n，只要q^r|2n+1。

一阶Lucas已消掉所有q的一阶障碍，但不能在除以q后无条件再次使用同一同余。Guo的Franel整除定理参数不同，不能直接代换。

新的全n等价条件为

(2n+1) | 151beta_n+192780beta_(n-1)，
beta_n=CT[(1+x+y)^3/(xy)-324(1+x+y)-540]^n。

其形式群准对数J若满足反对称CM关系 $J([a](u))+aJ(u)$ 为p整、a为p进单位，则一个首个非整系数引理会强迫J整。目前该关系的整形式群对应尚未构造；复数模方程本身不足以代替此步骤。

此前等价递推

(2n+1)u_(n+1)=1080n u_n+(357n+103)A_n

可作短时精确探索；不需要再次进行大规模素数扫描。此前的小范围整数吻合不是这一高次幂问题的证明。

## 运算与文件

本轮所有新符号证书各不到1秒；仅两个固定消元例外的直接有限核验稍多，仍约1秒。没有启动后台进程、定时工作或大规模搜索。

新九分支证明的关键是有限二次不变量的特征p积分常数控制，以及Hecke有理商的极点刚性；不是假定一般Dwork晶体猜想或套用不满足假设的Beukers最终定理。
