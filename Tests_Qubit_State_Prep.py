import unittest
import numpy as np
from Qubit_State_Prep import State_Preparation 

class TestQuantumStatePreparation(unittest.TestCase):
    
    def test_normalization_enforced(self):
        """Check that the output state is normalized."""
        amps = [1, 1, 1, 1]
        qs = State_Preparation(2, amps)
        psi = qs.prepare()
        self.assertAlmostEqual(np.sum(np.abs(psi)**2), 1, places=10)
    
    def test_correct_dimension(self):
        """Check that the state vector has correct dimension (2^num_qubits, 1)."""
        amps = [1, 0, 0, 0]
        qs = State_Preparation(2, amps)
        psi = qs.prepare()
        self.assertEqual(psi.shape, (4, 1))
    
    def test_invalid_number_of_amplitudes(self):
        """Check that wrong number of amplitudes raises ValueError."""
        with self.assertRaises(ValueError):
            qs = State_Preparation(2, [1, 0, 0])
            qs.prepare()
    
    def test_zero_amplitudes(self):
        """Check that all-zero amplitudes raise ValueError."""
        with self.assertRaises(ValueError):
            qs = State_Preparation(2, [0, 0, 0, 0])
            qs.prepare()

if __name__ == "__main__":
    unittest.main()
