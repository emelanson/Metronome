# import time
# import winsound

# def main(bpm = int(input('bpm: ')), bpb = int(input('bpb: ')), denom = int(input('beat value: '))  ):
# 	#bpm = setBPM()

# 	tick = bpm * (denom / 4)
# 	sleep = 60 / tick
# 	counter = bpb - 1
# 	while True:
# 		counter += 1
# 		if counter % bpb:
# 			winsound.PlaySound('low.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
# 			print('tick')
# 		else:
# 			winsound.PlaySound('hi.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
# 			print("TICK")
			
# 		time.sleep(sleep)


# main()	


import time
import winsound
#main needs beats per minute, beats per bar, and value of one beat
def main(bpm = int(input('bpm: ')), bpb = int(input('bpb: ')), denom = int(input('beat value: '))  ):
	
	#set rate/interval of metronome
	tick = bpm * (denom / 4)
	sleep = 60 / tick

	#use value of beat and number per measure to set number of pulses
	countstep = bpb * (denom / 4)

	#correct so metronome starts on accented beat
	counter = countstep - 1
	
	while True:
		counter += 1
		if counter % bpb:
			winsound.PlaySound('low.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
			print('tick')
		else:
			winsound.PlaySound('hi.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
			print("TICK")
			
		time.sleep(sleep)


main()	
