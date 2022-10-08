# Import required libs
import schemdraw
import schemdraw.elements as elm
import matplotlib
matplotlib.use('Agg')

with schemdraw.Drawing() as d:
    # make element leads shorter than normal
    d.config(unit=2)
    # Do the first push - so we can 'pop' back in later
    d.push()
    # Identify the battery
    d += (B := elm.Battery().label('Battery').down())
    # Draw a line to the right
    d += elm.Line().right(3).dot()
    # Pop back to the beginning of the push - the battery
    d.pop()
    # Draw a line to the right
    d += elm.Line().right(3).dot()
    # Draw the first diode - down - to close the first loop
    d += elm.Diode().label('Diode').down().dot()
    # Draw another line to the right
    d += elm.Line().right(3).dot()
    # Add another diode - Up, this time.
    # Reverse is added to make it face the same way as the other diode.
    d += elm.Diode().label('Diode').up().reverse().dot()
    # Create a new line left, introducing the hold() element
    # I assume this 'holds' the place, so the command after continues
    # The circuit in a logical fashion.
    d += elm.Line().left(3).hold()
    # Continue drawing the rest of the circuit
    d += elm.Line().right(3).dot()
    # Draw the last diode
    d += elm.Diode().label('Diode').down().dot()
    # close the circuit with a final left line
    d += elm.Line().left(3).dot()

    # Save the diagram
    d.save(fname='/home/gary/Documents/notes/ARRL/img/3/figure-3_3_b.jpg')
