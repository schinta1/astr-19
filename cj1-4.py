import sys


class Animal:
    def print(self):
        print("The animal's info is below.")
        print(f"Length of arms         =  {self.arms}")
        print(f"Length of legs         =  {self.legs}")
        print(f"Number of eyes         =  {self.eyes}")
        print(f"Does it have a tail?   =  {self.tail}")
        print(f"Is it a furry?         =  {self.furry}")

    def __init__(self, arms=3.00, legs=4.234, eyes=2, tail=True, furry=True):
        self.arms = arms
        self.legs = legs
        self.eyes = eyes
        self.tail = tail
        self.furry = furry


def main():
    arms = 450.03
    legs = 100.230
    eyes = 2
    tail = True
    furry = True

    if len(sys.argv) >= 2:
        arms = float(sys.argv[1])
    if len(sys.argv) >= 3:
        legs = float(sys.argv[2])
    if len(sys.argv) >= 4:
        eyes = int(sys.argv[3])
    if len(sys.argv) >= 5:
        tail = bool(sys.argv[4])
    if len(sys.argv) >= 6:
        furry = bool(sys.argv[5])
    animal = Animal(arms=arms, legs=legs, eyes=eyes, tail=tail, furry=furry)
    animal.print()


if __name__ == "__main__":
    main()
