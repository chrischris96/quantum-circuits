from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# instructions of the quantum system
# initializing with 2 qubits in the zero state; 
# with 2 classical bits set to zero;
circ = QuantumCircuit(3,3)

for idx in range(3):
   circ.h(idx)



circ.draw()

# Create a Quantum Circuit
meas = QuantumCircuit(3, 3)
# map the quantum measurement to the classical bits
meas.measure(range(3), range(3))

# The Qiskit circuit object supports composition using
# the addition operator.
qc = circ+meas

#drawing the circuit
qc.draw()

# calculation of all single-qubit gates on all the qubits happen simultaneously, the number of qubits in this circuit is equal to the width of the circuit
print(circ.width())
print(circ.depth())


backend = Aer.get_backend('statevector_simulator')
job = execute(circ, backend)
result = job.result()
outputstate = result.get_statevector(circ, decimals=3)

# Show the results
print(outputstate)

job_exp = execute(qc, backend=backend)
result_exp = job_exp.result()
counts_exp = result_exp.get_counts(circ)

plot_histogram(circ)
