import numpy as np
try:
    from pyaudio import PyAudio, paInt16
except ModuleNotFoundError:
    raise ModuleNotFoundError('Could not import module pyaudio, see readme for installation guide')


class MicEngine:

    def __init__(self):
        self.pyaudio_engine = PyAudio()
        self.stream = None
        self.sampling_rate = None
        self.frame_size = None

    def init_stream(self, sampling_rate=16000, frame_size=4000, callback_func=None):
        self.sampling_rate = sampling_rate
        self.frame_size = frame_size
        if self.stream is not None:
            self.stream.close()

        self.stream = self.pyaudio_engine.open(format=paInt16, channels=1, rate=self.sampling_rate,
                                               input=True, input_device_index=-1,
                                               frames_per_buffer=self.frame_size,
                                               stream_callback=callback_func)

    def get_audio_frame(self):
        if self.stream is not None:
            if self.stream.is_stopped:
                self.stream.start_stream()
            return np.frombuffer(self.stream.read(self.frame_size), dtype=np.int16).astype(float)
        else:
            raise Exception("stream does not exist run init_stream() first")

    def stop_stream(self):
        if self.stream is not None and self.stream.is_active():
            self.stream.stop_stream()

    def start_stream(self):
        if self.stream is not None and self.stream.is_stopped():
            self.stream.start_stream()
