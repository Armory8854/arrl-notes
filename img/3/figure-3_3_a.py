# Import required libs
import schemdraw
import schemdraw.elements as elm
import matplotlib
matplotlib.use('Agg')

with schemdraw.Drawing() as d:
    # Identify components
    d += (B := elm.Battery(label="Battery"))
    d += elm.Diode(label="Diode")
    d += elm.Diode()
    d += elm.Diode()

    # Create a line to close the loop
    d += elm.Line().down()

    # Use tox to determine how far the loop line is
    d += elm.Line().tox(B.start)

    # Close the loop
    d += elm.Source().up()
    
    # Save the diagram
    d.save(fname='/home/gary/Documents/notes/ARRL/img/3/figure-3_3_a.jpg')


