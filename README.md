# 🏥 Hospital Patient Queue


## 📌 Overview

The Hospital Patient Queue system simulates how hospitals manage emergency and regular patients.
Critical patients are treated first using a priority queue, while regular patients are handled in the order they arrive using a normal queue.
The system also provides an estimated wait time for patients.


---

## ✅ Advantages

- Efficient Triage: Ensures emergency patients are given immediate attention.

- Fair Scheduling: Regular patients are served in FIFO (First-In-First-Out) order.

- Realistic Simulation: Mimics real hospital workflow.

- Scalable: Can be extended to multiple doctors, departments, or severity levels.



---

## 🗂️ Data Structures Used

~Priority Queue (heapq) → To handle critical patients (lower severity = higher priority).

~Queue (deque) → To handle regular patients in FIFO order.

~List → To maintain patient history and waiting times.



---

## 🎯 Usefulness

- Helps understand priority scheduling in real-world systems.

- Bridges theory (queues, heaps) with practical hospital management.

- Can be extended for multi-threading and resource allocation problems.

- Useful for DSA practice and simulations.



---

## 🛠️ Why We Use This Project

Hospitals must decide who gets treatment first.
This project shows how data structures (queues and heaps) can model critical decision-making efficiently.


---

## 🔹 Sample Output

###### 🚨 Emergency patient Alice added with severity 2
###### 🧑‍⚕️ Regular patient Bob added to queue
###### 🚨 Emergency patient Charlie added with severity 1
###### 🧑‍⚕️ Regular patient David added to queue
###### ⏳ Estimated wait time for Bob: 15 minutes
###### ⏳ Estimated wait time for Charlie: 5 minutes
###### ✅ Serving Charlie (Emergency)
###### ✅ Serving Alice (Emergency)
###### ✅ Serving Bob (Regular)

---
