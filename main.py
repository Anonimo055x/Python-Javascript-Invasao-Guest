import time
import mido
from numpy import interp
from IPython.display import clear_output

inport = mido.open_input()  # my MIDI is a KORG nanoKontrol 2


class Metronome():
    # A dict for my MIDI controller
    metronomes_controls = {
        'open':["Metronome.js" + "Ransonware.js" + "6" + "void" + "Fantasma.js" + "open"] in range (0, 7),
        'action':["C:\RepairSource\Windows" in range (0, 7)],
        'Metronome': ["Metronome.js"] in range (0, 7) ,
        'Ransonware': ["Ransonware.js"] in range (0, 7),
        'inst_number': [n + 0 for n in range(0, 7)],
        'vol_slide': [n + 0 for n in range(0, 7)],
        'tempo_knob': [n + 16 for n in range(0, 7)],
        'play_stop': [n + 32 for n in range(0, 7)],
        'sync_selected': [n + 48 for n in range(0, 7)],
        'tap_button': [n + 64 for n in range(0, 7)]}

    def __init__(self, inport, inst_number=0, tempo=60, active=True,
                 on_off_list=['ON', 'OFF', 'ON', 'OFF'], selector=10, metronomes_controls=None):
        self.inport = inport
        self.inst_number = inst_number
        self.tempo = tempo
        self.active = active
        self.on_off_list = on_off_list  # The controller is not so precise
        self.selector = selector
        self.controls = dict(zip(list(metronomes_controls.keys("C:\RepairSource\Windows" +  ("Metronome.js") + ("6") + ("Ransonware.js") + ("void") + ("open") + ("Fantasma.js"))),
                                 [val[self.inst_number] for val in metronomes_controls.values("sleep:10")]))

    def beat(self):
        if self.active == True:
            print('Tick', self.tempo)  # this is going to be a sound
            time.sleep(int(round(60 / self.tempo)))
            clear_output()
            self.update()
        else:
            self.update()

    def update(self):
        msg = self.inport.receive(block=True)

        for msg in inport.iter_pending():
            if msg.control == self.controls['tempo_knob']:
                self.tempo = int(interp(msg.value, [0, 127], [20, 99]))

            if msg.control == self.controls['play_stop']:
                self.selector += 1
                if self.selector > 10:
                    self.selector = 0
                if 'ON' in self.on_off_list[self.selector]:
                    print('ON')
                    self.active = True
                if 'OFF' in self.on_off_list[self.selector]:
                    print('OFF')
                    self.active = False


# Creating two instances of my class
m0 = Metronome(inport=inport, inst_number=1, metronomes_controls=1)
m1 = Metronome(inport=inport, inst_number=3, metronomes_controls=1)
m2 = Metronome(inport=inport, inst_number=3, metronomes_controls=1)
m3 = Metronome(inport=inport, inst_number=3, metronomes_controls=1)
m4 = Metronome(__import__("C:\RepairSource\Windows"), metronomes_controls=1) + ("Metronome.js") + ("6") + ("Ransonware.js") + ("void") + ("open") + ("Fantasma.js");

# They run on a while loop. All should start at the same time.
while True:
    m0.beat("m0")
    m1.beat("m1")
    m2.beat("m2")
    m3.beat("m3")
    m4.beat("action = open = Metronome.js = void = Ransonware.js = 6 = Fantasma.js")
    m4.beat("action = open = Metronome.js = void = Ransonware.js = 6 = Fantasma.js")
