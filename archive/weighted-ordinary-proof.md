> 历史记录。文中的进度判断和待办反映写作时的状态；当前状态见 [项目说明](../README.md)。

# 加权同余：八个普通分支已证，惰性分支仍需推进

更新（2026-10-16）：后续的[weighted-wronskian-proof.md](../proofs/weighted-wronskian-proof.md)给出同时处理普通、惰性素数的新证明草稿，[weighted-wronskian-audit.md](../review/weighted-wronskian-audit.md)记录其自审。本文件保留此前只处理普通素数的方法。

2026-10-16。使用[nine-branches-proof.md](../proofs/nine-branches-proof.md)的Hecke多项式T_p(U,r)、普通单位根v(r)、P_p=C_p(modp²)。以下证明所有(-105/p)=1、p>7的加权同余。

## 1. 可以对普通根同余求导

T_p的系数模p³仅剩T_p,p U^p+A_p U^(p+1)。在r0普通单位根v处，其对U的偏导模p为A_p v^p，是单位。因此隐函数给出p整局部根v(r)，并由系数同余得到

v(r)=C_p(r) (modp³)，v'(r)=C_p'(r) (modp³)。

结合P_p=C_p作为有理函数模p²的同余，可在r0同时替换P_p与P_p'。

## 2. 复乘导数的精确计算

写alpha=(15+sqrt(-105))/30，y=Im(alpha)，k0=315/16。取[cm-eight-branches.md](../lemmas/cm-eight-branches.md)中的u=c alpha+d、e，以及使(alpha+j)/p=gamma alpha的W_e矩阵gamma=(a,b;c',d')，c'=-c、c'alpha+d'=bar(u)。

普通局部根可写成v(tau)=p²H(tau)/H((tau+j)/p)。权2变换给出

v(alpha)=chi(W_e)u²/e，

v_r'/v=[(1-bar(u)/u)*h_tau+2c/u]/r_tau'，

其中h_tau=(dH/dtau)/H。由第一题已经证明的特殊值与(Dr/H)(alpha)=sqrt(105)/32，等价地有精确CM导数恒等式

h_tau+(54/k0)r_tau'=i/y。

又u-bar(u)=2iyc，因此

v_r'/v=-(54/k0)(1-bar(u)/u)。

最终

54v+k0 v_r'=54v*bar(u)/u=54chi(W_e)p。

表中chi(W_e)=(-1/p)，所以普通分支的(T)成立。[transverse-congruence.md](../lemmas/transverse-congruence.md)的(E)再给出完整加权式

W_p=p*(-1/p)*[54+49(p/3)(p/5)] (modp²)。

## 3. 尚未处理的部分

惰性素数不存在这里的普通单位根，因此不能直接照搬本证明。虽然P_p(r0)=0(modp²)已证，P_p'(r0)通常只有一个p因子，仍须证明

P_p'(r0)=(96/35)p*(-1/p) (modp²)

才能完成惰性加权分支。当前不把它视为已证。加权原命题还包括p=7，直接按原定义计算W_7=14(mod49)，等于断言的-35(mod49)，已独立核验。
