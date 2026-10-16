# 悬赏范围核查（2026-10-15）

本页记录 2026-10-15 对悬赏条款及版本范围的检索结果。本次仓库整理沿用该记录，没有重新调查奖金状态。

## 可直接核验的作者条款

Zhi-Wei Sun, Open Conjectures on Congruences, Nanjing Univ. J. Math. Biquarterly 36 (2019), no. 1, 1–99，正文第34–35页，Conjecture 39 / Remark 39。

作者上传全文：
https://www.researchgate.net/publication/336577970_Open_Conjectures_on_Congruences

- 90美元：首个严格证明 357n+103、2160、-324 所组成的 90/pi 无穷级数恒等式。
- 105美元：首个正确证明整个 Conjecture 39，而非仅其中无权九分支超同余。
- 两笔奖金的对象是分别写出的；原文没有把级数恒等式设为105美元猜想39的组成部分。

用本工作区 A_n 记号，猜想39包含：

1. 对素数 p>5 的加权同余
   sum(n=0..p-1) (357n+103) binom(2n,n) A_n / 2160^n
   = p (-1/p) [54 + 49 (p/3)(p/5)] (mod p^2)。
2. 用户给出的无权 S_p 的九分支模 p^2 同余。
3. 对每个正整数 n 的整除断言
   n binom(2n-1,n-1) divides
   sum(k=0..n-1) (357k+103) 2160^(n-1-k) binom(2k,k) A_k。

Remark 39后面还谈到486、3645的另一条级数和相应整除问题；不能仅凭它们出现在同一注记中，就认定它们也属于105美元的Conjecture 39条款。

## 版本与时效边界

- arXiv:0911.5665 最新版本仍是2011-10-05的v59；访问日期新不等于条款更新。
  https://arxiv.org/abs/0911.5665
- 2020年MathOverflow原帖公式(3)为目标级数，但该帖不是新的奖金条款公告。
  https://mathoverflow.net/questions/369569/two-curious-series-for-1-pi
- 出版社页面确认2021年《数论与组合中的新猜想》的出版信息，但本轮未取得10.44及其注记原页，不能据此声称已经核验2021年奖金的范围或各小项编号对应。
  https://hitpress.hit.edu.cn/2021/1015/c12619a261001/pagem.htm
- 本轮未查到作者针对这两题较新的续悬赏、金额变更、撤回或兑付公告。这是检索结果的边界，不证明奖金仍可申领，也不证明已经失效。

## 其他检索入口

- Prize Problem Ledger（当前页标记2026.2，核查日期2026-07-27）收录作者其他悬赏；本轮没有找到本题的直接条目。
  https://prizeproblems.org/
- 2026年另有The Justin Sun Prize（孙宇晨奖，与出题人孙智伟不同）。本轮查看其官方问题索引，未定位到本题的专门条目；不把其一般奖励宣传视为本题的新奖金。
  https://github.com/TheJustinSunPrize/awards/blob/main/problems/README.md

## 对研究范围的影响

如果目标是处理现已核验的两笔历史悬赏，工作对象应分成：

- 级数恒等式（90美元条款）；
- 加权同余 + 无权九分支同余 + 全部正整数的整除断言（合起来才是2019年105美元条款）。

尚需取得2021年10.44原页，才能准确比较新版是否改变范围；不能先把旧版三项的编号强行对应为新版(ii)、(iii)、(iv)。
