# 孙智伟的一个 $90/\pi$ 级数及相关超同余

Research notes on a series for $90/\pi$ and related supercongruences proposed by Zhi-Wei Sun.

本仓库收录围绕孙智伟猜想 10.44(i)、(iv) 展开的研究草稿，范围扩展至 2019 年《Open Conjectures on Congruences》猜想 39 的三项断言：无权超同余、加权超同余与整数整除性。

**截至 2026 年 10 月 16 日，四项命题均有覆盖全部所述范围的证明草稿，并留有内部自审记录；尚未经独立数学审阅。** 本仓库不据此宣称已获作者认可、确认发表优先权或取得悬赏资格。各版本的范围见 [悬赏与版本说明](docs/bounty-scope.md)。

研究推导、程序和初稿主要由 **OpenAI Codex（AI 助手）** 根据项目发起人的要求生成。内部自审也由同一 AI 完成，不等同于独立验证。分工和限制见 [AI 参与说明](AI-DISCLOSURE.md)。

## 研究对象

令

$$
A_n=\sum_{k=0}^{n}\binom nk\binom{n+2k}{2k}\binom{2k}{k}(-324)^{n-k}.
$$

仓库中的四份主稿分别讨论：

| 命题 | 内容 | 主稿 |
| --- | --- | --- |
| 级数 | $\displaystyle\sum_{n\ge0}\frac{357n+103}{2160^n}\binom{2n}{n}A_n=\frac{90}{\pi}$ | [级数证明](proofs/proof-series.md) |
| 无权超同余 | $\displaystyle S_p=\sum_{n=0}^{p-1}\binom{2n}{n}A_n/2160^n$ 的九分支模 $p^2$ 公式 | [九分支证明](proofs/nine-branches-proof.md) |
| 加权超同余 | $\displaystyle W_p\equiv54p\left(\frac{-1}{p}\right)+49p\left(\frac{15}{p}\right)\pmod{p^2}$，$p>5$ | [加权证明](proofs/weighted-wronskian-proof.md) |
| 整除性 | $\displaystyle n\binom{2n-1}{n-1}\mid\sum_{k=0}^{n-1}(357k+103)2160^{n-1-k}\binom{2k}{k}A_k$，$n\ge1$ | [整除证明](proofs/divisibility-proof.md) |

其中 $W_p$ 为在 $S_p$ 的每一项上乘以 $357n+103$ 后所得的和。完整题面及九分支表见 [命题陈述](docs/problem-statement.md)。

## 从哪里读起

建议先读 [命题陈述](docs/problem-statement.md)，再依次读级数、无权超同余、加权超同余和整除性主稿。它们是分文件的研究草稿，尚未合并为期刊论文。

[阅读顺序](docs/reading-guide.md) 给出各主稿所依赖的引理和所需背景。[审阅说明](docs/status.md) 区分现有论证、内部自审与独立审阅，并列出适合优先审阅的步骤。[参考文献](docs/references.md) 汇集原始命题和主要数学工具的出处。

## 文件结构

```text
proofs/     四份证明主稿
lemmas/     生成函数、模形式、几何与形式群的辅助笔记
review/     此前的内部自审记录
scripts/    符号计算附件和有界数值探索
data/       七次模方程的多项式
docs/       题面、阅读顺序、文献及版本说明
archive/    历史进度、探索记录与原文件位置表
```

历史文件中的“尚缺”“下一步”等文字记录的是当时的进度，不能用来判断整套草稿的当前状态。

## 计算附件

正文阅读无需安装程序。计算附件使用 Python 和 SymPy；此前环境为 Python 3.14.3、SymPy 1.14.0。文件列表、运行方式及用途见 [计算附件说明](scripts/README.md)。

```sh
python -m pip install -r requirements.txt
python scripts/nl-certificate.py
```

这只是单个附件的运行示例。仓库没有自动批量计算或定时任务。代数附件用于核对正文中的公式，有界素数例子只作探索和转录检查，不能替代一般性论证。

## 原始问题与使用说明

级数见孙智伟的 [MathOverflow 原帖，公式 (3)](https://mathoverflow.net/questions/369569/two-curious-series-for-1-pi)。相关有限和断言见 [2019 年作者上传版本，猜想 39](https://www.researchgate.net/publication/336577970_Open_Conjectures_on_Congruences)，更早版本见 [arXiv:0911.5665](https://arxiv.org/abs/0911.5665)。

欢迎提交指出具体文件和步骤的数学意见，参见 [贡献说明](CONTRIBUTING.md)。本仓库尚未指定内容或代码的开放许可；公开可读与再使用授权应分别处理。
