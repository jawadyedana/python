class Robot:
    def _init_(self, name, purpose, capabilities):
        """
        Initialize the Robot object.

        Args:
            name (str): Name of the robot.
            purpose (str): Purpose of the robot.
            capabilities (list): List of capabilities of the robot.
        """
        self.name = name
        self.purpose = purpose
        self.capabilities = capabilities

    def introduce(self):
        """
        Introduce the robot.
        """
        print(f"Hello, I'm {self.name}!")
        print(f"My purpose is {self.purpose}.")
        print("I can do the following things:")
        for capability in self.capabilities:
            print(f"- {capability}")

# Create a robot object
my_robot = Robot(
    name="Zeta",
    purpose="Assist humans in daily tasks",
    capabilities=["Move objects", "Answer questions", "Perform calculations"]
)

# Introduce the robot
my_robot.introduce()