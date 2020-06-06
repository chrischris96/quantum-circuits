from qiskit import QuantumCircuit

circ = QuantumCircuit(15)

for idx in range(15):
   circ.h(idx)


circ.draw()
# calculation of all single-qubit gates on all the qubits happen simultaneously, the number of qubits in this circuit is equal to the width of the circuit
print(circ.width())
print(circ.depth())


