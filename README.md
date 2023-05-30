# My goals as of now are:
* image recognition for handwritten numbers [x]
* tic tac toe
* Math experiments

# Math experiments:
* then i think it would be cool to find simple math functions, inject uncertainty (of different sorts, in x, in y absolutely, or in y relatively, ie like +/- .1*y, vs x+/- 5, vs x +/- .1x)
* the reason this could be particularly cool, is that you could change how you train, such that you are improving as fast as possible given error in data
* for example, if there was 0 error in data, then every new piece of information can make big changes to the NN, and get insight quickly
* i'm also curious about random data vs perfectly distributed data
* I'm sure there is research on this, after I start experimenting I'll link stuff
* i'm really interested in how much slower learning happens with diffeernt levels of uncertiainty, and using a simple math function means infinite cheap "data" made anywhere i'm at/training it.
* basic train NN to match some basic funcitions, X, X^2, sinx, tanx(interesting!!)
* then some little improvements for all, ex bounding output range for sinx to [-1,1]
* then try random vs even distribution of data (not that this is super meaningful in practice, i'm just curious)
* then I'll work on adding different levels of error in the data, and see how things change (% error?)

# MNIST
* Still want to see total mistakes through each pass, and then total mistakes on first try with new data
* Show off every new image that was incorrectly identified

# tic tac toe