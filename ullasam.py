# Ullasam - Jython Version created by Gautham
from music import *

ullasam = Score("Ullasam", 140)

#defining the parts
initPart  = Part("Sax", SOPRANO_SAX, 0)
flutePart = Part("Flute", FLUTE, 1)
strPart   = Part("Violin", TREMOLO_STRINGS, 2)
vocalPart = Part("Vocal", ACCORDION, 3)
bassPart  = Part("Bass", BASS, 8)
drumsPart = Part("Drums", 0, 9)

#defining the phrases
saxPhrase    = Phrase(0.0)
bassPhrase   = Phrase(2.0)
flutePhrase  = Phrase(32.0)
stringPhrase = Phrase(64.0)
vocalPhrase  = Phrase(98.0)
bassDrumPhrase = Phrase(2.0)
hiHatPhrase1 = Phrase(2.0)
hiHatPhrase2 = Phrase(34.0)
hiHatPhrase3 = Phrase(66.0)
clapPhrase   = Phrase(98.0)
violinPhrase = Phrase(98.0)
endBeatPhrase= Phrase(114.0)
hHendPhrase1 = Phrase(130.0)
hHendPhrase2 = Phrase(130.0)
bassEndPhrase= Phrase(130.0)

#defining the SAX pitches
saxPitches0   = [D4, E4, D4, E4, E4, B3, B3, B3, D4, D4, D4, D4]
saxDurations0 = [EN, EN, EN, EN, QN, QN, QN, EN, EN, QN, EN, EN]
saxPitches1   = [D4, E4, D4, E4, E4, B3, B3, B3, D4, D4]
saxDurations1 = [EN, EN, EN, EN, QN, QN, QN, EN, EN, HN]
saxPitches2   = [E4, D4, B3, A3, A3, A3, FS3, FS3, FS3, E3, E3]
saxDurations2 = [EN, EN, EN, EN, QN, EN, EN, QN, EN, EN, DQN]
saxPitches3   = [CS4, B3, A3, FS3,FS3,A3, A3, B3, B3, A3, A3, FS3, REST]
saxDurations3 = [QN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, HN]

# defining the flute pitches
flutePitches0   = [D5, B4, D5, E5, FS5,E5, FS5, A5]
fluteDurations0 = [SN, SN, SN, SN, SN, SN, SN, SN ]
flutePitches1   = [B5, A5, B5, B5, B5, B5,CS6, B5, A5, FS5]
fluteDurations1 = [EN, EN, 3.5,QN, EN, EN, SN, SN, EN, EN ]
flutePitches2   = [A5, FS5, A5,  A5, A5, FS5,E5, FS5,E5, FS5,A5]
fluteDurations2 = [EN,  EN, 2.5, EN, EN, EN, 2, SN, SN, SN, SN]
flutePitches3   = [B5, A5, B5, D6, B5, B5, B5, D6, B5, A5, FS5,A5, FS5, A5, A5, A5, B5, B5, CS6,REST]
fluteDurations3 = [EN, EN, 3.5,EN, EN, EN, EN, SN, SN, EN, EN,  EN, EN,2.5, EN, EN, EN, EN, EN, HN]

# defining the violin (solo) pitches
violinPitches0   = [D5, E5, FS5,A5]
violinDurations0 = [EN, EN, EN, EN]
violinPitches1   = [B5, D6, B5, E6, CS6,A5,CS6, A5, FS5, G5, A5]
violinDurations1 = [HN, HN, HN, QN, QN, HN, HN, DQN, EN, EN,DQN]
violinPitches2   = [B5, D6, B5, E6, CS6,A5,CS6, CS6,D6, E6, D6, E6, D6, G6, A6]
violinDurations2 = [HN, HN, HN, QN, QN, HN, HN, EN, EN, EN, EN, EN, EN, EN, EN]

# defining the violin (with vocal) pitches
vioPitches0   = [REST]*14 + [G6, A6]
vioDurations0 = [EN] * 16

# defining the vocal pitches
vocalPitches0   = [D5, B4, D5, B4, D5, D5, B4, D5, D5, D5, E5]
vocalDurations0 = [EN, EN, EN, EN, QN, EN, EN, QN, EN, EN, HN]
vocalPitches1   = [D5, B4, D5, B4, D5, D5, D5, B4, D5, D5, D5, E5, D5, B4, A4]
vocalDurations1 = [EN, EN, EN, EN, EN, EN, EN, EN, QN, EN, EN, EN, EN, EN, EN]
vocalPitches2   = [D5, D5, B4, D5, D5, B4, D5, D5, D5,FS5, E5, D5, E5, REST]
vocalDurations2 = [QN, EN, EN, QN, EN, EN, EN, EN, EN, EN, SN, SN, EN, QN]
vocalPitches3   = [FS5,E5,FS5,FS5, E5, D5, D5, E5, E5,FS5, E5, D5,CS5]
vocalDurations3 = [EN, EN, QN, EN, EN, QN, EN, EN,DQN, SN, SN, EN, EN]
vocalPitches4   = [FS5,E5,FS5,FS5, E5, D5, D5, E5, E5]
vocalDurations4 = [EN, EN, QN, EN, EN, QN, EN, EN,DQN]

# defining the BASS pitches
bassPitches0   = [G1, G1, G1, G1, G1, G1, G1, E1, FS1, G1, A1, A1, A1, A1, A1, A1, A1, A1, A1, G1, FS1, E1]
bassDurations0 = [EN, QN, QN, QN, QN, QN, EN, EN, EN,  EN, EN] * 2

