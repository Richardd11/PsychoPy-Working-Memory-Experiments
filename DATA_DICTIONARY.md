# Data Dictionary - Working Memory & Mind Wandering Experiment

**Version:** 2.0.0  
**Last Updated:** 2026-09-02  
**Experiment:** PsychoPy Experiment 1 & 2 Replication

---

## Overview

This document provides a comprehensive description of all variables in the experiment data output files. Each trial generates one row in the CSV file with 50 columns.

---

## Participant Information

### `participant`
- **Type:** String
- **Description:** Unique participant identifier
- **Example:** `P001`, `SUB_042`
- **Required:** Yes
- **Notes:** Set by researcher at experiment start

### `session`
- **Type:** String
- **Description:** Session number for this participant
- **Example:** `001`, `002`
- **Default:** `001`
- **Notes:** Allows multiple sessions per participant

### `date`
- **Type:** String (datetime)
- **Description:** Date and time when experiment was run
- **Format:** `YYYY_MonDD_HHMM`
- **Example:** `2026_Sep02_1430`
- **Auto-generated:** Yes

### `age`
- **Type:** Integer or String
- **Description:** Participant's age in years
- **Range:** Typically 18-99
- **Example:** `25`, `not specified`

### `gender`
- **Type:** String (categorical)
- **Description:** Participant's gender identity
- **Values:** 
  - `male`
  - `female`
  - `other`
  - `prefer not to say`

### `exp_order`
- **Type:** String (categorical)
- **Description:** Order of experiment presentation (counterbalancing)
- **Values:**
  - `1-then-2` = Experiment 1 first, then Experiment 2
  - `2-then-1` = Experiment 2 first, then Experiment 1
- **Notes:** Critical for controlling order effects

---

## Trial Information

### `experiment_number`
- **Type:** Integer (categorical)
- **Description:** Which experiment (design) this trial belongs to
- **Values:**
  - `0` = Practice trial
  - `1` = Experiment 1 (simultaneous presentation)
  - `2` = Experiment 2 (sequential presentation)
- **Analysis:** Use to separate experiments for comparison

### `phase`
- **Type:** String (categorical)
- **Description:** Experimental phase
- **Values:**
  - `practice` = Practice trials (not analyzed)
  - `main` = Main experiment trials
- **Filter:** Typically filter for `phase == 'main'` in analysis

### `block`
- **Type:** Integer
- **Description:** Block number within experiment (every 36 trials)
- **Range:** 1-4 (for 144 trials)
- **Example:** `1`, `2`, `3`, `4`
- **Notes:** Used to track fatigue effects or performance changes

### `trial_number`
- **Type:** Integer
- **Description:** Trial number from condition file
- **Range:** 1-144 (main experiment), 1-6 (practice)
- **Example:** `1`, `72`, `144`

### `trial_index`
- **Type:** String
- **Description:** Legacy field (not currently used)
- **Value:** Always `NA`
- **Notes:** Kept for backward compatibility

---

## Experimental Conditions

### `load_condition`
- **Type:** Integer (categorical)
- **Description:** Cognitive load level (secondary task difficulty)
- **Values:**
  - `0` = No parity judgments (baseline)
  - `2` = Judge 2 digits
  - `4` = Judge 4 digits
- **Balance:** Each value appears in 48/144 trials (33.3%)
- **Analysis:** Primary independent variable

### `change_condition`
- **Type:** String (categorical)
- **Description:** Whether probe color changed from memory array
- **Values:**
  - `change` = Probe color is different from original
  - `no_change` = Probe color matches original
