---
layout: post
title: Value Iteration Algorithm Detail
---

## Value Iteration Algorithm Detail

<p class="message">
<font color="#C20000">An optimal policy maps each distinct state to an optimal action maximizing the value of the state over the horizon of some magnitude or even infinity</font>.  With an optimal policy, it's easy to evaluate the expected value from each possible starting state by executing it.  All above must be resorted to <font color="Green">value iteration</font>.
</p>

### <font color="Green">Value Iteration</font> Algorithm/Flow
>Let me try to express <font color="Green">value iteration</font> flow in below in this section.  
>
>Initialize $V_0(S)=0$ for all $S$.  
>Loop until $\left\|V_t-V_{t-1}\right\|<\varepsilon\cdot\frac{1-\gamma}\gamma$  
>>Loop for all $S$
>>>$$V_{t+1}(S)\leftarrow R(S)+\underset A{max}\left[\gamma\cdot\sum_{S'}P(S'\left|S,A\right.)\cdot V_{t}(S')\right]$$  
>
>Such flow comes with below features:  
>&#10112;$V_{t}$ converges to some optimized value, say $V^{*}$.  
>&#10113;no need to keep $V_{t+1}$ v.s. $V_{t}$, since it just converges.  
>&#10114;<font color="OrangeRed">asynchronous</font>(can do <font color="OrangeRed">random</font> state updates).  
>&#10115;we want $\left\|V_t-V^\ast\right\|=\underset{S'}{max}\left\|V_t-V^\ast\right\|<\varepsilon$,  
>then, the whole case is below $\varepsilon\cdot\frac{1-\gamma}\gamma$, I'd like to show you &#10115;  
>proof:  
>begin from $\left\|V_t-V_{t+1}\right\|=\gamma\cdot\left\|V_{t-1}-V_t\right\|$  
>...this holds W.R.T the above <font color="Green">value iteration</font>  
>next, focus on $\varepsilon\cdot(1-\gamma)$, where $V_t=\gamma\cdot V_{t-1}$  
>...the infinite horizon expected discounted reward  
>therefore, $V_{t-1}-V_t=V_{t-1}\cdot(1-\gamma)$  
$$\begin{array}{l}\therefore\left\|V_t-V_{t+1}\right\|\\=\gamma\cdot\left\|V_{t-1}-V_t\right\|<unknown\\=\gamma\cdot V_{t-1}\cdot(1-\gamma)<unknown\end{array}$$  
>next, express $unknown$ in terms of $\varepsilon$ and $1-\gamma$, this should hold, where $\varepsilon$ is a small and unknown coefficient by design.  
>next take $unknown=\varepsilon\cdot(1-\gamma)$, because $V_{t-1}-V_t$could be expressed with $(1-\gamma)$ term in it.  Then, the whole inequality becomes:  
$$\begin{array}{l}\gamma\cdot V_{t-1}\cdot(1-\gamma)<unknown\\\Rightarrow\gamma\cdot V_{t-1}\cdot(1-\gamma)<\varepsilon\cdot(1-\gamma)\\\Rightarrow\gamma\cdot\left\|V_{t-1}-V_t\right\|<\varepsilon\cdot(1-\gamma)\\\Rightarrow\left\|V_{t-1}-V_t\right\|<\varepsilon\cdot\frac{1-\gamma}\gamma\\\Rightarrow\left\|V_{t+1}-V_t\right\|<\varepsilon\cdot\frac{1-\gamma}\gamma\end{array}$$  
>as $t$ increases, we will have $V_{t-1}\approx V_t\approx V_{t+1}$.  

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Green">value iteration</font> -->
<!-- <font color="#00ADAD">policy</font> -->
<!-- <font color="#6100A8">full observable</font> -->
<!-- <font color="#FFAC12">partial observable</font> -->
<!-- <font color="#EB00EB">stochastic</font> -->
<!-- <font color="#8400E6">state transition</font> -->
<!-- <font color="#D600D6">discount factor gamma $\gamma$</font> -->
<!-- <font color="DeepSkyBlue">optimal action</font> -->
<!-- <font color="red">value of a state</font> -->
<!-- <font color="#D600D6">$V(S)$</font> -->
<!-- <font color="#9300FF">immediate reward R(S)</font> -->
<!-- <font color="#C20000">positive conclusion, finding</font> -->
<!-- <font color="green">negative conclusion, finding</font> -->