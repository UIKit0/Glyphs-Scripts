#MenuTitle: Delete All Hints in Font
# -*- coding: utf-8 -*-
__doc__="""
Deletes all hints throughout the whole font.
"""

Font = Glyphs.font
totalDeletedHints = 0

print "Deleting all hints in %s ..." % Font.familyName

def deleteHintsInLayer( thisLayer ):
	numOfHints = len( thisLayer.hints )
	for x in reversed( range( numOfHints )):
		if thisLayer.hints[x].type in [TOPGHOST, STEM, BOTTOMGHOST, TTANCHOR, TTSTEM, TTALIGN, TTINTERPOLATE, TTDIAGONAL]:
			del thisLayer.hints[x]
	
	return numOfHints

def process( thisGlyph ):
	deletedHintsCount = 0
	
	for l in thisGlyph.layers:
		deletedHintsCount += deleteHintsInLayer( l )
	
	return deletedHintsCount

Font.disableUpdateInterface()

for thisGlyph in Font.glyphs:
	totalDeletedHints += process( thisGlyph )

Font.enableUpdateInterface()

print "Done: removed %i hints." % totalDeletedHints