- **Balance:** 50% change, 50% no-change
- **Analysis:** Used to calculate signal detection metrics (d', criterion)

### `tested_position`
- **Type:** Integer (categorical)
- **Description:** Which of the 4 memory positions was tested
- **Values:** `1`, `2`, `3`, `4`
- **Mapping:**
  - `1` = Top-left
  - `2` = Top-right
  - `3` = Bottom-left
  - `4` = Bottom-right
- **Balance:** Each position tested equally (25% each)

---

## Memory Stimuli Positions

### `memory_pos_1_x`, `memory_pos_1_y`
### `memory_pos_2_x`, `memory_pos_2_y`
### `memory_pos_3_x`, `memory_pos_3_y`
### `memory_pos_4_x`, `memory_pos_4_y`

- **Type:** Float
- **Description:** X and Y coordinates of the 4 memory squares
- **Units:** Normalized units (proportion of screen height)
- **Range:** -0.5 to 0.5 (centered at 0, 0)
- **Fixed Values:**
  - Position 1: (-0.2, 0.2) = top-left
  - Position 2: (0.2, 0.2) = top-right
  - Position 3: (-0.2, -0.2) = bottom-left
  - Position 4: (0.2, -0.2) = bottom-right
- **Notes:** Positions are fixed across all trials

---

## Memory Stimuli Colors

### `memory_color_1`, `memory_color_2`, `memory_color_3`, `memory_color_4`

- **Type:** String (categorical)
- **Description:** Colors shown at the 4 memory positions
- **Values:** `red`, `green`, `blue`, `yellow`, `magenta`, `cyan`, `white`, `orange`
- **Randomization:** Randomly selected without replacement each trial
- **Notes:** All 4 colors in a trial are different

### `original_color`
- **Type:** String (categorical)
- **Description:** Original color at the tested position
- **Values:** Same as memory_color_* (8 possible colors)
- **Derivation:** `original_color = memory_color_N` where N = tested_position

### `probe_color`
- **Type:** String (categorical)
- **Description:** Color shown during memory test
- **Values:** Same as memory_color_* (8 possible colors)
- **Relationship to original_color:**
  - If `change_condition == 'change'`: probe_color ≠ original_color
  - If `change_condition == 'no_change'`: probe_color == original_color

---

## Parity Task (Secondary Task)

For each of 4 possible parity items:

### `parity_digit_N` (N = 1, 2, 3, 4)
- **Type:** Integer or String
- **Description:** Digit presented for odd/even judgment
- **Values:** `1`, `2`, `3`, `4`, `6`, `7`, `8`, `9`, `NA`
- **Exclusions:** Digit 5 excluded (ambiguous parity)
- **NA cases:** 
  - Load 0: All 4 are `NA`
  - Load 2: Two are digits, two are `NA`
  - Load 4: All 4 are digits

### `parity_response_N` (N = 1, 2, 3, 4)
- **Type:** String (categorical) or NA
- **Description:** Participant's response to parity judgment
- **Values:**
  - `f` = Judged as odd
  - `j` = Judged as even
  - `NA` = No parity item presented OR timeout
- **Mapping:** F key = odd, J key = even

### `parity_correct_N` (N = 1, 2, 3, 4)
- **Type:** Integer (binary) or String
- **Description:** Correctness of parity judgment
- **Values:**
  - `1` = Correct response
  - `0` = Incorrect response or timeout
  - `NA` = No parity item presented
- **Calculation:**
  - Odd digits (1,3,7,9): correct if response = 'f'
  - Even digits (2,4,6,8): correct if response = 'j'

### `parity_rt_N` (N = 1, 2, 3, 4)
- **Type:** Float or String
- **Description:** Reaction time for parity judgment
- **Units:** Seconds
- **Range:** 0.15 - 1.5 (timeout at 1.5s)
- **Values:**
  - Float value = time from stimulus onset to keypress
  - `NA` = No parity item presented OR timeout
- **Precision:** 0.001s (millisecond precision)
- **Notes:** RTs < 150ms may indicate anticipatory responses

---

## Memory Test

### `memory_response`
- **Type:** String (categorical)
- **Description:** Participant's response to change detection test
- **Values:**
  - `s` = Judged as SAME color
  - `d` = Judged as DIFFERENT color
  - `NA` = Timeout (no response within 5 seconds)
- **Mapping:** S key = same, D key = different

### `memory_correct`
- **Type:** Integer (binary)
- **Description:** Correctness of memory judgment
- **Values:**
  - `1` = Correct response
  - `0` = Incorrect response or timeout
- **Calculation:**
  - No-change trials: correct if response = 's'
  - Change trials: correct if response = 'd'
  - Timeout: always 0
- **Primary DV:** Main dependent variable for memory performance

### `memory_rt`
- **Type:** Float or String
- **Description:** Reaction time for memory test
- **Units:** Seconds
- **Range:** 0.2 - 5.0 (timeout at 5s)
- **Values:**
  - Float value = time from probe onset to keypress
  - `NA` = Timeout
- **Precision:** 0.001s
- **Analysis Notes:** Log-transform may improve normality

---

## Thought Probe

### `thought_probe_response`
- **Type:** String (integer as string)
- **Description:** Numeric response to thought probe question
- **Values:** `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `NA`
- **Mapping:** Number keys 1-8
- **Rare NA:** Should be rare (requires escape key or crash)

### `thought_probe_label`
- **Type:** String (categorical)
- **Description:** Text label for thought probe category
- **Values:**
  - `Task` = Focused on the current task (response 1)
  - `Task experience/performance` = Evaluating own performance (response 2)
  - `Everyday things` = Thoughts about daily life (response 3)
  - `Current state of being` = Bodily sensations, emotions (response 4)
  - `Personal worries` = Anxieties, concerns (response 5)
  - `Daydreams` = Fantasy, imagination (response 6)
  - `External environment` = Sounds, sights around them (response 7)
  - `Other` = Other thoughts (response 8)
  - `NA` = No response
- **Analysis:** 
  - On-task: Categories 1-2
  - Mind-wandering: Categories 3-8
  - Task-unrelated: Categories 3, 5, 6

### `thought_probe_rt`
- **Type:** Float or String
- **Description:** Reaction time for thought probe response
- **Units:** Seconds
- **Range:** 0.5 - 30+ (no timeout)
- **Values:**
  - Float value = time from question onset to keypress
  - `NA` = No response (should be rare)
- **Notes:** Higher RTs may indicate deliberation or confusion

---

## Timing Data (NEW in v2.0)

### `trial_start_time`
- **Type:** Float
- **Description:** Timestamp when trial began (fixation onset)
- **Units:** Seconds since experiment start
- **Reference:** Relative to experiment start (globalClock)
- **Example:** `123.456` = 123.456 seconds after experiment began
- **Usage:** Calculate time-on-task effects, detect technical issues

### `trial_end_time`
- **Type:** Float
- **Description:** Timestamp when trial ended (after thought probe)
- **Units:** Seconds since experiment start
- **Reference:** Same as trial_start_time
- **Example:** `143.789`

### `trial_duration`
- **Type:** Float
- **Description:** Total duration of the trial
- **Units:** Seconds
- **Calculation:** `trial_end_time - trial_start_time`
- **Range:** 
  - Experiment 1, Load 0: ~13-15 seconds
  - Experiment 1, Load 4: ~18-20 seconds
  - Experiment 2: ~20-25 seconds (varies more)
- **Analysis:** Use to detect technical problems, participant engagement

---

## Data Quality Indicators

### Missing Data Patterns

**Expected NA values:**
- `parity_digit_1-4`: Expected for load 0 trials
- `parity_response_1-4`: Expected for load 0 OR timeout
- `parity_correct_1-4`: Expected for load 0
- `parity_rt_1-4`: Expected for load 0 OR timeout

**Problematic NA values:**
- `memory_response`: Indicates timeout or technical issue
- `thought_probe_response`: Very rare, indicates problem
- High frequency suggests participant disengagement

### Outliers to Check

**Response Times:**
- `parity_rt_N` < 0.15s: Too fast (anticipatory)
- `parity_rt_N` > 1.4s: Near timeout (may miss response)
- `memory_rt` < 0.2s: Too fast (guessing)
- `memory_rt` > 4.5s: Near timeout
- `thought_probe_rt` > 10s: Unusually long deliberation

**Accuracy:**
- `memory_correct` = 0 for >80% trials: Disengaged participant
- `parity_correct_N` < 0.5: Below chance (check key mapping understanding)

---

## Derived Variables for Analysis

### Working Memory Capacity (K)

Calculate Cowan's K for each load condition:

```
K = set_size × (hit_rate + correct_rejection_rate - 1)
```

Where:
- set_size = 4 (always 4 items)
- hit_rate = P(response='d' | change_condition='change')
- correct_rejection_rate = P(response='s' | change_condition='no_change')

### Signal Detection Metrics

**d' (d-prime):** Sensitivity
```
d' = Z(hit_rate) - Z(false_alarm_rate)
```

**c (criterion):** Response bias
```
c = -0.5 × [Z(hit_rate) + Z(false_alarm_rate)]
```

Where:
- hit_rate = P(response='d' | change_condition='change')
- false_alarm_rate = P(response='d' | change_condition='no_change')
- Z = inverse normal CDF

### Mind-Wandering Rate

```
MW_rate = count(thought_probe_label in [Everyday, Worries, Daydreams]) / total_trials
```

Conservative definition (exclude categories 4, 7, 8).

### Parity Task Accuracy

For each trial with parity items:
```
parity_accuracy = sum(parity_correct_1-4 == 1) / count(parity_digit_1-4 != NA)
```

---

## Data Validation Checklist

Before analysis, verify:

1. **Complete data:**
   - ✓ All participant info fields filled
   - ✓ 144 trials per experiment (288 total main trials)
   - ✓ 6 practice trials (optional to include)

2. **Balance:**
   - ✓ Each load condition: 48 trials per experiment
   - ✓ Change vs no-change: 72 each per experiment
   - ✓ Each tested position: 36 trials per experiment

3. **Valid values:**
   - ✓ experiment_number in [0, 1, 2]
   - ✓ load_condition in [0, 2, 4]
   - ✓ All colors in allowed set
   - ✓ Response keys match expected values

4. **Timing:**
   - ✓ trial_duration > 10 seconds (reasonable minimum)
   - ✓ trial_end_time > trial_start_time
   - ✓ Consecutive trials don't overlap

5. **Missingness:**
   - ✓ < 10% memory_response = NA
   - ✓ < 5% thought_probe_response = NA
   - ✓ parity NA pattern matches load condition

---

## Example Data Row

```csv
P001,001,2026_Sep02_1430,25,female,1-then-2,1,main,1,1,NA,2,change,3,-0.2,0.2,0.2,0.2,-0.2,-0.2,0.2,-0.2,red,blue,green,yellow,green,cyan,7,f,0,0.823,9,j,0,0.991,NA,NA,NA,NA,NA,NA,NA,NA,d,1,1.234,3,Everyday things,2.156,45.123,58.456,13.333
```

---

## File Naming Convention

**Format:**
```
{ParticipantID}_{ExperimentName}_{DateTime}_detailed.csv
```

**Example:**
```
P001_WorkingMemory_MindWandering_2026_Sep02_1430_detailed.csv
```

**Location:** `data/` folder in experiment directory

---

## Version History

**v2.0.0 (2026-09-02):**
- Added: exp_order, block, trial timing fields
- Enhanced: Improved documentation
- Fixed: Various data quality issues

**v1.0.0 (2026-09-01):**
- Initial data structure

---

## Contact

For questions about data structure or analysis:
- Email: [your email]
- Lab: [your lab]
- Reference: https://econtent.hogrefe.com/doi/10.1027/1618-3169/a000599

---

## Citation

If using this experiment or data structure, please cite:

```
[Your citation format]
Based on: Holmqvist, K., & Sohlberg, R. (2024). [Paper details]
```

---

**END OF DATA DICTIONARY**
