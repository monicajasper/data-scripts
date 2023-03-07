#Python cheatsheet - code snips geared toward common GIS labelling needs



#GIS labelling: py if statement
def FindLabel ([Nearby_Bores.BOPRC_Ref]):
  if ([Nearby_Bores.BOPRC_Ref]) in ("BN-4274","BN-2033"):
    return [Nearby_Bores.BOPRC_Ref] + " (Observation Bore)"
  else:
    return [Nearby_Bores.BOPRC_Ref]
    
    
#GIS labeling: last X char (ex below last 5 char)
!Name![len(!Name!) - 5:]