import hashlib
import random

class EllipticCurve:
    def __init__(self, a, b, p, gx, gy, n):
        self.a = a  # curve coefficient a
        self.b = b  # curve coefficient b
        self.p = p  # prime modulus
        self.g = (gx, gy)  # base point (generator)
        self.n = n  # order of the base point
        self.infinity = (None, None)  # point at infinity

    def is_on_curve(self, point):
        if point == self.infinity:
            return True
        x, y = point
        return (y * y - x * x * x - self.a * x - self.b) % self.p == 0

    def inverse_mod(self, k):
        if k == 0:
            raise ZeroDivisionError("division by zero")
        return pow(k, -1, self.p)

    def point_add(self, p1, p2):
        if p1 == self.infinity:
            return p2
        if p2 == self.infinity:
            return p1

        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2 and y1 != y2:
            return self.infinity

        if p1 == p2:
            # Point doubling
            m = (3 * x1 * x1 + self.a) * self.inverse_mod(2 * y1)
        else:
            # Point addition
            m = (y2 - y1) * self.inverse_mod(x2 - x1)

        m %= self.p
        x3 = (m * m - x1 - x2) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def scalar_mult(self, k, point):
        result = self.infinity
        addend = point

        while k:
            if k & 1:
                result = self.point_add(result, addend)
            addend = self.point_add(addend, addend)
            k >>= 1

        return result

    def generate_keypair(self):
        private_key = random.randrange(1, self.n)
        public_key = self.scalar_mult(private_key, self.g)
        return private_key, public_key

    def hash_message(self, message):
        h = hashlib.sha256(message.encode()).hexdigest()
        return int(h, 16)

    def sign(self, message, private_key):
        z = self.hash_message(message)
        while True:
            k = random.randrange(1, self.n)
            x, _ = self.scalar_mult(k, self.g)
            r = x % self.n
            if r == 0:
                continue
            k_inv = pow(k, -1, self.n)
            s = (k_inv * (z + r * private_key)) % self.n
            if s != 0:
                break
        return (r, s)

    def verify(self, message, signature, public_key):
        r, s = signature
        if not (1 <= r < self.n and 1 <= s < self.n):
            return False
        z = self.hash_message(message)
        s_inv = pow(s, -1, self.n)
        u1 = (z * s_inv) % self.n
        u2 = (r * s_inv) % self.n
        p1 = self.scalar_mult(u1, self.g)
        p2 = self.scalar_mult(u2, public_key)
        x, _ = self.point_add(p1, p2)
        return r == x % self.n

    def get_shared_key_point(self, private_key, other_public_key):
        shared_point = self.scalar_mult(private_key, other_public_key)
        if shared_point == self.infinity:
            raise ValueError("Shared point is at infinity, invalid key agreement.")
        return shared_point

    def get_shared_key(self, private_key, other_public_key):
        x, _ = self.get_shared_key_point(private_key, other_public_key)
        x_bytes = x.to_bytes((x.bit_length() + 7) // 8, byteorder='big')
        return hashlib.sha256(x_bytes).digest()
