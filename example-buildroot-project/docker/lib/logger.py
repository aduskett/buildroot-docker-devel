class Logger:
    @staticmethod
    def print_error(message: str):
        """Print an error"""
        print(f"######## ERROR: {message} ########")

    @staticmethod
    def print_step(step: str):
        """Print the step."""
        print(f"######## {step} ########")
