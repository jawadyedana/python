class Expression:
    def _init_(self, expression):
        """
        Initialize the Expression class with an arithmetic expression.

        Args:
            expression (str): A string representing the arithmetic expression.
        """
        self.expression = expression

    def evaluate(self):
        """
        Evaluate the arithmetic expression.

        Returns:
            float: The result of the evaluated expression.
        """
        try:
            # Using eval() function to evaluate the expression
            # Note: eval() can pose a security risk if used with untrusted input
            result = eval(self.expression)
            return result
        except Exception as e:
            # Handle any exceptions that occur during evaluation
            print(f"Error evaluating expression: {str(e)}")
            return None

    def print_result(self):
        """
        Print the result of the evaluated expression.
        """
        result = self.evaluate()
        if result is not None:
            print(f"The result of the expression '{self.expression}' is: {result}")

# Example usage
if __name__ == "_main_":
    # Create an instance of the Expression class
    expression = Expression("10 + 5 * 2")

    # Print the result of the expression
    expression.print_result()
