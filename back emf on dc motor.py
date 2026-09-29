# back-emf-of-dc-motor
# Python program to calculate Back EMF of a DC Motor

V = float(input("Enter supply voltage (V): "))
Ia = float(input("Enter armature current (A): "))
Ra = float(input("Enter armature resistance (Ohm): "))

# Calculate Back EMF
Eb = V - (Ia * Ra)

print("\nBack EMF of DC Motor")
print("Supply Voltage =", V, "V")
print("Armature Current =", Ia, "A")
print("Armature Resistance =", Ra, "Ohm")
print("Back EMF =", round(Eb, 2), "V")

Example

Input:

Enter supply voltage (V): 220
Enter armature current (A): 10
Enter armature resistance (Ohm): 0.5


Output:

Back EMF of DC Motor
Supply Voltage = 220.0 V
Armature Current = 10.0 A
Armature Resistance = 0.5 Ohm
Back EMF = 215.0 V


Principle: When a DC motor rotates, an EMF is induced in the armature that opposes the applied supply voltage. This is called back EMF.
