import Speech2Text

transcriptList = Speech2Text.transcribe_file('resources/audio.raw')

# print out the list we receive back.
for transcript in transcriptList:
    print transcript