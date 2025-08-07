import hashlib
import random

class EllipticCurve:
    def __init__(self, a, b, p, gx, gy, n):


    def is_on_curve(self, point):


    def inverse_mod(self, k):


    def point_add(self, p1, p2):


    def scalar_mult(self, k, point):


    def generate_keypair(self):

    def hash_message(self, message):


    def sign(self, message, private_key):


    def verify(self, message, signature, public_key):


    def get_shared_key_point(self, private_key, other_public_key):


    def get_shared_key(self, private_key, other_public_key):

