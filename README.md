# Behavioral Economics Game: Reward Allocation Task

An interactive web-based experiment designed to explore human decision-making in contexts involving unequal rewards. Participants are asked to allocate resources between two options, each offering a different payoff structure.

---

## Concept

This game simulates a basic economic decision under asymmetric incentives. Users must drag and drop items (balls) into one of two containers:

- 🟨 **Yellow Container** – Yields **100% of the reward value** per item.
- 🟦 **Blue Container** – Yields **50% of the reward value** per item.

The rule of the task is to put the balls in Blue Container. The task challenges users to balance notions of fairness, gain maximization, and choice behavior.

---

##  Game Interface

### Task Arena

Below is the interface where participants interact with the game:

![Game Arena](./static/images/bdf35120-7f0c-4398-9712-4457d55a041f.png)

### Instructions

1. Drag each black ball from the center to either the **yellow** or **blue** container.
2. Once all balls have been placed, click the **Submit** button.
3. Your total earnings will be calculated based on the container values.

---

##  Project Structure

| File / Directory      | Description                                      |
|-----------------------|--------------------------------------------------|
| `instruction.html`    | Displays game instructions and overview          |
| `game.html`           | Main interactive interface                       |
| `__init__.py`         | Backend logic and server routing (e.g., Flask)   |
| `result.html`         | Displays final score and allocation summary      |


---

##  Research Applications

This task is useful for experiments or demonstrations in:

- Behavioral economics
- Social psychology
- Resource allocation studies
- Human-computer interaction (HCI)

---

## Requirements

- Python 3.x
- Modern browser (Chrome, Firefox, Edge)
