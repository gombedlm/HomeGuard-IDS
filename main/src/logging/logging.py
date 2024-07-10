class Logger:
    def __init__(self):
        # Initialize any setup if needed
        pass
    
    def info(self, message):
        self._log("INFO", message)
    
    def warning(self, message):
        self._log("WARNING", message)
    
    def error(self, message):
        self._log("ERROR", message)
    
    def _log(self, level, message):
        print(f"[{level}] {message}")

# Example usage
if __name__ == "__main__":
    logger = Logger()
    logger.info("This is an information message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
