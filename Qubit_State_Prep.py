import numpy as np
from itertools import product

class State_Preparation:
    """A class to create and display normalized quantum states."""

    def __init__(self, num_qubits, amplitudes):
        self.num_qubits = num_qubits
        self.amplitudes = np.array(amplitudes, dtype=complex)
        self.dim = 2 ** num_qubits
        self.psi = None

    def prepare(self):
        """Normalize and prepare the quantum state."""
        if self.amplitudes.size != self.dim:
            raise ValueError(f"For {self.num_qubits} qubits, you must provide {self.dim} amplitudes.")
        
        norm = np.linalg.norm(self.amplitudes)
        if norm == 0:
            raise ValueError("Amplitudes cannot all be zero.")
        
        self.psi = (self.amplitudes / norm).reshape((self.dim, 1))# Comment this out to make tests fail
        #self.psi = self.amplitudes.reshape((self.dim, 1)) # remove norm to break for normalization test
        #self.psi = (self.amplitudes / norm)  # remove reshape to break for dimensionality test
        return self.psi

    def dirac_notation(self):
        """Return the quantum state in Dirac (ket) notation."""
        if self.psi is None:
            raise RuntimeError("State not prepared yet. Call prepare() first.")
        
        basis_labels = [''.join(bits) for bits in product('01', repeat=self.num_qubits)]
        state_terms = []

        for amp, label in zip(self.psi.flatten(), basis_labels):
            if np.abs(amp) > 1e-10:
                amp_str = f"({amp.real:.3f}" + (f"{amp.imag:+.3f}j)" if abs(amp.imag) > 1e-10 else ")")
                state_terms.append(f"{amp_str}|{label}⟩")
        
        return " + ".join(state_terms)

    def show(self):
        """Print the full normalized state vector and Dirac form."""
        if self.psi is None:
            self.prepare()

        print(f"\nNormalized {self.num_qubits}-qubit state vector (column form):\n{self.psi}")
        print("\nState in Dirac notation:")
        print(f"|ψ⟩ = {self.dirac_notation()}")
        print("\nNormalization check:", np.sum(np.abs(self.psi)**2).real)


# ===============================
# This is the part that is used from the terminal
# ===============================
if __name__ == "__main__":
    num_qubits = int(input("Enter number of qubits: "))
    dim = 2 ** num_qubits
    print(f"Enter {dim} complex amplitudes (space-separated, e.g. 1+0j 0 1j 0):")
    amp_input = input().split()
    amplitudes = [complex(a) for a in amp_input]

    qs = State_Preparation(num_qubits, amplitudes)
    qs.prepare()
    qs.show()
