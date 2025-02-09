# src/physics/physics.py
import pybullet as p

class PhysicsSystem:
    def __init__(self):
        self.physics_client = p.connect(p.DIRECT)  # Using DIRECT mode (no GUI)

    def simulate(self):
        p.stepSimulation()

    def add_rigid_body(self, shape, position):
        mass = 1
        body = p.createMultiBody(baseMass=mass, basePosition=position, baseCollisionShapeIndex=shape)
        return body
