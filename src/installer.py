from abc import ABC, abstractmethod

class Installer(ABC):
    @abstractmethod
    def install(self) -> bool:
        """Function will run the package its installation script

        Returns:
            bool: True if the installation was successful
        """