from direct.showbase.ShowBase import ShowBase
from panda3d_animalese import AnimaleseLibrary, AnimaleseSynth

# Create a new showbase instance
base = ShowBase()

library = AnimaleseLibrary('assets/low')
synth = AnimaleseSynth(library)

synth.play('Hello World!')
base.run()