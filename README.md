# Aletheia Research Open

Uncovering model truth through constrained optimization challenges.
Aletheia Research Open is an open ML research tournament focused on efficient model design, parameter optimization, and iterative experimentation.

This repository serves as both:<br>
- a participatory learning system
- a public logbook of experiments and insights

Instead of chasing scale, we focus on:<br>
- efficiency
- tradeoffs
- reproducibility
- insight generation

---

## Round 1: Parameter Golf

### Goal:

Improve a baseline model under strict constraints (compute, size, or data).

Core Loop:

tweak → run → evaluate → log → repeat

What matters:<br>
- small, controlled changes
- consistent logging
- identifying "Goldilocks zones"
- reasoning about tradeoffs

---

## Getting Started

### 1. Clone baseline model

We use:<br>
- nanoGPT (minimal GPT training pipeline)

```
git clone https://github.com/karpathy/nanoGPT.git

cd nanoGPT
```

### 2. Run baseline

```
python train.py config/train_shakespeare_char.py
```

Confirm:<br>
- training runs
- loss decreases

### 3. Add logging

Track each run:<br>

```
run,learning_rate,batch_size,score
```

where score = final loss (initially)

### 4. Run experiments

Start with 3–5 runs:<br>
- vary one parameter at a time
- log results
- observe patterns

Experiment Log Format

Example:

<table>
  <tr>
    <th>run</th>
    <th>learning_rate</th>
    <th>batch_size</th>
    <th>predicted_score</th>
    <th>actual_score</th>
  </tr>
  <tr>
    <td>1</td>
    <td>1e-3</td>
    <td>32</td>
    <td>2.4</td>
    <td>2.5</td>
  </tr>
  <tr>
    <td>2</td>
    <td>5e-4</td>
    <td>32</td>
    <td>2.1</td>
    <td>2.1</td>
  </tr>
</table>

---

## Directory Structure

```
aletheia-research-open/
│
├── docs/               # notes, insights, write-ups
├── leaderboard/        # best configurations and scores
├── parameter-golf/
│   ├── configs/        # parameter configs (learning rate, batch size, etc.)
│   ├── experiments/    # scripts to run experiments
│   ├── logs/           # experiment logs (CSV / JSON)
│   ├── results/        # outputs from runs
│   └── eval/           # evaluation functions
├── LICENSE
├── .gitignore
├── README.md
│
```
---

## Roadmap

### Phase 1 — Baseline and Logging

[] Run baseline model<br>
[] Set up experiment log<br>
[] Run 10–20 experiments<br>
[] Identify initial parameter patterns

### Phase 2 — Pattern Recognition

[] Add predicted vs actual score<br>
[] Identify stable vs unstable regions<br>
[] Document "Goldilocks zones"

### Phase 3 — Predictive System 

[] Rank parameter moves by expected value<br>
[] Build simple heuristic model<br>
[] Reduce random experimentation

### Phase 4 — Automation

[] Add parameter sweeps<br>
[] Integrate optimization tools (e.g. Optuna)<br>
[] Automate experiment runs

### Phase 5 — Data Science Agent

[] Build agent that reads logs<br>
[] Suggest next parameter configurations

### Close the loop:

agent → experiment → evaluation → update

### Leaderboard

Track best configurations:<br>
- Lowest loss
- Most stable performance
- Best efficiency under constraints

### Participation

This is an open, evolving system.

You can:<br>
- fork the repo
- run your own experiments
- submit improvements
- share insights

### 💡 Core Principle

Learn → Test → Log → Predict → Improve

### Long-Term Vision

From manual experimentation →

- self-improving research system

From individual runs →

- a structured research tournament

### Status

Early-stage (active development)<br>
Goal: flight-ready system by Fall 2026
