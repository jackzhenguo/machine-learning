## Confidence Interval For a Sample: Steps

**Question**:

> A group of 10 foot surgery patients had a [mean ](https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/statistics-definitions/mean-median-mode/#mean)weight of 240 pounds. The sample[ standard deviation](https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/standard-deviation/) was 25 pounds. Find a confidence interval for a sample for the true mean weight of all foot surgery patients. Find a 95% CI.

**Step 1:** *Subtract 1 from your sample size*. 10 – 1 = 9. This gives you [degrees of freedom,](https://www.statisticshowto.datasciencecentral.com/degrees-of-freedom/) which you’ll need in step 3.

**Step 2:** *Subtract the confidence level from 1, then divide by two.*
(1 – .95) / 2 = .025

**Step 3:** *Look up your answers to step 1 and 2 in the t-distribution table.* For 9 degrees of freedom (**df**) and **α =** 0.025, my result is 2.262.

| **df** | **α = 0.1** | **0.05** | **0.025** | **0.01** | **0.005** | **0.001** | **0.0005** |
| ------ | ----------- | -------- | --------- | -------- | --------- | --------- | ---------- |
| **∞**  | tα=1.282    | 1.645    | 1.960     | 2.326    | 2.576     | 3.091     | 3.291      |
| **1**  | 3.078       | 6.314    | 12.706    | 31.821   | 63.656    | 318.289   | 636.578    |
| **2**  | 1.886       | 2.920    | 4.303     | 6.965    | 9.925     | 22.328    | 31.600     |
| **3**  | 1.638       | 2.353    | 3.182     | 4.541    | 5.841     | 10.214    | 12.924     |
| **4**  | 1.533       | 2.132    | 2.776     | 3.747    | 4.604     | 7.173     | 8.610      |
| **5**  | 1.476       | 2.015    | 2.571     | 3.365    | 4.032     | 5.894     | 6.869      |
| **6**  | 1.440       | 1.943    | 2.447     | 3.143    | 3.707     | 5.208     | 5.959      |
| **7**  | 1.415       | 1.895    | 2.365     | 2.998    | 3.499     | 4.785     | 5.408      |
| **8**  | 1.397       | 1.860    | 2.306     | 2.896    | 3.355     | 4.501     | 5.041      |
| **9**  | 1.383       | 1.833    | 2.262     |          |           |           |            |

**Step 4:** *Divide your sample standard deviation by the square root of your sample size.*
25 / √(10) = 7.90569415

**Step 5:** *Multiply step 3 by step 4.*
2.262 × 7.90569415 = 17.8826802

**Step 6:** *For the lower end of the range, subtract step 5 from the sample mean.*
240 – 17.8826802 = 222.117



**Step 7:** *For the upper end of the range, add step 5 to the sample mean.*
240 + 17.8826802 = 257.883