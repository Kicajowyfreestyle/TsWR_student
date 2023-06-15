from copy import copy
import numpy as np


class ESO:
    def __init__(self, A, B, W, L, state, Tp):
        self.A = A
        self.B = B
        self.W = W
        self.L = L
        self.state = np.pad(np.array(state), (0, A.shape[0] - len(state)))
        self.Tp = Tp
        self.states = []

    def set_B(self, B):
        self.B = B

    def update(self, q : float, u : float):
        self.states.append(copy(self.state))
        q_hat = self.state[0]
        factor = ((np.eye(3) + self.Tp *  self.A) @ self.state)
        factor_2 = self.Tp * self.B * u + self.Tp * self.L * (q - q_hat)
        factor_2 = factor_2.reshape((3,))

        self.state = factor + factor_2
        print(f'{factor=}')
        print(f'{factor_2=}')
        print(f'{self.state=}')

    def get_state(self):
        return self.state

    def get_q_dot_hat(self):
        return self.state[1]
    
    def get_q_hat(self):
        return self.state[0]
    
    def get_F_hat(self):
        return self.state[2]