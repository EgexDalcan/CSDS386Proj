import numpy as np
from qiskit.circuit import Parameter
from qiskit.transpiler import generate_preset_pass_manager
from qiskit import QuantumCircuit

def rxx_block(qc, q1, q2):
    qc.ry(np.pi/2, q1)
    qc.rxx(np.pi/2, q1, q2)

    qc.rx(-np.pi/2, q1)
    qc.ry(-np.pi/2, q1)

    qc.rx(-np.pi/2, q2)

qc = QuantumCircuit(4)

angle = Parameter("angle")

theta = np.zeros(4)

for i, t in enumerate(theta):
    qc.ry(t, i)

rxx_block(qc, 0, 1)
rxx_block(qc, 1, 2)
rxx_block(qc, 2, 3)
rxx_block(qc, 3, 0)

print(qc.draw("text"))
