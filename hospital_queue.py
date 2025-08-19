import heapq
from collections import deque
import time

# Patient Class

class Patient:
    def __init__(self, patient_id, name, severity, is_emergency=False):
        self.patient_id = patient_id
        self.name = name
        self.severity = severity  # Lower = more severe
        self.is_emergency = is_emergency

    def __repr__(self):
        status = "Emergency" if self.is_emergency else "Regular"
        return f"Patient({self.name}, Severity={self.severity}, {status})"


# Hospital Queue System

class HospitalQueue:
    def __init__(self):
        self.emergency_queue = []   # Min-Heap for emergencies
        self.regular_queue = deque()  # Normal queue for regular patients
        self.history = []           # List of served patients
        self.avg_service_time = 5   # Assume 5 minutes per patient

    # Add patient
    def add_patient(self, patient):
        if patient.is_emergency:
            heapq.heappush(self.emergency_queue, (patient.severity, patient))
            print(f"🚨 Emergency patient {patient.name} added with severity {patient.severity}")
        else:
            self.regular_queue.append(patient)
            print(f"🧑‍⚕️ Regular patient {patient.name} added to queue")

    # Serve next patient
    def serve_patient(self):
        if self.emergency_queue:
            _, patient = heapq.heappop(self.emergency_queue)
        elif self.regular_queue:
            patient = self.regular_queue.popleft()
        else:
            print("⚠️ No patients waiting.")
            return

        print(f"✅ Serving {patient.name} ({'Emergency' if patient.is_emergency else 'Regular'})")
        self.history.append((patient, time.ctime()))

    # Estimate wait time
    def estimate_wait_time(self, patient_name):
        position = 0
        for i, (_, p) in enumerate(self.emergency_queue):
            if p.name == patient_name:
                position = i + 1
                break
        for i, p in enumerate(self.regular_queue):
            if p.name == patient_name:
                position = len(self.emergency_queue) + i + 1
                break
        if position == 0:
            print(f"⚠️ {patient_name} not in queue.")
        else:
            print(f"⏳ Estimated wait time for {patient_name}: {position * self.avg_service_time} minutes")

    # Show history
    def show_history(self):
        if not self.history:
            print("📭 No patients served yet.")
            return
        print("\n📜 Service History:")
        for patient, t in self.history:
            print(f"{patient.name} ({'Emergency' if patient.is_emergency else 'Regular'}) at {t}")


# Simulation Example

if __name__ == "__main__":
    hospital = HospitalQueue()

    # Add patients
    p1 = Patient(1, "Alice", 2, is_emergency=True)
    p2 = Patient(2, "Bob", 5, is_emergency=False)
    p3 = Patient(3, "Charlie", 1, is_emergency=True)
    p4 = Patient(4, "David", 4, is_emergency=False)

    hospital.add_patient(p1)
    hospital.add_patient(p2)
    hospital.add_patient(p3)
    hospital.add_patient(p4)

    # Estimate wait times
    hospital.estimate_wait_time("Bob")
    hospital.estimate_wait_time("Charlie")

    # Serve patients
    hospital.serve_patient()
    hospital.serve_patient()
    hospital.serve_patient()

    # Show history
    hospital.show_history()
