#!/usr/bin/python3
"""Module for Animal abstract class and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal."""
        pass

class Dog(Animal):
    """Dog subclass of Animal."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Cat subclass of Animal."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
