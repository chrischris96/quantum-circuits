from qiskit import QuantumCircuit, BasicAer, execute
from qiskit.visualization import plot_bloch_multivector

circ = QuantumCircuit(10,10)

for idx in range(10):
   circ.h(idx)


circ.draw()
# calculation of all single-qubit gates on all the qubits happen simultaneously, the number of qubits in this circuit is equal to the width of the circuit
print(circ.width())
print(circ.depth())


backend = BasicAer.get_backend('statevector_simulator')
job = execute(circ, backend).result()
plot_bloch_multivector(job.get_statevector(), title="New Bloch Multivector")