# defining the bass drum pitches
bassPitches   = [ABD,ABD,REST,ABD, ABD]
bassDurations = [ EN, EN, DHN, HN,  HN]
# defining the high hat drum pitches
hiHatPitches1   = [CHH] + [PHH] + [REST] * 13 + [OHH]
hiHatDurations1 = [EN] * 16 
hiHatPitches2   = [CHH] + [PHH] + [REST] * 2 + [CLP] + [REST]*3 + [PHH, REST, REST, REST, CLP, REST, PHH, OHH]
hiHatDurations2 = [EN] * 16
hiHatPitches3   = [CHH] + [REST] * 3 + [CLP] + [REST]*3 + [PHH, REST, REST, REST, CLP, REST, PHH, OHH]
hiHatDurations3 = [EN] * 16
hiHatPitches3   = [LMT] + [REST] * 3 + [HMT] + [REST]*3 + [PHH, REST, REST, REST, HMT, REST, PHH, OHH]
hiHatDurations3 = [EN] * 16
# defining the clap drum pitches
clapPitches     = [REST]*4 + [CLP] + [REST]*7 + [CLP, REST, PHH, OHH]
clapDurations   = [EN] * 16
# defining the end drum ptches
endDrumPitches  = [ABD,ABD,REST,ABD, ABD]*2
endDrumDurations= [ EN, EN, DHN, HN,  HN] * 2

#adding note list to the SAX phrase
saxPhrase.addNoteList(saxPitches0,saxDurations0)
saxPhrase.addNoteList(saxPitches1,saxDurations1)
saxPhrase.addNoteList(saxPitches2,saxDurations2)
saxPhrase.addNoteList(saxPitches3,saxDurations3)

#adding note list to the BASS phrase
bassPhrase.addNoteList(bassPitches0,bassDurations0)
bassPhrase.addNoteList(bassPitches0,bassDurations0)
bassPhrase.addNoteList(bassPitches0,bassDurations0)
bassPhrase.addNoteList(bassPitches0,bassDurations0)
bassPhrase.addNoteList(bassPitches0,bassDurations0)
bassPhrase.addNoteList(bassPitches0,bassDurations0)
#adding notes to the BASS end Phrase
bassEndPhrase.addNoteList(bassPitches0,bassDurations0)
bassEndPhrase.addNoteList(bassPitches0,bassDurations0)

#adding note list to the DRUMS phrase
bassDrumPhrase.addNoteList(bassPitches, bassDurations)
Mod.repeat(bassDrumPhrase, 12)
hiHatPhrase1.addNoteList(hiHatPitches1, hiHatDurations1)
Mod.repeat(hiHatPhrase1, 4)
hiHatPhrase2.addNoteList(hiHatPitches2, hiHatDurations2)
Mod.repeat(hiHatPhrase2, 4)
hiHatPhrase3.addNoteList(hiHatPitches3, hiHatDurations3)
Mod.repeat(hiHatPhrase3, 4)
clapPhrase.addNoteList(clapPitches, clapDurations)
Mod.repeat(clapPhrase, 6)
endBeatPhrase.addNoteList(endDrumPitches, endDrumDurations)
Mod.repeat(endBeatPhrase, 2)
hHendPhrase1.addNoteList(hiHatPitches1, hiHatDurations1)
Mod.repeat(hHendPhrase1, 4)
hHendPhrase2.addNoteList(hiHatPitches3, hiHatDurations3)
Mod.repeat(hHendPhrase2, 4)

#adding note list to the FLUTE phrase
flutePhrase.addNoteList(flutePitches0,fluteDurations0)
flutePhrase.addNoteList(flutePitches1,fluteDurations1)
flutePhrase.addNoteList(flutePitches2,fluteDurations2)
flutePhrase.addNoteList(flutePitches3,fluteDurations3)

#adding note list to the STRING phrase
stringPhrase.addNoteList(violinPitches0,violinDurations0)
stringPhrase.addNoteList(violinPitches1,violinDurations1)
stringPhrase.addNoteList(violinPitches2,violinDurations2)

#adding note list to the VIOLIN phrase
violinPhrase.addNoteList(vioPitches0, vioDurations0)
Mod.repeat(violinPhrase, 2)

#adding note list to the VOCAL phrase
vocalPhrase.addNoteList(vocalPitches0, vocalDurations0)
vocalPhrase.addNoteList(vocalPitches1, vocalDurations1)
vocalPhrase.addNoteList(vocalPitches2, vocalDurations2)
vocalPhrase.addNoteList(vocalPitches3, vocalDurations3)
vocalPhrase.addNoteList(vocalPitches0, vocalDurations0)
vocalPhrase.addNoteList(vocalPitches1, vocalDurations1)
vocalPhrase.addNoteList(vocalPitches2, vocalDurations2)
vocalPhrase.addNoteList(vocalPitches4, vocalDurations4)

initPart.addPhrase(saxPhrase)
bassPart.addPhrase(bassPhrase)
bassPart.addPhrase(bassEndPhrase)
flutePart.addPhrase(flutePhrase)
strPart.addPhrase(stringPhrase)
vocalPart.addPhrase(vocalPhrase)
drumsPart.addPhrase(bassDrumPhrase)
drumsPart.addPhrase(hiHatPhrase1)
drumsPart.addPhrase(hiHatPhrase2)
drumsPart.addPhrase(hiHatPhrase3)
drumsPart.addPhrase(clapPhrase)
drumsPart.addPhrase(endBeatPhrase)
drumsPart.addPhrase(hHendPhrase1)
drumsPart.addPhrase(hHendPhrase2)
strPart.addPhrase(violinPhrase)

ullasam.addPart(initPart)
ullasam.addPart(bassPart)
ullasam.addPart(flutePart)
ullasam.addPart(strPart)
ullasam.addPart(vocalPart)
ullasam.addPart(drumsPart)

View.sketch(ullasam)
Play.midi(ullasam)
Write.midi(ullasam, "ullasam.mid")