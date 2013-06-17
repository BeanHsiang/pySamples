from PyQt4.QtMultimedia import *
from PyQt4.QtCore import *
import wave

buf=None
audioInput=None
def start():
    fileName="demo.raw"
    global buf
    buf=QBuffer()
    buf.open(QIODevice.WriteOnly|QIODevice.Truncate)

    format=QAudioFormat()
    #format.setFrequency(16000)
    format.setSampleRate(16000)
    format.setSampleSize(16) 
    format.setChannels(1)
    format.setByteOrder(QAudioFormat.LittleEndian)
    format.setSampleType(QAudioFormat.SignedInt)

    format.setCodec("audio/pcm");
    info=QAudioDeviceInfo.defaultInputDevice()
    print info.deviceName
    if not info.isFormatSupported(format):
        print "change"
        #format=info.nearestFormat(format)
    
    global audioInput  
    audioInput=QAudioInput(format)    
    audioInput.start(buf)
    
def stop():
    global buf
    global audioInput
    buf.close()
    if not audioInput == None:
        audioInput.stop()    
        #del audioInput
    wavfile=wave.open('demo.wav', 'wb')
    wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
    wavfile.writeframes(buf.data ())
if __name__ == "__main__":
    for code in QAudioDeviceInfo.defaultInputDevice().supportedCodecs():
        print code
